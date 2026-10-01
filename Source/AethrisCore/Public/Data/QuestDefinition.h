// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "QuestDefinition.generated.h"

/** Basis-Definition „Quest“ (ADR-031). Feature-spezifische Daten kommen über Fragmente; Felder in den Fachkapiteln. */
UCLASS(BlueprintType)
class AETHRISCORE_API UQuestDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("Quest")); }
};
