// Copyright AETHRIS Team.
#include "Data/AethrisDefinition.h"
#include "Misc/DataValidation.h"

EDataValidationResult UDefinitionFragment::ValidateFragment(FDataValidationContext& Context) const
{
	return EDataValidationResult::Valid;
}

#if WITH_EDITOR
EDataValidationResult UAethrisDefinition::IsDataValid(FDataValidationContext& Context) const
{
	EDataValidationResult Result = Super::IsDataValid(Context);
	if (Id.IsNone())
	{
		Context.AddError(NSLOCTEXT("Aethris", "NoId", "Definition ohne Id (K04 §7)."));
		Result = EDataValidationResult::Invalid;
	}
	for (const UDefinitionFragment* F : Fragments)
	{
		if (!F)
		{
			Context.AddError(NSLOCTEXT("Aethris", "NullFragment", "Leeres Fragment in Definition."));
			Result = EDataValidationResult::Invalid;
		}
		else if (F->ValidateFragment(Context) == EDataValidationResult::Invalid)
		{
			Result = EDataValidationResult::Invalid;
		}
	}
	return Result;
}
#endif
