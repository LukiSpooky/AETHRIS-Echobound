// Copyright AETHRIS Team.
#pragma once

#include "CoreMinimal.h"
#include "AethrisVfxTypes.generated.h"

/** VFX-Kategorien mit eigenem Budget (`Data/VFX/VfxBudgets.csv`, K58 §8). */
UENUM(BlueprintType)
enum class EAethrisVfxCategory : uint8
{
	Ambient, Weather, Echo, Ability, Crescendo, Status, Terrain, Story, Traversal, UI3D, Count UMETA(Hidden)
};

/** Budget einer Kategorie für die aktive Plattform (aus der CSV importiert). */
USTRUCT(BlueprintType)
struct GF_VFX_API FAethrisVfxBudget
{
	GENERATED_BODY()

	UPROPERTY(EditDefaultsOnly) int32 MaxParticles = 0;
	UPROPERTY(EditDefaultsOnly) float GpuMs = 0.f;
	UPROPERTY(EditDefaultsOnly) int32 MaxOverdraw = 2;
};

/** Parameter, mit denen eine Typ-Vorlage (`NS_Abl_<Kat>_<Form>`) eingefärbt und skaliert wird (K58 §4). */
USTRUCT(BlueprintType)
struct GF_VFX_API FAethrisAbilityVfxParams
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere) FLinearColor TypeColor = FLinearColor::White;   ///< TypeColors.csv, Modus aus ACC_COLORBLIND
	UPROPERTY(EditAnywhere) FName TypeMotif;                                ///< Niagara-Modul je Typ (TypeVfx.csv)
	UPROPERTY(EditAnywhere) float Scale = 1.f;                              ///< 0,6 + Stärke/150, max. 1,6
	UPROPERTY(EditAnywhere) float SmokePermille = 0.f;                      ///< entsättigter Anteil (K56 §3.2)
	UPROPERTY(EditAnywhere) int32 QuartzBeat = -1;                          ///< Trefferzeitpunkt auf Quartz-Schlag (Klang-Typ), -1 = frei
};

namespace Aethris::Vfx
{
	/** Photosensitivität (VFX-04): höchstens 3 Helligkeitsspitzen pro Sekunde, Mindestabstand 1/3 s. */
	inline constexpr double MinFlashIntervalSec = 1.0 / 3.0;

	/**
	 * Entscheidet, ob eine Helligkeitsspitze (Blitz, Bloom-Spitze, Evolutions-Höhepunkt) jetzt erlaubt ist.
	 * LastFlashSec = Zeitpunkt der letzten erlaubten Spitze (negativ = keine). bReduceMotion = ACC_MOTION.
	 * Bei ACC_MOTION werden Spitzen nie verboten, sondern als Helligkeit ≤ 40 % ausgespielt (siehe FlashIntensity).
	 */
	GF_VFX_API bool AllowFlash(double NowSec, double LastFlashSec);

	/** Helligkeitsfaktor einer erlaubten Spitze: 1,0 normal, 0,4 bei Bewegungsreduktion. */
	GF_VFX_API float FlashIntensity(bool bReduceMotion);

	/**
	 * Partikelanzahl nach Effektdichte (ACC_VFX_INTENSITY 100/70/40 %) und Budgetfüllung der Kategorie.
	 * Ab 80 % Füllung wird linear bis auf 25 % reduziert; bei 100 % Füllung nur noch Pflicht-Effekte (Rückgabe 0).
	 */
	GF_VFX_API int32 ScaleSpawnCount(int32 BaseCount, int32 IntensityPercent, float BudgetFill01, bool bMandatory);
}
