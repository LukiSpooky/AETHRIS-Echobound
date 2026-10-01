// Copyright AETHRIS Team.
// Aethris.Unit.Save.Container – Container v2 (K64 §2). Testvektor aus tools/ref/aethris_save.py vector.
#if WITH_DEV_AUTOMATION_TESTS
#include "Misc/AutomationTest.h"
#include "AethrisSaveContainer.h"

BEGIN_DEFINE_SPEC(FSaveContainerSpec, "Aethris.Unit.Save.Container",
	EAutomationTestFlags::EditorContext | EAutomationTestFlags::ProductFilter)
	static TArray<uint8> Vector()
	{
		const FString Hex = TEXT("41455448020000003f0000000b00312e302e302d434c31323380d8db700000000040db020000000000030052303311000000050000000208004543484f5f30303108004543484f5f30363702000000040043686f7203000000000000001000000088e2cece0b00576f726c642e5a6f6e6573010000001000000004000000cdfb3cb6000102030405060708090a0b0c0d0e0f01020304a074121d");
		TArray<uint8> Out;
		for (int32 i = 0; i + 1 < Hex.Len(); i += 2) { Out.Add(static_cast<uint8>(FParse::HexNumber(*Hex.Mid(i, 2)))); }
		return Out;
	}
END_DEFINE_SPEC(FSaveContainerSpec)

void FSaveContainerSpec::Define()
{
	It("liest den Referenzvektor (Header + 2 Fragmente)", [this]()
	{
		FAethrisSaveHeader H; TArray<FAethrisSaveFragmentBlob> F; TArray<FName> Bad;
		TestTrue(TEXT("lesbar"), Aethris::Save::ReadContainer(Vector(), H, F, Bad));
		TestEqual(TEXT("Region"), H.RegionId, FName(TEXT("R03")));
		TestEqual(TEXT("Rang"), H.WardenRank, 17);
		TestEqual(TEXT("Akkorde"), H.AkkordCount, 5);
		TestEqual(TEXT("Fragmente"), F.Num(), 2);
		TestEqual(TEXT("defekt"), Bad.Num(), 0);
		TestEqual(TEXT("Chor-Version"), F[0].Version, 3);
	});

	It("schreibt byte-identisch zum Referenzvektor (Rundreise)", [this]()
	{
		FAethrisSaveHeader H; TArray<FAethrisSaveFragmentBlob> F; TArray<FName> Bad;
		Aethris::Save::ReadContainer(Vector(), H, F, Bad);
		TArray<uint8> Out;
		Aethris::Save::WriteContainer(H, F, Out);
		TestTrue(TEXT("identisch"), Out == Vector());
	});

	It("meldet nur das beschädigte Fragment (SA-03)", [this]()
	{
		TArray<uint8> V = Vector();
		V[V.Num() - 6] ^= 0xFF;   // letztes Byte von World.Zones
		FAethrisSaveHeader H; TArray<FAethrisSaveFragmentBlob> F; TArray<FName> Bad;
		TestTrue(TEXT("Container lesbar"), Aethris::Save::ReadContainer(V, H, F, Bad));
		TestEqual(TEXT("ein defektes Fragment"), Bad.Num(), 1);
		TestEqual(TEXT("World.Zones"), Bad[0], FName(TEXT("World.Zones")));
		TestEqual(TEXT("Chor erhalten"), F.Num(), 1);
	});
}
#endif
