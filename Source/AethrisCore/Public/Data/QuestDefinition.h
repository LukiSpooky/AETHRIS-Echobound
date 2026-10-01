// Copyright AETHRIS Team.
#pragma once

#include "Data/AethrisDefinition.h"
#include "QuestDefinition.generated.h"

/** Questart (K48 §1). */
UENUM(BlueprintType)
enum class EQuestKind : uint8
{
	Main,        ///< MQ_*  (32, K44–K46)
	Side,        ///< SQ_### (210, K49–K51)
	FactionChain,///< FQ_F##_## – Container über Nebenquests einer Fraktion (K47/K48)
	Contract,    ///< CT_R##_## – wiederholbar (K13 §4)
	KodexTask,   ///< Kodex-Aufgaben (K39)
	WorldEvent   ///< Wetter-/Mond-/Sturm-gebundene Ereignisse (K14/K15)
};

/** Ein Questschritt (K48 §5, Quelle `Data/Quests/MainQuestSteps.csv` bzw. SQ-Daten). */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FQuestStep
{
	GENERATED_BODY()

	UPROPERTY(EditDefaultsOnly) FName StepId;            ///< STEP_<Quest>_##
	UPROPERTY(EditDefaultsOnly) FName Objective;         ///< OBJ_* aus ObjectiveTypes.csv
	UPROPERTY(EditDefaultsOnly) FName Target;            ///< NPC_/BOSS_/ARN_/ITM_/Zone/Bedingung
	UPROPERTY(EditDefaultsOnly) int32 Count = 1;
	UPROPERTY(EditDefaultsOnly) FName Location;          ///< SET_/POI_/R##(_Z##)/LOC_/dynamisch
	UPROPERTY(EditDefaultsOnly) bool bMilestone = false; ///< vergibt Wärter-EP (K48 §8)
	UPROPERTY(EditDefaultsOnly) FString Condition;       ///< optionale Zusatzbedingung (Bedingungssprache K48 §6)
	UPROPERTY(EditDefaultsOnly) FText JournalText;
};

/** Basis-Definition „Quest“ (ADR-031); Fach-Fragmente (Dialog, Kampf, Belohnung) hängen Feature-Plugins an. */
UCLASS(BlueprintType)
class AETHRISCORE_API UQuestDefinition : public UAethrisDefinition
{
	GENERATED_BODY()
public:
	virtual FPrimaryAssetType GetDefinitionType() const override { return FPrimaryAssetType(TEXT("Quest")); }

	UPROPERTY(EditDefaultsOnly, Category="Quest") EQuestKind Kind = EQuestKind::Side;
	UPROPERTY(EditDefaultsOnly, Category="Quest") FName RegionId;          ///< R## oder „dynamisch“
	UPROPERTY(EditDefaultsOnly, Category="Quest") FString Prerequisite;    ///< Bedingungssprache (K48 §6)
	UPROPERTY(EditDefaultsOnly, Category="Quest") int32 TruthLevel = 0;    ///< 0 oder 1–9 (CANON §38, L-01)
	UPROPERTY(EditDefaultsOnly, Category="Quest") int32 Intensity = 3;     ///< 1–10 (DR-29)
	UPROPERTY(EditDefaultsOnly, Category="Quest") FName FactionId;         ///< F01–F05 oder None
	UPROPERTY(EditDefaultsOnly, Category="Quest") FName ChainId;           ///< FQ_F##_## oder None
	UPROPERTY(EditDefaultsOnly, Category="Quest") TArray<FQuestStep> Steps;
};
