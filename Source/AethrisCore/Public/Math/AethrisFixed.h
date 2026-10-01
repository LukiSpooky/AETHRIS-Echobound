// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"

/**
 * Festkommazahl Q16.16 für die Determinismus-Zone (CS-14, ADR-029).
 * Wertebereich ca. ±32767, Auflösung 1/65536. Multiplikation/Division über int64.
 * Alle Operationen sind plattformunabhängig bitgenau (keine Fließkomma-Befehle).
 */
struct AETHRISCORE_API FAethrisFixed
{
	static constexpr int32 FracBits = 16;
	static constexpr int32 One = 1 << FracBits;

	int32 Raw = 0;

	constexpr FAethrisFixed() = default;
	static constexpr FAethrisFixed FromRaw(int32 InRaw) { FAethrisFixed F; F.Raw = InRaw; return F; }
	static constexpr FAethrisFixed FromInt(int32 V) { return FromRaw(V * One); }
	/** Bruch Num/Den, abgerundet Richtung null. Bevorzugte Art, Designwerte (z. B. 1,25 = 5/4) einzugeben. */
	static constexpr FAethrisFixed FromRatio(int32 Num, int32 Den) { return FromRaw(static_cast<int32>((static_cast<int64>(Num) << FracBits) / Den)); }
	/** Promille (z. B. 1250 = 1,25) – Format der Designdaten-CSV. */
	static constexpr FAethrisFixed FromPermille(int32 Permille) { return FromRatio(Permille, 1000); }

	constexpr int32 FloorToInt() const { return Raw >> FracBits; }
	constexpr int32 RoundToInt() const { return (Raw + (One >> 1)) >> FracBits; }

	constexpr FAethrisFixed operator+(FAethrisFixed O) const { return FromRaw(Raw + O.Raw); }
	constexpr FAethrisFixed operator-(FAethrisFixed O) const { return FromRaw(Raw - O.Raw); }
	constexpr FAethrisFixed operator*(FAethrisFixed O) const { return FromRaw(static_cast<int32>((static_cast<int64>(Raw) * O.Raw) >> FracBits)); }
	constexpr FAethrisFixed operator/(FAethrisFixed O) const { return FromRaw(static_cast<int32>((static_cast<int64>(Raw) << FracBits) / O.Raw)); }
	constexpr bool operator<(FAethrisFixed O) const { return Raw < O.Raw; }
	constexpr bool operator>(FAethrisFixed O) const { return Raw > O.Raw; }
	constexpr bool operator==(FAethrisFixed O) const { return Raw == O.Raw; }

	/** Binärer Logarithmus (Bit-für-Bit-Verfahren, 16 Nachkommabits). Erwartet Wert > 0. */
	static FAethrisFixed Log2(FAethrisFixed X);
	/** 2^X für X in Q16.16 (Ganzzahlteil per Shift, Bruchteil per Produkt aus 2^(2^-k)-Tabelle). */
	static FAethrisFixed Exp2(FAethrisFixed X);
	/** Base^Exp = 2^(Exp·log2(Base)). Für Formeln wie (ANG/VER)^0,85 (K32). Base > 0. */
	static FAethrisFixed Pow(FAethrisFixed Base, FAethrisFixed Exp) { return Exp2(Exp * Log2(Base)); }
	/** Begrenzung auf [Lo, Hi]. */
	static constexpr FAethrisFixed Clamp(FAethrisFixed V, FAethrisFixed Lo, FAethrisFixed Hi) { return V < Lo ? Lo : (V > Hi ? Hi : V); }
};
