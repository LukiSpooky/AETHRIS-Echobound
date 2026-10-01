// Copyright AETHRIS Team.
#include "Events/AethrisEventBus.h"
#include "AethrisLog.h"
#include "Engine/GameInstance.h"
#include "Engine/World.h"
#include "Containers/Ticker.h"

namespace
{
	/** Schutz gegen Endlosschleifen durch Events, die sich gegenseitig auslösen. */
	constexpr int32 MaxBroadcastDepth = 16;
}

UAethrisEventBus& UAethrisEventBus::Get(const UObject* WorldContext)
{
	const UWorld* World = WorldContext ? WorldContext->GetWorld() : nullptr;
	UGameInstance* GI = World ? World->GetGameInstance() : nullptr;
	check(GI); // Programmierfehler: Event-Bus ohne GameInstance ist nicht vorgesehen (CS-11).
	return *GI->GetSubsystem<UAethrisEventBus>();
}

void UAethrisEventBus::BroadcastInternal(FGameplayTag Channel, const FInstancedStruct& Payload)
{
	TRACE_CPUPROFILER_EVENT_SCOPE(AethrisEventBus_Broadcast);

	if (!ensureMsgf(BroadcastDepth < MaxBroadcastDepth,
		TEXT("Event-Rekursion > %d bei Kanal %s – Event-Kette prüfen"), MaxBroadcastDepth, *Channel.ToString()))
	{
		return;
	}
	TGuardValue<int32> DepthGuard(BroadcastDepth, BroadcastDepth + 1);

	// Vom konkreten Kanal aufwärts laufen: Event.Combat.Ended -> Event.Combat -> Event
	bool bIsExactLevel = true;
	for (FGameplayTag Current = Channel; Current.IsValid(); Current = Current.RequestDirectParent())
	{
		if (TArray<FListener>* Found = ListenersByChannel.Find(Current))
		{
			// Kopie: Listener dürfen sich während der Zustellung an-/abmelden.
			const TArray<FListener> Snapshot = *Found;
			for (const FListener& L : Snapshot)
			{
				if (!bIsExactLevel && L.Match == EAethrisEventMatch::Exact)
				{
					continue;
				}
				if (L.bHasOwner && !L.Owner.IsValid())
				{
					continue; // Owner zerstört – Aufräumen beim nächsten Register/Unregister
				}
				if (L.Type != Payload.GetScriptStruct())
				{
					UE_LOG(LogAethrisEvents, Warning, TEXT("Typkonflikt auf %s: erwartet %s, erhalten %s"),
						*Channel.ToString(), *GetNameSafe(L.Type), *GetNameSafe(Payload.GetScriptStruct()));
					continue;
				}
				L.Thunk(Channel, Payload);
			}
		}
		bIsExactLevel = false;
	}
}

FAethrisEventHandle UAethrisEventBus::RegisterInternal(FGameplayTag Channel, const UObject* Owner,
	const UScriptStruct* Type, FThunk&& Thunk, EAethrisEventMatch Match)
{
	check(Channel.IsValid());
	TArray<FListener>& List = ListenersByChannel.FindOrAdd(Channel);
	List.RemoveAll([](const FListener& L) { return L.bHasOwner && !L.Owner.IsValid(); });

	FListener& L = List.AddDefaulted_GetRef();
	L.Id = NextId++;
	L.Owner = Owner;
	L.bHasOwner = Owner != nullptr;
	L.Type = Type;
	L.Match = Match;
	L.Thunk = MoveTemp(Thunk);

	FAethrisEventHandle Handle;
	Handle.Channel = Channel;
	Handle.Id = L.Id;
	return Handle;
}

void UAethrisEventBus::Unregister(FAethrisEventHandle& Handle)
{
	if (!Handle.IsValid())
	{
		return;
	}
	if (TArray<FListener>* List = ListenersByChannel.Find(Handle.Channel))
	{
		List->RemoveAll([&Handle](const FListener& L) { return L.Id == Handle.Id; });
	}
	Handle = FAethrisEventHandle();
}

int32 UAethrisEventBus::NumListeners() const
{
	int32 Count = 0;
	for (const auto& Pair : ListenersByChannel)
	{
		Count += Pair.Value.Num();
	}
	return Count;
}

void UAethrisEventBus::ScheduleDeferredFlush()
{
	if (bFlushScheduled)
	{
		return;
	}
	bFlushScheduled = true;
	// Einmaliger Ticker: am Ende des aktuellen Frames zustellen.
	FTSTicker::GetCoreTicker().AddTicker(FTickerDelegate::CreateWeakLambda(this, [this](float)
	{
		FlushDeferred();
		return false;
	}));
}

void UAethrisEventBus::FlushDeferred()
{
	bFlushScheduled = false;
	// Nachrichten, die während des Flushs entstehen, landen in der nächsten Runde (kein Starvation-Risiko).
	TArray<TPair<FGameplayTag, FInstancedStruct>> Batch = MoveTemp(Deferred);
	Deferred.Reset();
	for (const auto& Item : Batch)
	{
		BroadcastInternal(Item.Key, Item.Value);
	}
}

void UAethrisEventBus::Deinitialize()
{
	ListenersByChannel.Reset();
	Deferred.Reset();
	Super::Deinitialize();
}
