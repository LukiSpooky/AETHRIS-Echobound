// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "AethrisSaveTypes.generated.h"

/**
 * Kopf eines Weltstand-Saves (K06 §7, Details K64).
 * Datei = Header + N Fragmente; jedes Fragment ist unabhängig versioniert.
 */
USTRUCT()
struct AETHRISCORE_API FAethrisSaveHeader
{
	GENERATED_BODY()

	/** Magic 'AETH' zur Erkennung. */
	static constexpr uint32 Magic = 0x48544541;

	UPROPERTY() uint32 FileMagic = Magic;
	/** Version des Container-Formats (nicht der Inhalte). v2 (K64): CRC32 je Fragment + Nutzlast-CRC. */
	UPROPERTY() int32 ContainerVersion = 2;
	/** Build, der den Save geschrieben hat (Diagnose). */
	UPROPERTY() FString BuildVersion;
	UPROPERTY() FDateTime SavedAtUtc;
	UPROPERTY() int64 PlayTimeSeconds = 0;
	/** Für die Slot-Vorschau: Region, Wärterrang, Akkorde, Chor-Spezies. */
	UPROPERTY() FName RegionId;
	UPROPERTY() int32 WardenRank = 1;
	UPROPERTY() int32 AkkordCount = 0;
	UPROPERTY() TArray<FName> ChorPreviewSpecies;
	/** CRC32 über alle Fragmentdaten (Korruptionserkennung). */
	UPROPERTY() uint32 PayloadCrc = 0;
};

UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class USaveFragmentProvider : public UInterface
{
	GENERATED_BODY()
};

/**
 * Jedes System, das Zustand speichert, implementiert diesen Vertrag und registriert sich beim
 * Save-System (GF_Save). So kennt GF_Save keine Features – Features kennen nur dieses Interface.
 */
class AETHRISCORE_API ISaveFragmentProvider
{
	GENERATED_BODY()
public:
	/** Stabile Fragment-ID, z. B. "Chor", "Sanctuary", "Quests", "World.Zones". Nie umbenennen. */
	virtual FName GetSaveFragmentId() const = 0;

	/** Aktuelle Schema-Version dieses Fragments. Bei jeder Formatänderung erhöhen ([SAVE-SCHEMA]). */
	virtual int32 GetSaveFragmentVersion() const = 0;

	/** Schreibt den Zustand. Muss deterministisch sein (gleicher Zustand → gleiche Bytes). */
	virtual void WriteSaveFragment(FArchive& Ar) const = 0;

	/**
	 * Liest den Zustand. FromVersion < aktuelle Version → Migration in derselben Funktion
	 * (Kette v1→v2→…), siehe K64. Rückgabe false = Fragment unlesbar → Fallback auf Default + Meldung.
	 */
	virtual bool ReadSaveFragment(FArchive& Ar, int32 FromVersion) = 0;

	/** Auf Standardzustand zurücksetzen (neuer Weltstand oder Fallback). */
	virtual void ResetSaveFragment() = 0;
};
