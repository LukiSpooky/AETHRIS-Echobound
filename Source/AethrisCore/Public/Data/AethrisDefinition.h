// Copyright AETHRIS Team.
#pragma once

#include "Engine/DataAsset.h"
#include "GameplayTagContainer.h"
#include "AethrisDefinition.generated.h"

/**
 * Basisklasse für Erweiterungen einer Definition durch Feature-Plugins (ADR-031).
 * Beispiel: GF_Capture hängt an UEchoSpeciesDefinition ein UEchoBondingFragment
 * (Bindungsrate, Lieblingsköder), ohne dass AethrisCore GF_Capture kennt.
 */
UCLASS(Abstract, EditInlineNew, DefaultToInstanced, CollapseCategories)
class AETHRISCORE_API UDefinitionFragment : public UObject
{
	GENERATED_BODY()
public:
	/** Validierung des Fragments im Editor (Data Validation). */
	virtual EDataValidationResult ValidateFragment(class FDataValidationContext& Context) const;
};

/**
 * Gemeinsame Basis aller Designdaten-Definitionen (CS-02).
 * Primary Asset ID = (Typ, Id) – Id folgt den Formaten aus K04 §7.
 */
UCLASS(Abstract)
class AETHRISCORE_API UAethrisDefinition : public UPrimaryDataAsset
{
	GENERATED_BODY()
public:
	/** Stabile ID (z. B. ECHO_001, ABL_A012). Nie wiederverwenden (Data/Meta/RetiredIds.csv). */
	UPROPERTY(EditDefaultsOnly, AssetRegistrySearchable, Category="Identity")
	FName Id;

	/** Lokalisierter Anzeigename (String-Table-Key <Domäne>.<Id>.Name, K04 §11). */
	UPROPERTY(EditDefaultsOnly, Category="Identity")
	FText DisplayName;

	/** Freie Tags zur Klassifikation (Filter, Regeln, KI). */
	UPROPERTY(EditDefaultsOnly, Category="Identity")
	FGameplayTagContainer Tags;

	/** Erweiterungen durch Feature-Plugins. */
	UPROPERTY(EditDefaultsOnly, Instanced, Category="Fragments")
	TArray<TObjectPtr<UDefinitionFragment>> Fragments;

	/** Erstes Fragment des angefragten Typs oder nullptr. */
	template <typename TFragment>
	const TFragment* FindFragment() const
	{
		for (const UDefinitionFragment* F : Fragments)
		{
			if (const TFragment* Typed = Cast<TFragment>(F)) { return Typed; }
		}
		return nullptr;
	}

	/** Primary-Asset-Typ – von Unterklassen festgelegt (EchoSpecies, Ability, Item, Quest). */
	virtual FPrimaryAssetType GetDefinitionType() const PURE_VIRTUAL(UAethrisDefinition::GetDefinitionType, return FPrimaryAssetType(););

	virtual FPrimaryAssetId GetPrimaryAssetId() const override { return FPrimaryAssetId(GetDefinitionType(), Id); }

#if WITH_EDITOR
	virtual EDataValidationResult IsDataValid(class FDataValidationContext& Context) const override;
#endif
};
