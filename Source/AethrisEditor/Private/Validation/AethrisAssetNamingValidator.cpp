// Copyright AETHRIS Team.
#include "Validation/AethrisAssetNamingValidator.h"

#include "Animation/AnimMontage.h"
#include "Animation/AnimSequence.h"
#include "Engine/SkeletalMesh.h"
#include "Engine/StaticMesh.h"
#include "Engine/Texture2D.h"
#include "Materials/Material.h"
#include "Materials/MaterialInstanceConstant.h"
#include "Misc/DataValidation.h"

#define LOCTEXT_NAMESPACE "AethrisAssetNamingValidator"

FString UAethrisAssetNamingValidator::ExpectedPrefix(const UClass* AssetClass)
{
	if (AssetClass->IsChildOf<UStaticMesh>())               return TEXT("SM_");
	if (AssetClass->IsChildOf<USkeletalMesh>())             return TEXT("SK_");
	if (AssetClass->IsChildOf<UAnimSequence>())             return TEXT("AS_");
	if (AssetClass->IsChildOf<UAnimMontage>())              return TEXT("AM_");
	if (AssetClass->IsChildOf<UMaterialInstanceConstant>()) return TEXT("MI_");
	if (AssetClass->IsChildOf<UMaterial>())                 return TEXT("M_");
	if (AssetClass->IsChildOf<UTexture2D>())                return TEXT("T_");
	return FString();
}

bool UAethrisAssetNamingValidator::CanValidateAsset_Implementation(const FAssetData& InAssetData, UObject* InObject, FDataValidationContext& InContext) const
{
	return InObject && InAssetData.PackagePath.ToString().StartsWith(TEXT("/Game/Aethris"));
}

EDataValidationResult UAethrisAssetNamingValidator::ValidateLoadedAsset_Implementation(const FAssetData& InAssetData, UObject* InAsset, FDataValidationContext& Context)
{
	const FString Name = InAssetData.AssetName.ToString();
	const FString Prefix = ExpectedPrefix(InAsset->GetClass());
	if (!Prefix.IsEmpty() && !Name.StartsWith(Prefix))
	{
		Context.AddError(FText::Format(LOCTEXT("Prefix", "{0}: erwartetes Präfix {1} (CANON §23)"), FText::FromString(Name), FText::FromString(Prefix)));
		return EDataValidationResult::Invalid;
	}
	if (InAsset->IsA<UTexture2D>())
	{
		static const TArray<FString> Suffixes = { TEXT("_D"), TEXT("_N"), TEXT("_ORM"), TEXT("_E"), TEXT("_M") };
		const bool bOk = Suffixes.ContainsByPredicate([&Name](const FString& S) { return Name.EndsWith(S); });
		if (!bOk)
		{
			Context.AddError(FText::Format(LOCTEXT("Suffix", "{0}: Textur ohne Suffix _D/_N/_ORM/_E/_M"), FText::FromString(Name)));
			return EDataValidationResult::Invalid;
		}
	}
	return EDataValidationResult::Valid;
}

#undef LOCTEXT_NAMESPACE
