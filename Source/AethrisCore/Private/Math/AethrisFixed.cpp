// Copyright AETHRIS Team.
#include "Math/AethrisFixed.h"

namespace
{
	/** 2^(2^-k) in Q16.16 für k = 1..16 (vorab berechnet, siehe tools/ref/aethris_fixed.py). */
	constexpr int32 Exp2FracTable[16] = {
		92682, 77936, 71468, 68438, 66971, 66250, 65892, 65714,
		65625, 65580, 65558, 65547, 65542, 65539, 65537, 65537
	};
}

FAethrisFixed FAethrisFixed::Log2(FAethrisFixed X)
{
	check(X.Raw > 0);
	int64 V = X.Raw;
	int32 IntPart = 0;
	// Normieren auf [1, 2) in Q16.16
	while (V >= (2LL << FracBits)) { V >>= 1; ++IntPart; }
	while (V < (1LL << FracBits))  { V <<= 1; --IntPart; }

	int32 Frac = 0;
	for (int32 Bit = FracBits - 1; Bit >= 0; --Bit)
	{
		V = (V * V) >> FracBits; // Quadrieren
		if (V >= (2LL << FracBits))
		{
			V >>= 1;
			Frac |= (1 << Bit);
		}
	}
	return FromRaw(IntPart * One + Frac);
}

FAethrisFixed FAethrisFixed::Exp2(FAethrisFixed X)
{
	const int32 IntPart = X.Raw >> FracBits;          // floor (auch für negative Werte)
	const int32 Frac = X.Raw & (One - 1);              // [0, 1)
	int64 Result = One;
	for (int32 k = 0; k < FracBits; ++k)
	{
		if (Frac & (1 << (FracBits - 1 - k)))
		{
			Result = (Result * Exp2FracTable[k]) >> FracBits;
		}
	}
	if (IntPart >= 0)
	{
		Result <<= IntPart;
	}
	else
	{
		Result >>= -IntPart;
	}
	return FromRaw(static_cast<int32>(FMath::Min<int64>(Result, MAX_int32)));
}
