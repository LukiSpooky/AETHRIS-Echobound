# K11 · Städte I – Eichenhall, Kharsholm, Morvenfurt, Qasr Sahrun, Saltrand-Hafen

| Feld | Wert |
|---|---|
| Dokument | Kapitel 11 von 68 · World Bible, Teil V |
| Version | 1.0 |
| Owner | Level Designer (City Lead) |
| Mitwirkende | Narrative Writer, Quest Designer, Audio Director, AI Engineer (NPC-Tagesabläufe), Economy Designer, Combat Designer (Arenen) |
| Baut auf | K03 §3 (Dienste), K07 (Chronik, Kultur), K08 §5 (Lage), K09/K10 (Biome) |
| Status | ✅ Freigegeben |
| Im Repository angelegt | `Data/World/Settlements.csv` (alle 62 Siedlungen), `Data/World/Arenas.csv` (alle 10 Arenen), `Data/Economy/Merchants.csv` (Städte dieses Kapitels) |
| Neue Kanon-Einträge | CANON §51 (Stadt-Template, Arena-System, Arenameister), §52 (Städte I), §53 (Bevölkerungsdarstellung) |

---

## Inhalt

1. [Stadt-Template](#1-stadt-template)
2. [Arena-System (gilt für alle 10 Arenen)](#2-arena-system-gilt-für-alle-10-arenen)
3. [Bevölkerungsdarstellung & Tagesabläufe](#3-bevölkerungsdarstellung--tagesabläufe)
4. [Eichenhall (R01)](#4-eichenhall-r01)
5. [Kharsholm (R02)](#5-kharsholm-r02)
6. [Morvenfurt (R03)](#6-morvenfurt-r03)
7. [Qasr Sahrun (R04)](#7-qasr-sahrun-r04)
8. [Saltrand-Hafen (R06)](#8-saltrand-hafen-r06)
9. [Code & Daten](#9-code--daten)
10. [Decision Records](#10-decision-records)
11. [Kanon-Updates](#11-kanon-updates)
12. [Kapitel-Checkliste](#12-kapitel-checkliste)

---

## 1. Stadt-Template

Das Briefing verlangt für jede Stadt: **Architektur, Geschichte, Händler, Arena, Quests, Musik, Einwohner mit Tagesablauf.** Jede der zehn Städte (K11/K12) wird mit diesem Template beschrieben:

| Block | Inhalt |
|---|---|
| Steckbrief | Region, Einwohner (Lore) / dargestellte NPCs, Fläche, Regierung, Fraktionspräsenz |
| Geschichte | Gründung, Wendepunkte (konsistent mit CANON §35), heutige Lage |
| Architektur & Layout | Stil, Materialien, Viertel (ASCII-Plan), Wahrzeichen, Traversal in der Stadt |
| Dienste | gemäß Siedlungsmatrix (K03 §3) |
| Händler | Liste (Daten: `Merchants.csv`) mit Öffnungszeiten und Besonderheiten |
| Arena | Arenameister, Spezialtyp, Arena-Eigenregel, Stufe |
| Quests | Hauptquest-Bezug, Nebenquest-Haken, Fraktionsquests |
| Musik | Stadtthema, Instrumentierung, Tag/Nacht-Variante, Arena-Variante |
| Einwohner | Schlüssel-NPCs mit Tagesablauf, Massenverhalten, Feste |

---

## 2. Arena-System (gilt für alle 10 Arenen)

### 2.1 Grundregeln (LOCKED)

| Regel | Festlegung |
|---|---|
| Aufbau | Jede Arena: **Vorprüfung** (2–3 Arena-Wärter, Format der Stufe) + **Arenameister**; Vorprüfung optional überspringbar nach einmaligem Sieg (Wiederholung) |
| Stufe | Gemäß CANON §15: Eichenhall fest Stufe 1, Prismara 9, Aerion 10; alle anderen skaliert nach Akkordzahl **beim ersten Betreten der Arena** (nicht der Region) – danach fixiert |
| Teamregeln | Spieler-Chor wie in der Oberwelt; keine Itemverbote; Gehorsamsregel gilt (CANON §18) |
| Arena-Eigenregel | Jede Arena hat eine **Feldregel** (Terrain/Umwelt-Mechanik), die den Spezialtyp des Meisters begünstigt, aber vom Spieler genutzt werden kann (DR-09: kein Pflichtwissen auf Standard) |
| Niederlage | Rückklang vor die Arena („Erneut versuchen“, K02 §11.2); Vorprüfung muss nicht wiederholt werden |
| Belohnung | **Akkord** + Klangschrift (Spezialtyp) + Sol + Wärter-EP + Erhöhung Gehorsamsgrenze (20 + 8 × Akkorde) |
| Revanche | Nach Story-Ende: **Meisterrunde** auf Level 75–85 (Endgame, K62) |
| Story-Kopplung | Nach dem Akkord öffnet der Meister die **Schlafstätte** der Ursprungsstimme (ab W4 erzählerisch erklärt, vorher als „Tradition“) |

### 2.2 Die zehn Arenameister (LOCKED)

| ID | Stadt | Meister | Spezialtyp | Feldregel | Persönlichkeit |
|---|---|---|---|---|---|
| ARN_01 | Eichenhall | **Maelis Wendt** | Blüte | Überwuchs | Ysoldes Schülerin und Nachfolgerin; warm, geduldig, testet Einfallsreichtum |
| ARN_02 | Kharsholm | **Torvik Hrall** | Stein / Schwerkraft | Wandernde Plattformen | Klanführer, wortkarg, Ehre über alles |
| ARN_03 | Morvenfurt | **Evhe Corrach** | Gift / Geist | Moornebel | Moorweise, rätselhaft, sympathisiert heimlich mit den Freien Stimmen |
| ARN_04 | Qasr Sahrun | **Shirah Harrâd** | Licht | Sonnenspiegel | Gastgeberin und Wahrheitsrichterin; kämpft nur nach Sonnenuntergang |
| ARN_05 | Schlackenwehr | **Kaldrex Vorn** | Glut / Metall | Schmiedeglut | Zunftmeister, laut, herzlich (K12) |
| ARN_06 | Saltrand-Hafen | **Beke Tamsen** | Flut / Sturm | Gezeitenbecken | Kapitänin a. D., Goldklang-nah, Wettfreudig |
| ARN_07 | Hvitmark | **Sigrun Fjall** | Frost | Spiegeleis | Gletscherführerin, verlor Familie in der Klangpest (K12) |
| ARN_08 | Dorunsruh | **Aevrin Thal** | Arkan | Glyphenfeld | Akademie-Professor, Venns Kollege – Zeuge des Verrats (K12) |
| ARN_09 | Prismara | **Ilyx Brannoc** | Kristall | Lichtbrechung | Kristallstimmerin, Nachfahrin Brannocs der Lauscherin (K12) |
| ARN_10 | Aerion | **Oruma Siyel** | Klang / Licht | Sternenfall | Hüterin Aeth'rions, Bewahrerin des Erstchor-Wissens (K12) |

**Arena-ID = Regionsnummer** (ARN_04 = Qasr Sahrun in R04, ARN_06 = Saltrand-Hafen in R06). Daten: `Data/World/Arenas.csv`.

### 2.3 Feldregeln (Spezifikation; Kampfmechanik-Anbindung in K32)

| Feldregel | Tag | Wirkung | Spieler-Gegenspiel |
|---|---|---|---|
| Überwuchs | `Arena.Rule.Overgrowth` | Alle 3 Züge wächst Terrain *Überwuchs* auf einer zufälligen Reihe (+Heilung/Zug für Blüte, −10 % GES für Nicht-Blüte) | Glut-Fähigkeiten brennen Überwuchs ab; Positionswechsel |
| Wandernde Plattformen | `Arena.Rule.ShiftingPlatforms` | Alle 4 Züge tauschen Vorder- und Hinterreihe beider Seiten automatisch | Zeitleiste zeigt den Tausch (DR-06); Fernkämpfer vorplanen |
| Moornebel | `Arena.Rule.Mist` | Ausweichen +1 Stufe für alle; Ziele in der Hinterreihe sind „verborgen“ (nur Bereichsangriffe) | Licht/Sturm-Fähigkeiten lichten den Nebel für 2 Züge |
| Sonnenspiegel | `Arena.Rule.SunMirrors` | Licht-Fähigkeiten treffen zusätzlich ein zweites Ziel (60 % Schaden) | Spiegel per Angriff (Stein/Metall) für 3 Züge zerstören |
| Schmiedeglut | `Arena.Rule.ForgeHeat` | Terrain *Glutboden* dauerhaft; Nicht-Glut-Echos erhalten pro Zug 3 % Max-HP Schaden in der Vorderreihe | Flut/Frost kühlen eine Reihe für 3 Züge |
| Gezeitenbecken | `Arena.Rule.Tide` | Wechselt alle 3 Züge zwischen Ebbe (+GES für Stein/Boden) und Flut (+SAN für Flut, Bodenangriffe −30 %) | Phase steht auf der Zeitleiste |
| Spiegeleis | `Arena.Rule.Ice` | Positionswechsel kosten 50 % weniger Zeit; Rückstoß-Effekte verdoppelt | Stein/Metall sind standfest |
| Glyphenfeld | `Arena.Rule.Glyphs` | Alle 5 Züge kehrt sich die Typtabelle für 1 Zug um (stark ↔ schwach) | Zeitleiste kündigt Umkehr an; Arkan-Echos des Spielers sind immun |
| Lichtbrechung | `Arena.Rule.Refraction` | Spezialangriffe werden zu 25 % auf ein zufälliges anderes Ziel gebrochen | Präzision ≥ Zielwert verhindert Brechung |
| Sternenfall | `Arena.Rule.Starfall` | Alle 4 Züge fällt ein Stern auf die Reihe mit den meisten Echos (Schaden + Harmonie +15 für die getroffene Seite) | Formation verteilen oder bewusst Harmonie nehmen |

**Design-Absicht:** Jede Feldregel ist eine *Lektion* über ein Kampfsystem (Terrain, Formation, Ausweichen, Mehrfachziel, Schaden über Zeit, Phasen, Zeitkosten, Typtabelle, Präzision, Harmonie). Die Reihenfolge der Akt-I-Arenen ist frei – daher ist jede Lektion für sich verständlich.

---

## 3. Bevölkerungsdarstellung & Tagesabläufe

### 3.1 Lore-Einwohner vs. dargestellte NPCs (LOCKED)

| Stadt | Einwohner (Lore) | Benannte NPCs (Actor + StateTree) | Ambient-NPCs (Mass Crowd) | Gleichzeitig sichtbar (PS5 / Switch 2) |
|---|---|---|---|---|
| Eichenhall | 9.000 | 48 | 220 | 140 / 70 |
| Kharsholm | 6.500 | 40 | 180 | 120 / 60 |
| Morvenfurt | 5.000 | 42 | 160 | 110 / 55 |
| Qasr Sahrun | 7.500 | 44 | 200 | 130 / 65 |
| Saltrand-Hafen | 11.000 | 52 | 260 | 160 / 80 |

**Prinzip:** Ambient-NPCs sind Mass-Entitäten mit Zone Graph (K06 §13); in < 25 m Spielerentfernung werden sie zu leichten Actors mit Barks und Blick-Reaktionen. Benannte NPCs haben vollständige Tagesabläufe (K53).

### 3.2 Tagesablauf-Muster

Spielzeit-Stunden (24 h = 72 min, CANON §4.3). Muster werden pro NPC-Rolle als StateTree-Daten vergeben; benannte NPCs können Abweichungen haben.

| Muster | 0–5 | 5–8 | 8–12 | 12–14 | 14–18 | 18–22 | 22–24 |
|---|---|---|---|---|---|---|---|
| **Tagwerk** (Händler, Handwerk) | Schlafen | Aufstehen, Frühstück | Arbeit | Mittag (Gasthaus) | Arbeit | Freizeit, Taverne | Schlafen |
| **Schicht A/B/C** (Kharsholm) | C arbeitet | A beginnt 6 Uhr | A | A | B ab 14 | B | C ab 22 |
| **Nachtvolk** (Morvenfurt, Qasr Sahrun) | Markt/Arbeit | Heimkehr | Schlafen | Schlafen | Aufstehen | Arbeit | Arbeit |
| **Wache/Wildwacht** | Patrouille (Nacht) | Wachwechsel | Patrouille | Pause | Patrouille | Wachwechsel | Patrouille |
| **Gelehrt** (Akademie) | Lesen/Schlaf | Schlafen | Vorlesung | Mensa | Labor | Bibliothek | Lesen |

Unterbrechungen durch Wetter (Regen → Unterstände), Ereignisse (Kampf in der Nähe → Zuschauen/Flüchten, K53) und Feste.

---

## 4. Eichenhall (R01)

### 4.1 Steckbrief

| Feld | Wert |
|---|---|
| Region / Lage | R01 Verdanthain, 2,6 / 4,8 km |
| Einwohner | 9.000 (Lore) |
| Regierung | Stadtrat (7 Räte) + Sitz des **Bundesrats** (CANON §36) |
| Fraktionen | **Wildwacht-Hauptsitz** (F03), Akademie-Außenstelle (F01), Kontor-Filiale (F02) |
| Arena | ARN_01, Maelis Wendt (Blüte), **fest Stufe 1** |
| Ursprungsstimme | Sylv'anor – unter der Arena (Wurzelhalle) |
| Fantasie | *„Die erste Stadt fühlt sich an wie eine Umarmung.“* |

### 4.2 Geschichte

| Jahr | Ereignis |
|---|---|
| 287 n.St. | Brannoc die Lauscherin rastet am Wurzelhain – Gründungslegende der Wildwacht |
| 312 n.St. | Gründung als Markt um den Wurzelhain |
| 703 n.St. | Während der Siegelkriege neutral; Zufluchtsort |
| 710 n.St. | Unterzeichnung des **Bundesvertrags** im Rathaus („Lindentisch“); Sitz des Bundesrats |
| 880 n.St. | Erste Arena des Weltakkords (Wendelin Aar) – Eichenhall ist Akkord 1 |
| 989–996 n.St. | Ysolde Varn ungeschlagene Arenameisterin |
| 1001 n.St. | Erste Stillezone in Verdanthain; Wildwacht im Ausnahmezustand |

### 4.3 Architektur & Layout

Stil: **Linnisches Fachwerk** mit Moosdächern, gebogene Holzbalken, Wurzelbrücken; im Zentrum die Riesenlinde, deren Wurzeln Gassen überspannen. Laternen aus Glockenblüten-Glas.

```
                         N
        ┌─────────────────────────────────────────┐
        │  WILDWACHT-VIERTEL   ║   AKADEMIE-      │
        │  (HQ, Ställe, Übungs-║   AUSSENSTELLE   │
        │   platz)             ║   (Bibliothek)   │
        │═══════ Wurzelbrücke ═╬═══════════════════│
        │                ╔═════╩═════╗             │
   W ───┤  HANDWERKER-   ║ WURZELHAIN║  MARKT-     ├─── O (Straße nach
 (Weg   │  GASSE         ║  (Linde,  ║  PLATZ      │      Morvenfurt)
 nach   │  (Harzhaus,    ║  Arena in ║  (Händler,  │
 Salt-  │   Schnitzerei) ║  den Wur- ║  Rathaus,   │
 rand)  │                ║  zeln)    ║  Kontor)    │
        │════════════════╚═══════════╝═════════════│
        │  WOHNVIERTEL      │ GASTHAUS │ KLANG-     │
        │  (Fachwerk)       │ Wurzelkrug│ BRUNNEN   │
        └─────────────────────────────────────────┘
                         S (Weg nach Lindwiesen)
```

**Wahrzeichen:** Die Riesenlinde (120 m Krone), der Lindentisch im Rathaus (Bundesvertrag), die Wurzelarena (Arena in einer Wurzelhöhle unter dem Baum, oben offen zum Blätterdach).
**Traversal:** Wurzelbrücken auf drei Ebenen; Kletterrouten auf die Linde (Aussichtspunkt, Gleitstart über die Stadt).

### 4.4 Dienste

Klangbrunnen (Marktplatz), Stadtstein, 6 Händler, Arena, Trainingsplatz (Wildwacht), Fraktionsbüros (Wildwacht, Akademie, Kontor), Questbrett, Werkbank + Kessel + Schmiede, Resonanzhain-Portal, Echo-Pflegestation, Online-Terminal, Gasthaus „Zum Wurzelkrug“.

### 4.5 Händler

| ID | Name / NPC | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_EICH_01 | Wendels Wärterbedarf (Wendel) | Allgemein | 7–20 | Starter-Siegel, Wildwacht-Rabatt |
| MER_EICH_02 | Lindenapotheke (Lorin) | Heilung | 8–19 | Lindblüten-Tonika |
| MER_EICH_03 | Harzhaus (Tilda) | Material | 6–14 | Klangharz (rotierend) |
| MER_EICH_04 | Zum Wurzelkrug (Odo) | Nahrung | 10–1 | Lager-Rezepte |
| MER_EICH_05 | Schnitzerei Anselm | Ausrüstung | 8–18 | Gleiter-Bespannungen I–II |
| MER_EICH_06 | Wildwacht-Kammer (Greta) | Fraktion | 6–22 | Wildwacht-Rufwaren |

### 4.6 Arena: Wurzelarena (ARN_01)

| Feld | Wert |
|---|---|
| Meister | **Maelis Wendt** (34), Blüte |
| Stufe | 1 (Ass Lv. 12, Chor 3, Duell) |
| Vorprüfung | 2 Arena-Wärter (Lv. 8–10) |
| Feldregel | **Überwuchs** |
| Dramaturgie | Maelis erkennt in Kampfstil des Spielers Ysoldes Schule; nach dem Sieg zeigt sie die Wurzelhalle („Hier unten schläft etwas“ – Vorahnung W4) |

### 4.7 Quests

| Typ | Inhalt |
|---|---|
| Hauptquest | Akt I-Auftakt (MQ_A1_01–03): Ankunft, Bundesrat-Anhörung zur Stillezone, Arena; Ysolde schickt den Spieler in die drei Nachbarregionen |
| Nebenquest-Haken | „Der Lindentisch“ (Bundesgeschichte), „Wurzelpfade“ (Kletter-Sammlung), „Das Echo im Harzfass“, Fotowettbewerb der Akademie-Außenstelle |
| Fraktion | Wildwacht-Einstieg (FQ_F03_01: Patrouille), Akademie-Außenstelle (Kodex-Aufträge) |

### 4.8 Musik

| Variante | Beschreibung |
|---|---|
| Stadtthema (Tag) | 6/8-Takt, Holzbläser (Flöte, Klarinette), Harfe, gezupfte Streicher; Leitmotiv „Linde“ (aufsteigende Quarte) |
| Nacht | Reduziert auf Harfe und Glockenspiel, langsamer (−15 BPM) |
| Arena | Thema im 4/4, Streicher-Ostinato, Pauken; bei Meister-Phase 2 Glockenblüten-Motiv |
| Fest | Linnisches Tanzlied (Fiedel, Rahmentrommel) |

### 4.9 Einwohner & Tagesabläufe (Auswahl)

| NPC | Rolle | Muster | Besonderheit |
|---|---|---|---|
| Maelis Wendt | Arenameisterin | Tagwerk; 6–7 Uhr Training mit Echos am Trainingsplatz | Abends am Brunnen ansprechbar (Lore-Gespräche) |
| Wendel | Händler | Tagwerk | Mittag im Wurzelkrug |
| Greta | Wildwacht-Quartiermeisterin | Wache | Bei Regen hilft sie im Stall |
| Rätin Elsbeth Moor | Bundesrätin | Tagwerk + Ratssitzungen (Tag 1 jeder Spielwoche) | Auslöser MQ_A1_02 |
| Ambient | Händlerkinder, Ranger, Pilger | Mass Crowd | Marktplatz-Dichte 10–18 Uhr hoch |

**Fest:** *Lindenfest* – jeden 7. Spieltag abends: Musik, Lampions, Echo-Parade (Fotomodus-Anlass).

---

## 5. Kharsholm (R02)

### 5.1 Steckbrief

| Feld | Wert |
|---|---|
| Region / Lage | R02 Kharsgrat, 4,2 / 2,2 km, in die Felswand über dem Grollschlund gehauen |
| Einwohner | 6.500 |
| Regierung | **Klanrat** (Brakk, Hrall, Torv – je ein Älteste/r) |
| Fraktionen | Wildwacht-Posten, Kontor-Erzhandel |
| Arena | ARN_02, Torvik Hrall (Stein/Schwerkraft), skaliert (Akt-I-Stufe 2–4) |
| Ursprungsstimme | Orh'gruun – im Schlund unter der Stadt |
| Fantasie | *„Eine Stadt, die nicht gebaut, sondern dem Berg abgerungen wurde.“* |

### 5.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -250 v.St. | Orh'gruun hebt Nimbara – zurück bleiben die Schwebefelsen |
| 398 n.St. | Vereinigung der Klans in Kharsholm (Schwur am Ahnenfelsen) |
| 702–709 n.St. | Siegelkriege: Kharsholm stellt Echo-Lastzüge – Schuld, über die man nicht spricht |
| 880 n.St. | Arena im **Schlundring** gebaut |
| 1004 n.St. | Stillezone im Grollschlund bedroht die tiefen Minen |

### 5.3 Architektur & Layout

Stil: **Kharske Felsbaukunst** – gemeißelte Fassaden, Basaltsäulen, Bronzetore, Kettenbrücken; Wohnhöhlen mit Rauchabzügen; Lastenaufzüge mit Gegengewichten (Klangwerk).

```
        Ebene 3 (oben):  KLANRAT-HALLE · Ahnenfelsen · Aussichtsplattform
                         ║ Lastenaufzug
        Ebene 2:        WOHNHÖHLEN ═══ Kettenbrücke ═══ SCHMIEDE + ERZKONTOR
                         ║
        Ebene 1:        MARKT-GALERIE · Gasthaus „Halle der Klans“ · Klangbrunnen
                         ║
        Ebene 0 (Schlund): SCHLUNDRING-ARENA (über der Tiefe, Gitterboden)
                         ║ (verschlossen bis W4)
                     ~~~ GROLLSCHLUND (Orh'gruuns Schlafstätte) ~~~
```

**Wahrzeichen:** Schlundring-Arena (kreisrunde Plattform über dem Abgrund), Ahnenfelsen (schwebend, Klanschwüre), Große Kettenbrücke.
**Traversal:** Vertikal – Aufzüge, Kletterwände zwischen Ebenen, Gleitstart vom Ahnenfelsen.

### 5.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_KHAR_01 | Brann & Söhne | Allgemein | 5–21 | Kletterhaken |
| MER_KHAR_02 | Grollschmiede | Ausrüstung | 6–22 | Ausrüstung II, Nachtrabatt |
| MER_KHAR_03 | Erzkontor | Material | 0–24 | Durchgehend (Schichten) |
| MER_KHAR_04 | Halle der Klans | Nahrung | 12–2 | Gipfelenzian-Schnaps (Kälteschutz) |
| MER_KHAR_05 | Ahnenstein-Tutorin Yrsa | Tutor | 9–17 | Stein/Schwerkraft-Fähigkeiten |

### 5.5 Arena: Schlundring (ARN_02)

| Feld | Wert |
|---|---|
| Meister | **Torvik Hrall** (51), Stein/Schwerkraft |
| Stufe | skaliert 2–4 (CANON §15) |
| Feldregel | **Wandernde Plattformen** (Reihentausch alle 4 Züge) |
| Dramaturgie | Torvik verlangt vor dem Kampf einen Klanschwur am Ahnenfelsen (Dialogentscheidung, beeinflusst nur Flavor/Ruf Wildwacht +) |

### 5.6 Quests

Hauptquest: regionale Akt-I-Kette (Stillezone im Schlund; ggf. W2-Fund der Stillsteine). Nebenquests: „Die Schuld der Lastzüge“ (Siegelkriegs-Erbe, moralische Entscheidung), „Drei Klans, ein Gipfel“ (Klan-Wettkampf), „Verschüttet“ (Minenrettung, Grabreiten später optional).

### 5.7 Musik

Tag: tiefer gemischter Chor (Brummstimmen), Ambosse auf Zählzeit 1 und 3, Hörner. Nacht: nur Brummchor + entfernte Hämmer (Schichtbetrieb). Arena: 7/8-Takt, Trommeln, Chor in Kharsk-Silben.

### 5.8 Einwohner & Tagesabläufe

| NPC | Rolle | Muster |
|---|---|---|
| Torvik Hrall | Arenameister, Klanältester | Tagwerk; 18 Uhr Klanrat (Tag 3 jeder Woche) |
| Tova | Erzkontor | Schicht A |
| Gerd | Wirt | Nachtvolk-ähnlich (12–2) |
| Ambient | Bergleute | Schichtmuster A/B/C – Stadt ist **rund um die Uhr** belebt |

**Fest:** *Schwurnacht* – jeder 10. Spieltag: Fackelzug zum Ahnenfelsen.

---

## 6. Morvenfurt (R03)

### 6.1 Steckbrief

| Feld | Wert |
|---|---|
| Region / Lage | R03 Morvenmoor, 5,4 / 4,8 km, Pfahl- und Kanalstadt |
| Einwohner | 5.000 (+ ~600 in der verborgenen Unterstadt) |
| Regierung | **Zunft der Fährleute** (gewählter Fährmeister) |
| Fraktionen | **Freie Stimmen** (Hauptsitz Unterstadt, F04), Kontor (Fischhandel), Orden (Kapelle) |
| Arena | ARN_03, Evhe Corrach (Gift/Geist), skaliert 2–4 |
| Ursprungsstimme | Nhael'vesh – im Versunkenen Turm |
| Fantasie | *„Alles schwimmt, alles flüstert, alles hat zwei Seiten.“* |

### 6.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ 500 n.St. | Fischersiedlung auf Pfählen um die Spitze des Versunkenen Turms |
| 640 n.St. | Bau der Kanäle; Morvenfurt wird Handelsknoten zwischen Verdanthain und Ael'Dorun |
| 967 n.St. | Skandal um ein Echo-Arbeitslager eines Kontor-Konsortiums im Moor → Gründung der **Freien Stimmen** in der alten Kanalisation (Unterstadt) |
| 1004 n.St. | Stillezone im Duvreth-Sumpf; Spannungen zwischen Kontor und Freien Stimmen |

### 6.3 Architektur & Layout

Stil: **Morvische Pfahlbauten** – Holz auf Steinsockeln, Schilfdächer, überdachte Brücken, Laternenstege, Bootsgaragen; die Unterstadt in alten Steinkanälen unter der Oberstadt.

```
   ╔═══════════════════ OBERSTADT ═══════════════════╗
   ║  Fährhaus (Rat)   ≈≈ Hauptkanal ≈≈   Fischhalle  ║
   ║      │                                   │       ║
   ║  Laternensteg ═══ Brückendach ═══ Nachtmarkt     ║
   ║      │              │                    │       ║
   ║  Kapelle (Orden)  Versunkener Turm   Bootsbauer  ║
   ║                    (Spitze = ARENA-PLATTFORM)    ║
   ╚══════════════╤════════════════════╤══════════════╝
         geheime Einstiege (Brunnen, Bootshaus)
   ┌──────────────┴─── UNTERSTADT ──────┴─────────────┐
   │ Freie-Stimmen-Versammlung · Der Schatten (Händler)│
   │ Echo-Zuflucht (befreite Arbeits-Echos)            │
   └───────────────────────────────────────────────────┘
```

**Wahrzeichen:** Turmspitzen-Arena (Plattform auf der aus dem Wasser ragenden Spitze des Versunkenen Turms), Nachtmarkt-Laternen, Brückendach.
**Traversal:** Boote (Fährleute als Schnellreise innerhalb der Stadt), Schwimmen, Stege; Unterstadt per Geheimeingängen.

### 6.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_MORV_01 | Laternensteg (Nialla) | Allgemein | 18–6 | Nachtmarkt |
| MER_MORV_02 | Moorweise Corrach | Heilung | 16–4 | Dunst-Tees, Gift-Heilmittel |
| MER_MORV_03 | Bootsbauer Finn | Ausrüstung | 6–18 | Schwimmreit-Sättel |
| MER_MORV_04 | Der Schatten (Unterstadt) | Selten | 22–4 | Schwarzmarkt, nur mit Freie-Stimmen-Ruf ≥ 2 |
| MER_MORV_05 | Fischhalle Duva | Nahrung | 4–12 | Morgenmarkt |

### 6.5 Arena: Turmspitze (ARN_03)

| Feld | Wert |
|---|---|
| Meister | **Evhe Corrach** (Alter unbekannt, wirkt 40), Gift/Geist; Schwester der Moorweisen Corrach |
| Stufe | skaliert 2–4 |
| Feldregel | **Moornebel** |
| Dramaturgie | Kampf nur nachts (Nebel), tagsüber gibt Evhe Rätsel statt Kämpfe; nach dem Sieg Hinweis auf die Unterstadt (Fraktionseinstieg F04) |

### 6.6 Quests

Hauptquest: regionale Akt-I-Kette; Erstkontakt **Tavesh Amaru** (CANON §46). Nebenquests: „Zwei Seiten des Kanals“ (Kontor vs. Freie Stimmen – erste Fraktionsentscheidung), „Irrlichtjagd“ (Jagd), „Der Fährmeister und das Turmgeheimnis“, „Laternen für die Toten“ (Erinnerung, Geist-Echos).

### 6.7 Musik

Tag (ruhig): Tin-Whistle-artige Flöte, Bodhrán, gezupfte Laute, viel Raum. Nacht (Hauptzeit): Nachtmarkt-Variante mit Fidel, Trommel, Stimmengewirr. Unterstadt: gedämpfte Variante, Echo-Hall, Summchor. Arena: Gift-Dissonanzen (Klarinetten), 5/4-Takt.

### 6.8 Einwohner & Tagesabläufe

| NPC | Rolle | Muster |
|---|---|---|
| Evhe Corrach | Arenameisterin | Nachtvolk |
| Fährmeisterin Ailsa Duvreth | Regierung | Tagwerk |
| Tavesh Amaru | Freie Stimmen | unregelmäßig, nachts in der Unterstadt |
| Ambient | Fischer (Morgen), Händler (Nacht) | Nachtvolk-dominiert |

**Fest:** *Laternennacht* – jeder 5. Spieltag: Laternen auf dem Hauptkanal (Gedenken), Geist-Echos erscheinen (Kodex-Gelegenheit).

---

## 7. Qasr Sahrun (R04)

### 7.1 Steckbrief

| Feld | Wert |
|---|---|
| Region / Lage | R04 Sahrun-Weite, 4,1 / 5,9 km, am Fuß des Sonnenhof-Plateaus |
| Einwohner | 7.500 |
| Regierung | **Rat der Sonnenhöfe** (Familienhäuser, Sprecherin wechselt jährlich) |
| Fraktionen | Kontor (Karawanen), Akademie-Grabung (Akt II), Freie-Stimmen-Zelle |
| Arena | ARN_04, Shirah Harrâd (Licht), skaliert (Akt-II-Stufe 5–8) |
| Ursprungsstimme | Ash'kareth – unter dem Sonnenhof |
| Fantasie | *„Im Schatten der Mauern ist man Gast – und Gäste sind heilig.“* |

### 7.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -400 v.St. | Dorunische Sonnenwarte auf dem Plateau (heute Sonnenhof) |
| 450 n.St. | Karawanenstadt an der Plateau-Quelle |
| 705 n.St. | Belagerung in den Siegelkriegen; das **Gastrecht** rettet die Stadt (Feinde wurden als Gäste aufgenommen) – Gründungsmythos des heutigen Gastrechts |
| 880 n.St. | Arena im Sonnenhof (Innenhof mit Spiegeln) |
| 1004 n.St. | Akademie-Expedition (Venn) gräbt am Sonnenhof (Akt II) |

### 7.3 Architektur & Layout

Stil: **Sahrunische Lehmarchitektur** – dicke Mauern, Kuppeln, Windtürme, Innenhöfe mit Klangbrunnen, Spiegelmosaike; Gassen schattig und eng; Plateau mit Sonnenhof darüber (Treppe der tausend Stufen).

```
                     SONNENHOF (Plateau, 420 m)
                     Arena-Innenhof mit Spiegeln
                     ║ Treppe der tausend Stufen
   ┌─────────────────╨──────────────────────────┐
   │ HAUS HARRÂD   │ RATSHOF  │ GLASBLÄSER-      │
   │ (Arenameisterin)│ (Rat)  │ VIERTEL          │
   │───────────────┼──────────┼──────────────────│
   │ KARAWANSEREI  │ BRUNNEN- │ STERNDEUTER-     │
   │ (Händler,      │ PLATZ    │ TURM (Harun)     │
   │  Ställe)       │(Klangbr.)│                  │
   │───────────────┴──────────┴──────────────────│
   │ OASENGÄRTEN (Palmen, Wasserkanäle)           │
   └──────────────────────────────────────────────┘
   Akademie-Grabungslager am Plateaufuß (Akt II, Data Layer)
```

**Wahrzeichen:** Sonnenhof-Arena (Spiegel bündeln Sonnenlicht; nachts Mondspiegel), Treppe der tausend Stufen, Windtürme (Kühlung, Klangröhren).
**Traversal:** Dächer verbunden (Parkour-Route im Schatten), Plateau-Kletterwände, Gleiten vom Sonnenhof über die Stadt.

### 7.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_QASR_01 | Karawanserei Amara | Allgemein | 16–8 | Nachtöffnung, Hitzeschutz |
| MER_QASR_02 | Glasbläserei Tavi | Material | 17–3 | Sonnenglas |
| MER_QASR_03 | Gewänder Mirsa | Ausrüstung | 17–2 | Kleidung III (Hitze) |
| MER_QASR_04 | Sterndeuter Harun | Selten | 20–5 | Mondphasen-Kalender, seltene Lockmittel |
| MER_QASR_05 | Brunnenküche Saya | Nahrung | 18–4 | Oasenminz-Tee |
| MER_QASR_06 | Lichttutorin Imra | Tutor | 19–1 | Licht/Arkan-Tutor |

### 7.5 Arena: Sonnenhof (ARN_04)

| Feld | Wert |
|---|---|
| Meisterin | **Shirah Harrâd** (29), Licht |
| Stufe | skaliert 5–8 |
| Feldregel | **Sonnenspiegel** (nachts Mondspiegel: Wirkung 50 %) |
| Dramaturgie | Kämpft nur nach Sonnenuntergang; vor dem Kampf **Gastmahl** – wer das Gastrecht verletzt hat (Quest-Flag), muss zuerst Wiedergutmachung leisten |

### 7.6 Quests

Hauptquest Akt II: Venns Grabung am Sonnenhof (Kronensplitter-Spur). Nebenquests: „Das Gastrecht“ (Kette, 4 Teile), „Glas aus Licht“ (Glasbläser-Wettbewerb), „Harun und der Neumond“ (Mondphasen, Q15), „Die verirrte Karawane“ (Sandsturm-Navigation).

### 7.7 Musik

Tag: sehr reduziert (Hitze-Stille), einzelne Oud-artige Laute, Wind durch Klangröhren. Nacht: volle Besetzung – Laute, Rahmentrommel, Kanun-artige Zither, Frauenchor; Tonleiter **eigens komponiert** (keine direkte Übernahme realer Maqam-Systeme; Musikberatung, K55). Arena: Rhythmus in 10/8, Chorrufe.

### 7.8 Einwohner & Tagesabläufe

| NPC | Rolle | Muster |
|---|---|---|
| Shirah Harrâd | Arenameisterin | Nachtvolk; Morgengebet am Sonnenhof (Sonnenaufgang) |
| Amara | Karawanenwirtin | Nachtvolk |
| Harun | Sterndeuter | Nachtvolk, schläft bis 18 Uhr |
| Ambient | Karawanenleute | Mittag (11–16) Straßen fast leer (Hitze) |

**Fest:** *Nacht der Gäste* – jeder 9. Spieltag: offene Tafeln, jeder NPC ist gesprächig (Bonus-Lore, Rufgewinne).

---

## 8. Saltrand-Hafen (R06)

### 8.1 Steckbrief

| Feld | Wert |
|---|---|
| Region / Lage | R06 Saltrand, 0,7 / 3,7 km, Linn-Mündung |
| Einwohner | 11.000 (größte Stadt) |
| Regierung | **Hafenrat** (Reedereien + Zünfte), faktisch stark vom Kontor geprägt |
| Fraktionen | **Goldklang-Kontor-Hauptsitz** (F02), Wildwacht-Hafenwache, Freie-Stimmen-Zelle |
| Arena | ARN_06, Beke Tamsen (Flut/Sturm), skaliert 2–4 |
| Ursprungsstimme | Thal'assyr – Tiefseegrotte vor dem Hafen |
| Fantasie | *„Alles, was es auf Aethris gibt, kommt irgendwann hier an.“* |

### 8.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -1000 v.St. | Älteste Küstensiedlung (Ruinen am Leuchtfelsen) |
| 520 n.St. | Werften, erste Seehandelsroute entlang der Küste |
| 610 n.St. | Gründung des **Goldklang-Kontors** im Haus mit der goldenen Glocke |
| 707 n.St. | Seeblockade in den Siegelkriegen |
| 880 n.St. | Arena im **Gezeitenbecken** (Hafenbecken mit Schleusen) |
| 1004 n.St. | Stillezone im Riff – Gezeiten in der Bucht stocken; Handel bricht ein |

### 8.3 Architektur & Layout

Stil: **Saltische Backsteingotik**-Anmutung (fiktiv abgewandelt): Giebelhäuser, Speicher mit Kränen, Kopfsteinpflaster, Holzstege, Kontorhaus mit goldener Glocke.

```
     MEER  ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
     ≈ Leuchtfelsen (N)        Tiefseegrotte (vor der Küste, W4)
     ╔══ MOLE ══╗   GEZEITENBECKEN-ARENA (Schleusen)
     ║ WERFTEN  ║═══════════════════════════════════╗
     ║ (Klaas)  ║ KAI · Kontor am Kai · Fischmarkt   ║
     ╚══════════╝═══════════════════════════════════║
       SPEICHERSTADT       │ GOLDKLANG-HAUPTHAUS     ║
       (Lager, Schmuggel-   │ (goldene Glocke)        ║
        keller → Höhlen)    │ Hafenrat                ║
       ────────────────────┼─────────────────────────║
       SEEMANNSVIERTEL      │ KURIOSITÄTEN · TAUCHER  ║
       (Tavernen)           │ KLANGBRUNNEN            ║
       ═══════ Linnbrücke (Straße nach Eichenhall) ═══
```

**Wahrzeichen:** Goldene Glocke (läutet bei jeder Flut), Gezeitenbecken-Arena (Wasserstand folgt den Gezeiten), Leuchtfelsen in Sichtweite.
**Traversal:** Kräne und Masten als Kletterpunkte, Schwimmen im Hafen, Schmugglerkeller verbunden mit Küstenhöhlen (bei Ebbe).

### 8.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_SALT_01 | Kontor am Kai (Jonte) | Allgemein | 6–20 | Größtes Sortiment in Akt I |
| MER_SALT_02 | Goldklang-Haupthaus | Fraktion | 8–18 | Rufwaren, Handelsaufträge |
| MER_SALT_03 | Taucherbedarf Hauke | Ausrüstung | 6–18 | Taucherausrüstung, Schwimmsattel |
| MER_SALT_04 | Fischmarkt | Nahrung | 4–11 | nur bei Ebbe + morgens |
| MER_SALT_05 | Kuriositäten Odalis | Selten | 10–22 | wechselnde Importware |
| MER_SALT_06 | Werftmeister Klaas | Material | 6–17 | Treibholz, Perlmutt |

### 8.5 Arena: Gezeitenbecken (ARN_06)

| Feld | Wert |
|---|---|
| Meisterin | **Beke Tamsen** (58), Flut/Sturm, Kapitänin a. D. |
| Stufe | skaliert 2–4 |
| Feldregel | **Gezeitenbecken** (Ebbe/Flut alle 3 Züge) |
| Dramaturgie | Beke wettet vor jedem Kampf (Sol-Einsatz optional, max. 500 ◎, kein Verlust bei Niederlage auf „Entspannt“) |

### 8.6 Quests

Hauptquest: regionale Akt-I-Kette (Gezeitenstillstand); Kontor-Einstieg mit **Marieke Holm**. Nebenquests: „Die goldene Glocke schweigt“, „Schmugglerkeller“ (Ebbe), „Bekes Wetten“ (Kampf-Herausforderungen), „Flaschenpost“ (Sammelreihe entlang der Küste, Lore).

### 8.7 Musik

Tag: Akkordeon-artige Harmonien, Shanty-Rhythmus (Stampfen, Klatschen), Glocke als Taktgeber. Nacht: Tavernenvariante (Fiedel, Gesang). Arena: Wellenrhythmus (wechselnde Taktarten 6/8 ↔ 3/4 synchron zu Ebbe/Flut).

### 8.8 Einwohner & Tagesabläufe

| NPC | Rolle | Muster |
|---|---|---|
| Marieke Holm | Handelsherrin | Tagwerk; 12 Uhr im Kontor erreichbar, abends auf dem Dach (Lore) |
| Beke Tamsen | Arenameisterin | Tagwerk; bei Flut im Becken |
| Hauke | Taucher | morgens im Wasser, nachmittags im Laden |
| Ambient | Seeleute, Händler, Hafenarbeiter | Hafen 5–20 hoch belebt; Tavernen 18–2 |

**Fest:** *Glockenflut* – bei Springflut (jeder 6. Spieltag): Bootsparade, Wettschwimmen mit Flut-Echos.

---

## 9. Code & Daten

### 9.1 Daten

- `Data/World/Settlements.csv` – alle 62 Siedlungen (ID gemäß K04 §7, Typ, Region, Anzeigename; Koordinaten für Städte und Lindwiesen; restliche in K13).
- `Data/World/Arenas.csv` – 10 Arenen (Meister, Spezialtyp, Stufenmodus, Feldregel, Ursprungsstimme).
- `Data/Economy/Merchants.csv` – Händler (K11 + K12), Schema: Id, Siedlung, NPC, Name, Kategorie, Öffnungszeiten, Besonderheit.

### 9.2 Arena-Stufe (GF_Quests bzw. Arena-Logik in GF_Combat-Integration über Service)

```cpp
// Plugins/GameFeatures/GF_Quests/Source/GF_Quests/Private/Arena/ArenaSubsystem.cpp (Auszug)
// Stufe wird beim ersten Betreten der ARENA fixiert (K11 §2.1) – analog zur Zonenfixierung (K08).
int32 UArenaSubsystem::ResolveStage(FName ArenaId)
{
	if (const int32* Fixed = FixedStages.Find(ArenaId))
	{
		return *Fixed;
	}
	const FArenaRow& Row = *ArenaTable->FindRow<FArenaRow>(ArenaId, TEXT("Arena"));
	int32 Stage = Row.FixedStage;
	if (Row.StageMode == TEXT("SCALED"))
	{
		// Akt I: Stufen 2–4, Akt II: 5–8 (Eichenhall = 1, Prismara = 9, Aerion = 10 sind fest)
		const int32 Akkorde = WorldState()->GetAkkordCount();
		const bool bActTwo = Row.RegionActIndex() == 2;
		Stage = bActTwo ? FMath::Clamp(Akkorde + 1, 5, 8) : FMath::Clamp(Akkorde + 1, 2, 4);
	}
	FixedStages.Add(ArenaId, Stage);   // Save-Fragment "Arenas"
	return Stage;
}
```

**Prüfung der Stufenlogik:** Akt I: Eichenhall gibt Akkord 1 → nächste Arena Stufe 2, dann 3, dann 4 ✔. Akt II: mit 4 Akkorden → Stufe 5 … bis 8 ✔. Eine Akt-II-Arena kann erst nach Akt-I-Abschluss (4 Akkorde) betreten werden (Story-Gates, CANON §42) – daher keine Lücke.

### 9.3 Händler-Öffnungszeiten (über Mitternacht)

```cpp
/** Öffnungsprüfung mit Spielstunden 0–24; From > To bedeutet „über Mitternacht“ (Merchants.csv). */
constexpr bool IsOpen(int32 From, int32 To, int32 Hour)
{
	if (From == 0 && To == 24) { return true; }
	return From <= To ? (Hour >= From && Hour < To) : (Hour >= From || Hour < To);
}
static_assert(IsOpen(18, 6, 23) && IsOpen(18, 6, 3) && !IsOpen(18, 6, 12), "Nachtmarkt-Logik");
```

---

## 10. Decision Records

### ADR-054 – Arena-Stufe wird beim Betreten der Arena fixiert, nicht der Region
- **Kontext:** Ein Spieler kann eine Region betreten (Zonen fixiert, K08) und die Arena erst später angehen, nachdem er anderswo Akkorde geholt hat.
- **Entscheidung:** Arena-Stufe fixiert beim ersten Betreten der Arena. Vorteil: Arena passt zur aktuellen Progression (Akkord-Reihenfolge immer 1→2→3→4). Nachteil: Region und Arena können um eine Stufe auseinanderliegen → akzeptiert (Arena ist der Prüfstein).

### ADR-055 – Feldregeln als Lektionen
- **Entscheidung:** Jede Arena lehrt ein Kampfsystem über ihre Feldregel (§2.3). Vorteil: Tutorialisierung ohne Textboxen, eigenständige Identität (Clean-Room Regel 3). Nachteil: zusätzlicher Balancing-Aufwand pro Arena → Simulator-Szenarien pro Feldregel (K63).

### ADR-056 – Lore-Einwohner ≠ dargestellte NPCs
- **Entscheidung:** Städte werden über Mass Crowds glaubwürdig dicht; Zahlen in §3.1 sind Budgets. Vorteil: Performance, Plattformparität. Nachteil: Lore-Zahlen und sichtbare Menge weichen ab → Mitigation: Städte mit vielen geschlossenen Häusern, „Leben hinter Fenstern“ (Licht, Geräusche).

### ADR-057 – Umgekehrte Stadtzeiten (Morvenfurt, Qasr Sahrun)
- **Entscheidung:** Händlerzeiten und Arenen dieser Städte orientieren sich an der Nacht. Konsistent mit ADR-048. Gasthäuser erlauben Zeitvorspulen, NPC-Hinweise erklären es.

---

## 11. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §51 | Stadt-Template (§1) | LOCKED |
| §51 | Arena-Regeln (§2.1): Vorprüfung + Meister, Stufe beim Betreten der Arena fixiert (ADR-054), Akt I Stufen 2–4, Akt II 5–8, Belohnungen, Meisterrunde Lv. 75–85 im Endgame | LOCKED |
| §51 | 10 Arenameister + Spezialtypen + Feldregeln (§2.2/§2.3), ARN_## = Regionsnummer, `Data/World/Arenas.csv` | LOCKED |
| §52 | Städte Eichenhall, Kharsholm, Morvenfurt, Qasr Sahrun, Saltrand-Hafen: Regierung, Geschichte, Layout, Händler, Arena-Dramaturgie, Quests, Musik, Tagesabläufe, Feste | LOCKED |
| §52 | Feste: Lindenfest (7. Tag), Schwurnacht (10.), Laternennacht (5.), Nacht der Gäste (9.), Glockenflut (6., Springflut) | LOCKED |
| §52 | Neue Figuren: Rätin Elsbeth Moor, Fährmeisterin Ailsa Duvreth, Händler-NPCs gemäß `Merchants.csv` | LOCKED |
| §53 | Bevölkerungsbudgets (§3.1), Tagesablauf-Muster Tagwerk/Schicht/Nachtvolk/Wache/Gelehrt (§3.2) | LOCKED |
| §53 | `Data/World/Settlements.csv` (62 Siedlungen), `Data/Economy/Merchants.csv` | LOCKED |
| §10 | ADR-054 – ADR-057 | LOCKED |

---

## 12. Kapitel-Checkliste

- [x] Stadt-Template gemäß Briefing (Architektur, Geschichte, Händler, Arena, Quests, Musik, Einwohner/Tagesablauf)
- [x] Arena-System inkl. Stufenlogik (verifiziert), Belohnungen, Meisterrunde
- [x] Alle 10 Arenameister mit Spezialtyp, Feldregel und Persönlichkeit
- [x] 10 Feldregeln als Kampfsystem-Lektionen
- [x] Bevölkerungsbudgets und Tagesablauf-Muster
- [x] Eichenhall, Kharsholm, Morvenfurt, Qasr Sahrun, Saltrand-Hafen vollständig nach Template
- [x] Siedlungs-, Arena- und Händlerdaten im Repository
- [x] Code: Arena-Stufe, Öffnungszeiten-Logik (mit static_assert)
- [x] ADR-054 – ADR-057, CANON aktualisiert

➡️ **Nächstes Kapitel: K12 – Städte II (Schlackenwehr, Hvitmark, Dorunsruh, Prismara, Aerion).**
