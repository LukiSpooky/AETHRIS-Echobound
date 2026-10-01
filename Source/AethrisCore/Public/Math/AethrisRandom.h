// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisRandom.generated.h"

/**
 * Deterministischer Zufallsgenerator (PCG32, XSH-RR-Variante) – CS-14, ADR-029.
 *
 * Warum nicht FRandomStream? FRandomStream ist ein einfacher LCG mit schwacher Verteilung in den
 * unteren Bits und Fließkomma-Hilfsfunktionen; für PvP-Replays und Genetik brauchen wir eine
 * plattformunabhängige, gut verteilte Ganzzahlquelle mit unabhängigen Teilströmen.
 *
 * Referenzimplementierung für Tests: tools/ref/aethris_random.py (identische Ausgaben).
 */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FAethrisRandom
{
	GENERATED_BODY()

	FAethrisRandom() { Seed(0x853C49E6748FEA9BULL, 0xDA3E39CB94B95BDBULL); }
	FAethrisRandom(uint64 InSeed, uint64 InStream) { Seed(InSeed, InStream); }

	/** Initialisiert Zustand und Strom (Stream wählt eine unabhängige Sequenz). */
	void Seed(uint64 InSeed, uint64 InStream)
	{
		State = 0;
		Inc = (InStream << 1u) | 1u;
		NextU32();
		State += InSeed;
		NextU32();
	}

	/** Nächste 32-Bit-Zufallszahl. */
	uint32 NextU32()
	{
		const uint64 Old = State;
		State = Old * 6364136223846793005ULL + Inc;
		const uint32 XorShifted = static_cast<uint32>(((Old >> 18u) ^ Old) >> 27u);
		const uint32 Rot = static_cast<uint32>(Old >> 59u);
		return (XorShifted >> Rot) | (XorShifted << ((32u - Rot) & 31u));
	}

	/** Gleichverteilte Zahl in [0, Bound) ohne Modulo-Bias (Rejection Sampling). */
	uint32 NextBounded(uint32 Bound)
	{
		check(Bound > 0);
		const uint32 Threshold = (0u - Bound) % Bound;
		for (;;)
		{
			const uint32 R = NextU32();
			if (R >= Threshold)
			{
				return R % Bound;
			}
		}
	}

	/** Gleichverteilte Ganzzahl in [Min, Max] (inklusive). */
	int32 RangeInclusive(int32 Min, int32 Max)
	{
		check(Max >= Min);
		return Min + static_cast<int32>(NextBounded(static_cast<uint32>(Max - Min) + 1u));
	}

	/** true mit Wahrscheinlichkeit Permille/1000 (Ganzzahl, deterministisch). */
	bool ChancePermille(int32 Permille)
	{
		if (Permille <= 0) { return false; }
		if (Permille >= 1000) { return true; }
		return static_cast<int32>(NextBounded(1000)) < Permille;
	}

	/** Leitet einen unabhängigen Teilstrom ab (z. B. pro Kampfteilnehmer oder pro Zuchtvorgang). */
	FAethrisRandom Fork(uint64 SubStreamId)
	{
		const uint64 NewSeed = (static_cast<uint64>(NextU32()) << 32) | NextU32();
		return FAethrisRandom(NewSeed, (Inc >> 1) ^ (SubStreamId * 0x9E3779B97F4A7C15ULL));
	}

	/** Zustand ist vollständig serialisierbar (Save, Replay, Netzwerk). */
	UPROPERTY(SaveGame) uint64 State = 0;
	UPROPERTY(SaveGame) uint64 Inc = 1;
};
