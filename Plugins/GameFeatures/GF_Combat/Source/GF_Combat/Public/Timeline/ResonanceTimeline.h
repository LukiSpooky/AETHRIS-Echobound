// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "Math/AethrisRandom.h"

/**
 * Resonanz-Zeitleiste (K31, löst Q1). Rein ganzzahlig, deterministisch, serverautoritativ im PvP (DR-21).
 * Bitgleich zu tools/ref/aethris_combat.py (Unit-Test Aethris.Unit.Combat.Timeline.PythonParity).
 */
namespace Aethris::Timeline
{
	inline constexpr int32 DelayNumerator = 300;
	inline constexpr int32 DelayOffset = 200;
	inline constexpr int32 MinDelay = 10;
	inline constexpr int32 ExternalDelayCap = 100;   ///< Anti-Lock: Fremdverzögerung zwischen zwei eigenen Zügen
	inline constexpr int32 VorgriffPerPriority = 25; ///< Vorgriff-Fenster je Prioritätsstufe
	inline constexpr int32 RoundTicks = 100;         ///< globale Runde (Terrain/Wetter)
	inline constexpr int32 SwitchCost = 60;
	inline constexpr int32 ChargeRecoveryCost = 50;

	/** Verzögerung = ⌊Zeitkosten × 300 / (GES_eff + 200)⌋, min. 10. */
	constexpr int32 Delay(int32 TimeCost, int32 SpeedEff)
	{
		const int32 D = TimeCost * DelayNumerator / ((SpeedEff > 0 ? SpeedEff : 1) + DelayOffset);
		return D < MinDelay ? MinDelay : D;
	}

	/** Effektive Zeitkosten unter Status: Verlangsamt ×1,3, Verflucht +20, Ungehorsam ×1,4 (CANON §18). */
	constexpr int32 EffectiveCost(int32 TimeCost, bool bSlowed, bool bCursed, bool bDisobedient)
	{
		int32 C = TimeCost;
		if (bSlowed) C = C * 13 / 10;
		if (bDisobedient) C = C * 14 / 10;
		return C + (bCursed ? 20 : 0);
	}

	static_assert(Delay(100, 100) == 100, "Referenz: Standardzug bei GES 100");
	static_assert(Delay(100, 394) == 50, "Kernwert-Maximum");
	static_assert(Delay(200, 1) == 298, "Langsamstes Crescendo");
	static_assert(Delay(10, 394) == MinDelay, "Mindestverzögerung");
}

/** Ein Teilnehmer auf der Zeitleiste. */
struct GF_COMBAT_API FTimelineEntry
{
	int32 CombatantId = INDEX_NONE;
	uint8 Side = 0;
	int32 SpeedEff = 0;
	int32 NextTick = 0;
	int32 ExternalDelayThisTurn = 0;
	int32 PendingResolveTick = INDEX_NONE; ///< Aufladung/Crescendo-Ankündigung
	bool bActive = true;
};

/** Ereignis-Warteschlange mit Gleichstandsregel (GES ↓, Seitenwechsel, PCG). */
class GF_COMBAT_API FResonanceTimeline
{
public:
	explicit FResonanceTimeline(const FAethrisRandom& InRng) : Rng(InRng) {}

	void Join(int32 CombatantId, uint8 Side, int32 SpeedEff, bool bAmbush);
	/** Nächster Teilnehmer; setzt Now auf dessen Tick. */
	int32 PopNext();
	void Commit(int32 CombatantId, int32 EffectiveCost);
	/** Fremdverzögerung mit Deckel; gibt tatsächlich angewendete Ticks zurück. */
	int32 PushBack(int32 CombatantId, int32 Ticks);
	void PullForward(int32 CombatantId, int32 Ticks);
	/** Vorgriff: Prioritätsfähigkeit vor dem eigenen Zug (Fenster 25 × Stufe). */
	bool CanVorgriff(int32 CombatantId, int32 Priority) const;
	/** Aufladung/Crescendo: Auflösung bei Now + Delay(Kosten); danach Nachklang-Zug. */
	void Announce(int32 CombatantId, int32 TimeCost);
	/** DR-06: Vorschau der nächsten N Züge, optional mit hypothetischer Aktion des aktuellen Teilnehmers. */
	void Preview(TArray<TPair<int32, int32>>& Out, int32 Count = 8, int32 HypotheticalCost = INDEX_NONE) const;

	int32 Now() const { return NowTick; }
	int32 Round() const { return NowTick / Aethris::Timeline::RoundTicks; }

private:
	FTimelineEntry* Find(int32 CombatantId);
	const FTimelineEntry* Find(int32 CombatantId) const;

	TArray<FTimelineEntry> Entries;
	FAethrisRandom Rng;
	int32 NowTick = 0;
	int32 CurrentId = INDEX_NONE;
	uint8 LastSide = 255;
};
