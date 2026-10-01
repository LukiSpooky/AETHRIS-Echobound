// Copyright AETHRIS Team.
#pragma once

#include "EditorValidatorBase.h"
#include "AethrisAssetNamingValidator.generated.h"

/**
 * Asset-Validator (K57 §8): Präfixe (CANON §23), Texturen-Suffixe, Texeldichte-Kennzeichnung, LOD-Anzahl je Asset-Klasse
 * (`Data/Art/AssetBudgets.csv`), Klangmal-Maske bei Echos. Läuft in Data Validation (Pre-Submit, CANON §27).
 */
UCLASS()
class AETHRISEDITOR_API UAethrisAssetNamingValidator : public UEditorValidatorBase
{
	GENERATED_BODY()
protected:
	virtual bool CanValidateAsset_Implementation(const FAssetData& InAssetData, UObject* InObject, FDataValidationContext& InContext) const override;
	virtual EDataValidationResult ValidateLoadedAsset_Implementation(const FAssetData& InAssetData, UObject* InAsset, FDataValidationContext& Context) override;

private:
	/** Erwartetes Präfix je Asset-Klasse (SM_, SK_, SKEL_, AS_, ABP_, AM_, M_, MI_, T_, NS_, MSS_, SW_, WBP_, PCG_, DA_, DT_). */
	static FString ExpectedPrefix(const UClass* AssetClass);
};
