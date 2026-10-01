// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "Echo/EchoTypes.h"

/**
 * Statusformeln (K18 §2). Rein ganzzahlig und constexpr – Determinismus-Zone (CS-14).
 * Bitgleich zur Referenz tools/ref/aethris_stats.py (Unit-Test Aethris.Unit.Core.Stats.PythonParity).
 */
namespace Aethris::Stats
{
	/** Maximalwerte (CANON §18/§79). */
	inline constexpr int32 MaxLevel = 100;
	inline constexpr int32 MaxAptitude = 15;
	inline constexpr int32 MaxPolishPerStat = 80;
	inline constexpr int32 MaxPolishTotal = 240;

	/** HP = ⌊B·(L+10)·(1000+10·A) / 40000⌋ + L + 12 + S */
	constexpr int32 ComputeHP(int32 Base, int32 Level, int32 Aptitude, int32 Polish)
	{
		return static_cast<int32>(int64(Base) * (Level + 10) * (1000 + 10 * Aptitude) / 40000) + Level + 12 + Polish;
	}

	/** Kernwert = ⌊⌊B·(L+10)·(1000+10·A) / 55000⌋ · P / 1000⌋ + ⌊S/2⌋, P = 1100 wenn Persönlichkeits-Stat. */
	constexpr int32 ComputeCore(int32 Base, int32 Level, int32 Aptitude, int32 Polish, bool bPersonalityBoost)
	{
		const int64 Raw = int64(Base) * (Level + 10) * (1000 + 10 * Aptitude) / 55000;
		return static_cast<int32>(Raw * (bPersonalityBoost ? 1100 : 1000) / 1000) + Polish / 2;
	}

	/** Präzision/Ausweichen = B + ⌊A/3⌋ (+5 bei Persönlichkeits-Stat). Levelunabhängig. */
	constexpr int32 ComputeSecondary(int32 Base, int32 Aptitude, bool bPersonalityBoost)
	{
		return Base + Aptitude / 3 + (bPersonalityBoost ? 5 : 0);
	}

	/** Stufenfaktoren −4…+4 (Data/Combat/StatStages.csv). */
	inline constexpr int32 CoreStagePermille[9] = { 500, 571, 667, 800, 1000, 1250, 1500, 1750, 2000 };
	inline constexpr int32 AccEvaStagePermille[9] = { 700, 775, 850, 925, 1000, 1075, 1150, 1225, 1300 };

	constexpr int32 ApplyStage(int32 Value, int32 Stage, bool bAccEva)
	{
		const int32 Idx = (Stage < -4 ? -4 : (Stage > 4 ? 4 : Stage)) + 4;
		return Value * (bAccEva ? AccEvaStagePermille[Idx] : CoreStagePermille[Idx]) / 1000;
	}

	/** Trefferchance in Promille, gedeckelt 500..1000 (DR-07). */
	constexpr int32 HitChancePermille(int32 AbilityAccuracyPermille, int32 Precision, int32 Evasion, int32 PrecStage, int32 EvaStage)
	{
		const int32 P = ApplyStage(Precision, PrecStage, true);
		const int32 E = ApplyStage(Evasion, EvaStage, true);
		const int32 Raw = AbilityAccuracyPermille * P / (E > 0 ? E : 1);
		return Raw < 500 ? 500 : (Raw > 1000 ? 1000 : Raw);
	}

	// Kompilierzeit-Prüfungen gegen die Python-Referenz (K18 §2.4)
	static_assert(ComputeHP(48, 5, 7, 0) == 36, "Fernlit L5 HP");
	static_assert(ComputeCore(42, 50, 7, 0, false) == 49, "Fernlit L50 ANG");
	static_assert(ComputeCore(140, 100, 15, 80, true) == 394, "Kernwert-Maximum");
	static_assert(HitChancePermille(950, 100, 120, 0, 0) == 791, "Trefferchance");
}
