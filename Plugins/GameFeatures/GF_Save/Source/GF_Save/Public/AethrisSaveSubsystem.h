// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "AethrisSaveContainer.h"
#include "AethrisSaveSubsystem.generated.h"

class ISaveFragmentProvider;

/** Speicherplätze (K64 §4). */
UENUM(BlueprintType)
enum class EAethrisSaveSlot : uint8
{
	World1, World2, World3,   ///< drei Weltstände (CANON §17), je 3 rotierende Autosave-Kopien
	Iron,                     ///< Eiserner Wärter: genau ein Stand, keine manuelle Kopie
	Finale,                   ///< Finale-Speicherpunkt (ADR-176), schreibgeschützt nach Erstellung
	Profile                   ///< Profil (Einstellungen, Erfolge, PvP, Album)
};

/**
 * Save-System (GF_Save, K64). Kennt keine Features: Systeme registrieren sich als ISaveFragmentProvider (SA-01).
 * Schreiben: Fragmente im Game Thread serialisieren (Budget ≤ 4 ms), Container + Kompression + Plattform-Schreiben asynchron.
 */
UCLASS()
class GF_SAVE_API UAethrisSaveSubsystem : public UGameInstanceSubsystem
{
	GENERATED_BODY()
public:
	void RegisterProvider(ISaveFragmentProvider* Provider);
	void UnregisterProvider(ISaveFragmentProvider* Provider);

	/** Autosave-Anfrage (AutosaveTriggers.csv). Mindestabstand 30 s außer bForce (Finale, Ruhemodus, Beenden). */
	void RequestAutosave(FName TriggerId, bool bForce = false);

	/** Manuelles Speichern in einen Weltstand-Slot (nicht im Kampf, nicht in Zwischensequenzen, nicht Iron). */
	bool SaveToSlot(EAethrisSaveSlot Slot);

	/** Lädt einen Slot; bei defektem Container die jüngste gültige Rotationskopie. Defekte Fragmente → Reset + Hinweis. */
	bool LoadFromSlot(EAethrisSaveSlot Slot);

	/** Fragmente, die ein älterer Build nicht kennt, bleiben erhalten und werden unverändert zurückgeschrieben (SA-04). */
	const TArray<FAethrisSaveFragmentBlob>& GetUnknownFragments() const { return UnknownFragments; }

private:
	TArray<ISaveFragmentProvider*> Providers;
	TArray<FAethrisSaveFragmentBlob> UnknownFragments;
	double LastAutosaveRealSec = -1000.0;
	int32 RotationIndex = 0;
};
