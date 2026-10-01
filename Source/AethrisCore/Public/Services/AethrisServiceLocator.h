// Copyright AETHRIS Team.
#pragma once

#include "Subsystems/GameInstanceSubsystem.h"
#include "UObject/Interface.h"
#include "AethrisServiceLocator.generated.h"

/**
 * Service Locator für Core-Interfaces (CANON §26).
 * Feature-Plugins registrieren beim Aktivieren ihre Implementierung eines in AethrisCore
 * definierten Interfaces; andere Features fragen sie ab, ohne das Plugin zu kennen.
 *
 * Beispiel:
 *   // GF_Capture, beim Aktivieren:
 *   UAethrisServiceLocator::Get(this).Register<IBondingService>(BondingSubsystem);
 *   // GF_Combat:
 *   if (IBondingService* Bonding = UAethrisServiceLocator::Get(this).Find<IBondingService>()) { ... }
 *
 * Ein fehlender Service ist ein gültiger Zustand (Plugin deaktiviert, K05 §4.3) – Aufrufer müssen
 * damit umgehen.
 */
UCLASS()
class AETHRISCORE_API UAethrisServiceLocator : public UGameInstanceSubsystem
{
	GENERATED_BODY()

public:
	static UAethrisServiceLocator& Get(const UObject* WorldContext);

	template <typename TInterface>
	void Register(UObject* Implementation)
	{
		check(Implementation && Implementation->GetClass()->ImplementsInterface(TInterface::UClassType::StaticClass()));
		Services.Add(TInterface::UClassType::StaticClass(), Implementation);
	}

	template <typename TInterface>
	void Unregister(UObject* Implementation)
	{
		const UClass* Key = TInterface::UClassType::StaticClass();
		if (Services.FindRef(Key) == Implementation)
		{
			Services.Remove(Key);
		}
	}

	template <typename TInterface>
	TInterface* Find() const
	{
		UObject* Obj = Services.FindRef(TInterface::UClassType::StaticClass());
		return Obj ? Cast<TInterface>(Obj) : nullptr;
	}

private:
	UPROPERTY() TMap<TObjectPtr<const UClass>, TObjectPtr<UObject>> Services;
};
