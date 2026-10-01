# CANON – Single Source of Truth

**Projekt:** AETHRIS: Echobound · **Pflege:** Creative Director (Inhalt), QA Lead (Konsistenzprüfung) · **Letztes Update:** K08

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
| ADR-016 | Kampfset 4 aktiv + 1 passiv + 1 Crescendo, Repertoire frei wechselbar | K03 |
| ADR-017 | Klangschriften wiederverwendbar, nicht handelbar | K03 |
| ADR-018 | Chor-Lernen (Reserve 50 % EP) statt EP-Teiler-Item | K03 |
| ADR-019 | Deterministischer Ungehorsam (+40 % Zeitkosten) | K03 |
| ADR-020 | Kodex-Nummerierung nach Story-Erstvorkommen | K03 |
| ADR-021 | Online-Aktionen nur mit geladenem Weltstand | K03 |
| ADR-022 | Echo-Namen global identisch (lat.), CJK transkribiert | K04 |
| ADR-023 | Deutsch = Design-Quellsprache, Englisch = Übersetzungspivot (parallel gepflegt) | K04 |
| ADR-024 | Zeitrechnung n.St., Gegenwart 1004 n.St. | K04 |
| ADR-025 | Echos grammatisch Neutrum, Zucht geschlechtsunabhängig | K04 |
| ADR-026 | Perforce für Produktion (ab P2), Git für Spezifikation | K05 |
| ADR-027 | Ein Game-Feature-Plugin pro Großfunktion, Schicht im Deskriptor | K05 |
| ADR-028 | C++20, Warnings-as-Errors | K05 |
| ADR-029 | Determinismus-Zone mit Ganzzahl/Festkomma + eigenem RNG | K05 |
| ADR-030 | Horde + BuildGraph + UGS | K05 |
| ADR-031 | Definition-Basisklassen in AethrisCore, Erweiterung per Fragmente | K05 |
| ADR-032 | GAS als Effekt-Framework, Zeitleiste als Aktivierungsinstanz | K06 |
| ADR-033 | Eigener Event-Bus (UAethrisEventBus) | K06 |
| ADR-034 | PCG32 als Projekt-RNG (FAethrisRandom) | K06 |
| ADR-035 | Fragmentierte, explizit serialisierte Saves | K06 |
| ADR-036 | CSV als Quelle der Wahrheit für Designdaten | K06 |
| ADR-037 | Nur Menschen als intelligente Spezies | K07 |
| ADR-038 | Arenen über den Schlafstätten der Ursprungsstimmen (Akkorde = Schlüssel) | K07 |
| ADR-039 | Zwei Enden + 4 Epilog-Varianten, beide mit vollem Endgame | K07 |
| ADR-040 | Keine Jahreszeiten in 1.0 | K07 |
| ADR-041 | Keine Schusswaffen, keine Verbrennungsmotoren (Klangwerk-Technik) | K07 |
| ADR-042 | Makrokarte als generierte, validierte Rasterdatei | K08 |
| ADR-043 | Welt faltet sich zur Mitte (Akt III unter/über dem Zentrum) | K08 |
| ADR-044 | Regionsweise Stufenfixierung beim ersten Betreten | K08 |
| ADR-045 | Höhen auf ~40 % skaliert | K08 |

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
| Q7 | ~~Namen der 10 Ursprungsstimmen~~ ✅ K07: 10 Ursprungsstimmen benannt | K07/K27 |
| Q8 | Bindungsstufen 0–1000 | K37 |
| Q9 | Tagesphasen-Stundengrenzen | K15 |
| Q10 | ~~Hauptquartiere der Fraktionen~~ ✅ K07: Hauptsitze festgelegt | K47 |
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
| Starterlinien | Fernlit → Fernwyn → Verdrath (Blüte) · Brokk → Brokkar → Torgrath (Stein) · Wisplet → Galewix → Zephyrion (Sturm); Kodex #001–#009 | LOCKED (Namen, K04); Zweittypen → K20 |
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

## §17 Spielstruktur & Zustände (LOCKED, K03 §1–§3)

- **Modi:** Weltspiel · Koop-Reise (2–4) · Arena-Halle (PvP) · Raid (1–4, Solo-Variante offline) · Tauschhalle · Fotomodus · Eiserner Wärter.
- **Profil** (Einstellungen, Erfolge, PvP-Rang, Gilde, Fotoalbum) vs. **Weltstand** (3 Slots + 1 Eiserner-Wärter-Slot).
- **Zustands-Tags:** `GameFlow.Boot|Title|Loading|ArenaHall`, `GameFlow.World.Explore|Combat|Bond|Sanctuary|Cinematic`, Overlays `GameFlow.Overlay.Dialogue|Menu|Photo|Map|SystemPrompt`.
- **Klassen:** `UAethrisGameFlowSubsystem` (GameInstance-Subsystem, einziger Weg für Zustandswechsel, sendet `GameFlow.StateChanged`), `UGameFlowStateDefinition` (Data Asset je Zustand).
- **Pausieren:** Solo-Menü/Dialog/Foto pausiert Weltzeit; Koop pausiert nie (60 s Schutz im Menü).
- **DR-30:** ≤ 800 m Hauptpfad zwischen zwei Klangbrunnen.
- **Zeit vorspulen:** Gasthaus/Zelt/Lager auf Morgendämmerung, Mittag, Abenddämmerung, Mitternacht; Wetter wird neu gewürfelt.

## §18 Echo-Progression & Kampfset (K03 §4–§6)

| Schlüssel | Wert | Status |
|---|---|---|
| Progressionsspuren | P1 Level · P2 Bindung · P3 Kampfset · P4 Evolution · P5 Schliff · P6 Wärterrang · P7 Skilltree · P8 Ausrüstung (Stufe I–V) · P9 Ruf · P10 Akkorde · P11 Kodex (256×4 Stufen) · P12 Hain-Ausbau | LOCKED |
| Kampfset | 4 aktiv + 1 passiv + 1 Crescendo (+ 0–1 Feldfähigkeit); alle gelernten Aktiven bleiben im **Repertoire** | LOCKED |
| Crescendo / Feld | Crescendo ab Bindungsstufe 2, Feldfähigkeit ab Bindungsstufe 1 | LOCKED |
| Passiv | 1–3 art-spezifische Optionen + 1 versteckte; Wechsel mit Item **Wandelklang** | LOCKED |
| Fähigkeitserwerb | Lernset · **Klangschriften** (90, wiederverwendbar, nicht handelbar) · Tutoren · Vererbung · Evolution | LOCKED |
| Schliff | Summe 240, max. 80 pro Wert | PROVISIONAL → K18 |
| Bindungsstufen | 6 Stufen (Grenzen → K37) | LOCKED (Anzahl) |
| Ruf | 6 Ränge pro Fraktion | LOCKED (Anzahl) |
| Gehorsam | Voll bei: selbst gebunden/gezüchtet ODER Level ≤ 20 + 8 × Akkorde ODER Bindungsstufe ≥ 3; sonst +40 % Zeitkosten | LOCKED |
| Chor-Lernen | Reserve-Echos 50 % EP (Option 100/50/0) | LOCKED |
| Echo-EP-Anteile | Kampf 70 % · Training 10 % · Entdeckung 15 % · Quests 5 % | LOCKED (Ziel) |
| Wärter-EP-Anteile | Haupt 25 · Neben 25 · Kodex 20 · Entdeckung 15 · Arenen 10 · Sonst 5 (%) | LOCKED (Ziel) |
| Hain | 10 Biom-Gärten, Kapazität 600 | PROVISIONAL → K37 |

## §19 Content-Verteilung (LOCKED, K03 §7 · Daten: `Data/World/RegionBudget.csv`)

| Region | km² | Erstvork. Arten | Dörfer | Außenp. | Nebenq. | Steine | POIs | Dungeons |
|---|---|---|---|---|---|---|---|---|
| R01 | 4,0 | 32 | 2 | 3 | 24 | 9 | 130 | 3 |
| R02 | 4,0 | 26 | 2 | 3 | 22 | 9 | 125 | 4 |
| R03 | 3,2 | 26 | 2 | 3 | 21 | 7 | 105 | 3 |
| R04 | 4,4 | 24 | 3 | 3 | 22 | 9 | 120 | 3 |
| R05 | 3,0 | 22 | 2 | 3 | 19 | 7 | 95 | 4 |
| R06 | 3,4 | 26 | 3 | 3 | 23 | 8 | 115 | 3 |
| R07 | 3,6 | 22 | 2 | 3 | 20 | 8 | 105 | 3 |
| R08 | 2,8 | 20 | 2 | 3 | 21 | 6 | 110 | 5 |
| R09 | 3,6 | 20 | 2 | 3 | 18 | 8 | 100 | 6 |
| R10 | 4,0 | 22 | 2 | 3 | 20 | 9 | 110 | 3 |
| **Σ** | **36,0** | **240** | **22** | **30** | **210** | **80** | **1.115** | **37** |

Sonderdörfer: **Wanderdorf** (R04, mobil), **Treibdorf** (R06, schwimmend). Jede Region beherbergt 45–65 auffindbare Arten. Prismtiefen-Höhlen liegen unter R02/R08 (keine Doppelzählung).

## §20 Kodex-Nummerierung (LOCKED, K03 §8)

| Kodex | Bereich | Katalog |
|---|---|---|
| #001–#032 | R01 Verdanthain (Starter #001–#009) | K20 |
| #033–#058 | R02 Kharsgrat | K21 |
| #059–#084 | R03 Morvenmoor | K21/K22 |
| #085–#110 | R06 Saltrand | K22/K23 |
| #111–#134 | R04 Sahrun-Weite | K23/K24 |
| #135–#156 | R05 Ignareth | K24 |
| #157–#178 | R07 Hvitfell | K25 |
| #179–#198 | R08 Ael'Dorun | K25/K26 |
| #199–#218 | R09 Prismtiefen | K26 |
| #219–#240 | R10 Nimbara | K27 |
| #241–#250 | 10 Ursprungsstimmen | K27 |
| #251–#256 | 6 Mythische | K27 |

Linienstruktur: 40 × 3-stufig (120) + 45 × 2-stufig (90) + 22 ohne Evolution + 8 Spezial-/Zweigformen = **240** regulär. Linien bleiben zusammenhängend nummeriert.

## §21 Glossar & verbotene Begriffe (LOCKED, K04 §2)

Vollständiges Glossar: `docs/kapitel/K04_Kanon_Glossar_Konventionen.md` §2. Ergänzte Begriffe: **Anlagen** (`Aptitude`, genetische Wertpotenziale), **Aufträge** (`Contract`, wiederholbar, nicht Teil der 210 Nebenquests), **Einklang** (perfekter Anschlag), **Einstimmen** (Beruhigungsphase), **Verstummt** (durch Stillezone erstarrtes, feindliches Echo).
Verboten im Spiel: „Monster“, Ball/Kapsel/Fangkugel/werfen (Bindung), „-dex“, „Box/PC“, „Orden“ als Abzeichen, „KP“, töten/sterben für Echos.

## §22 Namenssystem (LOCKED, K04 §3–§5)

- **Klangfamilien:** R01 Linnisch · R02 Kharsk · R03 Morvisch · R04 Sahrunisch · R05 Ignar · R06 Saltisch · R07 Hvitnisch · R08 Dorunisch (Altsprache, Apostrophe) · R09 Prismanisch · R10 Nimbari. Keine 1:1-Abbildung realer Kulturen; Sensitivity-Review für R04/R07.
- **Echo-Namen N1–N8:** 4–10 Zeichen; ASCII-Buchstaben (Apostrophe nur Ursprungsstimmen); Wurzel- + Form-Morphem; Linien teilen ein Element; kein reales Wort; erste 4 Buchstaben einzigartig **über Linien hinweg**; global identisch; ≤ 60 % Ähnlichkeit zu Fremdnamen. Prüfung: `tools/nameguard/nameguard.py` (CSV: id,name,kind,line).
- **Form-Morpheme:** Stufe 1 `-let -lit -kin -ling -i -o -ette -pip` · Stufe 2 `-ar -en -ix -ward -ow -el -una` · Stufe 3 `-ath -gor -oth -ion -rex -mire -aune -dral` · Gestalt `-wing/-wyn -paw -coil -fin -shell -hoof -mote`.
- **Wissenschaftliche Namen:** Aethrisch-Latein, *Genus epitheton* Autor, Jahr n.St. (z. B. Fernlit = *Pteridolis cantans* Vael, 812 n.St.).
- **Zeitrechnung:** n.St.; Gegenwart **1004 n.St.**

## §23 IDs, Tags, Assets (LOCKED, K04 §7–§9)

- IDs: `ECHO_###`, `ABL_A###/P###/U###/F###`, `ITM_<KAT>_<NAME>` (KAT: SEAL, HEAL, MAT, KEY, SCRIPT, GEAR, FOOD, LURE, TRAP, DECO), `RCP_…`, `R##`, `R##_Z##`, `SET_C|V|O_<NAME>`, `POI_R##_####`, `RST_R##_##`, `NPC_<NAME>`, `MQ_A#_##`, `SQ_###`, `FQ_F##_##`, `CT_R##_##`, `DLG_<Quest>_##`, `ARN_##`, `RAID_##`, `DR_##`, `GEN_<NAME>`, `STS_<NAME>`, `TER_<NAME>`. Instanzen: `FGuid`.
- IDs nie wiederverwenden → `Data/Meta/RetiredIds.csv`.
- Tag-Wurzeln: `Type. Stat. Status. Terrain. Weather. TimeOfDay. Region. Biome. Faction. Ability. Ability.Range. Formation. Combat.Format. Item. Niche. Mount. Behavior. Personality. Temperament. Feature. GameFlow. Event. Quest. Input. Cheat./Debug.`
- Weather-Tags: `Clear Rain Thunderstorm Fog Snow Heatwave Sandstorm Aurora Ashfall ResonanceStorm`; TimeOfDay: `Dawn Day Dusk Night`; Biome: `Forest Mountain Swamp Desert Volcano Coast Snow Ruins Crystal Sky`; Mount: `Ground Swim Climb Dig Fly`; Niche: `Combat Field Breeding Research Mount`.
- Asset-Präfixe: BP_, DA_, DT_, CT_/CV_, SM_, SK_, SKEL_, AS_, ABP_, AM_, M_/MI_, T_ (_D/_N/_ORM/_E/_M), NS_, MSS_, SW_, WBP_, L_/LI_, PCG_, ST_, BT_/BB_, GA_/GE_.

## §24 Stil & Lokalisierung (LOCKED, K04 §10–§11)

- Ton: warm, staunend, geheimnisvoll; Bedrohung durch Stille; ≤ 3 Zeilen / 160 Zeichen pro Textbox.
- Werte-Abkürzungen: **HP, ANG, VER, SAN, SVE, GES, PRÄ, AUS**.
- Spieler wird geduzt (Akademie-Würdenträger siezen). Ansprache wählbar: er / sie / neutral.
- Echos: grammatisch Neutrum. Typnamen als Eigennamen („Glut-Echo“). Sol: „250 ◎“.
- Sprachen: Text 12 (DE, EN, FR, ES-EU, ES-LatAm, IT, PT-BR, PL, JA, KO, ZH-Hans, ZH-Hant), Vertonung 5 (DE, EN, JA, FR, ES).
- String-Keys: `<Domäne>.<Id>.<Feld>`; Fähigkeits-/Itemnamen werden übersetzt, Echo-Namen nicht.

## §25 Engine & Repository (LOCKED, K05 §2–§3)

- UE 5.6 Source-Build, Fork `Aethris-Engine`; Engine-Änderungen nur mit `[ENGINE-MOD]` + Tech-Director-Review (Ziel < 40).
- Max. 1 Minor-Upgrade/Jahr; **Engine-Lock ab Alpha (Feb 2030)**.
- P1: dieses Git-Repo trägt Code-Gerüst/Daten/Tools. Ab P2 (Juli 2027): Perforce `//Aethris/Main` + `Dev-Combat|Echos|World|Story|Online` + `Release-1.0`; `docs/` bleibt in Git.
- Commit-Marker: `[ENGINE-MOD]`, `[DATA]`, `[SAVE-SCHEMA]`.

## §26 Module & Schichten (LOCKED, K05 §4 · Prüfer `tools/check_layers.py`)

| Schicht | Module | darf abhängen von |
|---|---|---|
| Core | AethrisCore | Engine |
| Game | AethrisGame | Core |
| Domain | GF_Monsters, GF_World, GF_Inventory | Core |
| Feature | GF_Combat, GF_Capture, GF_Companion, GF_Breeding, GF_Research, GF_Economy (inkl. Crafting), GF_Quests, GF_AI, GF_Save, GF_Multiplayer, GF_PvP | Core, Domain |
| Presentation | GF_UI, GF_Audio | Core, Domain, Feature |
| Editor | AethrisEditor | alle |

- Schicht steht im `.uplugin`-Feld `"AethrisLayer"`. Features kennen sich nie: nur **Event-Bus** (`UAethrisEventBus`), **Core-Interfaces** über `UAethrisServiceLocator`, **Domain-Daten**.
- Definition-Basisklassen in AethrisCore: `UEchoSpeciesDefinition`, `UAbilityDefinition`, `UItemDefinition`, `UQuestDefinition`; Erweiterung durch `UDefinitionFragment` (Instanced).
- Primary Asset Types: `EchoSpecies` (/GF_Monsters/Echos), `Ability` (/GF_Combat/Abilities), `Item` (/GF_Inventory/Items), `Quest` (/GF_Quests/Quests).
- Plugin-Off-Matrix nightly (außer GF_Combat, GF_Save).

## §27 Build & CI (LOCKED, K05 §6–§7)

- Targets: `Aethris` (Game, inkl. Listen-Server), `AethrisEditor`, `AethrisServer` (Linux, Dedicated).
- Horde + BuildGraph + UGS + UBA; Zen-Server-DDC.
- Pre-Submit (< 20 min): check_layers, nameguard, Data-Lint, Editor-Compile, `Aethris.Unit.*`, Data Validation.
- Continuous (2 h): alle Plattformen Development + Server + Smoke-Test (Lindwiesen-Bot, Kampf, Save/Load).
- Nightly (< 6 h): Cook, `Aethris.Functional.*`, Gauntlet-Traversal/Soak, Balancing-Simulator, Plugin-Off-Matrix, Non-Unity, Static Analysis, Pseudo-Loc.

## §28 Coding Standards & Tests (LOCKED, K05 §8–§10)

- Epic-Standard + CS-01–CS-19, CR-01–CR-03, BP-01–BP-07 (siehe K05).
- **Determinismus-Zone (CS-14):** `GF_Combat/Timeline`, `GF_Combat/Damage`, `GF_Breeding/Genetics`, Replay-Code → nur Ganzzahl / `FAethrisFixed` (Q16.16), RNG `FAethrisRandom`.
- Kein Tick per Default; keine synchronen Loads im Spielbetrieb; Instrumentierung jeder Systemfunktion.
- Kommentare Deutsch, Bezeichner Englisch; `TODO(AET-####)` Pflicht.
- Tests: `Aethris.Unit.<Plugin>.<Thema>` (Automation Spec), `Aethris.Functional.*`; Coverage Domain 80 %, Feature 60 %.
- Log-Kategorien `LogAethris<Bereich>` aus `AethrisCore/AethrisLog.h`.

## §29 Core-Framework (LOCKED, K06 · Code in `Source/AethrisCore`)

- Klassen: `UAethrisDefinition` (+ `UDefinitionFragment`), `UEchoSpeciesDefinition`, `UAbilityDefinition`, `UItemDefinition`, `UQuestDefinition`, `UAethrisEventBus`, `UAethrisServiceLocator`, `FAethrisRandom` (PCG32, Referenz `tools/ref/aethris_random.py`), `FAethrisFixed` (Q16.16, Referenz `tools/ref/aethris_fixed.py`), `TAethrisStateMachine<E>`, `UAethrisTelemetrySubsystem`, `ISaveFragmentProvider`, `FAethrisSaveHeader`.
- Echo-Daten: `FEchoStats` {HP, Attack, Defense, SpAttack, SpDefense, Speed, Precision, Evasion} (int32), `FEchoBaseStats`, `FEchoGenome` {Aptitudes, Loci[{Locus,A,B}], Morph, Mutations}, `FEchoOrigin` (Wärter, Zone, Wetter, Tageszeit, Spieltag, UTC, Methode 0 Bindung/1 Zucht/2 Geschenk/3 Event, Eltern, Signatur), `FEchoInstance` (InstanceId, Species, Nickname, Level, Experience, Bond, Personality, Temperament, Genome, Polish, CurrentHP, PersistentStatus, Repertoire, ActiveSlots ≤4, PassiveAbility, HeldItem, Origin).
- `EEchoRarity`: Common, Uncommon, Rare, VeryRare, Legendary, Mythical (ab Rare SpawnConditions Pflicht).
- Zustandsmaschinen: global `UAethrisGameFlowSubsystem` · Code-Abläufe `TAethrisStateMachine` · KI StateTree + Behavior Trees.
- GAS (in GF_Combat): `UEchoAbilitySystemComponent::ExecuteTurnAbility()` liefert Zeitkosten in Ticks; `UEchoAttributeSet` {CurrentHP, MaxHP, Attack, Defense, SpAttack, SpDefense, Speed, Precision, Evasion}; GAS-01 ganzzahlige Attribute, GAS-02 nur additive Ganzzahl-Modifikatoren oder Buff-Stufen −4…+4, GAS-03 Basiswerte nur bei Kampfbeginn, GAS-04 Rückschreiben nur CurrentHP + PersistentStatus. Keine Prediction, keine zeitbasierten Dauern.
- Seed-Hierarchie: Weltstand-Seed → Fork(1) Wetter, Fork(2) Spawn je Zone, Fork(3) Zucht, Fork(4) Loot; Kampf-Seed = Hash(Weltseed, Kampfzähler) → Fork(Teilnehmer). PvP/Raid: Server-Seed, im Replay gespeichert.
- ECS: Mass für ferne Echos (> 150 m) und Hintergrund-NPCs; Actor nah/in Interaktion.

## §30 Event-Kanäle & Services (LOCKED, K06 §4–§5)

- Kanäle: `Event.GameFlow.StateChanged`, `Event.Combat.Started|Ended`, `Event.Echo.Bonded|LevelUp|Evolved`, `Event.World.WeatherChanged|TimeOfDayChanged|Zone.BandFixed`, `Event.Quest.StepCompleted`, `Event.Save.Requested` (+ Erweiterungen der Fachkapitel). Nachrichtentypen liegen in `AethrisCore/Public/Events/Messages/`.
- Core-Interfaces: `IEchoRosterService` (GF_Monsters), `IWorldStateService` (GF_World), `IInventoryService` (GF_Inventory), `IBondingService` (GF_Capture), `ICombatService` (GF_Combat), `IKodexService` (GF_Research), `IQuestService` + `IReputationService` (GF_Quests), `IEconomyService` (GF_Economy), `ISaveService` (GF_Save). Regeln SV-01–SV-04 (Pflicht-Services: Roster, WorldState, Inventory, Save).

## §31 Datenpipeline (LOCKED, K06 §2–§3)

- `Data/**/*.csv` ist Quelle der Wahrheit → `data_lint.py` → Commandlet `AethrisCsvImport` → Definitionen (Felder im Editor gesperrt).
- CSV: erste Spalte `Id`; Fragment-Spalten `<Fragment>.<Feld>`; Listen `|`; Tags vollqualifiziert; Zahlen als Ganzzahl/Promille; Texte nur über String Tables; `#` = Kommentar.
- DD-01 Definitionen zur Laufzeit unveränderlich · DD-02 Referenzen per PrimaryAssetId/Soft · DD-03 Selbstvalidierung · DD-04 Ganzzahl/Promille.

## §32 Save-Architektur (LOCKED, K06 §10 · Detail K64)

- Datei = `FAethrisSaveHeader` (Magic 'AETH', ContainerVersion, Build, Zeit, Vorschau, CRC) + Fragment-Verzeichnis + Fragmente (je Id + Version), Oodle-komprimiert.
- SA-01 fragmentiert · SA-02 Migration pro Fragment · SA-03 fehlertolerant (Reset statt Absturz) · SA-04 unbekannte Fragmente mitschleppen · SA-05 atomar + 3 rotierende Autosaves · SA-06 explizite FArchive-Serialisierung.

## §33 Kosmologie (LOCKED, K07 §2–§4)

- Weltlied (Aethersang) = **10 Stimmen** (wo) × **15 Klangfarben** = Typen (wie) × **Pause** (Leere). Echos sind stabile Obertöne. Prinzipien: **Resonanz · Variation · Atem**.
- Seit der Großen Stille entstehen keine neuen Arten (Ausnahmen: Regionalformen, Morphs, Mutationen). Evolution = Tonartwechsel.
- Klangbrunnen (dorunisch) heilen nur Echos; Resonanzsteine teilen den Raum (nur aktivierte); Stillezonen: verstummte Echos grau, feindlich, nicht bindbar, erwachen bei Lösung; Resonanzsturm = globales Anschwellen.
- Typ-Mechanik-Identitäten (Vorgabe K17/K28): Glut DoT/Glutboden · Flut Positionsverschiebung/Heilung über Zeit · Stein Schilde/Vorderreihe · Sturm Zeitleisten-Beschleunigung/Mehrfachtreffer · Blüte Heilung/Überwuchs · Frost Verlangsamung/Präzision · Leere Entzug von Harmonie/Buffs · Licht Enthüllen/Reinigen · Gift stapelnde Schwächung · Metall Rüstung/Konter · Geist Täuschung/Formation ignorieren · Kristall Reflexion/Laden · Klang Zeitleisten-Manipulation/Harmonie · Schwerkraft Ziehen/Stoßen/Reihentausch · Arkan Regelbruch.
- Wärterlizenz (Bundesrecht seit 710 n.St.); der Spieler erhält sie im Prolog über Ysolde (Wildwacht).

## §34 Ursprungsstimmen & Mythische (LOCKED, K07 §5–§6)

| Kodex | Name | Region | Typen | Schlafort |
|---|---|---|---|---|
| #241 | Sylv'anor | R01 | Blüte/Klang | unter Arena Eichenhall |
| #242 | Orh'gruun | R02 | Stein/Schwerkraft | unter Kharsholm |
| #243 | Nhael'vesh | R03 | Gift/Geist | unter Morvenfurt |
| #244 | Thal'assyr | R06 | Flut/Sturm | Tiefseegrotte vor Saltrand-Hafen |
| #245 | Ash'kareth | R04 | Licht/Arkan | unter Qasr Sahrun |
| #246 | Pyr'thagon | R05 | Glut/Metall | Kraterherz unter Schlackenwehr |
| #247 | Isv'aldr | R07 | Frost/Licht | Gletscherdom unter Hvitmark |
| #248 | Ka'thurel | R08 | Geist/Arkan | Thronsaal-Gewölbe unter Dorunsruh |
| #249 | Prism'aion | R09 | Kristall/Klang | Resonanzkammer unter Prismara |
| #250 | Aeth'rion | R10 | Klang/Licht | Sternenarena von Aerion (Leitstimme) |

Keine Stimme trägt Leere. Bindbar nach Akkord + Regionalquest mit **Stimmsiegel** (10, nicht kaufbar); nicht Ranked-zulässig.

| Kodex | Mythisch | Typen | Zugang |
|---|---|---|---|
| #251 | Velnox | Leere/Schwerkraft | Akt-III-Finale → bindbar im Post-Game „Nachhall“ |
| #252 | Chronaire | Klang/Arkan | Zeitherausforderungen |
| #253 | Mirrowisp | Kristall/Geist | Fotografie-Meisterschaft |
| #254 | Ouroveth | Gift/Blüte | Zucht-Meisterschaft |
| #255 | Zenthrax | Schwerkraft/Metall | RAID_06 + Solo DR_08 |
| #256 | Aurelune | Licht/Leere | Resonanzsturm-Nacht (Event + storygebundener Solo-Sturm) |

## §35 Chronik (LOCKED, K07 §8)

Zeitrechnung v.St./n.St.; Gegenwart 1004 n.St. Eckdaten: Ael'Dorun ~-600 · Erstchor ~-300 · Nimbara gehoben ~-250 · Brunnen-/Steinnetz ~-200 · Resonanzkrone ab ~-120 (Archon Maedryn) · Missklang ~-20 · **Große Stille 0 (Ilen)** · Dunkle Jahre 1–300 · Brannoc (Wildwacht-Ursprung) 287 · Eichenhall 312 · Kharsholm 398 · Akademie 455 · Prismara 520 · Goldklang 610 · Siegelkriege 702–709 · **Aethrischer Bund 710** · Vael-Taxonomie 812 · **Weltakkord (Wendelin Aar) 880** · Klangpest/Eiðvik 948 · Orden der Stille 951 · Freie Stimmen 967 · Venn Rektor 981 · Ysolde Arenameisterin 989–996 · Stillezonen ab 990 · Verdanthain betroffen 1001.

## §36 Gesellschaft, Kultur, Technik (LOCKED, K07 §9–§11)

- **Aethrischer Bund**: 10 selbstverwaltete Städte, Bundesrat in Eichenhall (rotierender Vorsitz); Wildwacht = Bundesbehörde; keine Monarchien; Stadtgarden mit Echos.
- Nur Menschen als intelligente Spezies (ADR-037). Keine Schusswaffen/Motoren; **Klangwerk**-Technik mit Resonanzkristallen (ADR-041). Keine Jahreszeiten (ADR-040).
- Fraktionssitze: F01 Akademie – Dorunsruh (Rektor Aldric Venn) · F02 Goldklang – Saltrand-Hafen (Marieke Holm) · F03 Wildwacht – Eichenhall (Hralda Brakk) · F04 Freie Stimmen – Morvenfurt-Unterstadt (Tavesh Amaru) · F05 Orden – Kloster Schweigfels, Hvitfell (Sereth Vaun).
- Glauben: Lauscherglaube, Gezeitenkult, Ahnenfelsen, Sonnenhöfe, Moorweisheit, Lehre der Stille, Rationalismus – keiner wird als falsch bloßgestellt.
- Artefakte: Resonator, Siegel, Stimmsiegel, Akkord (dorunischer Schlüssel), Klangbrunnen, Resonanzsteine, **Stillsteine** (Orden), **Resonanzkrone** (10 Splitter), Klangschriften, Gleiter (nimbarisch).

## §37 Schlüsselfiguren (LOCKED, K07 §12)

Spieler (trägt Ilens **Nachklang**) · Ysolde Varn (Mentorin, kennt das Erbe) · Kael Duran (Rivale → Venns Protegé → Umkehr, stirbt nie) · **Aldric Venn** (Hauptantagonist, Motiv: Ordnung gegen Leid) · **Sereth Vaun** (Ordensoberhaupt, später Alternative „Sanfte Stille“) · Tavesh Amaru · Marieke Holm · Hralda Brakk · historisch: Ilen, Archon Maedryn, Wendelin Aar, Brannoc, Vael.

## §38 Story-Rückgrat (LOCKED, K07 §13–§14)

| Ebene | Wahrheit | Enthüllung |
|---|---|---|
| W1 | Stillezonen breiten sich aus | Prolog |
| W2 | Orden verstärkt Zonen mit Stillsteinen | Akt I Mitte |
| W3 | Ursache: Ilens Riegel um Velnox schwächelt | Akt I Ende |
| W4 | Arenen über den Stimmen, Akkorde = Schlüssel | Akt II Beginn |
| W5 | Spieler trägt Ilens Nachklang; Ysolde wusste es | Akt II Mitte |
| W6 | Verrat: Venn steuert den Orden, sammelt Kronensplitter | Akt II Wende |
| W7 | Große Stille war Ilens bewusste Tat gegen Maedryns Krone | Akt II Ende |
| W8 | Venn will Krone in Nimbara aktivieren → Riegel bricht | Akt III |
| W9 | Freies neues Lied nur durch Rückgabe des Nachklangs (Spieler verliert die Gabe) | Finale |

- Enden: **„Neues Lied“** (kanonisch) / **„Sanfte Stille“**; 4 Epilog-Varianten (Freie Stimmen, Kael, Sereth); beide → Post-Game **„Nachhall“** mit identischem Endgame.
- Lore-Kanäle: Kodex (256×3), **Klangfragmente (120)**, Wendelin-Tagebuch (20), Bücher (150), ~4.000 Barks. **L-01:** Keine Lore vor ihrer Wahrheitsebene; spätere Fragmente verzerrt bis zur Enthüllung.
- `ULoreEntryDefinition` (Primary Asset Type `Lore`, IDs `LORE_<KAT>_###`, Quelle `Data/Lore/LoreEntries.csv`, Feld TruthLevel 0–9).

## §39 Makrokarte & Koordinaten (LOCKED, K08 §2–§3, §10.1)

- Raster `Data/World/MacroMap.txt` 40 × 35 Zellen à 200 m (8 × 7 km), Himmel `MacroMap_Sky.txt`, Werte `MacroRegions.csv`, Generator `tools/gen_macromap.py` (prüft Flächen exakt + Zusammenhang). Grenzklippen 114 Zellen (nicht spielbar).
- Lage: R07 Hvitfell Norden · R02 Kharsgrat Nord-Mitte · R09 Prismtiefen-Krater West-Mitte · R08 Ael'Dorun Zentrum · R05 Ignareth Osten · R06 Saltrand Westküste · R01 Verdanthain Südwest-Mitte (Start) · R03 Morvenmoor Südost-Mitte · R04 Sahrun Süden · R10 Nimbara über dem Zentrum (1.400–2.600 m).
- UE-Koordinaten: X = (x_km − 4,0)·100.000, Y = (y_km − 3,5)·100.000 (Karten-y nach Süden), 1 m = 100 UU.

## §40 Zonen & Level (LOCKED, K08 §6 · `Data/World/Zones.csv`, `ZoneTiers.csv`)

- 50 Zonen: R01 6 (fest 2–14), R02/R03/R06 je 5 (T1–T3), R04/R05/R07 je 5 (T4–T7), R08 4 (T6–T7), R09 5 (fest 50–62), R10 5 (fest 58–70).
- Stufenbänder: T1 10–18 · T2 15–23 · T3 20–28 · T4 25–35 · T5 31–41 · T6 37–47 · T7 43–55. Stufe = Clamp(Akkorde, MinTier, MaxTier); Zonenband = [TierMin+OffMin, min(TierMax, TierMin+OffMax)].
- Erste Betretung fixiert **alle Zonen der Region** (ADR-044); Save-Fragment `World.Zones`. Alphas/Seltene +3…+8. Post-Game: Nachhall-Spawns 72–90 zusätzlich.

## §41 Siedlungsorte & Wege (LOCKED, K08 §5)

| Ort | Region | x/y km | Besonderheit |
|---|---|---|---|
| Lindwiesen | R01 | 1,9/5,7 | Startdorf |
| Eichenhall | R01 | 2,6/4,8 | Bundesrat, Wildwacht-HQ |
| Saltrand-Hafen | R06 | 0,7/3,7 | Linn-Mündung, Goldklang-HQ |
| Kharsholm | R02 | 4,2/2,2 | Felsstadt |
| Morvenfurt | R03 | 5,4/4,8 | Kanalstadt, Freie Stimmen |
| Qasr Sahrun | R04 | 4,1/5,9 | Fuß des Sonnenhof-Plateaus |
| Schlackenwehr | R05 | 6,7/3,5 | Festungsstadt an der Lavawehr |
| Hvitmark | R07 | 4,1/0,7 | Gletschertal; Kloster Schweigfels ≈ 3,3/1,1 |
| Dorunsruh | R08 | 4,8/3,3 | Akademie-HQ |
| Prismara | R09 | 2,9/3,0 | unterirdisch −180 m, Kraterlift |
| Aerion | R10 | 4,1/3,1 | Himmelsstadt 1.800 m |

Bundesstraßen: 13 Verbindungen (Wegfaktor 1,35); Weltquerung ≈ 7,3 km ≈ 29 min joggend / 9 min reitend.

## §42 Höhen, Grenzen, Gates, Steine, Metriken (LOCKED, K08 §4, §7–§9)

- Höhen (~40 % skaliert): Meer 0 · Morvenmoor 5–60 · Verdanthain 20–260 · Saltrand 0–180 · Sahrun 40–420 · Prismtiefen-Rand 150–380 (Krater −250, Höhlen −600) · Ael'Dorun 300–520 · Ignareth bis 1.150 · Kharsgrat bis 1.650 (Grollhorn) · Hvitfell bis 2.100 (Isvaldtind) · Nimbara 1.400–2.600 (Sternenarena 2.600).
- Gewässer: Linn (Kharsgrat → Verdanthain → Saltrand-Hafen), Morve (Ael'Dorun → Morvenmoor-Delta), Ignar-Lavastrom, Kristallsee (unterirdisch), Oasen (6).
- Weltgrenzen ohne unsichtbare Wände: Meeresströmung ab 400 m, Gletscherwände N, Resonanzwirbel > 2.800 m.
- Story-Gates: Sandsturm (R04), Ascheschleier (R05), Pass-Schneesturm (R07), Ruinensiegel (R08). Prolog-Grenze: Linn (eingestürzte Brücke).
- Traversal: Schwimm-/Kletter-/Grab-/Flugreiten öffnen ~6/5/5/4 % optionale Fläche; ≥ 3 Rückkehr-POIs je Region.
- Resonanzsteine: 10 Stadt + 22 Dorf + 48 Wild = 80; Hauptpfad ≤ 900 m zum nächsten Stein; kostenlos; nicht im Kampf.
- POI-Mix: Habitat 25 · Ressourcen 15 · Ruinen 12 · NPC 12 · Klangrätsel 8 · Cache 8 · Traversal 6 · Aussicht 5 · Schrein 5 · Höhle 4 (%). LD-Metriken: POI Ø 150–250 m (max 400), Straße 6 m / Pfad 2,5 m, ebene Kampffläche (r ≥ 12 m) alle 250 m, Wahrzeichen aus ≥ 2 km sichtbar, Kletterrast alle 20 m.

## §43 World Partition (LOCKED, K08 §10)

- `L_Aethris_World`; Landscape 8,1 × 7,1 km, 1 m Auflösung, −600…+2.800 m.
- Grids: MainGrid 128 m / 768 m (Switch 2: 512 m) · FarGrid 512 m / 3 km · Underground 64 m / 256 m · Sky 256 m / 2 km; 3 HLOD-Ebenen.
- Data Layers: `DL_Base`, `DL_Story_R##_Silence`, `DL_Story_R##_Healed`, `DL_Story_Gates`, `DL_Nachhall`, `DL_Event_*`, `DL_Editor_Blockout`.
- Validatoren: Regionsfläche ±3 %, POI 400 m, Brunnen 800 m, Steine 900 m, Rückkehr-POIs ≥ 3, Kampfflächen alle 250 m.
