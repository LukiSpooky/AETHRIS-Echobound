// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "GameplayTagContainer.h"
#include "AbilityDefinition.generated.h"

/** Fähigkeitsart (K28 §2, CANON §97). ID-Präfix: ABL_A / ABL_P / ABL_U / ABL_F. */
UENUM(BlueprintType)
enum class EAbilityKind : uint8
{
	Active,     ///< Kampfset-Slot 1–4, Repertoire
	Passive,    ///< Kampfset-Slot 5 (eine aktiv), Auslöser-basiert
	Crescendo,  ///< Kampfset-Slot 6, verbraucht Harmonie (K30/K33)
	Field       ///< Feldfähigkeit außerhalb des Kampfes (K30/K40)
};

UENUM(BlueprintType)
enum class EAbilityCategory : uint8 { Physical, Special, Status };

UENUM(BlueprintType)
enum class EAbilityTarget : uint8 { Single, Row, Enemies, Self, Ally, AllyRow, Allies, Field, AnySingle };

/** Ein Effekt der Effekt-DSL, z. B. Status(Brand,300). Der Import (AethrisEditor) zerlegt die CSV-Zeichenkette;
 *  zur Laufzeit wird nur noch über Op (FName → Effekt-Primitiv im GF_Combat-Registry) dispatcht (DR-25). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FAbilityEffectSpec
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadOnly) FName Op;
	UPROPERTY(EditAnywhere, BlueprintReadOnly) TArray<FName> Args;
};

/** Basis-Definition „Ability“ (ADR-031). Quelle: Data/Abilities/Abilities.csv (Import-Pipeline K06 §3). */
UCLASS(BlueprintType)
class AETHRISCORE_API UAbilityDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("Ability")); }

	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") EAbilityKind Kind = EAbilityKind::Active;
	/** Klangfarbe, z. B. Type.Ember. Pflicht – es gibt keine typlosen Fähigkeiten (CANON §77). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") FGameplayTag Type;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") EAbilityCategory Category = EAbilityCategory::Status;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") int32 Power = 0;
	/** Genauigkeit in Promille; 0 = kein Trefferwurf (Selbst/Feld). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") int32 AccuracyPermille = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") EAbilityTarget Target = EAbilityTarget::Single;
	/** Zeitkosten (100 = Standardzug); aus dem Machtbudget berechnet, nie handgesetzt (K28 §3). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") int32 TimeCost = 100;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") int32 Budget = 0;
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") TArray<FAbilityEffectSpec> Effects;
	/** Nur Passive: Auslöser-Tag, z. B. Trigger.OnHitTaken (K29 §2). */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") FGameplayTag Trigger;
	/** Ability.Tag.Contact, Ability.Tag.Sound, Ability.Tag.Ground, Field.* … */
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Ability") FGameplayTagContainer Tags;
};

namespace Aethris::Abilities
{
	/** Zeitkosten aus Machtpunkten: clamp(round10(20 + V), 50, 200) – identisch zu tools/abilities/abl.py. */
	constexpr int32 TimeCostFromBudget(int32 Budget)
	{
		const int32 Raw = (20 + Budget + 5) / 10 * 10;
		return Raw < 50 ? 50 : (Raw > 200 ? 200 : Raw);
	}

	/** Schadensanteil des Budgets: Stärke × Genauigkeit × Zielfaktor × mittlere Treffer (alles Promille). */
	constexpr int32 DamageBudget(int32 Power, int32 AccuracyPermille, int32 TargetFactorPermille, int32 HitsPermille)
	{
		return Power * (AccuracyPermille ? AccuracyPermille : 1000) / 1000 * TargetFactorPermille / 1000 * HitsPermille / 1000;
	}

	static_assert(TimeCostFromBudget(44) == 60, "Funkenbiss");
	static_assert(TimeCostFromBudget(114) == 130, "Esseneruption");
	static_assert(DamageBudget(100, 850, 1700, 1000) == 144, "Flächenschaden");
	static_assert(TimeCostFromBudget(400) == 200, "Deckel");
}
