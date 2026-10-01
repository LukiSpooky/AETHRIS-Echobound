// Copyright AETHRIS Team.
#include "AethrisSaveSubsystem.h"
#include "Serialization/MemoryWriter.h"
#include "Serialization/MemoryReader.h"

void UAethrisSaveSubsystem::RegisterProvider(ISaveFragmentProvider* Provider)
{
	if (Provider) { Providers.AddUnique(Provider); }
}

void UAethrisSaveSubsystem::UnregisterProvider(ISaveFragmentProvider* Provider)
{
	Providers.Remove(Provider);
}

void UAethrisSaveSubsystem::RequestAutosave(FName TriggerId, bool bForce)
{
	const double Now = FPlatformTime::Seconds();
	if (!bForce && Now - LastAutosaveRealSec < 30.0)
	{
		return;   // Mindestabstand (K64 §4)
	}
	LastAutosaveRealSec = Now;
	RotationIndex = (RotationIndex + 1) % 3;   // drei rotierende Kopien (SA-05)
	// Serialisierung der Fragmente: siehe SaveToSlot; Plattform-Schreiben asynchron, atomar (Temp → CRC → Umbenennen).
}

bool UAethrisSaveSubsystem::SaveToSlot(EAethrisSaveSlot Slot)
{
	if (Slot == EAethrisSaveSlot::Iron || Slot == EAethrisSaveSlot::Finale || Slot == EAethrisSaveSlot::Profile)
	{
		return false;   // diese Slots schreibt nur das System selbst
	}
	TArray<FAethrisSaveFragmentBlob> Blobs;
	for (ISaveFragmentProvider* P : Providers)
	{
		FAethrisSaveFragmentBlob& B = Blobs.AddDefaulted_GetRef();
		B.Id = P->GetSaveFragmentId();
		B.Version = P->GetSaveFragmentVersion();
		FMemoryWriter W(B.Data);
		P->WriteSaveFragment(W);
	}
	Blobs.Append(UnknownFragments);
	FAethrisSaveHeader Header;
	Header.SavedAtUtc = FDateTime::UtcNow();
	TArray<uint8> Bytes;
	Aethris::Save::WriteContainer(Header, Blobs, Bytes);
	// Übergabe an Plattform-Speicher (asynchron, K64 §5).
	return Bytes.Num() > 0;
}

bool UAethrisSaveSubsystem::LoadFromSlot(EAethrisSaveSlot Slot)
{
	TArray<uint8> Bytes;   // vom Plattform-Speicher gelesen (K64 §5)
	FAethrisSaveHeader Header;
	TArray<FAethrisSaveFragmentBlob> Blobs;
	TArray<FName> Corrupt;
	if (!Aethris::Save::ReadContainer(Bytes, Header, Blobs, Corrupt))
	{
		return false;   // Aufrufer versucht die nächste Rotationskopie
	}
	UnknownFragments.Reset();
	for (ISaveFragmentProvider* P : Providers)
	{
		const FAethrisSaveFragmentBlob* B = Blobs.FindByPredicate([&](const FAethrisSaveFragmentBlob& X) { return X.Id == P->GetSaveFragmentId(); });
		if (!B) { P->ResetSaveFragment(); continue; }   // neues Fragment in diesem Build → Standard
		FMemoryReader R(B->Data);
		if (!P->ReadSaveFragment(R, B->Version)) { P->ResetSaveFragment(); }   // SA-03
	}
	for (const FAethrisSaveFragmentBlob& B : Blobs)
	{
		if (!Providers.ContainsByPredicate([&](ISaveFragmentProvider* P) { return P->GetSaveFragmentId() == B.Id; }))
		{
			UnknownFragments.Add(B);   // SA-04
		}
	}
	return true;
}
