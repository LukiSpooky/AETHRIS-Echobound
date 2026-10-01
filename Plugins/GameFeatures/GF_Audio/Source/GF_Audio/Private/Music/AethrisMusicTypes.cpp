// Copyright AETHRIS Team.
#include "Music/AethrisMusicTypes.h"

namespace Aethris::Audio
{
	int32 QuantizeToScaleCents(int32 CentsAboveD4)
	{
		// Oktave abtrennen (auch negativ), innerhalb der Oktave auf die nächste Stufe ziehen – Referenz: aethris_music.quantize
		const int32 Octave = (CentsAboveD4 >= 0) ? CentsAboveD4 / 1200 : -((-CentsAboveD4 + 1199) / 1200);
		const int32 Inner = CentsAboveD4 - Octave * 1200;
		int32 Best = ScaleCents[0];
		for (int32 Step : ScaleCents)
		{
			if (FMath::Abs(Step - Inner) < FMath::Abs(Best - Inner))
			{
				Best = Step;
			}
		}
		return Octave * 1200 + Best;
	}
}
