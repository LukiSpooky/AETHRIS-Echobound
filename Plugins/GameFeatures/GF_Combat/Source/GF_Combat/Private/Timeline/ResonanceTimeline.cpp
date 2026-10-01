// Copyright AETHRIS Team.
#include "Timeline/ResonanceTimeline.h"

using namespace Aethris::Timeline;

void FResonanceTimeline::Join(int32 CombatantId, uint8 Side, int32 SpeedEff, bool bAmbush)
{
	FTimelineEntry& E = Entries.AddDefaulted_GetRef();
	E.CombatantId = CombatantId;
	E.Side = Side;
	E.SpeedEff = SpeedEff;
	// Startzug: Standardaktion × 850–1000 ‰ (gedeckelter Zufall, DR-07); Hinterhalt −200 ‰ (DR-14)
	const int32 Jitter = static_cast<int32>(Rng.RangeInclusive(850, 1000)) - (bAmbush ? 200 : 0);
	E.NextTick = NowTick + FMath::Max(1, Delay(100, SpeedEff) * Jitter / 1000);
}

int32 FResonanceTimeline::PopNext()
{
	auto TickOf = [](const FTimelineEntry& E) { return E.PendingResolveTick != INDEX_NONE ? E.PendingResolveTick : E.NextTick; };
	int32 T = MAX_int32;
	for (const FTimelineEntry& E : Entries) if (E.bActive) T = FMath::Min(T, TickOf(E));
	// Gleichstand: 1) höhere GES, 2) Seite, die zuletzt NICHT gehandelt hat, 3) PCG unter den verbleibenden (Python-Parität)
	TArray<FTimelineEntry*> Tied;
	for (FTimelineEntry& E : Entries) if (E.bActive && TickOf(E) == T) Tied.Add(&E);
	Tied.StableSort([this](const FTimelineEntry& A, const FTimelineEntry& B)
	{
		if (A.SpeedEff != B.SpeedEff) return A.SpeedEff > B.SpeedEff;
		return (A.Side != LastSide) && (B.Side == LastSide);
	});
	int32 Equal = 1;
	while (Equal < Tied.Num() && Tied[Equal]->SpeedEff == Tied[0]->SpeedEff && (Tied[Equal]->Side == LastSide) == (Tied[0]->Side == LastSide)) ++Equal;
	FTimelineEntry* Best = Tied[Equal > 1 ? static_cast<int32>(Rng.NextBounded(static_cast<uint32>(Equal))) : 0];
	NowTick = T;
	LastSide = Best->Side;
	Best->ExternalDelayThisTurn = 0;
	CurrentId = Best->CombatantId;
	return CurrentId;
}

void FResonanceTimeline::Commit(int32 CombatantId, int32 EffectiveCost)
{
	if (FTimelineEntry* E = Find(CombatantId))
	{
		E->NextTick = NowTick + Delay(EffectiveCost, E->SpeedEff);
	}
}

int32 FResonanceTimeline::PushBack(int32 CombatantId, int32 Ticks)
{
	FTimelineEntry* E = Find(CombatantId);
	if (!E) return 0;
	const int32 Room = FMath::Max(0, ExternalDelayCap - E->ExternalDelayThisTurn);
	const int32 D = FMath::Min(Ticks, Room);
	if (E->PendingResolveTick != INDEX_NONE) E->PendingResolveTick += D; else E->NextTick += D;
	E->ExternalDelayThisTurn += D;
	return D;
}

void FResonanceTimeline::PullForward(int32 CombatantId, int32 Ticks)
{
	if (FTimelineEntry* E = Find(CombatantId))
	{
		E->NextTick = FMath::Max(NowTick + 1, E->NextTick - Ticks);
	}
}

bool FResonanceTimeline::CanVorgriff(int32 CombatantId, int32 Priority) const
{
	const FTimelineEntry* E = Find(CombatantId);
	return E && E->bActive && E->PendingResolveTick == INDEX_NONE && Priority > 0
		&& E->NextTick - NowTick <= VorgriffPerPriority * Priority;
}

void FResonanceTimeline::Announce(int32 CombatantId, int32 TimeCost)
{
	if (FTimelineEntry* E = Find(CombatantId))
	{
		E->PendingResolveTick = NowTick + Delay(TimeCost, E->SpeedEff);
		E->NextTick = E->PendingResolveTick + Delay(ChargeRecoveryCost, E->SpeedEff);
	}
}

void FResonanceTimeline::Preview(TArray<TPair<int32, int32>>& Out, int32 Count, int32 HypotheticalCost) const
{
	TArray<FTimelineEntry> Sim = Entries;
	if (HypotheticalCost != INDEX_NONE)
	{
		for (FTimelineEntry& E : Sim) if (E.CombatantId == CurrentId) E.NextTick = NowTick + Delay(HypotheticalCost, E.SpeedEff);
	}
	Out.Reset();
	while (Out.Num() < Count)
	{
		FTimelineEntry* Best = nullptr;
		for (FTimelineEntry& E : Sim) if (E.bActive && (!Best || E.NextTick < Best->NextTick || (E.NextTick == Best->NextTick && E.SpeedEff > Best->SpeedEff))) Best = &E;
		if (!Best) break;
		Out.Emplace(Best->NextTick, Best->CombatantId);
		Best->NextTick += Delay(100, Best->SpeedEff);
	}
}

FTimelineEntry* FResonanceTimeline::Find(int32 CombatantId)
{
	return Entries.FindByPredicate([CombatantId](const FTimelineEntry& E) { return E.CombatantId == CombatantId; });
}

const FTimelineEntry* FResonanceTimeline::Find(int32 CombatantId) const
{
	return Entries.FindByPredicate([CombatantId](const FTimelineEntry& E) { return E.CombatantId == CombatantId; });
}
