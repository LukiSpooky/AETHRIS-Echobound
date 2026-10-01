# 00 · Kapitelplan – AETHRIS: Echobound

**Owner:** Game Director · **Pflege:** Producer / QA Lead · **Stand:** K19 abgeschlossen

Das Projekt ist in **68 Kapitel** in **12 Teilen** gegliedert. Jedes Kapitel baut auf den vorherigen auf und darf nur Entscheidungen verwenden, die in [`CANON.md`](CANON.md) eingetragen sind (oder es trägt neue ein).

> **Abweichung von der ursprünglichen Reihenfolge (ADR-004):** Das Briefing nennt die Reihenfolge *Executive Summary → GDD → Welt → Kreaturen → Kampf → Codearchitektur → UI → Multiplayer → Assets → Roadmap*. Wir ziehen das **technische Fundament (K05–K06)** direkt hinter das GDD. Grund: Alle späteren Kapitel enthalten Datenstrukturen, Klassenmodelle und Pseudocode. Wenn diese auf einer bereits festgelegten Architektur (Modulnamen, Basisklassen, Event-Bus, Data-Asset-Schema) aufbauen, entstehen keine widersprüchlichen Code-Beispiele. Die restliche Reihenfolge folgt dem Briefing.

## Legende

| Symbol | Bedeutung |
|---|---|
| ✅ | abgeschlossen, Inhalte in CANON übernommen |
| 🔄 | in Arbeit |
| ⬜ | geplant |

## Teil I – Vision & Fundament

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K01 | Executive Summary | Game Director | – | ✅ |
| K02 | GDD I – Design-Säulen, Spielerfantasie, Core Loops | Game Director, Creative Director | K01 | ✅ |
| K03 | GDD II – Spielstruktur, Progression, Feature-Matrix | Game Director, RPG Systems Designer | K02 | ✅ |
| K04 | Kanon, Glossar, Namens- & ID-Konventionen | Creative Director, Narrative Writer | K01–K03 | ✅ |
| K05 | TDD I – Engine-Setup, Modul- & Projektstruktur, Coding Standards | Unreal Senior Dev, Lead Gameplay Programmer | K01, K03 | ✅ |
| K06 | TDD II – Core-Framework: Data-Driven, Event-Bus, State Machines, GAS, Save-Architektur | Lead Gameplay Programmer | K05 | ✅ |

## Teil II – Welt

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K07 | World Bible I – Kosmologie, Weltlied, Geschichte | Creative Director, Narrative Writer | K04 | ✅ |
| K08 | Weltgeographie & Makro-Layout (36 km²) | Level Designer | K07 | ✅ |
| K09 | Biome I – Verdanthain, Kharsgrat, Morvenmoor, Sahrun-Weite, Ignareth | Level Designer, Technical Artist | K08 | ✅ |
| K10 | Biome II – Saltrand, Hvitfell, Ael'Dorun, Prismtiefen, Nimbara | Level Designer, Technical Artist | K08 | ✅ |
| K11 | Städte I (5 Städte) | Level Designer, Narrative Writer | K09 | ✅ |
| K12 | Städte II (5 Städte) | Level Designer, Narrative Writer | K10 | ✅ |
| K13 | Dörfer & Außenposten | Level Designer, Quest Designer | K11, K12 | ✅ |
| K14 | Wettersystem | Technical Artist, Gameplay Programmer | K06, K08 | ✅ |
| K15 | Tageszyklus & Beleuchtung | Technical Artist | K14 | ✅ |

## Teil III – Kreaturen

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K16 | Monster Bible I – Designregeln, Taxonomie, Datenschema | Creative Director, RPG Systems Designer | K06, K07 | ✅ |
| K17 | Typensystem & Effektivitätstabelle | Combat Designer | K16 | ✅ |
| K18 | Statuswerte, Persönlichkeit, Temperament, Wachstumsraten | RPG Systems Designer | K17 | ✅ |
| K19 | Evolutionssystem | RPG Systems Designer | K18, K14, K15 | ✅ |
| K20 | Kreaturenkatalog 1 (#001–#032) | Creature Team | K19 | ⬜ |
| K21 | Kreaturenkatalog 2 (#033–#064) | Creature Team | K20 | ⬜ |
| K22 | Kreaturenkatalog 3 (#065–#096) | Creature Team | K21 | ⬜ |
| K23 | Kreaturenkatalog 4 (#097–#128) | Creature Team | K22 | ⬜ |
| K24 | Kreaturenkatalog 5 (#129–#160) | Creature Team | K23 | ⬜ |
| K25 | Kreaturenkatalog 6 (#161–#192) | Creature Team | K24 | ⬜ |
| K26 | Kreaturenkatalog 7 (#193–#224) | Creature Team | K25 | ⬜ |
| K27 | Kreaturenkatalog 8 (#225–#256, inkl. Legendäre) | Creature Team | K26 | ⬜ |
| K28 | Fähigkeiten I – System, Datenschema, Passive | Combat Designer | K17, K18 | ⬜ |
| K29 | Fähigkeiten II – Aktive Fähigkeiten | Combat Designer | K28 | ⬜ |
| K30 | Fähigkeiten III – Ultimates & Feldfähigkeiten | Combat Designer | K29 | ⬜ |

## Teil IV – Kampf

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K31 | Kampfsystem I – Resonanz-Zeitleiste, Initiative, Priorität | Combat Designer, Lead Gameplay Programmer | K28 | ⬜ |
| K32 | Kampfsystem II – Schadensformel, Status, Terrain, Wetter | Combat Designer | K31 | ⬜ |
| K33 | Kampfsystem III – Positionierung, Combos, Synergien, Formate | Combat Designer | K32 | ⬜ |
| K34 | Kampf-KI (Trainer & Wild) | AI Engineer | K33 | ⬜ |
| K35 | Raids | Combat Designer, Network Engineer | K33, K34 | ⬜ |

## Teil V – Bindung

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K36 | Fangsystem (Resonanzbindung) | Lead Gameplay Programmer, RPG Systems Designer | K31 | ⬜ |
| K37 | Begleitersystem | RPG Systems Designer, Animation | K36 | ⬜ |
| K38 | Zucht & Genetik | RPG Systems Designer | K18, K37 | ⬜ |
| K39 | Forschung, Echo-Kodex & Fotografie | RPG Systems Designer, UI/UX | K36 | ⬜ |

## Teil VI – Spielersysteme

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K40 | Ausrüstung, Reittiere & Traversal | Gameplay Programmer, Level Designer | K08 | ⬜ |
| K41 | Ressourcen & Crafting | Economy Designer | K40 | ⬜ |
| K42 | Wirtschaft | Economy Designer | K41 | ⬜ |
| K43 | Skilltree & Spielerprogression | RPG Systems Designer | K36–K42 | ⬜ |

## Teil VII – Narrative

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K44 | Story Akt I | Narrative Writer | K07, K11 | ⬜ |
| K45 | Story Akt II | Narrative Writer | K44 | ⬜ |
| K46 | Story Akt III & Finale | Narrative Writer | K45 | ⬜ |
| K47 | Fraktionen & Rufsystem | Narrative Writer, Quest Designer | K46 | ⬜ |
| K48 | Quest Bible & Questsystem-Technik | Quest Designer, Gameplay Programmer | K47 | ⬜ |
| K49 | Nebenquests 1 (#SQ001–#SQ070) | Quest Designer | K48 | ⬜ |
| K50 | Nebenquests 2 (#SQ071–#SQ140) | Quest Designer | K49 | ⬜ |
| K51 | Nebenquests 3 (#SQ141–#SQ210) | Quest Designer | K50 | ⬜ |

## Teil VIII – Lebendige Welt / KI

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K52 | Monster-Ökologie & Schwarm-KI | AI Engineer | K16–K27 | ⬜ |
| K53 | NPC-KI (Tagesabläufe, Reaktionen, Gruppen) | AI Engineer | K13, K15 | ⬜ |

## Teil IX – Präsentation

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K54 | UI/UX | UI/UX Designer | alle Systemkapitel | ⬜ |
| K55 | Audio Bible | Sound Designer | K07–K15 | ⬜ |
| K56 | Art Bible | Creative Director, Technical Artist | K07–K27 | ⬜ |
| K57 | Asset Pipeline, Animation & Technical Art | Technical Artist | K56 | ⬜ |
| K58 | VFX | Technical Artist | K57 | ⬜ |

## Teil X – Online

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K59 | Multiplayer-Architektur | Network Engineer | K06 | ⬜ |
| K60 | Koop, Tausch, Gilden | Network Engineer, Game Director | K59 | ⬜ |
| K61 | PvP & Ranked | Combat Designer, Network Engineer | K59, K33 | ⬜ |

## Teil XI – Endgame & Balancing

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K62 | Endgame | Game Director | K46, K61 | ⬜ |
| K63 | Balancing-Mathematik | RPG Systems Designer, Economy Designer | alle Systemkapitel | ⬜ |
| K64 | Save-System (Autosave, Cloud, Versionierung) | Lead Gameplay Programmer | K06, K59 | ⬜ |

## Teil XII – Produktion

| # | Kapitel | Hauptverantwortung | Abhängigkeiten | Status |
|---|---|---|---|---|
| K65 | Performance & Plattformen | Unreal Senior Dev | K57 | ⬜ |
| K66 | QA-Strategie | QA Lead | alle | ⬜ |
| K67 | Produktions-Roadmap (Phase 1–6) | Game Director, Producer | alle | ⬜ |
| K68 | LiveOps, Updates & Post-Launch | Game Director | K67 | ⬜ |

## Dokument-Mapping (Briefing → Kapitel)

| Gefordertes Dokument | Kapitel |
|---|---|
| Game Design Document | K01–K04, K43 |
| Technical Design Document | K05, K06, K59, K64, K65 |
| Art Bible | K56–K58 |
| Audio Bible | K55 |
| Combat Guide | K17, K28–K35 |
| World Bible | K07–K15 |
| Monster Bible | K16–K27 |
| Quest Bible | K44–K51 |
