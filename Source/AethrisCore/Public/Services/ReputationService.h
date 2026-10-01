// Copyright AETHRIS Team.
#pragma once

#include "GameplayTagContainer.h"
#include "UObject/Interface.h"
#include "ReputationService.generated.h"

/** Rufstand einer Fraktion (K47 §3). Ganzzahlig, deterministisch; Rang 1–6 aus `Data/Factions/ReputationRanks.csv`. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FReputationStanding
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadOnly) FGameplayTag Faction;        ///< Faction.Academy | Goldklang | Wildwatch | FreeVoices | Order
	UPROPERTY(BlueprintReadOnly) int32 Points = 0;            ///< kumuliert, ≥ 0
	UPROPERTY(BlueprintReadOnly) int32 Rank = 1;              ///< 1–6
	UPROPERTY(BlueprintReadOnly) int32 PointsToNextRank = 0;  ///< 0 bei Rang 6
	UPROPERTY(BlueprintReadOnly) int32 DiscountPermille = 0;  ///< 0/50/100/150 (K42 §9)
	UPROPERTY(BlueprintReadOnly) bool bUnlocked = false;      ///< Fraktion bekannt (RepStart-Quest abgeschlossen)
};

/** Ergebnis einer Rufänderung; löst Event.Reputation.Changed bzw. Event.Reputation.RankUp aus. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FReputationDelta
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadOnly) int32 Applied = 0;           ///< nach Tageskappe und Rangboden
	UPROPERTY(BlueprintReadOnly) int32 CappedAway = 0;        ///< durch DailyCap verworfen
	UPROPERTY(BlueprintReadOnly) int32 OldRank = 1;
	UPROPERTY(BlueprintReadOnly) int32 NewRank = 1;
};

UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class UReputationService : public UInterface { GENERATED_BODY() };

/**
 * Rufsystem (K47, implementiert in GF_Quests). Regeln:
 *  - Ruf sinkt nie unter die Schwelle des erreichten Rangs (ADR-177); negative Beträge werden dort abgeschnitten.
 *  - Tageskappen je Quelle (`ReputationSources.csv`, ADR-181) über die Spieluhr (Spieltag, K15), nicht Echtzeit.
 *  - Ruf ist Fortschritt, keine Gesinnung: Story-Haltungen liegen in Story-Flags (ADR-178).
 *  - Server-autoritativ im Koop; Gäste erhalten Ruf in ihrer eigenen Welt (K60).
 */
class AETHRISCORE_API IReputationService
{
	GENERATED_BODY()
public:
	virtual FReputationStanding GetStanding(FGameplayTag Faction) const = 0;

	/** Wendet eine Rufquelle an (SourceId aus `ReputationSources.csv`, z. B. REP_RELEASE). */
	virtual FReputationDelta AddReputation(FGameplayTag Faction, int32 Amount, FName SourceId) = 0;

	/** Höchster Rabatt über alle Fraktionen, deren Händler den Artikel führen (Rabatte stapeln nicht, K42 §9). */
	virtual int32 GetBestDiscountPermille(const FGameplayTagContainer& MerchantFactions) const = 0;

	/** Prüft eine Rang-Bedingung (Blaupausen, Tutoren, Ketten). */
	virtual bool MeetsRank(FGameplayTag Faction, int32 RequiredRank) const = 0;
};
