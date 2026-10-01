// Copyright AETHRIS Team.
#pragma once

#include "AbilitySystemComponent.h"
#include "Math/AethrisRandom.h"
#include "EchoAbilitySystemComponent.generated.h"

/** Kontext eines Zuges – wird von der Zeitleiste (K31) gefüllt und an die Fähigkeit übergeben. */
USTRUCT(BlueprintType)
struct GF_COMBAT_API FEchoTurnContext
{
	GENERATED_BODY()
	UPROPERTY() int64 Tick = 0;                          // Zeitpunkt auf der Zeitleiste
	UPROPERTY() TArray<TObjectPtr<AActor>> Targets;      // gewählte Ziele
	UPROPERTY() FGameplayTag Weather;                    // aktuelles Wetter
	UPROPERTY() FGameplayTagContainer Terrain;           // aktive Feldzustände
	FAethrisRandom* Rng = nullptr;                       // Kampf-RNG (deterministisch), nie null während Ausführung
};

/**
 * Rundenbasierter Wrapper um GAS (CANON §9, ADR-032).
 *
 * GAS ist für Echtzeit mit Client-Prediction gebaut. Wir nutzen GAS als Daten- und Effekt-Framework
 * (Attribute, GameplayEffects für Status/Buffs, Tags, Cues für VFX/SFX), aber NICHT seine
 * Aktivierungs- und Prediction-Pipeline für die Spiellogik:
 *  - Aktivierung erfolgt ausschließlich durch die Zeitleiste über ExecuteTurnAbility().
 *  - Ausführung ist synchron und serverautoritativ; Clients erhalten das Ergebnis (K59).
 *  - Dauerangaben von Effekten sind in Zügen/Ticks, nicht in Sekunden (Duration-Policy „Infinite“
 *    + Entfernen durch die Zeitleiste).
 */
UCLASS(ClassGroup=(Aethris), meta=(BlueprintSpawnableComponent))
class GF_COMBAT_API UEchoAbilitySystemComponent : public UAbilitySystemComponent
{
	GENERATED_BODY()
public:
	UEchoAbilitySystemComponent();

	/**
	 * Führt eine Fähigkeit als Zug aus. Liefert die Zeitkosten in Ticks (K31), die die Zeitleiste
	 * für die nächste Aktivierung dieses Echos verwendet. Fehlschlag (z. B. blockiert) liefert die
	 * Mindestkosten – DR-10: kein Zug ist verschwendet, der Aufrufer vergibt Harmonie.
	 */
	int32 ExecuteTurnAbility(FGameplayAbilitySpecHandle Ability, const FEchoTurnContext& Context);

	/** Rundet ein Attribut deterministisch auf Ganzzahl (CS-14). */
	int32 GetIntAttribute(const FGameplayAttribute& Attribute) const;

	/** Zählt Zug-basierte Effektdauern herunter und entfernt abgelaufene Effekte (vom Zug-Ende aufgerufen). */
	void AdvanceTurnDurations();
};
