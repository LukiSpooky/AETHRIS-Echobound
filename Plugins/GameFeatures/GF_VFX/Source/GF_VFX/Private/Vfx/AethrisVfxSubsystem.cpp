// Copyright AETHRIS Team.
#include "Vfx/AethrisVfxSubsystem.h"
#include "NiagaraComponent.h"
#include "NiagaraFunctionLibrary.h"
#include "NiagaraSystem.h"

void UAethrisVfxSubsystem::SetBudget(EAethrisVfxCategory Category, const FAethrisVfxBudget& Budget)
{
	Budgets[(int32)Category] = Budget;
}

float UAethrisVfxSubsystem::GetBudgetFill(EAethrisVfxCategory Category) const
{
	const int32 Idx = (int32)Category;
	int32 Max = Budgets[Idx].MaxParticles;
	if (bStoryActive && Category != EAethrisVfxCategory::Story && Category != EAethrisVfxCategory::UI3D)
	{
		Max /= 2;   // Story-Setpiece: andere Kategorien halbiert
	}
	return Max > 0 ? float(ActiveParticles[Idx]) / float(Max) : 1.f;
}

UNiagaraComponent* UAethrisVfxSubsystem::RequestEffect(EAethrisVfxCategory Category, UNiagaraSystem* System,
                                                       const FTransform& Where, const FAethrisAbilityVfxParams& Params, bool bMandatory)
{
	if (!System)
	{
		return nullptr;
	}
	// UI-Markierungen sind von der Effektdichte ausgenommen (Lesbarkeit, ACC_VFX_INTENSITY).
	const int32 Intensity = Category == EAethrisVfxCategory::UI3D ? 100 : IntensityPercent;
	const int32 Spawn = Aethris::Vfx::ScaleSpawnCount(1000, Intensity, GetBudgetFill(Category), bMandatory);
	if (Spawn <= 0)
	{
		return nullptr;
	}
	UNiagaraComponent* Comp = UNiagaraFunctionLibrary::SpawnSystemAtLocation(
		GetWorld(), System, Where.GetLocation(), Where.Rotator(), Where.GetScale3D() * Params.Scale,
		/*bAutoDestroy*/ true, /*bAutoActivate*/ true, ENCPoolMethod::AutoRelease);
	if (Comp)
	{
		Comp->SetVariableLinearColor(TEXT("User.TypeColor"), Params.TypeColor);
		Comp->SetVariableFloat(TEXT("User.SpawnScale"), Spawn / 1000.f);
		Comp->SetVariableFloat(TEXT("User.Smoke"), Params.SmokePermille / 1000.f);
		Comp->SetVariableInt(TEXT("User.QuartzBeat"), Params.QuartzBeat);
	}
	return Comp;
}

float UAethrisVfxSubsystem::RequestFlash()
{
	const double Now = GetWorld() ? GetWorld()->GetRealTimeSeconds() : 0.0;
	if (!Aethris::Vfx::AllowFlash(Now, LastFlashSec))
	{
		return 0.f;
	}
	LastFlashSec = Now;
	return Aethris::Vfx::FlashIntensity(bReduceMotion);
}
