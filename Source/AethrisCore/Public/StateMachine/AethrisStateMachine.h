// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"

/**
 * Leichtgewichtige, tabellengetriebene Zustandsmaschine für Code-Abläufe
 * (Rückklang, Bindungsphasen, Kampfphasen). Für KI → StateTree, für globale Spielzustände →
 * UAethrisGameFlowSubsystem (K06 §5).
 *
 * Eigenschaften: erlaubte Übergänge explizit, Enter/Exit-Callbacks, Übergangs-Guard, keine Heap-
 * Allokation pro Wechsel, deterministisch (Determinismus-Zone-tauglich).
 *
 * Beispiel:
 *   enum class EBondPhase : uint8 { Listen, Approach, Attune, Strike, Done, Count };
 *   TAethrisStateMachine<EBondPhase> Fsm(EBondPhase::Listen);
 *   Fsm.Allow(EBondPhase::Listen, EBondPhase::Approach);
 *   Fsm.OnEnter(EBondPhase::Strike, [this]{ OpenTimingWindow(); });
 *   Fsm.TryTransition(EBondPhase::Approach);
 */
template <typename TStateEnum>
class TAethrisStateMachine
{
	static_assert(TIsEnum<TStateEnum>::Value, "TStateEnum muss ein enum class mit Eintrag 'Count' sein");
	static constexpr int32 N = static_cast<int32>(TStateEnum::Count);

public:
	using FCallback = TFunction<void()>;
	using FGuard = TFunction<bool()>;

	explicit TAethrisStateMachine(TStateEnum Initial) : Current(Initial) {}

	void Allow(TStateEnum From, TStateEnum To, FGuard Guard = nullptr)
	{
		Allowed[Idx(From)][Idx(To)] = true;
		Guards[Idx(From)][Idx(To)] = MoveTemp(Guard);
	}

	void OnEnter(TStateEnum S, FCallback Cb) { Enter[Idx(S)] = MoveTemp(Cb); }
	void OnExit(TStateEnum S, FCallback Cb)  { Exit[Idx(S)] = MoveTemp(Cb); }

	/** Wechselt, falls erlaubt und Guard (falls vorhanden) zustimmt. */
	bool TryTransition(TStateEnum To)
	{
		const int32 F = Idx(Current), T = Idx(To);
		if (!Allowed[F][T] || (Guards[F][T] && !Guards[F][T]()))
		{
			return false;
		}
		if (Exit[F])  { Exit[F](); }
		Previous = Current;
		Current = To;
		if (Enter[T]) { Enter[T](); }
		return true;
	}

	TStateEnum Get() const { return Current; }
	TStateEnum GetPrevious() const { return Previous; }
	bool Is(TStateEnum S) const { return Current == S; }

private:
	static constexpr int32 Idx(TStateEnum S) { return static_cast<int32>(S); }

	TStateEnum Current;
	TStateEnum Previous = Current;
	bool Allowed[N][N] = {};
	FGuard Guards[N][N];
	FCallback Enter[N];
	FCallback Exit[N];
};
