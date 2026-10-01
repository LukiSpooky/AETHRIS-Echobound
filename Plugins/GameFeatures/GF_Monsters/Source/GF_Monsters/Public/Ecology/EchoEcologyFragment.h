// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "EchoEcologyFragment.generated.h"

/** Ökologische Rolle (K52 §3) – aus Verhaltensmerkmalen abgeleitet, im Editor überschreibbar. */
UENUM(BlueprintType)
enum class EEchoEcoRole : uint8
{
	PrimaryConsumer,  ///< Grazer, Pollinator, Filterer, Lithophage, Sunbather, Thermal
	Predator,         ///< Hunter, Ambusher – Klangbiss, nie Tötung (ADR-007)
	ResonanceScavenger, ///< Scavenger – Klangreste erschöpfter Echos
	Generalist        ///< alle übrigen
};

UENUM(BlueprintType)
enum class EEchoGroupKind : uint8 { Herd, Pack, Swarm, FamilyGroup, Solitary, Loose };

/**
 * Ökologie-Fragment an UEchoSpeciesDefinition (CD-09, K16 §2; Daten K52 `Data/Ecology/EcologyFragments.csv`).
 * Liegt in GF_Monsters (Domain); GF_AI liest es über die Definition (ADR-031).
 */
UCLASS(meta=(DisplayName="Ökologie"))
class GF_MONSTERS_API UEchoEcologyFragment : public UDefinitionFragment
{
	GENERATED_BODY()
public:
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") EEchoEcoRole Role = EEchoEcoRole::Generalist;
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") FText Food;
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") FText SleepSite;
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") FText Reproduction;
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") EEchoGroupKind Group = EEchoGroupKind::Loose;

	/** Tragfähigkeit je Zone (Individuen) und Mindestbestand (K52 §6). */
	UPROPERTY(EditDefaultsOnly, Category="Population", meta=(ClampMin=1)) int32 Capacity = 12;
	UPROPERTY(EditDefaultsOnly, Category="Population", meta=(ClampMin=1)) int32 Floor = 3;

	/** Beute (bis 3) aus `FoodWeb.csv`; leer bei Nicht-Räubern. */
	UPROPERTY(EditDefaultsOnly, Category="Ökologie") TArray<FPrimaryAssetId> Prey;
};
