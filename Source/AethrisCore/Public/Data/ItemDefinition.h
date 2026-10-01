// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "ItemDefinition.generated.h"

/** Basis-Definition „Item“ (ADR-031). Feature-spezifische Daten kommen über Fragmente; Felder in den Fachkapiteln. */
UCLASS(BlueprintType)
class AETHRISCORE_API UItemDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("Item")); }
};
