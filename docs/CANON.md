# CANON – Single Source of Truth

**Projekt:** AETHRIS: Echobound · **Pflege:** Creative Director (Inhalt), QA Lead (Konsistenzprüfung) · **Letztes Update:** K02

Dieses Dokument enthält **alle verbindlichen Designentscheidungen**. Jedes Kapitel liest es vor Beginn und schreibt am Ende neue Einträge hinein.

- `LOCKED` – verbindlich. Änderung nur per Change Request (§10).
- `PROVISIONAL` – Arbeitsstand. Wird im angegebenen Kapitel finalisiert.

---

## §1 Identität

| Schlüssel | Wert | Status | Quelle |
|---|---|---|---|
| Titel | AETHRIS: Echobound | LOCKED | K01 ADR-001 |
| Genre | Open-World-Monster-Collecting-RPG, rundenbasierte Kämpfe | LOCKED | K01 |
| Engine | Unreal Engine 5.6 | LOCKED | K01 ADR-003 |
| Plattformen | PC, PS5, Xbox Series X\|S, Nintendo Switch 2 | LOCKED | K01 §11 |
| FPS-Ziel | 60 auf allen Plattformen; Switch 2 Fallback 30 (Gate: VS-Review) | LOCKED | K01 §11 |
| Altersfreigabe-Ziel | PEGI 7 / USK 6 / ESRB E10+ | LOCKED | K01 §10 |
| Geschäftsmodell | Premium + Expansion-Pass (2 Erweiterungen) + rein kosmetischer Shop, keine Lootboxen, kein P2W | LOCKED | K01 §14 |
| Release-Ziel | November 2030 | PROVISIONAL → K67 | K01 §16 |

## §2 Design-Säulen (LOCKED, K01 §3)

| # | Säule | Priorität |
|---|---|---|
| S1 | Lebendige Resonanz | 3 |
| S2 | Bindung durch Verstehen | 1 |
| S3 | Taktische Harmonie | 2 |
| S4 | Erbe & Einzigartigkeit | 4 |
| S5 | Gemeinsamer Chor | 5 |

## §3 Content-Zielzahlen (LOCKED, K01 §9)

| Schlüssel | Wert |
|---|---|
| Weltfläche | 36 km² (32 km² Boden + 4 km² Himmelinseln-Footprint) |
| Regionen | 10 (1 Biom = 1 Region) |
| Städte / Dörfer / Außenposten | 10 / 22 / 30 |
| Echo-Arten Grundspiel | 256 (Kodex #001–#256), davon 16 legendär/mythisch (10 Ursprungsstimmen + 6 Mythische) |
| Typen | 15 |
| Fähigkeiten | 330 = 180 Aktiv + 90 Passiv + 30 Ultimate + 30 Feld |
| Hauptquests | ~32 (PROVISIONAL → K44–K46) |
| Nebenquests | 210 (SQ001–SQ210) |
| Fraktionen | 5 |
| Wetterzustände | 10 |
| Arenen | 10 (1 pro Stadt) |
| Endgame-Dungeons („Tiefenresonanzen“) | 8 |
| Raid-Bosse zum Launch | 6 |

## §4 Welt

### §4.1 Prämisse (LOCKED, K01 §5)
- Kontinent **Aethris**, einst durchdrungen vom **Weltlied** (*Aethersang*).
- Vor ~1.000 Jahren: **Die Große Stille** – das Weltlied zerbrach.
- **Echos** = Kreaturen als lebende Fragmente des Weltlieds.
- **Wärter** = Menschen, die beruflich mit Echos in Resonanz treten. Spielercharakter ist ein junger Wärter aus Verdanthain mit der seltenen Gabe, die **Grundfrequenz** eines Echos zu hören.
- **Stillezonen** = Gebiete, in denen Echos erstarren/verblassen (Kernkonflikt).

### §4.2 Regionen (LOCKED, K01 §5.1)

| ID | Region | Biom | Hauptstadt | Akt |
|---|---|---|---|---|
| R01 | Verdanthain | Wälder | Eichenhall | I (Start) |
| R02 | Kharsgrat | Gebirge | Kharsholm | I–II |
| R03 | Morvenmoor | Sümpfe | Morvenfurt | I–II |
| R04 | Sahrun-Weite | Wüste | Qasr Sahrun | II |
| R05 | Ignareth | Vulkan | Schlackenwehr | II |
| R06 | Saltrand | Küste | Saltrand-Hafen | I–II |
| R07 | Hvitfell | Schnee | Hvitmark | II–III |
| R08 | Ael'Dorun | Ruinen | Dorunsruh | II–III |
| R09 | Prismtiefen | Kristallhöhlen | Prismara | III + Endgame |
| R10 | Nimbara | Himmelinseln | Aerion | III + Finale |

### §4.3 Zeit (LOCKED, K01 §8)
- 24-h-Spieltag = **72 Echtzeitminuten** (1 Spielstunde = 3 Minuten).
- Phasen: Morgendämmerung, Tag, Abenddämmerung, Nacht (Stundengrenzen → K15, PROVISIONAL).

### §4.4 Wetter (LOCKED, K01 §9.2)

| ID | Wetter | ID | Wetter |
|---|---|---|---|
| W01 | Klar | W06 | Hitzewelle |
| W02 | Regen | W07 | Sandsturm |
| W03 | Gewittersturm | W08 | Aurora |
| W04 | Nebel | W09 | Aschefall |
| W05 | Schneefall | W10 | Resonanzsturm (selten, global, Story/Endgame) |

## §5 Kreaturen (Echos)

| Schlüssel | Wert | Status | Quelle |
|---|---|---|---|
| Oberbegriff | Echo, Plural Echos | LOCKED | ADR-001 |
| Level | 1–100 | LOCKED | ADR-008 |
| Statuswerte | HP, Angriff, Verteidigung, Spezialangriff, Spezialverteidigung, Geschwindigkeit, Präzision, Ausweichen | LOCKED | Briefing/K01 |
| Zusatzmerkmale | Persönlichkeit, Temperament, Wachstumsrate | LOCKED (Ausprägungen → K18) | K01 |
| Evolutionsformen | keine / 2-stufig / 3-stufig / Spezial | LOCKED | K01 |
| Evolutionsauslöser | Level, Bindung, Items, Tageszeit, Wetter, Gebiet, Kombinationen | LOCKED | K01 |
| Bindungswert | 0–1000 (Stufen → K37) | LOCKED (Skala) | K01 §13.3 |
| Pflicht-Animationsstates | Idle, Rennen, Schlafen, Essen, Kämpfen, Spezialangriff, Treffer, Sieg, Niederlage | LOCKED | K01 §8.2 |
| Niederlage | „Erschöpft/verklungen“, nie Tod durch Spieler | LOCKED | ADR-007 |
| Legendäre | 10 **Ursprungsstimmen** + 6 Mythische; immer mit Solo-Zugangsweg | LOCKED (Namen → K07/K27) | K01 §3/§9 |

### §5.1 Typen (LOCKED, K01 §9.1) – Tabelle → K17

| ID | Intern (Code) | Anzeige DE | GameplayTag |
|---|---|---|---|
| T01 | Ember | Glut | `Type.Ember` |
| T02 | Tide | Flut | `Type.Tide` |
| T03 | Stone | Stein | `Type.Stone` |
| T04 | Storm | Sturm | `Type.Storm` |
| T05 | Bloom | Blüte | `Type.Bloom` |
| T06 | Frost | Frost | `Type.Frost` |
| T07 | Void | Leere | `Type.Void` |
| T08 | Light | Licht | `Type.Light` |
| T09 | Venom | Gift | `Type.Venom` |
| T10 | Metal | Metall | `Type.Metal` |
| T11 | Spirit | Geist | `Type.Spirit` |
| T12 | Crystal | Kristall | `Type.Crystal` |
| T13 | Sound | Klang | `Type.Sound` |
| T14 | Gravity | Schwerkraft | `Type.Gravity` |
| T15 | Arcane | Arkan | `Type.Arcane` |

Regel: Ein Echo hat 1 oder 2 Typen. Klang hat erzählerische Sonderrolle, **keine** mechanische Überlegenheit.

## §6 Spieler & Systeme – Begriffe (LOCKED, K01)

| Begriff | Bedeutung | Detail-Kapitel |
|---|---|---|
| **Chor** | Aktiver Trupp, 6 Echos | K33 (ADR-009) |
| **Resonanzhain** | Begehbares Refugium für nicht mitgeführte Echos (ersetzt Box-System) | K37 |
| **Resonanzbindung** | Fangsystem: Annähern → Beruhigen/Locken → Timing-Fenster | K36 (ADR-006) |
| **Resonator** | Dauerhaftes Werkzeug des Wärters für Bindung und Resonanzsinn | K36 |
| **Siegel** | Verbrauchsgut, verankert die Bindung; wird am Resonator angeschlagen, nicht geworfen | K36 |
| **Fallen** | Platzierbare Weltobjekte zum Festhalten/Beruhigen | K36 |
| **Resonanzsinn** | Wahrnehmungsmodus (Spuren, Frequenzen, Nester) | K36/K39 |
| **Echo-Kodex** | Bestiarium mit Forschungsstufen | K39 |
| **Kodex-Linse** | Kamerasystem/Fotografie | K39 |
| **Resonanz-Zeitleiste** | Initiative-basierte Zugfolge (Conditional Turn-Based) | K31 (ADR-005) |
| **Harmonie** | Team-Leiste für Combos | K33 |
| **Crescendo** | Ultimate-Ausführung, verbraucht Harmonie | K30/K33 |
| **Formation** | Vorder-/Hinterreihe | K33 |
| **Wärterrang** | Spielerlevel 1–40 | K43 (ADR-008) |
| **Resonanzsteine** | Schnellreisepunkte | K08 |
| **Tiefenresonanzen** | Endgame-Dungeons | K62 |
| **Arenameister** | Leiter einer Stadt-Arena | K11/K12 |
| **Akkord** | Arena-Abzeichen; 10 Akkorde = *Weltakkord* | K02 §9.2 |
| **Sol** (◎) | Währung (Singular = Plural) | K42 |
| **Rückklang** | Fehlerzustand bei erschöpftem Chor (Regeln §16) | K02 §11.2 |
| **Klangbrunnen** | Heilpunkt in Siedlungen | K02 §4.5 |
| **Lager-Moment** | Rastplatz-Interaktion (Kochen, Füttern, Chor) | K02 §4.4 |

### §6.1 Kampfformate (LOCKED)
Duell 1v1 · Duo 2v2 · Trio 3v3 · Raid (4 Spieler vs. Boss). Wechsel aus Reserve kostet Zeitleisten-Zeit.

### §6.2 Skilltree-Äste (LOCKED, Inhalte → K43)
Bindung · Überleben · Forschung · Kampf

### §6.3 Crafting-Grundressourcen (LOCKED)
Holz · Erz · Kristalle · Kräuter (+ Echo-Materialien, K41)

## §7 Fraktionen (LOCKED Namen, Details → K47)

| ID | Fraktion | Archetyp |
|---|---|---|
| F01 | Akademie der Resonanz | Forscher |
| F02 | Goldklang-Kontor | Händler |
| F03 | Wildwacht | Ranger |
| F04 | Freie Stimmen | Rebellen |
| F05 | Orden der Stille | Antagonisten |

## §8 Leitplanken (LOCKED)

1. **Clean-Room-Policy** (K01 §4.3): keine übernommenen Begriffe, Silhouetten, 1:1-Mechaniken, Typfarben; eigene Namensmorphologie mit Markenprüfung.
2. **Kein Pay-to-Win**, keine Lootboxen, keine käuflichen Echos/Werte/Siegel/Morphs.
3. **Offline vollständig**: Story und Sammeln ohne Online-Zwang.
4. **Echos sterben nicht** durch Spielerhandlung (ADR-007).
5. **Legendäre** haben immer einen Solo-Zugangsweg.

## §9 Technik (LOCKED, K01 §11.3/§13)

| Bereich | Entscheidung |
|---|---|
| Sprache | C++ + Blueprints |
| Fähigkeiten/Status | Gameplay Ability System, rundenbasierter Wrapper `UEchoAbilitySystemComponent` |
| Populationen | Mass Entity (ECS) |
| Einzel-KI | StateTree + Behavior Trees/Blackboards |
| Welt | World Partition, Level Instances, Data Layers, PCG |
| Rendering | Nanite, Lumen, VSM, TSR (Switch 2: eigenes Profil) |
| VFX/Audio | Niagara / MetaSounds + Quartz |
| UI | CommonUI + UMG + MVVM |
| Netzwerk | Iris; Dedicated Server (PvP/Raid), Listen-Server (Koop) |
| Modularität | Game Features Plugins (Liste s. u.) |
| Kommunikation | Feature-Plugins nur über Aethris Event-Bus oder Core-Interfaces |
| Daten | Data Assets + Data Tables, Primary Asset IDs, CSV/JSON-Quelle in Git |

**Module:** `AethrisCore`, `AethrisGame`, `AethrisEditor`
**Game-Feature-Plugins:** `GF_Monsters`, `GF_Combat`, `GF_Capture`, `GF_Companion`, `GF_Breeding`, `GF_World`, `GF_AI`, `GF_Inventory`, `GF_Economy`, `GF_Quests`, `GF_Research`, `GF_UI`, `GF_Audio`, `GF_Save`, `GF_Multiplayer`, `GF_PvP`

**Verbindliche Klassennamen:**
| Name | Art | Zweck |
|---|---|---|
| `UEchoSpeciesDefinition` | UPrimaryDataAsset | Statische Spezies-Daten |
| `FEchoInstance` | USTRUCT | Laufzeit-/Save-Instanz eines Echos (`InstanceId` = FGuid) |
| `FEchoBaseStats` | USTRUCT | 8 Basiswerte |
| `FEchoGenome` | USTRUCT | Allele, Morph, Mutationen |
| `UEchoAbilitySystemComponent` | UAbilitySystemComponent | Rundenbasierter GAS-Wrapper |

**Pflichtfelder `UEchoSpeciesDefinition` (K02, Validator DR-02/05/15):** `ObservableTraits` (≥3), `Niches` (≥1), `Rarity`, `SpawnConditions` (Pflicht ab Rarity ≥ Rare).
**Progression:** `FWardenRankRow` → Data Table `DT_WardenRank` (Quelle `Data/Progression/WardenRank.csv`).

**Namenskonvention:** statische Designdaten = `U…Definition`; Laufzeitdaten = `F…Instance` / `U…Component`. Spezies-IDs `ECHO_###`.

## §10 ADR-Index

| ADR | Titel | Kapitel |
|---|---|---|
| ADR-001 | Titel & Branding, Begriffe Echo/Wärter | K01 |
| ADR-002 | Säulen-Priorität S2>S3>S1>S4>S5 | K01 |
| ADR-003 | Engine UE 5.6 | K01 |
| ADR-004 | Kapitelreihenfolge mit frühem TDD | K01 |
| ADR-005 | Resonanz-Zeitleiste statt simultaner Runden | K01 |
| ADR-006 | Resonanzbindung ohne Wurfgegenstand | K01 |
| ADR-007 | Echos sterben nicht | K01 |
| ADR-008 | Level 1–100, Wärterrang 1–40 | K01 |
| ADR-009 | Chor = 6 Echos | K01 |
| ADR-010 | Design-Regeln DR-01–DR-29 als Regelwerk (DR-19/21/22 unverhandelbar) | K02 |
| ADR-011 | Diegetische Starterwahl „Erstresonanz“ | K02 |
| ADR-012 | Gestaffelte Offenheit, Akkord-skalierte Arenen, einmalig fixierte Wildzonen | K02 |
| ADR-013 | Nahtloser Kampf am Ort (Kampfkreis 12–18 m) | K02 |
| ADR-014 | Rückklang ohne Bindungsverlust | K02 |
| ADR-015 | Spielzeit statt Echtzeit für Wartezeiten | K02 |

## §11 Change Requests

| CR | Datum | Betrifft | Änderung | Begründung | Genehmigt |
|---|---|---|---|---|---|
| – | – | – | – | – | – |

## §12 Offene Punkte (PROVISIONAL-Tracker)

| # | Punkt | Ziel-Kapitel |
|---|---|---|
| Q1 | Zeitleisten-Formel, Tick-Größe | K31 |
| Q2 | Effektivitätsmultiplikatoren | K17 |
| Q3 | Genom: Allelanzahl, Morph-Wahrscheinlichkeiten | K38 |
| Q4 | Koop: geteilter Story-Fortschritt? | K60 |
| Q5 | Ranked-Level-Normalisierung | K61 |
| Q6 | Split-Screen-Koop Machbarkeit | K65 |
| Q7 | Namen der 10 Ursprungsstimmen | K07/K27 |
| Q8 | Bindungsstufen 0–1000 | K37 |
| Q9 | Tagesphasen-Stundengrenzen | K15 |
| Q10 | Hauptquartiere der Fraktionen | K47 |
| Q11 | Bewegungs-/Ausdauer-/Gleiter-Tuning (Startwerte K02 §4.1) | K40 |
| Q12 | Bindungs-Timingfenster (Startwerte K02 §4.2) | K36 |
| Q13 | Arena-Stufentabelle (Startwerte K02 §9.2) | K63 |
| Q14 | Wärterrang-EP-Kurve (Startwerte K02 §13.2) | K43/K63 |

---

## §13 Design-Regeln (LOCKED, K02 §2)

| ID | Kurzform | Säule |
|---|---|---|
| DR-01 | Wissen schlägt Items bei Bindung | S2 |
| DR-02 | ≥3 beobachtbare Verhaltensmerkmale pro Art | S2 |
| DR-03 | Bindung = Dialog; Entscheidung vor Timing | S2 |
| DR-04 | Echos reagieren sichtbar auf Spieler | S2 |
| DR-05 | Kein Echo ist wertlos (≥1 Nische) | S2 |
| DR-06 | Zeitleiste zeigt ≥8 Züge, Zeitkosten vor Bestätigung | S3 |
| DR-07 | Zufall nur mit Gegenspiel und Deckel | S3 |
| DR-08 | Jeder Typ hat eigene Mechanik-Identität | S3 |
| DR-09 | Story auf Standard ohne Combos/Formation gewinnbar | S3 |
| DR-10 | Kein Zug ist verschwendet | S3 |
| DR-11 | Kampfdauer: Wild 60–120 s, Trainer 3–6 min, Arena 8–15 min, Ranked-Trio ≤20 min | S3 |
| DR-12 | Welt läuft ohne Zuschauer (Sim-LOD) | S1 |
| DR-13 | Jedes Weltsystem beeinflusst ≥2 andere | S1 |
| DR-14 | Sichtbare Begegnungen; max. 1 angekündigter Hinterhalt pro Quest | S1 |
| DR-15 | Seltenheit = erlernbare Bedingungen; reiner Zufall nur für Morphs | S1 |
| DR-16 | Jede Instanz speichert Herkunft | S4 |
| DR-17 | Optik nur durch Genetik/Fundort/Leistung, nie Shop | S4 |
| DR-18 | Kompetitiv perfektes Echo in ≤15 h züchtbar | S4 |
| DR-19 | Allein vollständig; keine tauschexklusiven Arten | S5 (unverhandelbar) |
| DR-20 | Koop-Boni nie Machtvorteile | S5 |
| DR-21 | Kompetitives serverautoritativ + levelnormalisiert | S5 (unverhandelbar) |
| DR-22 | Clean-Room hat Vorrang | quer (unverhandelbar) |
| DR-23 | Keine Pflicht-Wartezeit >30 s, keine Echtzeit-Timer für Kernfortschritt | quer |
| DR-24 | Jedes Signal visuell **und** akustisch | quer |
| DR-25 | Content ohne neuen C++-Code (außer neue Primitiva) | quer |
| DR-26 | Drei-Ding-Regel: ≥3 ungeplante Angebote pro 300 m | S1 |
| DR-27 | Kein Belohnungstyp >50 % in 30 min | quer |
| DR-28 | Hauptpfad jeder Region mit frühester Traversal-Ausstattung spielbar | S1 |
| DR-29 | Atemzug-Regel: ≥20 min Ruhe nach Intensität ≥7 | quer |

## §14 Onboarding & Starter (K02 §8)

| Schlüssel | Wert | Status |
|---|---|---|
| Starterwahl | Diegetisch durch Spurwahl im Prolog (ADR-011) | LOCKED |
| Starter-Zyklus | **Blüte > Stein > Sturm > Blüte** (bindend für K17) | LOCKED |
| Starter-Arbeitsnamen | Fernlit (Blüte), Brokk (Stein), Wisplet (Sturm); Kodex #001–#009 | PROVISIONAL → K04/K20 |
| Startdorf | Lindwiesen (R01), angrenzend Lindwald | LOCKED |
| Mentorin | Ysolde Varn – Wildwacht-Wärterin, ehem. Arenameisterin Eichenhall | LOCKED |
| Rivale | Kael Duran – Jugendfreund, Akademie-Anwärter | LOCKED |
| Onboarding-Ende | Ankunft Eichenhall (~3:00 h); Gleiter bei ~2:20 h | LOCKED (Timing-Ziel) |

## §15 Progression (K02 §9)

| Schlüssel | Wert | Status |
|---|---|---|
| Struktur | Prolog (R01) → Akt I: R01, dann R02/R03/R06 frei → Akt II: R04/R05/R07 frei, R08 nach 2 weiteren → Akt III: R09, R10 | LOCKED |
| Akkorde | Akt I: 4 (Eichenhall fix zuerst), Akt II: 4, Akt III: 2 (Prismara = Stufe 9, Aerion = Stufe 10) | LOCKED |
| Wild-Level-Korridore | Prolog 2–5 · Akt I 5–28 · Akt II 25–55 · Akt III 50–70 · Endgame 70–100 | LOCKED |
| Zonen-Skalierung | Frei wählbare Regionen: Stufe nach Akkordanzahl, beim ersten Betreten **einmalig fixiert** | LOCKED |
| Story-Finale | Spieler-Echos ~Lv. 68–70, Wärterrang ~28 | PROVISIONAL → K63 |
| Chorgröße | Rang 1: 2 · Rang 2: 3 · Rang 5: 4 · Rang 10: 5 · Rang 14: 6 | PROVISIONAL → K43 |
| Freischaltungen | Duo ab Rang 5, Trio ab 10, Zucht ab 14 (Ende Akt I), Raid ab 22, Ranked ab 28 | PROVISIONAL → K43 |
| Traversal-Reihenfolge | Gleiter (Prolog) → Bodenreiten (nach Akkord 1) → Schwimm-/Kletterreiten (Akt I) → Grabreiten (Akt II, Sahrun) → Flugreiten (Akt II, nach 6 Akkorden) | LOCKED |

## §16 Schwierigkeit & Fehlerzustand (K02 §11)

| Schlüssel | Wert | Status |
|---|---|---|
| Grade | Entspannt (EP 1,25×) · Wärter (Standard) · Meister · Modifikator Eiserner Wärter | LOCKED |
| Rückklang | Teleport zum nächsten aktivierten Resonanzstein/Klangbrunnen, Heilung, **kein** Bindungsverlust; Boss → Retry vor Arena | LOCKED |
| Strafe | Nur Meister: −10 % Sol, max. 5.000 ◎ | LOCKED |
| Eiserner Wärter | Erschöpfte Echos für laufende Region gesperrt | LOCKED |
| Zugänglichkeit | Jede Frequenz-Mechanik hat visuelles Wellenmuster (DR-24) | LOCKED |
