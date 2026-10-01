// Copyright AETHRIS Team.
#pragma once

#include "Subsystems/GameInstanceSubsystem.h"
#include "AethrisTelemetry.generated.h"

/** Ein Telemetrie-Ereignis (Namensschema domain.object.verb, K04 §7). */
USTRUCT()
struct AETHRISCORE_API FAethrisTelemetryEvent
{
	GENERATED_BODY()
	UPROPERTY() FName Name;                         // z. B. combat.end
	UPROPERTY() TMap<FName, FString> Attributes;    // flache Schlüssel/Werte
	UPROPERTY() double SessionSeconds = 0.0;
};

/**
 * Sammelt Telemetrie (nur mit Opt-in, DSGVO) und gibt sie gebündelt an registrierte Senken weiter
 * (Datei im Playtest-Labor, HTTP-Ingest im Live-Betrieb). Gameplay-Code ruft nur Record().
 */
UCLASS()
class AETHRISCORE_API UAethrisTelemetrySubsystem : public UGameInstanceSubsystem
{
	GENERATED_BODY()
public:
	void Record(FName EventName, TMap<FName, FString> Attributes);
	void SetOptIn(bool bInOptIn) { bOptIn = bInOptIn; }
	/** Senken (Interface in K06 §8) werden von Plattform-/Online-Modulen registriert. */
	void AddSink(TFunction<void(TConstArrayView<FAethrisTelemetryEvent>)> Sink) { Sinks.Add(MoveTemp(Sink)); }
	/** Puffer leeren (alle 30 s, beim Speichern, beim Beenden). */
	void Flush();

private:
	TArray<FAethrisTelemetryEvent> Buffer;
	TArray<TFunction<void(TConstArrayView<FAethrisTelemetryEvent>)>> Sinks;
	bool bOptIn = false;
};
