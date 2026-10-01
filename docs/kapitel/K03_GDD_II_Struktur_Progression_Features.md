# K03 · GDD II – Spielstruktur, Progression, Feature-Matrix

| Feld | Wert |
|---|---|
| Dokument | Kapitel 03 von 68 · Game Design Document, Teil II |
| Version | 1.0 |
| Owner | Game Director |
| Mitwirkende | RPG Systems Designer, Level Designer, Producer, Lead Gameplay Programmer, Network Engineer |
| Baut auf | K01, K02 (CANON §1–§16) |
| Status | ✅ Freigegeben |
| Neue Kanon-Einträge | CANON §17 (Spielstruktur & Zustände), §18 (Kampfset & Fähigkeitserwerb), §19 (Content-Verteilung), §20 (Kodex-Reihenfolge) |

---

## Inhalt

1. [Spielmodi](#1-spielmodi)
2. [Globale Spielzustände (Game Flow)](#2-globale-spielzustände-game-flow)
3. [Hub-Struktur: Siedlungstypen und ihre Dienste](#3-hub-struktur-siedlungstypen-und-ihre-dienste)
4. [Progressionssysteme – Gesamtschau](#4-progressionssysteme--gesamtschau)
5. [Das Kampfset eines Echos & Fähigkeitserwerb](#5-das-kampfset-eines-echos--fähigkeitserwerb)
6. [Erfahrungsquellen und -verteilung](#6-erfahrungsquellen-und--verteilung)
7. [Content-Verteilung pro Region](#7-content-verteilung-pro-region)
8. [Kodex-Nummerierung](#8-kodex-nummerierung)
9. [Menüarchitektur (Top-Level)](#9-menüarchitektur-top-level)
10. [Feature-Abhängigkeiten & kritischer Pfad](#10-feature-abhängigkeiten--kritischer-pfad)
11. [Feature-Matrix nach Meilenstein](#11-feature-matrix-nach-meilenstein)
12. [Datenstrukturen & Code](#12-datenstrukturen--code)
13. [Decision Records](#13-decision-records)
14. [Kanon-Updates](#14-kanon-updates)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Spielmodi

| Modus | Zugang | Spieler | Speicherstand | Online nötig | Beschreibung |
|---|---|---|---|---|---|
| **Weltspiel** (Story + offene Welt) | Hauptmenü | 1 | Eigener Weltstand (3 Slots) | Nein | Kernerfahrung inkl. Endgame-Inhalten offline |
| **Koop-Reise** | Im Weltspiel über Resonanzstein „Chor öffnen“ | 2–4 | Host-Welt; Gäste behalten Chor, Kodex, Items, EP (K60) | Ja (oder lokal Split-Screen 2, *Should*) | Gemeinsam erkunden, kämpfen, Raids im Overworld-Format |
| **Arena-Halle** (PvP) | Menü „Online“ oder Arena-Terminal in jeder Stadt | 2 | Kein Weltstand; nutzt Chor/Hain | Ja | Casual, Ranked, Freundeskampf, Turniere |
| **Raid** | Raid-Portal (Tiefenresonanzen-Eingang) oder Menü | 1–4 (KI füllt auf) | Beute in Weltstand | Ja (Solo-Variante offline → DR-19) | Bosskämpfe mit Phasen (K35) |
| **Tauschhalle** | Menü / Goldklang-Kontor | 2+ | Hain | Ja | Direkt- und Gildentausch (K60) |
| **Fotomodus** | Jederzeit (außer Zwischensequenz) | 1 | Fotoalbum | Nein | Freie Kamera (K39) |
| **Eiserner Wärter** | Modifikator beim Erstellen | 1 | Eigener Slot (markiert) | Nein | Challenge-Regeln (CANON §16) |

**Profil vs. Weltstand (LOCKED):**
- **Profil** (plattformgebunden, cloud-synchronisiert): Einstellungen, Erfolge, PvP-Rang, Gildenzugehörigkeit, Fotoalbum.
- **Weltstand** (bis zu 3 Slots + 1 Eiserner-Wärter-Slot): Welt, Story, Chor, Hain, Inventar, Kodex.
- Online-Funktionen nutzen immer den **aktuell geladenen Weltstand** als Quelle für Echos (Tausch, PvP), damit es keine weltübergreifende Duplikation gibt.

---

## 2. Globale Spielzustände (Game Flow)

### 2.1 Zustandsmodell

Das Spiel kennt **exklusive Zustände** (genau einer aktiv) und **Overlay-Zustände** (über einem exklusiven Zustand gestapelt). Die Trennung verhindert die typische Zustandsexplosion („Menü während Dialog während Kampf“).

```
                       ┌──────────┐
                       │   BOOT   │  Plattform-Init, Shader-Precache, EULA
                       └────┬─────┘
                            ▼
                       ┌──────────┐
                       │  TITLE   │  Profil-Login, Hauptmenü
                       └────┬─────┘
                  Slot wählen / Online-Modus
                            ▼
                       ┌──────────┐
                       │ LOADING  │  World Partition Streaming, Save-Load, Migration
                       └────┬─────┘
          ┌─────────────────┼──────────────────────────────┐
          ▼                 ▼                              ▼
   ┌─────────────┐   ┌──────────────┐               ┌──────────────┐
   │  WORLD.     │◄─►│  WORLD.      │               │  ARENA_HALL  │ (PvP-Lobby, eigene Map)
   │  EXPLORE    │   │  COMBAT      │               └──────────────┘
   │ (Oberwelt)  │◄─►│ (am Ort)     │
   └──┬───┬───┬──┘   └──────┬───────┘
      │   │   │             │ Bindungs-Option nach Erschöpfung
      │   │   └────────────►▼
      │   │          ┌──────────────┐
      │   └─────────►│  WORLD.BOND  │ Resonanzbindung (Anschlag-Phase)
      │              └──────────────┘
      │              ┌──────────────┐
      ├─────────────►│ WORLD.SANCT. │ Resonanzhain (Sub-Level, eigener Streaming-Kontext)
      │              └──────────────┘
      │              ┌──────────────┐
      └─────────────►│ WORLD.CINE   │ Zwischensequenz (Sequencer)
                     └──────────────┘

   OVERLAYS (stapelbar über WORLD.*):  DIALOGUE · MENU · PHOTO · MAP · SYSTEM_PROMPT
```

### 2.2 Übergangstabelle (Auszug, vollständig im Code als Daten)

| Von | Nach | Auslöser | Bedingung | Dauer-Ziel |
|---|---|---|---|---|
| EXPLORE | COMBAT | Kontakt mit aggressivem Echo / Wärter-Herausforderung / Spieler startet Kampf | Kampfkreis-Solver findet Fläche (ADR-013) | < 1,5 s |
| COMBAT | EXPLORE | Sieg, Flucht, Niederlage (→ Rückklang), Bindung abgeschlossen | – | < 1,0 s |
| COMBAT | BOND | Gegner erschöpft + Spieler wählt „Binden“ | Wildes Echo, Siegel vorhanden | sofort |
| EXPLORE | BOND | Oberwelt-Anschlag nach Einstimmen | Echo „ruhig“ (K36) | sofort |
| EXPLORE | SANCTUARY | Resonanzhain-Portal / Menü „Zum Hain“ | Nicht in Kampf, nicht in Koop als Gast | < 4 s (Ladebildschirm-frei durch Vorladen) |
| EXPLORE | CINE | Quest-Trigger | – | – |
| * | DIALOGUE (Overlay) | NPC-Interaktion | Nicht in COMBAT außer Kampfdialog | sofort |
| * | MENU (Overlay) | Menütaste | Pausiert nur offline/Solo; online läuft Welt weiter | sofort |
| * | PHOTO (Overlay) | Fotomodus-Taste | Nicht in CINE | sofort |

### 2.3 Pausierregeln

| Situation | Weltzeit | Kampf-Zeitleiste | Hinweis |
|---|---|---|---|
| Solo, Menü geöffnet | angehalten | angehalten | – |
| Solo, Dialog | angehalten | – | Tageszeit läuft während Dialogen nicht weiter |
| Koop, Menü (eines Spielers) | läuft | läuft nicht (Kämpfe sind pro Spieler-Kreis; Mitspieler kann warten) | Spieler ist für 60 s „geschützt“ (Echos greifen nicht an) |
| PvP | – | Zugtimer läuft | – |
| Fotomodus Solo | angehalten (optional „Zeit läuft“ für Wolken/Wasser) | angehalten | – |

### 2.4 Zustandsverantwortung

- Zustände werden vom **`UAethrisGameFlowSubsystem`** (GameInstance-Subsystem) verwaltet.
- Jeder Zustand ist ein Data Asset (`UGameFlowStateDefinition`) mit Input-Mapping-Kontext, UI-Layer, Audio-Snapshot und erlaubten Overlays → reine Daten, keine Sonderfälle im Code (DR-25).
- Übergänge laufen ausschließlich über das Subsystem, das ein Event `GameFlow.StateChanged` auf dem Event-Bus sendet (CANON §9).

---

## 3. Hub-Struktur: Siedlungstypen und ihre Dienste

| Dienst | Stadt (10) | Dorf (22) | Außenposten (30) | Resonanzstein (Welt) |
|---|---|---|---|---|
| Klangbrunnen (Heilung) | ✔ | ✔ | ✔ (Feldbrunnen, langsamer: 10 s Kanalisieren) | – |
| Schnellreise | ✔ (Stadtstein) | ✔ | ✔ | ✔ |
| Händler (Grundsortiment) | ✔ (mehrere, spezialisiert) | ✔ (1–2) | ✔ (1, Wanderhändler) | – |
| Spezialhändler / seltene Waren | ✔ | Selten (rotierend) | – | – |
| Arena + Arenameister | ✔ | – | – | – |
| Trainingsplatz (Wärter-Kämpfe, Übung) | ✔ | ✔ | – | – |
| Fraktionsbüro | ✔ (alle in Hauptsitz-Stadt, sonst 2–3) | Gelegentlich 1 | Wildwacht-Posten (Außenposten sind meist Wildwacht) | – |
| Questbrett | ✔ | ✔ | ✔ (Aufträge) | – |
| Crafting-Station (Werkbank, Kessel, Schmiede) | ✔ alle 3 | ✔ 1–2 | ✔ Werkbank | Lager-Moment (Feldkessel) |
| Resonanzhain-Portal | ✔ | ✔ | – | ✔ (bei aktivierten Steinen, ab Akt I Mitte) |
| Echo-Pflegestation (Zuchtabgabe, Training) | ✔ | Selten | – | – |
| Tausch-/Online-Terminal | ✔ | – | – | – |
| Gasthaus (Zeit vorspulen, Rast) | ✔ | ✔ | ✔ (Zelt) | Lager-Moment |

**Regel DR-30:** Zwischen zwei Klangbrunnen auf dem Hauptpfad liegen höchstens **800 m** Wegstrecke. (Zusammen mit DR-29 sorgt das für Rhythmus aus Wagnis und Ankunft.)

**Zeit vorspulen:** In Gasthäusern/Zelten/Lager-Moment auf Morgendämmerung, Mittag, Abenddämmerung, Mitternacht (Wetter würfelt dabei neu nach regionaler Tabelle, K14). Wichtig für Spawn- und Evolutionsbedingungen (DR-15, DR-23).

---

## 4. Progressionssysteme – Gesamtschau

AETHRIS hat **zwölf Progressionsspuren**. Sie verteilen sich auf drei Träger: das einzelne Echo, den Wärter und die Welt.

```
 ┌──────────────── ECHO (pro Instanz) ───────────────┐   ┌────────── WÄRTER (pro Weltstand) ─────────┐
 │ P1 Level 1–100           (EP)                      │   │ P6 Wärterrang 1–40   (Wärter-EP)          │
 │ P2 Bindung 0–1000        (Pflege, gemeinsame Zeit) │   │ P7 Skilltree, 4 Äste (Skillpunkte)        │
 │ P3 Kampfset              (Lernen, Klangschriften)  │   │ P8 Ausrüstung        (Crafting/Händler)   │
 │ P4 Evolution             (Bedingungen, K19)        │   │ P9 Ruf bei 5 Fraktionen                   │
 │ P5 Schliff (Training)    (Trainingsaktivitäten)    │   │ P10 Akkorde 0–10                          │
 └────────────────────────────────────────────────────┘   └───────────────────────────────────────────┘
 ┌──────────────── WELT / SAMMLUNG ───────────────────────────────────────────────────────────────────┐
 │ P11 Echo-Kodex (256 Arten × 4 Forschungsstufen = 1.024 Stufen)                                     │
 │ P12 Resonanzhain-Ausbau (Biome im Hain, Kapazität, Zuchtstationen)                                 │
 └────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Spuren im Detail

| # | Spur | Bereich | Maximum | Haupttreiber | Gate für | Kapitel |
|---|---|---|---|---|---|---|
| P1 | Echo-Level | Echo | 100 | Kampf-EP, Training, Entdeckung | Fähigkeiten, Evolution, Werte | K18/K63 |
| P2 | Bindung | Echo | 1000 (6 Stufen) | Pflege, Kämpfe gemeinsam, Reisen, Fütterung | Crescendo, Bindungs-Evolution, Gehorsam (gehandelte Echos) | K37 |
| P3 | Kampfset | Echo | 4 aktiv + 1 passiv + 1 Crescendo | Level, Klangschriften, Tutoren, Vererbung | Taktik | §5, K28–K30 |
| P4 | Evolution | Echo | 1–3 Stufen / Spezial | Bedingungen | Werte, Optik | K19 |
| P5 | Schliff | Echo | Summe 240 (pro Wert max. 80) | Trainingsaktivitäten, Gegner-Art | Werteausrichtung | K18 |
| P6 | Wärterrang | Wärter | 40 | Alle Aktivitäten | Skillpunkte, Chorgröße, Features | K43 |
| P7 | Skilltree | Wärter | 50 Punkte, 4 Äste | Wärterrang, Meilensteine | Bindungs-, Überlebens-, Forschungs-, Kampfboni | K43 |
| P8 | Ausrüstung | Wärter | Stufe I–V | Crafting, Händler, Fraktionen | Traversal, Komfort, Bindungs-Boni (gedeckelt, DR-01) | K40/K41 |
| P9 | Ruf | Wärter | 5 Fraktionen × 6 Ränge | Fraktionsquests, Entscheidungen | Belohnungen, Händler, Quests | K47 |
| P10 | Akkorde | Wärter | 10 | Arenen | Story, Gehorsamsgrenze, Ranked | K02/K11/K12 |
| P11 | Echo-Kodex | Sammlung | 1.024 Forschungsstufen | Beobachten, Kämpfen, Foto, Binden, Züchten | Bindungsboni, Infos, Evolutionshinweise | K39 |
| P12 | Hain-Ausbau | Sammlung | 10 Biom-Gärten, Kapazität 600 | Sol, Material, Fraktion Wildwacht | Lagerplatz, Zucht, Echo-Wohlbefinden | K37 |

### 4.2 Gehorsam (LOCKED-Prinzip)

Ein Echo gehorcht im Kampf vollständig, wenn **eine** der Bedingungen erfüllt ist:
1. Der Spieler hat es selbst gebunden oder gezüchtet, **oder**
2. sein Level ≤ **Gehorsamsgrenze** = 20 + 8 × Akkorde (10 Akkorde → 100), **oder**
3. seine Bindung zum aktuellen Wärter ≥ Stufe 3 (K37).

Ungehorsam (nur getauschte Echos über der Grenze) wirkt nicht durch zufälliges Verweigern (DR-07!), sondern deterministisch: Das Echo erhält **+40 % Zeitkosten** pro Aktion („zögert“). Lesbar auf der Zeitleiste, nie ein verschwendeter Zug.

---

## 5. Das Kampfset eines Echos & Fähigkeitserwerb

### 5.1 Kampfset (LOCKED, ADR-016)

| Slot | Anzahl | Herkunft | Wechselbar |
|---|---|---|---|
| Aktive Fähigkeit | **4** | Lernset (Level), Klangschriften, Tutoren, Vererbung, Evolution | Außerhalb des Kampfes jederzeit aus allen gelernten („Repertoire“) |
| Passive Fähigkeit | **1** | Aus 1–3 art-spezifischen Optionen; 1 versteckte (Zucht/seltene Fundorte) | An Pflegestation mit **Wandelklang** (Item) |
| Crescendo (Ultimate) | **1** | Art-spezifisch (bzw. pro Evolutionslinie) | Nein; freigeschaltet ab **Bindungsstufe 2** |
| Feldfähigkeit | 0–1 | Art-spezifisch | Nein; nutzbar ab Bindungsstufe 1 |

**Repertoire:** Ein Echo vergisst nichts. Alle je gelernten aktiven Fähigkeiten bleiben im Repertoire und können außerhalb des Kampfes frei in die 4 Slots gelegt werden. *Begründung:* DR-23 (Respekt vor Spielerzeit) – kein „Fähigkeit verlernen“-Frust, kein Item-Grind.

### 5.2 Fähigkeitserwerb

| Quelle | Beschreibung | Anteil am Repertoire (Ziel, typisches Echo Lv. 60) |
|---|---|---|
| **Lernset** | Art-spezifisch, Level-Schwellen | 55 % |
| **Klangschriften** | Wiederverwendbare Items (nicht verbrauchend!), die einem kompatiblen Echo eine Fähigkeit lehren. 90 Klangschriften im Spiel. | 25 % |
| **Tutoren** | NPCs in Städten (gegen Sol/Material/Ruf), lehren seltene Fähigkeiten | 10 % |
| **Vererbung** | Zucht (K38) | 5 % |
| **Evolution** | Evolutionsfähigkeiten beim Entwickeln | 5 % |

---

## 6. Erfahrungsquellen und -verteilung

### 6.1 Echo-EP

| Quelle | Wer erhält | Ziel-Anteil Echo-EP (Story) |
|---|---|---|
| Kampf (Sieg/Bindung) | Kämpfende Echos 100 %, Reserve-Chor 50 % („Chor-Lernen“, immer aktiv) | 70 % |
| Training (Lager-Moment, Trainingsplätze) | gewähltes Echo | 10 % |
| Entdeckung (POIs, Resonanzsteine, Kodex-Stufen) | ganzer Chor | 15 % |
| Questbelohnungen | ganzer Chor | 5 % |

*Entscheidung:* Kein „EP-Teiler“-Item. Der ganze Chor lernt immer mit (50 %), damit Chorwechsel nie bestraft werden. Spieler, die Überleveln vermeiden wollen, können **„Chor-Lernen“** in den Optionen reduzieren (100 % / 50 % / 0 %).

### 6.2 Wärter-EP

| Quelle | Ziel-Anteil |
|---|---|
| Hauptquests | 25 % |
| Nebenquests & Aufträge | 25 % |
| Kodex-Forschung | 20 % |
| Entdeckung (POIs, Steine, Regionen) | 15 % |
| Arenen & Wärterkämpfe | 10 % |
| Crafting & Sonstiges | 5 % |

*Begründung:* Wärter-EP bewusst breit verteilt → jeder Spielstil (Persona Mara, Jonas, Deniz) kommt voran.

---

## 7. Content-Verteilung pro Region

**LOCKED** (Summen müssen CANON §3 entsprechen; vom Daten-Validator geprüft).

| ID | Region | Fläche km² | Neue Arten (Erstvorkommen) | Ursprungsstimme | Dörfer | Außenposten | Nebenquests | Resonanzsteine | POIs (Ziel) | Dungeons/Höhlen |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Verdanthain | 4,0 | 32 | 1 | 2 (inkl. Lindwiesen) | 3 | 24 | 9 | 130 | 3 |
| R02 | Kharsgrat | 4,0 | 26 | 1 | 2 | 3 | 22 | 9 | 125 | 4 |
| R03 | Morvenmoor | 3,2 | 26 | 1 | 2 | 3 | 21 | 7 | 105 | 3 |
| R04 | Sahrun-Weite | 4,4 | 24 | 1 | **3** (+ Wanderdorf) | 3 | 22 | 9 | 120 | 3 |
| R05 | Ignareth | 3,0 | 22 | 1 | 2 | 3 | 19 | 7 | 95 | 4 |
| R06 | Saltrand | 3,4 | 26 | 1 | **3** (+ Treibdorf) | 3 | 23 | 8 | 115 | 3 |
| R07 | Hvitfell | 3,6 | 22 | 1 | 2 | 3 | 20 | 8 | 105 | 3 |
| R08 | Ael'Dorun | 2,8 | 20 | 1 | 2 | 3 | 21 | 6 | 110 | 5 |
| R09 | Prismtiefen | 3,6 | 20 | 1 | 2 | 3 | 18 | 8 | 100 | 6 (inkl. Tiefenresonanzen-Zugänge) |
| R10 | Nimbara | 4,0 (Footprint) | 22 | 1 | 2 | 3 | 20 | 9 | 110 | 3 |
| **Σ** | | **36,0** | **240** | **10** | **22** | **30** | **210** | **80** | **~1.115** | **37** |

Zusätzlich **6 Mythische** (#251–#256) ohne feste Region (Endgame, Tiefenresonanzen, globale Ereignisse wie Resonanzsturm W10).

**Hinweis Prismtiefen:** Die 3,6 km² umfassen den Oberflächen-Footprint (Kraterzugänge zwischen Kharsgrat und Ael'Dorun); das Höhlensystem selbst liegt unter diesen Regionen in eigenen Streaming-Zellen und zählt nicht doppelt.

**Arten pro Region gesamt (inkl. regionsübergreifender Vorkommen):** Jede Region beherbergt neben ihren Erstvorkommen 20–40 % Arten aus Nachbarregionen; Ziel: **45–65 Arten pro Region** auffindbar.

---

## 8. Kodex-Nummerierung

Der Kodex ist nach **Erstvorkommen in der Story-Reihenfolge** nummeriert (LOCKED). Damit fällt die Reihenfolge der Kataloge K20–K27 fest:

| Kodex-Bereich | Region | Katalog-Kapitel |
|---|---|---|
| #001–#032 | R01 Verdanthain (inkl. Starter #001–#009) | K20 |
| #033–#058 | R02 Kharsgrat | K21 (bis #064) |
| #059–#084 | R03 Morvenmoor | K21/K22 |
| #085–#110 | R06 Saltrand | K22/K23 |
| #111–#134 | R04 Sahrun-Weite | K23/K24 |
| #135–#156 | R05 Ignareth | K24 |
| #157–#178 | R07 Hvitfell | K25 |
| #179–#198 | R08 Ael'Dorun | K25/K26 |
| #199–#218 | R09 Prismtiefen | K26 |
| #219–#240 | R10 Nimbara | K27 |
| #241–#250 | Die 10 Ursprungsstimmen | K27 |
| #251–#256 | Die 6 Mythischen | K27 |

**Evolutionslinien bleiben zusammenhängend nummeriert**, auch wenn eine spätere Stufe erst in einer anderen Region vorkommt (Linie wird bei ihrer Basisform einsortiert).

### 8.1 Linienstruktur (LOCKED-Ziel, finale Zuordnung K20–K27)

| Linientyp | Linien | Arten |
|---|---|---|
| 3-stufig | 40 | 120 |
| 2-stufig | 45 | 90 |
| Ohne Evolution | 22 | 22 |
| Spezialentwicklungen (Zweige/Sonderformen zusätzlich zu Linien) | – | 8 |
| **Reguläre Arten** | | **240** |
| Ursprungsstimmen + Mythische | | 16 |
| **Gesamt** | | **256** |

Spezialentwicklungen sind Verzweigungen (z. B. eine 2. Stufe entwickelt sich je nach Wetter in eine von zwei Endformen) – die 8 zusätzlichen Arten sind diese alternativen Formen.

---

## 9. Menüarchitektur (Top-Level)

Pausenmenü als **Radial-Hub** (Gamepad) bzw. Tab-Leiste (Maus/Tastatur). Detaildesign K54.

```
                         ┌──────────┐
                ┌────────│  CHOR    │────────┐
                │        └──────────┘        │
          ┌──────────┐                 ┌──────────┐
          │  KODEX   │                 │ INVENTAR │
          └──────────┘    [ WÄRTER ]   └──────────┘
          ┌──────────┐   (Zentrum:     ┌──────────┐
          │  KARTE   │   Rang, Sol,    │ CRAFTING │
          └──────────┘   Skilltree)    └──────────┘
                │        ┌──────────┐        │
                └────────│ QUESTLOG │────────┘
                         └──────────┘
          Unterleiste: Fotoalbum · Online · Einstellungen · Speichern
```

| Bereich | Inhalt | Shortcut |
|---|---|---|
| Chor | 6 Echos, Kampfset, Werte, Bindung, Formation-Vorgabe | Steuerkreuz ↑ (gehalten) |
| Kodex | 256 Einträge, Forschungsstufen, Fundorte | – |
| Inventar | Taschen nach Kategorie (Siegel, Heilung, Material, Schlüssel, Klangschriften, Ausrüstung) | – |
| Karte | Weltkarte, Wetterprognose (Skilltree Forschung), Resonanzsteine | Touchpad/View |
| Crafting | Rezepte, Stationen (mobile Rezepte im Feld) | – |
| Questlog | Haupt-, Neben-, Fraktions-Quests, Jagden, Rätsel | – |
| Wärter (Zentrum) | Rang, Skilltree, Ausrüstung, Ruf, Akkorde | – |

---

## 10. Feature-Abhängigkeiten & kritischer Pfad

### 10.1 Abhängigkeitsgraph (Produktion)

```
 [Core Framework K06] ──┬──► [Echo-Datenmodell K16] ──► [Typen K17] ──► [Werte K18] ──► [Fähigkeiten K28-30]
                        │                                                                  │
                        │                                                                  ▼
                        ├──► [Game Flow §2] ─────────────────────────────────────► [Kampf K31-33] ──► [Kampf-KI K34] ──► [Raids K35]
                        │                                                                  │                               ▲
                        ├──► [Welt-Streaming K08] ──► [Wetter K14] ──► [Tageszeit K15]     │                               │
                        │            │                     │                                ▼                               │
                        │            ▼                     └────────────────► [Spawns/Ökologie K52] ──► [Bindung K36] ─────┤
                        │   [Biome/Städte K09-13] ──► [NPC-KI K53] ──► [Quests K48]                   │                    │
                        │                                                   │                         ▼                    │
                        ├──► [Inventar] ──► [Crafting K41] ──► [Wirtschaft K42]                [Begleiter K37] ──► [Zucht K38]
                        │                                                                                                  │
                        ├──► [Save K64] ◄──────────────────── (alle Systeme registrieren Save-Fragmente)                   │
                        └──► [Netzwerk K59] ──► [Koop/Tausch K60] ──► [PvP K61] ───────────────────────────────────────────┘
```

### 10.2 Kritischer Pfad (Vertical Slice)

`Core Framework → Echo-Datenmodell → Typen/Werte → 40 Fähigkeiten → Kampf (Duell+Duo) → Bindung → Welt-Streaming (3 km²) → Wetter/Tageszeit → Ökologie (2 Herdenarten) → Quests (5) → Save`

Alles, was nicht auf diesem Pfad liegt (Zucht, PvP, Raids, Gilden, Fotografie-Bewertung), wird im VS höchstens als Prototyp gezeigt.

---

## 11. Feature-Matrix nach Meilenstein

Legende: **P** Prototyp · **F** funktional (Pre-Alpha) · **C** content-vollständig · **Q** Ship-Qualität

| Feature | Greenlight (Jun 27) | Vertical Slice (Mär 28) | Alpha (Feb 30) | Beta (Jun 30) | Gold (Sep 30) |
|---|---|---|---|---|---|
| Zeitleisten-Kampf | P | F (Duell/Duo) | C (alle Formate) | Q | Q |
| Resonanzbindung | P | F | C | Q | Q |
| Welt (Fläche) | Graybox 1 km² | 3 km² Q-Grafik | 36 km² C | Q | Q |
| Echos | 6 (Graybox) | 16 | 256 | Q | Q |
| Fähigkeiten | 20 | 60 | 330 | Q | Q |
| Wetter/Tageszeit | P | F (5 Wetter) | C (10) | Q | Q |
| Ökologie/Schwärme | P (1 Herde) | F | C | Q | Q |
| Städte | – | 1 (Eichenhall) | 10 | Q | Q |
| Quests | 1 | 5 | 32 Haupt + 210 Neben | Q | Q |
| Zucht/Genetik | Papier | P | C | Q | Q |
| Kodex/Fotografie | – | F (Kodex) / P (Foto) | C | Q | Q |
| Crafting/Wirtschaft | – | F (Basis) | C | Q (Balancing) | Q |
| Skilltree | – | P | C | Q | Q |
| Koop | – | P (2 Spieler) | F (4) | Q | Q |
| PvP Ranked | – | – | F | Q (Beta-Saison) | Q |
| Raids | – | – | F (2 Bosse) | C (6) | Q |
| Switch 2 | Render-Test | 30+ FPS Gate | F | Q | Q (Zertifizierung) |

---

## 12. Datenstrukturen & Code

### 12.1 Game-Flow-Zustände

```cpp
// AethrisGame/GameFlow/GameFlowTypes.h
// Globale Spielzustände (K03 §2). Exklusive Zustände werden über GameplayTags
// identifiziert, damit neue Zustände per Daten ergänzt werden können (DR-25).
//
// Tag-Hierarchie (LOCKED):
//   GameFlow.Boot, GameFlow.Title, GameFlow.Loading, GameFlow.ArenaHall,
//   GameFlow.World.Explore, GameFlow.World.Combat, GameFlow.World.Bond,
//   GameFlow.World.Sanctuary, GameFlow.World.Cinematic
//   GameFlow.Overlay.Dialogue, .Menu, .Photo, .Map, .SystemPrompt

/** Daten eines Spielzustands – ein Data Asset pro Zustand. */
UCLASS(BlueprintType)
class AETHRISGAME_API UGameFlowStateDefinition : public UPrimaryDataAsset
{
    GENERATED_BODY()
public:
    /** Eindeutiger Zustands-Tag (GameFlow.*). */
    UPROPERTY(EditDefaultsOnly) FGameplayTag StateTag;

    /** true = Overlay (stapelbar), false = exklusiver Zustand. */
    UPROPERTY(EditDefaultsOnly) bool bIsOverlay = false;

    /** Erlaubte Overlays über diesem Zustand. */
    UPROPERTY(EditDefaultsOnly) FGameplayTagContainer AllowedOverlays;

    /** Erlaubte Folgezustände (Whitelist). */
    UPROPERTY(EditDefaultsOnly) FGameplayTagContainer AllowedTransitions;

    /** Enhanced-Input-Kontext, der in diesem Zustand aktiv ist. */
    UPROPERTY(EditDefaultsOnly) TSoftObjectPtr<UInputMappingContext> InputContext;

    /** Pausiert dieser Zustand die Weltzeit im Solo-Spiel? (§2.3) */
    UPROPERTY(EditDefaultsOnly) bool bPausesWorldTimeSolo = false;

    /** Audio-Mix-Snapshot (K55). */
    UPROPERTY(EditDefaultsOnly) TSoftObjectPtr<USoundControlBusMix> AudioMix;
};
```

```cpp
// AethrisGame/GameFlow/AethrisGameFlowSubsystem.h
/**
 * Verwaltet exklusiven Zustand + Overlay-Stapel.
 * Einziger erlaubter Weg, Spielzustände zu wechseln (K03 §2.4).
 */
UCLASS()
class AETHRISGAME_API UAethrisGameFlowSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()
public:
    /** Versucht, in einen exklusiven Zustand zu wechseln. Liefert false, wenn der Übergang nicht erlaubt ist. */
    UFUNCTION(BlueprintCallable) bool RequestState(FGameplayTag NewState);

    /** Legt ein Overlay auf den Stapel, falls der aktuelle Zustand es erlaubt. */
    UFUNCTION(BlueprintCallable) bool PushOverlay(FGameplayTag Overlay);

    UFUNCTION(BlueprintCallable) void PopOverlay(FGameplayTag Overlay);

    UFUNCTION(BlueprintPure) FGameplayTag GetCurrentState() const { return CurrentState; }

    /** true, wenn Weltzeit gerade laufen darf (berücksichtigt Solo/Koop und Overlays). */
    UFUNCTION(BlueprintPure) bool IsWorldTimeRunning() const;

private:
    bool IsTransitionAllowed(FGameplayTag From, FGameplayTag To) const;

    UPROPERTY() TMap<FGameplayTag, TObjectPtr<UGameFlowStateDefinition>> States;
    FGameplayTag CurrentState;
    TArray<FGameplayTag> OverlayStack;
};
```

```cpp
// AethrisGame/GameFlow/AethrisGameFlowSubsystem.cpp (Auszug)
bool UAethrisGameFlowSubsystem::RequestState(FGameplayTag NewState)
{
    if (!IsTransitionAllowed(CurrentState, NewState))
    {
        UE_LOG(LogAethrisFlow, Warning, TEXT("Übergang %s -> %s nicht erlaubt."),
            *CurrentState.ToString(), *NewState.ToString());
        return false;
    }

    // Overlays, die im neuen Zustand nicht erlaubt sind, werden geschlossen.
    const UGameFlowStateDefinition* Def = States.FindChecked(NewState);
    OverlayStack.RemoveAll([Def](const FGameplayTag& O){ return !Def->AllowedOverlays.HasTagExact(O); });

    const FGameplayTag Old = CurrentState;
    CurrentState = NewState;

    // Event-Bus statt direkter Abhängigkeiten (CANON §9).
    FGameFlowStateChangedMsg Msg{Old, NewState};
    UAethrisEventBus::Get(this).Broadcast(AethrisTags::Event_GameFlow_StateChanged, Msg);
    return true;
}
```

### 12.2 Regionsbudget-Validierung

```cpp
// AethrisCore/World/RegionContentBudgetRow.h
/** Eine Zeile aus Data/World/RegionBudget.csv (K03 §7). Wird vom Editor-Validator gegen den tatsächlich platzierten Content geprüft. */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FRegionContentBudgetRow : public FTableRowBase
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere) FName RegionId;          // R01..R10
    UPROPERTY(EditAnywhere) float AreaKm2 = 0.f;
    UPROPERTY(EditAnywhere) int32 FirstAppearanceSpecies = 0;
    UPROPERTY(EditAnywhere) int32 Villages = 0;
    UPROPERTY(EditAnywhere) int32 Outposts = 0;
    UPROPERTY(EditAnywhere) int32 SideQuests = 0;
    UPROPERTY(EditAnywhere) int32 ResonanceStones = 0;
    UPROPERTY(EditAnywhere) int32 TargetPOIs = 0;
    UPROPERTY(EditAnywhere) int32 Dungeons = 0;
};
```

Die Datei `Data/World/RegionBudget.csv` wird in diesem Kapitel angelegt (siehe Repository).

### 12.3 Gehorsamsprüfung (Pseudocode)

```text
FUNKTION GetObedienceTimeMultiplier(echo, warden):
    WENN echo.OriginalWardenId == warden.Id: RÜCKGABE 1.0          // selbst gebunden/gezüchtet
    WENN echo.Level <= 20 + 8 * warden.AkkordCount: RÜCKGABE 1.0
    WENN BondTier(echo.Bond) >= 3: RÜCKGABE 1.0
    RÜCKGABE 1.4                                                     // „zögert“, deterministisch, DR-07
```

---

## 13. Decision Records

### ADR-016 – Kampfset 4 + 1 + 1 mit Repertoire
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) 4 Fähigkeiten, Verlernen nötig | Genre-vertraut | Frust, Item-Grind, DR-23 |
| (b) 4 aktiv + 1 passiv + 1 Crescendo, Repertoire frei wechselbar | Taktische Vorbereitung statt Grind; Crescendo verknüpft Kampf mit Bindung (S2) | Mehr UI; Teams leichter auf Gegner anpassbar → Arenameister brauchen Gegenstrategie-KI (K34) |
- **Entscheidung:** (b).

### ADR-017 – Klangschriften wiederverwendbar
- **Entscheidung:** Fähigkeits-Lehrgegenstände werden nicht verbraucht. Begründung: DR-18 (Zeit statt Ressourcen-Grind), Sammelanreiz (90 Stück als Weltfunde/Belohnungen). Nachteil: Ökonomischer Wert fällt weg → Klangschriften sind **nicht handelbar** und nicht verkaufbar.

### ADR-018 – Chor-Lernen statt EP-Teiler-Item
- **Entscheidung:** Reserve erhält immer 50 % EP; Option zum Reduzieren. Begründung: Wechsel nie bestrafen (DR-10), einfache Mathematik für Balancing (K63).

### ADR-019 – Deterministischer Ungehorsam
- **Entscheidung:** Statt zufälliger Befehlsverweigerung +40 % Zeitkosten. Begründung: DR-07, DR-10.

### ADR-020 – Kodex nach Story-Erstvorkommen
- **Entscheidung:** Kodex-Nummern folgen der empfohlenen Story-Reihenfolge (R01, R02, R03, R06, R04, R05, R07, R08, R09, R10). Da Akt I/II frei sind, sieht nicht jeder Spieler die Nummern aufsteigend – akzeptiert; die Nummer ist Ordnung, nicht Pfad.

### ADR-021 – Profil/Weltstand-Trennung und Online-Quelle
- **Entscheidung:** Online-Aktionen nutzen nur den geladenen Weltstand. Verhindert Duplikation über Slots und vereinfacht Cheat-Prüfung (R-10).

---

## 14. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §17 | Spielmodi (7), Profil vs. Weltstand (3 Slots + 1 Eiserner Wärter) | LOCKED |
| §17 | Zustands-Tags `GameFlow.*`, Overlay-Prinzip, `UAethrisGameFlowSubsystem`, `UGameFlowStateDefinition` | LOCKED |
| §17 | Pausierregeln (§2.3) | LOCKED |
| §17 | Siedlungsdienste-Matrix, DR-30 (≤800 m zwischen Klangbrunnen) | LOCKED |
| §18 | Kampfset 4 aktiv + 1 passiv + 1 Crescendo (+0–1 Feld), Repertoire | LOCKED |
| §18 | Crescendo ab Bindungsstufe 2, Feldfähigkeit ab Stufe 1 | LOCKED |
| §18 | Klangschriften: 90, wiederverwendbar, nicht handelbar | LOCKED |
| §18 | Wandelklang (Item für Passiv-Wechsel) | LOCKED |
| §18 | Schliff: Summe 240, pro Wert max. 80 | PROVISIONAL → K18 |
| §18 | Gehorsamsgrenze 20 + 8 × Akkorde; Ungehorsam = +40 % Zeitkosten | LOCKED |
| §18 | Chor-Lernen: Reserve 50 % EP (Option 100/50/0) | LOCKED |
| §18 | Bindungsstufen: 6 (Grenzen → K37) | LOCKED (Anzahl) |
| §18 | Ruf: 6 Ränge pro Fraktion | LOCKED (Anzahl) |
| §18 | Hain: 10 Biom-Gärten, Kapazität 600 | PROVISIONAL → K37 |
| §19 | Regionsbudget-Tabelle (§7) inkl. Flächen | LOCKED |
| §19 | Resonanzsteine 80, POIs ~1.115, Dungeons 37 | LOCKED (Ziel) |
| §19 | Sonderdörfer: Wanderdorf (R04), Treibdorf (R06) | LOCKED |
| §20 | Kodex-Bereiche je Region (§8), Linienstruktur 40×3 + 45×2 + 22×1 + 8 Spezial = 240 | LOCKED |
| §10 | ADR-016 – ADR-021 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] 7 Spielmodi, Profil-/Weltstand-Modell
- [x] Globale Zustandsmaschine (exklusiv + Overlays), Übergangstabelle, Pausierregeln
- [x] Siedlungsdienste-Matrix, Zeit vorspulen, DR-30
- [x] 12 Progressionsspuren mit Maxima, Treibern und Gates
- [x] Gehorsamsregel (deterministisch)
- [x] Kampfset 4+1+1, Repertoire, Fähigkeitserwerb (Lernset, Klangschriften, Tutoren, Vererbung, Evolution)
- [x] Echo-EP- und Wärter-EP-Verteilung, Chor-Lernen
- [x] Content-Verteilung pro Region (Flächen, Arten, Siedlungen, Quests, Steine, POIs, Dungeons) – Summen validiert
- [x] Kodex-Nummerierung nach Region und Linienstruktur (240 + 16)
- [x] Menü-Top-Level-Architektur
- [x] Feature-Abhängigkeitsgraph, kritischer Pfad Vertical Slice
- [x] Feature-Matrix nach Meilenstein
- [x] Code: `UGameFlowStateDefinition`, `UAethrisGameFlowSubsystem`, `FRegionContentBudgetRow`, Gehorsam
- [x] `Data/World/RegionBudget.csv` angelegt
- [x] ADR-016 – ADR-021, CANON aktualisiert

➡️ **Nächstes Kapitel: K04 – Kanon, Glossar, Namens- & ID-Konventionen.**
