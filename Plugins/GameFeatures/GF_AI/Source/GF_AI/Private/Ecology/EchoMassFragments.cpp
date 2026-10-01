// Copyright AETHRIS Team.
#include "Ecology/EchoMassFragments.h"

namespace Aethris::Ecology
{
	int32 SpawnWeight(int32 RarityWeight, int32 ActivityPermille, int32 WeatherPermille,
	                  int32 MoonPermille, int32 PopulationPermille)
	{
		// Reihenfolge und Abrundung wie tools/ref/aethris_ecology.py (Referenz): jede Stufe ⌊x·m/1000⌋.
		const int64 A = FMath::Max<int32>(80, ActivityPermille);          // Minimum 80 ‰ (CANON §67)
		const int64 P = FMath::Clamp<int32>(PopulationPermille, 200, 1000); // Bestand: mindestens 20 % Gewicht
		int64 W = int64(RarityWeight) * A / 1000;
		W = W * WeatherPermille / 1000;
		W = W * MoonPermille / 1000;
		W = W * P / 1000;
		return int32(W);
	}
}
