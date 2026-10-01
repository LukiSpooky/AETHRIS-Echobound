// Copyright AETHRIS Team.
#include "AethrisSaveContainer.h"
#include "Misc/Crc.h"

namespace Aethris::Save
{
	namespace
	{
		void PutU16(TArray<uint8>& O, uint16 V) { O.Add(V & 0xFF); O.Add(V >> 8); }
		void PutU32(TArray<uint8>& O, uint32 V) { for (int32 i = 0; i < 4; ++i) { O.Add((V >> (8 * i)) & 0xFF); } }
		void PutI32(TArray<uint8>& O, int32 V) { PutU32(O, static_cast<uint32>(V)); }
		void PutI64(TArray<uint8>& O, int64 V) { for (int32 i = 0; i < 8; ++i) { O.Add((uint64(V) >> (8 * i)) & 0xFF); } }
		void PutStr(TArray<uint8>& O, const FString& S)
		{
			const FTCHARToUTF8 U(*S);
			PutU16(O, static_cast<uint16>(U.Length()));
			O.Append(reinterpret_cast<const uint8*>(U.Get()), U.Length());
		}

		struct FReader
		{
			const TArray<uint8>& B; int32 Pos = 0; bool bOk = true;
			bool Need(int32 N) { bOk = bOk && Pos + N <= B.Num(); return bOk; }
			uint16 U16() { if (!Need(2)) return 0; const uint16 V = B[Pos] | (B[Pos + 1] << 8); Pos += 2; return V; }
			uint32 U32() { if (!Need(4)) return 0; uint32 V = 0; for (int32 i = 0; i < 4; ++i) V |= uint32(B[Pos + i]) << (8 * i); Pos += 4; return V; }
			int64 I64() { if (!Need(8)) return 0; uint64 V = 0; for (int32 i = 0; i < 8; ++i) V |= uint64(B[Pos + i]) << (8 * i); Pos += 8; return int64(V); }
			FString Str()
			{
				const uint16 L = U16();
				if (!Need(L)) return FString();
				const FUTF8ToTCHAR Conv(reinterpret_cast<const ANSICHAR*>(B.GetData() + Pos), L);
				Pos += L;
				return FString(Conv.Length(), Conv.Get());
			}
		};

		uint32 Crc(const uint8* Data, int32 Num) { return FCrc::MemCrc32(Data, Num); }   // zlib-kompatibles CRC-32
	}

	void WriteContainer(const FAethrisSaveHeader& Header, const TArray<FAethrisSaveFragmentBlob>& Fragments, TArray<uint8>& Out)
	{
		TArray<uint8> H;
		PutStr(H, Header.BuildVersion);
		PutI64(H, Header.SavedAtUtc.ToUnixTimestamp());
		PutI64(H, Header.PlayTimeSeconds);
		PutStr(H, Header.RegionId.ToString());
		PutI32(H, Header.WardenRank);
		PutI32(H, Header.AkkordCount);
		H.Add(static_cast<uint8>(FMath::Min(Header.ChorPreviewSpecies.Num(), 6)));
		for (int32 i = 0; i < FMath::Min(Header.ChorPreviewSpecies.Num(), 6); ++i) { PutStr(H, Header.ChorPreviewSpecies[i].ToString()); }

		Out.Reset();
		PutU32(Out, FAethrisSaveHeader::Magic);
		PutU32(Out, 2);
		PutU32(Out, H.Num());
		Out.Append(H);
		PutU32(Out, Fragments.Num());
		uint32 Offset = 0;
		for (const FAethrisSaveFragmentBlob& F : Fragments)
		{
			PutStr(Out, F.Id.ToString());
			PutU32(Out, uint32(F.Version));
			PutU32(Out, Offset);
			PutU32(Out, uint32(F.Data.Num()));
			PutU32(Out, Crc(F.Data.GetData(), F.Data.Num()));
			Offset += F.Data.Num();
		}
		const int32 PayloadStart = Out.Num();
		for (const FAethrisSaveFragmentBlob& F : Fragments) { Out.Append(F.Data); }
		PutU32(Out, Crc(Out.GetData() + PayloadStart, Out.Num() - PayloadStart));
	}

	bool ReadContainer(const TArray<uint8>& In, FAethrisSaveHeader& OutHeader, TArray<FAethrisSaveFragmentBlob>& OutFragments, TArray<FName>& OutCorrupt)
	{
		FReader R{In};
		if (R.U32() != FAethrisSaveHeader::Magic) { return false; }
		OutHeader.ContainerVersion = int32(R.U32());
		const uint32 HeaderSize = R.U32();
		const int32 HeaderEnd = R.Pos + int32(HeaderSize);
		OutHeader.BuildVersion = R.Str();
		OutHeader.SavedAtUtc = FDateTime::FromUnixTimestamp(R.I64());
		OutHeader.PlayTimeSeconds = R.I64();
		OutHeader.RegionId = FName(*R.Str());
		OutHeader.WardenRank = int32(R.U32());
		OutHeader.AkkordCount = int32(R.U32());
		if (!R.Need(1)) { return false; }
		const int32 Chor = In[R.Pos++];
		OutHeader.ChorPreviewSpecies.Reset();
		for (int32 i = 0; i < Chor; ++i) { OutHeader.ChorPreviewSpecies.Add(FName(*R.Str())); }
		R.Pos = HeaderEnd;   // künftige Header-Felder überspringen (Vorwärtskompatibilität)

		const uint32 Count = R.U32();
		struct FEntry { FName Id; uint32 Version, Offset, Size, Crc; };
		TArray<FEntry> Entries;
		for (uint32 i = 0; i < Count && R.bOk; ++i)
		{
			FEntry E;
			E.Id = FName(*R.Str());
			E.Version = R.U32(); E.Offset = R.U32(); E.Size = R.U32(); E.Crc = R.U32();
			Entries.Add(E);
		}
		if (!R.bOk || In.Num() < R.Pos + 4) { return false; }
		const int32 PayloadStart = R.Pos;
		const int32 PayloadSize = In.Num() - 4 - PayloadStart;
		OutFragments.Reset();
		OutCorrupt.Reset();
		for (const FEntry& E : Entries)
		{
			if (int64(E.Offset) + E.Size > PayloadSize) { OutCorrupt.Add(E.Id); continue; }
			const uint8* Data = In.GetData() + PayloadStart + E.Offset;
			if (Crc(Data, int32(E.Size)) != E.Crc) { OutCorrupt.Add(E.Id); continue; }
			FAethrisSaveFragmentBlob& B = OutFragments.AddDefaulted_GetRef();
			B.Id = E.Id;
			B.Version = int32(E.Version);
			B.Data.Append(Data, int32(E.Size));
		}
		return true;
	}
}
