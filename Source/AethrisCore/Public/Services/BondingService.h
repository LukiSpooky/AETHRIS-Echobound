// Copyright AETHRIS Team.
#pragma once

#include "UObject/Interface.h"
#include "BondingService.generated.h"

/** Vorschau einer Resonanzbindung (K36 §3): kein Prozentwurf, sondern Resonanz gegen Schwelle + Timing-Fenster. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FBondPreview
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadOnly) int32 Resonance = 0;        ///< 0–1000, aus Spielerentscheidungen
	UPROPERTY(BlueprintReadOnly) int32 Threshold = 0;        ///< Seltenheits-Schwelle − Siegelbonus
	UPROPERTY(BlueprintReadOnly) int32 GoodWindowMs = 0;     ///< 160–400 ms (Q12), × Temperament × Siegel × Option
	UPROPERTY(BlueprintReadOnly) int32 PerfectWindowMs = 0;  ///< 25 % des Gut-Fensters, min. 60 ms
	UPROPERTY(BlueprintReadOnly) int32 AttemptsLeft = 0;     ///< 2–4 je Temperament
	UPROPERTY(BlueprintReadOnly) bool bRequiresSpecialSeal = false; ///< Stimm-/Sternensiegel
};

UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class UBondingService : public UInterface { GENERATED_BODY() };

/** Vertrag der Resonanzbindung (implementiert in GF_Capture, K36). Deterministisch, kein Erfolgswurf (DR-03/DR-07). */
class AETHRISCORE_API IBondingService
{
	GENERATED_BODY()
public:
	/** Vorschau für UI und KI (K36 §3). */
	virtual FBondPreview PreviewBond(const FGuid& WildEchoId, FPrimaryAssetId SealItem) const = 0;

	/** Startet die Anschlag-Phase; Ergebnis kommt als Event.Echo.Bonded, Event.Bond.Approached oder Event.Bond.Failed. */
	virtual bool BeginStrikePhase(const FGuid& WildEchoId, FPrimaryAssetId SealItem, bool bFromCombat) = 0;
};
