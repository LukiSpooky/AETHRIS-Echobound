// Copyright AETHRIS Team.
#pragma once

#include "UObject/Interface.h"
#include "BondingService.generated.h"

UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class UBondingService : public UInterface { GENERATED_BODY() };

/** Vertrag der Resonanzbindung (implementiert in GF_Capture, K36). */
class AETHRISCORE_API IBondingService
{
	GENERATED_BODY()
public:
	/** Vorschau der Bindungschance in Promille für UI und KI (K36). */
	virtual int32 PreviewBondChancePermille(const FGuid& WildEchoId, FPrimaryAssetId SealItem) const = 0;

	/** Startet die Anschlag-Phase; Ergebnis kommt als Event.Echo.Bonded oder Event.Bond.Failed. */
	virtual bool BeginStrikePhase(const FGuid& WildEchoId, FPrimaryAssetId SealItem, bool bFromCombat) = 0;
};
