// Copyright AETHRIS Team.
#pragma once

#include "GameplayTagContainer.h"
#include "CombatMessages.generated.h"

/** Kanal Event.Combat.Started (K06 §4.3). */
USTRUCT()
struct AETHRISCORE_API FCombatStartedMsg
{
	GENERATED_BODY()
	UPROPERTY() FGuid CombatId;
	UPROPERTY() FGameplayTag Format;      // Combat.Format.*
	UPROPERTY() FVector Center = FVector::ZeroVector;
	UPROPERTY() float Radius = 0.f;       // Kampfkreis (ADR-013), Präsentationswert – nicht Teil der Kampflogik
};

/** Kanal Event.Combat.Ended (K06 §4.2). */
USTRUCT()
struct AETHRISCORE_API FCombatEndedMsg
{
	GENERATED_BODY()
	UPROPERTY() FGuid CombatId;
	UPROPERTY() FGameplayTag Format;
	UPROPERTY() uint8 Result = 0;          // 0 Sieg, 1 Niederlage, 2 Flucht, 3 Bindung
	UPROPERTY() TArray<FPrimaryAssetId> DefeatedSpecies;
	UPROPERTY() int32 DurationSeconds = 0;
};
