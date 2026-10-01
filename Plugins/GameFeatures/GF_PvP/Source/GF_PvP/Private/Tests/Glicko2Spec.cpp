// Copyright AETHRIS Team.
// Aethris.Unit.PvP.Glicko2 – Wertung (K61 §4.4). Erwartete Werte aus tools/ref/aethris_pvp.py (glicko2_update).
#if WITH_DEV_AUTOMATION_TESTS
#include "Misc/AutomationTest.h"
#include "Ranked/AethrisRankedTypes.h"

BEGIN_DEFINE_SPEC(FGlicko2Spec, "Aethris.Unit.PvP.Glicko2",
	EAutomationTestFlags::EditorContext | EAutomationTestFlags::ServerContext | EAutomationTestFlags::ProductFilter)
END_DEFINE_SPEC(FGlicko2Spec)

void FGlicko2Spec::Define()
{
	It("Sieg 1500/200 gegen 1400/30 entspricht der Referenz", [this]()
	{
		FAethrisGlicko2 A; A.Rating = 1500; A.Deviation = 200; A.Volatility = 0.06;
		FAethrisGlicko2 B; B.Rating = 1400; B.Deviation = 30;  B.Volatility = 0.06;
		const FAethrisGlicko2 R = Aethris::Ranked::Update(A, B, 1.0);
		TestEqual(TEXT("R"), R.Rating, 1563.5641943063383, 1e-6);
		TestEqual(TEXT("RD"), R.Deviation, 175.402655938555, 1e-6);
		TestEqual(TEXT("σ"), R.Volatility, 0.059998657304847616, 1e-9);
	});

	It("Niederlage eines neuen Kontos gegen ein neues Konto", [this]()
	{
		const FAethrisGlicko2 R = Aethris::Ranked::Update(FAethrisGlicko2(), FAethrisGlicko2(), 0.0);
		TestEqual(TEXT("R"), R.Rating, 1337.6891060937023, 1e-6);
		TestEqual(TEXT("RD"), R.Deviation, 290.31896371798047, 1e-6);
	});

	It("Stufen aus der konservativen Wertung", [this]()
	{
		TestEqual(TEXT("Summen"), Aethris::Ranked::TierFor(800.0), EAethrisRankTier::Summen);
		TestEqual(TEXT("Lied"), Aethris::Ranked::TierFor(1400.0), EAethrisRankTier::Lied);
		TestEqual(TEXT("Weltakkord"), Aethris::Ranked::TierFor(2050.0), EAethrisRankTier::Weltakkord);
	});
}
#endif
