// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "GameplayTagContainer.h"
#include "Math/AethrisRandom.h"
#include "EchoTypes.generated.h"

/** Seltenheitsstufen (K06 §6). Bestimmen Spawn-Gewichte (K52) und Validator-Pflichten (DR-15). */
UENUM(BlueprintType)
enum class EEchoRarity : uint8
{
	Common,
	Uncommon,
	Rare,
	VeryRare,
	Legendary,   // Ursprungsstimmen
	Mythical
};

/** Die acht Statuswerte (CANON §5). Ganzzahlen – Determinismus-Zone (CS-14). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoStats
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 HP = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 Attack = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 Defense = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 SpAttack = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 SpDefense = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 Speed = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 Precision = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) int32 Evasion = 0;

	/** Summe der sechs Kernwerte (ohne PRÄ/AUS) – Kennzahl für Balancing (K18). */
	int32 CoreTotal() const { return HP + Attack + Defense + SpAttack + SpDefense + Speed; }
};

/** Basiswerte einer Art (statisch, in UEchoSpeciesDefinition). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoBaseStats : public FEchoStats
{
	GENERATED_BODY()
};

/** Ein Allelpaar eines Genlocus (K38). Allele sind kleine Ganzzahlen; Bedeutung pro Locus in Daten. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoAllelePair
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) FName Locus;   // z. B. GEN_COLOR_BASE
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) uint8 A = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) uint8 B = 0;
};

/** Genom einer Echo-Instanz (Struktur hier, Regeln in K38). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoGenome
{
	GENERATED_BODY()

	/** Genetische Wertpotenziale („Anlagen“) je Statuswert (Skala → K18). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) FEchoStats Aptitudes;

	/** Optische/merkmalbezogene Loci. */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) TArray<FEchoAllelePair> Loci;

	/** Ausgeprägter Morph (None = Standard). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) FName Morph;

	/** Mutationen (Tags, z. B. Mutation.HiddenPassive). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, SaveGame) FGameplayTagContainer Mutations;
};

/** Herkunftssignatur (DR-16) – fälschungssicher signiert für Online-Nutzung (K59). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoOrigin
{
	GENERATED_BODY()
	UPROPERTY(SaveGame) FGuid OriginalWardenId;
	UPROPERTY(SaveGame) FString OriginalWardenName;
	UPROPERTY(SaveGame) FName ZoneId;           // R##_Z##
	UPROPERTY(SaveGame) FGameplayTag Weather;   // Weather.*
	UPROPERTY(SaveGame) FGameplayTag TimeOfDay; // TimeOfDay.*
	UPROPERTY(SaveGame) int64 GameDay = 0;      // Spieltag seit Spielbeginn
	UPROPERTY(SaveGame) FDateTime RealTimeUtc;
	UPROPERTY(SaveGame) uint8 Method = 0;       // 0 Bindung, 1 Zucht, 2 Geschenk, 3 Event
	UPROPERTY(SaveGame) FGuid ParentA;          // Zucht
	UPROPERTY(SaveGame) FGuid ParentB;
	UPROPERTY(SaveGame) TArray<uint8> Signature; // Server-Signatur (leer = offline, K59)
};

/**
 * Laufzeit- und Save-Instanz eines konkreten Echos (CANON §9).
 * Reine Daten – Logik liegt in Domain-/Feature-Systemen.
 */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoInstance
{
	GENERATED_BODY()

	UPROPERTY(SaveGame, BlueprintReadOnly) FGuid InstanceId;
	UPROPERTY(SaveGame, BlueprintReadOnly) FPrimaryAssetId Species;          // EchoSpecies:ECHO_###
	UPROPERTY(SaveGame, BlueprintReadOnly) FText Nickname;
	UPROPERTY(SaveGame, BlueprintReadOnly) int32 Level = 1;                  // 1..100
	UPROPERTY(SaveGame, BlueprintReadOnly) int64 Experience = 0;
	UPROPERTY(SaveGame, BlueprintReadOnly) int32 Bond = 0;                   // 0..1000
	UPROPERTY(SaveGame, BlueprintReadOnly) FGameplayTag Personality;         // Personality.*
	UPROPERTY(SaveGame, BlueprintReadOnly) FGameplayTag Temperament;         // Temperament.*
	UPROPERTY(SaveGame, BlueprintReadOnly) FEchoGenome Genome;
	UPROPERTY(SaveGame, BlueprintReadOnly) FEchoStats Polish;                // Schliff (K18 §8): 0–80 je Kernwert, Σ ≤ 240
	UPROPERTY(SaveGame, BlueprintReadOnly) FGameplayTagContainer PolishLocks; // gesperrte Werte (Stat.*), K18 §8
	UPROPERTY(SaveGame, BlueprintReadOnly) int32 CurrentHP = 0;
	UPROPERTY(SaveGame, BlueprintReadOnly) FGameplayTagContainer PersistentStatus;
	UPROPERTY(SaveGame, BlueprintReadOnly) TArray<FPrimaryAssetId> Repertoire;   // alle gelernten Aktiven
	UPROPERTY(SaveGame, BlueprintReadOnly) TArray<FPrimaryAssetId> ActiveSlots;  // max. 4
	UPROPERTY(SaveGame, BlueprintReadOnly) FPrimaryAssetId PassiveAbility;
	UPROPERTY(SaveGame, BlueprintReadOnly) FPrimaryAssetId HeldItem;
	UPROPERTY(SaveGame, BlueprintReadOnly) FEchoOrigin Origin;

	bool IsValid() const { return InstanceId.IsValid() && Species.IsValid(); }
};
