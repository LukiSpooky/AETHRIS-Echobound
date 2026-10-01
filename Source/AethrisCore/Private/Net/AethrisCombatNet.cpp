// Copyright AETHRIS Team.
#include "Net/AethrisCombatNet.h"

bool FAethrisCombatCommand::Pack(uint8 (&Out)[7]) const
{
	const uint8 Act = static_cast<uint8>(Action);
	if (Slot > 7 || Act > 7 || Ability > 15 || Target > 15 || Reserve > 7)
	{
		return false;
	}
	// 17 Bit Nutzdaten hinter dem 32-Bit-Tick: Slot(3) | Action(3) | Ability(4) | Target(4) | Reserve(3)
	const uint32 Bits = uint32(Slot) | (uint32(Act) << 3) | (uint32(Ability) << 6) | (uint32(Target) << 10) | (uint32(Reserve) << 14);
	const uint64 Word = uint64(Tick) | (uint64(Bits) << 32);
	for (int32 i = 0; i < 7; ++i)
	{
		Out[i] = uint8((Word >> (8 * i)) & 0xFF);
	}
	return true;
}

bool FAethrisCombatCommand::Unpack(const uint8 (&In)[7], FAethrisCombatCommand& Out)
{
	uint64 Word = 0;
	for (int32 i = 0; i < 7; ++i)
	{
		Word |= uint64(In[i]) << (8 * i);
	}
	if ((Word >> 49) != 0)
	{
		return false;   // gesetzte Bits jenseits des Layouts → manipuliertes Paket
	}
	const uint32 Bits = uint32(Word >> 32);
	Out.Tick = uint32(Word & 0xFFFFFFFFull);
	Out.Slot = uint8(Bits & 0x7);
	const uint8 Act = uint8((Bits >> 3) & 0x7);
	if (Act > static_cast<uint8>(EAethrisCombatAction::Forfeit))
	{
		return false;
	}
	Out.Action = static_cast<EAethrisCombatAction>(Act);
	Out.Ability = uint8((Bits >> 6) & 0xF);
	Out.Target = uint8((Bits >> 10) & 0xF);
	Out.Reserve = uint8((Bits >> 14) & 0x7);
	return true;
}

namespace Aethris::Net
{
	uint64 Fnv1a64(const uint8* Data, int32 Num, uint64 Seed)
	{
		uint64 H = Seed;
		for (int32 i = 0; i < Num; ++i)
		{
			H ^= Data[i];
			H *= 0x100000001b3ull;
		}
		return H;
	}
}
