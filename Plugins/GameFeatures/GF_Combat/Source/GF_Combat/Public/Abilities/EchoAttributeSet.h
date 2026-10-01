// Copyright AETHRIS Team.
#pragma once

#include "AttributeSet.h"
#include "AbilitySystemComponent.h"
#include "EchoAttributeSet.generated.h"

#define AETHRIS_ATTRIBUTE_ACCESSORS(ClassName, PropertyName) \
	GAMEPLAYATTRIBUTE_PROPERTY_GETTER(ClassName, PropertyName) \
	GAMEPLAYATTRIBUTE_VALUE_GETTER(PropertyName) \
	GAMEPLAYATTRIBUTE_VALUE_SETTER(PropertyName) \
	GAMEPLAYATTRIBUTE_VALUE_INITTER(PropertyName)

/**
 * GAS-Attribute eines kämpfenden Echos (K06 §6). Werte werden zu Kampfbeginn aus FEchoInstance
 * berechnet (K18) und am Kampfende zurückgeschrieben (nur CurrentHP und dauerhafte Zustände).
 * GAS speichert Attribute als float; die Kampflogik liest sie gerundet als Ganzzahl (CS-14) –
 * Modifikatoren sind ausschließlich additive Ganzzahlen oder Stufen (Buff-Stufen, K32).
 */
UCLASS()
class GF_COMBAT_API UEchoAttributeSet : public UAttributeSet
{
	GENERATED_BODY()
public:
	UPROPERTY() FGameplayAttributeData CurrentHP;   AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, CurrentHP)
	UPROPERTY() FGameplayAttributeData MaxHP;       AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, MaxHP)
	UPROPERTY() FGameplayAttributeData Attack;      AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, Attack)
	UPROPERTY() FGameplayAttributeData Defense;     AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, Defense)
	UPROPERTY() FGameplayAttributeData SpAttack;    AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, SpAttack)
	UPROPERTY() FGameplayAttributeData SpDefense;   AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, SpDefense)
	UPROPERTY() FGameplayAttributeData Speed;       AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, Speed)
	UPROPERTY() FGameplayAttributeData Precision;   AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, Precision)
	UPROPERTY() FGameplayAttributeData Evasion;     AETHRIS_ATTRIBUTE_ACCESSORS(UEchoAttributeSet, Evasion)

	virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;
};
