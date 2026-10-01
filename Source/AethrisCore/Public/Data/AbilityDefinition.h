// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "AbilityDefinition.generated.h"

/** Basis-Definition „Ability“ (ADR-031). Feature-spezifische Daten kommen über Fragmente; Felder in den Fachkapiteln. */
UCLASS(BlueprintType)
class AETHRISCORE_API UAbilityDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("Ability")); }
};
