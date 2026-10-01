// Copyright AETHRIS Team.
#pragma once

#include "Subsystems/GameInstanceSubsystem.h"
#include "GameplayTagContainer.h"
#include "StructUtils/InstancedStruct.h"
#include "AethrisEventBus.generated.h"

/** Wie ein Listener auf Kanäle reagiert (K06 §4.2). */
UENUM()
enum class EAethrisEventMatch : uint8
{
	/** Nur exakt dieser Kanal. */
	Exact,
	/** Dieser Kanal und alle Unterkanäle (z. B. Event.Combat hört Event.Combat.Ended). */
	Partial
};

/** Handle zum Abmelden eines Listeners. Ungültig nach Unregister. */
USTRUCT()
struct AETHRISCORE_API FAethrisEventHandle
{
	GENERATED_BODY()

	bool IsValid() const { return Id != 0; }

	UPROPERTY() FGameplayTag Channel;
	UPROPERTY() uint64 Id = 0;
};

/**
 * Projektweiter Event-Bus (CANON §26). Einziger erlaubter Weg, wie Feature-Plugins
 * einander benachrichtigen. Nachrichten sind beliebige USTRUCTs (typsicher über Templates),
 * Kanäle sind GameplayTags unter "Event.".
 *
 * Eigenschaften:
 *  - Synchrone Zustellung (Broadcast) oder verzögert am Frame-Ende (BroadcastDeferred),
 *    letzteres verhindert Re-Entrancy-Probleme in Kampf- und Quest-Logik.
 *  - Listener werden während der Zustellung sicher hinzugefügt/entfernt (Kopie der Liste).
 *  - Typprüfung: Ein Listener für FMsgA erhält keine Nachricht vom Typ FMsgB (Warnung im Log).
 *  - Bewusst nicht netzwerkfähig: Replikation ist Aufgabe der Features (K59).
 */
UCLASS()
class AETHRISCORE_API UAethrisEventBus : public UGameInstanceSubsystem
{
	GENERATED_BODY()

public:
	/** Bequemer Zugriff aus jedem UObject mit World-Kontext. */
	static UAethrisEventBus& Get(const UObject* WorldContext);

	/** Sendet sofort an alle passenden Listener. */
	template <typename TMessage>
	void Broadcast(FGameplayTag Channel, const TMessage& Message)
	{
		BroadcastInternal(Channel, FInstancedStruct::Make(Message));
	}

	/** Reiht die Nachricht ein; Zustellung am Ende des aktuellen Frames (FIFO). */
	template <typename TMessage>
	void BroadcastDeferred(FGameplayTag Channel, const TMessage& Message)
	{
		Deferred.Emplace(Channel, FInstancedStruct::Make(Message));
		ScheduleDeferredFlush();
	}

	/**
	 * Registriert einen Listener. Der Callback erhält die Nachricht als const-Referenz.
	 * Owner: wird schwach gehalten; ist er zerstört, wird der Listener automatisch übersprungen und entfernt.
	 */
	template <typename TMessage>
	FAethrisEventHandle Register(FGameplayTag Channel, const UObject* Owner,
		TFunction<void(FGameplayTag, const TMessage&)>&& Callback,
		EAethrisEventMatch Match = EAethrisEventMatch::Exact)
	{
		auto Thunk = [Cb = MoveTemp(Callback)](FGameplayTag ActualChannel, const FInstancedStruct& Payload)
		{
			if (const TMessage* Msg = Payload.GetPtr<TMessage>())
			{
				Cb(ActualChannel, *Msg);
			}
		};
		return RegisterInternal(Channel, Owner, TBaseStructure<TMessage>::Get(), MoveTemp(Thunk), Match);
	}

	/** Meldet einen Listener ab. Mehrfaches Abmelden ist harmlos. */
	void Unregister(FAethrisEventHandle& Handle);

	/** Anzahl der Listener (Debug/Tests). */
	int32 NumListeners() const;

	// UGameInstanceSubsystem
	virtual void Deinitialize() override;

private:
	using FThunk = TFunction<void(FGameplayTag, const FInstancedStruct&)>;

	struct FListener
	{
		uint64 Id = 0;
		TWeakObjectPtr<const UObject> Owner;
		bool bHasOwner = false;
		const UScriptStruct* Type = nullptr;
		EAethrisEventMatch Match = EAethrisEventMatch::Exact;
		FThunk Thunk;
	};

	void BroadcastInternal(FGameplayTag Channel, const FInstancedStruct& Payload);
	FAethrisEventHandle RegisterInternal(FGameplayTag Channel, const UObject* Owner,
		const UScriptStruct* Type, FThunk&& Thunk, EAethrisEventMatch Match);
	void ScheduleDeferredFlush();
	void FlushDeferred();

	TMap<FGameplayTag, TArray<FListener>> ListenersByChannel;
	TArray<TPair<FGameplayTag, FInstancedStruct>> Deferred;
	uint64 NextId = 1;
	bool bFlushScheduled = false;
	int32 BroadcastDepth = 0;
};
