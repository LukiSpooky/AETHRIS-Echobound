# K05 · TDD I – Engine-Setup, Modul- & Projektstruktur, Coding Standards

| Feld | Wert |
|---|---|
| Dokument | Kapitel 05 von 68 · Technical Design Document, Teil I |
| Version | 1.0 |
| Owner | Unreal Senior Developer (Tech Director als Approver) |
| Mitwirkende | Lead Gameplay Programmer, Build/DevOps, QA Lead (Testautomation), Technical Artist |
| Baut auf | K01 §11–§13, K03 §2, K04 §7–§9 (CANON §9, §17, §23) |
| Status | ✅ Freigegeben |
| Im Repository angelegt | `AETHRIS.uproject`, `Source/*` (3 Module, 3 Targets), `Plugins/GameFeatures/*` (16 Plugins), `tools/check_layers.py` |
| Neue Kanon-Einträge | CANON §25 (Engine & Repository), §26 (Module & Schichten), §27 (Build & CI), §28 (Coding Standards & Tests) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Engine-Version, Fork & Upgrade-Politik](#2-engine-version-fork--upgrade-politik)
3. [Versionskontrolle & Branching](#3-versionskontrolle--branching)
4. [Modul- und Schichtenarchitektur](#4-modul--und-schichtenarchitektur)
5. [Verzeichnisstruktur](#5-verzeichnisstruktur)
6. [Build-Targets & Konfigurationen](#6-build-targets--konfigurationen)
7. [CI/CD-Pipeline](#7-cicd-pipeline)
8. [Coding Standards](#8-coding-standards)
9. [Blueprint-Richtlinien](#9-blueprint-richtlinien)
10. [Teststrategie (Code)](#10-teststrategie-code)
11. [Konfiguration & Settings](#11-konfiguration--settings)
12. [Infrastruktur für Entwickler](#12-infrastruktur-für-entwickler)
13. [Decision Records](#13-decision-records)
14. [Kanon-Updates](#14-kanon-updates)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Ziele

| Ziel | Messgröße |
|---|---|
| **Modularität** – Features unabhängig entwickel-, test- und abschaltbar | Jedes Feature-Plugin kann deaktiviert werden, ohne dass der Build bricht (nightly „Plugin-Off-Matrix“) |
| **Iterationsgeschwindigkeit** | Inkrementeller Editor-Build < 90 s, Live Coding für Gameplay-C++, Daten-Hotreload für CSV/Data Assets |
| **Stabilität** | Pre-Submit-Gate verhindert kaputte Builds auf `Main` (Ziel: < 1 Build-Bruch/Woche) |
| **Skalierbarkeit** | 60+ Programmierer gleichzeitig ohne Merge-Hölle (Plugin-Grenzen = Team-Grenzen, K01 §15.2) |
| **Testbarkeit** | Domain-Logik ohne Welt testbar (headless), Ziel-Coverage Domain 80 %, Feature 60 % |

---

## 2. Engine-Version, Fork & Upgrade-Politik

| Thema | Entscheidung |
|---|---|
| Basisversion | **Unreal Engine 5.6** (Source-Build von GitHub, nicht Launcher) |
| Fork | `Aethris-Engine` – eigener Branch auf Basis `5.6` |
| Erlaubte Engine-Änderungen | Nur mit Tag im Commit `[ENGINE-MOD]`, Ticket und Review durch Tech Director. Jede Änderung wird in `docs/engine_mods.md` (ab P2) gelistet. Ziel: < 40 Änderungen bis Release. |
| Bevorzugte Erweiterung | Plugins und Subklassen statt Engine-Änderungen |
| Upgrades | Max. **ein Minor-Upgrade pro Jahr** (z. B. 5.6 → 5.7 in P2, → 5.8 in P3) durch ein Upgrade-Strike-Team auf separatem Stream; Merge erst, wenn Pre-Submit + Nightly grün |
| Engine-Lock | Ab **Alpha (Feb 2030)** keine Minor-Upgrades mehr; nur Hotfix-Cherry-Picks |
| Plattform-SDKs | Gemäß Engine-Version; SDK-Wechsel nur im Upgrade-Fenster |

**Kritische Engine-Features und Status in 5.6 (Bewertung Tech Director):**

| Feature | Einsatz bei uns | Reifegrad-Einschätzung | Risiko-Mitigation |
|---|---|---|---|
| World Partition + HLOD | Gesamte Oberwelt | Produktiv | Streaming-Budgets, Traversal-Bots (K65) |
| Nanite (inkl. Foliage/Tessellation-Verbesserungen) | Umgebung, Felsen, Vegetation | Produktiv auf Current-Gen | Switch-2-Profil ohne/mit reduziertem Nanite (K65) |
| Lumen | GI/Reflexionen | Produktiv | Switch 2: Baked + SSGI |
| Gameplay Ability System | Fähigkeiten, Status | Produktiv | Rundenbasierter Wrapper (K06) |
| Mass Entity | Herden, Schwärme, Hintergrund-NPCs | Produktiv, API in Bewegung | Eigene Abstraktionsschicht in `GF_AI` |
| StateTree | NPC- und Echo-High-Level-KI | Produktiv | – |
| PCG Framework | Biome, Vegetation | Produktiv | Generierung zur Editorzeit (keine Runtime-PCG in Shipping außer Hain-Deko) |
| Iris Replication | Koop, PvP, Raids | Produktiv/opt-in | Fallback auf klassische Replikation per Config bis VS-Entscheidung |
| MetaSounds / Quartz | Adaptive Musik | Produktiv | – |
| CommonUI + MVVM | Gesamte UI | Produktiv | – |

---

## 3. Versionskontrolle & Branching

### 3.1 Systeme

| Inhalt | System | Grund |
|---|---|---|
| Spielprojekt (Code, Content, Configs, Daten) ab P2 | **Perforce Helix Core** (Streams) | Große Binärdateien, exklusives Sperren von `.uasset`/`.umap`, UGS-Integration, Branch-Performance |
| Engine-Fork | Perforce (`//Aethris-Engine/...`), Spiegel von GitHub-Upstream | Engine-Merges über p4 + Skripte |
| Design-/Spezifikations-Repository (dieses Repo) | **Git** | Text-zentriert, Review per Pull Request, Doku-Tooling |
| Preproduction (P1) | Dieses Git-Repo trägt auch Code-Gerüst, Daten-CSV, Tools | Kleines Team, schnelle Iteration |

**Migration (Beginn P2, Juli 2027):** `Source/`, `Plugins/`, `Config/`, `Data/`, `tools/` werden nach `//Aethris/Main` importiert (Historie via `git p4`). Danach ist Perforce die Quelle der Wahrheit für alles außer `docs/`; `docs/` bleibt in Git und wird nächtlich nach `//Aethris/Main/docs` gespiegelt (read-only).

### 3.2 Stream-Struktur

```
//Aethris/Main                      ← Mainline, immer spielbar (Pre-Submit-Gate)
   ├── //Aethris/Dev-Combat         ← Pod COMBAT  (Task-Streams bei Bedarf)
   ├── //Aethris/Dev-Echos          ← Pod ECHOS
   ├── //Aethris/Dev-World          ← Pod WORLD
   ├── //Aethris/Dev-Story          ← Pod STORY & QUESTS
   ├── //Aethris/Dev-Online         ← Pod ONLINE
   ├── //Aethris/Dev-EngineUpgrade  ← temporär pro Upgrade
   └── //Aethris/Release-1.0        ← ab Beta; nur Fixes, Merge-down nach Main
         └── //Aethris/Release-1.0-Hotfix
```

| Regel | Beschreibung |
|---|---|
| Copy-up | Dev-Streams kopieren nach Main mind. **2× pro Woche**, nur mit grünem Nightly des Dev-Streams |
| Merge-down | Main → Dev täglich automatisch (Robomerge) |
| Content-Sperren | `.umap` und geteilte `.uasset` nur mit exklusivem Lock; One-File-Per-Actor (World Partition) minimiert Kollisionen |
| Commit-Beschreibung | `[Bereich] Kurzbeschreibung #Ticket` + Testnotiz; `[ENGINE-MOD]`, `[DATA]`, `[SAVE-SCHEMA]` als Pflichtmarker für besondere Prüfungen |

---

## 4. Modul- und Schichtenarchitektur

### 4.1 Schichten (verbindlich, siehe auch K01 §13.2)

| Schicht | Module | Darf abhängen von |
|---|---|---|
| **Core** | `AethrisCore` | nur Engine |
| **Game** | `AethrisGame` | Core |
| **Domain** | `GF_Monsters`, `GF_World`, `GF_Inventory` | Core |
| **Feature** | `GF_Combat`, `GF_Capture`, `GF_Companion`, `GF_Breeding`, `GF_Research`, `GF_Economy`, `GF_Quests`, `GF_AI`, `GF_Save`, `GF_Multiplayer`, `GF_PvP` | Core, Domain |
| **Presentation** | `GF_UI`, `GF_Audio` | Core, Domain, Feature |
| **Editor** | `AethrisEditor` | alle (nur Editor-Builds) |

Die Schicht eines Plugins steht im Feld `"AethrisLayer"` der `.uplugin`-Datei (UE ignoriert unbekannte Felder). `tools/check_layers.py` prüft Regeln R1–R6 sowie verbotene `#include`s zwischen Feature-Plugins und ist Pre-Submit-Gate.

> **Präzisierung gegenüber K01 §13.1:** `GF_Economy` enthält auch das Crafting (Rezepte, Stationen), weil Crafting und Preise dieselben Daten (Materialwerte) nutzen. Das Inventar selbst (Items, Taschen, Ausrüstung) bleibt in `GF_Inventory` (Domain). Die Plugin-Liste aus CANON §9 bleibt unverändert.

### 4.2 Wie Features miteinander sprechen

Features dürfen sich nicht kennen. Drei erlaubte Mechanismen:

| Mechanismus | Wann | Beispiel |
|---|---|---|
| **Event-Bus** (`UAethrisEventBus`, K06) | Fire-and-forget-Benachrichtigungen | `GF_Combat` sendet `Event.Combat.Ended`; `GF_Quests` und `GF_Research` hören zu |
| **Core-Interfaces** (`I…` in `AethrisCore`) | Abfragen/Befehle mit Rückgabewert | `IBondingService::TryStartBond()` – implementiert in `GF_Capture`, aufgerufen von `GF_Combat` über `UAethrisServiceLocator` |
| **Domain-Daten** | Gemeinsamer Zustand | `FEchoInstance` (GF_Monsters) wird von Combat, Capture, Breeding gelesen/geschrieben |

```
  GF_Combat ──Broadcast(Event.Combat.Ended)──► [UAethrisEventBus] ──► GF_Quests (Zielzähler)
                                                                  └─► GF_Research (Kodex +1)
  GF_Combat ──ServiceLocator.Get<IBondingService>()──► (Interface in AethrisCore)
                                                         ▲ implementiert & registriert von GF_Capture
```

### 4.3 Game Features: Laden und Aktivieren

- Alle `GF_*` sind **Game Feature Plugins** (`ExplicitlyLoaded: true`, `BuiltInInitialFeatureState: Active`).
- Ein Plugin registriert beim Aktivieren über **Game Feature Actions**: Komponenten an Aktoren (`AddComponents`), Data-Registry-Quellen, Input-Kontexte, Subsysteme.
- **Plugin-Off-Matrix** (nightly): Build und Smoke-Test mit jeweils einem deaktivierten Feature-Plugin. Pflicht für alle Feature-Plugins außer `GF_Combat` (ohne Kampf kein Spiel) und `GF_Save`.

### 4.4 Modul-Aufbau eines Plugins (Vorlage)

```
Plugins/GameFeatures/GF_Combat/
├── GF_Combat.uplugin
├── Content/                       ← Assets dieses Features (GA_, GE_, WBP_ …)
├── Config/Tags/GF_Combat.ini      ← eigene GameplayTags
└── Source/GF_Combat/
    ├── GF_Combat.Build.cs
    ├── Public/
    │   ├── Timeline/              ← öffentliche API (nur das, was andere brauchen)
    │   └── GF_CombatTypes.h
    ├── Private/
    │   ├── Timeline/
    │   ├── Damage/
    │   └── GF_CombatModule.cpp
    └── Tests/                     ← Automation Specs (nur mit WITH_DEV_AUTOMATION_TESTS)
```

Beispiel einer generierten Build-Datei (Feature-Schicht):

```csharp
// Plugins/GameFeatures/GF_Combat/Source/GF_Combat/GF_Combat.Build.cs
// Copyright AETHRIS Team. Schicht: Feature (siehe K05 §4).
using UnrealBuildTool;

public class GF_Combat : ModuleRules
{
	public GF_Combat(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;
		CppStandard = CppStandardVersion.Cpp20;

		// Erlaubte Abhängigkeiten gemäß Schichtenregel – geprüft durch tools/check_layers.py
		PublicDependencyModuleNames.AddRange(new string[]
		{
			"Core", "CoreUObject", "Engine", "GameplayTags", "GameplayAbilities", "GameplayTasks",
			"AethrisCore", "GF_Monsters", "GF_World", "GF_Inventory"
		});
	}
}
```

---

## 5. Verzeichnisstruktur

```
AETHRIS/
├── AETHRIS.uproject
├── Source/
│   ├── Aethris.Target.cs, AethrisEditor.Target.cs, AethrisServer.Target.cs
│   ├── AethrisCore/          Public/ Private/   (Event-Bus, IDs, RNG, Save-Interfaces, Service Locator)
│   ├── AethrisGame/          Public/ Private/   (GameInstance, GameMode, PlayerController, Game Flow)
│   └── AethrisEditor/        Public/ Private/   (Validatoren, CSV-Importer, Batch-Tools)
├── Plugins/
│   └── GameFeatures/GF_*/    (16 Feature-Plugins, §4)
├── Content/                  (nur Kern-Content: Maps, Charakter-Basis, globale Materialien)
│   ├── World/R01_Verdanthain … R10_Nimbara/
│   ├── Characters/  Core/  Maps/
├── Config/
│   ├── DefaultEngine.ini DefaultGame.ini DefaultInput.ini DefaultScalability.ini
│   ├── Tags/                 (Wurzel-Tags aus K04 §8)
│   └── <Platform>/           (Windows, PS5, XSX, Switch2 – Overrides)
├── Data/                     (CSV/JSON-Quellen, Single Source für Data Tables, K06)
│   ├── Echos/  Abilities/  Items/  Quests/  World/  Progression/  Meta/
├── Build/BuildGraph/         (CI-Skripte)
├── Tests/                    (Gauntlet-Tests, Testdaten, Replays)
├── tools/                    (Python-Tools: canon.py, check_layers.py, nameguard/, …)
└── docs/                     (dieses Kapitelsystem)
```

**Regeln:** Kein Content in `Content/` eines Features außerhalb seines Plugins; regionale Weltinhalte gehören in `Content/World/R##_*` (Pod WORLD). Daten-CSV liegen **nie** nur als `.uasset` vor – die CSV ist Quelle, der Import erzeugt die Data Table (DR-25, Diffbarkeit).

---

## 6. Build-Targets & Konfigurationen

| Target | Typ | Zweck | Plattformen |
|---|---|---|---|
| `Aethris` | Game | Client inkl. Listen-Server für Koop | Win64, PS5, XSX, Switch 2 |
| `AethrisEditor` | Editor | Entwicklung | Win64 (Linux für Build-Agenten) |
| `AethrisServer` | Server | Dedicated Server für PvP/Raids (K59) | Linux x64 |

| Konfiguration | Nutzung | Checks | Cheats/Konsole |
|---|---|---|---|
| Debug / DebugGame | Programmierer-Debugging | alle | ja |
| Development | Tägliche Arbeit, Playtests intern | `check`, `ensure` | ja |
| Test | Performance- und Zertifizierungstests | `ensure` nur geloggt | eingeschränkt (Perf-Overlays) |
| Shipping | Release | keine | nein |

**Compiler/Sprache:** C++20 (`CppStandardVersion.Cpp20`), Warnungen als Fehler für Projektmodule (`bWarningsAsErrors` in CI), Unity-Build in CI, Non-Unity-Build nightly (Include-Hygiene).

---

## 7. CI/CD-Pipeline

Orchestrierung: **Unreal Horde** (Build-Farm, Test-Jobs, Artefakte) + **BuildGraph**-Skripte; **UnrealGameSync (UGS)** für Entwickler-Sync mit vorgebauten Editor-Binaries.

### 7.1 Pipeline-Stufen

```
 PRE-SUBMIT (pro Changelist, Ziel < 20 min)
   ├─ check_layers.py ─┐
   ├─ nameguard (geänderte Namen-CSV)
   ├─ Data-Lint (CSV-Schema, IDs K04 §7, RetiredIds)
   ├─ Editor Win64 (inkrementell) ──► Unit-Tests (Automation: Aethris.Unit.*)
   └─ Data Validation (geänderte Assets)
                        │ grün
                        ▼
 CONTINUOUS (pro Copy-up / alle 2 h auf Main)
   ├─ Game Win64 + PS5 + XSX + Switch 2 (Development) Kompilieren
   ├─ Server Linux
   └─ Smoke-Test: Boot → Lindwiesen laden → 60 s Bot-Lauf → Kampf → Speichern/Laden
                        ▼
 NIGHTLY (Ziel < 6 h)
   ├─ Vollständiger Cook alle Plattformen
   ├─ Functional Tests (Aethris.Functional.*) auf Testmaps
   ├─ Gauntlet: Traversal-Bots (FPS/Hitch-Messung, K65), Kampf-Soak 500 Kämpfe headless
   ├─ Balancing-Simulator (K63) – Regressionsbericht
   ├─ Plugin-Off-Matrix (§4.3)
   ├─ Non-Unity-Build, Static Analysis (PVS-Studio/Clang-Tidy)
   └─ Lokalisierung: Pseudo-Loc-Screenshots
                        ▼
 WEEKLY
   ├─ Playtest-Build (Test-Config) mit Telemetrie, Verteilung an QA/Playtest-Labor
   └─ Memory-Report pro Plattform (Budget-Abweichungen → Ticket)
```

### 7.2 BuildGraph-Auszug

```xml
<!-- Build/BuildGraph/AethrisPreSubmit.xml (Auszug) -->
<BuildGraph xmlns="http://www.epicgames.com/BuildGraph">
  <Option Name="ProjectRoot" DefaultValue="$(RootDir)/AETHRIS" Description="Projektpfad"/>

  <Agent Name="PreSubmit Checks" Type="Win64_Editor">
    <Node Name="Layer Check">
      <Spawn Exe="python" Arguments="$(ProjectRoot)/tools/check_layers.py"/>
    </Node>
    <Node Name="Data Lint" Requires="Layer Check">
      <Spawn Exe="python" Arguments="$(ProjectRoot)/tools/data_lint.py --changed-only"/>
    </Node>
    <Node Name="Compile Editor" Requires="Data Lint">
      <Compile Target="AethrisEditor" Platform="Win64" Configuration="Development"
               Arguments="-Project=$(ProjectRoot)/AETHRIS.uproject -WarningsAsErrors"/>
    </Node>
    <Node Name="Unit Tests" Requires="Compile Editor">
      <Command Name="RunUnreal" Arguments="-project=$(ProjectRoot)/AETHRIS.uproject -test=EngineTest -runtest=Aethris.Unit -nullrhi -unattended"/>
    </Node>
  </Agent>

  <Aggregate Name="PreSubmit" Requires="Unit Tests"/>
</BuildGraph>
```

### 7.3 Artefakte & Aufbewahrung

| Artefakt | Aufbewahrung |
|---|---|
| Editor-Binaries (UGS) | 14 Tage |
| Nightly-Cooks | 30 Tage, Meilenstein-Builds dauerhaft |
| Testberichte, Perf-Captures | 90 Tage, Trenddaten dauerhaft (Datenbank) |
| Symbole (PDB/DSYM) | dauerhaft für alle verteilten Builds (Crash-Analyse) |

---

## 8. Coding Standards

Basis ist der **Epic C++ Coding Standard**. Die folgenden Projektregeln ergänzen oder verschärfen ihn (LOCKED).

### 8.1 Benennung & Struktur

| Regel | Beschreibung |
|---|---|
| CS-01 | Typpräfixe nach Epic (`U`, `A`, `F`, `E`, `I`, `T`); Projektklassen enthalten den Bereich: `UEchoAbilitySystemComponent`, `FCombatTimeline`. |
| CS-02 | **Designdaten** = `U…Definition` (UPrimaryDataAsset); **Laufzeit** = `F…Instance` / `U…Component` / `U…Subsystem` (CANON §9). |
| CS-03 | Eine Klasse pro Header; Dateiname = Klassenname ohne Präfix. |
| CS-04 | Öffentliche API eines Plugins nur unter `Public/`; alles andere `Private/`. Interne Helfer in `namespace Aethris::<Feature>::Private`. |
| CS-05 | Konstanten und Tuning-Zahlen nie im Code: in `UDeveloperSettings`-Klassen, Data Assets oder Curve Tables. Ausnahme: mathematische Konstanten. |

### 8.2 Kommentare & Dokumentation

| Regel | Beschreibung |
|---|---|
| CS-06 | Jede öffentliche Klasse, Funktion und `UPROPERTY` hat einen `/** */`-Doxygen-Kommentar (wird in Editor-Tooltips angezeigt). |
| CS-07 | Kommentare erklären **Warum**, nicht Was. Verweise auf Spezifikation im Format `(K31 §4.2)` oder Design-Regel `(DR-07)`. |
| CS-08 | Sprache der Code-Kommentare: **Deutsch** im Gameplay-Code (Teamsprache), Englisch erlaubt in Engine-Modifikationen und Tools für externe Partner. Bezeichner immer Englisch. |
| CS-09 | `TODO` nur mit Ticket: `// TODO(AET-1234): …` – Pre-Submit lehnt `TODO` ohne Ticket ab. |

### 8.3 Sicherheit & Robustheit

| Regel | Beschreibung |
|---|---|
| CS-10 | `TObjectPtr<>` für UObject-Member, `TWeakObjectPtr<>` für nicht-besitzende Referenzen über Frames, `TSoftObjectPtr<>` für Assets in Daten. Kein rohes `new`/`delete` außer in Low-Level-Allocatoren. |
| CS-11 | `check()` nur für Programmierfehler, die das Spiel ohnehin zerstören; `ensureMsgf()` für behandelbare Fehler mit Fallback; Spielerdaten-Fehler (Save, Netzwerk) nie mit `check`. |
| CS-12 | Logging nur über Projekt-Kategorien (`LogAethrisCombat`, `LogAethrisSave` …), definiert in `AethrisCore/AethrisLog.h`. |
| CS-13 | **Kein Tick per Default** (`PrimaryComponentTick.bCanEverTick = false`). Tick nur mit Begründung und Tick-Intervall; bevorzugt Timer, Events, Mass-Prozessoren. |
| CS-14 | **Determinismus-Zone:** Code in `GF_Combat/Timeline`, `GF_Combat/Damage`, `GF_Breeding/Genetics` und alles, was Replays/PvP berechnet, verwendet **nur** Ganzzahl- oder Festkomma-Arithmetik (`FAethrisFixed`, K06) und den projekteigenen RNG (`FAethrisRandom`). Keine `FMath::Rand`, keine `float` in Entscheidungslogik. Ein Static-Analysis-Check sucht nach Verstößen in diesen Ordnern. |
| CS-15 | Netzwerk: Server-autoritative Logik in `Server…`-Funktionen mit Validierung; Client sendet nur Absichten (DR-21). |
| CS-16 | Threading: Gameplay auf Game Thread; Hintergrundarbeit über `UE::Tasks`; geteilte Daten mit `FRWLock` oder Immutable-Snapshots. Keine Blueprints in Worker-Threads. |

### 8.4 Performance-Grundregeln

| Regel | Beschreibung |
|---|---|
| CS-17 | Keine synchronen Asset-Loads im Spielbetrieb (`LoadSynchronous` ist im Shipping-Pfad verboten; Ausnahme: Ladebildschirm). |
| CS-18 | Container mit `Reserve()` füllen, wenn Größe bekannt; `TInlineAllocator` für kleine, kurzlebige Arrays. |
| CS-19 | Jede neue Systemfunktion mit `TRACE_CPUPROFILER_EVENT_SCOPE` / `SCOPE_CYCLE_COUNTER` instrumentiert (Unreal Insights). |

### 8.5 Beispiel: konforme Klasse

```cpp
// Plugins/GameFeatures/GF_Combat/Source/GF_Combat/Public/Timeline/CombatTimelineComponent.h
#pragma once

#include "Components/ActorComponent.h"
#include "CombatTimelineComponent.generated.h"

/**
 * Hält die Resonanz-Zeitleiste eines laufenden Kampfes (K31).
 * Determinismus-Zone (CS-14): Alle Zeitwerte sind Ganzzahl-Ticks.
 */
UCLASS(ClassGroup=(Aethris), meta=(BlueprintSpawnableComponent))
class GF_COMBAT_API UCombatTimelineComponent : public UActorComponent
{
	GENERATED_BODY()

public:
	UCombatTimelineComponent();

	/** Liefert die nächsten N Züge für die UI-Vorschau (DR-06: mind. 8). */
	UFUNCTION(BlueprintCallable, Category="Aethris|Combat")
	void GetUpcomingTurns(int32 Count, TArray<FCombatTurnPreview>& OutTurns) const;

private:
	/** Aktueller Zeitpunkt der Zeitleiste in Ticks. */
	UPROPERTY(VisibleInstanceOnly, Category="Aethris|Combat")
	int64 CurrentTick = 0;
};
```

```cpp
// Private/Timeline/CombatTimelineComponent.cpp
#include "Timeline/CombatTimelineComponent.h"

UCombatTimelineComponent::UCombatTimelineComponent()
{
	// CS-13: Die Zeitleiste ist ereignisgetrieben, kein Tick nötig.
	PrimaryComponentTick.bCanEverTick = false;
}
```

### 8.6 Code-Review

| Regel | Beschreibung |
|---|---|
| CR-01 | Jede Changelist mit Code hat mindestens **einen** Reviewer (Swarm); Determinismus-Zone, Save-Schema und Netzwerk-Code benötigen **zwei**, davon einer aus dem zuständigen Pod-Lead-Kreis. |
| CR-02 | Reviewer prüfen: Spezifikationsbezug, Tests, Instrumentierung, CS-Regeln, Lokalisierbarkeit (kein Hardcoded-Text, nur `FText`/`LOCTEXT`). |
| CR-03 | Changelists > 800 geänderte Zeilen (ohne generierte Dateien) werden aufgeteilt. |

---

## 9. Blueprint-Richtlinien

| Regel | Beschreibung |
|---|---|
| BP-01 | **Blueprints für Content, C++ für Systeme.** Systeme (Zeitleiste, Genetik, Save, Netz) existieren nur in C++. |
| BP-02 | Blueprint-Graphen > ~50 Knoten Logik werden refaktoriert (C++-Funktion oder Unterfunktionen). |
| BP-03 | Kein Tick in Blueprints außer visueller Kosmetik mit Begründung. |
| BP-04 | **Data-Only-Blueprints** bevorzugt (Varianten von Echos, Items, NPCs) – reine Parameter, keine Graphen. |
| BP-05 | Blueprint-Funktionen, die Gameplay-Werte ändern, rufen C++-API auf (GAS, Services) – keine Direktmanipulation von Attributen. |
| BP-06 | Keine harten Referenzen auf große Assets in häufig geladenen Blueprints (Soft References + Async Load). Referenzviewer-Check im Content-Review. |
| BP-07 | Animation Blueprints nutzen **Thread-Safe Update** und Property Access; Logik im AnimGraph minimal (K57). |

---

## 10. Teststrategie (Code)

| Ebene | Werkzeug | Inhalt | Laufzeit | Ziel-Abdeckung |
|---|---|---|---|---|
| **Unit** | Automation Spec (`BEGIN_DEFINE_SPEC`) | Domain-/Feature-Logik ohne Welt: Formeln, Zeitleiste, Genetik, Save-Migration | < 3 min gesamt (Pre-Submit) | Domain 80 %, Feature 60 % (Zeilen) |
| **Functional** | `AFunctionalTest` auf Testmaps | Integrationen: Kampf am Ort, Bindungsablauf, Quest-Trigger, Streaming | Nightly | alle Must-Features |
| **Simulation** | Headless-Kampfsimulator (Programm-Target, teilt Code von `GF_Combat`) | 10⁵–10⁶ Kämpfe für Balancing (K63) | Nightly | – |
| **Gauntlet** | Gauntlet-Controller | Bots: Traversal, Soak, Multiplayer-Lasttests | Nightly/Weekly | – |
| **Manuell** | QA (K66) | Exploratives Testen, Zertifizierung | kontinuierlich | – |

Beispiel-Unit-Test (Konvention: `Aethris.Unit.<Plugin>.<Thema>`):

```cpp
// GF_Combat/Tests/TimelineSpec.cpp
#include "Misc/AutomationTest.h"
#include "Timeline/TimelineMath.h"

BEGIN_DEFINE_SPEC(FTimelineSpec, "Aethris.Unit.Combat.Timeline",
	EAutomationTestFlags::EditorContext | EAutomationTestFlags::ProductFilter)
END_DEFINE_SPEC(FTimelineSpec)

void FTimelineSpec::Define()
{
	Describe("ComputeActionDelay", [this]()
	{
		It("liefert bei Geschwindigkeit 100 genau die Basis-Zeitkosten", [this]()
		{
			// K31: Delay = Kosten × 200 / (GES + 100) → bei GES 100 Faktor 1,0
			TestEqual(TEXT("Delay"), Aethris::Combat::ComputeActionDelay(/*Cost*/100, /*Speed*/100), 100);
		});

		It("ist für schnellere Echos kürzer", [this]()
		{
			TestTrue(TEXT("schneller"), Aethris::Combat::ComputeActionDelay(100, 200) < 100);
		});
	});
}
```

*Hinweis:* Die Zeitleisten-Formel wird in K31 final festgelegt; der Test zeigt die Konvention.

---

## 11. Konfiguration & Settings

| Ebene | Datei/Klasse | Inhalt |
|---|---|---|
| Engine | `DefaultEngine.ini` | Renderer, World Partition, Netzwerk (Iris), Asset Manager (Primary Asset Types) |
| Spiel | `DefaultGame.ini` | Projektinfos, Lokalisierung, Game-Feature-Konfiguration |
| Tuning (designerfreundlich) | `UDeveloperSettings`-Unterklassen pro Plugin, z. B. `UAethrisCombatSettings` | Kampf-Konstanten (Tick-Größe, Harmonie-Gewinne), editierbar unter *Projekteinstellungen → Aethris* |
| Skalierung | `DefaultScalability.ini` + Plattform-Overrides | Qualitätsstufen (K65) |
| Plattform | `Config/<Platform>/<Platform>Engine.ini` | Speicherbudgets, Rendering-Profile (Switch 2!) |
| Laufzeit-Schalter | Console Variables `aethris.*` | Debug, Live-Tuning (Development/Test) |

**Primary Asset Types (DefaultEngine.ini, Auszug):**

```ini
[/Script/Engine.AssetManagerSettings]
+PrimaryAssetTypesToScan=(PrimaryAssetType="EchoSpecies",AssetBaseClass="/Script/AethrisCore.EchoSpeciesDefinition",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/GF_Monsters/Echos")),Rules=(Priority=-1,ChunkId=-1,bApplyRecursively=True,CookRule=AlwaysCook))
+PrimaryAssetTypesToScan=(PrimaryAssetType="Ability",AssetBaseClass="/Script/AethrisCore.AbilityDefinition",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/GF_Combat/Abilities")),Rules=(CookRule=AlwaysCook))
+PrimaryAssetTypesToScan=(PrimaryAssetType="Item",AssetBaseClass="/Script/AethrisCore.ItemDefinition",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/GF_Inventory/Items")),Rules=(CookRule=AlwaysCook))
+PrimaryAssetTypesToScan=(PrimaryAssetType="Quest",AssetBaseClass="/Script/AethrisCore.QuestDefinition",bHasBlueprintClasses=False,bIsEditorOnly=False,Directories=((Path="/GF_Quests/Quests")),Rules=(CookRule=AlwaysCook))
```

*Festlegung:* Die Basisklassen `UAbilityDefinition`, `UItemDefinition`, `UQuestDefinition` liegen – wie `UEchoSpeciesDefinition` – in **`AethrisCore`**, damit jedes Feature sie referenzieren kann, ohne andere Features zu kennen. Spezialisierte Logik lebt in den Plugins.

---

## 12. Infrastruktur für Entwickler

| Bereich | Standard |
|---|---|
| Workstation Programmierer/Artist | 24–32 Kerne, 128 GB RAM, RTX-Klasse mit ≥ 16 GB VRAM, 2× NVMe (4 TB) |
| Shader-/Derived Data Cache | **Zen Server** (Cloud DDC) pro Standort + Shared Shader Cache; Ziel: frischer Editor-Start < 10 min |
| Build-Farm | Horde-Agenten (Windows/Linux), Konsolen-Devkits im Lab für automatisierte Tests |
| Distributed Compilation | UBA (Unreal Build Accelerator) |
| Crash-Reporting | Crash Report Client → eigener Sammel-Server + Symbolisierung (Backtrace/Sentry-Integration) |
| Telemetrie | Eigene Ingest-Pipeline (K06 §Telemetrie), Dashboards |
| Ticketing | Jira (Projekt `AET`) |
| Dokumentation | Dieses Repo (`docs/`), generierte API-Doku (Doxygen) nightly |

---

## 13. Decision Records

### ADR-026 – Perforce für Produktion, Git für Spezifikation
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Git + LFS für alles | Ein System, moderne Reviews | Schwaches Sperren von Binärdateien, Performance bei TB-Repos, schlechtere UGS/Horde-Integration |
| (b) Perforce für alles | Branchen-Standard UE | Doku-Review umständlich |
| (c) Perforce für Projekt, Git für `docs/` | Bestes Werkzeug je Inhalt | Zwei Systeme, Spiegelung nötig |
- **Entscheidung:** (c), mit Git-only während P1.

### ADR-027 – Ein Game-Feature-Plugin pro Großfunktion, Schicht im Deskriptor
- **Entscheidung:** 16 Plugins, Schichtenzuordnung in `.uplugin` (`AethrisLayer`), automatisierte Prüfung. **Vorteil:** Team-Grenzen = Code-Grenzen, abschaltbare Features (Plattform-Varianten, Demo-Builds). **Nachteil:** Mehr Boilerplate, Interfaces in Core wachsen. **Mitigation:** Core-Interfaces brauchen Tech-Director-Review (CR-01).

### ADR-028 – C++20, Warnings-as-Errors
- **Entscheidung:** C++20 für alle Projektmodule (Concepts, `constexpr`-Erweiterungen, Designated Initializers), Warnungen als Fehler in CI.

### ADR-029 – Determinismus-Zone mit Ganzzahl-/Festkomma-Arithmetik
- **Kontext:** PvP-Replays, Raid-Synchronität und Kampfsimulation erfordern bitgenaue Reproduzierbarkeit über Plattformen (x64, ARM auf Switch 2).
- **Entscheidung:** Kampf- und Genetik-Logik ohne Fließkomma in Entscheidungen; eigener RNG. **Nachteil:** Formeln weniger „natürlich“ zu schreiben. **Mitigation:** `FAethrisFixed` (Q16.16) mit Hilfsfunktionen (Pow-Approximation via Lookup-Tabellen), Tests gegen Python-Referenz des Balancing-Simulators (K63).

### ADR-030 – Horde + BuildGraph + UGS
- **Entscheidung:** Epic-eigene Toolchain statt Jenkins/TeamCity. Vorteil: native Integration (UBA, Test-Reports, Device-Management). Nachteil: Abhängigkeit von Epic-Tooling-Releases.

### ADR-031 – Definition-Basisklassen in AethrisCore
- **Entscheidung:** `UEchoSpeciesDefinition`, `UAbilityDefinition`, `UItemDefinition`, `UQuestDefinition` liegen in `AethrisCore`; Feature-spezifische Erweiterungen über **Instanced-Fragmente** (`TArray<TObjectPtr<UDefinitionFragment>>`, K06), die Plugins beisteuern. So kennt Core keine Feature-Logik, und Features kennen sich nicht.

---

## 14. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §25 | UE 5.6 Source-Build, Fork `Aethris-Engine`, max. 1 Minor-Upgrade/Jahr, Engine-Lock ab Alpha, `[ENGINE-MOD]`-Marker | LOCKED |
| §25 | Perforce (Streams) ab P2 für Projekt; Git für `docs/`; Stream-Layout Main/Dev-<Pod>/Release-1.0 | LOCKED |
| §26 | Schichten Core/Game/Domain/Feature/Presentation/Editor + Regeln R1–R6; Schicht im `.uplugin`-Feld `AethrisLayer`; Prüfer `tools/check_layers.py` | LOCKED |
| §26 | Domain-Plugins: GF_Monsters, GF_World, GF_Inventory; Presentation: GF_UI, GF_Audio; Rest Feature | LOCKED |
| §26 | Crafting liegt in `GF_Economy` | LOCKED |
| §26 | Kommunikation: Event-Bus, Core-Interfaces + `UAethrisServiceLocator`, Domain-Daten | LOCKED |
| §26 | Definition-Basisklassen in AethrisCore: `UEchoSpeciesDefinition`, `UAbilityDefinition`, `UItemDefinition`, `UQuestDefinition`; Erweiterung über `UDefinitionFragment` | LOCKED |
| §27 | Targets `Aethris`, `AethrisEditor`, `AethrisServer` (Linux) | LOCKED |
| §27 | CI: Horde + BuildGraph + UGS; Pre-Submit < 20 min; Nightly-Inhalte (§7.1) | LOCKED |
| §28 | Coding Standards CS-01–CS-19, Review-Regeln CR-01–CR-03, Blueprint-Regeln BP-01–BP-07 | LOCKED |
| §28 | Determinismus-Zone (CS-14): `GF_Combat/Timeline`, `GF_Combat/Damage`, `GF_Breeding/Genetics`, Replays – nur Ganzzahl/`FAethrisFixed`, RNG `FAethrisRandom` | LOCKED |
| §28 | Testnamensraum `Aethris.Unit.*`, `Aethris.Functional.*`; Coverage-Ziel Domain 80 %, Feature 60 % | LOCKED |
| §28 | Code-Kommentare Deutsch, Bezeichner Englisch | LOCKED |
| §10 | ADR-026 – ADR-031 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Engine-Version, Fork, Upgrade- und Lock-Politik; Feature-Reifegrad-Bewertung
- [x] Versionskontrolle (Perforce/Git), Stream-Layout, Commit-Konventionen, Migrationsplan
- [x] Schichtenarchitektur mit automatisierter Prüfung (`tools/check_layers.py` – 19 Module, 0 Verstöße)
- [x] Inter-Feature-Kommunikation (Event-Bus, Interfaces, Domain-Daten)
- [x] Game-Feature-Aktivierung und Plugin-Off-Matrix
- [x] Verzeichnisstruktur des Projekts
- [x] **Im Repo:** `AETHRIS.uproject`, 3 Targets, 3 Kernmodule, 16 Plugin-Deskriptoren mit Build-Dateien
- [x] Build-Konfigurationen, Compiler-Einstellungen
- [x] CI/CD-Pipeline (Pre-Submit, Continuous, Nightly, Weekly) + BuildGraph-Beispiel
- [x] Coding Standards (19 Regeln), Code-Review-Regeln, Blueprint-Richtlinien
- [x] Teststrategie mit Unit-Test-Beispiel
- [x] Konfigurationsebenen, Primary Asset Types
- [x] Entwickler-Infrastruktur
- [x] ADR-026 – ADR-031, CANON aktualisiert

➡️ **Nächstes Kapitel: K06 – TDD II: Core-Framework (Data-Driven, Event-Bus, State Machines, GAS, Save-Architektur).**
