// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisRankedTypes.generated.h"

/** Sichtbare Klangstufen (`Data/PvP/RankTiers.csv`, K61 §4). */
UENUM(BlueprintType)
enum class EAethrisRankTier : uint8
{
	Summen, Ruf, Lied, Chor, Hymne, Weltakkord
};

/** Glicko-2-Wertung (Glickman 2012), serverseitig im Ranked-Dienst; Referenz tools/ref/aethris_pvp.py. */
USTRUCT(BlueprintType)
struct GF_PVP_API FAethrisGlicko2
{
	GENERATED_BODY()

	UPROPERTY() double Rating = 1500.0;      ///< R (Glicko-Skala)
	UPROPERTY() double Deviation = 350.0;    ///< RD
	UPROPERTY() double Volatility = 0.06;    ///< σ
	UPROPERTY() int32 Matches = 0;

	/** Konservative Wertung für die sichtbare Stufe: R − 2·RD. */
	double Conservative() const { return Rating - 2.0 * Deviation; }
};

namespace Aethris::Ranked
{
	inline constexpr int32 NormLevel = 70;          ///< Q5 (K61 §2): alle Echos werden auf Level 70 umgerechnet
	inline constexpr int32 PlacementMatches = 5;    ///< danach sichtbare Stufe
	inline constexpr double Tau = 0.5;              ///< Glicko-2-Systemkonstante

	/** Ein Kampf = eine Bewertungsperiode. Score 1 Sieg, 0 Niederlage, 0,5 Zeitlimit-Gleichstand. */
	GF_PVP_API FAethrisGlicko2 Update(const FAethrisGlicko2& Self, const FAethrisGlicko2& Opponent, double Score);

	/** RD-Anstieg bei Inaktivität: je Woche ohne Kampf wie eine leere Bewertungsperiode (max. 350). */
	GF_PVP_API FAethrisGlicko2 DecayWeek(const FAethrisGlicko2& Self);

	/** Sichtbare Stufe aus der konservativen Wertung (Grenzen 1150/1350/1550/1750/2050). */
	GF_PVP_API EAethrisRankTier TierFor(double Conservative);
}
