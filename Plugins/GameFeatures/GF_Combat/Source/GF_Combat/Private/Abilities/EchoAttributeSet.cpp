// Copyright AETHRIS Team.
#include "Abilities/EchoAttributeSet.h"

void UEchoAttributeSet::PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue)
{
	Super::PreAttributeChange(Attribute, NewValue);
	// HP nie unter 0 oder über Maximum; alle Werte ganzzahlig (CS-14).
	if (Attribute == GetCurrentHPAttribute())
	{
		NewValue = FMath::Clamp(FMath::RoundToFloat(NewValue), 0.f, GetMaxHP());
	}
	else
	{
		NewValue = FMath::Max(1.f, FMath::RoundToFloat(NewValue));
	}
}
