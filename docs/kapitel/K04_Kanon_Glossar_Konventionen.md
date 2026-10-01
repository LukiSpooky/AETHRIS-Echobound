# K04 · Kanon, Glossar, Namens- & ID-Konventionen

| Feld | Wert |
|---|---|
| Dokument | Kapitel 04 von 68 |
| Version | 1.0 |
| Owner | Creative Director |
| Mitwirkende | Narrative Writer, Lokalisierung, Lead Gameplay Programmer, Legal, QA Lead |
| Baut auf | K01–K03 (CANON §1–§20) |
| Status | ✅ Freigegeben |
| Neue Kanon-Einträge | CANON §21 (Glossar), §22 (Namenssystem), §23 (IDs & Tags), §24 (Stil & Lokalisierung) |

---

## Inhalt

1. [Zweck](#1-zweck)
2. [Glossar](#2-glossar)
3. [Sprachfamilien der Welt](#3-sprachfamilien-der-welt)
4. [Echo-Namenssystem (Morphem-Lexikon)](#4-echo-namenssystem-morphem-lexikon)
5. [Wissenschaftliche Namen](#5-wissenschaftliche-namen)
6. [Namensprüfung (Clean-Room & Marken)](#6-namensprüfung-clean-room--marken)
7. [ID-Konventionen](#7-id-konventionen)
8. [GameplayTag-Hierarchie](#8-gameplaytag-hierarchie)
9. [Asset- und Dateibenennung](#9-asset--und-dateibenennung)
10. [Text-Stilrichtlinie](#10-text-stilrichtlinie)
11. [Lokalisierungskonventionen](#11-lokalisierungskonventionen)
12. [Werkzeuge & Code](#12-werkzeuge--code)
13. [Decision Records](#13-decision-records)
14. [Kanon-Updates](#14-kanon-updates)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Zweck

Ein Projekt mit 256 Kreaturen, 330 Fähigkeiten, ~600.000 Wörtern Text und 12 Sprachen bricht ohne verbindliche Benennungsregeln zusammen. Dieses Kapitel ist die **Sprachverfassung** von AETHRIS: Es legt fest, wie Dinge heißen, wie sie im Code identifiziert werden und wie Text klingt.

**Hierarchie bei Konflikten:** Clean-Room (DR-22) > dieses Kapitel > Wünsche einzelner Disziplinen.

---

## 2. Glossar

Alphabetisch. Spalte „Code“ = Bezeichner in Code/Daten (englisch). Begriffe mit ★ sind spielerseitig sichtbar und dürfen in Texten nie durch Synonyme ersetzt werden.

| Begriff (DE) | Code | Definition | Eingeführt |
|---|---|---|---|
| ★ Akkord | `Akkord` | Arena-Abzeichen; 10 Akkorde = Weltakkord | K02 |
| ★ Akademie der Resonanz | `Faction.Academy` | Forscher-Fraktion (F01) | K01 |
| ★ Anlagen | `Aptitude` | Genetisch festgelegte Wertpotenziale eines Echos (K18/K38) | K04 |
| ★ Anschlag | `Strike` | Timing-Aktion der Resonanzbindung, bei der das Siegel am Resonator angeschlagen wird | K01 |
| ★ Arenameister | `ArenaMaster` | Leiter einer Stadt-Arena | K01 |
| ★ Aufträge | `Contract` | Kurze, wiederholbare Aufgaben (Questbrett/Außenposten), zählen nicht zu den 210 Nebenquests | K04 |
| ★ Außenposten | `Outpost` | Kleinste Siedlungsform (30) | K01 |
| ★ Bindung | `Bond` | Beziehungswert Wärter↔Echo (0–1000, 6 Stufen) | K01 |
| ★ Chor | `Chor` | Aktiver Trupp, max. 6 Echos | K01 |
| ★ Crescendo | `Crescendo` | Ultimate-Fähigkeit, verbraucht 100 Harmonie | K01 |
| ★ Echo | `Echo` | Kreatur von Aethris; lebendes Fragment des Weltlieds | K01 |
| ★ Echo-Kodex | `Kodex` | Bestiarium mit 4 Forschungsstufen pro Art | K01 |
| ★ Einklang | `PerfectStrike` | Perfektes Timing beim Anschlag | K02 |
| ★ Einstimmen | `Attune` | Beruhigungsphase vor dem Anschlag | K02 |
| ★ Erschöpft / verklungen | `Exhausted` | Kampfunfähiger Zustand eines Echos (nie Tod) | K01 |
| ★ Erstresonanz | `FirstResonance` | Prolog-Bindung des Starters | K02 |
| ★ Feldfähigkeit | `FieldAbility` | Fähigkeit mit Oberweltwirkung | K01 |
| ★ Formation | `Formation` | Vorder-/Hinterreihe im Kampf | K01 |
| ★ Freie Stimmen | `Faction.FreeVoices` | Rebellen-Fraktion (F04) | K01 |
| ★ Goldklang-Kontor | `Faction.Goldklang` | Händler-Fraktion (F02) | K01 |
| ★ Grundfrequenz | `RootFrequency` | Individuelle Schwingung eines Echos; der Spieler kann sie hören | K01 |
| ★ Große Stille | `GreatSilence` | Zerbrechen des Weltlieds vor ~1.000 Jahren | K01 |
| ★ Harmonie | `Harmony` | Team-Leiste im Kampf (0–100) | K01 |
| ★ Hain → Resonanzhain | `Sanctuary` | Begehbares Refugium | K01 |
| ★ Klangbrunnen | `SoundWell` | Heilpunkt | K02 |
| ★ Klangschrift | `SoundScript` | Wiederverwendbarer Lehrgegenstand für Fähigkeiten | K03 |
| ★ Kodex-Linse | `KodexLens` | Kamera/Fotografie | K01 |
| ★ Lager-Moment | `Camp` | Rastplatz-Interaktion | K02 |
| ★ Morph | `Morph` | Seltene genetische Erscheinungsvariante | K01 |
| ★ Orden der Stille | `Faction.Order` | Antagonisten-Fraktion (F05) | K01 |
| ★ Repertoire | `Repertoire` | Alle gelernten aktiven Fähigkeiten eines Echos | K03 |
| ★ Resonanzbindung | `Bonding` | Fangsystem | K01 |
| ★ Resonanzhain | `Sanctuary` | s. o. | K01 |
| ★ Resonanzsinn | `ResonanceSense` | Wahrnehmungsmodus | K01 |
| ★ Resonanzstein | `ResonanceStone` | Schnellreisepunkt | K01 |
| ★ Resonanzsturm | `Weather.ResonanceStorm` | Seltenes globales Wetter (W10) | K01 |
| ★ Resonator | `Resonator` | Werkzeug des Wärters | K01 |
| ★ Rückklang | `Rueckklang` | Fehlerzustand bei erschöpftem Chor | K02 |
| ★ Ruf | `Reputation` | Fraktionsansehen, 6 Ränge | K03 |
| ★ Schliff | `Polish` | Trainingswerte (Summe 240) | K03 |
| ★ Siegel | `Seal` | Verbrauchsgut der Bindung | K01 |
| ★ Sol (◎) | `Sol` | Währung | K02 |
| ★ Stillezone | `SilenceZone` | Gebiet, in dem Echos verstummen | K01 |
| ★ Temperament | `Temperament` | Kampf- und Bindungsverhalten eines Echos | K01 |
| ★ Tiefenresonanz | `DeepResonance` | Endgame-Dungeon (8) | K01 |
| ★ Persönlichkeit | `Personality` | Wesenszug eines Echos | K01 |
| ★ Ursprungsstimme | `PrimordialVoice` | Eine der 10 legendären Echos | K01 |
| ★ Verstummt | `Silenced` | Durch Stillezone erstarrtes Echo (grau, gegnerisch) | K02 |
| ★ Wachstumsrate | `GrowthRate` | EP-Kurve einer Art | K01 |
| ★ Wandelklang | `ShiftTone` | Item für Passiv-Wechsel | K03 |
| ★ Wärter | `Warden` | Mensch, der mit Echos in Resonanz tritt; Spielerrolle | K01 |
| ★ Wärterrang | `WardenRank` | Spielerlevel 1–40 | K01 |
| ★ Weltakkord | `WorldChord` | Alle 10 Akkorde | K02 |
| ★ Weltlied (Aethersang) | `WorldSong` | Urresonanz, aus der alles Leben stammt | K01 |
| ★ Wildwacht | `Faction.Wildwatch` | Ranger-Fraktion (F03) | K01 |
| ★ Zeitleiste → Resonanz-Zeitleiste | `Timeline` | Initiative-System im Kampf | K01 |

### 2.1 Verbotene Begriffe (Clean-Room-Liste, Auszug)

In keinem spielerseitigen Text, Asset-Namen, Code-Kommentar oder Marketingtext erlaubt. Die vollständige Liste führt Legal im Werkzeug `NameGuard` (§12).

| Kategorie | Verboten (Beispiele) | Stattdessen |
|---|---|---|
| Kreaturenoberbegriffe | „Monster“ (spielerseitig), „Pocket-…“, „Digi-…“, „-mon“-Endungen | **Echo** |
| Fanggeräte | „Ball“, „Kapsel“, „Fangkugel“, „werfen“ im Bindungskontext | **Siegel**, **Anschlag** |
| Enzyklopädie | „-dex“-Endung | **Echo-Kodex** |
| Abzeichen | „Orden“ für Arena-Abzeichen (auch wegen Kollision mit *Orden der Stille*) | **Akkord** |
| Aufbewahrung | „Box“, „PC“, „Lager-Box“ | **Resonanzhain** |
| Heilzentrum | „Center“, „Klinik“ als Kettenmarke | **Klangbrunnen** |
| Kampf | „KP“ als Abkürzung für Lebenspunkte | **HP** (siehe §10.4) |
| Zustände | „besiegt“ im Sinne von Tod, „getötet“, „sterben“ für Echos | **erschöpft**, **verklungen** |

„Monster“ darf in internen Produktionsdokumenten als Genrebegriff vorkommen (z. B. „Monster-Collecting-RPG“), nie im Spiel.

---

## 3. Sprachfamilien der Welt

Jede Region hat eine fiktive **Klangfamilie**, aus der Orts-, Personen- und regionale Echo-Namen gebildet werden. Damit klingt jede Region unverwechselbar, und Namen verraten dem Spieler Herkunft (S1 Lebendige Resonanz). Alle Familien sind **fiktiv**; reale Sprachen dienen nur als lautliche Anmutung und werden nie wörtlich übernommen.

| Region | Klangfamilie | Lautcharakter | Silbenmuster | Beispiele Ortsnamen | Beispiele Personennamen |
|---|---|---|---|---|---|
| R01 Verdanthain | **Linnisch** | weich, l/n/w, Diminutive | KV(K)-KV | Lindwiesen, Eichenhall, Moosgrund, Farnbrück | Ysolde, Wendel, Lorin, Maelis |
| R02 Kharsgrat | **Kharsk** | hart, k/r/g, Doppelkonsonanten | KVKK | Kharsholm, Grollschlund, Brakkfels | Torvik, Hralda, Brann |
| R03 Morvenmoor | **Morvisch** | gehaucht, v/m/h, lange Vokale | KVV-KVK | Morvenfurt, Fennhaven, Duvreth | Aoibhe → *Evhe*, Corrach, Nialla |
| R04 Sahrun-Weite | **Sahrunisch** | offen, s/r/h, a-lastig, Doppelvokale | KV-KVVK | Qasr Sahrun, Harrâd, Mirsaan | Amaru, Shirah, Tavesh |
| R05 Ignareth | **Ignar** | gerollt, r/th/x, „-eth/-ax“ | VK-KVK | Schlackenwehr, Ignareth, Vorthax | Kaldrex, Seraphe, Ithren |
| R06 Saltrand | **Saltisch** | Seemannssprache, kurze Silben, „-sund/-hafen“ | KVK | Saltrand-Hafen, Kliffsund, Tangwerft | Jonte, Marieke, Beke, Hauke |
| R07 Hvitfell | **Hvitnisch** | nordisch-kühl, hv/fj/ð | KKVK | Hvitmark, Fjallstad, Eiðvik | Sigrun, Haldor, Ylva |
| R08 Ael'Dorun | **Dorunisch (Altsprache)** | alt, Apostrophe, Vokalhäufung, „ae/ue“ | V'KVK | Ael'Dorun, Dorunsruh, Thae'Luun | Ka'Thurel, Ilen, Aevrin |
| R09 Prismtiefen | **Prismanisch** (Bergbau-Jargon + Lichtwörter) | spitz, i/y, „-ara/-yx“ | KKV-KV | Prismara, Glanzschacht, Quarzgrund | Ilyx, Brannoc, Seren |
| R10 Nimbara | **Nimbari** | luftig, Vokale, m/b/l, kaum Konsonantencluster | KV-KV-KV | Aerion, Nimbara, Lumeya | Aelia, Oruma, Siyel |

**Kulturregel (Narrative):** Keine Region ist eine 1:1-Abbildung einer realen Kultur. Kulturelle Elemente werden **gemischt und neu kombiniert**; Sensitivity-Review durch externe Berater für R04 (Wüstenkultur) und R07 (nordische Anmutung) ist Pflicht (K07).

---

## 4. Echo-Namenssystem (Morphem-Lexikon)

### 4.1 Grundregeln (LOCKED)

| # | Regel |
|---|---|
| N1 | Länge **4–10 Zeichen** (UI-Limit 12, Japanisch max. 6 Kana). |
| N2 | 1–3 Silben, aussprechbar in DE/EN/FR/ES ohne Sonderzeichen. Keine Apostrophe, Umlaute oder ß in Echo-Namen (Ausnahme: Ursprungsstimmen dürfen dorunische Apostrophe tragen). |
| N3 | Namen bestehen aus **Wurzel-Morphem** (Typ/Motiv) + **Form-Morphem** (Stufe/Gestalt). |
| N4 | Evolutionslinien teilen ein erkennbares Element (Wurzel *oder* Klangmuster), aber nie mechanisch „Name + Zahl“. |
| N5 | Keine realen Wörter einer Hauptsprache als vollständiger Name (Prüfung durch `NameGuard`). |
| N6 | Erste 4 Buchstaben einzigartig **über Evolutionslinien hinweg** (innerhalb derselben Linie erlaubt, da N4 gemeinsame Wurzeln verlangt). Lesbarkeit in Listen, Suche. |
| N7 | Namen sind **global identisch** in allen lateinischen Sprachen; Japanisch/Chinesisch/Koreanisch erhalten phonetische Transkription (ADR-022). |
| N8 | Keine Namen, die bekannte Kreaturennamen anderer Franchises zu > 60 % (normalisierte Levenshtein-Ähnlichkeit) treffen. |

### 4.2 Wurzel-Morpheme nach Typ

Jeder Typ hat 8 Wurzeln. Wurzeln dürfen frei mit Formsilben kombiniert und lautlich angepasst werden.

| Typ | Wurzeln | Assoziation |
|---|---|---|
| Glut (Ember) | `pyr`, `cind`, `emb`, `brand`, `scor`, `ign`, `fla`, `kohl` | Asche, Funke, Glimmen |
| Flut (Tide) | `mar`, `nau`, `und`, `brin`, `tid`, `rill`, `aqu`, `wel` | Welle, Salz, Quelle |
| Stein (Stone) | `brok`, `grav`, `lith`, `crag`, `kies`, `peb`, `tor`, `ston` | Fels, Kiesel, Klippe |
| Sturm (Storm) | `wisp`, `gal`, `zeph`, `volt`, `thun`, `aer`, `bri`, `skir` | Böe, Blitz, Pfeifen |
| Blüte (Bloom) | `fern`, `bloss`, `myrt`, `thorn`, `vern`, `petal`, `ros`, `moss` | Farn, Dorn, Moos |
| Frost (Frost) | `glac`, `rim`, `hvit`, `cryo`, `nive`, `isk`, `frore`, `sleet` | Reif, Eis, Weiß |
| Leere (Void) | `nul`, `vac`, `umbr`, `noct`, `hol`, `voi`, `ebb`, `nihl` | Nichts, Schatten, Sog |
| Licht (Light) | `lum`, `sol`, `glim`, `aur`, `ray`, `luc`, `shin`, `dawn` | Strahl, Glanz, Morgen |
| Gift (Venom) | `tox`, `vir`, `ven`, `mire`, `rot`, `scab`, `blight`, `spor` | Sumpf, Spore, Fäulnis |
| Metall (Metal) | `ferr`, `cobal`, `rivet`, `bras`, `forg`, `alloy`, `steel`, `tin` | Schmiede, Niete, Erz |
| Geist (Spirit) | `wraith`, `ani`, `mem`, `phan`, `shea`, `wisk`, `soul`, `lorn` | Erinnerung, Schemen |
| Kristall (Crystal) | `prism`, `quar`, `fac`, `gem`, `geo`, `shard`, `clar`, `opal` | Facette, Splitter |
| Klang (Sound) | `chim`, `hum`, `reso`, `tun`, `cant`, `bell`, `aria`, `drum` | Glocke, Summen, Lied |
| Schwerkraft (Gravity) | `mass`, `orb`, `grav`, `pond`, `tetr`, `well`, `anch`, `zen` | Anziehung, Anker, Kern |
| Arkan (Arcane) | `rune`, `glyph`, `myst`, `arc`, `sigil`, `ether`, `vex`, `aeth` | Rune, Muster, Ur-Magie |

*Hinweis:* `grav` erscheint bei Stein und Schwerkraft – zulässig, da die Form-Morpheme den Unterschied tragen (Prüfregel N6 greift trotzdem).

### 4.3 Form-Morpheme (Stufe/Gestalt)

| Funktion | Morpheme | Verwendung |
|---|---|---|
| **Stufe 1** (jung, klein) | `-let`, `-lit`, `-kin`, `-ling`, `-i`, `-o`, `-ette`, `-pip` | Basisformen |
| **Stufe 2** (Jugend, Wachstum) | `-ar`, `-en`, `-ix`, `-ward`, `-ow`, `-el`, `-una` | Mittelformen |
| **Stufe 3** (voll entwickelt, mächtig) | `-ath`, `-gor`, `-oth`, `-ion`, `-rex`, `-mire`, `-aune`, `-dral` | Endformen |
| **Einzelart** (keine Evolution) | freie Zweisilber, oft Lautmalerei | – |
| **Gestalt-Morpheme** (Körperbau) | `-wing`/`-wyn` (Flug), `-paw` (Vierbeiner), `-coil` (Schlange), `-fin` (Wasser), `-shell` (Panzer), `-hoof` (Huftier), `-mote` (Schwarm) | optional, ersetzt Stufen-Morphem |

### 4.4 Ableitungsbeispiele (verbindliche Starter)

| Linie | Stufe 1 | Stufe 2 | Stufe 3 | Konstruktion |
|---|---|---|---|---|
| Blüte-Starter | **Fernlit** | **Fernwyn** | **Verdrath** | `fern`+`lit` → `fern`+`wyn` (Gestalt Flug-Schwingen aus Blättern) → `vern`+`ath` lautlich zu *Verdrath* (Echo von *Verdanthain*) |
| Stein-Starter | **Brokk** | **Brokkar** | **Torgrath** | `brok` (+k, kharske Verdopplung) → `brok`+`ar` → `tor`+`gr`+`ath` |
| Sturm-Starter | **Wisplet** | **Galewix** | **Zephyrion** | `wisp`+`let` → `gal`+`ew`+`ix` → `zeph`+`yr`+`ion` |

Die Starter-Namen sind damit **LOCKED** (CANON §14 aktualisiert). Typen der Endstufen werden in K20 festgelegt.

### 4.5 Ursprungsstimmen & Mythische

Ursprungsstimmen tragen **dorunische Namen** (Altsprache, Apostrophe erlaubt), da sie älter sind als alle heutigen Kulturen. Mythische tragen Namen, die in **keiner** Klangfamilie wurzeln (fremd, unheimlich). Namen werden in K07 vergeben.

---

## 5. Wissenschaftliche Namen

Jede Art besitzt einen wissenschaftlichen Namen im Stil der **Akademie der Resonanz** (fiktives „Aethrisch-Latein“).

**Format:** *Genus epitheton* (kursiv), optional *Autor, Jahr* der Akademie-Zeitrechnung (n.St. = nach der Stille).

| Bestandteil | Regel | Beispiel |
|---|---|---|
| Genus | Abgeleitet vom **Archetyp** (Körperbau-Familie, K16) + lateinisierendes Suffix `-ia`, `-us`, `-ops`, `-odon`, `-therium`, `-ptera` | *Felisonia* (katzenartige Echos) |
| Epitheton | Typ- oder Verhaltensbezug, lateinisierend | *verdantis*, *cantans* (singend), *nivalis* |
| Autor | Fiktive Forschende der Akademie | *Vael, 812 n.St.* |

Beispiel: **Fernlit** – *Pteridolis cantans* Vael, 812 n.St. („singender Farnling“).

**Zeitrechnung (LOCKED):** Das aktuelle Spieljahr ist **1004 n.St.** (Jahre nach der Großen Stille).

---

## 6. Namensprüfung (Clean-Room & Marken)

Jeder neue Name (Echo, Ort, Person, Item, Fähigkeit) durchläuft eine **dreistufige Pipeline**:

```
 ┌───────────────┐    ┌────────────────────────┐    ┌──────────────────────┐    ┌───────────────┐
 │ 1. Vorschlag  │───►│ 2. NameGuard (auto)    │───►│ 3. Legal-Review      │───►│ 4. Freigabe   │
 │ (Designer im  │    │ • Regeln N1–N8         │    │ • Markenregister     │    │ → CANON /     │
 │  Name-Sheet)  │    │ • Ähnlichkeit vs. Ref- │    │   (EUIPO, USPTO, JPO)│    │   Data Table  │
 │               │    │   DB (~5.000 Namen)    │    │ • Kultur-/Slang-Check│    │               │
 │               │    │ • Wörterbücher 12 Spr. │    │   in 12 Sprachen     │    │               │
 │               │    │ • Blacklist §2.1       │    │                      │    │               │
 └───────────────┘    └──────────┬─────────────┘    └──────────┬───────────┘    └───────────────┘
                                 │ fail                         │ fail
                                 ▼                              ▼
                           zurück an Designer              zurück an Designer
```

**Durchsatzziel:** 40 Namen/Woche in P4. Puffer: 20 % Ersatznamen pro Batch.

**Slang-/Bedeutungsprüfung:** Muttersprachliche Lokalisierungsleads prüfen jeden Echo-Namen auf unerwünschte Bedeutungen (z. B. Schimpfwörter, Markenanklänge) – Pflicht vor LOCKED.

---

## 7. ID-Konventionen

IDs sind **stabil, englisch-neutral, nie wiederverwendet** (auch nicht nach Löschung). Sie sind die Grundlage für Save-Kompatibilität (K64).

| Entität | Format | Beispiel | Anmerkung |
|---|---|---|---|
| Echo-Art | `ECHO_###` | `ECHO_001` | Kodexnummer = Zahl; Updates ab 257 |
| Echo-Form (Regionalform/Zweig) | `ECHO_###_<Form>` | `ECHO_045_ASH` | Formen teilen Kodexnummer, wenn kosmetisch; eigene Nummer, wenn eigene Art |
| Aktive Fähigkeit | `ABL_A###` | `ABL_A001` | 180 |
| Passive Fähigkeit | `ABL_P###` | `ABL_P001` | 90 |
| Crescendo | `ABL_U###` | `ABL_U001` | 30 |
| Feldfähigkeit | `ABL_F###` | `ABL_F001` | 30 |
| Item | `ITM_<KAT>_<NAME>` | `ITM_SEAL_RAW`, `ITM_HEAL_TONIC_S` | KAT ∈ SEAL, HEAL, MAT, KEY, SCRIPT, GEAR, FOOD, LURE, TRAP, DECO |
| Klangschrift | `ITM_SCRIPT_##` | `ITM_SCRIPT_01` | 90 |
| Rezept | `RCP_<KAT>_<NAME>` | `RCP_HEAL_TONIC_S` | – |
| Region | `R##` | `R01` | 10 |
| Zone | `R##_Z##` | `R02_Z05` | Subregionen für Spawns/Level |
| Siedlung | `SET_<C|V|O>_<NAME>` | `SET_C_EICHENHALL`, `SET_V_LINDWIESEN`, `SET_O_FARNWACHT` | C=Stadt, V=Dorf, O=Außenposten |
| POI | `POI_R##_####` | `POI_R01_0042` | – |
| Resonanzstein | `RST_R##_##` | `RST_R01_03` | – |
| NPC | `NPC_<NAME>` bzw. `NPC_R##_<NAME>` | `NPC_YSOLDE`, `NPC_R01_WENDEL` | Hauptfiguren ohne Region |
| Hauptquest | `MQ_A#_##` | `MQ_A1_04` | Akt + Nummer; Prolog = `MQ_A0_##` |
| Nebenquest | `SQ_###` | `SQ_001` | 210 |
| Fraktionsquest | `FQ_F##_##` | `FQ_F03_02` | zählt zu den 210, wenn optional (Mapping-Tabelle K48) |
| Auftrag | `CT_R##_##` | `CT_R04_07` | wiederholbar |
| Dialog | `DLG_<QuestId>_<##>` | `DLG_MQ_A1_04_03` | – |
| Wetter | `W##` + Tag | `W03` / `Weather.Thunderstorm` | – |
| Typ | `T##` + Tag | `T13` / `Type.Sound` | – |
| Fraktion | `F##` + Tag | `F05` / `Faction.Order` | – |
| Arena | `ARN_##` | `ARN_01` (Eichenhall) | Reihenfolge = Akkord-Stufe nicht fix (K02) |
| Raid-Boss | `RAID_##` | `RAID_01` | – |
| Tiefenresonanz | `DR_##` | `DR_01` | Dungeon |
| Genom-Locus | `GEN_<NAME>` | `GEN_COLOR_BASE` | K38 |
| Statuszustand | `STS_<NAME>` + Tag | `STS_BURN` / `Status.Burn` | K32 |
| Terrain | `TER_<NAME>` + Tag | `TER_OVERGROWTH` / `Terrain.Overgrowth` | K32 |
| Telemetrie-Event | `domain.object.verb` | `combat.end` | K02 §12 |

**Instanz-IDs** (Laufzeit, gespeichert): `FGuid` (Echo-Instanzen, Item-Stacks mit Herkunft, Fotos).

---

## 8. GameplayTag-Hierarchie

Wurzel-Tags sind **LOCKED**; Unter-Tags werden von den Fachkapiteln ergänzt. Tags werden in `Config/Tags/*.ini` pro Plugin gepflegt (eine Datei pro Wurzel).

```
Type.                 Ember, Tide, Stone, Storm, Bloom, Frost, Void, Light, Venom,
                      Metal, Spirit, Crystal, Sound, Gravity, Arcane
Stat.                 HP, Attack, Defense, SpAttack, SpDefense, Speed, Precision, Evasion
Status.               (K32)  z. B. Status.Burn, Status.Silenced …
Terrain.              (K32)
Weather.              Clear, Rain, Thunderstorm, Fog, Snow, Heatwave, Sandstorm,
                      Aurora, Ashfall, ResonanceStorm
TimeOfDay.            Dawn, Day, Dusk, Night
Region.               R01 … R10   (+ Region.R01.Z01 … für Zonen)
Biome.                Forest, Mountain, Swamp, Desert, Volcano, Coast, Snow, Ruins, Crystal, Sky
Faction.              Academy, Goldklang, Wildwatch, FreeVoices, Order
Ability.              Active, Passive, Crescendo, Field  (+ Ability.Category.*, K28)
Ability.Range.        Melee, Ranged, Area, Self, Ally   (K33)
Formation.            Front, Back
Combat.Format.        Duel, Duo, Trio, Raid
Item.                 Seal, Heal, Material, Key, Script, Gear, Food, Lure, Trap, Deco
Niche.                Combat, Field, Breeding, Research, Mount
Mount.                Ground, Swim, Climb, Dig, Fly
Behavior.             (K52) z. B. Behavior.Diurnal, Behavior.Territorial, Behavior.Herd …
Personality.          (K18)
Temperament.          (K18)
Feature.              Combat.Duo, Combat.Trio, Breeding, Raid, Ranked, … (Freischaltungen)
GameFlow.             (K03)
Event.                (Event-Bus-Kanäle, K06)
Quest.                (K48)
Input.                (Enhanced Input Actions, K54)
Cheat./Debug.         (nur Development-Builds)
```

**Regel:** Kein Code vergleicht Strings für diese Konzepte; immer `FGameplayTag`. Native Tags werden in `AethrisCore/AethrisTags.h` über `UE_DECLARE_GAMEPLAY_TAG_EXTERN` deklariert (K06).

---

## 9. Asset- und Dateibenennung

Basierend auf der verbreiteten UE-Präfixkonvention, ergänzt um Projektregeln.

| Asset | Präfix | Beispiel |
|---|---|---|
| Blueprint | `BP_` | `BP_Echo_Base` |
| Data Asset (Definition) | `DA_` | `DA_Echo_001_Fernlit` |
| Data Table | `DT_` | `DT_WardenRank` |
| Curve Table / Curve | `CT_` / `CV_` | `CT_GrowthRates` |
| Static Mesh | `SM_` | `SM_R01_Oak_Large_01` |
| Skeletal Mesh | `SK_` | `SK_Echo_001_Fernlit` |
| Skeleton | `SKEL_` | `SKEL_Archetype_Quadruped_S` |
| Animation Sequence | `AS_` | `AS_Echo_001_Idle_01` |
| Animation Blueprint | `ABP_` | `ABP_Archetype_Quadruped` |
| Montage | `AM_` | `AM_Echo_001_Ability_A012` |
| Material / Instance | `M_` / `MI_` | `MI_Echo_001_Body_Morph02` |
| Texture | `T_` + Suffix `_D/_N/_ORM/_E/_M` | `T_Echo_001_Body_D` |
| Niagara System | `NS_` | `NS_Ability_A012_Impact` |
| MetaSound Source | `MSS_` | `MSS_Echo_001_Call` |
| Sound Wave | `SW_` | `SW_Amb_R03_Night_Loop_01` |
| Widget | `WBP_` | `WBP_Combat_Timeline` |
| Level / Level Instance | `L_` / `LI_` | `L_Aethris_World`, `LI_SET_C_Eichenhall` |
| PCG Graph | `PCG_` | `PCG_R01_Forest_Understory` |
| StateTree | `ST_` | `ST_NPC_Villager` |
| Behavior Tree / Blackboard | `BT_` / `BB_` | `BT_Echo_Territorial`, `BB_Echo` |
| Gameplay Ability / Effect | `GA_` / `GE_` | `GA_A012_EmberBite`, `GE_Status_Burn` |

**Ordnerstruktur:** Assets eines Feature-Plugins liegen ausschließlich in dessen Content-Ordner (`/GF_Monsters/Echos/001_Fernlit/…`). Region-Content liegt unter `/Game/World/R01_Verdanthain/…`. Details K05.

---

## 10. Text-Stilrichtlinie

### 10.1 Tonalität

| Dimension | Ziel | Nicht |
|---|---|---|
| Grundton | Warm, staunend, geheimnisvoll | Zynisch, ironisch-distanziert |
| Humor | Leise, situativ, oft durch Echos | Meta-Witze, Popkultur-Referenzen |
| Bedrohung | Unheimlich durch **Stille** und Abwesenheit | Gore, Grausamkeit (PEGI 7) |
| Dialoglänge | ≤ 3 Zeilen pro Textbox, ≤ 160 Zeichen | Textwände |
| Wortwahl | Klang-Metaphorik bewusst dosiert (max. 1 Klangmetapher pro Dialogzeile) | Klang-Kalauer in jedem Satz |

### 10.2 Fraktionsstimmen

| Fraktion | Sprachstil | Beispielzeile |
|---|---|---|
| Akademie der Resonanz | Präzise, neugierig, Fachbegriffe, spricht in Hypothesen | „Wenn die Frequenz hier abfällt, müssen wir die Ursache flussaufwärts vermuten.“ |
| Goldklang-Kontor | Freundlich-geschäftstüchtig, Zahlen, Sprichwörter des Handels | „Ein guter Handel klingt für beide Seiten richtig – und meiner etwas lauter.“ |
| Wildwacht | Knapp, naturnah, praktisch | „Wind dreht. Die Herde zieht ab. Wir auch.“ |
| Freie Stimmen | Leidenschaftlich, misstrauisch gegenüber Institutionen | „Wer bestimmt, welche Stimme klingen darf? Niemand.“ |
| Orden der Stille | Ruhig, sanft, fast tröstend – darum unheimlich | „Hörst du, wie friedlich es wird, wenn alles schweigt?“ |

### 10.3 Ansprache

- Der Spieler wird in NPC-Dialogen **geduzt**, außer von formellen Akademie-Würdenträgern (gesiezt, „Wärter[in]“).
- Systemtexte: Imperativ, kurz („Halte LT, um zu lauschen.“).

### 10.4 Schreibweisen (LOCKED)

| Element | Regel |
|---|---|
| Werte-Abkürzungen | HP, ANG (Angriff), VER (Verteidigung), SAN (Spezialangriff), SVE (Spezialverteidigung), GES (Geschwindigkeit), PRÄ (Präzision), AUS (Ausweichen) |
| Typnamen | Immer großgeschrieben als Eigennamen: „ein Glut-Echo“, „Klang-Fähigkeit“ |
| Echo-Namen | Ohne Artikel im Fließtext, wo möglich („Fernlit springt.“); Genus grammatisch **neutrum** („das Echo“) |
| Zahlen | Ziffern ab 10, Tausenderpunkt („1.000“), Sol mit ◎ nach der Zahl („250 ◎“) |
| Zeit | Spielzeit „Tag/Nacht“ in Texten, keine Uhrzeiten außer im Uhr-UI |

### 10.5 Spielercharakter & Pronomen

Der Charakter-Editor bietet **Ansprache** (unabhängig vom Körpermodell): *er*, *sie*, *neutral* (Name statt Pronomen, im Deutschen über Umformulierung gelöst). Alle Dialogzeilen mit Spielerbezug werden in **drei Varianten** geschrieben bzw. so formuliert, dass sie neutral funktionieren (bevorzugt). Das Lokalisierungssystem unterstützt Variablen `{Player.Pronoun.Subject}` etc. (§11).

---

## 11. Lokalisierungskonventionen

| Thema | Entscheidung |
|---|---|
| Sprachen Text (12) | DE, EN, FR, ES (EU), ES (LatAm), IT, PT-BR, PL, JA, KO, ZH-Hans, ZH-Hant |
| Sprachen Vertonung (5) | DE, EN, JA, FR, ES |
| Quellsprache | **Deutsch** für Design und Erzählung, **Englisch** als Pivot für Übersetzung (beide Master-Texte durch Narrative-Team gepflegt) |
| String Tables | Pro Domäne: `ST_Echos`, `ST_Abilities`, `ST_Items`, `ST_Quest_<Id>`, `ST_UI`, `ST_World` |
| Key-Format | `<Domäne>.<Id>.<Feld>` – z. B. `Echos.ECHO_001.Name`, `Echos.ECHO_001.Kodex.L3`, `Abilities.ABL_A012.Desc` |
| Variablen | `{Name}`-Syntax mit Formatierungsfunktionen (Plural, Genus) via ICU/FText-Argumente |
| Genus-Handling | `FText`-Gender-Argumente (`ETextGender`) für Spieler und benannte NPCs; Echos grammatisch neutrum (DE), Sprachen ohne Neutrum per Fallback-Regel im Style-Guide der Sprache |
| Textlängen | +35 % Pufferregel für UI (DE/FR/PL am längsten), Pseudo-Lokalisierung ab P2 im CI |
| Kontext | Jeder String hat Kontext-Kommentar + automatisierten Screenshot (Risiko R-12) |
| Echo-Namen | Global identisch (lat. Schrift), CJK phonetisch transkribiert (ADR-022) |
| Fähigkeits-/Itemnamen | Werden **übersetzt** (beschreibend) |

---

## 12. Werkzeuge & Code

### 12.1 NameGuard (Python-Tool, CI-Stufe)

```python
# Tools/NameGuard/nameguard.py
"""
NameGuard – prüft Namensvorschläge gegen die Regeln N1–N8 (K04 §4.1).
Eingabe: CSV mit Spalten id,name,kind (echo|place|person|item|ability) und optional line (Evolutionslinie)
Ausgabe: Bericht (Markdown) + Exitcode != 0 bei Verstößen (CI-Gate).
"""
from __future__ import annotations
import csv, sys, unicodedata
from dataclasses import dataclass
from pathlib import Path

REFERENCE_DB = Path(__file__).with_name("reference_names.txt")  # ~5.000 Fremdnamen (Legal pflegt)
BLACKLIST = Path(__file__).with_name("blacklist.txt")           # verbotene Begriffe (§2.1)
DICTIONARIES = Path(__file__).with_name("dicts")                # Wortlisten 12 Sprachen

@dataclass
class Finding:
    rule: str
    message: str

def normalized(s: str) -> str:
    """Kleinbuchstaben, ohne Diakritika – Basis für Ähnlichkeitsvergleich."""
    nfkd = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def similarity(a: str, b: str) -> float:
    """Normalisierte Levenshtein-Ähnlichkeit 0..1."""
    a, b = normalized(a), normalized(b)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return 1.0 - prev[-1] / max(len(a), len(b), 1)

def check_echo_name(name: str, others: list[str], refs: list[str], words: set[str]) -> list[Finding]:
    """others = Namen anderer Linien (N6 gilt nur linienübergreifend)."""
    f: list[Finding] = []
    if not 4 <= len(name) <= 10:
        f.append(Finding("N1", f"Länge {len(name)} außerhalb 4–10"))
    if not name.isascii() or not name.isalpha():
        f.append(Finding("N2", "Nur ASCII-Buchstaben erlaubt (keine Umlaute/Apostrophe)"))
    if normalized(name) in words:
        f.append(Finding("N5", "Name ist ein reales Wort einer Zielsprache"))
    prefix = normalized(name)[:4]
    clash = [o for o in others if normalized(o)[:4] == prefix]
    if clash:
        f.append(Finding("N6", f"Präfix '{prefix}' bereits vergeben: {', '.join(clash)}"))
    worst = max(refs, key=lambda r: similarity(name, r), default=None)
    if worst and similarity(name, worst) > 0.60:
        f.append(Finding("N8", f"Zu ähnlich zu Referenzname (Ähnlichkeit {similarity(name, worst):.2f})"))
    return f

def main(csv_path: str) -> int:
    refs = REFERENCE_DB.read_text(encoding="utf-8").split() if REFERENCE_DB.exists() else []
    words = set()
    if DICTIONARIES.exists():
        for d in DICTIONARIES.glob("*.txt"):
            words |= {normalized(w) for w in d.read_text(encoding="utf-8").split()}
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
    failed = 0
    for r in rows:
        if r["kind"] != "echo":
            continue
        line = r.get("line") or r["id"]
        others = [o["name"] for o in rows
                  if o["kind"] == "echo" and o["name"] != r["name"] and (o.get("line") or o["id"]) != line]
        for finding in check_echo_name(r["name"], others, refs, words):
            failed += 1
            print(f"- **{r['id']} {r['name']}** · {finding.rule}: {finding.message}")
    print(f"\n{len(rows)} Namen geprüft, {failed} Verstöße.")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
```

Das Tool liegt ab diesem Kapitel unter `tools/nameguard/nameguard.py` im Repository und wird in den Katalog-Kapiteln K20–K27 gegen alle Echo-Namen ausgeführt.

### 12.2 ID-Validierung in UE (Data Validation)

```cpp
// AethrisEditor/Validation/AethrisIdValidator.cpp (Auszug)
// Prüft Primary Asset IDs gegen die Formate aus K04 §7.
static const TMap<FPrimaryAssetType, FRegexPattern> GIdPatterns = {
    { FPrimaryAssetType(TEXT("EchoSpecies")), FRegexPattern(TEXT("^ECHO_\\d{3}(_[A-Z]+)?$")) },
    { FPrimaryAssetType(TEXT("Ability")),     FRegexPattern(TEXT("^ABL_[APUF]\\d{3}$")) },
    { FPrimaryAssetType(TEXT("Item")),        FRegexPattern(TEXT("^ITM_[A-Z]+_[A-Z0-9_]+$")) },
    { FPrimaryAssetType(TEXT("Quest")),       FRegexPattern(TEXT("^(MQ_A\\d_\\d{2}|SQ_\\d{3}|FQ_F\\d{2}_\\d{2})$")) },
};

EDataValidationResult UAethrisIdValidator::ValidateLoadedAsset_Implementation(
    const FAssetData& AssetData, UObject* Asset, FDataValidationContext& Context)
{
    const UPrimaryDataAsset* PDA = Cast<UPrimaryDataAsset>(Asset);
    const FPrimaryAssetId Id = PDA->GetPrimaryAssetId();
    if (const FRegexPattern* Pattern = GIdPatterns.Find(Id.PrimaryAssetType))
    {
        FRegexMatcher M(*Pattern, Id.PrimaryAssetName.ToString());
        if (!M.FindNext())
        {
            AssetFails(Asset, FText::Format(
                NSLOCTEXT("Aethris", "BadId", "ID '{0}' verletzt K04 §7."),
                FText::FromName(Id.PrimaryAssetName)));
            return EDataValidationResult::Invalid;
        }
    }
    AssetPasses(Asset);
    return EDataValidationResult::Valid;
}
```

### 12.3 Gestrichene IDs

Gelöschte Inhalte werden in `Data/Meta/RetiredIds.csv` eingetragen. Der Validator verhindert Wiederverwendung (Save-Kompatibilität, K64).

---

## 13. Decision Records

### ADR-022 – Echo-Namen global identisch
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Pro Sprache lokalisierte Namen | Wortspiele je Sprache | 256 × 11 Namensprüfungen, Community spricht aneinander vorbei, PvP/Tausch international verwirrend |
| (b) Global identisch (lat.), CJK transkribiert | Eine Prüfung, globale Community, Marketing einheitlich | Keine sprachspezifischen Wortspiele |
- **Entscheidung:** (b). Fiktive Morpheme sind ohnehin sprachneutral konstruiert.

### ADR-023 – Deutsch als Design-Quellsprache, Englisch als Übersetzungspivot
- **Kontext:** Kernteam arbeitet deutsch; Übersetzer-Markt arbeitet primär aus dem Englischen.
- **Entscheidung:** Narrative schreibt DE, ein internes Team pflegt die englische Master-Fassung parallel (nicht nachträglich). **Nachteil:** doppelter Schreibaufwand (~+15 % Narrative-Kosten). **Vorteil:** höhere Qualität aller 11 Übersetzungen, keine Qualitätsverluste durch Doppelübersetzung.

### ADR-024 – Zeitrechnung „n.St.“, Spieljahr 1004
- **Entscheidung:** Jahreszahlen relativ zur Großen Stille; Gegenwart 1004 n.St. („~1.000 Jahre“ aus K01 bleibt gültig).

### ADR-025 – Neutrum für Echos
- **Entscheidung:** Echos sind grammatisch Neutrum („das Echo“, „es“). Bindungs-/Persönlichkeitstexte vermitteln Individualität über Verhalten, nicht über Pronomen. Vorteil: konsistente Lokalisierung, keine Geschlechtszuschreibung für Kreaturen (Zucht-Genetik ist geschlechtsunabhängig, K38).

---

## 14. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §21 | Glossar (§2) inkl. Code-Bezeichner; verbotene Begriffe (§2.1) | LOCKED |
| §21 | Neue Begriffe: Anlagen, Aufträge, Einklang, Einstimmen, Verstummt | LOCKED |
| §22 | 10 Klangfamilien der Regionen | LOCKED |
| §22 | Namensregeln N1–N8, Morphem-Lexikon (§4.2/§4.3) | LOCKED |
| §22 | Starterlinien: **Fernlit → Fernwyn → Verdrath**, **Brokk → Brokkar → Torgrath**, **Wisplet → Galewix → Zephyrion** | LOCKED (Namen) |
| §22 | Wissenschaftliche Namen: Aethrisch-Latein, Autor + Jahr n.St. | LOCKED |
| §22 | Zeitrechnung n.St., Gegenwart 1004 n.St. | LOCKED |
| §23 | ID-Formate (§7), Tag-Wurzeln (§8), Asset-Präfixe (§9) | LOCKED |
| §23 | `Data/Meta/RetiredIds.csv` – IDs nie wiederverwenden | LOCKED |
| §24 | Tonalität, Fraktionsstimmen, Werte-Abkürzungen (HP, ANG, VER, SAN, SVE, GES, PRÄ, AUS), Schreibweisen | LOCKED |
| §24 | Spieler-Ansprache er/sie/neutral | LOCKED |
| §24 | 12 Textsprachen, 5 Vertonungssprachen, Key-Format | LOCKED |
| §24 | Echos grammatisch Neutrum; Zucht geschlechtsunabhängig | LOCKED |
| §10 | ADR-022 – ADR-025 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Glossar mit über 60 Begriffen inkl. Code-Bezeichnern
- [x] Clean-Room-Blacklist verbotener Begriffe
- [x] 10 fiktive Klangfamilien (Orts-/Personennamen pro Region)
- [x] Namensregeln N1–N8, Morphem-Lexikon (15 Typen × 8 Wurzeln, Stufen- und Gestaltmorpheme)
- [x] Starterlinien-Namen final (9 Echos)
- [x] Wissenschaftliche Namenskonvention, Zeitrechnung 1004 n.St.
- [x] Dreistufige Namensprüfungs-Pipeline
- [x] ID-Formate für alle Entitäten, Retired-ID-Regel
- [x] GameplayTag-Wurzelhierarchie
- [x] Asset-Präfixe und Ordnerregel
- [x] Text-Stilrichtlinie, Fraktionsstimmen, Schreibweisen, Pronomen-System
- [x] Lokalisierungskonventionen (12/5 Sprachen, Keys, Genus, Pseudo-Loc)
- [x] Code: NameGuard (Python, im Repo), ID-Validator (UE)
- [x] ADR-022 – ADR-025, CANON aktualisiert

➡️ **Nächstes Kapitel: K05 – TDD I: Engine-Setup, Modul- & Projektstruktur, Coding Standards.**
