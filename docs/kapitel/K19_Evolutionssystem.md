# K19 · Evolutionssystem

| Feld | Wert |
|---|---|
| Dokument | Kapitel 19 von 68 · Monster Bible, Teil III |
| Version | 1.0 |
| Owner | RPG Systems Designer |
| Mitwirkende | Creature Design Lead, Lead Gameplay Programmer, Narrative (Kodex-Hinweise), Animation/VFX (Evolutionssequenz), Audio (Stinger), Economy Designer (Items) |
| Baut auf | CANON §5 (Formen & Auslöser), §20 (Linienstruktur 40/45/22/8), §33 (Evolution = Tonartwechsel), §64–§67 (Tageszeit, Mond), §61 (Wetter), §72 (Datenschema), §79–§83 (Werte, Wachstum) |
| Status | ✅ Freigegeben |
| Im Repository | `tools/ref/evo_condition.py` (Parser-Referenz mit Tests), `Data/Items/EvolutionItems.csv` (25 Items), Validator-Erweiterung in `tools/gen_catalog.py` |
| Neue Kanon-Einträge | CANON §84 (Evolutionsformen & Linienregeln), §85 (Bedingungssprache), §86 (Evolutionsablauf & Übertragungsregeln), §87 (Evolutions-Items), §88 (Pacing-Richtwerte) |

---

## Inhalt

1. [Evolution in AETHRIS](#1-evolution-in-aethris)
2. [Evolutionsformen](#2-evolutionsformen)
3. [Auslöser](#3-auslöser)
4. [Die Bedingungssprache](#4-die-bedingungssprache)
5. [Evolutions-Items](#5-evolutions-items)
6. [Ablauf einer Evolution](#6-ablauf-einer-evolution)
7. [Was übertragen wird – und was sich ändert](#7-was-übertragen-wird--und-was-sich-ändert)
8. [Pacing-Richtwerte](#8-pacing-richtwerte)
9. [Entdeckbarkeit: Evolutionsahnung & Kodex](#9-entdeckbarkeit-evolutionsahnung--kodex)
10. [Präsentation](#10-präsentation)
11. [Online-Regeln](#11-online-regeln)
12. [Code](#12-code)
13. [Decision Records](#13-decision-records)
14. [Kanon-Updates](#14-kanon-updates)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Evolution in AETHRIS

**Weltlogik (CANON §33):** Evolution ist ein **Tonartwechsel** – ein Echo wächst in einen höheren Oberton hinein, wenn seine Schwingung stark genug ist (Level), wenn es mit seinem Wärter in Einklang ist (Bindung) oder wenn äußere Klänge es anstoßen (Items, Wetter, Ort, Zeit).

**Designziele:**

| Ziel | Umsetzung |
|---|---|
| Entdeckung (S1/S2) | Viele Bedingungen sind **Weltbedingungen** (Wetter, Mond, Ort) – die Welt selbst ist Teil der Evolution |
| Bindung (S2) | Bindungsgebundene Evolutionen belohnen Pflege; Crescendo-Freischaltung schon ab Bindungsstufe 2 |
| Kontrolle | Der Spieler entscheidet immer, ob und wann sich ein Echo entwickelt |
| Keine Pflicht-Online-Interaktion | **Keine tauschgebundenen Evolutionen** (DR-19) |
| Lesbarkeit | Bedingungen sind in einer prüfbaren Sprache formuliert; der Kodex verrät sie schrittweise |

---

## 2. Evolutionsformen

Gemäß Briefing („keine Evolution, zweistufig, dreistufig, Spezialentwicklung“) und CANON §20:

| Form | `LineKind` | Anzahl Linien | Arten | Beschreibung |
|---|---|---|---|---|
| **Keine Evolution** | `Single` | 22 | 22 | Eigenständige, vollständige Arten (Kernsumme 430–520) |
| **Zweistufig** | `Two` | 45 | 90 | Stufe 1 → Stufe 2 |
| **Dreistufig** | `Three` | 40 | 120 | Stufe 1 → 2 → 3 |
| **Spezialentwicklung** | `Branch` | (in Linien enthalten) | 8 | Zusätzliche Endformen, die eine Linie **verzweigen** |
| Legendär / Mythisch | `Legendary` / `Mythical` | – | 16 | Keine Evolution |

### 2.1 Spezialentwicklungen (Zweige)

Eine Spezialentwicklung ist eine **alternative** Endform. Die Linie bekommt dadurch einen Zweig:

```
  Dreistufige Linie mit Zweig:            Zweistufige Linie mit Zweig:
     S1 ──► S2 ──► S3   (Standard)            S1 ──► S2  (Standard)
                │                              │
                └──► S3' (Zweig, Bedingung)    └──► S2' (Zweig, Bedingung)
```

**Regeln (LOCKED):**
- Zweigformen haben dieselbe Gattung (wissenschaftlich) und dieselbe Stufe wie die Standard-Endform; `LineKind = Branch`.
- Zweigbedingungen enthalten **mindestens eine Weltbedingung** (Wetter, Mond, Tageszeit, Zone/Region) – der Zweig ist eine Entdeckung, kein Item-Kauf.
- Sind die Bedingungen beider Formen gleichzeitig erfüllt, wählt der Spieler (Evolutionsdialog zeigt beide Silhouetten).
- 8 Zweige insgesamt (CANON §20); Kernsumme wie die Standard-Endform (±10).

---

## 3. Auslöser

| Auslöser | Schlüssel | Beispiel | Weltbezug |
|---|---|---|---|
| Level | `Level` | `Level>=16` | Wachstum |
| Bindung | `BondTier` | `BondTier>=4` (Stufen K37) | Partnerschaft |
| Item | `Item` | `Item=ITM_EVO_TIDE` | äußerer Klang |
| Tageszeit | `TimeOfDay` | `TimeOfDay=Night` | Rhythmus |
| Wetter | `Weather` | `Weather=Thunderstorm` | Klima |
| Gebiet | `Zone` / `Region` | `Zone=R06_Z05`, `Region=R07` | Stimme des Ortes |
| Mond | `Moon` | `Moon=FullMoon` | Kalender |
| Fähigkeit beherrschen | `Knows` | `Knows=ABL_A042` | Übung |
| Chor-Partner | `ChorHas` | `ChorHas=Type.Spirit` | Symbiose |
| Persönlichkeit / Temperament | `Personality`, `Temperament` | `Temperament=Stoic` | Charakter |
| Leistungen | `WinsWhileHolding`, `StepsInRegion` | `WinsWhileHolding>=10` (Siege mit gehaltenem Item) | Erfahrung |
| Wertverhältnis | `Stat:<A> <op> <B>` | `Stat:Attack>Defense` | Körperbau |
| **Kombinationen** | `&`, `|`, `!`, `( )` | `Level>=30 & Weather=Rain` | – |

**Verteilungsziele für die 107 Linien (Validator-Kennzahl, K20–K27):**

| Auslösertyp (Hauptbedingung) | Anteil der Evolutionsschritte |
|---|---|
| reines Level | 55 % |
| Level + Weltbedingung (Wetter/Zeit/Mond/Ort) | 18 % |
| Bindung (+ ggf. Zeit) | 10 % |
| Item (Obertonkristall oder Spezialitem) | 10 % |
| Sonstige (Fähigkeit, Chor-Partner, Leistung, Wertverhältnis) | 7 % |

---

## 4. Die Bedingungssprache

### 4.1 Grammatik (LOCKED)

```
 expr    := term { '|' term }                 Oder
 term    := factor { '&' factor }             Und
 factor  := '!' factor | '(' expr ')' | atom   Nicht, Klammern
 atom    := KEY OP VALUE
 KEY     := Level | BondTier | Item | TimeOfDay | Weather | Zone | Region | Moon | Knows | ChorHas
          | Personality | Temperament | WinsWhileHolding | StepsInRegion | Stat:<Wert>
 OP      := >= | <= | = | > | <
```

**Typregeln:** Zahl-Schlüssel (`Level`, `BondTier`, `WinsWhileHolding`, `StepsInRegion`) erlauben alle Operatoren; Kategorie-Schlüssel nur `=`; `Stat:<A>` vergleicht zwei aktuelle Werte (`Stat:Attack>Defense`).

**Werte:** `TimeOfDay` ∈ {Dawn, Day, Dusk, Night}; `Weather` ∈ {Clear, Rain, Thunderstorm, Fog, Snow, Heatwave, Sandstorm, Aurora, Ashfall, ResonanceStorm}; `Moon` ∈ 8 Phasen-Namen (CANON §66); `Region` R01–R10; `Zone` aus `Zones.csv`; `Item` aus `EvolutionItems.csv`; `BondTier` 1–6.

### 4.2 Beispiele

| Bedingung | Bedeutung |
|---|---|
| `Level>=16` | ab Level 16 |
| `Level>=30 & Weather=Rain` | ab Level 30, während es regnet |
| `BondTier>=4 & TimeOfDay=Night` | hohe Bindung, nachts |
| `Item=ITM_EVO_TIDE \| (Level>=40 & Zone=R06_Z05)` | Obertonkristall (Flut) **oder** Lv. 40 im Riffgrund |
| `Stat:Attack>Defense & Level>=28` | Endform hängt vom Körperbau ab (Zweig-Beispiel) |
| `!(Moon=NewMoon) & Level>=22` | nicht bei Neumond |

### 4.3 Validierung

`tools/ref/evo_condition.py` (Referenz-Parser mit Tests) wird vom Katalog-Validator für **jede** Bedingung aufgerufen: Syntax, bekannte Schlüssel, gültige Werte, existierende Items/Zonen, Wertebereiche. Ein ungültiger Ausdruck blockiert den Pre-Submit.

### 4.4 Auswertung im Spiel

Bedingungen werden **ereignisgetrieben** geprüft – nicht jeden Frame:

| Ereignis | Geprüfte Echos |
|---|---|
| `Event.Echo.LevelUp` | das betroffene Echo |
| `Event.World.WeatherChanged` / `TimeOfDayChanged` (Region des Spielers) | Chor (6) |
| Bindungsstufe steigt (K37) | betroffenes Echo |
| Item „Benutzen“ auf Echo | betroffenes Echo |
| Betreten einer Zone / Region | Chor |
| Lager-Moment geöffnet | Chor (vollständige Prüfung) |

---

## 5. Evolutions-Items

Daten: `Data/Items/EvolutionItems.csv` (25 Items).

| Gruppe | Items | Bezug |
|---|---|---|
| **Obertonkristalle** (15) | `ITM_EVO_<TYP>` – je ein Kristall mit eingeschlossener Typfrequenz | Fund, Crafting (K41), Händler; Leere-Kristall nur aus geheilten Stillezonen |
| **Spezialitems** (10) | Mondtau (R04), Aschefeder (R05), Gezeitenperle (R06), Glyphensplitter (R08), Aurorafaden (R07), Sternenstaub (R10), Wurzelherz (R01), Nebelschleier (R03), Glutkern (R05), Klangmuschel (R06) | an Weltereignisse gebunden (Vollmond, Springflut, Aurora …) |

**Regeln:** Items werden beim Auslösen verbraucht. Spezialitems entstehen **unter Weltbedingungen** (z. B. Mondtau nur nachts bei Vollmond auf Dünen) – damit sind auch Item-Evolutionen Entdeckungen (DR-15-Geist). Preise und Crafting-Rezepte: K41/K42.

---

## 6. Ablauf einer Evolution

```
 Bedingung erfüllt (Ereignis §4.4)
          │
          ▼
 ┌─────────────────────────────────┐
 │ EVOLUTIONSAHNUNG                │  Klangmal des Echos pulsiert doppelt; Begleiter zeigt Unruhe;
 │ (Zustand „bereit“ am Echo)       │  HUD-Hinweis „Fernlit spürt einen neuen Ton …“
 └───────────────┬─────────────────┘
                 │  nächster sicherer Moment: Kampfende, Lager, Menü (nie mitten im Kampf/Dialog)
                 ▼
 ┌─────────────────────────────────┐
 │ EVOLUTIONSDIALOG                │  Optionen: „Entwickeln“ · „Später“ · (bei Zweigen: Form wählen)
 └───────┬─────────────────┬───────┘
         │ Entwickeln       │ Später
         ▼                 ▼
 Evolutionssequenz        Zustand bleibt „bereit“, solange die Bedingung gilt.
 (6–10 s, überspringbar)  Zeit-/Wetterbedingungen müssen zum Auslösezeitpunkt erfüllt sein
         │                → Hinweis im Kodex: „Bei Regen erneut versuchen“.
         ▼                Level-/Bindungs-/Item-Evolutionen bleiben dauerhaft verfügbar
 Daten umschreiben (§7)    (Lager-Moment: „Tonart wechseln …“).
 Lernset prüfen, Kodex-Eintrag, Event.Echo.Evolved, Autosave
```

**Kontrolle (LOCKED):** Es gibt **keinen** Abbruch durch Tastendruck während der Sequenz (die Entscheidung fällt im Dialog). Option „Evolutionen immer automatisch annehmen“ in den Einstellungen (für Spieler, die es so wollen). „Später“ hat keine Kosten.

---

## 7. Was übertragen wird – und was sich ändert

| Feld (`FEchoInstance`) | Bei Evolution |
|---|---|
| InstanceId, Origin (Herkunft), Nickname | **bleibt** (DR-16) |
| Level, Experience | bleibt (EP-Kurve kann wechseln → EP wird auf die neue Kurve umgerechnet: gleicher **Fortschritt im aktuellen Level**) |
| Bond | bleibt; **+50** Bindung (Tonartwechsel gemeinsam erlebt) |
| Persönlichkeit, Temperament | bleibt |
| Genome (Anlagen, Loci, Mutationen) | bleibt |
| Morph | wird auf die **entsprechende Morph-Variante** der neuen Stufe abgebildet (Tabelle im Genetik-Fragment, K38) – Optik bleibt erkennbar verwandt |
| Polish (Schliff), PolishLocks | bleibt |
| Species | **neu** |
| Basiswerte, Typen, Größe, Archetyp | **neu** (aus neuer Spezies) – Werte sofort neu berechnet; HP-Anteil (Prozent) bleibt erhalten |
| Repertoire | bleibt + **Evolutionsfähigkeit** der neuen Stufe (falls definiert, K28–K30) + neue Lernset-Einträge ≤ Level |
| ActiveSlots | bleiben; wenn eine Evolutionsfähigkeit gelernt wird, bietet ein Dialog den Tausch an |
| PassiveAbility | wird auf die **gleichrangige** Passive der neuen Stufe abgebildet (Index 1→1, 2→2, versteckt→versteckt) |
| HeldItem | bleibt (außer es war das verbrauchte Evolutions-Item) |
| Kodex | Neue Art erhält Forschungsstufe 3 („durch Evolution beobachtet“), falls niedriger |

---

## 8. Pacing-Richtwerte

Richtwerte für Level-Schwellen (Validator gibt Warnungen, keine Fehler – Designfreiheit bleibt):

| Linie | Region der Basisform | Stufe 1 → 2 | Stufe 2 → 3 |
|---|---|---|---|
| 3-stufig | Akt I (R01, R02, R03, R06) | Lv. 14–22 | Lv. 30–38 |
| 3-stufig | Akt II (R04, R05, R07, R08) | Lv. 28–36 | Lv. 42–50 |
| 3-stufig | Akt III (R09, R10) | Lv. 40–48 | Lv. 56–62 |
| 2-stufig | Akt I | Lv. 20–30 | – |
| 2-stufig | Akt II | Lv. 34–44 | – |
| 2-stufig | Akt III | Lv. 50–58 | – |
| **Starterlinien** (LOCKED) | R01 | **Lv. 16** | **Lv. 34** |

**Abgleich mit der Story-Kurve (CANON §15):** Ende Akt I liegen Spieler-Echos bei ~Lv. 26–28 → Akt-I-Linien sind auf Stufe 2; die Starter erreichen Stufe 3 (Lv. 34) früh in Akt II – ein emotionaler Höhepunkt kurz nach dem Akt-Übergang (Pacing-Kurve K02 §10).

**Gehorsam (CANON §18):** Höherentwickelte gehandelte Echos unterliegen weiterhin der Gehorsamsgrenze; Evolution ändert daran nichts.

---

## 9. Entdeckbarkeit: Evolutionsahnung & Kodex

| Wissensstufe | Was der Spieler sieht |
|---|---|
| Kodex 1 (beobachtet) | „Diese Art scheint sich weiterentwickeln zu können.“ (nur, falls Evolution existiert) |
| Kodex 2 | Silhouette der nächsten Form; Hauptbedingungstyp als Symbol (Level/Bindung/Item/Welt) |
| Kodex 3 | Bedingung in Worten, ungefähre Zahlen („um Level 30, wenn es regnet“) |
| Kodex 4 | Exakte Bedingung inkl. Zweige; Akademie-Notiz (`KodexL4`) |
| Skill *Forschung* „Tonartgespür“ (K43) | Resonanzsinn zeigt Chor-Echos, die *unter aktuellen Weltbedingungen* bereit wären |

**Designregel DR-33 (neu):** Jede Evolutionsbedingung muss durch das Spiel selbst (Kodex, NPC-Hinweis, Lore) erlernbar sein – keine Bedingung darf nur über externe Wikis auffindbar sein. Validator prüft, dass `KodexL4` jeder Art mit Evolution die Bedingung inhaltlich erwähnt (Stichwortprüfung) – Detail im Lore-Review.

---

## 10. Präsentation

| Element | Spezifikation |
|---|---|
| Sequenz | 6–10 s: Kamera umkreist, Klangmal beginnt zu leuchten, Echo wird zu Lichtnoten-Silhouette (Shader-Morph über Dissolve + Notenpartikel), neue Silhouette formt sich, Klangmal in neuer Form, Jubel-Animation |
| Musik | Stinger: das Leitmotiv-Fragment der Region (CANON §56) wird in eine höhere Tonart moduliert (wörtlich ein „Tonartwechsel“) |
| Zweigwahl | Dialog zeigt beide Silhouetten nebeneinander mit Bedingungs-Symbolen |
| Fotomodus | Nach der Sequenz 5 s Pose für ein Foto (Kodex-Linse, K39) |
| Performance | Sequenz lädt das neue Mesh **vor** dem Start (Async, Ladezeit verdeckt durch Dialog); Budget ≤ 1 s Ladezeit |
| Zugänglichkeit | Blitz-/Flackerintensität gedrosselt bei „Lichteffekte reduzieren“ |

---

## 11. Online-Regeln

| Regel | Festlegung |
|---|---|
| Tauschevolutionen | **Gibt es nicht** (DR-19) |
| Evolution im Koop | Nur in der eigenen Instanz; Gäste können entwickeln (Bedingungen gelten in der Host-Welt: Wetter/Zeit des Hosts) |
| PvP | Keine Evolution im Kampf; Ranked-Teams sind fest |
| Herkunftssignatur | Evolution ändert die Signatur nicht; der Server prüft beim Online-Einsatz, ob die Art aus der Herkunftsart per gültiger Linie erreichbar ist (Anti-Cheat, K59) |

---

## 12. Code

### 12.1 Bedingung (C++, rekursiver Abstieg – Struktur identisch zur Python-Referenz)

```cpp
// GF_Monsters/Public/Evolution/EvoCondition.h
/** Kontext für die Auswertung (vom EvolutionService aus Echo, Welt und Inventar befüllt). */
struct FEvoContext
{
	int32 Level = 1;
	int32 BondTier = 1;
	FGameplayTag TimeOfDay, Weather, Moon, Personality, Temperament;
	FName Zone, Region;
	TSet<FName> Items;           // verfügbare Evolutions-Items im Inventar
	TSet<FName> KnownAbilities;
	FGameplayTagContainer ChorTypes;
	TMap<FName, int32> Counters; // WinsWhileHolding, StepsInRegion
	FEchoStats Stats;
};

/** Kompilierte Bedingung (AST). Wird beim Laden der Spezies einmal geparst (Fehler → Data-Validation). */
class GF_MONSTERS_API FEvoCondition
{
public:
	static TOptional<FEvoCondition> Parse(const FString& Source, FString& OutError);
	bool Evaluate(const FEvoContext& Ctx) const;
	/** Welche Ereignisse eine Neuprüfung auslösen (Optimierung §4.4). */
	FGameplayTagContainer GetTriggeringEvents() const;
	/** Für Kodex-Text: Hauptbedingungstyp (Level/Bond/Item/World/Other). */
	FGameplayTag GetPrimaryKind() const;

private:
	enum class ENodeKind : uint8 { And, Or, Not, Atom };
	struct FNode { ENodeKind Kind; int32 Left = INDEX_NONE, Right = INDEX_NONE; FName Key; FName Op; FString Value; FName StatA; };
	TArray<FNode> Nodes;   // flache Speicherung, Index 0 = Wurzel
	bool EvalNode(int32 Index, const FEvoContext& Ctx) const;
};
```

```cpp
// Private/Evolution/EvoCondition.cpp (Auszug: Atom-Auswertung)
bool FEvoCondition::EvalNode(int32 I, const FEvoContext& C) const
{
	const FNode& N = Nodes[I];
	switch (N.Kind)
	{
	case ENodeKind::And: return EvalNode(N.Left, C) && EvalNode(N.Right, C);
	case ENodeKind::Or:  return EvalNode(N.Left, C) || EvalNode(N.Right, C);
	case ENodeKind::Not: return !EvalNode(N.Left, C);
	default: break;
	}
	auto Cmp = [&N](int32 A, int32 B)
	{
		if (N.Op == ">=") return A >= B; if (N.Op == "<=") return A <= B;
		if (N.Op == ">")  return A > B;  if (N.Op == "<")  return A < B;
		return A == B;
	};
	if (N.Key == "Level")     return Cmp(C.Level, FCString::Atoi(*N.Value));
	if (N.Key == "BondTier")  return Cmp(C.BondTier, FCString::Atoi(*N.Value));
	if (N.Key == "Item")      return C.Items.Contains(FName(*N.Value));
	if (N.Key == "Knows")     return C.KnownAbilities.Contains(FName(*N.Value));
	if (N.Key == "Zone")      return C.Zone == FName(*N.Value);
	if (N.Key == "Region")    return C.Region == FName(*N.Value);
	if (N.Key == "Weather")   return C.Weather.GetTagName() == FName(*(TEXT("Weather.") + N.Value));
	if (N.Key == "TimeOfDay") return C.TimeOfDay.GetTagName() == FName(*(TEXT("TimeOfDay.") + N.Value));
	if (N.Key == "Moon")      return C.Moon.GetTagName() == FName(*(TEXT("Moon.") + N.Value));
	if (N.Key == "ChorHas")   return C.ChorTypes.HasTagExact(FGameplayTag::RequestGameplayTag(FName(*N.Value)));
	if (N.Key == "Stat")      return Cmp(StatValue(C.Stats, N.StatA), StatValue(C.Stats, FName(*N.Value)));
	if (const int32* V = C.Counters.Find(N.Key)) { return Cmp(*V, FCString::Atoi(*N.Value)); }
	return false;
}
```

### 12.2 Evolution ausführen

```cpp
// GF_Monsters/Private/Evolution/EvolutionService.cpp (Auszug)
bool UEvolutionService::Evolve(FEchoInstance& Echo, FPrimaryAssetId TargetSpecies)
{
	const UEchoSpeciesDefinition* From = Species(Echo.Species);
	const UEchoSpeciesDefinition* To = Species(TargetSpecies);
	if (!From || !To || !IsValidStep(*From, *To)) { return false; }    // gleiche Linie, Stufe + 1 bzw. Zweig

	const int32 HpPercentPermille = Echo.CurrentHP * 1000 / FMath::Max(1, StatsService->ComputeStats(Echo).HP);
	const float LevelProgress = ExpProgressInLevel(Echo, From->GrowthRate);  // Anteil im aktuellen Level

	Echo.Species = TargetSpecies;
	Echo.Experience = ExpForLevel(To->GrowthRate, Echo.Level)
	                + FMath::FloorToInt64(LevelProgress * ExpSpan(To->GrowthRate, Echo.Level));
	Echo.Bond = FMath::Min(1000, Echo.Bond + 50);
	Echo.Genome.Morph = GeneticsMap->MapMorph(From, To, Echo.Genome.Morph);
	Echo.PassiveAbility = MapPassive(*From, *To, Echo.PassiveAbility);
	LearnEvolutionAbilities(Echo, *To);
	Echo.CurrentHP = StatsService->ComputeStats(Echo).HP * HpPercentPermille / 1000;
	ConsumeEvolutionItemIfAny(Echo, *From, *To);

	UAethrisEventBus::Get(this).Broadcast(AethrisTags::Event_Echo_Evolved,
		FEchoEvolvedMsg{ Echo.InstanceId, From->GetPrimaryAssetId(), TargetSpecies });
	return true;
}
```

### 12.3 Tests

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Monsters.EvoCondition.PythonParity` | 500 Ausdrücke aus den Katalogdaten + Zufallskontexte: C++ = Python |
| `Aethris.Unit.Monsters.Evolution.Transfer` | Tabelle §7 (InstanceId, Bindung +50, HP-Anteil, EP-Fortschritt) |
| `Aethris.Unit.Monsters.Evolution.Branch` | Beide Bedingungen erfüllt → Auswahl; nur eine → automatisch richtige Form |
| `Aethris.Functional.Monsters.EvolutionSequence` | Sequenz ohne Hitch (Async-Load ≤ 1 s) |

---

## 13. Decision Records

### ADR-088 – Bedingungssprache statt fester Evolutions-Enums
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Enum-Typen (LevelUp, Item, Friendship …) | Einfach | Kombinationen (Briefing!) kaum abbildbar |
| (b) Kleine DSL mit Parser, Validator, Python-Referenz | Beliebige Kombinationen, datengetrieben (DR-25), maschinell prüfbar | Parserpflege, Designer müssen Syntax lernen → Editor-Widget mit Bausteinen (K05 Tools) |
- **Entscheidung:** (b).

### ADR-089 – Keine tauschgebundenen Evolutionen
- **Entscheidung:** DR-19; Online ist Bonus, nie Voraussetzung.

### ADR-090 – Spieler kontrolliert jede Evolution, „Später“ kostenlos
- **Entscheidung:** Siehe §6. Vorteil: Spieler-Autonomie, strategisches Zurückhalten (z. B. Lernset der Vorstufe). Nachteil: Mehr UI → automatische Annahme als Option.

### ADR-091 – Evolution gibt +50 Bindung
- **Entscheidung:** Erzählerisch („gemeinsam erlebter Tonartwechsel“), mechanisch klein. Unterstützt S2.

### ADR-092 – Spezialentwicklungen brauchen eine Weltbedingung
- **Entscheidung:** Zweige sind Entdeckungen (S1/S2), keine Kaufentscheidung; verbindet Evolution mit Wetter, Zeit, Mond und Orten.

---

## 14. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §84 | Formen: Single 22, Two 45, Three 40, Branch 8 (alternative Endformen, gleiche Gattung/Stufe, Kernsumme ±10, ≥ 1 Weltbedingung, Spielerwahl bei Gleichzeitigkeit); Legendäre/Mythische ohne Evolution | LOCKED |
| §84 | Auslöser-Verteilungsziele: Level 55 % · Level+Welt 18 % · Bindung 10 % · Item 10 % · Sonstige 7 % | LOCKED (Ziel) |
| §85 | Bedingungssprache (Grammatik §4.1, Schlüssel, Operatoren, Wertebereiche); Referenz `tools/ref/evo_condition.py`; Validierung im Katalog; ereignisgetriebene Prüfung (§4.4); C++ `FEvoCondition` (flacher AST) | LOCKED |
| §86 | Ablauf: Evolutionsahnung → Dialog am sicheren Moment → Sequenz 6–10 s; „Später“ kostenlos; Option Auto-Annahme; Welt-Bedingungen müssen beim Auslösen gelten | LOCKED |
| §86 | Übertragung (§7): bleibt alles außer Spezies/Basiswerte/Typen/Größe; EP-Fortschritt im Level erhalten; HP-Anteil erhalten; Bindung +50; Morph und Passive abgebildet; Evolutionsfähigkeit gelernt; Kodex der neuen Art ≥ Stufe 3 | LOCKED |
| §86 | Keine Tauschevolutionen; Koop: Host-Weltbedingungen; Server prüft Linien-Erreichbarkeit | LOCKED |
| §87 | 25 Evolutions-Items (`EvolutionItems.csv`): 15 Obertonkristalle `ITM_EVO_<TYP>` + 10 Spezialitems an Weltereignisse gebunden; Verbrauch beim Auslösen | LOCKED |
| §88 | Pacing-Richtwerte (§8); **Starter: Lv. 16 und Lv. 34** | LOCKED |
| §13 | DR-33: Jede Evolutionsbedingung ist im Spiel erlernbar (Kodex 2–4, NPC, Lore) | LOCKED |
| §10 | ADR-088 – ADR-092 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Evolution als Tonartwechsel (Weltlogik) und Designziele
- [x] Alle Briefing-Formen: keine, zwei-, dreistufig, Spezialentwicklung (Zweige)
- [x] Alle Briefing-Auslöser: Level, Freundschaft (Bindung), Items, Tageszeit, Wetter, Gebiet, Kombinationen (+ Mond, Fähigkeit, Chor, Leistung, Wertverhältnis)
- [x] Bedingungssprache mit Grammatik, Parser-Referenz (getestet) und Validator-Integration
- [x] 25 Evolutions-Items als Daten
- [x] Ablauf, Spielerkontrolle, Übertragungsregeln
- [x] Pacing-Richtwerte inkl. Starter-Schwellen
- [x] Entdeckbarkeit (Kodex-Stufen, Skill, DR-33)
- [x] Präsentation, Online-Regeln
- [x] Code (Parser/AST, Evolutionsausführung), Tests
- [x] ADR-088 – ADR-092, CANON aktualisiert

➡️ **Nächstes Kapitel: K20 – Kreaturenkatalog 1 (#001–#032, Verdanthain).**
