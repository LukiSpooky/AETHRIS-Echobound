// Copyright AETHRIS Team.
#include "Services/AethrisServiceLocator.h"
#include "Engine/GameInstance.h"
#include "Engine/World.h"

UAethrisServiceLocator& UAethrisServiceLocator::Get(const UObject* WorldContext)
{
	const UWorld* World = WorldContext ? WorldContext->GetWorld() : nullptr;
	UGameInstance* GI = World ? World->GetGameInstance() : nullptr;
	check(GI);
	return *GI->GetSubsystem<UAethrisServiceLocator>();
}
