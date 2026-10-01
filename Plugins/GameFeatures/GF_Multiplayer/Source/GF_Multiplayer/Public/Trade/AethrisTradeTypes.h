// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisTradeTypes.generated.h"

/** Zustände einer Tausch-Transaktion (Treuhand, K60 §4.3). Server-autoritativ; Client zeigt nur an. */
UENUM(BlueprintType)
enum class EAethrisTradeState : uint8
{
	Draft,           ///< Angebot wird zusammengestellt (lokal)
	Validating,      ///< Legalitätsprüfung + Signatur (K59 §9.3)
	AwaitingPartner, ///< Direkttausch: Gegenseite stellt zusammen · Börse: wartet auf Kreis
	Review,          ///< beide Seiten sehen alles; Halten 3 s zum Bestätigen (UX-06)
	Escrow,          ///< beide bestätigt; Server hält alle Teile
	Completed,       ///< atomar übertragen, Spielstände aktualisiert
	Cancelled,       ///< abgebrochen; alles zurück
	Rejected         ///< Legalität/Regel verletzt (TR-xx), Begründung an Client
};

/** Ein Teil eines Tauschs (Echo oder Gegenstand aus der Tauschliste). */
USTRUCT(BlueprintType)
struct GF_MULTIPLAYER_API FAethrisTradeItem
{
	GENERATED_BODY()

	UPROPERTY() FGuid EchoInstanceId;     ///< gesetzt bei Echos
	UPROPERTY() FName ItemId;             ///< gesetzt bei Gegenständen (Ressource, Gericht, Lockmittel)
	UPROPERTY() int32 Count = 0;          ///< Gegenstände: 1–20 gesamt je Seite (TR-01)
};

/** Angebot auf der Klangbörse (TR-07): ein Echo + Wunschliste (bis 3 Arten). */
USTRUCT(BlueprintType)
struct GF_MULTIPLAYER_API FAethrisBoardOffer
{
	GENERATED_BODY()

	UPROPERTY() FGuid OfferId;
	UPROPERTY() FGuid EchoInstanceId;
	UPROPERTY() FName OfferedSpecies;
	UPROPERTY() TArray<FName> WantedSpecies;   ///< 1–3
	UPROPERTY() int32 MinLevel = 1;
	UPROPERTY() bool bWantMorph = false;
	UPROPERTY() FDateTime ExpiresUtc;          ///< Laufzeit 72 h
};

namespace Aethris::Trade
{
	inline constexpr int32 MaxEchosPerSide = 3;
	inline constexpr int32 MaxItemsPerSide = 20;
	inline constexpr int32 RetradeLockHours = 24;
	inline constexpr int32 MaxActiveBoardOffers = 3;
	inline constexpr int32 MaxBoardTradesPerDay = 5;
	inline constexpr int32 MaxDirectTradesPerDay = 30;

	/** Erlaubte Zustandsübergänge der Treuhand. */
	GF_MULTIPLAYER_API bool IsTransitionAllowed(EAethrisTradeState From, EAethrisTradeState To);
}
