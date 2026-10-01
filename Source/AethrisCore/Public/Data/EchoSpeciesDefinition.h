// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "Echo/EchoTypes.h"
#include "EchoSpeciesDefinition.generated.h"

/** Bedingung für Spawn/Evolution – Detail-Fragmente in K19/K52. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FEchoCondition
{
	GENERATED_BODY()
	UPROPERTY(EditDefaultsOnly) FGameplayTagQuery Requirement; // z. B. Weather.Rain UND TimeOfDay.Night
};

/** Statische Spezies-Definition (CANON §9; Pflichtfelder gemäß K02 §13.1). Felder werden in K16 vervollständigt. */
UCLASS(BlueprintType)
class AETHRISCORE_API UEchoSpeciesDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("EchoSpecies")); }

	UPROPERTY(EditDefaultsOnly, Category="Identity", meta=(ClampMin=1)) int32 KodexNumber = 1;
	UPROPERTY(EditDefaultsOnly, Category="Identity") FText ScientificName;
	UPROPERTY(EditDefaultsOnly, Category="Typing", meta=(Categories="Type")) FGameplayTag PrimaryType;
	UPROPERTY(EditDefaultsOnly, Category="Typing", meta=(Categories="Type")) FGameplayTag SecondaryType;
	UPROPERTY(EditDefaultsOnly, Category="Stats") FEchoBaseStats BaseStats;
	UPROPERTY(EditDefaultsOnly, Category="Stats") FName GrowthRate;              // K18
	UPROPERTY(EditDefaultsOnly, Category="Ecology") EEchoRarity Rarity = EEchoRarity::Common;
	UPROPERTY(EditDefaultsOnly, Category="Ecology", meta=(Categories="Behavior")) FGameplayTagContainer ObservableTraits; // DR-02: ≥ 3
	UPROPERTY(EditDefaultsOnly, Category="Ecology", meta=(Categories="Niche")) FGameplayTagContainer Niches;             // DR-05: ≥ 1
	UPROPERTY(EditDefaultsOnly, Category="Ecology") TArray<FEchoCondition> SpawnConditions;                              // DR-15
	UPROPERTY(EditDefaultsOnly, Category="Ecology", meta=(Categories="Region")) FGameplayTagContainer Regions;
};
