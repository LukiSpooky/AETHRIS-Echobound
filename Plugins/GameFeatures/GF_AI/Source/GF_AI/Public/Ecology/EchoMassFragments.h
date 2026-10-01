// Copyright AETHRIS Team.
#pragma once

#include "MassEntityTypes.h"
#include "EchoMassFragments.generated.h"

/** Sim-Stufe eines Wildechos (K52 §7). */
UENUM()
enum class EEchoSimLOD : uint8
{
	Actor,       ///< < 150 m oder in Interaktion: voller Actor, StateTree, Animation
	MassNear,    ///< 150–500 m: Mass, vereinfachte Steuerung, ISM/Vertex-Animation
	MassFar,     ///< 500 m – Streaming-Grenze: Mass ohne Rendering, 1 Hz
	Statistical  ///< außerhalb der gestreamten Zellen: nur Zähler je (Zone, Art), Spieltag-Takt
};

/** Kern eines Wildechos in Mass. Kein Kampfzustand (Kampf = Actor, K31). */
USTRUCT()
struct GF_AI_API FEchoAgentFragment : public FMassFragment
{
	GENERATED_BODY()
	FPrimaryAssetId Species;
	uint16 ZoneIndex = 0;
	uint16 GroupId = 0;          ///< 0 = keiner Gruppe zugehörig
	uint8 State = 0;             ///< EEchoBehaviorState (K52 §8)
	uint8 bAlpha : 1;
	uint8 bResting : 1;
	int16 Fear = 0;              ///< 0–1000 ‰
	int16 Hunger = 0;            ///< 0–1000 ‰ (Räuber: Klanghunger)
	FVector HomeLocation = FVector::ZeroVector;
	FEchoAgentFragment() : bAlpha(0), bResting(0) {}
};

/** Gruppe (Herde, Rudel, Schwarm, Familie) – Steuerparameter aus `GroupBehaviors.csv`. */
USTRUCT()
struct GF_AI_API FEchoGroupFragment : public FMassSharedFragment
{
	GENERATED_BODY()
	uint16 GroupId = 0;
	int32 SeparationCm = 180;
	int16 CohesionPermille = 600;
	int16 AlignmentPermille = 500;
	int16 SeparationPermille = 700;
	int32 WanderRadiusCm = 12000;
	FMassEntityHandle Leader;
};

/** Wahrnehmungsprofil aus Verhaltensmerkmalen (`Data/Ecology/PerceptionProfiles.csv`). */
USTRUCT()
struct GF_AI_API FEchoPerceptionFragment : public FMassConstSharedFragment
{
	GENERATED_BODY()
	int32 SightCm = 2500;
	int32 HearingCm = 1500;
	int32 FleeCm = 0;            ///< Shy: 1500
	int32 ApproachCm = 0;        ///< Curious: 800
	int32 AggroCm = 0;           ///< Aggressive/Territorial
	int16 SightConeDeg = 120;
};

namespace Aethris::Ecology
{
	/** Spawn-Gewicht (K52 §4.2) in ‰-Ganzzahl: Seltenheit × Aktivität × Wetter × Mond × Bestand. */
	GF_AI_API int32 SpawnWeight(int32 RarityWeight, int32 ActivityPermille, int32 WeatherPermille,
	                            int32 MoonPermille, int32 PopulationPermille);
}
