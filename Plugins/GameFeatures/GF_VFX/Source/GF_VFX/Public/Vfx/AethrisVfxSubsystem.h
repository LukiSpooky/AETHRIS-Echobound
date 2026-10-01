// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "Subsystems/WorldSubsystem.h"
#include "Vfx/AethrisVfxTypes.h"
#include "AethrisVfxSubsystem.generated.h"

class UNiagaraSystem;
class UNiagaraComponent;

/**
 * Zentrale VFX-Steuerung (K58 §8–§9): Budgets je Kategorie, Significance, Pooling, Effektdichte, Blitzbegrenzung.
 * Gameplay ruft nie direkt `SpawnSystemAtLocation`, sondern `RequestEffect`; Kategorien über Budget werden
 * gedrosselt (nicht Pflicht) oder durch die Low-Variante ersetzt (Pflicht: Treffer-Lesbarkeit, Status-Onset).
 */
UCLASS()
class GF_VFX_API UAethrisVfxSubsystem : public UWorldSubsystem
{
	GENERATED_BODY()
public:
	/** Fordert einen Effekt an. Gibt nullptr zurück, wenn er wegen Budget/Significance entfällt. */
	UNiagaraComponent* RequestEffect(EAethrisVfxCategory Category, UNiagaraSystem* System, const FTransform& Where,
	                                 const FAethrisAbilityVfxParams& Params, bool bMandatory = false);

	/** Meldet eine Helligkeitsspitze an; liefert den Helligkeitsfaktor (0 = unterdrückt). */
	float RequestFlash();

	/** Story-Setpiece aktiv: andere Kategorien werden halbiert (VfxBudgets.csv, VFX_STORY). */
	void SetStorySetpieceActive(bool bActive) { bStoryActive = bActive; }

	void SetBudget(EAethrisVfxCategory Category, const FAethrisVfxBudget& Budget);
	void SetIntensityPercent(int32 Percent) { IntensityPercent = FMath::Clamp(Percent, 40, 100); }
	void SetReduceMotion(bool bReduce) { bReduceMotion = bReduce; }

	/** Füllgrad 0–1 der Kategorie (geschätzte aktive Partikel / Budget). */
	float GetBudgetFill(EAethrisVfxCategory Category) const;

private:
	FAethrisVfxBudget Budgets[(int32)EAethrisVfxCategory::Count];
	/** Geschätzte aktive Partikel je Kategorie; pro Frame aus den registrierten Komponenten aktualisiert (Niagara-Statistik). */
	int32 ActiveParticles[(int32)EAethrisVfxCategory::Count] = {};
	int32 IntensityPercent = 100;
	bool bReduceMotion = false;
	bool bStoryActive = false;
	double LastFlashSec = -1.0;
};
