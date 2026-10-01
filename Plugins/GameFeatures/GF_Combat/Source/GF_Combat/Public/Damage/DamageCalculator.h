// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"

/**
 * Schadensformel (K32 §2) – deterministisch, ohne Streuung (ADR-112), ganzzahlig.
 * Bitgleich zu tools/ref/aethris_combat.py::damage_chain (Test Aethris.Unit.Combat.Damage.PythonParity).
 */
namespace Aethris::Damage
{
	inline constexpr int32 Divisor = 180;
	inline constexpr int32 EigenklangPermille = 1250;
	inline constexpr int32 EigenklangMaxPermille = 1400;
	inline constexpr int32 CritPermille = 1500;
	inline constexpr int32 BurnAttackPermille = 750;
	inline constexpr int32 DuelAreaPermille = 800;
	inline constexpr int32 CritChancePermille[4] = { 42, 125, 250, 500 };

	/** Basis = ⌊Stärke × A × (L + 10) / (V × 180)⌋ + 2 */
	constexpr int32 Base(int32 Power, int32 Attack, int32 Defense, int32 Level)
	{
		return static_cast<int32>(int64(Power) * Attack * (Level + 10) / (int64(Defense > 0 ? Defense : 1) * Divisor)) + 2;
	}

	/** Ein Faktor in Promille, abgerundet (Reihenfolge CANON §77). */
	constexpr int32 Apply(int32 Value, int32 Permille) { return static_cast<int32>(int64(Value) * Permille / 1000); }

	struct FChainInput
	{
		int32 Power = 0, Attack = 0, Defense = 0, Level = 1;
		int32 EigenklangPermille = 1000;   // 1000 oder 1250–1400
		int32 TypePermille = 1000;         // Produkt der Zieltypen
		int32 WeatherPermille = 1000;
		bool bCrit = false;
		int32 FormationPermille = 1000;    // K33
		int32 OtherPermille = 1000;        // Passive, Terrain, Charged, Duell-Fläche … (bereits multipliziert)
	};

	constexpr int32 Compute(const FChainInput& In)
	{
		int32 V = Base(In.Power, In.Attack, In.Defense, In.Level);
		V = Apply(V, In.EigenklangPermille);
		V = Apply(V, In.TypePermille);
		V = Apply(V, In.WeatherPermille);
		V = Apply(V, In.bCrit ? CritPermille : 1000);
		V = Apply(V, In.FormationPermille);
		V = Apply(V, In.OtherPermille);
		return V < 1 ? 1 : V;
	}

	static_assert(Base(80, 87, 87, 50) == 28, "Referenzwert K32 §2");
	static_assert(Compute({ 80, 87, 87, 50, 1250, 1600, 1000, false, 1000, 1000 }) == 56, "Eigenklang × sehr effektiv");
	static_assert(Compute({ 10, 1, 400, 1, 1000, 391, 800, false, 750, 1000 }) == 1, "Mindestschaden 1");
}
