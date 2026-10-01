// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisMusicTypes.generated.h"

/** Adaptive Musikzustände (`Data/Audio/MusicStates.csv`, K55 §4). Reihenfolge = Priorität (kleiner = wichtiger). */
UENUM(BlueprintType)
enum class EAethrisMusicState : uint8
{
	Story, Decision, Boss, Arena, CombatTrainer, CombatWild, Bond, Silence, Storm, Town, ExploreDay, ExploreNight, Camp, Pause
};

/** Rufprofil einer Art (`Data/Audio/EchoCalls.csv`) – Parameter für den MetaSounds-Patch des Typs. */
USTRUCT(BlueprintType)
struct GF_AUDIO_API FEchoCallProfile
{
	GENERATED_BODY()

	UPROPERTY(EditDefaultsOnly) int32 MidiPitch = 62;      ///< 0 = Pause (Leere)
	UPROPERTY(EditDefaultsOnly) int32 Bpm = 56;            ///< aus dem Klangmal (K16 §3) oder Größe
	UPROPERTY(EditDefaultsOnly) FName Rhythm;              ///< Rufreihe | Klickfolge | Schwarmchor | Nachahmung | Einzelruf
	UPROPERTY(EditDefaultsOnly) FName TimbrePatch;         ///< MSS_Type_<Typ>
	UPROPERTY(EditDefaultsOnly) FName OvertonePatch;       ///< Sekundärtyp, optional
};

namespace Aethris::Audio
{
	/** Aethrische Skala (D-Dorisch) als Cent-Stufen über dem Grundton. */
	inline constexpr int32 ScaleCents[8] = { 0, 200, 300, 500, 700, 900, 1000, 1200 };

	/** Resonanzsturm (CANON §63): zieht eine Tonhöhe (Cent über D4, beliebige Oktave) auf die nächste Skalenstufe. */
	GF_AUDIO_API int32 QuantizeToScaleCents(int32 CentsAboveD4);
}
