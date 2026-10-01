# K06 · TDD II – Core-Framework

| Feld | Wert |
|---|---|
| Dokument | Kapitel 06 von 68 · Technical Design Document, Teil II |
| Version | 1.0 |
| Owner | Lead Gameplay Programmer |
| Mitwirkende | Unreal Senior Dev, AI Engineer, Network Engineer, QA Lead |
| Baut auf | K01 §13, K03 §2, K04 §7–§8, K05 (CANON §9, §17, §23, §25–§28) |
| Status | ✅ Freigegeben |
| Im Repository angelegt | `Source/AethrisCore/**` (Log, Tags, Event-Bus, Service Locator, RNG, Festkomma, Definitionen, Echo-Typen, Save-Interfaces, Zustandsmaschine, Telemetrie), `GF_Combat/…/Abilities/*` (GAS-Wrapper, AttributeSet), `tools/ref/*.py` |
| Neue Kanon-Einträge | CANON §29 (Core-Framework), §30 (Event-Kanäle & Services), §31 (Datenpipeline), §32 (Save-Architektur) |

---

## Inhalt

1. [Überblick](#1-überblick)
2. [Data-Driven Design](#2-data-driven-design)
3. [Datenpipeline: CSV → Unreal](#3-datenpipeline-csv--unreal)
4. [Event-Bus](#4-event-bus)
5. [Services & Interfaces](#5-services--interfaces)
6. [Zustandsmaschinen](#6-zustandsmaschinen)
7. [Gameplay Ability System – rundenbasiert](#7-gameplay-ability-system--rundenbasiert)
8. [Determinismus: RNG & Festkomma](#8-determinismus-rng--festkomma)
9. [Echo-Datenmodell (Laufzeit)](#9-echo-datenmodell-laufzeit)
10. [Save-Architektur](#10-save-architektur)
11. [Asset-Loading-Strategie](#11-asset-loading-strategie)
12. [Telemetrie](#12-telemetrie)
13. [ECS (Mass) – Einordnung](#13-ecs-mass--einordnung)
14. [Decision Records](#14-decision-records)
15. [Kanon-Updates](#15-kanon-updates)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Überblick

Das Core-Framework ist die gemeinsame Sprache aller 16 Feature-Plugins. Es enthält **keine Spielregeln**, sondern die Mechanismen, mit denen Regeln datengetrieben, entkoppelt, deterministisch und speicherbar umgesetzt werden.

```
                         ┌─────────────────────── AethrisCore ───────────────────────┐
                         │                                                            │
   Designdaten (CSV) ───►│  UAethrisDefinition ◄── Fragmente (von Plugins)            │
                         │   ├ UEchoSpeciesDefinition  ├ UAbilityDefinition           │
                         │   ├ UItemDefinition         └ UQuestDefinition             │
                         │                                                            │
                         │  FEchoInstance · FEchoStats · FEchoGenome · FEchoOrigin    │◄── Domain-Daten
                         │                                                            │
   Features ── Broadcast►│  UAethrisEventBus (Kanäle = Event.*‑Tags)                  │──► Features hören
   Features ── Register ►│  UAethrisServiceLocator (Core-Interfaces)                  │──► Features fragen
                         │                                                            │
                         │  FAethrisRandom (PCG32) · FAethrisFixed (Q16.16)           │◄── Determinismus-Zone
                         │  TAethrisStateMachine<E>                                   │
                         │  ISaveFragmentProvider · FAethrisSaveHeader                │◄── GF_Save
                         │  UAethrisTelemetrySubsystem · LogAethris*                  │
                         └────────────────────────────────────────────────────────────┘
```

---

## 2. Data-Driven Design

### 2.1 Grundsatz

**Alles, was ein Designer tunen oder ein Content-Ersteller hinzufügen will, ist Daten** (DR-25). Code liefert *Primitiva* (z. B. „Schaden mit Formel X“, „Status anwenden“, „Zeitleiste verschieben“); Daten kombinieren sie.

| Datenform | Wofür | Quelle der Wahrheit |
|---|---|---|
| **Definition** (`UAethrisDefinition`-Unterklasse, Primary Data Asset) | Entitäten mit Identität: Echo-Art, Fähigkeit, Item, Quest | CSV/JSON in `Data/` → Importer erzeugt/aktualisiert Asset |
| **Data Table** (`FTableRowBase`) | Tabellen ohne eigene Asset-Identität: Wärterrang, Regionsbudget, Typtabelle, Preise | CSV in `Data/` |
| **Curve Table** | Kurven: Wachstumsraten, Spawn-Gewichte über Tageszeit | CSV in `Data/` |
| **Developer Settings** | Globale Konstanten eines Systems (Tick-Größe, Harmonie-Werte) | `Config/DefaultGame.ini` |
| **Blueprint (Data-Only)** | Visuelle Varianten, Präsentation | Unreal-Asset |

### 2.2 Fragment-Muster (ADR-031)

Eine Definition in `AethrisCore` hat nur die Felder, die **mehrere** Plugins brauchen. Alles Feature-Spezifische hängt als **Fragment** daran:

```
UEchoSpeciesDefinition "ECHO_001 Fernlit"
 ├─ Kernfelder (AethrisCore): KodexNumber, Typen, BaseStats, GrowthRate, Rarity, Traits, Niches, Spawn …
 └─ Fragments[]
     ├─ UEchoBondingFragment     (GF_Capture)   Bindungsrate, Unruhe-Profil, Lieblingsköder
     ├─ UEchoLearnsetFragment    (GF_Combat)    Lernset, Crescendo, Passiv-Optionen
     ├─ UEchoEvolutionFragment   (GF_Monsters)  Evolutionsbedingungen (K19)
     ├─ UEchoEcologyFragment     (GF_AI)        Verhaltensprofil, Herdengröße, Nahrung
     ├─ UEchoGeneticsFragment    (GF_Breeding)  Loci, Morph-Tabelle
     ├─ UEchoKodexFragment       (GF_Research)  Forschungsschwellen, Lore-Texte, Foto-Posen
     ├─ UEchoMountFragment       (GF_Companion) Reitart, Geschwindigkeit (falls reitbar)
     └─ UEchoPresentationFragment(GF_UI/Audio)  Mesh, AnimBP, Rufe, Icons
```

Ist ein Plugin deaktiviert, wird sein Fragment beim Laden ignoriert (Klasse fehlt → Fragment null → Validator-Warnung nur im Editor mit aktivem Plugin).

### 2.3 Regeln

| ID | Regel |
|---|---|
| DD-01 | Definitionen sind **unveränderlich zur Laufzeit**. Laufzeitzustand gehört in Instanzen (`FEchoInstance`) oder Komponenten. |
| DD-02 | Referenzen zwischen Definitionen über `FPrimaryAssetId` oder `TSoftObjectPtr`, nie harte Pointer (Ladekontrolle, §11). |
| DD-03 | Jede Definition validiert sich selbst (`IsDataValid`), Fragmente via `ValidateFragment`. |
| DD-04 | Zahlenwerte in CSV als **Ganzzahl oder Promille** (z. B. `1250` = 1,25) – passt zur Festkomma-Arithmetik (§8). |

---

## 3. Datenpipeline: CSV → Unreal

### 3.1 Ablauf

```
 Designer bearbeitet         Pre-Submit                  Editor (lokal oder CI)              Laufzeit
 Data/Echos/Species.csv  ──► data_lint.py ──────────► UAethrisCsvImporter (Commandlet) ──► Primary Data Assets
 (Git/Perforce, diffbar)     • Schema (Spalten/Typen)   • erzeugt/aktualisiert DA_*        /GF_Monsters/Echos/…
                             • IDs (K04 §7)             • setzt nur importierte Felder     ──► Asset Manager
                             • Referenzen existieren    • Fragmente aus Spalten-Präfix
                             • Summen (Regionsbudget)     (z. B. "Bond.Rate" → Bonding-
                             • RetiredIds                  Fragment)
```

### 3.2 CSV-Konventionen

| Konvention | Beispiel |
|---|---|
| Erste Spalte `Id`, eindeutig | `ECHO_001` |
| Spalten für Fragmente mit Präfix `<Fragment>.<Feld>` | `Bond.BaseRate`, `Learn.L1`, `Eco.HerdMin` |
| Listen mit `|` getrennt | `Behavior.Diurnal|Behavior.Shy|Behavior.Singer` |
| Tags vollqualifiziert | `Type.Bloom` |
| Lokalisierte Texte **nicht** in der Daten-CSV, sondern in String Tables (K04 §11) | Spalte `Name` enthält nur den Key-Suffix |
| Kommentarzeilen beginnen mit `#` | – |

### 3.3 Importer (Auszug)

```cpp
// AethrisEditor/Private/Import/AethrisCsvImporter.cpp (Auszug)
// Commandlet: UnrealEditor-Cmd AETHRIS.uproject -run=AethrisCsvImport -source=Data/Echos/Species.csv
int32 UAethrisCsvImportCommandlet::Main(const FString& Params)
{
	FString Source;
	FParse::Value(*Params, TEXT("source="), Source);

	FCsvTable Table;                                    // projekteigener CSV-Parser (RFC 4180, '#'-Kommentare)
	if (!Table.Load(FPaths::ProjectDir() / Source))
	{
		UE_LOG(LogAethrisData, Error, TEXT("CSV nicht lesbar: %s"), *Source);
		return 1;
	}

	const FAethrisImportProfile& Profile = FindProfileFor(Source);   // Zielklasse, Pfad, Spalten-Mapping
	int32 Errors = 0;
	for (const FCsvRow& Row : Table.Rows)
	{
		UAethrisDefinition* Def = FindOrCreateDefinition(Profile, Row.Get(TEXT("Id")));
		Errors += ApplyCoreColumns(Profile, Row, Def);       // Reflection: Spaltenname → UPROPERTY
		Errors += ApplyFragmentColumns(Profile, Row, Def);   // "Bond.BaseRate" → UEchoBondingFragment::BaseRate
		Def->MarkPackageDirty();
	}
	SaveDirtyPackages();
	return Errors > 0 ? 1 : 0;
}
```

**Einweg-Prinzip:** Felder, die aus CSV stammen, sind im Editor schreibgeschützt (`meta=(EditCondition="false")` per Importer-Markierung). So kann niemand die CSV „überschreiben“, und Diffs bleiben in Textform reviewbar.

---

## 4. Event-Bus

Implementierung: `Source/AethrisCore/Public/Events/AethrisEventBus.h` (im Repository).

### 4.1 Eigenschaften

| Eigenschaft | Umsetzung |
|---|---|
| Typsicher | Nachrichten sind USTRUCTs; `Register<TMessage>` prüft `UScriptStruct` zur Laufzeit |
| Hierarchische Kanäle | `Event.Combat.Ended` erreicht Listener auf `Event.Combat` mit `EAethrisEventMatch::Partial` |
| Sicher bei Re-Entrancy | Snapshot der Listener-Liste pro Zustellung; Rekursionstiefe max. 16 (`ensure`) |
| Verzögert | `BroadcastDeferred` – Zustellung am Frame-Ende, FIFO |
| Lebensdauer | Owner schwach gehalten; tote Owner werden übersprungen und aufgeräumt |
| Kein Netzwerk | Replikation bleibt Aufgabe der Features (Server sendet eigene RPCs, K59) |

### 4.2 Verwendung

```cpp
// GF_Combat sendet:
USTRUCT() struct FCombatEndedMsg
{
	GENERATED_BODY()
	UPROPERTY() FGuid CombatId;
	UPROPERTY() FGameplayTag Format;        // Combat.Format.*
	UPROPERTY() uint8 Result = 0;           // 0 Sieg, 1 Niederlage, 2 Flucht, 3 Bindung
	UPROPERTY() TArray<FPrimaryAssetId> DefeatedSpecies;
	UPROPERTY() int32 DurationSeconds = 0;
};
UAethrisEventBus::Get(this).Broadcast(AethrisTags::Event_Combat_Ended, Msg);

// GF_Research hört (beim Aktivieren des Plugins):
Handle = UAethrisEventBus::Get(this).Register<FCombatEndedMsg>(AethrisTags::Event_Combat_Ended, this,
	[this](FGameplayTag, const FCombatEndedMsg& Msg)
	{
		for (const FPrimaryAssetId& Species : Msg.DefeatedSpecies)
		{
			AddResearchProgress(Species, EResearchSource::Combat); // K39
		}
	});
```

**Wo liegen Nachrichtentypen?** Nachrichten, die mehrere Plugins lesen, liegen in `AethrisCore/Public/Events/Messages/` (sonst müsste der Empfänger den Sender kennen). Regel: **Sender-Plugin definiert nie Nachrichten, die andere Plugins empfangen sollen.**

### 4.3 Kanal-Katalog (Stand K06, wird von Fachkapiteln erweitert)

| Kanal | Nachricht | Sender | Typische Empfänger |
|---|---|---|---|
| `Event.GameFlow.StateChanged` | `FGameFlowStateChangedMsg` | AethrisGame | UI, Audio, Input |
| `Event.Combat.Started` | `FCombatStartedMsg` | GF_Combat | Audio, AI (Kampfkreis meiden), UI |
| `Event.Combat.Ended` | `FCombatEndedMsg` | GF_Combat | Quests, Research, Companion (Bindung), Telemetrie |
| `Event.Echo.Bonded` | `FEchoBondedMsg` | GF_Capture | Research, Quests, Companion |
| `Event.Echo.LevelUp` | `FEchoLevelUpMsg` | GF_Monsters | UI, Combat (Lernset) |
| `Event.Echo.Evolved` | `FEchoEvolvedMsg` | GF_Monsters | Research, Quests, UI, Audio |
| `Event.World.WeatherChanged` | `FWeatherChangedMsg` | GF_World | AI (Spawns), Audio, Combat (Typ-Resonanz), UI |
| `Event.World.TimeOfDayChanged` | `FTimeOfDayChangedMsg` | GF_World | AI, Economy (Händler), Audio |
| `Event.World.Zone.BandFixed` | `FZoneBandFixedMsg` | GF_World | Save, Telemetrie |
| `Event.Quest.StepCompleted` | `FQuestStepMsg` | GF_Quests | UI, Save (Autosave), Telemetrie |
| `Event.Save.Requested` | `FSaveRequestMsg` | beliebig | GF_Save |

---

## 5. Services & Interfaces

Implementierung Locator: `Source/AethrisCore/Public/Services/AethrisServiceLocator.h`.

### 5.1 Core-Interfaces (Verträge in `AethrisCore/Public/Services/`)

| Interface | Implementiert von | Zweck (Auszug) |
|---|---|---|
| `IEchoRosterService` | GF_Monsters | Chor & Hain lesen/schreiben, Instanz per GUID finden |
| `IWorldStateService` | GF_World | Wetter, Tageszeit, aktuelle Region/Zone, Zonen-Band |
| `IInventoryService` | GF_Inventory | Items hinzufügen/entfernen/prüfen |
| `IBondingService` | GF_Capture | Bindung starten (aus Kampf/Oberwelt), Chance-Vorschau |
| `ICombatService` | GF_Combat | Kampf starten (Format, Teilnehmer, Ort) |
| `IKodexService` | GF_Research | Forschungsstufe abfragen, Fortschritt melden |
| `IQuestService` | GF_Quests | Questzustand abfragen, Ziele melden |
| `IEconomyService` | GF_Economy | Preise abfragen, Kauf/Verkauf |
| `ISaveService` | GF_Save | Speichern/Laden anstoßen, Provider registrieren |
| `IReputationService` | GF_Quests | Ruf abfragen/ändern |

### 5.2 Regeln

| ID | Regel |
|---|---|
| SV-01 | Interfaces enthalten nur **Abfragen und Befehle mit klaren Ergebnissen**; Benachrichtigungen laufen über den Event-Bus. |
| SV-02 | Aufrufer behandeln `nullptr` (Plugin deaktiviert). Für Pflicht-Services (Roster, WorldState, Inventory, Save) prüft der Game-Flow beim Laden, dass sie registriert sind. |
| SV-03 | Interfaces sind **synchron**; lang laufende Operationen (Cloud-Save) liefern ein Handle + Event. |
| SV-04 | Neue Interfaces oder Signaturänderungen brauchen Tech-Director-Review (ADR-027). |

```cpp
// AethrisCore/Public/Services/BondingService.h
UINTERFACE(MinimalAPI, meta=(CannotImplementInterfaceInBlueprint))
class UBondingService : public UInterface { GENERATED_BODY() };

/** Vertrag der Resonanzbindung (implementiert in GF_Capture, K36). */
class AETHRISCORE_API IBondingService
{
	GENERATED_BODY()
public:
	/** Vorschau der Bindungschance in Promille für UI und KI (K36). */
	virtual FBondPreview PreviewBond(const FGuid& WildEchoId, FPrimaryAssetId SealItem) const = 0; // CR-002 (K36): ersetzt PreviewBondChancePermille

	/** Startet die Anschlag-Phase; Ergebnis kommt als Event.Echo.Bonded oder Event.Bond.Failed. */
	virtual bool BeginStrikePhase(const FGuid& WildEchoId, FPrimaryAssetId SealItem, bool bFromCombat) = 0;
};
```

---

## 6. Zustandsmaschinen

Drei Werkzeuge für drei Ebenen (LOCKED):

| Ebene | Werkzeug | Beispiele | Warum |
|---|---|---|---|
| **Global** (Spielzustand) | `UAethrisGameFlowSubsystem` + `UGameFlowStateDefinition` (K03) | Explore ↔ Combat ↔ Bond | Datengetrieben, Overlay-Stapel, Event bei Wechsel |
| **Code-Abläufe** | `TAethrisStateMachine<E>` (`AethrisCore/Public/StateMachine/`) | Rückklang-Sequenz, Bindungsphasen, Kampfphasen, Raid-Phasen | Leichtgewichtig, deterministisch, testbar |
| **KI-Verhalten** | **StateTree** (High-Level) + **Behavior Tree/Blackboard** (Taktik) | Echo: Schlafen/Fressen/Revier; NPC: Tagesablauf; Trainer-KI | Editor-Debugging, Designer-Zugriff |

**Warum nicht überall StateTree?** StateTree ist hervorragend für KI und Designer-Logik, aber für kleine Code-Abläufe (5 Zustände, Enter/Exit) zu schwergewichtig und schwerer unit-testbar. **Warum nicht überall die Code-FSM?** Designer könnten KI nicht ohne Programmierer anpassen (DR-25).

Beispiel Bindungsphasen (K36 wird ausgearbeitet):

```cpp
enum class EBondPhase : uint8 { Listen, Approach, Attune, Strike, Resolved, Count };

TAethrisStateMachine<EBondPhase> Fsm(EBondPhase::Listen);
Fsm.Allow(EBondPhase::Listen,   EBondPhase::Approach);
Fsm.Allow(EBondPhase::Approach, EBondPhase::Attune);
Fsm.Allow(EBondPhase::Approach, EBondPhase::Strike, [this]{ return bEchoCalm; });  // DR-03: Weg über Ruhe
Fsm.Allow(EBondPhase::Attune,   EBondPhase::Strike);
Fsm.Allow(EBondPhase::Strike,   EBondPhase::Resolved);
Fsm.Allow(EBondPhase::Strike,   EBondPhase::Attune);   // Fehlversuch, Echo bleibt
Fsm.OnEnter(EBondPhase::Strike, [this]{ OpenTimingWindow(); });
```

---

## 7. Gameplay Ability System – rundenbasiert

Implementierung (Gerüst): `Plugins/GameFeatures/GF_Combat/Source/GF_Combat/Public/Abilities/EchoAbilitySystemComponent.h`, `EchoAttributeSet.h`.

### 7.1 Was wir von GAS nutzen – und was nicht

| GAS-Baustein | Nutzung | Begründung |
|---|---|---|
| `UAttributeSet` | ✅ 9 Attribute (CurrentHP, MaxHP + 8 Werte ohne HP-Basis → MaxHP) | Einheitliche Modifikator-Pipeline, Debug-Tools (`showdebug abilitysystem`) |
| `UGameplayEffect` | ✅ Status, Buffs/Debuffs, Terrain-/Wetterboni | Stapelregeln, Tags, Immunitäten per Tag |
| GameplayTags auf ASC | ✅ Zustände (`Status.*`), Blockaden | Abfragen in Daten |
| `UGameplayAbility` | ✅ als **Ausführungs-Container** einer Fähigkeit (Schadensberechnung, Effekte, Cues) | Wiederverwendbare Ability-Klassen pro Primitiv (Schaden, Heilung, Status, Zeitleiste) |
| `GameplayCue` | ✅ VFX/SFX/Kamera | Entkoppelt Präsentation (GF_UI/GF_Audio) |
| Ability-Aktivierung durch Input | ❌ | Zeitleiste aktiviert (K31) |
| Client-Prediction | ❌ | Rundenbasiert, serverautoritativ |
| Zeitbasierte Effektdauer | ❌ (Infinite + Zugzähler) | Dauer in Zügen (K32) |
| `ExecutionCalculation` für Schaden | ✅, aber Mathe in Festkomma (CS-14) | Formel K32 |

### 7.2 Ausführungsfluss eines Zuges

```
 Zeitleiste (K31)                 UEchoAbilitySystemComponent               Effekte / Präsentation
 ────────────────                 ───────────────────────────               ──────────────────────
 NächsterAkteur()  ───────────►  ExecuteTurnAbility(Handle, Ctx)
                                   │ 1. Prüfen: Status blockiert? (Tags)
                                   │ 2. Fähigkeit instanziieren (InstancedPerExecution)
                                   │ 3. Treffer-/Ausweichwurf (Ctx.Rng, K32)
                                   │ 4. ExecutionCalculation (Festkomma)  ──────► GE_Damage auf Ziel
                                   │ 5. Sekundäreffekte (Status, Terrain) ──────► GE_Status_* / Terrain
                                   │ 6. GameplayCues auslösen  ─────────────────► Niagara, MetaSounds, Kamera
                                   │ 7. Harmonie-Ereignis an Zeitleiste
                                   ▼
 Zeitkosten (Ticks)  ◄────────── return Cost
 Echo neu einsortieren (K31)
 AdvanceTurnDurations() am Zugende
```

### 7.3 Attribut-Regeln

| Regel | Beschreibung |
|---|---|
| GAS-01 | Attribute enthalten immer ganzzahlige Werte (`PreAttributeChange` rundet). |
| GAS-02 | Modifikatoren: additive Ganzzahlen oder **Stufen** (Buff-Stufen −4…+4, Multiplikator-Tabelle in Festkomma, K32). Keine freien float-Multiplikatoren. |
| GAS-03 | Basiswerte werden zu Kampfbeginn aus `FEchoInstance` berechnet (Formel K18) und nie während des Kampfes neu berechnet (Level-Ups erst nach Kampfende wirksam). |
| GAS-04 | Am Kampfende werden nur `CurrentHP` und `PersistentStatus` zurück in die Instanz geschrieben. |

---

## 8. Determinismus: RNG & Festkomma

### 8.1 `FAethrisRandom` (PCG32)

Implementierung: `AethrisCore/Public/Math/AethrisRandom.h`; Referenz: `tools/ref/aethris_random.py`.

| Funktion | Zweck |
|---|---|
| `Seed(seed, stream)` | Initialisierung; Stream wählt unabhängige Sequenz |
| `NextU32()` | 32 Bit |
| `NextBounded(n)` / `RangeInclusive(a,b)` | bias-frei (Rejection Sampling) |
| `ChancePermille(p)` | Wahrscheinlichkeiten in Promille (passt zu DD-04) |
| `Fork(id)` | Teilstrom (pro Teilnehmer, pro Zuchtvorgang) – Änderungen an einem Teilsystem verschieben nicht die Zufallsfolge anderer |

**Verifikation:** Für `seed=42, stream=54` liefert die Python-Referenz `0xa15c02b7, 0x7b47f409, 0xba1d3330, 0x83d2f293, 0xbfa4784b, 0xcbed606e` – identisch mit den veröffentlichten PCG32-Referenzwerten. Der C++-Unit-Test `Aethris.Unit.Core.Random` prüft dieselben Werte.

**Seed-Hierarchie (LOCKED):**

```
Weltstand-Seed (bei Neuerstellung, 64 Bit)
 ├─ Fork(1)  Wetter-Strom        (K14)
 ├─ Fork(2)  Spawn-Strom pro Zone (K52)  → Fork(ZoneHash)
 ├─ Fork(3)  Zucht-Strom          (K38)  → Fork(BreedingCounter)
 ├─ Fork(4)  Loot-Strom
 └─ Kampf-Seed = Hash(Weltstand-Seed, CombatCounter)   → Fork(ParticipantIndex)
PvP/Raid: Kampf-Seed vom Server (zufällig), im Replay gespeichert (K61)
```

### 8.2 `FAethrisFixed` (Q16.16)

Implementierung: `AethrisCore/Public/Math/AethrisFixed.h` / `Private/Math/AethrisFixed.cpp`; Referenz: `tools/ref/aethris_fixed.py`.

| Operation | Verfahren | Genauigkeit (gemessen gegen float64) |
|---|---|---|
| `+ - * /` | int64-Zwischenwerte | exakt bis Rundung 2⁻¹⁶ |
| `Log2` | Bit-für-Bit-Quadrieren | ≤ 2⁻¹⁵ |
| `Exp2` | Produkt aus Tabelle 2^(2^-k) | ≤ 2⁻¹⁵ |
| `Pow(b, e)` | `Exp2(e · Log2(b))` | 2^0,85 → 1,80247 (Soll 1,80250), 1,6^0,85 → 1,49104 (Soll 1,49108) |

Damit sind Schadensformeln mit gebrochenen Exponenten (z. B. `(ANG/VER)^0,85`, K32) deterministisch auf x64 und ARM berechenbar.

---

## 9. Echo-Datenmodell (Laufzeit)

Implementierung: `AethrisCore/Public/Echo/EchoTypes.h`.

```
FEchoInstance  (gespeichert, tauschbar, ~400–600 Byte serialisiert)
 ├─ InstanceId : FGuid                  ─ stabil über Tausch/Cloud
 ├─ Species    : FPrimaryAssetId        ─ EchoSpecies:ECHO_###
 ├─ Nickname, Level (1–100), Experience, Bond (0–1000)
 ├─ Personality : Tag, Temperament : Tag         (K18)
 ├─ Genome : FEchoGenome
 │    ├─ Aptitudes : FEchoStats (Anlagen)       (K18/K38)
 │    ├─ Loci[] : {Locus, A, B}                  (K38)
 │    ├─ Morph : FName, Mutations : Tags
 ├─ Polish : FEchoStats (Schliff)                (K18)
 ├─ CurrentHP, PersistentStatus
 ├─ Repertoire[], ActiveSlots[≤4], PassiveAbility, HeldItem
 └─ Origin : FEchoOrigin (DR-16)
      ├─ OriginalWardenId/Name, ZoneId, Weather, TimeOfDay, GameDay, RealTimeUtc
      ├─ Method (Bindung/Zucht/Geschenk/Event), ParentA/B
      └─ Signature (Server, K59)
```

`EEchoRarity` (LOCKED): **Common, Uncommon, Rare, VeryRare, Legendary, Mythical** (DR-15: ab `Rare` sind SpawnConditions Pflicht).

---

## 10. Save-Architektur

Implementierung Verträge: `AethrisCore/Public/Save/AethrisSaveTypes.h`. Vollständige Spezifikation (Autosave, Cloud, Versionierung, Migration): **K64**.

### 10.1 Format

```
 ┌──────────────────────────────────────────────────────────┐
 │ FAethrisSaveHeader                                       │
 │  Magic 'AETH' · ContainerVersion · BuildVersion · Zeit   │
 │  Vorschau (Region, Rang, Akkorde, Chor) · PayloadCrc     │
 ├──────────────────────────────────────────────────────────┤
 │ Fragment-Verzeichnis: [Id, Version, Offset, Größe] × N   │
 ├──────────────────────────────────────────────────────────┤
 │ Fragment "Chor"        (v3)  ← GF_Monsters               │
 │ Fragment "Sanctuary"   (v1)  ← GF_Companion              │
 │ Fragment "Inventory"   (v2)  ← GF_Inventory              │
 │ Fragment "World.Zones" (v1)  ← GF_World (fixierte Bänder)│
 │ Fragment "Quests"      (v4)  ← GF_Quests                 │
 │ …                                                        │
 └──────────────────────────────────────────────────────────┘
   komprimiert (Oodle) · plattformspezifisch verschlüsselt/signiert
```

### 10.2 Prinzipien

| ID | Prinzip |
|---|---|
| SA-01 | **Fragmentiert**: Jedes System besitzt sein Fragment (`ISaveFragmentProvider`); GF_Save kennt keine Features. |
| SA-02 | **Versioniert pro Fragment**: Migration in `ReadSaveFragment(Ar, FromVersion)` als Kette. |
| SA-03 | **Fehlertolerant**: Unlesbares Fragment → Reset auf Default + Hinweis; nie Absturz, nie Totalverlust. |
| SA-04 | **Unbekannte Fragmente werden mitgeschleppt** (Rohbytes erhalten), damit ein älterer Build einen neueren Save nicht beschädigt (Cloud-Sync zwischen Geräten). |
| SA-05 | **Atomar**: Schreiben in Temp-Datei → Prüfsumme → Umbenennen; 3 rotierende Autosave-Kopien. |
| SA-06 | **Explizite Serialisierung** (`FArchive <<`), nicht pauschal `UPROPERTY(SaveGame)`-Reflexion für Kernfragmente – kontrollierbare Bytes, Determinismus (gleicher Zustand → gleiche Bytes). `SaveGame`-Flags dienen als Dokumentation und für Debug-Dumps. |

---

## 11. Asset-Loading-Strategie

| Ebene | Mechanismus | Beispiel |
|---|---|---|
| Immer geladen | Core-Definitionen (alle 256 Spezies-Definitionen ohne Präsentationsfragment-Assets: ~2 MB) | Kodex, Regeln |
| Bundles | Asset-Manager-Bundles `Combat`, `World`, `UI` pro Definition | Fähigkeits-VFX erst bei Kampfstart |
| Streaming | World Partition (Welt), Async-Load für Echo-Meshes beim Annähern (Ökologie-LOD, K52) | Herde in 150 m |
| Vorladen | Chor-Echos (6 × Mesh/Anim/VFX) dauerhaft resident; Kampf-Assets der Gegner beim Kampfkreis-Solve (≤ 1,5 s Budget, K02) | – |

Regel CS-17 (keine synchronen Loads) gilt; der Kampfübergang verdeckt die Ladezeit durch die Einleitungskamera (K31).

---

## 12. Telemetrie

Implementierung: `AethrisCore/Public/Telemetry/AethrisTelemetry.h`.

| Aspekt | Festlegung |
|---|---|
| Einwilligung | Opt-in beim ersten Start; ohne Opt-in werden keine Ereignisse gepuffert |
| Namensschema | `domain.object.verb` (K04 §7) |
| Transport | Puffer (max. 256 Ereignisse / 30 s) → Senken (Datei im Playtest-Labor, HTTP im Live-Betrieb) |
| Datenschutz | Keine Klarnamen; Wärter-ID pseudonymisiert; DSGVO-konforme Löschung über Profil |
| Pflicht-Ereignisse | K02 §12 + jedes Fachkapitel ergänzt seine Liste |

---

## 13. ECS (Mass) – Einordnung

Das Briefing fordert „ECS wo sinnvoll“. Entscheidung (LOCKED): **Mass Entity** für alles, was in großer Zahl und mit einfacher Logik existiert; klassische Aktoren für alles, mit dem der Spieler direkt interagiert.

| Entität | Repräsentation | Übergang |
|---|---|---|
| Echo fern (> 150 m) | Mass-Entity (Position, Bedürfnisse, Herdenzugehörigkeit), Rendering per Instanced Static Mesh / Vertex-Animation | – |
| Echo nah (≤ 150 m) | Mass-Entity + Actor-Repräsentation (Skeletal Mesh, AnimBP) über **Mass Representation** | LOD-Wechsel automatisch |
| Echo in Interaktion (Kampf, Bindung, Begleiter) | Vollwertiger Actor mit ASC | Entity „ausgeliehen“, nach Ende zurückgegeben |
| Hintergrund-NPCs (Städte) | Mass Crowd (Zone Graph) | nah → Actor mit StateTree |
| Benannte NPCs | Actor + StateTree | – |

Details: K52 (Ökologie) und K53 (NPC-KI).

---

## 14. Decision Records

### ADR-032 – GAS als Effekt-Framework, Zeitleiste als Aktivierungsinstanz
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Eigenes Effektsystem | Volle Kontrolle, rundenbasiert nativ | Hoher Aufwand (~6–8 Engineer-Jahre), kein Debug-Tooling |
| (b) GAS vollständig inkl. Aktivierung | Standard | Prediction/Echtzeit-Annahmen kollidieren mit Zeitleiste |
| (c) GAS für Attribute/Effekte/Cues, Aktivierung durch Zeitleiste | Bewährtes Tooling + rundenbasierte Kontrolle | Disziplin nötig (Regeln GAS-01–04), float-Attribute erfordern Rundungsregel |
- **Entscheidung:** (c). Risiko R-04 bleibt bis Prototyp-Review Feb 27 beobachtet.

### ADR-033 – Eigener Event-Bus statt GameplayMessageSubsystem aus Beispielprojekten
- **Kontext:** Ein vergleichbares Subsystem existiert in Epic-Beispielprojekten, ist aber kein Engine-Bestandteil.
- **Entscheidung:** Eigene Implementierung in AethrisCore (~250 Zeilen) mit verzögerter Zustellung, Rekursionsschutz und Typwarnungen. Vorteil: Keine Abhängigkeit von Beispielcode, an unsere Regeln angepasst. Nachteil: Eigene Wartung.

### ADR-034 – PCG32 als Projekt-RNG
- **Entscheidung:** PCG32 mit Teilströmen. Vorteile: klein, schnell, gut verteilt, unabhängige Ströme, Referenzwerte verfügbar. Alternativen (xoshiro256**, FRandomStream) verworfen: xoshiro hat größeren Zustand ohne Vorteil für unsere Anwendung; FRandomStream siehe Header-Kommentar.

### ADR-035 – Fragmentierte, explizit serialisierte Saves
- **Entscheidung:** SA-01–SA-06. Vorteil: Features unabhängig migrierbar, Plugin-Off-fähig, Vorwärtskompatibilität durch Mitschleppen. Nachteil: Mehr Code pro System (Write/Read/Reset). **Mitigation:** Vorlagen und Unit-Test-Generator für Round-Trip-Tests.

### ADR-036 – CSV als Quelle der Wahrheit für Designdaten
- **Entscheidung:** Designdaten leben in `Data/*.csv`, Assets sind generiert. Vorteil: Diffs, Reviews, Massenänderungen per Tabelle/Skript, Balancing-Simulator liest dieselben Dateien. Nachteil: Zwei Darstellungen. **Mitigation:** Einweg-Import, Felder im Editor gesperrt, Pre-Submit erzwingt Re-Import.

---

## 15. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §29 | Core-Klassen: `UAethrisDefinition`, `UDefinitionFragment`, `UAethrisEventBus`, `UAethrisServiceLocator`, `FAethrisRandom` (PCG32), `FAethrisFixed` (Q16.16), `TAethrisStateMachine<E>`, `UAethrisTelemetrySubsystem`, `ISaveFragmentProvider`, `FAethrisSaveHeader` | LOCKED |
| §29 | Echo-Laufzeitdaten: `FEchoStats` (8 Werte, int32), `FEchoGenome` (Aptitudes, Loci, Morph, Mutations), `FEchoOrigin`, `FEchoInstance`-Felder | LOCKED |
| §29 | `EEchoRarity`: Common, Uncommon, Rare, VeryRare, Legendary, Mythical | LOCKED |
| §29 | Zustandsmaschinen-Ebenen: GameFlow (global) · TAethrisStateMachine (Code) · StateTree + BT (KI) | LOCKED |
| §29 | GAS rundenbasiert: `UEchoAbilitySystemComponent::ExecuteTurnAbility`, `UEchoAttributeSet` (CurrentHP, MaxHP, Attack, Defense, SpAttack, SpDefense, Speed, Precision, Evasion); Regeln GAS-01–04 | LOCKED |
| §29 | Seed-Hierarchie (Wetter 1, Spawn 2, Zucht 3, Loot 4, Kampf = Hash(Weltseed, Kampfzähler)) | LOCKED |
| §29 | Mass für ferne Echos/Hintergrund-NPCs, Actor-Übergabe in Interaktion; Nah-Radius 150 m | LOCKED |
| §30 | Event-Kanäle (§4.3), Nachrichten in `AethrisCore/Public/Events/Messages/` | LOCKED |
| §30 | Core-Interfaces (§5.1) + Regeln SV-01–SV-04 | LOCKED |
| §31 | Datenpipeline CSV → Importer-Commandlet → Definitionen; Fragment-Spalten `<Fragment>.<Feld>`; Listen mit `|`; Promille-Werte (DD-04); Regeln DD-01–DD-04 | LOCKED |
| §32 | Save: Header + versionierte Fragmente, SA-01–SA-06, Oodle-Kompression, 3 rotierende Autosaves | LOCKED (Detail K64) |
| §10 | ADR-032 – ADR-036 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Data-Driven-Grundsatz, Datenformen, Fragment-Muster, Regeln DD-01–DD-04
- [x] CSV-Pipeline mit Lint, Importer-Commandlet, Einweg-Prinzip
- [x] **Code im Repo:** Event-Bus (typsicher, hierarchisch, verzögert, rekursionsgeschützt)
- [x] **Code im Repo:** Service Locator + Interface-Katalog + Regeln SV-01–04
- [x] **Code im Repo:** Zustandsmaschine (Code-Ebene) + Ebenenmodell
- [x] **Code im Repo:** GAS-Wrapper und AttributeSet (rundenbasiert, ganzzahlig)
- [x] **Code im Repo:** PCG32-RNG und Q16.16-Festkomma mit Python-Referenzen (verifiziert)
- [x] **Code im Repo:** Definitionen, Echo-Laufzeitdaten, Save-Verträge, Telemetrie, Log-Kategorien, native Tags
- [x] Save-Architektur (Fragmente, Versionierung, Fehlertoleranz)
- [x] Asset-Loading-Strategie
- [x] ECS-Einordnung (Mass vs. Actor)
- [x] ADR-032 – ADR-036, CANON aktualisiert, Schichtenprüfung 0 Verstöße

➡️ **Nächstes Kapitel: K07 – World Bible I: Kosmologie, Weltlied, Geschichte.**
