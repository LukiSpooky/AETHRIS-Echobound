// Copyright AETHRIS Team.
#include "Vfx/AethrisVfxTypes.h"

namespace Aethris::Vfx
{
	bool AllowFlash(double NowSec, double LastFlashSec)
	{
		return LastFlashSec < 0.0 || (NowSec - LastFlashSec) >= MinFlashIntervalSec;
	}

	float FlashIntensity(bool bReduceMotion)
	{
		return bReduceMotion ? 0.4f : 1.0f;
	}

	int32 ScaleSpawnCount(int32 BaseCount, int32 IntensityPercent, float BudgetFill01, bool bMandatory)
	{
		const float Intensity = FMath::Clamp(IntensityPercent, 40, 100) / 100.f;
		float BudgetFactor = 1.f;
		if (BudgetFill01 >= 1.f)
		{
			BudgetFactor = bMandatory ? 0.25f : 0.f;
		}
		else if (BudgetFill01 > 0.8f)
		{
			BudgetFactor = FMath::Lerp(1.f, 0.25f, (BudgetFill01 - 0.8f) / 0.2f);
		}
		const int32 Count = FMath::FloorToInt32(BaseCount * Intensity * BudgetFactor);
		return bMandatory ? FMath::Max(Count, 1) : Count;
	}
}
