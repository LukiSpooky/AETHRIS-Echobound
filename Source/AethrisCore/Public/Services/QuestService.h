// Copyright AETHRIS Team.
#pragma once

#include "UObject/Interface.h"
#include "QuestService.generated.h"

/** Laufzeitzustand einer Quest (K48 §10.2). */
UENUM(BlueprintType)
enum class EQuestState : uint8
{
	Hidden,     ///< Vorbedingung nicht erfüllt, nicht sichtbar
	Available,  ///< angeboten (Auftraggeber, Hinweis, Brett)
	Active,     ///< angenommen; genau ein aktueller Schritt
	Completed,  ///< abgeschlossen, Belohnung ausgezahlt
	Deferred    ///< vom Spieler zurückgestellt (nur Neben-/Fraktionsquests)
};

USTRUCT(BlueprintType)
struct AETHRISCORE_API FQuestProgress
{
	GENERATED_BODY()

	UPROPERTY(BlueprintReadOnly) FName QuestId;
	UPROPERTY(BlueprintReadOnly) EQuestState State = EQuestState::Hidden;
	UPROPERTY(BlueprintReadOnly) int32 StepIndex = 0;     ///< 0-basiert
	UPROPERTY(BlueprintReadOnly) int32 StepCount = 0;     ///< Fortschritt im Zähl-Schritt (z. B. 2/3 Heilkreise)
	UPROPERTY(BlueprintReadOnly) bool bTracked = false;
};

UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class UQuestService : public UInterface { GENERATED_BODY() };

/**
 * Questsystem (K48, implementiert in GF_Quests). Ereignisgetrieben: Zieltypen abonnieren Event-Kanäle
 * (K06 §4) und melden Fortschritt; der Dienst wertet Bedingungen (K48 §6) nur bei relevanten Ereignissen aus.
 * Host-autoritativ im Koop (K48 §10.5).
 */
class AETHRISCORE_API IQuestService
{
	GENERATED_BODY()
public:
	virtual FQuestProgress GetProgress(FName QuestId) const = 0;
	virtual bool AcceptQuest(FName QuestId) = 0;
	virtual void DeferQuest(FName QuestId) = 0;
	virtual void SetTracked(FName QuestId, bool bTracked) = 0;

	/** Meldet Fortschritt eines Zieltyps (OBJ_*) mit Ziel-ID; wird von Feature-Plugins aufgerufen. */
	virtual void ReportObjective(FName Objective, FName Target, int32 Amount = 1) = 0;

	/** Story-Flags (StoryFlags.csv): ganzzahlig; Enum-Flags als Index. */
	virtual int32 GetFlag(FName Flag) const = 0;
	virtual void SetFlag(FName Flag, int32 Value) = 0;

	/** Wertet einen Ausdruck der Bedingungssprache aus (K48 §6). */
	virtual bool EvaluateCondition(const FString& Expression) const = 0;
};
