# K48 · Quest-Bibel und Questsystem-Technik

| Feld | Wert |
|---|---|
| Dokument | Kapitel 48 von 68 |
| Version | 1.0 |
| Owner | Lead Quest Designer, Gameplay Programmer (GF_Quests) |
| Mitwirkende | Narrative Director, Lead Writer, UI Designer, QA Lead, Tools Programmer |
| Baut auf | K02 (Säulen, DR-01–DR-33), K03 §7 (Content-Verteilung), K06 (Services, Events, Datenpipeline), K13 §4 (Aufträge), K39 (Kodex-Aufgaben), K43 (Wärter-EP), K44–K46 (Hauptstory), K47 (Fraktionen, Ruf) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Quests/ObjectiveTypes.csv` (21 Zieltypen), `MainQuestSteps.csv` (98 Schritte), `SideQuests.csv` (210 Nebenquest-Gerüste), `Data/World/StoryPOIs.csv`, `tools/gen_quests.py` (Validator QV-01–QV-10), `tools/authoring/sq_plan.py`, `QuestDefinition.h`, `Services/QuestService.h` |
| Neue Kanon-Einträge | CANON §185 (Questarten und Regeln), §186 (Questdaten und Zieltypen), §187 (Nebenquest-Gerüst), §188 (Questsystem-Technik) |

---

## Inhalt

1. [Questarten](#1-questarten)
2. [Die Quest-Bibel: zwölf Regeln](#2-die-quest-bibel-zwölf-regeln)
3. [Schreibregeln](#3-schreibregeln)
4. [Nebenquest-Gerüst](#4-nebenquest-gerüst)
5. [Anatomie einer Quest](#5-anatomie-einer-quest)
6. [Bedingungssprache](#6-bedingungssprache)
7. [Hauptquest-Schritte](#7-hauptquest-schritte)
8. [Belohnungen](#8-belohnungen)
9. [Hinweise, Tagebuch, Markierungen](#9-hinweise-tagebuch-markierungen)
10. [Questsystem-Technik](#10-questsystem-technik)
11. [Validator und Tests](#11-validator-und-tests)
12. [Produktionspipeline](#12-produktionspipeline)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Questarten

| Art | ID | Anzahl | Wiederholbar | Inhalt | Kapitel |
|---|---|---|---|---|---|
| **Hauptquest** | `MQ_P##`, `MQ_A#_##` | 32 | nein | Story, Wahrheiten W1–W9, Akkorde | K44–K46 |
| **Nebenquest** | `SQ_###` | 210 | nein | Geschichten von Menschen, Echos, Orten | K49–K51 |
| **Fraktionskette** | `FQ_F##_##` | 18 | nein | Container aus 3–6 Nebenquests einer Fraktion, Rangeinstieg | K47, K49–K51 |
| **Auftrag** | `CT_R##_##` | Vorlagen 10 | ja (Abklingzeit) | Beobachten, Liefern, Retten … | K13 §4 |
| **Kodex-Aufgabe** | `KT_*` | je Art | nein | Forschung an Arten | K39 |
| **Weltereignis** | `WE_*` | ~40 | zyklisch | Resonanzsturm-Nächte, Mondfeste, Ausbrüche | K14/K15, K62 |
| **Echo-Bitte** | `EB_*` | prozedural | ja | Spontane Mini-Bitten eines Begleiters (30–90 s) | K37 |

**Abgrenzung:** Nur Haupt- und Nebenquests sind „Quests“ im Tagebuch mit eigener Geschichte. Aufträge und Echo-Bitten erscheinen im Bereich „Aufgaben“; Kodex-Aufgaben im Kodex. So bleibt das Tagebuch lesbar (ADR-182).

---

## 2. Die Quest-Bibel: zwölf Regeln

| Regel | Inhalt | Bezug |
|---|---|---|
| **QR-01 Jede Quest erzählt** | Jede Haupt- und Nebenquest hat einen Anlass, eine Wendung und eine Auflösung; „bring mir 10 X“ ist ein Auftrag, keine Quest | S5 |
| **QR-02 Verstehen vor Kämpfen** | Jede Nebenquest enthält mindestens einen Schritt, der über Beobachten, Untersuchen, Zuhören oder Entscheiden läuft | S2, DR-01 |
| **QR-03 Kein reines Sammeln** | `OBJ_COLLECT` ist nie der einzige oder der letzte Schritt einer Quest | – |
| **QR-04 Dritte Lösung** | Dilemmata zwischen Fraktionen bieten eine Option, die über Verstehen statt Parteinahme läuft (K47 §7) | K47 |
| **QR-05 Sichtbare Folgen** | Jede Nebenquest verändert sichtbar etwas in der Welt (NPC-Position, Echo-Population, Gebäude, Bark), mindestens bis zum Nachhall | DR-13 |
| **QR-06 Keine Zeitnot** | Keine Echtzeit-Timer, keine Fristen in Quests (Fristen nur in Aufträgen); keine Quest scheitert durch Warten | DR-23 |
| **QR-07 Ein Hinterhalt** | Höchstens ein angekündigter Hinterhalt pro Quest; Begegnungen sind sichtbar | DR-14 |
| **QR-08 Niemand stirbt durch den Spieler** | Gegner werden erschöpft, Menschen fliehen, geben auf, werden gestellt | ADR-007 |
| **QR-09 Tagesphase und Wetter** | ≥ 25 % der Nebenquests einer Region nutzen Tageszeit, Wetter oder Mond (Bedingung oder Variante) | DR-32, DR-13 |
| **QR-10 Belohnungsmischung** | Keine Quest belohnt nur mit Sol; mindestens eine nicht-monetäre Belohnung (Kodex, Fragment, Echo-Begegnung, Rezept, Ruf, Hain-Dekor) | DR-27, DR-31 |
| **QR-11 Allein spielbar** | Jede Quest ist allein lösbar; Koop ändert Schwierigkeit, nicht den Zugang | DR-19 |
| **QR-12 L-01** | Keine Lore über der Wahrheitsebene des Spielstands; Nebenquests mit Story-Bezug haben `TruthLevel` und warten oder verzerren | CANON §38 |

**Länge:** Nebenquests 15–45 min (Ziel Ø 35 min), 3–6 Schritte; Kettenquests bis 60 min. Hauptquests 40–200 min (K44–K46).

**Intensität:** Nebenquests haben Intensität 1–6; ≥ 7 nur für Kettenabschlüsse, dann mit Atemzug danach (DR-29).

---

## 3. Schreibregeln

| Bereich | Regel |
|---|---|
| **Titel** | 2–5 Wörter, bildhaft, kein Spoiler („Die Glocke von Kaldra“, nicht „Rette den Glockengießer“) |
| **Auftraggeber** | Jede Nebenquest hat einen benannten NPC oder ein Echo als Auslöser; je NPC höchstens 3 Geschichten – eine Fraktionskette zählt als eine Geschichte (außer Fraktionsoberhäupter) |
| **Tagebuchtext** | Ich-Perspektive des Wärters, 1–2 Sätze je Schritt, Präsens („Ich soll herausfinden, warum …“) |
| **Dialog** | Zeilen ≤ 160 Zeichen; Auswahlantworten in drei Haltungen (ADR-162) bei jeder Entscheidung; Schweigegelübde des Ordens: Schiefertafel ≤ 80 Zeichen (CANON §55) |
| **Barks** | Jede Nebenquest liefert 3–6 Barks für die Zeit danach (QR-05), Tag `Quest.<ID>.After` |
| **Namen** | Regionale Klangfamilien (CANON §22), Namensprüfung über `nameguard` (K04) |
| **Humor** | In Figuren, nicht in Erzählerstimme; nie auf Kosten von Echos oder Kulturen |
| **Sensitivität** | R04/R07-Quests mit Sensitivity-Review (CANON §22); Trauer (Eiðvik) ohne Ausschlachtung |
| **Echos** | Echos „sprechen“ nonverbal; Untertitel beschreiben Laut und Haltung („*[summt tief, Ohren angelegt]*“) |

---

## 4. Nebenquest-Gerüst

Die 210 Nebenquests sind nach Regionsbudget (`RegionBudget.csv`, CANON §19) und Akt-Reihenfolge nummeriert. Das Gerüst legt **Region, Kategorie, Fraktion, Verfügbarkeit und Kette** jeder Quest fest; Titel, Auftraggeber und Inhalt schreiben K49–K51.

### 4.1 Regionen und Kategorien

| Region | IDs | Anzahl | Fraktion | Echo-Geschichte | Menschen | Forschung | Rätsel & Ruinen | Wärterprüfung | Weltereignis | Kapitel |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | SQ_001–SQ_024 | 24 | 14 | 2 | 2 | 2 | 2 | 1 | 1 | K49 |
| R02 | SQ_025–SQ_046 | 22 | 13 | 1 | 2 | 2 | 2 | 1 | 1 | K49 |
| R03 | SQ_047–SQ_067 | 21 | 12 | 1 | 1 | 2 | 2 | 2 | 1 | K49 |
| R06 | SQ_068–SQ_090 | 23 | 13 | 2 | 1 | 1 | 2 | 2 | 2 | K49, K50 |
| R04 | SQ_091–SQ_112 | 22 | 13 | 2 | 1 | 1 | 1 | 2 | 2 | K50 |
| R05 | SQ_113–SQ_131 | 19 | 11 | 2 | 1 | 1 | 1 | 1 | 2 | K50 |
| R07 | SQ_132–SQ_151 | 20 | 11 | 2 | 2 | 2 | 1 | 1 | 1 | K50, K51 |
| R08 | SQ_152–SQ_172 | 21 | 12 | 1 | 2 | 2 | 2 | 1 | 1 | K51 |
| R09 | SQ_173–SQ_190 | 18 | 10 | 1 | 1 | 2 | 2 | 1 | 1 | K51 |
| R10 | SQ_191–SQ_210 | 20 | 11 | 1 | 1 | 1 | 2 | 2 | 2 | K51 |
| **Σ** |  | 210 | 120 | 15 | 14 | 16 | 17 | 14 | 14 |  |

| Kategorie | Inhalt | Typische Zieltypen |
|---|---|---|
| Fraktion | Aufträge mit Geschichte einer Fraktion; Teil der 120 Fraktionsquests (K47) | TALK, INVESTIGATE, CHOICE, DELIVER |
| Echo-Geschichte | Ein einzelnes Echo oder eine Herde mit Problem (verletzt, verirrt, Revierkonflikt) | OBSERVE, ESCORT, HEALZONE |
| Menschen | Familien, Händler, Handwerker; Beziehungen zwischen Menschen und Echos | TALK, CHOICE, DELIVER |
| Forschung | Kodex-nahe Rätsel: Verhalten, Evolution, Regionalformen | OBSERVE, PHOTO, INVESTIGATE |
| Rätsel & Ruinen | Dorunische Glyphen, Wendelin-Seiten, Akkord-Säulen | PUZZLE, INVESTIGATE, TRAVERSE |
| Wärterprüfung | Besondere Kämpfe mit Regeln (Formation, Wetter, nur ein Typ) | BATTLE |
| Weltereignis | An Wetter, Mond, Sturm oder Ausbruch gebunden | CONDITION, GOTO, OBSERVE |

### 4.2 Fraktionen und Ketten

| Fraktion | Quests | Regionen | Ketten |
|---|---|---|---|
| F01 | 27 | R01 3, R02 2, R03 2, R06 1, R04 5, R07 1, R08 6, R09 4, R10 3 | FQ_F01_01, FQ_F01_02, FQ_F01_03, FQ_F01_04 |
| F02 | 27 | R01 3, R02 4, R06 7, R04 3, R05 5, R09 3, R10 2 | FQ_F02_01, FQ_F02_02, FQ_F02_03, FQ_F02_04 |
| F03 | 28 | R01 5, R02 6, R03 2, R06 2, R04 1, R05 2, R07 4, R08 1, R09 2, R10 3 | FQ_F03_01, FQ_F03_02, FQ_F03_03, FQ_F03_04 |
| F04 | 26 | R01 3, R02 1, R03 6, R06 3, R04 4, R05 4, R07 1, R08 2, R10 2 | FQ_F04_01, FQ_F04_02, FQ_F04_03, FQ_F04_04 |
| F05 | 12 | R03 2, R07 5, R08 3, R09 1, R10 1 | FQ_F05_01, FQ_F05_02 |

Jede Kette `FQ_F##_##` umfasst 4 Quests (Orden: 2 Ketten à 6 – FQ_F05_01 ab Akt III, FQ_F05_02 bis in den Nachhall), beginnt beim Rufrang ihres Index (Kette 1 ab Rang 1 … Kette 4 ab Rang 4, K47) und endet mit einem Kettenabschluss (+400 Ruf). Fraktionsquests außerhalb von Ketten sind frei zugänglich.

### 4.3 Verfügbarkeit

| Region | Akt I | Akt II | Akt III | Nachhall |
|---|---|---|---|---|
| R01 | 21 | 1 | 1 | 1 |
| R02 | 19 | 1 | 1 | 1 |
| R03 | 16 | 1 | 3 | 1 |
| R06 | 20 | 1 | 1 | 1 |
| R04 | 0 | 19 | 2 | 1 |
| R05 | 0 | 13 | 3 | 3 |
| R07 | 0 | 11 | 6 | 3 |
| R08 | 0 | 13 | 3 | 5 |
| R09 | 0 | 0 | 12 | 6 |
| R10 | 0 | 0 | 13 | 7 |
| **Σ** | 76 | 60 | 45 | 29 |

**Regel:** Jede dritte ungekettete Nebenquest einer Region (zusammen mit den Ordensquests ~25 %) öffnet erst in einem späteren Akt oder im Nachhall; Kettenquests bleiben im Akt ihrer Region. So lohnt die Rückkehr in alte Regionen (CANON §42: ≥ 3 Rückkehr-POIs je Region), und Spätquests können auf spätere Wahrheiten eingehen (QR-12). Ordensquests (F05) öffnen frühestens in Akt III (ADR-180).

### 4.4 Datenfelder

| Name | RegionId | Category | Faction | Available | Chain | Chapter |
|---|---|---|---|---|---|---|
| SQ_001 | R01 | FACTION | F01 | Akt I | FQ_F01_01 | K49 |
| SQ_002 | R01 | ECHO | – | Akt I |  | K49 |
| SQ_003 | R01 | FACTION | F01 | Akt I | FQ_F01_01 | K49 |
| SQ_004 | R01 | ECHO | – | Akt I |  | K49 |
| SQ_005 | R01 | FACTION | F01 | Akt I | FQ_F01_01 | K49 |
| SQ_006 | R01 | EVENT | – | Akt II |  | K49 |
| SQ_007 | R01 | FACTION | F02 | Akt I | FQ_F02_01 | K49 |
| SQ_008 | R01 | MYSTERY | – | Akt I |  | K49 |
| SQ_009 | R01 | FACTION | F02 | Akt I | FQ_F02_01 | K49 |
| SQ_010 | R01 | MYSTERY | – | Akt I |  | K49 |
| SQ_011 | R01 | FACTION | F02 | Akt I | FQ_F02_01 | K49 |
| SQ_012 | R01 | PEOPLE | – | Akt III |  | K49 |
| SQ_013 | R01 | FACTION | F03 | Akt I | FQ_F03_01 | K49 |
| SQ_014 | R01 | PEOPLE | – | Akt I |  | K49 |
| SQ_015 | R01 | FACTION | F03 | Akt I | FQ_F03_01 | K49 |
| SQ_016 | R01 | RESEARCH | – | Akt I |  | K49 |
| SQ_017 | R01 | FACTION | F03 | Akt I | FQ_F03_01 | K49 |
| SQ_018 | R01 | RESEARCH | – | Nachhall |  | K49 |
| SQ_019 | R01 | FACTION | F03 | Akt I | FQ_F03_01 | K49 |
| SQ_020 | R01 | TRIAL | – | Akt I |  | K49 |
| SQ_021 | R01 | FACTION | F03 | Akt I | FQ_F03_02 | K49 |
| SQ_022 | R01 | FACTION | F04 | Akt I | FQ_F04_01 | K49 |
| SQ_023 | R01 | FACTION | F04 | Akt I | FQ_F04_01 | K49 |
| SQ_024 | R01 | FACTION | F04 | Akt I | FQ_F04_01 | K49 |

*(Auszug R01; vollständig in `Data/Quests/SideQuests.csv`.)* K49–K51 ergänzen je Quest: `Title`, `Giver`, `Location`, `Intensity`, `TruthLevel`, `DurationMin`, `Steps` (in `SideQuestSteps.csv`), `Rewards`, `Variant` (Tageszeit/Wetter/Mond), `Consequence` (QR-05).

---

## 5. Anatomie einer Quest

```
                       ┌───────────────────────── Quest ─────────────────────────┐
  Vorbedingung ──►     │ Angebot ─► Annahme ─► Schritt 1 ─► … ─► Schritt n ─► Abschluss │ ──► Folgen
  (Bedingungssprache)  │  (Giver,    (Tagebuch)  (Zieltyp,      (Zieltyp,    (Belohnung, │     (Flags, Barks,
                       │   Hinweis)               Ziel, Ort)     Meilenstein)  Ruf, EP)   │      Data Layer)
                       └──────────────────────────────────────────────────────────┘
```

| Element | Pflicht | Inhalt |
|---|---|---|
| Vorbedingung | ja | Ausdruck der Bedingungssprache (§6); bei Nebenquests mindestens `Available`-Akt |
| Angebot | ja | Giver (NPC/Echo/Brett/Fund), Hinweistext, optionaler Dialog |
| Schritte | 1–8 | Zieltyp, Ziel, Anzahl, Ort, Meilenstein, optionale Bedingung |
| Verzweigung | optional | `OBJ_CHOICE` setzt Flags; folgende Schritte können per Bedingung variieren |
| Abschluss | ja | Belohnung (§8), Ruf (K47), Flags, Folgen (QR-05) |

### 5.1 Zieltypen

| Name | DisplayName | Params | Completion | Hint | Pillar |
|---|---|---|---|---|---|
| OBJ_TALK | Sprechen | NPC | Dialogende mit Knoten Complete | Name im Kompass | S5 |
| OBJ_GOTO | Ort erreichen | Location|Radius | Spieler im Radius | Ziel auf Karte (ungefähr) | S1 |
| OBJ_INVESTIGATE | Untersuchen | Location|Clues | Alle Hinweise mit Resonanzsinn gefunden | Resonanzsinn pulsiert stärker | S2 |
| OBJ_OBSERVE | Beobachten | Species|Trait | Verhaltensmerkmal im Kodex erfasst | Kodex-Eintrag markiert | S2 |
| OBJ_PHOTO | Fotografieren | Species|Stars | Foto mit ≥ Sternen | Kodex-Linse zeigt Rahmen | S2 |
| OBJ_BOND | Binden | Species|Count | Bindung erfolgreich | – | S2 |
| OBJ_BATTLE | Wärterkampf | Trainer|Format | Kampf gewonnen oder Story-Niederlage | Gegner sichtbar | S3 |
| OBJ_BOSS | Bosskampf | Boss | Boss besiegt (oder Phase 4 bei Velnox) | Arena-Eingang | S3 |
| OBJ_ARENA | Arena | Arena | Akkord erhalten | Arena-Banner | S3 |
| OBJ_HEALZONE | Stillezone heilen | Zone|Circles | Alle Heilkreise geschlossen | Graue Ränder auf der Karte | S2 |
| OBJ_COLLECT | Sammeln | Item|Count | Anzahl im Inventar | Material-Symbol | S1 |
| OBJ_DELIVER | Liefern | Item|NPC | Übergabe | Name im Kompass | S1 |
| OBJ_ESCORT | Begleiten | NPC|Location | NPC erreicht Ziel | NPC-Symbol | S1 |
| OBJ_TRAVERSE | Traversal | Mount|Location | Ziel mit Fähigkeit erreicht | Traversal-Symbol | S1 |
| OBJ_PUZZLE | Rätsel | PuzzleId | Rätsel gelöst | – | S1 |
| OBJ_CHOICE | Entscheidung | ChoiceId | Option gewählt | – | S5 |
| OBJ_CINEMATIC | Zwischensequenz | SequenceId | Sequenz beendet oder übersprungen | – | S5 |
| OBJ_REST | Lager-Moment | Location | Lager aufgeschlagen und Gespräch(e) geführt | Lagerfeuer-Symbol | S5 |
| OBJ_FLEE | Flucht | Route | Ausgang erreicht | Pfeile an Wänden | S3 |
| OBJ_CONDITION | Bedingung | Condition | Bedingung erfüllt | Hinweis im Tagebuch | S4 |
| OBJ_DECIDE_ENDING | Finale Entscheidung | – | Ende gewählt | – | S5 |

**Neue Zieltypen** sind neue „Primitiva“ im Sinne von DR-25 (Content ohne neuen C++-Code, außer neue Primitiva): Sie brauchen ein Tech-Review und einen Eintrag in `ObjectiveTypes.csv`. Alles andere – jede einzelne Quest – entsteht ohne Programmierung.

### 5.2 Verwendung in den Hauptquests

| Zieltyp | Hauptquest-Schritte |
|---|---|
| OBJ_ARENA | 10 |
| OBJ_BATTLE | 2 |
| OBJ_BOND | 1 |
| OBJ_BOSS | 10 |
| OBJ_CHOICE | 8 |
| OBJ_CINEMATIC | 7 |
| OBJ_COLLECT | 0 |
| OBJ_CONDITION | 5 |
| OBJ_DECIDE_ENDING | 1 |
| OBJ_DELIVER | 1 |
| OBJ_ESCORT | 0 |
| OBJ_FLEE | 1 |
| OBJ_GOTO | 15 |
| OBJ_HEALZONE | 5 |
| OBJ_INVESTIGATE | 9 |
| OBJ_OBSERVE | 0 |
| OBJ_PHOTO | 0 |
| OBJ_PUZZLE | 2 |
| OBJ_REST | 5 |
| OBJ_TALK | 13 |
| OBJ_TRAVERSE | 3 |

---

## 6. Bedingungssprache

Vorbedingungen, Schrittbedingungen und Dialogzweige nutzen eine kleine, deterministische Ausdruckssprache (ADR-183). Sie wird zur Ladezeit in einen Syntaxbaum übersetzt und nur bei relevanten Ereignissen neu ausgewertet.

```
Ausdruck   := Oder
Oder       := Und ( "|" Und )*
Und        := Nicht ( "&" Nicht )*
Nicht      := "!" Nicht | Vergleich | "(" Ausdruck ")"
Vergleich  := Wert ( ">=" | "<=" | "==" | "!=" | ">" | "<" ) Zahl | Prädikat
Wert       := "Akkorde" | "AktIIAkkorde" | "Rang" | "Rank." Fraktion | "Flag." Name | "Bond." EchoArt | "Kodex." Art
Prädikat   := "Quest." Id | "Act=" Akt | "Act>=" Akt | "Time=" Tagesphase | "Weather=" Wetter | "Moon=" Phase
              | "Region=" R## | "Ending=" (NewSong|SoftSilence) | "Truth>=" W#
```

| Beispiel | Bedeutung |
|---|---|
| `Akkorde>=4 & Quest.MQ_A1_06` | Vorbedingung von MQ_A1_08 |
| `Act=Akt III & Rank.F05>=2` | Ordensladen öffnet |
| `Time=Night & Weather=Fog` | Nebenquest-Variante im Morvenmoor |
| `Flag.FS_STANCE>=0 \| Rank.F04>=4` | Freie Stimmen bieten Zellenquest an (Haltung oder Taten, ADR-178) |
| `Truth>=W6` | Nebenquest mit Kronensplitter-Bezug wird freigegeben (QR-12) |
| `Moon=Full & Region=R07` | Weltereignis „Polarlicht-Chor“ |

**Regeln:** Keine Zufallsfunktionen (Determinismus, Koop-Synchronität); keine Echtzeit (DR-23); Auswertung ohne Seiteneffekte. Unbekannte Namen sind Validator-Fehler (QV-Bedingungen in K49–K51).

---

## 7. Hauptquest-Schritte

Alle 32 Hauptquests sind in `MainQuestSteps.csv` in Schritte zerlegt. Schritte mit **Meilenstein** vergeben Wärter-EP (§8). Story-Orte ohne Siedlung sind in `Data/World/StoryPOIs.csv` registriert (Nummernkreis 9001+, CANON §23).

| Name | RegionId | DisplayName |
|---|---|---|
| POI_R01_9001 | R01 | Ruine am Lindwald (Gleiter-Fund) |
| POI_R03_9001 | R03 | Versunkener Turm unter Morvenfurt |
| POI_R04_9001 | R04 | Glasebene-Turm |
| POI_R04_9002 | R04 | Akademie-Grabung am Sonnenhof-Plateau |
| POI_R05_9001 | R05 | Kontor-Lager am Kraterrand |
| POI_R07_9001 | R07 | Ruinen von Eiðvik |
| POI_R07_9002 | R07 | Gletscher über der Gletscherwacht |
| POI_R08_9001 | R08 | Thronsaal-Gewölbe des Archon Maedryn |
| POI_R08_9002 | R08 | Akademie-Gewölbe unter der Halle der Grundfrequenzen |
| POI_R09_9001 | R09 | Resonanzkammer von Prismara |
| POI_R09_9002 | R09 | Tiefste Missklang-Adern |
| POI_R10_9001 | R10 | Kronenwerft |

### 7.1 Schrittliste

| Name | Quest | Objective | Target | Location | Milestone | Text |
|---|---|---|---|---|---|---|
| STEP_P01_01 | MQ_P01 | OBJ_CINEMATIC | SEQ_P01_COLDOPEN | R01 | 0 | Kalte Eröffnung: Nimbara-Vision |
| STEP_P01_02 | MQ_P01 | OBJ_TALK | NPC_YSOLDE | SET_V_LINDWIESEN | 0 | Ysolde und Kael am Waldrand |
| STEP_P01_03 | MQ_P01 | OBJ_INVESTIGATE | CLUE_P01_SILENCE | R01_Z01 | 0 | Die Stille im Lindwald mit dem Resonanzsinn verfolgen |
| STEP_P01_04 | MQ_P01 | OBJ_BOND | STARTER | R01_Z01 | 1 | Spurwahl und Erstresonanz mit dem Starter |
| STEP_P02_01 | MQ_P02 | OBJ_GOTO | POI_R01_9001 | R01_Z01 | 0 | Zur Ruine am Lindwald |
| STEP_P02_02 | MQ_P02 | OBJ_BATTLE | NPC_KAEL | R01_Z01 | 0 | Übungskampf gegen Kael |
| STEP_P02_03 | MQ_P02 | OBJ_BOSS | BOSS_P01 | R01_Z01 | 1 | Der verstummte Wächter |
| STEP_P03_01 | MQ_P03 | OBJ_TRAVERSE | GLIDER | POI_R01_9001 | 0 | Gleiter aus der Ruine bergen und erstmals gleiten |
| STEP_P03_02 | MQ_P03 | OBJ_INVESTIGATE | CLUE_P03_FRAGMENT | R01 | 0 | Erstes Klangfragment hören |
| STEP_P03_03 | MQ_P03 | OBJ_TALK | NPC_YSOLDE | SET_V_LINDWIESEN | 1 | Resonator und Wärterlizenz von Ysolde |
| STEP_A1_01_01 | MQ_A1_01 | OBJ_GOTO | SET_C_EICHENHALL | R01 | 0 | Reise nach Eichenhall |
| STEP_A1_01_02 | MQ_A1_01 | OBJ_TALK | NPC_HRALDA | SET_C_EICHENHALL | 0 | Hralda Brakk und der erste Sattel |
| STEP_A1_01_03 | MQ_A1_01 | OBJ_BATTLE | NPC_KAEL | SET_C_EICHENHALL | 1 | Rivalenkampf vor der Arena |
| STEP_A1_01_04 | MQ_A1_01 | OBJ_ARENA | ARN_01 | SET_C_EICHENHALL | 1 | Arena der Wurzeln – Maelis Wendt |
| STEP_A1_02_01 | MQ_A1_02 | OBJ_GOTO | R01_Z04 | R01 | 0 | Zum Rand der Lindwald-Stillezone |
| STEP_A1_02_02 | MQ_A1_02 | OBJ_HEALZONE | ZONE_R01_LINDWALD | R01_Z04 | 1 | Drei Heilkreise schließen |
| STEP_A1_02_03 | MQ_A1_02 | OBJ_BOSS | BOSS_A1_01 | R01_Z04 | 1 | Stillkern von Lindwald |
| STEP_A1_02_04 | MQ_A1_02 | OBJ_CINEMATIC | SEQ_A1_VERNAUNE | R01_Z04 | 0 | Vernaune erwacht; der Weg teilt sich |
| STEP_A1_03_01 | MQ_A1_03 | OBJ_GOTO | SET_C_KHARSHOLM | R02 | 0 | Nach Kharsholm über die Kettenbrücken |
| STEP_A1_03_02 | MQ_A1_03 | OBJ_CHOICE | DLG_A1_03_01 | SET_C_KHARSHOLM | 0 | Klanschwur am Ahnenfelsen |
| STEP_A1_03_03 | MQ_A1_03 | OBJ_HEALZONE | ZONE_R02_MAIN | R02 | 1 | Stillezone im Kharsgrat |
| STEP_A1_03_04 | MQ_A1_03 | OBJ_ARENA | ARN_02 | SET_C_KHARSHOLM | 1 | Torvik Hrall |
| STEP_A1_04_01 | MQ_A1_04 | OBJ_GOTO | SET_C_MORVENFURT | R03 | 0 | Nach Morvenfurt |
| STEP_A1_04_02 | MQ_A1_04 | OBJ_TALK | NPC_TAVESH | SET_C_MORVENFURT | 0 | Tavesh Amaru in der Unterstadt |
| STEP_A1_04_03 | MQ_A1_04 | OBJ_CHOICE | DLG_A1_04_03 | SET_C_MORVENFURT | 0 | Das Geheimnis der Freien Stimmen |
| STEP_A1_04_04 | MQ_A1_04 | OBJ_HEALZONE | ZONE_R03_MAIN | R03 | 1 | Stillezone im Moor |
| STEP_A1_04_05 | MQ_A1_04 | OBJ_ARENA | ARN_03 | SET_C_MORVENFURT | 1 | Evhe Corrach (nachts) |
| STEP_A1_05_01 | MQ_A1_05 | OBJ_GOTO | SET_C_SALTRANDHAFEN | R06 | 0 | Nach Saltrand-Hafen |
| STEP_A1_05_02 | MQ_A1_05 | OBJ_TALK | NPC_MARIEKE | SET_C_SALTRANDHAFEN | 0 | Marieke Holm und der Vorschuss |
| STEP_A1_05_03 | MQ_A1_05 | OBJ_CHOICE | DLG_A1_05_02 | SET_C_SALTRANDHAFEN | 0 | Kontor-Kredit annehmen oder nicht |
| STEP_A1_05_04 | MQ_A1_05 | OBJ_HEALZONE | ZONE_R06_MAIN | R06 | 1 | Stillezone vor der Küste |
| STEP_A1_05_05 | MQ_A1_05 | OBJ_ARENA | ARN_06 | SET_C_SALTRANDHAFEN | 1 | Beke Tamsen (Gezeiten) |
| STEP_A1_06_01 | MQ_A1_06 | OBJ_INVESTIGATE | CLUE_A1_STILLSTONES | dynamisch | 0 | Graue Steine im Kreis |
| STEP_A1_06_02 | MQ_A1_06 | OBJ_BOSS | BOSS_A1_02 | dynamisch | 1 | Ordenskommandant Ulrek |
| STEP_A1_06_03 | MQ_A1_06 | OBJ_CHOICE | DLG_A1_06_04 | dynamisch | 0 | Sereth spricht |
| STEP_A1_06_04 | MQ_A1_06 | OBJ_DELIVER | ITM_EMAT_STILLSHARD | NPC_YSOLDE | 1 | Stillstein-Splitter zu Ysolde |
| STEP_A1_07_01 | MQ_A1_07 | OBJ_CONDITION | Akkorde>=3 | – | 0 | Drei Akkorde |
| STEP_A1_07_02 | MQ_A1_07 | OBJ_CINEMATIC | SEQ_A1_VENNSPEECH | SET_C_EICHENHALL | 0 | Venns Rede auf dem Marktplatz |
| STEP_A1_07_03 | MQ_A1_07 | OBJ_TALK | NPC_VENN | SET_C_EICHENHALL | 1 | Fragment-Analyse; Kael wird Anwärter |
| STEP_A1_08_01 | MQ_A1_08 | OBJ_CONDITION | Akkorde>=4 & Quest.MQ_A1_06 | – | 0 | Vier Akkorde |
| STEP_A1_08_02 | MQ_A1_08 | OBJ_PUZZLE | PZ_TOWER_CHORDS | POI_R03_9001 | 0 | Die Akkorde lassen das Wasser weichen |
| STEP_A1_08_03 | MQ_A1_08 | OBJ_BOSS | BOSS_A1_03 | POI_R03_9001 | 1 | Stillkern im Morvenmoor |
| STEP_A1_08_04 | MQ_A1_08 | OBJ_CINEMATIC | SEQ_A1_ILENVISION | POI_R03_9001 | 1 | Vision Ilens (W3) |
| STEP_A1_09_01 | MQ_A1_09 | OBJ_GOTO | SET_V_LINDWIESEN | R01 | 0 | Heimkehr |
| STEP_A1_09_02 | MQ_A1_09 | OBJ_REST | SET_V_LINDWIESEN | R01 | 1 | Lager-Moment mit dem Chor; Ysolde am Brunnen |
| STEP_A2_01_01 | MQ_A2_01 | OBJ_TALK | NPC_HRALDA | SET_C_EICHENHALL | 0 | Ruf ins Wildwacht-Archiv |
| STEP_A2_01_02 | MQ_A2_01 | OBJ_INVESTIGATE | CLUE_A2_WENDELIN | SET_C_EICHENHALL | 1 | Wendelins Seite vierzig (W4) |
| STEP_A2_01_03 | MQ_A2_01 | OBJ_CHOICE | DLG_A2_01_02 | SET_C_EICHENHALL | 0 | Antwort auf Wendelin |
| STEP_A2_02_01 | MQ_A2_02 | OBJ_TRAVERSE | Mount.Dig | R04 | 0 | Grabreiten in der Sahrun-Weite |
| STEP_A2_02_02 | MQ_A2_02 | OBJ_INVESTIGATE | CLUE_A2_ASHURIM | SET_V_ASHURIM | 0 | Das Wanderdorf finden |
| STEP_A2_02_03 | MQ_A2_02 | OBJ_BOSS | BOSS_A2_01 | POI_R04_9001 | 1 | Glaskoloss der Weite |
| STEP_A2_02_04 | MQ_A2_02 | OBJ_TALK | NPC_VENN | POI_R04_9002 | 0 | Akademie-Grabung am Sonnenhof |
| STEP_A2_02_05 | MQ_A2_02 | OBJ_ARENA | ARN_04 | SET_C_QASRSAHRUN | 1 | Shirah Harrad |
| STEP_A2_03_01 | MQ_A2_03 | OBJ_TALK | NPC_MARIEKE | SET_C_SCHLACKENWEHR | 0 | Mariekes Kisten |
| STEP_A2_03_02 | MQ_A2_03 | OBJ_CHOICE | DLG_A2_03_02 | R05 | 0 | Kisten liefern / öffnen / zurückbringen |
| STEP_A2_03_03 | MQ_A2_03 | OBJ_HEALZONE | ZONE_R05_CAMP | POI_R05_9001 | 1 | Lagerbefreiung mit Tavesh |
| STEP_A2_03_04 | MQ_A2_03 | OBJ_ARENA | ARN_05 | SET_C_SCHLACKENWEHR | 1 | Kaldrex Vorn |
| STEP_A2_04_01 | MQ_A2_04 | OBJ_INVESTIGATE | CLUE_A2_EIDVIK | POI_R07_9001 | 1 | Klangpest-Nachhall in Eiðvik |
| STEP_A2_04_02 | MQ_A2_04 | OBJ_TALK | NPC_SERETH | LOC_KLOSTER_SCHWEIGFELS | 0 | Sereths Geschichte |
| STEP_A2_04_03 | MQ_A2_04 | OBJ_BOSS | BOSS_A2_02 | POI_R07_9002 | 1 | Venns Schatten |
| STEP_A2_04_04 | MQ_A2_04 | OBJ_ARENA | ARN_07 | SET_C_HVITMARK | 1 | Sigrun Fjall |
| STEP_A2_05_01 | MQ_A2_05 | OBJ_CONDITION | AktIIAkkorde>=2 | – | 0 | Zwei Akkorde in Akt II |
| STEP_A2_05_02 | MQ_A2_05 | OBJ_REST | NPC_YSOLDE | dynamisch | 1 | Ysoldes Geständnis (W5) |
| STEP_A2_06_01 | MQ_A2_06 | OBJ_CONDITION | Akkorde>=6 | – | 0 | Sechs Akkorde; Kaels Brief |
| STEP_A2_06_02 | MQ_A2_06 | OBJ_GOTO | SET_C_DORUNSRUH | R08 | 0 | Nach Dorunsruh |
| STEP_A2_06_03 | MQ_A2_06 | OBJ_TALK | NPC_VENN | SET_C_DORUNSRUH | 1 | Die Messung; Flugsattel |
| STEP_A2_07_01 | MQ_A2_07 | OBJ_INVESTIGATE | CLUE_A2_VAULT | POI_R08_9002 | 1 | Das Gewölbe (W6) |
| STEP_A2_07_02 | MQ_A2_07 | OBJ_CHOICE | DLG_A2_07_06 | POI_R08_9002 | 0 | Venn und Kael |
| STEP_A2_07_03 | MQ_A2_07 | OBJ_FLEE | ROUTE_R08_ESCAPE | SET_C_DORUNSRUH | 1 | Flucht über die Säulen |
| STEP_A2_08_01 | MQ_A2_08 | OBJ_GOTO | FLAG_SHELTER | R08 | 0 | Zum Unterschlupf |
| STEP_A2_08_02 | MQ_A2_08 | OBJ_REST | FLAG_SHELTER | R08 | 1 | Unter Freunden; Sereths Bericht |
| STEP_A2_09_01 | MQ_A2_09 | OBJ_TALK | NPC_AEVRIN | SET_V_THAELUUN | 0 | Aevrin Thal |
| STEP_A2_09_02 | MQ_A2_09 | OBJ_PUZZLE | PZ_GLYPHS_DORUN | SET_V_SAEULENRAST | 0 | Glyphenweg über Säulenrast |
| STEP_A2_09_03 | MQ_A2_09 | OBJ_ARENA | ARN_08 | SET_C_DORUNSRUH | 1 | Glyphenhof |
| STEP_A2_10_01 | MQ_A2_10 | OBJ_CONDITION | Akkorde>=8 | – | 0 | Acht Akkorde |
| STEP_A2_10_02 | MQ_A2_10 | OBJ_BOSS | BOSS_A2_03 | POI_R08_9001 | 1 | Kronensplitter-Wächter |
| STEP_A2_10_03 | MQ_A2_10 | OBJ_CINEMATIC | SEQ_A2_MAEDRYN_ILEN | POI_R08_9001 | 1 | Vision Maedryn und Ilen (W7); Kael nimmt den Splitter |
| STEP_A2_11_01 | MQ_A2_11 | OBJ_REST | SET_C_DORUNSRUH | R08 | 1 | Rat auf der Terrasse |
| STEP_A3_01_01 | MQ_A3_01 | OBJ_GOTO | SET_O_LIFTSTATIONKRATERRAND | R09 | 0 | Liftstation Kraterrand |
| STEP_A3_01_02 | MQ_A3_01 | OBJ_TALK | NPC_ILYX | SET_C_PRISMARA | 1 | Ilyx Brannoc und die Energiekrise |
| STEP_A3_02_01 | MQ_A3_02 | OBJ_GOTO | POI_R09_9002 | R09 | 0 | Missklang-Wacht und tiefste Adern |
| STEP_A3_02_02 | MQ_A3_02 | OBJ_BOSS | BOSS_A3_01 | POI_R09_9002 | 1 | Missklang-Hydra |
| STEP_A3_02_03 | MQ_A3_02 | OBJ_INVESTIGATE | CLUE_A3_PLAN | POI_R09_9002 | 1 | Venns Ritualplan (W8) |
| STEP_A3_03_01 | MQ_A3_03 | OBJ_ARENA | ARN_09 | SET_C_PRISMARA | 1 | Ilyx Brannoc (fest 9) |
| STEP_A3_03_02 | MQ_A3_03 | OBJ_CHOICE | DLG_A3_03_03 | POI_R09_9001 | 1 | Der zehnte Splitter |
| STEP_A3_04_01 | MQ_A3_04 | OBJ_REST | SET_O_KRISTALLSEELAGER | R09 | 1 | Die letzte Nacht am Boden |
| STEP_A3_05_01 | MQ_A3_05 | OBJ_TRAVERSE | Mount.Fly | R10 | 0 | Durch die Windbänder |
| STEP_A3_05_02 | MQ_A3_05 | OBJ_GOTO | SET_V_LUMEYA | R10 | 0 | Lumeya und Wolkenrast |
| STEP_A3_05_03 | MQ_A3_05 | OBJ_GOTO | SET_O_WINDANKER | R10 | 1 | Windanker sichern |
| STEP_A3_06_01 | MQ_A3_06 | OBJ_INVESTIGATE | CLUE_A3_WALLOFTEN | SET_C_AERION | 0 | Die Wand der Zehn |
| STEP_A3_06_02 | MQ_A3_06 | OBJ_ARENA | ARN_10 | SET_C_AERION | 1 | Oruma Siyel (fest 10) |
| STEP_A3_06_03 | MQ_A3_06 | OBJ_CINEMATIC | SEQ_A3_TENVOICES | SET_C_AERION | 0 | Zehn Stimmen erwachen; Point of no Return |
| STEP_A3_07_01 | MQ_A3_07 | OBJ_GOTO | POI_R10_9001 | R10 | 0 | Zur Kronenwerft |
| STEP_A3_07_02 | MQ_A3_07 | OBJ_BOSS | BOSS_A3_02 | POI_R10_9001 | 1 | Aldric Venn mit der Resonanzkrone |
| STEP_A3_08_01 | MQ_A3_08 | OBJ_BOSS | BOSS_A3_03 | R10 | 1 | Velnox – Phasen 1–3 |
| STEP_A3_08_02 | MQ_A3_08 | OBJ_DECIDE_ENDING | FLAG_ENDING | R10 | 1 | Die Entscheidung (W9) |
| STEP_A3_09_01 | MQ_A3_09 | OBJ_CINEMATIC | SEQ_A3_EPILOG | R01 | 0 | Epilog (Endsequenz, Vignetten, Schlussbild, Brief) |
| STEP_A3_09_02 | MQ_A3_09 | OBJ_GOTO | SET_V_LINDWIESEN | R01 | 1 | Nachhall: Erwachen in Lindwiesen |

---

## 8. Belohnungen

### 8.1 Wärter-EP

K43 legt die Spannen fest (Hauptquest-Schritt 300–1.500, Nebenquest 400–2.000) und die Zielanteile (Haupt 25 %, Neben 25 %). K48 macht daraus Formeln:

| Quelle | Formel | Spanne |
|---|---|---|
| Hauptquest-Meilenstein | `150 + 50 × Intensität + Aktzuschlag (0/100/200/200)`, Boss-Schritt × 1,5, auf 50 gerundet; Arena-Schritte 0 (Akkord-EP aus K43) | 300–1.275 |
| Nebenquest | `round50( (300 + 40 × Dauer_min) × Aktfaktor )`, Aktfaktor 1,0 / 1,3 / 1,6 / 1,8 (Akt I/II/III/Nachhall) | 400–2.000 |
| Kettenabschluss | Nebenquest-EP × 1,5 | ≤ 2.000 (gedeckelt) |

**Hauptquest-EP je Akt** (aus den Daten berechnet, `gen_quests.py ep_table`):

| Abschnitt | Hauptquests | Meilensteine | Hauptquest-EP | Wärter-EP gesamt (K43) | Anteil | Ziel |
|---|---|---|---|---|---|---|
| Prolog | 3 | 3 | 1.500 | 2.400 | 62 % | 25 % |
| Akt I | 9 | 16 | 7.850 | 30.000 | 26 % | 25 % |
| Akt II | 11 | 17 | 9.800 | 40.000 | 24 % | 25 % |
| Akt III | 9 | 12 | 8.000 | 30.000 | 27 % | 25 % |

Der Prolog liegt bewusst über dem Zielanteil: Er ist ein Tutorial und besteht fast nur aus Hauptquest (K02 §8); seine 2.400 EP fallen in der Gesamtrechnung nicht ins Gewicht. Die drei Akte liegen im Band 25 % ± 5 (QV-10).

**Nebenquest-Kontrolle:** Mit Ø 35 min ergibt die Formel 1.700 / 2.000 / 2.000 EP (Akt I/II/III, gedeckelt). Der Zielanteil „Neben 25 %“ entspricht in der Story-Phase (~102.400 Wärter-EP bis Ende Akt III, K43 §3.1) rund **25.600 EP** – also ~14 Nebenquests, etwa 8 h der ~50 h Story. Das deckt sich mit dem Story-Fokus-Profil (K01 §7.4); die übrigen ~190 Nebenquests tragen das Completionist-Profil (80–110 h) im Nachhall. Feinabstimmung im Balancing (K63).

### 8.2 Hauptquest-EP je Quest

| Quest | Titel | Intensität | Schritte | Meilensteine | Wärter-EP |
|---|---|---|---|---|---|
| MQ_P01 | Ein Ton im Dunkel | 7 | 4 | 1 | 500 |
| MQ_P02 | Der verstummte Wächter | 6 | 3 | 1 | 700 |
| MQ_P03 | Was der Wald erzählt | 3 | 3 | 1 | 300 |
| MQ_A1_01 | Die Arena der Wurzeln | 5 | 4 | 2 | 500 |
| MQ_A1_02 | Stille über Lindwald | 7 | 4 | 2 | 1.500 |
| MQ_A1_03 | Fels und Ahnen | 6 | 4 | 2 | 550 |
| MQ_A1_04 | Nebel über dem Moor | 6 | 5 | 2 | 550 |
| MQ_A1_05 | Gezeiten und Handel | 6 | 5 | 2 | 550 |
| MQ_A1_06 | Die Stillsteine | 8 | 4 | 2 | 1.650 |
| MQ_A1_07 | Ein Riss im Lied | 4 | 3 | 1 | 450 |
| MQ_A1_08 | Der versunkene Turm | 9 | 4 | 2 | 1.750 |
| MQ_A1_09 | Nachklang | 2 | 2 | 1 | 350 |
| MQ_A2_01 | Die Schlösser der Stimmen | 4 | 3 | 1 | 550 |
| MQ_A2_02 | Die Wahrheit unter dem Sonnenhof | 7 | 5 | 2 | 1.050 |
| MQ_A2_03 | Das Kraterherz | 6 | 4 | 2 | 650 |
| MQ_A2_04 | Eiðvik | 8 | 4 | 3 | 1.850 |
| MQ_A2_05 | Was Ysolde verschwieg | 5 | 2 | 1 | 600 |
| MQ_A2_06 | Die Messung | 4 | 3 | 1 | 550 |
| MQ_A2_07 | Der Verrat | 9 | 3 | 2 | 1.600 |
| MQ_A2_08 | Unter Freunden | 3 | 2 | 1 | 500 |
| MQ_A2_09 | Glyphen von Dorunsruh | 6 | 3 | 1 | 0 |
| MQ_A2_10 | Der Thronsaal | 9 | 3 | 2 | 2.000 |
| MQ_A2_11 | Neun von Zehn | 2 | 1 | 1 | 450 |
| MQ_A3_01 | Hinab nach Prismara | 5 | 2 | 1 | 600 |
| MQ_A3_02 | Der versteinerte Missklang | 8 | 3 | 2 | 1.850 |
| MQ_A3_03 | Das neunte Schloss | 6 | 2 | 2 | 650 |
| MQ_A3_04 | Die letzte Nacht am Boden | 2 | 1 | 1 | 450 |
| MQ_A3_05 | Aufstieg nach Nimbara | 6 | 3 | 1 | 650 |
| MQ_A3_06 | Die Sternenarena | 7 | 3 | 1 | 0 |
| MQ_A3_07 | Die Krone | 9 | 2 | 1 | 1.200 |
| MQ_A3_08 | Die Große Pause | 10 | 2 | 2 | 2.150 |
| MQ_A3_09 | Nachhall | 2 | 2 | 1 | 450 |

### 8.3 Sol, Items, Ruf

| Belohnung | Regel | Kapitel |
|---|---|---|
| Sol | Nebenquests 300–3.000 ◎ nach Akt (K42 §4), × RewardScale des Zonenbands | K42 |
| Items | 1 Item-Belohnung je Quest aus Rezept, Klangschrift, Ausrüstungsteil, Lockmittel, Hain-Dekor; nie Siegel-Massen (Bindung bleibt Wissen, DR-01) | K40/K41 |
| Ruf | Nebenquest 150, Kettenabschluss 400, Hauptquest laut K47 §4.2 | K47 |
| Kodex/Lore | Beobachtungen, Klangfragmente, Wendelin-Seiten (QR-10) | K39 |
| Echo-Begegnung | Seltene oder Alpha-Echos als Belohnungsbegegnung (nicht als geschenktes Echo; DR-01) | K36 |

**Keine geschenkten Echos:** Quests belohnen nie mit einem fertig gebundenen Echo (außer Starter, K44). Stattdessen öffnen sie eine Begegnung, bei der der Spieler binden *kann* (ADR-184). Ausnahme: Eier aus Zucht-Nebenquests (K38), die der Spieler selbst ausbrütet.

---

## 9. Hinweise, Tagebuch, Markierungen

### 9.1 Hinweisstufen

AETHRIS bevorzugt diegetische Hinweise; Markierungen sind eine Einstellung, keine Pflicht.

| Stufe | Name | Was der Spieler sieht | Standard |
|---|---|---|---|
| 0 | Lauschend | Nur Tagebuchtext, Resonanzsinn-Pulse, NPC-Wegbeschreibungen | – |
| 1 | Geführt | + ungefährer Kreis auf der Karte (Radius 80–150 m), Kompass-Richtung | **Standard** |
| 2 | Markiert | + exakter Marker für Personen und Orte (nie für Untersuchungsziele) | – |

`OBJ_INVESTIGATE`, `OBJ_OBSERVE` und `OBJ_PUZZLE` werden auf keiner Stufe exakt markiert (S2: Wissen schlägt Items).

### 9.2 Angebote in der Welt

| Quelle | Darstellung |
|---|---|
| NPC mit Quest | Kein Symbol über dem Kopf; der NPC handelt sichtbar (sucht, ruft, winkt) und hat einen Bark im Vorbeigehen |
| Echo mit Quest | Auffälliges Verhalten (kreist, ruft, folgt) + Resonanzsinn-Puls |
| Questbrett | Aufträge und 1–2 Nebenquest-Aushänge je Siedlung |
| Fund | Brief, Glyphe, Tagebuchseite (Untersuchen startet die Quest) |
| Gerücht | Barks in Gasthäusern verweisen auf Nebenquests der Region (je 2–3 Barks pro Quest) |

DR-26 (Drei-Ding-Regel) wird über Angebote, POIs und Begegnungen gemeinsam erfüllt (K57 prüft je 300 m).

### 9.3 Tagebuch

```
┌─ TAGEBUCH ───────────────────────────────────────────────────────────────┐
│ [Hauptquest] [Nebenquests 14] [Fraktionen] [Aufgaben] [Erledigt]          │
│                                                                           │
│ ▸ Eiðvik                         Hvitfell · Akt II · ◆ verfolgt           │
│   Ich soll nach Eiðvik gehen und hinhören. Ysolde hat nicht gesagt,       │
│   was ich dort finden werde.                                              │
│   ☐ In den Ruinen den Nachhall finden (2/4)                               │
│   ☐ …                                                                     │
│                                                                           │
│ ▸ Die Glocke von Kaldra          Ignareth · Kontor · 25 min               │
│ ▸ Wendelins letzter Stein       Nimbara · Rätsel & Ruinen                │
└───────────────────────────────────────────────────────────────────────────┘
```

- Zukünftige Schritte sind verborgen (☐ … ), um Wendungen nicht zu verraten.
- Bedingungen mit Tagesphase/Wetter/Mond zeigen ein Symbol und die Vorhersage (K14 §11).
- **Zurückstellen** (`Deferred`) blendet eine Nebenquest aus, ohne sie abzubrechen; nichts geht verloren.

---

## 10. Questsystem-Technik

### 10.1 Datenmodell

`UQuestDefinition` (`Source/AethrisCore/Public/Data/QuestDefinition.h`): `Kind`, `RegionId`, `Prerequisite`, `TruthLevel`, `Intensity`, `FactionId`, `ChainId`, `Steps[]` (`FQuestStep`: StepId, Objective, Target, Count, Location, bMilestone, Condition, JournalText). Fach-Fragmente (ADR-031) liefern Dialog (`UQuestDialogueFragment`), Belohnung (`UQuestRewardFragment`), Kampf (`UQuestEncounterFragment`) und Folgen (`UQuestConsequenceFragment`: Flags, Data Layer, Barks).

### 10.2 Zustandsmaschine

```
            Vorbedingung erfüllt                Annehmen
  Hidden ─────────────────────────► Available ───────────► Active ──┐
     ▲                                  │  ▲                  │      │ letzter Schritt erfüllt
     │ (nie zurück)                     │  │ Fortsetzen       │      ▼
     └──────────────────────────────    │  └──── Deferred ◄───┘   Completed
                                        │        (Zurückstellen)
                                        └─ Hauptquests werden automatisch angenommen
```

- Genau **ein aktueller Schritt** je aktiver Quest; Parallelität entsteht durch mehrere Quests, nicht durch parallele Schritte (ADR-185). Zähl-Schritte (3 Heilkreise) zählen beliebige Reihenfolge.
- Hauptquests gehen von `Available` sofort nach `Active`; sie können nicht zurückgestellt werden, aber pausieren nie die Welt.
- `Completed` ist endgültig; Folgen werden als Flags und Data-Layer-Zustände gespeichert, nicht als Questzustand abgeleitet.

### 10.3 Ereignisgetriebene Auswertung

```
Feature-Plugin (z. B. GF_Combat) ──Event.Combat.Ended──► GF_Quests::ObjectiveRouter
                                                          │  Index: (Objective, Target) → aktive Schritte
                                                          ▼
                                                   ReportObjective(OBJ_BOSS, BOSS_A2_01)
                                                          │
                                                   Schritt erfüllt? → Next / Complete
                                                          │
                                                   Bedingungs-Index: welche Hidden-Quests hängen an
                                                   (Akkorde, Flag.X, Quest.Y, Time, Weather …)?
                                                          ▼
                                                   nur diese neu auswerten → Available
```

Der Bedingungs-Index vermeidet Polling: Jede Quest registriert die Variablen ihrer Vorbedingung; nur ein Ereignis, das eine dieser Variablen ändert, löst eine Auswertung aus. Budget: ≤ 0,2 ms pro Ereignis auf PS5 bei 250 Quests (K65).

### 10.4 Save-Fragment

| Fragment | Inhalt |
|---|---|
| `Player.Quests` | je Quest: Zustand (2 Bit), StepIndex (1 Byte), StepCount (2 Byte), Tracked (1 Bit); nur Quests ≠ Hidden |
| `Player.StoryFlags` | Map Flag → int32 (`StoryFlags.csv`) |
| `World.QuestConsequences` | aktive Data Layer und NPC-Zustände aus Folgen |

Datenänderungen nach Release (neue Schritte) werden über `StepId` statt Index migriert (K64): Das Fragment speichert zusätzlich die `StepId` des aktuellen Schritts; beim Laden wird der Index neu bestimmt.

### 10.5 Koop

| Thema | Regel |
|---|---|
| Hauptquests | Fortschritt nur in der Welt des Hosts; Gäste sehen Szenen als Zuschauer, erhalten keine Story-Flags (K60) |
| Nebenquests | Teilen: Gast kann eine Nebenquest des Hosts „mitspielen“; besitzt er sie selbst im gleichen Schritt, schreitet sie bei ihm mit fort |
| Belohnungen | Jede Person erhält Belohnungen in ihrer eigenen Welt; keine doppelten Echo-Begegnungen (instanziert je Teilnehmer wie bei Mythischen, CANON §131) |
| Autorität | Host-autoritativ; `ReportObjective` nur auf dem Host, repliziert als Ereignis (DR-21 gilt nicht, da kooperativ) |

### 10.6 Dialogsystem (Schnittstelle)

| Element | Format |
|---|---|
| Dialog-ID | `DLG_<Quest>_##` (CANON §23) |
| Knotentypen | Line, Choice (3 Haltungen oder Dilemma), Condition, SetFlag, Event (Kamera, Animation), End |
| Haltungen | `Stance.Empathic`, `Stance.Curious`, `Stance.Resolute`; Reaktion je Haltung Pflicht (K44 §10.2 Regel 3) |
| Sprachausgabe | Hauptquests voll vertont; Nebenquests: Kernzeilen vertont (Auftrag, Wendung, Abschluss), Rest Text + Laute (K55) |
| Werkzeug | Dialoge als Daten (`DT_Dialogue_*`), Editor-Graph im AethrisEditor-Modul |

---

## 11. Validator und Tests

`tools/gen_quests.py validate` läuft in CI (K05 §7) auf jeder Datenänderung:

| Regel | Prüfung |
|---|---|
| QV-01 | Jede Hauptquest hat Schritte, Reihenfolge lückenlos |
| QV-02 | Zieltypen existieren |
| QV-03 | Boss-Schritte passen zur Quest; jeder Story-Boss genau einmal |
| QV-04 | Akkord-Schritte passen; alle 10 Arenen genau einmal |
| QV-05 | Orte existieren (Siedlungen, Story-POIs, Regionen/Zonen) |
| QV-06 | Vorbedingungen verweisen auf existierende Quests |
| QV-07 | W1–W9 genau einmal und in Reihenfolge |
| QV-08 | DR-29 Atemzug (Ausnahmen ADR-168) |
| QV-09 | Story-Flags werden in existierenden Quests gesetzt |
| QV-10 | Hauptquest-EP je Akt 25 % ± 5; jeder Meilenstein 300–1.500 |

**Aktueller Lauf:** 32 Hauptquests, 98 Schritte, 0 Fehler.

**DR-29-Prüfung aus den Daten:**

| Von | Intensität | Nach | Intensität | Bewertung |
|---|---|---|---|---|
| MQ_P01 | 7 | MQ_P02 | 6 | ✓ Atemzug |
| MQ_A1_02 | 7 | MQ_A1_03 | 6 | ✓ Atemzug |
| MQ_A1_06 | 8 | MQ_A1_07 | 4 | ✓ Atemzug |
| MQ_A1_08 | 9 | MQ_A1_09 | 2 | ✓ Atemzug |
| MQ_A2_02 | 7 | MQ_A2_03 | 6 | ✓ Atemzug |
| MQ_A2_04 | 8 | MQ_A2_05 | 5 | ✓ Atemzug |
| MQ_A2_07 | 9 | MQ_A2_08 | 3 | ✓ Atemzug |
| MQ_A2_10 | 9 | MQ_A2_11 | 2 | ✓ Atemzug |
| MQ_A3_02 | 8 | MQ_A3_03 | 6 | ✓ Atemzug |
| MQ_A3_06 | 7 | MQ_A3_07 | 9 | Ausnahme ADR-168 |
| MQ_A3_07 | 9 | MQ_A3_08 | 10 | Ausnahme ADR-168 |
| MQ_A3_08 | 10 | MQ_A3_09 | 2 | ✓ Atemzug |

### 11.1 Automatisierte Tests

| Test | Inhalt | Kapitel |
|---|---|---|
| **Quest-Bot** | Spielt jede Quest über Debug-Befehle (`Cheat.Quest.Step`) und prüft Zustandswechsel, Belohnungen, Flags, Save/Load in jedem Schritt | K66 |
| **Reihenfolge-Matrix** | Alle 6 Akt-I- und 6 Akt-II-Reihenfolgen (je Starterlinie) bis zum Aktende | K66 |
| **L-01-Scanner** | Prüft, dass kein Text mit `TruthLevel` > aktuellem Stand ausgespielt wird | K39/K66 |
| **Bedingungs-Fuzzer** | Zufällige Spielstände gegen alle Vorbedingungen: keine Ausnahme, keine Endlosschleife | K66 |

---

## 12. Produktionspipeline

```
 Quest-Pitch (1 Seite) ─► Review (Narrative + Quest Lead) ─► Daten (CSV) ─► Validator ─► Blockout (LD)
        │                                                        │
        └── Titel, Giver, Wendung, dritte Lösung, Folge ─────────┘
 ─► Dialog (Writer) ─► Implementierung ohne Code (DR-25) ─► Quest-Bot ─► Playtest ─► VO ─► Lokalisierung
```

| Phase | Ziel je Nebenquest | Verantwortlich |
|---|---|---|
| Pitch | 0,5 Tage | Quest Designer |
| Daten + Blockout | 1,5 Tage | Quest Designer, Level Designer |
| Dialog | 1 Tag (~120 Zeilen) | Writer |
| Implementierung | 1 Tag | Quest Designer (Skript-Bausteine) |
| Test/Polish | 1 Tag | QA, Designer |
| **Summe** | **5 Personentage** | 210 × 5 = 1.050 PT (≈ 5 Personenjahre) |

Hauptquests: ~25 Personentage je Quest (inkl. Cinematics) → 32 × 25 = 800 PT. Planung und Personal in K67.

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Quest Design | 210 Nebenquests (Ø 35 min) auf dem Gerüst (`SideQuests.csv`) mit Titeln, Givern, Schritten, Folgen | K49–K51 |
| Programmierung | GF_Quests: `IQuestService`, ObjectiveRouter, Bedingungsparser + Index, Save-Fragmente, Debug-Befehle | K05/K06 |
| Tools | Dialog-Editor, Quest-Daten-Import, Validator in CI | K05 §7 |
| Level Design | Story-POIs aus `StoryPOIs.csv` platzieren; Angebote nach §9.2 | K57 |
| UI | Tagebuch, Hinweisstufen, Kompass, Vorhersage-Symbole | K54 |
| Audio/VO | Vertonungsumfang §10.6, Barks `Quest.<ID>.After` | K55 |
| QA | Quest-Bot, Reihenfolge-Matrix, L-01-Scanner, Fuzzer | K66 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-182 | Tagebuch trennt Quests (Haupt/Neben/Fraktion) von Aufgaben (Aufträge, Echo-Bitten) | Lesbarkeit; Geschichten gehen nicht im Wiederholbaren unter | Ein gemeinsames Questlog |
| ADR-183 | Eigene deterministische Bedingungssprache mit Index statt Blueprint-Bedingungen | Datengetrieben (DR-25), validierbar, performant, Koop-synchron | Blueprint-Funktionen je Quest |
| ADR-184 | Quests schenken keine gebundenen Echos, sondern Begegnungen | Bindung bleibt Wissen und Entscheidung (DR-01, DR-03) | Belohnungs-Echos |
| ADR-185 | Genau ein aktueller Schritt je Quest | Einfache Zustände, robuste Saves, klare Tagebuchanzeige | Parallele Schritt-Graphen |
| ADR-186 | Nebenquest-Gerüst wird generiert (Region, Kategorie, Fraktion, Akt, Kette) und vor dem Schreiben festgelegt | Verteilung und Fraktionsziele (K47) sind vor dem Content abgesichert | freie Nummernvergabe beim Schreiben |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §185 | Questarten (Haupt, Neben, Fraktionskette, Auftrag, Kodex-Aufgabe, Weltereignis, Echo-Bitte), Quest-Bibel QR-01–QR-12, Längen | LOCKED |
| §186 | Questdaten: `ObjectiveTypes.csv` (21 Zieltypen), `MainQuestSteps.csv` (98 Schritte), `StoryPOIs.csv`; Bedingungssprache; EP-Formeln | LOCKED |
| §187 | Nebenquest-Gerüst `SideQuests.csv`: Nummerierung nach Akt-Reihenfolge R01, R02, R03, R06, R04, R05, R07, R08, R09, R10; 120 Fraktionsquests, 18 Ketten; ~25 % später verfügbar (Ketten nie verschoben) | LOCKED |
| §188 | Questsystem-Technik: Zustände, ein Schritt je Quest, ereignisgetriebene Auswertung, Save-Fragmente, Koop, Validator QV-01–QV-10 | LOCKED |
| §10 | ADR-182 – ADR-186 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Questarten und Abgrenzung
- [x] Quest-Bibel (12 Regeln), Schreibregeln
- [x] Nebenquest-Gerüst: Regionen, Kategorien, Fraktionen, Ketten, Verfügbarkeit
- [x] Anatomie, Zieltypen, Bedingungssprache
- [x] Alle Hauptquests in Schritte zerlegt; Story-POIs registriert
- [x] Belohnungsformeln (EP aus Daten geprüft), Sol/Items/Ruf, keine geschenkten Echos
- [x] Hinweisstufen, Angebote, Tagebuch
- [x] Technik: Datenmodell, Zustandsmaschine, Ereignis-Auswertung, Save, Koop, Dialog-Schnittstelle
- [x] Validator (0 Fehler), Tests, Pipeline und Aufwand
- [x] Anforderungen, ADR-182 – ADR-186, CANON §185–§188

➡️ **Nächstes Kapitel: K49 – Nebenquests I (SQ_001–SQ_070).**
