// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "NpcScheduleTypes.generated.h"

/** Aktivitätscodes der Tagesabläufe (`Data/World/SchedulePatterns.csv`, K53 §4). */
UENUM(BlueprintType)
enum class ENpcActivity : uint8
{
	Sleep, Wake, Work, Meal, Free, Tavern, Market, Home, Patrol, Shift,
	Lecture, Lab, Library, Read, Silence, Fish, Herd, School, Play, Travel, Rest
};

/** Ein Tagesablauf-Muster: Aktivität je Spielstunde (0–23). */
USTRUCT(BlueprintType)
struct GF_AI_API FNpcSchedulePattern
{
	GENERATED_BODY()

	UPROPERTY(EditDefaultsOnly) FName Name;                 ///< Tagwerk, Schicht, Nachtvolk, Wache, Gelehrt, Kloster, Fischer, Hirte, Kind, Karawane
	UPROPERTY(EditDefaultsOnly) TArray<ENpcActivity> Hours; ///< genau 24 Einträge
};

/** Laufzeitdaten eines benannten NPCs (Register `Data/World/Npcs.csv`). */
USTRUCT(BlueprintType)
struct GF_AI_API FNpcRuntimeState
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadOnly) FName NpcId;
	UPROPERTY(BlueprintReadOnly) FName Pattern;
	UPROPERTY(BlueprintReadOnly) uint8 ShiftGroup = 0;      ///< 0 = A, 1 = B, 2 = C (nur Muster „Schicht“)
	UPROPERTY(BlueprintReadOnly) ENpcActivity Current = ENpcActivity::Sleep;
	UPROPERTY(BlueprintReadOnly) FName OverrideReason;       ///< Wetter, Fest, Quest, Kampf (K53 §6) – None = Plan
	UPROPERTY(BlueprintReadOnly) int32 LastBarkGameMinute = -100000;
};

namespace Aethris::Npc
{
	/** Aktivität zur Spielstunde; Schichtgruppen verschieben das Muster um 8 h je Gruppe (A 6–14, B 14–22, C 22–6). */
	GF_AI_API ENpcActivity ActivityAt(const FNpcSchedulePattern& Pattern, int32 GameHour, uint8 ShiftGroup = 0);
}
