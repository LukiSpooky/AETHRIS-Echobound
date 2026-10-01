// Copyright AETHRIS Team.
#include "Abilities/EchoAbilitySystemComponent.h"
#include "AethrisLog.h"

UEchoAbilitySystemComponent::UEchoAbilitySystemComponent()
{
	// Kein Tick, keine Prediction: Zeitleiste steuert alles (ADR-032).
	PrimaryComponentTick.bCanEverTick = false;
	SetIsReplicated(true);
	ReplicationMode = EGameplayEffectReplicationMode::Minimal;
}

int32 UEchoAbilitySystemComponent::GetIntAttribute(const FGameplayAttribute& Attribute) const
{
	// Attribute enthalten durch die Modifikator-Regeln stets ganzzahlige Werte; Rundung nur als Schutz.
	return FMath::RoundToInt(GetNumericAttribute(Attribute));
}

int32 UEchoAbilitySystemComponent::ExecuteTurnAbility(FGameplayAbilitySpecHandle Ability, const FEchoTurnContext& Context)
{
	check(Context.Rng);
	TRACE_CPUPROFILER_EVENT_SCOPE(EchoASC_ExecuteTurnAbility);
	// Vollständige Implementierung in K31 (Zeitleiste) und K32 (Schaden/Status).
	UE_LOG(LogAethrisCombat, Verbose, TEXT("ExecuteTurnAbility @Tick %lld"), Context.Tick);
	return 100;
}

void UEchoAbilitySystemComponent::AdvanceTurnDurations()
{
	// Implementierung in K32 (Statusdauern in Zügen).
}
