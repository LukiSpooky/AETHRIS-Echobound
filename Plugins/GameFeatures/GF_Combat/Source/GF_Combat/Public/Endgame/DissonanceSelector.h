// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"

/**
 * Auswahl der Dissonanzen einer Tiefenresonanz (K62 §3.4, `Data/Endgame/Dissonances.csv`).
 * Deterministisch aus Weltseed, Spieltag und Ort: Alle Spielenden derselben Welt (auch Koop-Gäste) sehen
 * am selben Spieltag dieselben Dissonanzen; die Auswahl ist vor dem Betreten sichtbar (DR-06, DR-07).
 */
namespace Aethris::Endgame
{
	inline constexpr int32 NumDissonances = 12;

	/**
	 * Liefert Count verschiedene Dissonanz-Indizes (0 … NumDissonances − 1) in OutIndices.
	 * Substream = Fork(6) der Weltsaat (CANON §29 erweitert: Fork(6) Endgame), Mischung aus Spieltag und Ort.
	 */
	GF_COMBAT_API void SelectDissonances(uint64 WorldSeed, int32 GameDay, int32 LocationIndex, int32 Count, TArray<int32>& OutIndices);
}
