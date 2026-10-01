# CANON – Single Source of Truth

**Projekt:** AETHRIS: Echobound · **Pflege:** Creative Director (Inhalt), QA Lead (Konsistenzprüfung) · **Letztes Update:** K35

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
| ADR-084 | Persönlichkeiten nur mit Boni, ohne Abzüge (16) | K18 |
| ADR-085 | Anlage multiplikativ (bis +15 %), Schliff additiv | K18 |
| ADR-086 | Trefferchance gedeckelt auf 50–100 % | K18 |
| ADR-087 | Bindung gibt mehr EP als Erschöpfen (×1,2) | K18 |
| ADR-088 | Evolutions-Bedingungssprache (DSL) statt fester Enums | K19 |
| ADR-089 | Keine tauschgebundenen Evolutionen | K19 |
| ADR-090 | Spieler kontrolliert jede Evolution, „Später“ kostenlos | K19 |
| ADR-091 | Evolution gibt +50 Bindung | K19 |
| ADR-092 | Spezialentwicklungen brauchen eine Weltbedingung | K19 |
| ADR-093 | Zeitkosten aus Machtbudget berechnet, nie handgesetzt | K28 |
| ADR-094 | Keine Abklingzeiten auf aktiven Fähigkeiten | K28 |
| ADR-095 | Effekt-DSL mit Primitiv-Registry | K28 |
| ADR-096 | Jeder Typ mit physischen und speziellen Fähigkeiten (12 je Typ) | K28 |
| ADR-097 | Ein Haupt-Status + Gift parallel; Starre-Immunität | K28 |
| ADR-098 | Lernsets regelbasiert und deterministisch generiert | K29 |
| ADR-099 | Zwei Abdeckungstypen je Art aus der Typtabelle | K29 |
| ADR-100 | Feldklang als exklusive Passive der Legendären/Mythischen | K29 |
| ADR-101 | Versteckte Passive aus Fremdtyp | K29 |
| ADR-102 | Tutoren lehren Schwer-Fähigkeiten gegen Fraktionsruf | K29 |
| ADR-103 | Crescendo mit Zeitkosten 200 und Ankündigung auf der Zeitleiste | K30 |
| ADR-104 | Harmoniekosten aus dem Machtbudget (60–90) | K30 |
| ADR-105 | Feldfähigkeiten statt Schlüssel-Items; Pfad-Tore mit ≥ 2 Lösungen | K30 |
| ADR-106 | Reitarten bleiben Art-Eigenschaft | K30 |
| ADR-107 | Verzögerung = ⌊Kosten × 300/(GES + 200)⌋, 100 Ticks = Standardzug | K31 |
| ADR-108 | Fremdverzögerungs-Deckel 100 Ticks (Anti-Lock) | K31 |
| ADR-109 | Priorität als Vorgriff auf der Zeitleiste | K31 |
| ADR-110 | Status-Dauern in eigenen Zügen, Feld-Dauern in Runden | K31 |
| ADR-111 | Flucht ohne Zufall über Rückzugsmarker | K31 |
| ADR-112 | Keine Schadensstreuung, exakte Vorschau | K32 |
| ADR-113 | Schadensdivisor 180 aus Simulation | K32 |
| ADR-114 | Volltreffer ×1,5 ignoriert ungünstige Stufen | K32 |
| ADR-115 | Ein Haupt-Status ohne Überschreiben | K32 |
| ADR-116 | Gegen-Terrains neutralisieren | K32 |
| ADR-117 | Zwei Reihen mit Hinterreihen-Schutz 750 ‰ und Kontaktregel | K33 |
| ADR-118 | Kombos über Typfolge und 60-Tick-Fenster | K33 |
| ADR-119 | Harmonie als gemeinsame Seitenleiste | K33 |
| ADR-120 | Chor-Akkorde als kleine Kompositions-Synergie | K33 |
| ADR-121 | Leihbegleitung bei nicht freigeschaltetem Arena-Format | K33 |
| ADR-122 | Utility-KI mit Nutzwert je Zeiteinheit | K34 |
| ADR-123 | Schwierigkeit über mehrere Hebel | K34 |
| ADR-124 | Wild-KI aus Merkmalen und Temperament | K34 |
| ADR-125 | Fairness-Regeln F-1 bis F-5 | K34 |
| ADR-126 | Adaptiver Rivale mit einer Anpassung je Begegnung | K34 |
| ADR-127 | Bosse als Basisart + Spuren + Phasen + Mechanik-Primitiva | K35 |
| ADR-128 | Weiches Anschwellen statt hartem Timer | K35 |
| ADR-129 | Raid-Belohnungen gleich für alle, kein Sperrtimer | K35 |
| ADR-130 | Instanzierte Bindung Mythischer im Raid | K35 |

## §11 Change Requests

| CR | Datum | Betrifft | Änderung | Begründung | Genehmigt |
|---|---|---|---|---|---|
| CR-001 | K14 | §17 „Zeit vorspulen … Wetter wird neu gewürfelt“ | Präzisiert: Zeit vorspulen springt im **deterministischen Wetterfahrplan** (§61) in einen späteren Block – neues Wetter, aber reproduzierbar; Laden eines Saves ändert das Wetter nicht | Determinismus, Koop-Synchronität, kein Save-Scumming (ADR-066) | Game Director, Tech Director |

## §12 Offene Punkte (PROVISIONAL-Tracker)

| # | Punkt | Ziel-Kapitel |
|---|---|---|
| Q1 | ~~Zeitleisten-Formel, Tick-Größe~~ ✅ K31 §3: Verzögerung = ⌊Kosten×300/(GES+200)⌋, 100 Ticks = Standardzug | K31 |
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
| DR-33 | Jede Evolutionsbedingung im Spiel erlernbar (Kodex 2–4, NPC, Lore) | S2 |

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

## §79 Statusformeln & Stufen (LOCKED, K18 §2–§3 · `EchoStatCalculator.h`, `tools/ref/aethris_stats.py`)

- HP = ⌊B·(L+10)·(1000+10·A)/40000⌋ + L + 12 + S
- Kernwert = ⌊⌊B·(L+10)·(1000+10·A)/55000⌋·P/1000⌋ + ⌊S/2⌋ (P = 1100 für Persönlichkeits-Wert); HP-Persönlichkeit: Ergebnis ×1,1
- PRÄ/AUS = B + ⌊A/3⌋ (+5 bei Persönlichkeit), levelunabhängig
- Stufen −4…+4 (`Data/Combat/StatStages.csv`): Kern 500/571/667/800/1000/1250/1500/1750/2000 ‰; PRÄ/AUS 700/775/850/925/1000/1075/1150/1225/1300 ‰; Reservewechsel setzt zurück.
- Treffer (‰) = clamp(Genauigkeit × PRÄ_eff / AUS_eff, 500, 1000).
- Grenzwerte: Kern max. 394, HP max. 698.

## §80 Anlagen & Schliff (LOCKED, K18 §7–§8)

- **Anlagen** 0–15 je Wert (8 Werte), +1 %/Punkt (HP/Kern) bzw. +1 je 3 (PRÄ/AUS); wild gleichverteilt, Rare/VeryRare garantieren 2/3 Werte mit 15; Anzeige 4 Klassen (schwach 0–4, solide 5–9, stark 10–13, vollendet 14–15) bzw. exakt per Skill; **Klangstimmung** (Endgame) setzt einen Wert auf 15.
- **Schliff** 0–80 je Kernwert, Σ ≤ 240; Kampf über `PolishYield` (Stat:1–3) der Gegnerart; Training 4–8 Punkte, 1 Spieltag Abklingzeit je Echo; `PolishLocks` sperren Werte; Reset über **Klangbad** (Thermen Seraphe) / Item Klangsalz.

## §81 Persönlichkeiten (LOCKED, K18 §4 · `Data/Echos/Personalities.csv`)

16: Mutig, Wild (ANG) · Standhaft, Gelassen (VER) · Klug, Träumerisch (SAN) · Sanft, Geduldig (SVE) · Flink, Rastlos (GES) · Zäh, Gutmütig (HP) · Scharfsichtig, Gewissenhaft (PRÄ +5) · Verspielt, Listig (AUS +5). Nur Boni (+10 %), keine Abzüge; je Lieblingsinteraktion (Training/Spielen/Streicheln/Loben/Füttern), Begleiter-Idle, KI-Neigung. Änderung per **Wesensklang** (Endgame-Crafting).

## §82 Temperamente (LOCKED, K18 §5 · `Data/Echos/Temperaments.csv`)

Ruhig (Fenster ×1,2, 4 Anschläge, bleibt, Flucht 15 %) · Feurig (×0,9, 2, greift an, Harmonie ×1,1 beim Angreifen, flieht nie) · Wachsam (×1,0, 2, flieht, Wahrnehmung ×1,3, Flucht 35 %) · Neugierig (×1,1, 3, nähert sich, Wahrnehmung ×0,8) · Stoisch (×1,0, 3, bleibt, Furcht halbiert, Harmonie ×0,95). Standardverteilung 30/15/20/20/15 %, sichtbar ab Kodex-Stufe 2 (Farbton der Frequenzwelle).

## §83 Wachstum & EP (LOCKED, K18 §6 · `Data/Echos/GrowthRates.csv`)

- Swift 0,6·L³ (L100 600.000) · Steady 0,8·L³ (800.000) · Late L³·(0,45+0,65·L/100) (1.100.000) · Wave L³·(0,8+0,08·sin(L/6)) (734.524); Legendäre/Mythische Late.
- EP = ⌊Ertrag × Ld × (2·Ld+10) / ((Ld+Lp+10)·6)⌋ × Quelle (Kampf 1,0 · Bindung 1,2 · Trainer 1,3) × Bonus (Reserve 0,5, Entspannt 1,25, Items ≤ 1,2). Ertrag Stufe 1 ≈ 60 · Stufe 2 ≈ 140 · Stufe 3/Einzel ≈ 210 · Legendär 320 (Tuning K63).
- `Species.csv` + Spalten `ExpYield`, `PolishYield`; `FEchoInstance` + `PolishLocks`.

## §84 Evolutionsformen (LOCKED, K19 §2–§3)

- Single 22 · Two 45 · Three 40 · **Branch 8** (alternative Endformen: gleiche Gattung und Stufe wie Standard-Endform, Kernsumme ±10, ≥ 1 Weltbedingung, Spielerwahl bei gleichzeitiger Erfüllung); Legendäre/Mythische entwickeln sich nicht.
- Auslöser-Verteilungsziel der Evolutionsschritte: reines Level 55 % · Level + Weltbedingung 18 % · Bindung 10 % · Item 10 % · Sonstige 7 %.

## §85 Bedingungssprache (LOCKED, K19 §4 · `tools/ref/evo_condition.py`)

- `expr := term {'|' term}`, `term := factor {'&' factor}`, `factor := '!' factor | '(' expr ')' | KEY OP VALUE`.
- Schlüssel: Level, BondTier (1–6), Item (`EvolutionItems.csv`), TimeOfDay (Dawn/Day/Dusk/Night), Weather (10 Namen), Zone (`Zones.csv`), Region (R01–R10), Moon (8 Phasen), Knows (`ABL_*`), ChorHas (`Type.*`), Personality, Temperament, WinsWhileHolding, StepsInRegion, `Stat:<A>` (Vergleich zweier Werte). Kategorie-Schlüssel nur `=`.
- Validierung im Katalog-Validator; Laufzeit `FEvoCondition` (flacher AST), Auswertung ereignisgetrieben (LevelUp, Wetter/Tageszeit, Bindungsstufe, Item, Zonenwechsel, Lager).

## §86 Evolutionsablauf & Übertragung (LOCKED, K19 §6–§7, §11)

- Evolutionsahnung (Klangmal pulsiert doppelt) → Dialog am sicheren Moment (Entwickeln/Später/Zweigwahl) → Sequenz 6–10 s (überspringbar). „Später“ kostenlos; Option Auto-Annahme. Welt-Bedingungen müssen beim Auslösen gelten.
- Bleibt: InstanceId, Herkunft, Name, Level, EP-Fortschritt im Level, Persönlichkeit, Temperament, Genom, Schliff, Repertoire, HeldItem, HP-Anteil. Neu: Spezies, Basiswerte, Typen, Größe. Bindung **+50**; Morph/Passive auf neue Stufe abgebildet; Evolutionsfähigkeit gelernt; Kodex der neuen Art ≥ Stufe 3.
- Keine Tauschevolutionen; Koop: Weltbedingungen des Hosts; Server prüft Linien-Erreichbarkeit.

## §87 Evolutions-Items (LOCKED, K19 §5 · `Data/Items/EvolutionItems.csv`)

15 **Obertonkristalle** `ITM_EVO_<TYP>` (Leere nur aus geheilten Stillezonen) + 10 Spezialitems an Weltereignisse gebunden: Mondtau (R04, Vollmondnacht), Aschefeder (R05), Gezeitenperle (R06, Springflut), Glyphensplitter (R08), Aurorafaden (R07, Aurora), Sternenstaub (R10), Wurzelherz (R01), Nebelschleier (R03), Glutkern (R05), Klangmuschel (R06). Verbrauch beim Auslösen.

## §88 Evolutions-Pacing (LOCKED, K19 §8)

3-stufig: Akt I 14–22 / 30–38 · Akt II 28–36 / 42–50 · Akt III 40–48 / 56–62. 2-stufig: Akt I 20–30 · Akt II 34–44 · Akt III 50–58. **Starter: Lv. 16 → Stufe 2, Lv. 34 → Stufe 3.**

## §89 Arten #001–#032 (LOCKED, K20 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 001 | Fernlit | Blüte | L001/1 Three | Fernwyn [Level>=16] | Support | – |
| 002 | Fernwyn | Blüte/Sturm | L001/2 Three | Verdrath [Level>=34] | Support | – |
| 003 | Verdrath | Blüte/Klang | L001/3 Three | – | Support | Bodenreiten |
| 004 | Brokk | Stein | L002/1 Three | Brokkar [Level>=16] | Tank | – |
| 005 | Brokkar | Stein | L002/2 Three | Torgrath [Level>=34] | Tank | – |
| 006 | Torgrath | Stein/Schwerkraft | L002/3 Three | – | Tank | Bodenreiten |
| 007 | Wisplet | Sturm | L003/1 Three | Galewix [Level>=16] | Speed | – |
| 008 | Galewix | Sturm | L003/2 Three | Zephyrion [Level>=34] | Speed | – |
| 009 | Zephyrion | Sturm/Licht | L003/3 Three | – | Speed | Flugreiten |
| 010 | Chimkin | Klang | L004/1 Three | Chimbal [Level>=18] | Control | – |
| 011 | Chimbal | Klang | L004/2 Three | Cantaroth [Level>=32 & TimeOfDay=Dusk]; Lorncant [Level>=32 & Weather=Fog & TimeOfDay=Night] | Control | – |
| 012 | Cantaroth | Klang/Blüte | L004/3 Three | – | Control | Kletterreiten |
| 013 | Lorncant | Geist/Klang | L004/3 Branch | – | Control | – |
| 014 | Mossling | Blüte | L005/1 Three | Myrthorn [Level>=18] | Tank | – |
| 015 | Myrthorn | Blüte | L005/2 Three | Vernaune [BondTier>=4]; Glyphaune [BondTier>=4 & Moon=FullMoon & Zone=R01_Z06] | Tank | Bodenreiten |
| 016 | Vernaune | Blüte/Licht | L005/3 Three | – | Tank | Bodenreiten |
| 017 | Glyphaune | Arkan/Blüte | L005/3 Branch | – | Control | Bodenreiten |
| 018 | Lumpip | Licht | L006/1 Three | Lumow [Level>=15] | Caster | – |
| 019 | Lumow | Licht/Geist | L006/2 Three | Phantalume [Level>=30 & TimeOfDay=Night] | Caster | – |
| 020 | Phantalume | Geist/Licht | L006/3 Three | – | Caster | – |
| 021 | Rillo | Flut | L007/1 Two | Rillward [Level>=22] | Caster | – |
| 022 | Rillward | Flut/Blüte | L007/2 Two | – | Caster | – |
| 023 | Sporlet | Gift | L008/1 Two | Sporix [Level>=24 & Weather=Fog] | Control | – |
| 024 | Sporix | Gift/Geist | L008/2 Two | – | Control | – |
| 025 | Skirmote | Sturm | L009/1 Two | Skirrow [Level>=22] | Speed | – |
| 026 | Skirrow | Sturm/Klang | L009/2 Two | – | Speed | – |
| 027 | Thornkin | Blüte | L010/1 Two | Thorncoil [Item=ITM_EVO_BLOOM] | Striker | – |
| 028 | Thorncoil | Blüte/Gift | L010/2 Two | – | Striker | – |
| 029 | Pebi | Stein | L011/1 Two | Orbeloth [Stat:Defense>Attack & Level>=24] | Tank | – |
| 030 | Orbeloth | Schwerkraft/Stein | L011/2 Two | – | Tank | – |
| 031 | Rivetkin | Metall | L012/1 Single | – | Tank | – |
| 032 | Cindrel | Glut | L013/1 Single | – | Caster | – |

Lockmittel-Liste `Data/Items/Lures.csv` (24 Einträge, Wirkung K36). Authoring-Werkzeuge: `tools/authoring/catalog_lib.py`, `build_catalog_chapter.py`; Linienplan `docs/kapitel/_Linienplan_K20-K27.md` (R01 6/5/2/2, R02 4/5/3/1, R03 4/5/3/1, R06 4/5/3/1, R04 4/5/2/0, R05 4/4/2/0, R07 4/4/1/1, R08 4/3/2/0, R09 3/4/2/1, R10 3/5/2/1 – 3er/2er/Einzel/Zweig).

## §90 Arten #033–#064 (LOCKED, K21 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 033 | Craglet | Stein | L014/1 Three | Cragar [Level>=18] | Tank | – |
| 034 | Cragar | Stein | L014/2 Three | Kraggoth [Level>=34]; Anchrex [Level>=34 & Zone=R02_Z02 & Moon=FullMoon] | Tank | Kletterreiten |
| 035 | Kraggoth | Stein/Metall | L014/3 Three | – | Tank | Kletterreiten |
| 036 | Anchrex | Schwerkraft/Stein | L014/3 Branch | – | Control | Kletterreiten |
| 037 | Tetri | Schwerkraft | L015/1 Three | Tetrel [Level>=20] | Control | – |
| 038 | Tetrel | Schwerkraft/Stein | L015/2 Three | Ponderath [Level>=36] | Control | – |
| 039 | Ponderath | Schwerkraft | L015/3 Three | – | Control | – |
| 040 | Ferrkin | Metall | L016/1 Three | Ferrow [Level>=20] | Striker | – |
| 041 | Ferrow | Metall/Stein | L016/2 Three | Forgoth [Level>=34] | Striker | – |
| 042 | Forgoth | Metall/Stein | L016/3 Three | – | Striker | Bodenreiten |
| 043 | Gratkin | Sturm | L017/1 Three | Gratwyn [Level>=20] | Speed | – |
| 044 | Gratwyn | Sturm | L017/2 Three | Gratrex [Level>=36 & Weather=Thunderstorm] | Speed | – |
| 045 | Gratrex | Sturm/Metall | L017/3 Three | – | Striker | Flugreiten |
| 046 | Kiesi | Stein | L018/1 Two | Kiesward [Level>=24] | AllRound | – |
| 047 | Kiesward | Stein/Klang | L018/2 Two | – | AllRound | – |
| 048 | Lithi | Stein | L019/1 Two | Lithshell [Level>=26] | Tank | – |
| 049 | Lithshell | Stein/Flut | L019/2 Two | – | Tank | Bodenreiten |
| 050 | Rimlet | Frost | L020/1 Two | Rimpaw [Level>=24 & Weather=Snow] | Speed | – |
| 051 | Rimpaw | Frost/Sturm | L020/2 Two | – | Speed | – |
| 052 | Quarling | Kristall | L021/1 Two | Quarcoil [Level>=26] | Caster | – |
| 053 | Quarcoil | Kristall/Stein | L021/2 Two | – | Caster | – |
| 054 | Emblit | Glut | L022/1 Two | Dawnix [Level>=26 & TimeOfDay=Dawn] | Caster | – |
| 055 | Dawnix | Licht/Glut | L022/2 Two | – | Caster | – |
| 056 | Memoro | Geist | L023/1 Single | – | Support | – |
| 057 | Resonix | Klang | L024/1 Single | – | Speed | – |
| 058 | Runkar | Arkan/Stein | L025/1 Single | – | Control | – |
| 059 | Mirepip | Gift | L026/1 Three | Mirel [Level>=18] | Control | – |
| 060 | Mirel | Gift/Flut | L026/2 Three | Toxmire [Level>=32] | Control | – |
| 061 | Toxmire | Gift/Flut | L026/3 Three | – | Control | – |
| 062 | Undling | Flut | L027/1 Three | Undfin [Level>=18] | Tank | – |
| 063 | Undfin | Flut | L027/2 Three | Undrath [Level>=34 & Weather=Rain] | Tank | Schwimmreiten |
| 064 | Undrath | Flut/Geist | L027/3 Three | – | Tank | Schwimmreiten |

## §91 Arten #065–#096 (LOCKED, K22 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 065 | Irrlit | Geist | L028/1 Three | Irrel [Level>=16 & TimeOfDay=Night] | Caster | – |
| 066 | Irrel | Geist/Licht | L028/2 Three | Irraune [Level>=32]; Sigilaune [Level>=32 & Zone=R03_Z05 & Moon=NewMoon] | Caster | – |
| 067 | Irraune | Geist/Licht | L028/3 Three | – | Caster | – |
| 068 | Sigilaune | Arkan/Geist | L028/3 Branch | – | Control | – |
| 069 | Blossi | Blüte | L029/1 Three | Blossar [Level>=20] | Striker | – |
| 070 | Blossar | Blüte/Gift | L029/2 Three | Blossmire [Level>=36] | Striker | – |
| 071 | Blossmire | Blüte/Gift | L029/3 Three | – | Striker | – |
| 072 | Virmote | Gift | L030/1 Two | Virwyn [Level>=24] | Speed | – |
| 073 | Virwyn | Gift/Sturm | L030/2 Two | – | Speed | – |
| 074 | Blightkin | Gift | L031/1 Two | Blightar [Level>=26] | Control | – |
| 075 | Blightar | Gift/Flut | L031/2 Two | – | Control | – |
| 076 | Brinlet | Flut | L032/1 Two | Brinshell [Level>=28] | Tank | – |
| 077 | Brinshell | Flut/Blüte | L032/2 Two | – | Tank | Bodenreiten |
| 078 | Umbrling | Leere | L033/1 Two | Umbracoil [Level>=28 & TimeOfDay=Night] | Caster | – |
| 079 | Umbracoil | Leere/Flut | L033/2 Two | – | Caster | – |
| 080 | Weidlit | Blüte | L034/1 Two | Weiduna [BondTier>=3 & TimeOfDay=Dusk] | Support | – |
| 081 | Weiduna | Geist/Blüte | L034/2 Two | – | Support | – |
| 082 | Morhaw | Sturm/Flut | L035/1 Single | – | Striker | Flugreiten |
| 083 | Humbog | Klang/Gift | L036/1 Single | – | Support | – |
| 084 | Torfgor | Stein/Blüte | L037/1 Single | – | Tank | – |
| 085 | Marlit | Flut | L038/1 Three | Marwyn [Level>=20] | Speed | – |
| 086 | Marwyn | Flut | L038/2 Three | Maraune [Level>=36 & Weather=Thunderstorm] | Speed | Schwimmreiten |
| 087 | Maraune | Flut/Sturm | L038/3 Three | – | Speed | Flugreiten |
| 088 | Tidling | Flut | L039/1 Three | Tidel [Level>=18] | Control | – |
| 089 | Tidel | Flut | L039/2 Three | Tidrex [Level>=34] | Control | Schwimmreiten |
| 090 | Tidrex | Flut/Arkan | L039/3 Three | – | Control | Schwimmreiten |
| 091 | Brikin | Sturm | L040/1 Three | Brisel [Level>=18] | Speed | – |
| 092 | Brisel | Sturm/Flut | L040/2 Three | Brision [Level>=36] | Speed | – |
| 093 | Brision | Sturm/Flut | L040/3 Three | – | Speed | Flugreiten |
| 094 | Aquapip | Flut | L041/1 Three | Aquafin [Level>=16] | Caster | – |
| 095 | Aquafin | Flut/Licht | L041/2 Three | Aquadral [Level>=32]; Mystdral [Level>=32 & Moon=NewMoon & Zone=R06_Z05] | Caster | – |
| 096 | Aquadral | Flut/Licht | L041/3 Three | – | Caster | Schwimmreiten |

## §92 Arten #097–#128 (LOCKED, K23 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 097 | Mystdral | Arkan/Flut | L041/3 Branch | – | Control | – |
| 098 | Aerlet | Sturm | L042/1 Two | Aerluna [Level>=24] | Control | – |
| 099 | Aerluna | Sturm/Licht | L042/2 Two | – | Control | – |
| 100 | Stonlet | Stein | L043/1 Two | Stonshell [Level>=26] | Tank | – |
| 101 | Stonshell | Stein/Flut | L043/2 Two | – | Tank | Bodenreiten |
| 102 | Glimkin | Licht | L044/1 Two | Glimar [Level>=22] | Support | – |
| 103 | Glimar | Licht/Flut | L044/2 Two | – | Support | – |
| 104 | Ariette | Klang | L045/1 Two | Ariuna [Level>=28 & TimeOfDay=Dusk] | Support | – |
| 105 | Ariuna | Klang/Flut | L045/2 Two | – | Support | Schwimmreiten |
| 106 | Tangi | Blüte | L046/1 Two | Tangix [Level>=24 & Weather=Rain] | Support | – |
| 107 | Tangix | Gift/Blüte | L046/2 Two | – | Control | – |
| 108 | Brassel | Metall/Flut | L047/1 Single | – | AllRound | – |
| 109 | Sheamast | Geist/Flut | L048/1 Single | – | Caster | – |
| 110 | Opalisk | Kristall/Flut | L049/1 Single | – | Tank | – |
| 111 | Solkit | Licht | L050/1 Three | Solvar [Level>=18] | Striker | – |
| 112 | Solvar | Licht | L050/2 Three | Solaryx [Level>=36] | Striker | – |
| 113 | Solaryx | Licht/Glut | L050/3 Three | – | Striker | – |
| 114 | Dunkalb | Stein | L051/1 Three | Dunhorn [Level>=20] | Tank | – |
| 115 | Dunhorn | Stein | L051/2 Three | Dunmarsch [Level>=38 & Zone=R04_Z04] | Tank | Bodenreiten |
| 116 | Dunmarsch | Stein/Schwerkraft | L051/3 Three | – | Tank | Bodenreiten |
| 117 | Skarit | Schwerkraft | L052/1 Three | Skaral [Level>=18] | Control | – |
| 118 | Skaral | Schwerkraft/Stein | L052/2 Three | Skarabon [Level>=34] | Control | – |
| 119 | Skarabon | Schwerkraft/Licht | L052/3 Three | – | Control | – |
| 120 | Sengel | Glut | L053/1 Three | Sengar [Level>=22] | Striker | – |
| 121 | Sengar | Glut/Stein | L053/2 Three | Sengrath [Level>=40] | Striker | Grabreiten |
| 122 | Sengrath | Glut/Stein | L053/3 Three | – | Striker | Grabreiten |
| 123 | Stachik | Gift | L054/1 Two | Stacharon [Level>=26] | Striker | – |
| 124 | Stacharon | Gift/Stein | L054/2 Two | – | Striker | – |
| 125 | Sirrkorn | Sturm | L055/1 Two | Sirrsturm [Level>=26 & Weather=Sandstorm] | Speed | – |
| 126 | Sirrsturm | Sturm/Stein | L055/2 Two | – | Speed | – |
| 127 | Mirasel | Arkan | L056/1 Two | Mirazhar [Level>=28 & Weather=Heatwave] | Control | – |
| 128 | Mirazhar | Arkan/Licht | L056/2 Two | – | Control | – |

## §93 Arten #129–#160 (LOCKED, K24 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 129 | Vitrel | Licht | L057/1 Two | Vitrapha [Level>=24 & TimeOfDay=Night] | Support | – |
| 130 | Vitrapha | Licht/Kristall | L057/2 Two | – | Support | – |
| 131 | Mesakil | Stein | L058/1 Two | Mesakor [Level>=30] | Tank | – |
| 132 | Mesakor | Stein/Glut | L058/2 Two | – | Tank | Bodenreiten |
| 133 | Qadrant | Metall/Schwerkraft | L059/1 Single | – | Control | – |
| 134 | Mahrsil | Geist/Sturm | L060/1 Single | – | Caster | – |
| 135 | Pyrolm | Glut | L061/1 Three | Pyrolax [Level>=18] | Caster | – |
| 136 | Pyrolax | Glut | L061/2 Three | Pyroluth [Level>=36] | Caster | – |
| 137 | Pyroluth | Glut/Stein | L061/3 Three | – | Caster | – |
| 138 | Ambolt | Metall | L062/1 Three | Ambrak [Level>=20] | Tank | – |
| 139 | Ambrak | Metall/Glut | L062/2 Three | Ambross [Level>=38] | Tank | – |
| 140 | Ambross | Metall/Glut | L062/3 Three | – | Tank | – |
| 141 | Aschwel | Glut | L063/1 Three | Aschund [Level>=16] | Speed | – |
| 142 | Aschund | Glut | L063/2 Three | Aschgrim [Level>=34] | Speed | – |
| 143 | Aschgrim | Glut/Leere | L063/3 Three | – | Speed | – |
| 144 | Obsikin | Stein | L064/1 Three | Obsidar [Level>=22] | Tank | – |
| 145 | Obsidar | Stein/Kristall | L064/2 Three | Obsidrax [Level>=40] | Tank | – |
| 146 | Obsidrax | Stein/Kristall | L064/3 Three | – | Tank | Bodenreiten |
| 147 | Ignavyr | Glut | L065/1 Two | Ignavor [Level>=42] | Striker | – |
| 148 | Ignavor | Glut/Schwerkraft | L065/2 Two | – | Striker | Flugreiten |
| 149 | Fumel | Leere | L066/1 Two | Fumaroth [Level>=28 & TimeOfDay=Night] | Control | – |
| 150 | Fumaroth | Leere/Glut | L066/2 Two | – | Control | – |
| 151 | Drusil | Kristall | L067/1 Two | Drusaro [Level>=28] | Support | – |
| 152 | Drusaro | Kristall/Glut | L067/2 Two | – | Support | – |
| 153 | Volket | Sturm | L068/1 Two | Voltarn [Level>=30] | Speed | – |
| 154 | Voltarn | Metall/Sturm | L068/2 Two | – | Speed | Flugreiten |
| 155 | Bassalt | Klang/Stein | L069/1 Single | – | Support | – |
| 156 | Nucleox | Schwerkraft/Glut | L070/1 Single | – | Caster | – |
| 157 | Snevel | Frost | L071/1 Three | Snevar [Level>=18] | Speed | – |
| 158 | Snevar | Frost | L071/2 Three | Snevrik [Level>=36] | Speed | – |
| 159 | Snevrik | Frost/Licht | L071/3 Three | – | Speed | – |
| 160 | Kjalf | Frost | L072/1 Three | Kjalmur [Level>=22] | Tank | – |

## §94 Arten #161–#192 (LOCKED, K25 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 161 | Kjalmur | Frost/Stein | L072/2 Three | Kjalgrund [Level>=40 & Weather=Snow] | Tank | Bodenreiten |
| 162 | Kjalgrund | Frost/Stein | L072/3 Three | – | Tank | Bodenreiten |
| 163 | Uvlet | Frost | L073/1 Three | Uvarn [Level>=18] | Caster | – |
| 164 | Uvarn | Frost/Geist | L073/2 Three | Uvalis [Level>=36]; Uvasil [Level>=36 & Zone=R07_Z03 & TimeOfDay=Night] | Caster | – |
| 165 | Uvalis | Frost/Geist | L073/3 Three | – | Caster | Flugreiten |
| 166 | Uvasil | Leere/Frost | L073/3 Branch | – | Control | – |
| 167 | Lyskin | Licht | L074/1 Three | Lysmara [Level>=20 & Weather=Clear] | Support | – |
| 168 | Lysmara | Licht/Frost | L074/2 Three | Lysthane [Level>=38] | Support | Flugreiten |
| 169 | Lysthane | Licht/Klang | L074/3 Three | – | Support | Flugreiten |
| 170 | Vardlit | Stein | L075/1 Two | Vardholm [Level>=28] | Tank | – |
| 171 | Vardholm | Stein/Frost | L075/2 Two | – | Tank | – |
| 172 | Eidrun | Geist | L076/1 Two | Eidwacht [Level>=30 & Moon=FullMoon] | Caster | – |
| 173 | Eidwacht | Geist/Klang | L076/2 Two | – | Caster | – |
| 174 | Hallkid | Klang | L077/1 Two | Hallbrand [Level>=30] | Speed | – |
| 175 | Hallbrand | Klang/Stein | L077/2 Two | – | Speed | Kletterreiten |
| 176 | Glazil | Kristall | L078/1 Two | Glazvind [Level>=28 & Weather=Snow] | Control | – |
| 177 | Glazvind | Sturm/Kristall | L078/2 Two | – | Control | – |
| 178 | Tysvorn | Leere/Frost | L079/1 Single | – | Striker | – |
| 179 | Skriv | Arkan | L080/1 Three | Skrivar [Level>=20] | Caster | – |
| 180 | Skrivar | Arkan | L080/2 Three | Skriveth [Level>=38] | Caster | – |
| 181 | Skriveth | Arkan/Licht | L080/3 Three | – | Caster | – |
| 182 | Thaelit | Arkan | L081/1 Three | Thaelon [Level>=20] | Tank | – |
| 183 | Thaelon | Geist/Arkan | L081/2 Three | Thaelarch [Level>=40] | Tank | – |
| 184 | Thaelarch | Geist/Metall | L081/3 Three | – | Tank | – |
| 185 | Tikkel | Metall | L082/1 Three | Tikkar [Level>=18] | Control | – |
| 186 | Tikkar | Metall/Arkan | L082/2 Three | Tikkoran [Level>=36] | Control | – |
| 187 | Tikkoran | Metall/Schwerkraft | L082/3 Three | – | Control | – |
| 188 | Sarkel | Geist | L083/1 Three | Sarkon [Level>=24] | Striker | – |
| 189 | Sarkon | Geist/Stein | L083/2 Three | Sarkothar [Level>=42 & Moon=NewMoon] | Striker | Bodenreiten |
| 190 | Sarkothar | Geist/Arkan | L083/3 Three | – | Striker | Bodenreiten |
| 191 | Tilgel | Leere | L084/1 Two | Tilgrath [Level>=30] | Control | – |
| 192 | Tilgrath | Leere/Arkan | L084/2 Two | – | Control | – |

## §95 Arten #193–#224 (LOCKED, K26 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 193 | Hymlit | Klang | L085/1 Two | Hymnora [Level>=26 & BondTier>=3] | Support | – |
| 194 | Hymnora | Klang/Geist | L085/2 Two | – | Support | – |
| 195 | Optil | Licht | L086/1 Two | Optikor [Level>=32 & TimeOfDay=Night] | Caster | – |
| 196 | Optikor | Schwerkraft/Licht | L086/2 Two | – | Caster | – |
| 197 | Menhirok | Stein/Arkan | L087/1 Single | – | Tank | – |
| 198 | Kronvaal | Arkan/Metall | L088/1 Single | – | Caster | – |
| 199 | Klirrit | Kristall | L089/1 Three | Klirrflug [Level>=20] | Speed | – |
| 200 | Klirrflug | Kristall/Klang | L089/2 Three | Klirrathan [Level>=38]; Klirrnox [Level>=38 & Zone=R09_Z04] | Speed | – |
| 201 | Klirrathan | Kristall/Klang | L089/3 Three | – | Speed | Flugreiten |
| 202 | Klirrnox | Leere/Kristall | L089/3 Branch | – | Striker | – |
| 203 | Spatling | Kristall | L090/1 Three | Spatwurm [Level>=22] | Tank | – |
| 204 | Spatwurm | Kristall/Stein | L090/2 Three | Spathorn [Level>=40] | Tank | Grabreiten |
| 205 | Spathorn | Kristall/Schwerkraft | L090/3 Three | – | Tank | Grabreiten |
| 206 | Ligrel | Schwerkraft | L091/1 Three | Ligrath [Level>=20] | Control | – |
| 207 | Ligrath | Schwerkraft/Leere | L091/2 Three | Ligravor [Level>=38] | Control | – |
| 208 | Ligravor | Schwerkraft/Kristall | L091/3 Three | – | Control | Kletterreiten |
| 209 | Facetin | Kristall | L092/1 Two | Facettor [Level>=28 & BondTier>=3] | Caster | – |
| 210 | Facettor | Kristall/Licht | L092/2 Two | – | Caster | – |
| 211 | Mullit | Metall | L093/1 Two | Mullhorn [Level>=30] | Striker | – |
| 212 | Mullhorn | Metall/Stein | L093/2 Two | – | Striker | – |
| 213 | Misslit | Leere | L094/1 Two | Missgrath [Level>=32] | Caster | – |
| 214 | Missgrath | Leere/Kristall | L094/2 Two | – | Caster | – |
| 215 | Psionit | Arkan | L095/1 Two | Psioneth [Level>=30 & Moon=FullMoon] | Control | – |
| 216 | Psioneth | Arkan/Kristall | L095/2 Two | – | Control | – |
| 217 | Miasmar | Gift/Leere | L096/1 Single | – | Control | – |
| 218 | Stalakkord | Klang/Kristall | L097/1 Single | – | Support | – |
| 219 | Nimbel | Sturm | L098/1 Three | Nimbor [Level>=26] | Tank | – |
| 220 | Nimbor | Sturm/Klang | L098/2 Three | Nimbaroth [Level>=44] | Tank | Flugreiten |
| 221 | Nimbaroth | Sturm/Schwerkraft | L098/3 Three | – | Tank | Flugreiten |
| 222 | Cirrel | Sturm | L099/1 Three | Cirrhawk [Level>=20] | Speed | – |
| 223 | Cirrhawk | Sturm/Licht | L099/2 Three | Cirrhaven [Level>=38] | Speed | – |
| 224 | Cirrhaven | Sturm/Licht | L099/3 Three | – | Speed | Flugreiten |

## §96 Arten #225–#256 (LOCKED, K27 · `Data/Echos/Species.csv`)

| # | Name | Typen | Linie/Stufe | Evolution → | Rolle | Reiten |
|---|---|---|---|---|---|---|
| 225 | Nubi | Licht | L100/1 Three | Nubilo [Level>=18] | Support | – |
| 226 | Nubilo | Licht/Sturm | L100/2 Three | Nubiluna [Level>=34]; Nubisk [Level>=34 & Moon=NewMoon & Zone=R10_Z02] | Support | – |
| 227 | Nubiluna | Licht/Klang | L100/3 Three | – | Support | – |
| 228 | Nubisk | Leere/Licht | L100/3 Branch | – | Control | – |
| 229 | Harfel | Klang | L101/1 Two | Harfion [Level>=28] | Support | – |
| 230 | Harfion | Klang/Sturm | L101/2 Two | – | Support | – |
| 231 | Tintel | Klang | L102/1 Two | Tintabul [Level>=30 & TimeOfDay=Dusk] | Caster | – |
| 232 | Tintabul | Klang/Licht | L102/2 Two | – | Caster | – |
| 233 | Holmel | Schwerkraft | L103/1 Two | Holmgard [Level>=34] | Tank | – |
| 234 | Holmgard | Schwerkraft/Stein | L103/2 Two | – | Tank | Bodenreiten |
| 235 | Levitel | Schwerkraft | L104/1 Two | Levithar [Level>=32] | Control | – |
| 236 | Levithar | Arkan/Schwerkraft | L104/2 Two | – | Control | – |
| 237 | Graupel | Frost | L105/1 Two | Graupix [Level>=30 & Weather=Thunderstorm] | Striker | – |
| 238 | Graupix | Kristall/Sturm | L105/2 Two | – | Striker | – |
| 239 | Lumaskiff | Licht/Sturm | L106/1 Single | – | AllRound | Flugreiten |
| 240 | Astraviel | Arkan/Licht | L107/1 Single | – | Caster | – |
| 241 | Sylv'anor | Blüte/Klang | L108/1 Legendary | – | Support | – |
| 242 | Orh'gruun | Stein/Schwerkraft | L109/1 Legendary | – | Tank | – |
| 243 | Nhael'vesh | Gift/Geist | L110/1 Legendary | – | Control | – |
| 244 | Thal'assyr | Flut/Sturm | L111/1 Legendary | – | Speed | – |
| 245 | Ash'kareth | Licht/Arkan | L112/1 Legendary | – | Caster | – |
| 246 | Pyr'thagon | Glut/Metall | L113/1 Legendary | – | Striker | – |
| 247 | Isv'aldr | Frost/Licht | L114/1 Legendary | – | Support | – |
| 248 | Ka'thurel | Geist/Arkan | L115/1 Legendary | – | Control | – |
| 249 | Prism'aion | Kristall/Klang | L116/1 Legendary | – | Caster | – |
| 250 | Aeth'rion | Klang/Licht | L117/1 Legendary | – | AllRound | – |
| 251 | Velnox | Leere/Schwerkraft | L118/1 Mythical | – | Control | – |
| 252 | Chronaire | Klang/Arkan | L119/1 Mythical | – | Speed | – |
| 253 | Mirrowisp | Kristall/Geist | L120/1 Mythical | – | Control | – |
| 254 | Ouroveth | Gift/Blüte | L121/1 Mythical | – | Tank | – |
| 255 | Zenthrax | Schwerkraft/Metall | L122/1 Mythical | – | Striker | – |
| 256 | Aurelune | Licht/Leere | L123/1 Mythical | – | Caster | – |

## §97 Fähigkeitsarten & IDs (LOCKED, K28 §1–§2 · `Data/Abilities/Abilities.csv`)

- Aktiv **180** (12 je Typ, `ABL_A001–A180`) · Passiv **90** (6 je Typ, `ABL_P001–P090`) · Crescendo **30** (2 je Typ, `ABL_U001–U030`) · Feld **30** (2 je Typ, `ABL_F001–F030`) = **330**.
- Kampfset 4 aktiv + 1 passiv + 1 Crescendo (+ 0–1 Feld); Repertoire ohne Vergessen; **keine Abklingzeiten** auf Aktiven (ADR-094).
- Jede Fähigkeit hat einen Typ (keine typlosen); Anzeigenamen global eindeutig, keine Kollision mit Echo-Namen.

## §98 Machtbudget & Zeitkosten (LOCKED, K28 §3 · `tools/abilities/abl.py`, `AbilityDefinition.h`)

- V = Schaden + Σ Effektwerte; Schaden = Stärke × Gen/1000 × Zielfaktor/1000 × mittlere Treffer/1000 (ganzzahlig).
- **Zeitkosten = clamp(rund10(20 + V), 50, 200)**, 100 = Standardzug; nie handgesetzt (ADR-093). Zielfaktoren Single 1000 · Row 1400 · Enemies 1700 ‰.
- Effektwerte K28 §3.2 (Tuning in K63). Wer-Faktor Einzel 1000 · Reihe 1300 · Gruppe 1600 ‰.

## §99 Effekt-DSL (LOCKED, K28 §4)

- `Effekt(Arg,…)` mit `;` getrennt; 42 Primitiva in 9 Gruppen; Laufzeit über Primitiv-Registry in `GF_Combat` (DR-25); Regeltexte generiert.

## §100 Status-Effekte (LOCKED Namen/Immunitäten, Zahlen PROVISIONAL → K32 · `Data/Abilities/StatusEffects.csv`)

- 15 Status, je Typ eine Immunität: Brand (Glut) · Ausgetrocknet (Flut) · Rückstoß (Stein) · Verlangsamt (Sturm) · Welke (Blüte) · Starre (Frost) · Entzug (Leere) · Geblendet (Licht) · Vergiftet (Gift) · Erschüttert (Metall) · Furcht (Geist) · Gebrochen (Kristall) · Verstummt (Klang) · Schwebend (Schwerkraft) · Verflucht (Arkan).
- Ein Haupt-Status + Gift (1–5 Stapel) parallel; Rückstoß/Erschüttert sind Sofort-Effekte; nach Starre 2 Runden Immunität (ADR-097).

## §101 Aktive Fähigkeiten (LOCKED, K28 §7–§8)

- 12 je Typ nach Slot-Schema (Einstieg 1–2, Mittel 3–5, Schwer 6, Status/Feld/Identität 7–12); ≥ 2 physisch, ≥ 2 speziell, ≥ 3 Status je Typ; ≥ 3 Identitäts-Fähigkeiten je Typ (CANON §78).
- Kennzahlen: Physisch 48 · Speziell 63 · Status 69; Ø Stärke 66; Zeitkosten 50–150.
- Tags: `Contact`, `Sound` (durch Verstummt blockiert), `Ground` (verfehlt Schwebend). Validator `tools/gen_abilities.py` AB-01…AB-14.

## §102 Passive & Auslöser (LOCKED, K29 §1–§3 · `Data/Abilities/Abilities.csv` ABL_P, `Data/Echos/PassiveOptions.csv`)

- 6 Passive je Typ (90, inkl. 16 Feldklänge); 1 aktive Passive je Echo; 1–3 sichtbare Optionen aus eigenen Typen + 1 versteckte aus Fremdtyp; Wildverteilung 60/30/10 % (versteckt 0 %, Sehr selten 5 %); Wechsel per **Wandelklang**; versteckt frei über Kodex 4 oder Zucht.
- Auslöser: Always, BattleStart, SwitchIn, TurnStart, HitTaken, ContactTaken, HitDealt, CritDealt, LowHP (≤ 33 %, einmal), StatusReceived, AllyFainted, EnemyFainted, RowFront, RowBack, HarmonyFull, Weather.X, Terrain.X, FieldSong.
- Statische Primitiva: Mod (≤ 1150 ‰ dauerhaft, ≤ 1300 bedingt), TypePower (≤ 1100, LowHP ≤ 1500), Resist (≥ 700), Immune, StatusChance, HealPower, TimeCost (≥ −10), Custom (nur Feldklang); Mod-Ketten ≤ 1500 ‰.

## §103 Feldklänge (LOCKED, K29 §4)

- 16 exklusive Passive der Ursprungsstimmen/Mythischen (Wurzellied, Bergschwere, Moorgedächtnis, Gezeitenwende, Rätselglanz, Weltenschmiede, Aurora der Erhaltung, Weltgedächtnis, Brechung, Einklang, Große Pause, Taktwechsel, Spiegelwelt, Ewiger Kreis, Sternensturz, Finsternis); nur einer gleichzeitig aktiv (zuerst eingewechselt); nicht Ranked; je ein `UFieldSongPrimitive`.

## §104 Lernsets (LOCKED, K29 §5–§7 · `Data/Echos/Learnsets.csv`, `tools/gen_learnsets.py`)

- Generiert und deterministisch (stabile Hashes); Overrides nur per `LearnsetOverrides.csv` (K63).
- Lernstufen E (≤ 45, Lv. 1–8) · M (50–75, Lv. 10–30) · S (Status, Lv. 6–34) · L (≥ 80 oder Zeit ≥ 110, Lv. 28–44) · H (≥ 100, Lv. 36–52); Zielgrößen 9/11/13 (Dreier), 10/12 (Zweier), 13 (Einzel/Zweig/Legendär).
- Je Art 2 **Abdeckungstypen** (sehr effektiv gegen die Resistenzen der Primärfarbe); 1 Evolutionsfähigkeit ab Stufe 2; 3 Ei-Fähigkeiten je Linie. Regeln LS-01…LS-12.

## §105 Klangschriften & Tutoren (LOCKED, K29 §8–§9 · `Data/Items/Klangschriften.csv`, `Data/Abilities/Tutors.csv`)

- 90 Klangschriften `ITM_KS_001–090`, 6 je Typ (Mittel/Spät/Status); nutzbar, wenn Fähigkeitstyp = Typ des Echos oder Abdeckungstyp.
- 30 Tutor-Fähigkeiten (2 je Typ, bevorzugt Schwer-Fähigkeit), Fraktionslehrer, Rufrang 3–4, 2.000/3.500 ◎ (Startwerte → K42/K47).

## §106 Crescendo-Regeln (LOCKED, K30 §1–§5 · `Data/Echos/CrescendoOptions.csv`)

- 30 Crescendos (2 je Typ: Schaden + Team); Budget 200–320 MP; Zeitkosten 200; Harmoniekosten clamp(rund10(60 + (V−200)/3), 60, 100) → 60–90 (Tag `HarmonyCost`).
- Ankündigung als goldener Marker auf der Zeitleiste; 1 je Echo und Kampf, 1 je Seite und Runde; ab Bindungsstufe 2, ab Stufe 5 Kosten −10; Verklingen vor Ausführung → 50 % Rückerstattung.
- Inszenierung ≤ 4,0 s (Option kurz 1,5 s, PvP immer kurz). Arten lernen alle Crescendos ihrer Typen bei Bindungsstufe 2; ★ bevorzugt (Schaden für Striker/Caster/Speed, sonst Team).
- Harmonie-Leiste 100; Startwerte Harmonie-Gewinn: Treffer +5, sehr effektiv +8, Kombo +10–20, Status-Fehlschlag +5, erlittener Volltreffer +5 (final K33).

## §107 Feldfähigkeiten & Pfad-Tore (LOCKED, K30 §6–§9 · `Data/Echos/FieldOptions.csv`)

- 30 Feldfähigkeiten (2 je Typ), Kategorien `Field.Traversal|Sense|Gather|Puzzle|Social`; ab Bindungsstufe 1, Echo im Chor; Ausdauerkosten 25/10/10/15/10, Regeneration 5/s.
- Bedingung: Typ der Art + Merkmal/Größe; 0–1 je Art (240 von 256 Arten); jede Feldfähigkeit ≥ 3 Arten.
- 12 Pfad-Tor-Typen (Eis/Dorn, Geröll, Spalt, Wasser, Gestrüpp, Dunkel, Mechanik, Ahnen, Prisma, Glyphe, Siegel, Last); PT-1 ≥ 2 Lösungen, davon ≥ 1 typunabhängig; PT-2 nie auf Hauptpfad; PT-3 ≥ 6 Tor-Typen je Region. Reitarten sind keine Feldfähigkeiten.

## §108 Fähigkeitenbestand (LOCKED, K30 §10)

- 330 Fähigkeiten: 180 aktiv · 90 passiv (inkl. 16 Feldklänge) · 30 Crescendo · 30 Feld; `tools/gen_abilities.py validate --final` und `tools/gen_learnsets.py validate` ohne Verstöße.

## §109 Zeiteinheiten (LOCKED, K31 §2 – löst Q1)

- **Tick** ganzzahlig; 100 Ticks = Standardzug (Kosten 100) bei GES 100. **Zug** = Handlung eines Echos (Status-Dauern in eigenen Zügen). **Runde** = 100 Ticks globaler Zeit (Terrain/Wetter/Arena-Mechaniken).
- Kampf-Seed aus `Fork(5)` der Weltsaat + Begegnungs-ID; PvP-Seed vom Server; Replays = Seed + Eingaben.

## §110 Verzögerungsformel (LOCKED, K31 §3 · `tools/ref/aethris_combat.py`, `ResonanceTimeline.h`)

- Verzögerung = max(10, ⌊Kosten_eff × 300 / (GES_eff + 200)⌋); Kosten_eff = Kosten × 1,3 (Verlangsamt) × 1,4 (Ungehorsam) + 20 (Verflucht); GES_eff mit Stufenfaktor.

## §111 Zugablauf & Modifikatoren (LOCKED, K31 §4–§6)

- Startzug = Verzögerung(100) × 850–1000 ‰ (Hinterhalt −200 ‰). Zugablauf: TurnBegin → Status-Tick → Passive → Sonderfälle → Wahl → Auflösung → Commit → TurnEnd.
- Fremdverzögerung (Delay, Erschüttert +50, Starre +100) ≤ **100 Ticks** zwischen zwei eigenen Zügen; Haste frühestens Jetzt + 1; Items Zeitkosten 60 (nicht Ranked).

## §112 Vorgriff, Ankündigung, Gleichstand (LOCKED, K31 §7–§9)

- **Vorgriff:** Prioritätsfähigkeit bis 25 Ticks × Stufe vor dem eigenen Zug, zu Beginn eines fremden Zuges, 1× je Zyklus; Folgezug ab Originalposition.
- **Ankündigung** (Charge, Crescendo): Marker bei Jetzt + Verzögerung(Kosten); verschiebbar (Deckel), Abbruch durch Starre, Verstummt (Sound), Verklingen; Nachklang 50; Ankündigungen lösen vor normalen Zügen desselben Ticks auf.
- **Gleichstand:** GES_eff ↓ → Seite, die zuletzt nicht handelte → PCG; PvP/Koop planen gleichzeitig bei gleichem Tick.

## §113 Wechsel, Flucht, Kampfende (LOCKED, K31 §10–§11)

- Wechsel: Zeitkosten 60, Eingang bei Jetzt + Verzögerung(60); Ersatz nach Verklingen bei 500 ‰ der Startverzögerung; Stufen/Status des ausgehenden Echos zurückgesetzt.
- Flucht per Rückzugsmarker (Verzögerung 100 des schnellsten eigenen Echos), nicht gegen Arena/Boss/PvP; kein Zufall.
- Formate: Duell 1+5, Duo 2+4, Trio 3+3, Raid (K35); Duell: Flächenschaden ×0,8 (K32).

## §114 Schadensformel (LOCKED, K32 §2 · `DamageCalculator.h`, `aethris_combat.damage_chain`)

- Basis = ⌊Stärke × A_eff × (L+10) / (V_eff × 180)⌋ + 2; Kette (je ⌊⌋, Promille): Eigenklang 1250 (Boni ≤ 1400) × Typ × Wetter × Volltreffer 1500 × Formation × Sonstige; Mindestschaden 1.
- **Keine Schadensstreuung** (ADR-112); Volltreffer-Stufen 42/125/250/500 ‰, ignoriert ungünstige Stufen; Brand ANG ×0,75 (physisch); Duell-Flächenfähigkeiten ×0,8; fester Schaden (Status, Terrain, Wetter, Meteore) in ‰ Max-HP.

## §115 Auflösungsreihenfolge (LOCKED, K32 §1)

- Zielbestimmung → Reflexion → Trefferwurf (Fehlschlag +5 Harmonie) → Volltreffer → Schaden → Schild → HP → Effekte → Anwender-Folgen (Drain/Recoil/Exhaust) → Reaktionen (Konter, Passive) → Harmonie/Kombo. Mehrfachtreffer je Treffer, Reaktionen einmal; Flächen in Zeitleisten-Reihenfolge.

## §116 Status final (LOCKED, K32 §5 · `Data/Abilities/StatusEffects.csv`)

- Dauern in eigenen Zügen; Brand 60 ‰ Max-HP/Zug, Gift 30 ‰ je Stapel (1–5); ein Haupt-Status ohne Überschreiben (Ausnahme Starre über Verlangsamt); Reinigen entfernt Haupt-Status + Gift; Reservewechsel beendet Furcht/Schwebend, halbiert Gift; Status enden mit Kampfende (Eiserner Wärter: bis Klangbrunnen).

## §117 Terrain (LOCKED, K32 §6 · `Data/Combat/Terrains.csv`)

- 15 Terrains, Boost 1200 ‰ (Stille/Missklang 1100), ein Terrain gleichzeitig; Gegen-Terrain (Spalte EndedBy) neutralisiert ohne zu legen; Runden-Effekte bei Tick-Vielfachen von 100; Arena-Terrains dauerhaft, kehren nach Überlagerung zurück.

## §118 Kampfwetter (LOCKED, K32 §7)

- Kampf übernimmt Weltwetter der Zone; `Weather(X,n)` überschreibt n Runden; Sonderregeln je Runde (Blitz alle 4 Runden, Sand −4 %, Aurora +5 Harmonie …); Ranked Klar; unter Tage nur Resonanzsturm und Fähigkeitswetter; Schilde addieren bis 50 % Max-HP; Revive 1× je Echo/Kampf.

## §119 Formation (LOCKED, K33 §2–§3)

- Vorder-/Hinterreihe in Duo (VV/VH), Trio (mind. 1 vorn), Raid (K35); Duell ohne Formation.
- Kontakt-Fähigkeiten nur gegen die Vorderreihe (außer IgnoreFormation oder leere Vorderreihe); übrige Fähigkeiten gegen Hinterreihe ×750 ‰.
- Hinterreihe: keine Kontakt-Fähigkeiten; Heilung/Schilde ×1,1; Status-Fähigkeiten +2 Harmonie. Leere Vorderreihe → Hinterreihe rückt kostenlos vor.
- Stellungswechsel Zeitkosten 40 (Flutfeld 20, Schwerefeld 60); Schwebend/Bind verhindern Reihenwechsel.

## §120 Harmonie-Ökonomie (LOCKED, K33 §4)

- Leiste 0–100 je Seite. Quellen: Treffer +5, sehr effektiv +8, Kombo +10–20, Fehlschlag +5, erlittener Volltreffer +5, verklungener Verbündeter +10, Daten (Harmony), Wetter/Terrain. Senken: Crescendo, HarmonyDrain, Stillefeld, Entzug, Missklang (½).

## §121 Kombos (LOCKED, K33 §5–§6 · `Data/Combat/Combos.csv`)

- 36 Kombos: Typ First → Typ Second, zwei verschiedene Verbündete, gleiches Ziel, Fenster 60 Ticks (+20 Bindungs-Duett); Bonus 1100–1400 ‰ auf die zweite Fähigkeit + Effekte + Harmonie; 1 Kombo je Ziel/Auflösung; Fehlschlag behält Anklang; Gegner können kombinieren. Jeder Typ ≥ 4 Kombos.

## §122 Synergien (LOCKED, K33 §7 · `Data/Combat/Chords.csv`)

- 15 Chor-Akkorde (jeder Typ in 3), wirksam bei je ≥ 1 Echo der drei Typen im Chor; max. 2 aktiv; +10 Start-Harmonie, Typen ×1,05. Bindungs-Duett (beide Bindungsstufe ≥ 4): Fenster +20, erste Kombo +5. Linienklang (2 Echos einer Linie): +5. Start-Harmonie aus Synergien ≤ 30.

## §123 Formate & Begegnungen (LOCKED, K33 §8–§10)

- Duell 1+5, Duo 2+4 (ab Rang 5), Trio 3+3 (ab Rang 10), Raid 4 Spieler (ab Rang 22). Arena-Formate laut K02 §9.2; Leihbegleitung bei fehlender Freischaltung.
- Begegnungen: Einzel (Duell), Herde (Format = Anzahl), Alpha, Wärter, Rivale, Arena, Stille-Echo (Sieg heilt, keine Bindung), Boss/Raid, PvP. Koop: Format nach Spielerzahl, gemeinsame Harmonie, Kombos zwischen Spielern.

## §124 KI-Architektur (LOCKED, K34 §2–§3 · `tools/ref/aethris_ai.py`)

- Utility-KI: Aktionsgenerator → 12 Betrachtungen (Schaden, Kill, Status, Setup, Debuff, Heilung, Tempo, Kombo, Wechsel, Crescendo, Formation, Risiko) → Nutzwert / Verzögerung × 100 → Auswahl (Profil-Rauschen, Gleichstand = Datenreihenfolge). StateTree nur außerhalb des Kampfes. Kampf-RNG, < 2 ms/Entscheidung.

## §125 KI-Profile (LOCKED, K34 §4–§6 · `Data/Combat/AIProfiles.csv`)

- 11 Profile (Wild, Scheu, Angriffslustig, Verspielt, Alpha, Anfänger, Geübt, Veteran, Arenameister, Rivale, Boss). Wild-Profile über Merkmale/Temperamente moduliert (Shy: Fluchtmarker < 50 % HP; Aggressive/Territorial: keine Flucht).
- Kampfset-Bau Learnset / Best / Signature / Script; Wechsel per MatchupScore mit Hysterese 2 Züge; Crescendo bei ≥ 35 % gegnerischer HP-Summe, Not oder Konter; Harmonie nie > 2 Runden auf 100.

## §126 Schwierigkeit & Fairness (LOCKED, K34 §8–§9)

- Grade skalieren Profil, Kampfset, Anlagen NPC (5/9/13), Schliff NPC (0/40/80 % des Levels), Wechsel, KI-Kombos, Wissensstand (Sichtbar/Kodex2). Zielbänder Arena erster Versuch: Entspannt ≥ 90 %, Wärter 65–80 %, Meister 35–55 % (→ K63).
- Fairness F-1 kein Eingabelesen, F-2 kein Würfelbetrug, F-3 Wissensstand, F-4 keine verdeckten Werte-Boni, F-5 Absicht im Protokoll.

## §127 Arenameister & Rivale (LOCKED, K34 §7)

- Signatur-Taktik je Arena als Gewichts-Overlay + Startaktion passend zur Feldregel; Rivale Kael adaptiv mit genau einer Anpassung je Begegnung (aus Spielstand, offline).

## §128 Boss-Anatomie (LOCKED, K35 §2)

- Boss = Basisart + 1–3 Spuren auf der Zeitleiste + Phasen (HP-Schwellen; Schaden an der Schwelle gekappt) + 2–4 Mechaniken. HP = Art-HP (Anlage 15) × HP-Faktor × (1 + Skalierung‰ × (Spieler − 1)).
- Status-Anti-Lock (gleicher Status 2× → 3 Runden immun); Starre auf Bosse = +50 Ticks; Fremdverzögerungs-Deckel je Spur; weiches Anschwellen ×1,1 je Runde (max. ×1,5) ab Runde 20 (Story) / 25 (Tiefenresonanz) / 30 (Raid) – kein harter Timer.

## §129 Raid-Format (LOCKED, K35 §3)

- 1–4 Spieler ab Wärterrang 22; 2 Aktive je Spieler (2 Spieler: 3; Solo: Trio); gemeinsame Vorder-/Hinterreihe (je max. 4), gemeinsame Harmonie, 1 Revive je Echo; Solo-Variante offline (HP ×0,6, Ankündigungen +1 Runde); Belohnungen gleich für alle; kein Sperrtimer (Erstabschluss je Spieltag, K62).

## §130 Boss-Mechaniken (LOCKED, K35 §4 · `Data/Combat/BossMechanics.csv`)

- 18 Mechaniken, alle angekündigt (≥ 1 Runde) mit Gegenspiel aus einer anderen Klangfarbe als der des Bosses; max. 4 je Boss, 2 aktiv je Phase.

## §131 Boss-Verzeichnis (LOCKED, K35 §5–§9 · `Data/Combat/Bosses.csv`)

- 28 Bosse: 10 Story (Prolog bis Velnox-Finale), 8 Raids RAID_01–08 (RAID_06 Zenthrax), 10 Tiefenresonanzen DR_01–10 (DR_08 Zenthrax solo). Raid-HP-Faktoren 10–13, Skalierung 700 ‰. Mythische Bindung im Fenster ≤ 15 % HP, instanziert je Teilnehmer; Velnox im Finale nicht bindbar (Nachhall „Stille Stunde“). Stille-Echos werden durch Sieg geheilt.
