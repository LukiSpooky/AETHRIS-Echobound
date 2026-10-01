// Copyright AETHRIS Team.
#include "Npc/NpcScheduleTypes.h"

namespace Aethris::Npc
{
	ENpcActivity ActivityAt(const FNpcSchedulePattern& Pattern, int32 GameHour, uint8 ShiftGroup)
	{
		if (Pattern.Hours.Num() != 24)
		{
			return ENpcActivity::Free;
		}
		const int32 Shifted = ((GameHour - int32(ShiftGroup) * 8) % 24 + 24) % 24;
		return Pattern.Hours[Shifted];
	}
}
