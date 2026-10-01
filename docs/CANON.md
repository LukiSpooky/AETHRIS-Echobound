# CANON – Single Source of Truth

**Projekt:** AETHRIS: Echobound · **Pflege:** Creative Director (Inhalt), QA Lead (Konsistenzprüfung) · **Letztes Update:** K17

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
| ADR-046 | Umweltbelastung ohne Tod, mit automatischem Rückzug | K09 |
| ADR-047 | Typverteilung pro Region als bindende Datenvorgabe | K09 |
| ADR-048 | Umgekehrte Tagesrhythmen als Biom-Identität (Sahrun, Morvenmoor) | K09 |
| ADR-049 | Ressourcen-Stufen spiegeln Akt-Progression | K09 |
| ADR-050 | Unterwasser ohne Ertrinken, nur mit Schwimm-Echo (Atemkugel) | K10 |
| ADR-051 | Resonanzsprung statt Fallschaden | K10 |
| ADR-052 | Lichtwert ohne GPU-Readback (Lichtproben-Gitter) | K10 |
| ADR-053 | Regionale Tageslängen: Hvitfell +2 h Nacht, Nimbara +2 h Tag | K10 |
| ADR-054 | Arena-Stufe beim ersten Betreten der Arena fixiert | K11 |
| ADR-055 | Arena-Feldregeln als Kampfsystem-Lektionen | K11 |
| ADR-056 | Lore-Einwohner ≠ dargestellte NPCs (Mass Crowds) | K11 |
| ADR-057 | Umgekehrte Stadtzeiten (Morvenfurt, Qasr Sahrun) | K11 |
| ADR-058 | Aerion isoliert; Wendelin Aar 880 n.St. einzige Verbindung (10. Arena) | K12 |
| ADR-059 | Schweigegelübde als Präsentationsform (Tafel-/Gestendialoge) | K12 |
| ADR-060 | Weltlied-Fragmente in allen Stadtthemen | K12 |
| ADR-061 | Energiekrise als Weltzustand ab Akt II | K12 |
| ADR-062 | Siedlungen algorithmisch vorplatziert (Farthest-Point, ≥ 400 m, LD-Toleranz 300 m) | K13 |
| ADR-063 | Siedlungszustände Bedroht/Stabil/Blühend ohne Rückfall | K13 |
| ADR-064 | Wanderdorf Ashurim mit mitreisendem Resonanzstein | K13 |
| ADR-065 | Aufträge ohne Exklusivbelohnungen (DR-31) | K13 |
| ADR-066 | Deterministischer Wetterfahrplan statt replizierten Zufallswetters | K14 |
| ADR-067 | Kalibrierte Auswahlgewichte als generierte Daten | K14 |
| ADR-068 | Wetter-Typresonanz moderat (0,8–1,3), Ranked neutral | K14 |
| ADR-069 | Resonanzsturm offline per Sturmstimmgabel | K14 |
| ADR-070 | Switch 2: TOD-Irradiance-Blending statt Lumen | K15 |
| ADR-071 | Eine globale Spieluhr, regionale Sonnenkurven | K15 |
| ADR-072 | Mondzyklus 16 Spieltage (8 Phasen × 2) | K15 |
| ADR-073 | 7-Tage-Woche mit Stilltag | K15 |
| ADR-074 | 18 Archetypen als Rig-/Animationsgrundlage | K16 |
| ADR-075 | Kreaturenkatalog aus Daten generiert und validiert (`tools/gen_catalog.py`) | K16 |
| ADR-076 | Klangmal als universelles Gestaltungselement | K16 |
| ADR-077 | Nicht gewählte Starter solo erhältlich (Uralthain nach Akt I + Zucht) | K16 |
| ADR-078 | Präzision/Ausweichen als Sekundärwerte außerhalb der Kernsumme | K16 |
| ADR-079 | Effektivitätsstufen 1,6 / 1,0 / 0,625 / 0,4 (keine Immunität) | K17 |
| ADR-080 | Typtabelle als generierte Daten mit Balance-Bericht | K17 |
| ADR-081 | Gift schlägt Metall (Korrosion) | K17 |
| ADR-082 | Licht und Leere gegenseitig sehr effektiv | K17 |
| ADR-083 | Effektivitätsvorschau ab Kodex-Stufe 2 (Entspannt immer) | K17 |

## §11 Change Requests

| CR | Datum | Betrifft | Änderung | Begründung | Genehmigt |
|---|---|---|---|---|---|
| CR-001 | K14 | §17 „Zeit vorspulen … Wetter wird neu gewürfelt“ | Präzisiert: Zeit vorspulen springt im **deterministischen Wetterfahrplan** (§61) in einen späteren Block – neues Wetter, aber reproduzierbar; Laden eines Saves ändert das Wetter nicht | Determinismus, Koop-Synchronität, kein Save-Scumming (ADR-066) | Game Director, Tech Director |

## §12 Offene Punkte (PROVISIONAL-Tracker)

| # | Punkt | Ziel-Kapitel |
|---|---|---|
| Q1 | Zeitleisten-Formel, Tick-Größe | K31 |
| Q2 | ~~Effektivitätsmultiplikatoren~~ ✅ K17 §2 | K17 |
| Q3 | Genom: Allelanzahl, Morph-Wahrscheinlichkeiten | K38 |
| Q4 | Koop: geteilter Story-Fortschritt? | K60 |
| Q5 | Ranked-Level-Normalisierung | K61 |
| Q6 | Split-Screen-Koop Machbarkeit | K65 |
| Q7 | ~~Namen der 10 Ursprungsstimmen~~ ✅ K07: 10 Ursprungsstimmen benannt | K07/K27 |
| Q8 | Bindungsstufen 0–1000 | K37 |
| Q9 | ~~Tagesphasen-Stundengrenzen~~ ✅ K14 §3 | K15 |
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
| DR-30 | ≤ 800 m Hauptpfad zwischen zwei Klangbrunnen | S1 |
| DR-31 | Aufträge nie einzige Quelle einer Belohnung | quer |
| DR-32 | Jede Region in jeder Tagesphase ≥ 1 exklusive Aktivität | S1 |

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
- **Zeit vorspulen:** Gasthaus/Zelt/Lager auf Morgendämmerung, Mittag, Abenddämmerung, Mitternacht; Wetter folgt dem Fahrplan (CR-001).

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

- Kanäle: `Event.GameFlow.StateChanged`, `Event.Combat.Started|Ended`, `Event.Echo.Bonded|LevelUp|Evolved`, `Event.World.WeatherChanged|TimeOfDayChanged|Zone.BandFixed`, `Event.Quest.StepCompleted`, `Event.Save.Requested`, `Event.World.SettlementStateChanged` (K13) (+ Erweiterungen der Fachkapitel). Nachrichtentypen liegen in `AethrisCore/Public/Events/Messages/`.
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
| Q15 | ~~Mondphasen (für seltene Spawns, z. B. Neumond in Sahrun)~~ ✅ K15 §3.2 | K15 |
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

## §44 Biom-Template & Umweltbelastung (LOCKED, K09 §1–§2)

- Biom-Template (Steckbrief, Fantasie, Visuell, Wahrzeichen, Wetter/Tageszeit, Belastung, Ökologie, Ressourcen, Kultur, Quests, Stillezone, Tech-Art/Audio) gilt für alle 10 Regionen.
- Umweltbelastung `Exposure.Heat|Cold|Miasma|Ash|Silence`, Wert 0–100; Raten Schwach 0,5 · Mittel 1 · Stark 2 · Extrem 4 pro s; Stufen ≥ 50 Ausdauer-Regen −40 %, ≥ 80 kein Sprint/Klettern −30 %, 100 → automatischer **Rückzug** zum nächsten Rastpunkt (kein Tod); Schutzzonen −20/s.
- Schutz: Kleidung ≤ 60 % · Nahrung/Trank ≤ 30 % · Echo-Aura ≤ 25 % · Skilltree ≤ 20 % (Summe ≤ 100 %). Meister: Rückzug −5 % Sol (max. 2.000 ◎).
- Echo-Auren (Begleiterslot): Glut→Kälte 25 · Frost→Hitze 25 · Blüte/Licht→Dunst 20 · Stein→Asche 15 · Klang→Stille 25 (%). Echos erleiden außerhalb des Kampfes keine Belastung.

## §45 Regionsdaten (LOCKED, K09 §3 · `Data/World/RegionTypeDistribution.csv`, `RegionWeather.csv`, `Data/Items/Resources.csv`)

- Primärtyp-Verteilung der Erstvorkommen je Region ist **bindend** für K20–K27 (Summen: Glut 13, Flut 16, Stein 25, Sturm 24, Blüte 13, Frost 12, Leere 12, Licht 18, Gift 13, Metall 15, Geist 16, Kristall 15, Klang 17, Schwerkraft 16, Arkan 15 = 240).
- Wetter je Region (Summe 100 %), Aurora nur nachts, Resonanzsturm nur global; R09 Höhlenklima 100 % Klar; Kraterrand nutzt R08.
- 48 Ressourcen (Holz 10, Erz 12, Kristall 11, Kraut 15), Stufen I–II Akt I, III–IV Akt II, V Akt III (ADR-049).
- Prüfung: `tools/data_lint.py`.

## §46 Biome R01–R05 (LOCKED, K09 §4–§8)

| Region | Wahrzeichen | Besonderheit | Belastung | Nebenq. |
|---|---|---|---|---|
| R01 Verdanthain | Wurzelhain Eichenhall, Ruinenturm Lindwald, Farnschlucht, Uralthain, Linnbrücke | Glockenblüten tönen im Wind | keine (Prolog-Stille) | 24 |
| R02 Kharsgrat | Grollhorn, Kharsholm (Kettenbrücken), Schwebende Ahnenfelsen, Erzgrat-Minen, Linn-Quelle | Schichtbetrieb (NPCs auch nachts), Schwerkraft-Anomalien | Kälte Z04/Z05 | 22 |
| R03 Morvenmoor | Morvenfurt, Versunkener Turm, Nebelwald Corrach, Riesen-Seerosen, Morve-Delta | Nachtmärkte; Regen hebt Wasserstand +0,4 m | Dunst Z03/Z05 | 21 |
| R04 Sahrun-Weite | Sonnenhof-Plateau, Glasebene, Singende Dünen, Harrâd-Oase, Wanderdorf | nachtaktiv; Sandsturm-Navigation per Resonanzsinn; Sensitivity-Review | Hitze Tag / Kälte Nacht | 22 |
| R05 Ignareth | Ignar-Krater, Schlackenwehr, Obsidianklamm, Vorthax-Schlackenstrom, Schmiedeterrassen | Ausbruch alle 3 Spieltage (Lava-Layer A/B); 6 Schmiedeglocken/Tag | Hitze, Asche | 19 |

Story-Platzierung: W2 (Stillsteine) in der ersten betretenen freien Akt-I-Region; Tavesh-Erstkontakt in Morvenmoor bzw. erster Akt-I-Region; Sereth-Erstauftritt in erster Akt-II-Region; Venn-Grabung am Sonnenhof (Akt II).
Tech-Art: PCG `PCG_R##_<Layer>` (Canopy, Understory, Ground, Rocks, Water, Props, Hazards), Editorzeit-gebacken; Foliage-Budget PS5 ≤ 1,6 Mio. Nanite-Instanzen / 250 k Gras, Switch 2 ≤ 400 k / 60 k; Stille über `MPC_Silence`.

## §47 Siedlungsnamen R01–R05 (LOCKED, K09)

| Region | Dörfer | Außenposten |
|---|---|---|
| R01 | Lindwiesen, Moosgrund | Farnwacht, Linnfurt-Posten, Uralthain-Lager |
| R02 | Brakkfels, Hrallsted | Passwacht Nord, Erzgrat-Hütte, Grollhorn-Biwak |
| R03 | Fennhaven, Duvreth | Corrach-Stelzenposten, Riedwacht, Senkenlager |
| R04 | Harrâd, Mirsaan, Wanderdorf Ashurim | Glasebene-Turm, Dünenwacht, Plateau-Lager |
| R05 | Vorthax, Kaldra | Aschehütte, Obsidianwacht, Kraterrand-Posten |

## §48 Biome R06–R10 (LOCKED, K10 §2–§6)

| Region | Wahrzeichen | Besonderheit | Belastung | Nebenq. |
|---|---|---|---|---|
| R06 Saltrand | Saltrand-Hafen, Leuchtfelsen (180 m), Treibdorf Flottholm, Riffgrund, Felsbogen „Thal'assyrs Rippe“ | **Gezeiten**: 12-Spielstunden-Zyklus, ±1,2 m, Ebbe < −60 cm öffnet Pfade; Flottholm 2 Positionen; Unterwasser | keine (Böen an Klippen) | 23 |
| R07 Hvitfell | Isvaldtind, Hvitmark, Kloster Schweigfels, Eiðvik-Ruinen, Gletscherdom | **Erinnerungseis** (Lore-Medium), Nacht +2 h, Aurora | Kälte mittel–extrem | 20 |
| R08 Ael'Dorun | Thronstadt/Archontenkuppel, Säulenfeld Thae'Luun, Dorunsruh, Resonanzturm-Stumpf, **Treppe der Zehn** (Ilen gesichtslos) | 12 Geisterszenen bei Nebel; Glyphen (`MPC_Glyphs`); Metall-Echos sind keine Roboter; W6/W7 | Stille | 21 |
| R09 Prismtiefen | Kraterrand + Liftstation (ab Akt I), Prismara (Geodenkaverne), Kristallsee, Missklang-Adern, Tiefe Resonanz | Höhlen Akt III; Kristallpuls alle 6 Spielstunden; Lichtbrechungsrätsel; blinde Klang-Jäger | Dunkelheit, Dunst | 18 |
| R10 Nimbara | Aerion (1.800 m, ~800 Einw.), Sternenarena (2.600 m, Finale), Kronenwerft, Lumeya-Inseln, Wolkenfälle | Tag +2 h; Aufwinde/Windströme; Inselendemiten; nach „Sanfte Stille“ Inseln niedriger, Inhalte gleich | Kälte | 20 |

## §49 Siedlungsnamen R06–R10 (LOCKED, K10)

| Region | Dörfer | Außenposten |
|---|---|---|
| R06 | Tangwerft, Möwenhuk, Treibdorf Flottholm | Leuchtfelsen-Wacht, Dünenkate, Riffposten |
| R07 | Fjallstad, Eiðvik-Neu | Gletscherwacht, Passhütte, Isvaldtind-Biwak (+ Sonderort Kloster Schweigfels) |
| R08 | Thae'Luun, Säulenrast | Grabungslager Nord, Archontenwacht, Ruinenpfad-Posten |
| R09 | Glanzschacht, Quarzgrund | Liftstation Kraterrand, Kristallsee-Lager, Missklang-Wacht |
| R10 | Lumeya, Wolkenrast | Kronenwerft-Wacht, Sternwarte Oruma, Windanker |

Damit sind alle 22 Dörfer und 30 Außenposten benannt (§47 + §49).

## §50 Sondermechaniken (LOCKED, K10 §1)

- **Unterwasser:** Tauchen nur mit Schwimmreiten (Atemkugel); Oberflächenschwimmen Ausdauer −6/s, bei 0 Treiben ans Ufer; kein Ertrinken.
- **Dunkelheit:** Lichtwert 0–100 (Lichtproben-Gitter 2 m + Gameplay-Lichtquellen); < 15 eingeschränkte Sicht; Lichtquellen: Laterne, Kristall-Leuchten, Licht/Glut-Begleiter (8 m).
- **Fallrettung:** Fall > 30 m → Auto-Gleiter (Option, Standard an); Fall ins Nichts > 2 s → Resonanzsprung zum letzten sicheren Boden, keine Strafe.
- **Aufwinde** 6 m/s, **Windströme** 18 m/s; Gewitter: Aufwind +50 %, Flugsteuerung −20 %, Blitzwarnung 1,5 s.

## §51 Stadt-Template & Arena-System (LOCKED, K11 §1–§2 · `Data/World/Arenas.csv`)

- Stadt-Template: Steckbrief · Geschichte · Architektur & Layout · Dienste · Händler · Arena · Quests · Musik · Einwohner/Tagesabläufe/Feste.
- Arena: Vorprüfung (2–3 Arena-Wärter, nach einmaligem Sieg überspringbar) + Meister. Stufe beim ersten Betreten **der Arena** fixiert (ADR-054): ARN_01 fest 1, ARN_09 fest 9, ARN_10 fest 10; Akt I = Clamp(Akkorde+1, 2, 4), Akt II = Clamp(Akkorde+1, 5, 8). Belohnung: Akkord + Klangschrift (Spezialtyp) + Sol + Wärter-EP. Niederlage → Rückklang vor die Arena. Post-Game-Meisterrunde Lv. 75–85. Meister öffnet danach die Schlafstätte.

| ID | Stadt | Meister | Typ | Feldregel (Tag) |
|---|---|---|---|---|
| ARN_01 | Eichenhall | Maelis Wendt | Blüte | Überwuchs (`Arena.Rule.Overgrowth`) |
| ARN_02 | Kharsholm | Torvik Hrall | Stein/Schwerkraft | Wandernde Plattformen (`ShiftingPlatforms`) – Reihentausch alle 4 Züge |
| ARN_03 | Morvenfurt | Evhe Corrach | Gift/Geist | Moornebel (`Mist`) – AUS +1, Hinterreihe nur per Bereich; nur nachts |
| ARN_04 | Qasr Sahrun | Shirah Harrâd | Licht | Sonnenspiegel (`SunMirrors`) – Licht trifft 2. Ziel 60 %; nur nachts (Mondspiegel 50 %) |
| ARN_05 | Schlackenwehr | Kaldrex Vorn | Glut/Metall | Schmiedeglut (`ForgeHeat`) – Glutboden, 3 % Max-HP/Zug Vorderreihe |
| ARN_06 | Saltrand-Hafen | Beke Tamsen | Flut/Sturm | Gezeitenbecken (`Tide`) – Ebbe/Flut alle 3 Züge |
| ARN_07 | Hvitmark | Sigrun Fjall | Frost | Spiegeleis (`Ice`) – Wechsel −50 % Zeit, Rückstoß ×2 |
| ARN_08 | Dorunsruh | Aevrin Thal | Arkan | Glyphenfeld (`Glyphs`) – Typtabelle alle 5 Züge für 1 Zug umgekehrt |
| ARN_09 | Prismara | Ilyx Brannoc | Kristall | Lichtbrechung (`Refraction`) – 25 % Brechung auf anderes Ziel |
| ARN_10 | Aerion | Oruma Siyel | Klang/Licht | Sternenfall (`Starfall`) – alle 4 Züge, Treffer + Harmonie +15 |

## §52 Städte I (LOCKED, K11 §4–§8)

| Stadt | Einw. | Regierung | Fraktionen | Fest (Spieltag-Rhythmus) |
|---|---|---|---|---|
| Eichenhall | 9.000 | Stadtrat (7) + Bundesrat (Lindentisch) | Wildwacht-HQ, Akademie-Außenstelle, Kontor | Lindenfest (jeder 7.) |
| Kharsholm | 6.500 | Klanrat (Brakk, Hrall, Torv) | Wildwacht, Kontor | Schwurnacht (jeder 10.) |
| Morvenfurt | 5.000 (+600 Unterstadt) | Zunft der Fährleute (Fährmeisterin Ailsa Duvreth) | Freie Stimmen (Unterstadt), Kontor, Orden-Kapelle | Laternennacht (jeder 5.) |
| Qasr Sahrun | 7.500 | Rat der Sonnenhöfe | Kontor, Akademie-Grabung (Akt II), Freie-Stimmen-Zelle | Nacht der Gäste (jeder 9.) |
| Saltrand-Hafen | 11.000 | Hafenrat (kontorgeprägt) | Goldklang-HQ, Wildwacht-Hafenwache, Freie-Stimmen-Zelle | Glockenflut (jeder 6., Springflut) |

Wahrzeichen/Arenen: Wurzelarena unter der Riesenlinde · Schlundring über dem Grollschlund · Turmspitzen-Arena auf dem Versunkenen Turm · Sonnenhof-Arena auf dem Plateau (Treppe der tausend Stufen) · Gezeitenbecken-Arena mit Schleusen (goldene Glocke läutet bei Flut). Neue NPCs: Rätin Elsbeth Moor (Eichenhall), Fährmeisterin Ailsa Duvreth, Händler gemäß `Data/Economy/Merchants.csv`.

## §53 Bevölkerungsdarstellung (LOCKED, K11 §3 · `Data/World/Settlements.csv`)

- Budgets (benannt / Mass / sichtbar PS5 / Switch 2): Eichenhall 48/220/140/70 · Kharsholm 40/180/120/60 · Morvenfurt 42/160/110/55 · Qasr Sahrun 44/200/130/65 · Saltrand-Hafen 52/260/160/80. Mass-NPCs werden < 25 m zu leichten Actors.
- Tagesablauf-Muster: **Tagwerk**, **Schicht A/B/C** (6/14/22 Uhr), **Nachtvolk**, **Wache**, **Gelehrt**.
- `Settlements.csv`: 62 Siedlungen (10 City, 22 Village, 30 Outpost), IDs `SET_C|V|O_<NAME>`.

## §54 Städte II (LOCKED, K12 §1–§5)

| Stadt | Einw. | Regierung | Arena (Meister, Stufe) | Fest | Story-Rolle |
|---|---|---|---|---|---|
| Schlackenwehr | 5.500 | Zunftrat der Schmiede | Große Esse – Kaldrex Vorn, 5–8 (Schmiedeprobe vorab, +1 VER-Stufe 3 Züge, optional) | Glockenguss (jeder 12.) | Kraterherz erkaltet; Zunft-Gelübde gegen Waffen (seit Siegelkriegen) |
| Hvitmark | 4.200 | Thing (alle 10 Spieltage), Sprecherin Astrid Eiðsen | Spiegelsee – Sigrun Fjall, 5–8 | Tag der Stimmen (jährlich, Echtzeit, Schweigeminute) | Klangpest-Mahnmal; Tor zum Kloster |
| Dorunsruh | 6.000 (~1.400 Akademie) | Stadtkuratorium (Venn mit Sitz) | Glyphenhof – Aevrin Thal, 5–8 | Tag des Kodex (jeder 15.) | Rektorat Venn (vor W6 begegenbar, Gelehrt-Muster), W6/W7; Aevrin öffnet nach W6 Venns Aufzeichnungen; Kael bis W6 im Labor |
| Prismara | 3.800 | Stimmergilde (Seren Quarz) | Prismenhalle – Ilyx Brannoc, fest 9 | Kristallpuls-Nacht | Lift ab Akt I außer Betrieb; Energiekrise ab Akt II (`DL_Story_EnergyCrisis`, Lichter flackern weltweit); Ilyx hört schwach Grundfrequenzen |
| Aerion | ~800 | Rat der Baumeister (Hüterin Oruma Siyel) | Sternenarena – Oruma Siyel, fest 10 (= Finalschauplatz) | Sternenlesen (Neumond) | Isoliert seit der Stille; Wand der Zehn (Ilens Gesicht erhalten); erloschener Resonanzstein → Nebenquest verbindet mit Eichenhall |

Händler gesamt: 54 (`Data/Economy/Merchants.csv`).

## §55 Kloster Schweigfels (LOCKED, K12 §6)

R07 am Pass (≈ 3,3/1,1 km), Ordenssitz, ~120 Mitglieder, Schweigegelübde (Dialoge als Schiefertafel/Geste, ≤ 80 Zeichen), keine Musik/Glocken (nur Raumklang; ein tiefer Ton bei Sereths Auftritt), verhüllter (funktionierender) Klangbrunnen, Stillstein-Werkstatt, verstummte Echos schlafend in Ruhezellen, nur Ordensladen (Ruf F05).

## §56 Städte gesamt & Musik-Leitmotiv (LOCKED, K12 §7–§8)

- Gesamtbevölkerung der 10 Städte ≈ 59.300.
- **Weltlied-Leitmotiv** (7 Töne, Komposition K55 vor den Stadtthemen): Eichenhall Töne 1–2 · Kharsholm 2–3 · Morvenfurt 3–4 · Saltrand 4–5 · Qasr Sahrun 5–6 · Schlackenwehr 6–7 · Hvitmark Umkehrung · Dorunsruh Krebs, fragmentiert · Prismara arpeggiert 1/3/5/7 · Aerion vollständig; Finale verschmilzt alle Fragmente.
- Dialog-Präsentation `EDialoguePresentation` {Voiced, Barked, SlateWritten, Gesture}, `FDialogueLineSpec`.

## §57 Dörfer (LOCKED, K13 §2 · Koordinaten `Data/World/Settlements.csv`)

| Region | Dorf (Einw.) – Schlüssel-NPC – Haken |
|---|---|
| R01 | **Lindwiesen** (240, Start; Ysolde, Bäckerin Hedda, Müller Jost) · **Moosgrund** (310; Köhlerin Brida; Pilzringe) |
| R02 | **Brakkfels** (420; Ulf Brakk; Lorenlauf/Minenunglück) · **Hrallsted** (280; Hirtin Svala; verlorene Herde) |
| R03 | **Fennhaven** (190; Lorcan; Reusen-Mysterium) · **Duvreth** (230, halb evakuiert; Moorweise Ama Duvreth; Rückkehr nach Heilung) |
| R04 | **Harrâd** (520; Brunnenwächterin Nadira) · **Mirsaan** (260; Dünenbauer Kesh) · **Wanderdorf Ashurim** (150; Imran; Route A 6,3/5,9 → B 3,5/5,5 → C 2,6/5,8 → D 4,7/6,0, je ~18 Spielstunden, Stein reist mit) |
| R05 | **Vorthax** (330; Thessa; Ausbruchstag) · **Kaldra** (210; Kurwirtin Malva; Klangpest-Kurgäste) |
| R06 | **Tangwerft** (360; Marlene) · **Möwenhuk** (180; Okko) · **Treibdorf Flottholm** (140; Ebba; Ebbe 1,3/4,9 – Flut 1,1/4,6) |
| R07 | **Fjallstad** (250; Leif; Schwester im Kloster) · **Eiðvik-Neu** (160; Halla, Klangpest-Überlebende) |
| R08 | **Thae'Luun** (300; Dr. Imke Vael) · **Säulenrast** (140; Bruder Odvar – spricht außerhalb des Klosters) |
| R09 | **Glanzschacht** (380, −120 m; Steiger Brannoc d. Ä.) · **Quarzgrund** (120, −310 m; Schleiferin Nyx; Dunkelheit) |
| R10 | **Lumeya** (90, 1.650 m; Elun) · **Wolkenrast** (110, 1.500 m; Windseglerin Ria) |

Σ ≈ 5.560 Einwohner. Dienste-Standard: Klangbrunnen, Stein, 1–3 Händler, Questbrett, Gasthaus; teils Werkbank/Kessel/Hain-Portal.

## §58 Außenposten (LOCKED, K13 §3)

- 30 Posten, Typen: **WW** Wildwacht 9 · **AK** Akademie 8 · **GK** Kontor 4 · **ZV** zivil 9. Standarddienste: Feldbrunnen (10 s), Wildstein ≤ 150 m, Werkbank, Auftragsbrett, Zelt; Wanderhändler an 50 % (rotierend).
- Story-relevant: Dünenwacht (Sandsturm-Gate), Aschehütte (Ascheschleier-Gate), Passhütte (Schneesturm-Gate), Archontenwacht (große Stillezone), Liftstation Kraterrand (Aussicht ab Akt I, Lift ab Akt III), Kronenwerft-Wacht (Akt III), Kraterrand-Posten (kündigt Ausbrüche 1 Spieltag vorher an).
- Platzierung `tools/place_settlements.py` (Farthest-Point, Mindestabstand ≥ 0,4 km, real ≥ 0,54 km; LD darf ≤ 300 m verschieben).

## §59 Aufträge (LOCKED, K13 §4 · `Data/Quests/ContractTemplates.csv`)

- 10 Vorlagen: CT_OBSERVE, CT_PHOTO, CT_BOND, CT_GATHER, CT_DELIVER, CT_ESCORT, CT_CALM, CT_RESCUE, CT_SILENCE, CT_SURVEY (Basis-Sol 70–240, Abklingzeit 1–3 Spieltage, Fraktionsruf Akademie/Kontor/Wildwacht).
- Slots: Außenposten 1, Dorf 2, Stadt 3; Generierung bei Spieltag-Wechsel, deterministisch über Loot-Strom Fork(4); bevorzugt Arten mit niedriger Kodex-Stufe; Belohnung = BaseSol × RewardScale(Zonenband-Mitte) (K42).
- **DR-31:** Aufträge sind nie die einzige Quelle einer Belohnung.

## §60 Siedlungszustände & Ereignisse (LOCKED, K13 §5–§6)

- Zustände **Bedroht (0) / Stabil (1) / Blühend (2)**, nur aufwärts (ADR-063). Bedroht: Sortiment −40 %, nur Aufträge Stufe 0. Blühend: +1 Händler (Sonderwaren), Aufträge Stufe 2, einmaliges Dorffest, EP-Bonus. Außenposten: 5 Aufträge → Blühend.
- Data Layers `DL_SET_<Id>_State0/1/2`, Save-Fragment `Settlements`, Event `Event.World.SettlementStateChanged`, `USettlementSubsystem`.
- Ereignisse: Echo-Besuch (1 pro 2 Spieltage je Dorf), Herde am Rand, Händlerkarawane (1/Woche je Region), Wetterschaden (20 % nach Unwetter), Alpha-Bedrohung, Dorffest (einmalig), verirrter Reisender.

## §61 Wetterzustände & Planer (LOCKED, K14 §2–§5)

- Daten: `WeatherDefinitions.csv` – Dauer (Spielstunden): Klar 4–10, Regen 2–6, Gewitter 1–3, Nebel 2–5, Schnee 3–8, Hitzewelle 4–8 (nur Tag), Sandsturm 1–3, Aurora 2–4 (nur Nacht), Asche 2–6, Resonanzsturm 1–2. Sicht: Regen 350, Gewitter 250, Nebel 60, Schnee 120, Sandsturm 40, Asche 80, Resonanzsturm 200 m. Nasser Fels nicht kletterbar bei Regen/Gewitter/Schnee.
- **Fahrplan** je Region aus Weltseed Fork(1) × Region; Block = (Start, Wetter, Dauer). Auswahl ∝ Auswahlgewicht·24·2000 / (Fenster·(Min+Max)) (Ganzzahl), keine direkte Wiederholung; Überblendung 10–20 Spielminuten.
- Auswahlgewichte **kalibriert** und generiert: `WeatherSelectionWeights.csv` via `tools/sim_weather.py` (Ganzzahl-identisch zum C++-Planer; Toleranz ≤ 3 pp, erreicht ≤ 1,8 pp).
- Koop: Weltseed an Gäste, Spielzeit repliziert, Wetter lokal berechnet; nur Overrides (Story, Resonanzsturm) werden repliziert/gespeichert.
- Mikroklima `ZoneWeatherRemap.csv` (R02 Schnee nur Z04/Z05, Gipfel-Regen→Schnee; R07_Z01 Schnee→Nebel; R09 alles→Klar außer Resonanzsturm; R10_Z01 Regen→Nebel); Grenz-Überblendung 150 m.
- Klassen: `FWeatherScheduler` (rein, testbar), `UWeatherSubsystem`, `AWeatherPresentationManager`, `FWeatherOverride`; Event `Event.World.WeatherChanged` nur für Regionen mit Spieler-/Kampfpräsenz.

## §62 Wetterwirkungen (LOCKED, K14 §6–§9 · `WeatherTypeResonance.csv`, `WeatherSpawnModifiers.csv`)

| Wetter | Kampf (Fähigkeitstyp) | Sonderregel |
|---|---|---|
| Regen | Flut 1,2 · Blüte 1,1 · Glut 0,8 | – |
| Gewitter | Sturm 1,2 · Flut 1,1 · Glut 0,9 | Blitzschlag alle 4 Züge: Metall 6 % Max-HP, Sturm +10 Harmonie |
| Nebel | Geist 1,2 · Leere 1,1 · Licht 0,9 | Fernkampf auf Hinterreihe −1 PRÄ-Stufe |
| Schnee | Frost 1,2 · Blüte/Glut 0,9 | Nicht-Frost −5 % GES |
| Hitzewelle | Glut 1,2 · Licht 1,1 · Frost 0,8 · Flut 0,9 | – |
| Sandsturm | Stein 1,2 · Schwerkraft 1,1 | Nicht Stein/Metall/Schwerkraft −4 % Max-HP pro Zug |
| Aurora | Licht 1,2 · Klang 1,2 · Arkan 1,1 · Leere 0,8 | +5 Harmonie/Zug beide Seiten |
| Aschefall | Leere 1,2 · Glut 1,1 · Blüte 0,8 | −1 PRÄ-Stufe außer Glut/Leere |
| Resonanzsturm | alle 1,1 · Klang 1,3 | Harmonie ×2, Crescendo −25 % |

Grenzen 0,8–1,3; kein Typ wirkungslos; **Ranked = Klar**; Fähigkeiten können Kampfwetter lokal für N Züge ändern. Spawns: Multiplikator je Wetter × Primärtyp. NPCs: Unterstände (Regen 60 %, Gewitter 85 %), Siesta 11–16 (Hitze), Tore zu (Sandsturm), alle draußen (Aurora), Sturmpreise +10 % (Resonanzsturm). Traversal: Resonanzsinn +50 % im Nebel, Schneespuren, Sandsturm kein Klettern/Gleiten, Reiten −30 %, Blitztreffer erzwingt Landung ohne Schaden.

## §63 Resonanzsturm & Vorhersage (LOCKED, K14 §10–§11)

- Resonanzsturm: Story (W6-Wende, Finale), Post-Game-Item **Sturmstimmgabel** (Abklingzeit 3 Spieltage), LiveOps-Events; 1–2 Spielstunden, global inkl. unter Tage; Wildechos Aggression +1; Aurelune nur Nacht + Resonanzsturm; alle Echo-Rufe tonal quantisiert.
- Vorhersage: 0 Himmel lesen (10–20 Spielminuten vorher) · 1 Wetterhäuschen (nächster Block) · 2 Wetterkunde I (Karte, nächster Block aller besuchten Regionen) · 3 Wetterkunde II (2 Blöcke + seltene Bedingungen). Immer korrekt.

## §64 Tagesphasen (LOCKED, K14 §3 – löst Q9)

| Phase | Standard | Hvitfell | Nimbara |
|---|---|---|---|
| Morgendämmerung `TimeOfDay.Dawn` | 05–07 | 06–08 | 04–06 |
| Tag `TimeOfDay.Day` | 07–19 | 08–18 | 06–20 |
| Abenddämmerung `TimeOfDay.Dusk` | 19–21 | 18–20 | 20–22 |
| Nacht `TimeOfDay.Night` | 21–05 | 20–06 | 22–04 |

## §65 Spieluhr & Kalender (LOCKED, K15 §2–§3)

- `UAethrisGameClock`: `int64 GameMinute`, 3 s Echtzeit je Spielminute, Start **Tag 1, 06:30**, nur vorwärts, Host-autoritativ (Replikation 1 Hz). Zeit vorspulen auf 05/12/19/00 Uhr. Uhr-UI optional (Kompass zeigt Sonne/Mond + Phase).
- Woche = 7 Spieltage: Wurzeltag, Blatttag, Wassertag, Steintag, Windtag, Lichttag, **Stilltag** (General-Händler öffnen 2 h später). Keine Monate/Jahreszeiten.

## §66 Mondphasen (LOCKED, K15 §3.2 · `Data/World/MoonPhases.csv` – löst Q15)

Ein Mond („Lunar“, volkstümlich „der Schweigende“). 8 Phasen × 2 Spieltage = 16 Spieltage. Phasenindex = ((Spieltag − 1)/2 + 1) mod 8 (0 = Neumond); Tag 1 = Zunehmende Sichel, Vollmond Tag 7–8. Nachtlicht +0…0,25 lx; nachtaktive Spawns ×0,8 (Neumond) … ×1,2 (Vollmond).

## §67 Aktivitätsmuster (LOCKED, K15 §5 · `Data/World/ActivityCurves.csv`)

- Genau ein Muster je Art (zählt für DR-02): `Behavior.Activity.Diurnal` (Nacht 100/Dämm. 500/Tag 950 ‰), `Nocturnal` (950/500/100), `Crepuscular` (150/1000/150–400), `Cathemeral` (650 konstant), `Midday` (80/80–450/450–1000).
- Spawn-Gewicht × Aktivität (Minimum 80 ‰); < 300 ‰ → Ruhe/Schlaf an Habitaten: Wahrnehmung −50 %, Einstimmen +1 Ruhestufe, Wecken je nach Temperament.
- **DR-32:** Jede Region bietet in jeder Tagesphase ≥ 1 exklusive Aktivität.

## §68 Beleuchtung (LOCKED, K15 §6–§9 · `Data/World/TimeOfDayCurves.csv`)

- Sonne astronomisch 06:00 auf / 20:00 unter (Mitte der Dämmerungen), Max. 55° um 13:00 (Hvitfell Max. 30°, Bogen 07–19; Nimbara 05–21). Goldene Stunde = Dämmerungen.
- Nachtlesbarkeit L-N1 (Mittelgrau ≥ 18 %), L-N2 (Laternen alle 60–80 m), L-N3 (Interaktions-Emissive nachts), L-N4 (Biolumineszenz je Biom), L-N5 (mechanische Dunkelheit nur in Höhlen/Gewölben). Laternen 19:30–05:30; Fensterlicht 18–23 Uhr deterministisch je Haus-ID.
- Regionale Licht-Profile `DA_LightProfile_R##`; Modulationsreihenfolge Basiskurve → Region → Wetter → Story (`MPC_Silence`); Grenzüberblendung 300 m.
- Current-Gen: Sonne + Mond als Directional Lights, Sky Atmosphere, Volumetric Clouds, SkyLight Real-Time Capture, Lumen, VSM. **Switch 2:** TOD-Irradiance-Blending (4 Schlüsselzeiten je Region, ~45 MB, Zustandsvarianten für R05/R08), SkyLight-Capture alle 10 s, DFAO, SSGI (½), CSM 3 Kaskaden; Innenräume zusätzlich Lightmaps.

## §69 Kreaturendesign-Regeln (LOCKED, K16 §2)

CD-01 Silhouetten-Ähnlichkeit ≥ 0,80 (Formvektor, 3 Ansichten) → Redesign · CD-02 kein „Tier + Elementfarbe“, ≥ 2 Gestaltungsachsen (Ort/Klang/Leben) sichtbar · CD-03 keine Genre-Signaturen · CD-04 Palette ≤ 3 Farben + Klangmal-Akzent, Typfarben aus K56 · CD-05 Art/Typ auf 30 m erkennbar · CD-06 Typ-Leitmerkmal je Typ sichtbar · CD-07 Linien teilen Formmotiv, Stufe 3 ≥ 2× Stufe 1 · CD-08 Emotionsträger für 6 Emotionen · CD-09 Ökologie vollständig · CD-10 Bewegung folgt Körperbau (Schweben nur Schwerkraft/Geist/Leere/Sturm) · CD-11 Dichte 0,1–4 kg/dm³ (Ausnahmen Geist/Kristall/Metall/Schwerkraft/Sturm/Leere) · CD-12 Lebensraum passt · CD-13 Nische · CD-14 ≥ 3 Merkmale inkl. 1 Aktivität · CD-15 Unruhe-Profil + Vorliebe · CD-16 Kampfrolle · CD-17 Reiten ab L (Schwimmen ab M), Sitzbereich · CD-18 kein Blut/Wunden · CD-19 unheimlich ja, grausam nein · CD-20 Mix niedlich/majestätisch/fremd 40/35/25 %.

## §70 Taxonomie (LOCKED, K16 §4 · `Data/Echos/Archetypes.csv`, `BehaviorTraits.csv`)

- Archetypen A01 Vierbeiner leicht · A02 Vierbeiner schwer · A03 Huftier · A04 Zweibeiner · A05 Vogel · A06 Gleitschwimmer · A07 Schlange/Wurm · A08 Fisch · A09 Amphib · A10 Gliederfüßer · A11 Panzerträger · A12 Schwebend amorph · A13 Konstrukt/Elementar · A14 Pflanzenwesen · A15 Drache · A16 Schwarm · A17 Kopffüßer/Tentakel · A18 Kletterer/Primat; Anteil je Archetyp 2–12 %; Skelette `SKEL_Arch_*`.
- Größenklassen XS < 0,3 · S 0,3–0,8 · M 0,8–1,6 · L 1,6–3 · XL 3–8 · XXL > 8 m.
- Kategorie = „‹Bild›-Echo“. Reich *Resonantia*; Stämme Quadrupedia, Bipedia, Volantia, Serpentia, Aquatica, Articulata, Testudinia, Spectralia, Elementia, Botanica; Familien je Primärtyp: Ignidae, Undidae, Lithidae, Procellidae, Floridae, Glacidae, Vacuidae, Lucidae, Venenidae, Ferridae, Animidae, Crystallidae, Sonidae, Gravidae, Arcanidae; Gattung je Linie.
- Verhaltensvokabular: 40 `Behavior.*`-Merkmale (`BehaviorTraits.csv`).

## §71 Seltenheit & Basiswerte (LOCKED, K16 §5–§6)

- Spawngewicht Common 1000 · Uncommon 400 · Rare 120 (≥ 1 Bedingung) · VeryRare 30 (≥ 2 Bedingungen) ‰; `Spawn.None` zulässig; Zielanteile 40/28/18/8 %.
- Kernsumme (6 Werte): 3er-Linie 280–340 / 400–460 / 500–560 · 2er-Linie 320–380 / 470–530 · ohne Evolution 430–520 · Ursprungsstimmen 640–680 · Mythische 600–660. PRÄ/AUS je 80–120, Summe 190–210.

## §72 Datenschema & Katalogpipeline (LOCKED, K16 §7–§10)

- `Data/Echos/Species.csv` (Spalten: Name, KodexNumber, DisplayName, ScientificName, Category, Line, Stage, LineKind {Three, Two, Single, Branch, Legendary, Mythical}, Archetype, SizeClass, HeightM, WeightKg, PrimaryType, SecondaryType, Region, Habitat, Zones, Rarity, SpawnConditions, Activity, Traits, Niches, Role {Tank, Striker, Caster, Speed, Support, Control, AllRound}, Mount, GrowthRate, 6 Basiswerte, Precision, Evasion, EvolvesTo, EvoCondition, BondRate, BondLure, SignatureConcept, SoundMark).
- `Data/Echos/SpeciesLore.csv`: LoreOrigin, LoreBehavior, LoreMyth, LoreHumans, KodexL4 (je ≤ 320 Zeichen).
- `tools/gen_catalog.py validate|render|stats` prüft: Kodex lückenlos, Regionsbereiche, exakte Typverteilung je vollständiger Region, Kernsummen, PRÄ/AUS, Größe/Dichte, DR-02/05/15, Linien (Stufen, Gattung, Zählung 40/45/22/8), NameGuard, Archetyp-Anteile, Lore-Vollständigkeit. Kataloge K20–K27 werden generiert.
- `UEchoSpeciesDefinition` + Category, LineId, Stage, LineKind, Archetype, SizeClass, HeightM, WeightKg, Activity, Role, Mount.

## §73 Klangmal (LOCKED, K16 §3)

Jedes Echo trägt ein leuchtendes **Klangmal** (Grundfrequenz sichtbar): Timing-Signal der Bindung (hellster Puls = Einklang), Emotionsanzeige, Treffer-Flackern statt Blut, Erlöschen bei Erschöpfung/Verstummung, erblich über `GEN_SOUNDMARK_PATTERN`/`GEN_SOUNDMARK_COLOR`. Technik: Maske `T_Echo_###_SoundMark` (R Muster, G Phasen-Offset, B Intensität), Parameter `SoundMarkPulse` (BPM je Art/Stimmung).

## §74 Starter-Verfügbarkeit & #001 (LOCKED, K16 §11)

- #001 **Fernlit**: *Pteridolis cantans*, Farnkitz-Echo, L001 Stufe 1, A01, S 0,45 m 6,2 kg, Blüte, Dämmerungsaktiv, Scheu/Sänger/Familienverband, Kampf+Feld, Support, Werte 48/42/50/55/58/47 = 300, PRÄ 100, AUS 105, Wachstum Steady, → Fernwyn ab Lv. 16, Bindungsrate 45, Vorliebe Lindblüten-Honig, Klangmal Lindgold-Spirale 52 BPM.
- Nicht gewählte Starter wild im Uralthain (R01_Z06) nach Akt I (VeryRare): Fernlit Regen + Morgendämmerung, Brokk Klar + Mittag an Felsen, Wisplet Gewitter; zusätzlich Zucht.

## §75 Effektivitätsstufen (LOCKED, K17 §2 – löst Q2)

Sehr effektiv **1600** (●) · neutral **1000** (·) · resistent **625** (○) · gedämpft **400** (◌) Promille. Keine Immunität. Stärke × Resistenz = 1.

## §76 Typtabelle (LOCKED, K17 §3 · `Data/Combat/TypeChart.csv`, Quelle `tools/build_typechart.py`)

| Fähigkeitstyp | sehr effektiv gegen | resistiert von | gedämpft von |
|---|---|---|---|
| Glut | Blüte, Frost, Metall | Glut, Flut, Stein | – |
| Flut | Glut, Stein, Gift | Flut, Blüte, Frost | – |
| Stein | Glut, Sturm, Frost | Blüte, Metall, Geist, Schwerkraft | – |
| Sturm | Flut, Blüte, Klang | Sturm, Frost, Kristall | Stein |
| Blüte | Flut, Stein, Leere | Glut, Sturm, Gift | – |
| Frost | Sturm, Blüte, Gift | Glut, Frost, Metall, Klang | – |
| Leere | Licht, Klang, Arkan | Blüte, Schwerkraft | Leere |
| Licht | Leere, Gift, Geist | Licht, Metall, Kristall | – |
| Gift | Flut, Blüte, Metall | Stein, Sturm, Gift, Geist, Kristall | – |
| Metall | Stein, Frost, Kristall | Flut, Metall | – |
| Geist | Geist, Schwerkraft, Arkan | Stein, Leere, Licht | – |
| Kristall | Leere, Licht, Geist | Metall, Kristall | – |
| Klang | Stein, Metall, Kristall | Blüte, Gift, Klang, Arkan | Leere |
| Schwerkraft | Sturm, Metall, Kristall | Schwerkraft, Arkan | Geist |
| Arkan | Kristall, Schwerkraft, Arkan | Stein, Leere, Metall | – |

Balance: jeder Typ 3× sehr effektiv; Offensiv-EV 0,980 (Klang) – 1,070 (Metall/Kristall); Defensiv-EV 0,990 (Leere) – 1,070 (Arkan); Doppeltypen 0,25–2,56 (39 von 105 mit ×2,56-Schwäche). Starter-Zyklus und Rückrichtung automatisch geprüft. Licht ↔ Leere gegenseitig sehr effektiv; Gift > Metall (Korrosion).

## §77 Typregeln (LOCKED, K17 §6–§8)

- Doppeltyp-Faktor = Produkt in Promille, gerundet; mögliche Werte 2560, 1600, 1000, 640, 625, 400, 391, 250.
- **Eigenklang** (Fähigkeitstyp = eigener Typ) ×1,25, durch Boni max. ×1,4. Keine typlosen Schadensfähigkeiten.
- Tabellenumkehr (Glyphenfeld, Arkan): 1600→625, 625→1600, 400→1600, 1000 bleibt; 1 Zug, angekündigt.
- Faktor-Reihenfolge (Vorgabe K32): Basis × Eigenklang × Typfaktor × Wetter × Kritisch × Formation × Sonstige.
- Typwechsel nur durch Arkan-Fähigkeiten (2 Züge) und Evolution; Morphs nie.
- `FAethrisTypeChart` in AethrisCore (Promille-Lookup, Umkehr, Eigenklang).

## §78 Typ-Identitäten & Darstellung (LOCKED, K17 §7, §9)

- Kernmechaniken: Glut DoT/Glutboden · Flut Positionsverschiebung/Heilung über Zeit · Stein Schilde/Rückstoß-Resistenz · Sturm eigene Zeitkosten −/Mehrfachtreffer · Blüte Heilung/Überwuchs · Frost Gegner-Zeitkosten +/Präzision · Leere Entzug von Harmonie/Buffs/Schilden · Licht Enthüllen/Reinigen · Gift stapelnde Schwächung · Metall Rüstung/Konter · Geist Täuschung/Formation ignorieren · Kristall Reflexion/Laden · Klang Zeitleisten-Manipulation/Harmonie · Schwerkraft Ziehen/Stoßen/Reihentausch · Arkan Regelbruch.
- Je Typ genau eine Status-Immunität (Arbeitsnamen: Brand, Ausgetrocknet, Rückstoß, Verlangsamt, Welke, Starre, Entzug, Geblendet, Vergiftet, Erschüttert, Furcht, Gebrochen, Verstummt, Schwebend, Verflucht) – final in K32.
- Typfarben (Arbeitsstand, final K56): Glut #E8562A · Flut #2E8BC0 · Stein #8C7B65 · Sturm #7FD1E8 · Blüte #5DAA4C · Frost #BFE6F5 · Leere #2B2240 · Licht #F6D86B · Gift #8E4FB0 · Metall #9AA3AD · Geist #B7A4E0 · Kristall #E28FC6 · Klang #F2A93B · Schwerkraft #4B5BA6 · Arkan #3FB8A8; jeder Typ mit eigener Symbolform; immer Symbol + Name.
- Effektivitätsvorschau im Kampf ab Kodex-Stufe 2 der Zielart (Entspannt: immer).
