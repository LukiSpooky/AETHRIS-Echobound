// Copyright AETHRIS Team.
#include "Endgame/DissonanceSelector.h"
#include "Math/AethrisRandom.h"

namespace Aethris::Endgame
{
	void SelectDissonances(uint64 WorldSeed, int32 GameDay, int32 LocationIndex, int32 Count, TArray<int32>& OutIndices)
	{
		OutIndices.Reset();
		Count = FMath::Clamp(Count, 0, NumDissonances);
		FAethrisRandom Rng = FAethrisRandom(WorldSeed, 0).Fork(6).Fork((uint64(uint32(GameDay)) << 8) | uint64(uint32(LocationIndex) & 0xFF));
		// Teilweise Fisher-Yates über die Indexliste: Count verschiedene Einträge, reihenfolgestabil.
		int32 Pool[NumDissonances];
		for (int32 i = 0; i < NumDissonances; ++i) { Pool[i] = i; }
		for (int32 i = 0; i < Count; ++i)
		{
			const int32 j = i + static_cast<int32>(Rng.NextBounded(uint32(NumDissonances - i)));
			Swap(Pool[i], Pool[j]);
			OutIndices.Add(Pool[i]);
		}
	}
}
