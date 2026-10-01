// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisSessionTypes.generated.h"

/** Online-Modi (`Data/Online/ModeTopology.csv`, K59 §2). */
UENUM(BlueprintType)
enum class EAethrisOnlineMode : uint8
{
	Coop, Raid, PvpCasual, PvpRanked, Trade, Friends, Events, PhotoShare
};

/** Sitzungszustände (K59 §6). Übergänge nur über UAethrisSessionSubsystem; jeder Wechsel sendet Event.Online.SessionChanged. */
UENUM(BlueprintType)
enum class EAethrisSessionState : uint8
{
	Offline,          ///< Kein Backend; Solo-Weltspiel vollständig (CANON §8.3)
	Connecting,       ///< Anmeldung Plattform-Konto → Aethris-Konto
	OnlineIdle,       ///< Präsenz, Freunde, Tausch, Events verfügbar
	Hosting,          ///< Koop: eigene Welt als Listen-Server
	JoiningHost,      ///< Koop: Gast lädt Host-Welt (Weltseed, Zustands-Snapshot)
	InGuestWorld,     ///< Koop: Gast in fremder Welt
	Matchmaking,      ///< Raid/PvP-Suche
	InDedicatedMatch, ///< Raid/PvP auf Dedicated Server
	Reconnecting,     ///< Verbindungsverlust; Fenster 60 s (PvP: Zugtimer läuft weiter)
	Returning         ///< Rückkehr in die eigene Welt (Gast-Protokoll anwenden)
};

/** Was ein Gast aus einer fremden Welt mitnimmt (K59 §6.4; Story-Frage Q4 entscheidet K60). */
USTRUCT(BlueprintType)
struct GF_MULTIPLAYER_API FAethrisGuestLedgerEntry
{
	GENERATED_BODY()

	UPROPERTY() FName Kind;              ///< Item | Echo | Experience | KodexEntry | Sol | Reputation
	UPROPERTY() FName Id;                ///< ItemId / SpeciesId / FactionId …
	UPROPERTY() int32 Amount = 0;
	UPROPERTY() FGuid InstanceId;        ///< bei Echos: Instanz (mit Ursprung „Koop-Welt des Hosts“)
	UPROPERTY() int64 HostSignature = 0; ///< vom Host signiert, beim Zurückkehren geprüft
};

namespace Aethris::Session
{
	/** Erlaubte Zustandsübergänge (Tabelle K59 §6.1). */
	GF_MULTIPLAYER_API bool IsTransitionAllowed(EAethrisSessionState From, EAethrisSessionState To);

	/** Wiederverbindungsfenster in Sekunden je Modus (Koop 120, Raid 90, PvP 60, sonst 0). */
	GF_MULTIPLAYER_API int32 ReconnectWindowSec(EAethrisOnlineMode Mode);
}
