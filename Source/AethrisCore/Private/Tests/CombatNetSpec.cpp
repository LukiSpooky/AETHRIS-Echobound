// Copyright AETHRIS Team.
// Aethris.Unit.Core.CombatNet – Kampfbefehl-Packing (K59 §5.2). Erwartete Bytes aus tools/ref/aethris_net.py (pack_examples).
#if WITH_DEV_AUTOMATION_TESTS
#include "Misc/AutomationTest.h"
#include "Net/AethrisCombatNet.h"

BEGIN_DEFINE_SPEC(FCombatNetSpec, "Aethris.Unit.Core.CombatNet",
	EAutomationTestFlags::EditorContext | EAutomationTestFlags::ServerContext | EAutomationTestFlags::ProductFilter)
	static FAethrisCombatCommand Make(uint32 Tick, uint8 Slot, EAethrisCombatAction A, uint8 Ability, uint8 Target, uint8 Reserve)
	{
		FAethrisCombatCommand C; C.Tick = Tick; C.Slot = Slot; C.Action = A; C.Ability = Ability; C.Target = Target; C.Reserve = Reserve;
		return C;
	}
END_DEFINE_SPEC(FCombatNetSpec)

void FCombatNetSpec::Define()
{
	Describe("Pack", [this]()
	{
		It("entspricht dem Referenzvektor (Fähigkeit 2 auf Gegnerplatz 9, Tick 1200)", [this]()
		{
			uint8 Out[7];
			TestTrue(TEXT("packbar"), Make(1200, 0, EAethrisCombatAction::Ability, 2, 9, 0).Pack(Out));
			const uint8 Expected[7] = { 0xb0, 0x04, 0x00, 0x00, 0x80, 0x24, 0x00 };
			for (int32 i = 0; i < 7; ++i) { TestEqual(FString::Printf(TEXT("Byte %d"), i), Out[i], Expected[i]); }
		});

		It("entspricht dem Referenzvektor (Wechsel auf Reserveplatz 3, Tick 5100)", [this]()
		{
			uint8 Out[7];
			TestTrue(TEXT("packbar"), Make(5100, 0, EAethrisCombatAction::Switch, 0, 0, 3).Pack(Out));
			const uint8 Expected[7] = { 0xec, 0x13, 0x00, 0x00, 0x08, 0xc0, 0x00 };
			for (int32 i = 0; i < 7; ++i) { TestEqual(FString::Printf(TEXT("Byte %d"), i), Out[i], Expected[i]); }
		});

		It("weist Werte außerhalb der Bitbreiten ab", [this]()
		{
			uint8 Out[7];
			TestFalse(TEXT("Slot 8"), Make(1, 8, EAethrisCombatAction::Guard, 0, 0, 0).Pack(Out));
			TestFalse(TEXT("Ziel 16"), Make(1, 0, EAethrisCombatAction::Ability, 0, 16, 0).Pack(Out));
		});
	});

	Describe("Unpack", [this]()
	{
		It("ergibt nach Pack denselben Befehl (Rundreise)", [this]()
		{
			const FAethrisCombatCommand In = Make(3450, 1, EAethrisCombatAction::Ability, 4, 8, 0);
			uint8 Bytes[7]; In.Pack(Bytes);
			FAethrisCombatCommand Out;
			TestTrue(TEXT("lesbar"), FAethrisCombatCommand::Unpack(Bytes, Out));
			TestTrue(TEXT("gleich"), In == Out);
		});

		It("weist gesetzte Bits jenseits des Layouts ab", [this]()
		{
			const uint8 Bad[7] = { 0, 0, 0, 0, 0, 0, 0x80 };
			FAethrisCombatCommand Out;
			TestFalse(TEXT("manipuliert"), FAethrisCombatCommand::Unpack(Bad, Out));
		});
	});
}
#endif
