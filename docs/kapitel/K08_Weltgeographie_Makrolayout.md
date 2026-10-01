# K08 · Weltgeographie & Makro-Layout

| Feld | Wert |
|---|---|
| Dokument | Kapitel 08 von 68 · World Bible, Teil II |
| Version | 1.0 |
| Owner | Level Designer (Lead World Designer) |
| Mitwirkende | Technical Artist, Unreal Senior Dev (World Partition), Quest Designer, Narrative |
| Baut auf | K02 §9, K03 §7, K07 (CANON §4, §15, §19, §33–§36) |
| Status | ✅ Freigegeben |
| Im Repository angelegt | `tools/gen_macromap.py`, `Data/World/MacroMap.txt`, `MacroMap_Sky.txt`, `MacroRegions.csv`, `Zones.csv`, `ZoneTiers.csv` |
| Neue Kanon-Einträge | CANON §39 (Makrokarte & Koordinaten), §40 (Zonen & Level), §41 (Siedlungsorte & Wege), §42 (Höhen, Grenzen, Traversal-Gates), §43 (World Partition) |

---

## Inhalt

1. [Zweck & Methode](#1-zweck--methode)
2. [Die Makrokarte](#2-die-makrokarte)
3. [Regionen: Lage, Fläche, Nachbarschaft](#3-regionen-lage-fläche-nachbarschaft)
4. [Höhenprofil, Gewässer, Weltgrenzen](#4-höhenprofil-gewässer-weltgrenzen)
5. [Hauptorte & Wegenetz](#5-hauptorte--wegenetz)
6. [Zonen & Level-Bänder](#6-zonen--level-bänder)
7. [Traversal-Gates & Metroidvania-Struktur](#7-traversal-gates--metroidvania-struktur)
8. [Resonanzsteine & Schnellreise](#8-resonanzsteine--schnellreise)
9. [POI-Dichte & Level-Design-Metriken](#9-poi-dichte--level-design-metriken)
10. [Technische Umsetzung: World Partition](#10-technische-umsetzung-world-partition)
11. [Code: Zonenauflösung](#11-code-zonenauflösung)
12. [Decision Records](#12-decision-records)
13. [Kanon-Updates](#13-kanon-updates)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Zweck & Methode

Dieses Kapitel legt fest, **wo** alles liegt. Statt einer Skizze, die später niemand mehr mit den Zahlen abgleicht, ist die Makrokarte eine **Datei**: `Data/World/MacroMap.txt` (40 × 35 Zellen à 200 m = 8 × 7 km). Das Skript `tools/gen_macromap.py` erzeugt sie aus Saatpunkten und dem Regionsbudget (CANON §19) und **beweist** bei jedem Lauf:

- jede Region hat **exakt** die budgetierte Fläche (1 Zelle = 0,04 km²),
- jede Region ist **zusammenhängend**,
- Bodenfläche = **32,0 km²**, Himmelinseln = **4,0 km²** → **36,0 km²** (CANON §3).

Die Rasterkarte ist die **Blockout-Vorlage** für das Level-Design (World Partition Landscape wird darauf aufgebaut, K09/K10). Feinkonturen (Küsten, Flussläufe) entstehen im Landscape, müssen aber pro Region ±3 % der Zellfläche einhalten (Validator, §10.4).

---

## 2. Die Makrokarte

### 2.1 Bodenkarte (Norden oben, 1 Zeichen = 200 m × 200 m)

```
~~~~~~~~~~~~~~~~~~HHHHHH~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~HHHHHHHHH~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~HHHHHHHHHHHH~~~~~~~~~~~~~
~~~~~~~~~~~~~~HHHHHHHHHHHHHH~~~~~~~~~~~~
~~~~~~~~~~~~HHHHHHHHHHHHHHHHH~~~~~~~~~~~
~~~~~~~~~~~^HHHHHHHHHHHHHHHHH^~~~~~~~~~~
~~~~~~~~~^^^HKHHHHHHHHHHHHHHK^^~~~~~~~~~
~~~~~~~~^^^KKKKKKKKKKKKKKKKKK^^^^~~~~~~~
~~~~~~^^^^^KKKKKKKKKKKKKKKKKKK^^^^~~~~~~
~~~~~^^^^^^PPKKKKKKKKKKKKKKKKK^^^^^~~~~~
~~~~^^^^^^PPPPKKKKKKKKKKKKKKKK^^^^^^~~~~
~~~~^^^^^PPPPPPPKKKKKKKKKKAKKK^^^^^^^~~~
~~~^^^^^PPPPPPPPPKKKKKKKAAAAKK^^^^I^^^~~
~~~CCCC^PPPPPPPPPPKKKKAAAAAAA^^IIIIIII^~
~~CCCCCCCPPPPPPPPPPKKAAAAAAAAAIIIIIIII^~
~~CCCCCCCCPPPPPPPPPPAAAAAAAAAAIIIIIIIII~
~~CCCCCCCCPPPPPPPPPPAAAAAAAAAAIIIIIIIII~
~~CCCCCCCCPPPPPPPPPPAAAAAAAAAAIIIIIIIII~
~~CCCCCCCCCPPPPPPPPPAAAAAAAAAMIIIIIIIII~
~~CCCCCCCCVVVVPPPPPPAAAAAAAMMMIIIIIIIII~
~~CCCCCCCCVVVVVVVVPPPAAAMMMMMMMIIIIIII^~
~~~CCCCCCVVVVVVVVVVVSMMMMMMMMMMIIIIII^^~
~~~CCCCCCVVVVVVVVVVVSMMMMMMMMMMM^^I^^^~~
~~~CCCCCVVVVVVVVVVVSSMMMMMMMMMMM^^^^^^~~
~~~CCCCCVVVVVVVVVVSSSSMMMMMMMMMM^^^^^~~~
~~~~CCCVVVVVVVVVVSSSSSMMMMMMMMMM^^^^^~~~
~~~~^VVVVVVVVVVVSSSSSSSMMMMMMMMS^^^^~~~~
~~~~~VVVVVVVVVVSSSSSSSSSSMMMMMMS^^^^~~~~
~~~~~^VVVVVVVVSSSSSSSSSSSSMMMSSS^^^~~~~~
~~~~~~VVVVVSSSSSSSSSSSSSSSSSSSSSS^~~~~~~
~~~~~~~^VSSSSSSSSSSSSSSSSSSSSSSSS~~~~~~~
~~~~~~~~~SSSSSSSS~~~~~SSSSSSSSS~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

| Zeichen | Region | Zeichen | Region |
|---|---|---|---|
| `V` | R01 Verdanthain (Wald) | `C` | R06 Saltrand (Küste) |
| `K` | R02 Kharsgrat (Gebirge) | `H` | R07 Hvitfell (Schnee) |
| `M` | R03 Morvenmoor (Sumpf) | `A` | R08 Ael'Dorun (Ruinen) |
| `S` | R04 Sahrun-Weite (Wüste) | `P` | R09 Prismtiefen (Krater-Oberfläche; Höhlen darunter) |
| `I` | R05 Ignareth (Vulkan) | `^` | Unpassierbare Grenzklippen / Steilküste (114 Zellen = 4,56 km², nicht spielbar) |
| `~` | Meer (Weltgrenze) | | |

### 2.2 Himmelschicht – Nimbara (R10)

Die Himmelinseln schweben in **1.400–2.600 m** Höhe über dem Zentrum (über Prismtiefen, Ael'Dorun und Kharsgrat-Süd). Footprint 100 Zellen = 4,0 km² (`N`):

```
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
....................N...................
.................NNNNNNN................
...............NNNNNNNNNNN..............
..............NNNNNNNNNNNN..............
..............NNNNNNNNNNNNN.............
..............NNNNNNNNNNNNN.............
..............NNNNNNNNNNNNN.............
...............NNNNNNNNNNN..............
...............NNNNNNNNNNN..............
.................NNNNNNN................
....................N...................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
........................................
```

### 2.3 Lesart der Karte (Design-Absicht)

```
                          ┌──────────── NORDEN: Hvitfell (Akt II–III) ───────────┐
                          │        Gletscher, Kloster Schweigfels, Hvitmark       │
                          ├──────────── Kharsgrat (Akt I) – Gebirgsriegel ────────┤
   WESTKÜSTE              │                                                       │     OSTEN
   Saltrand  ◄── Krater ──┤  Prismtiefen-Krater ◄─► Ael'Dorun (Zentrum, Ruinen)   ├──► Ignareth
   (Akt I)      (Akt III) │         ▲ darüber schweben die Himmelinseln Nimbara    │    (Akt II)
                          ├──────────── Verdanthain (Start) ◄──► Morvenmoor ──────┤
                          │                         (Akt I)       (Akt I)          │
                          └──────────── SÜDEN: Sahrun-Weite (Akt II) ─────────────┘
```

- **Start im Südwesten-Zentrum** (Verdanthain): Von dort sind alle drei Akt-I-Regionen (Kharsgrat N, Morvenmoor O, Saltrand W) direkt erreichbar – Gestaffelte Offenheit (ADR-012) folgt der Geographie.
- **Akt II liegt am Rand** (Wüste S, Vulkan O, Schnee N) plus das **Zentrum** Ael'Dorun, das der Spieler die ganze Zeit „sieht“, aber erst in Akt II betritt (Sichtachse auf die Ruinen und die Himmelinseln darüber = permanenter Story-Haken).
- **Akt III liegt in der Mitte**: unter (Prismtiefen) und über (Nimbara) dem Zentrum – die Welt „faltet sich zur Mitte“.

---

## 3. Regionen: Lage, Fläche, Nachbarschaft

Werte aus `Data/World/MacroRegions.csv` (Koordinaten in km, Ursprung = Nordwestecke der Karte).

| Region | Zellen | Fläche | Schwerpunkt (x, y) | Ausdehnung x | Ausdehnung y | Nachbarn | Übergänge (Gates §7) |
|---|---|---|---|---|---|---|---|
| R01 Verdanthain | 100 | 4,0 km² | 2,45 / 4,91 | 1,0–4,0 | 3,8–6,2 | R06, R09, R08, R03, R04 | offen (Wege) |
| R02 Kharsgrat | 100 | 4,0 km² | 4,25 / 1,97 | 2,2–6,0 | 1,2–3,0 | R07, R09, R08, R05 | Pässe; Gipfel nur Klettern |
| R03 Morvenmoor | 80 | 3,2 km² | 5,39 / 4,76 | 4,2–6,4 | 3,6–5,8 | R01, R08, R05, R04 | Furten; Tiefsumpf Schwimmreiten |
| R04 Sahrun-Weite | 110 | 4,4 km² | 4,22 / 5,77 | 1,8–6,6 | 4,2–6,4 | R01, R03, R05 | Story-Gate Akt II (Sandsturm-Barriere) |
| R05 Ignareth | 75 | 3,0 km² | 6,88 / 3,48 | 6,0–7,8 | 2,4–4,6 | R02, R08, R03, R04 | Story-Gate Akt II (Ascheschleier) |
| R06 Saltrand | 85 | 3,4 km² | 1,18 / 3,81 | 0,4–2,2 | 2,6–5,2 | R01, R09 | offen |
| R07 Hvitfell | 90 | 3,6 km² | 4,13 / 0,81 | 2,4–5,8 | 0,0–1,4 | R02 | Story-Gate Akt II (Schneesturm am Pass) |
| R08 Ael'Dorun | 70 | 2,8 km² | 4,97 / 3,27 | 4,0–6,0 | 2,2–4,2 | R02, R09, R01, R03, R05 | Story-Gate: Ruinensiegel (nach 2 Akt-II-Regionen) |
| R09 Prismtiefen | 90 | 3,6 km² | 2,87 / 3,05 | 1,6–4,2 | 1,8–4,2 | R06, R02, R08, R01 | Oberfläche offen ab Akt I (Kraterrand = Aussichtspunkt), Höhlen Akt III |
| R10 Nimbara | 100 | 4,0 km² | 4,09 / 3,10 | 2,8–5,4 | 2,0–4,2 | (Himmel) | Flugreiten + Story Akt III |

**Story-Gates sind diegetisch** (Wetter-/Resonanzbarrieren, die durch Hauptquests gelöst werden), nie unsichtbare Wände (DR-14-Geist: Respekt vor Spielerintelligenz). Wer vor der Zeit in ein Akt-II-Gebiet will, sieht und versteht die Barriere.

---

## 4. Höhenprofil, Gewässer, Weltgrenzen

### 4.1 Höhen (LOCKED, Landscape-Vorgabe)

| Ort | Höhe (m ü. M.) | Anmerkung |
|---|---|---|
| Meeresspiegel | 0 | Westküste, Südküste (Sahrun), Ostküste (Ignareth) |
| Verdanthain | 20–260 | sanfte Hügel, Wälder |
| Morvenmoor | 5–60 | Senke, Grundwasser nahe Oberfläche |
| Saltrand | 0–180 | Klippen bis 180 m (Leuchtfelsen) |
| Sahrun-Weite | 40–420 | Dünen bis 90 m Höhe, Sonnenhof-Plateau 420 m |
| Prismtiefen (Kraterrand) | 150–380 | Krater fällt auf **−250 m** (Höhlen bis −600 m) |
| Ael'Dorun | 300–520 | Tafelland mit Ruinenterrassen |
| Ignareth | 60–1.150 | Ignar-Krater-Rand 1.150 m |
| Kharsgrat | 400–1.650 | Grollhorn 1.650 m |
| Hvitfell | 900–2.100 | Isvaldtind 2.100 m (höchster Punkt am Boden) |
| Nimbara | 1.400–2.600 | Sternenarena von Aerion auf 2.600 m |

> **Maßstab-Hinweis:** Die Höhen sind gegenüber realen Gebirgen auf ~40 % skaliert, damit Kletterwege (1,6 m/s, K02) in Minuten statt Stunden bleiben. Silhouetten werden durch Nebel/Atmosphäre und Matte-Painting-Skyboxen (ferne Gipfel außerhalb der Spielwelt) größer inszeniert.

### 4.2 Gewässer

| Gewässer | Verlauf | Funktion |
|---|---|---|
| **Linn** (Fluss) | Kharsgrat-Süd → Verdanthain → Saltrand (Mündung bei Saltrand-Hafen) | Prolog-Grenze (Lindwald), Schwimmreiten-Route |
| **Morve** | Ael'Dorun → Morvenmoor (verästelt sich zum Delta) | Kanalstadt Morvenfurt |
| **Ignar-Lavastrom** | Ignar-Krater → Ostküste | Glutboden-Terrain, Obsidianbrücken |
| **Kristallsee** | Kraterboden Prismtiefen (unterirdisch) | Akt III |
| **Schmelzwasser-Fälle** | Hvitfell → Kharsgrat | Kletter-/Gleitrouten |
| **Oasen** | 6 in Sahrun | Rast, Spawns |

### 4.3 Weltgrenzen (LOCKED)

| Rand | Darstellung | Mechanik |
|---|---|---|
| Meer (W, S, O) | Offenes Meer, Strömung wird stärker | Ab 400 m vor Küste: Gegenströmung + Klangsignal + Echo weigert sich weiterzuschwimmen; kein Sterben, kein unsichtbarer Wall |
| Norden | Gletscherwände, Dauersturm | Kletterverbot (glatte Eisflächen), Schneesturm drückt zurück |
| Himmel | Über 2.800 m Resonanzwirbel | Flugreittier sinkt sanft ab |
| Unterwelt | Prismtiefen-Boden −600 m | Begrenzte Höhlensysteme |

---

## 5. Hauptorte & Wegenetz

### 5.1 Städte und wichtige Orte (Koordinaten in km)

| Ort | Region | x / y | Lage | Hinweis |
|---|---|---|---|---|
| **Lindwiesen** (Dorf, Start) | R01 | 1,9 / 5,7 | Südwestlich am Lindwald | Prolog |
| **Eichenhall** | R01 | 2,6 / 4,8 | Waldzentrum, um den Wurzelhain | Bundesrat, Wildwacht-HQ, Arena (Sylv'anor) |
| **Saltrand-Hafen** | R06 | 0,7 / 3,7 | Linn-Mündung, Westküste | Goldklang-HQ |
| **Kharsholm** | R02 | 4,2 / 2,2 | In den Fels gebaut, über dem Grollschlund | Arena (Orh'gruun) |
| **Morvenfurt** | R03 | 5,4 / 4,8 | Kanalstadt auf Pfählen | Freie Stimmen (Unterstadt) |
| **Qasr Sahrun** | R04 | 4,1 / 5,9 | Am Fuß des Sonnenhof-Plateaus | Akt II |
| **Schlackenwehr** | R05 | 6,7 / 3,5 | Festungsstadt an der Lavawehr | Akt II |
| **Hvitmark** | R07 | 4,1 / 0,7 | Gletschertal | Akt II; Kloster Schweigfels am Pass (≈ 3,3 / 1,1) |
| **Dorunsruh** | R08 | 4,8 / 3,3 | Am Ruinenrand | Akademie-HQ |
| **Prismara** | R09 | 2,9 / 3,0 | **Unterirdisch** (−180 m), Zugang über Kraterlift | Akt III |
| **Aerion** | R10 | 4,1 / 3,1 | Himmelsstadt auf 1.800 m | Akt III, Finale |

### 5.2 Wegenetz (Bundesstraßen)

Wegfaktor 1,35 (Kurven/Gelände) auf Luftlinie. Laufzeiten: Joggen 4,2 m/s, Bodenreiten 14 m/s (K02 §4.1).

| Verbindung | Wegstrecke | Joggen | Reiten |
|---|---|---|---|
| Lindwiesen – Eichenhall | 1,5 km | 6 min | 1,8 min |
| Eichenhall – Saltrand-Hafen | 3,0 km | 12 min | 3,5 min |
| Eichenhall – Prismtiefen-Kraterrand (Prismara-Lift) | 2,5 km | 10 min | 2,9 min |
| Eichenhall – Qasr Sahrun | 2,5 km | 10 min | 3,0 min |
| Eichenhall – Morvenfurt | 3,8 km | 15 min | 4,5 min |
| Kraterrand – Kharsholm | 2,1 km | 8 min | 2,5 min |
| Kharsholm – Hvitmark | 2,0 km | 8 min | 2,4 min |
| Kharsholm – Dorunsruh | 1,7 km | 7 min | 2,0 min |
| Morvenfurt – Dorunsruh | 2,2 km | 9 min | 2,6 min |
| Morvenfurt – Schlackenwehr | 2,5 km | 10 min | 3,0 min |
| Morvenfurt – Qasr Sahrun | 2,3 km | 9 min | 2,7 min |
| Dorunsruh – Schlackenwehr | 2,6 km | 10 min | 3,1 min |
| Saltrand-Hafen – Kraterrand | 3,1 km | 12 min | 3,7 min |

```
                               Hvitmark
                                  │ 2,0
            Kraterrand ──2,1── Kharsholm ──1,7── Dorunsruh ──2,6── Schlackenwehr
          (Prismara-Lift)                          │ 2,2                │ 2,5
         3,1 /     \ 2,5                           │                    │
 Saltrand-Hafen     Eichenhall ─────────3,8─────── Morvenfurt ──────────┘
            \ 3,0  /  │ 1,5   \ 2,5                │ 2,3
             ──────   │        Qasr Sahrun ────────┘
                   Lindwiesen
```

**Querung der ganzen Welt** (Saltrand → Schlackenwehr): ~7,3 km Weg ≈ 29 min joggend / 9 min reitend. Ziel aus K02: Region in 4–7 h „durchdringen“ – die Dichte, nicht die Größe, trägt die Spielzeit.

---

## 6. Zonen & Level-Bänder

Daten: `Data/World/Zones.csv` (50 Zonen), `Data/World/ZoneTiers.csv` (7 Stufen). Prinzip aus CANON §15: Feste Regionen (R01, R09, R10) haben feste Bänder; frei wählbare Regionen nutzen **Stufenbänder**, beim ersten Betreten anhand der Akkordzahl **einmalig fixiert**.

### 6.1 Stufenbänder

| Stufe | Akkorde beim Betreten | Band | Gilt für |
|---|---|---|---|
| T1 | 1 | 10–18 | R02, R03, R06 (Akt I) |
| T2 | 2 | 15–23 | R02, R03, R06 |
| T3 | 3 | 20–28 | R02, R03, R06 |
| T4 | 4 | 25–35 | R04, R05, R07 (Akt II) |
| T5 | 5 | 31–41 | R04, R05, R07 |
| T6 | 6 | 37–47 | R04, R05, R07, R08 |
| T7 | 7 | 43–55 | R04, R05, R07, R08 |

Stufe = `Clamp(Akkorde, MinTier, MaxTier)` der Region. Zonenband = `[TierMin + OffMin, min(TierMax, TierMin + OffMax)]`.

### 6.2 Zonenübersicht

| Region | Zonen (Offsets bzw. feste Level) |
|---|---|
| **R01 Verdanthain** (fest) | Z01 Lindwald 2–5 · Z02 Lindwiesen-Auen 4–8 · Z03 Eichenhall-Forst 6–10 · Z04 Moosgrund-Hügel 7–11 · Z05 Farnschlucht 8–12 · Z06 Uralthain 10–14 |
| **R02 Kharsgrat** (T1–T3) | Z01 Brakkfels-Ausläufer +0..4 · Z02 Kharsholm-Terrassen +1..5 · Z03 Grollschlund +2..6 · Z04 Erzgrat +3..7 · Z05 Grollhorn-Gipfel +5..8 |
| **R03 Morvenmoor** (T1–T3) | Z01 Fennhaven-Ried +0..4 · Z02 Morvenfurt-Kanäle +1..5 · Z03 Duvreth-Sümpfe +2..6 · Z04 Nebelwald Corrach +3..7 · Z05 Versunkene Senke +5..8 |
| **R06 Saltrand** (T1–T3) | Z01 Dünenküste +0..4 · Z02 Tangwerft-Bucht +1..5 · Z03 Kliffsund +2..6 · Z04 Leuchtfelsen +3..7 · Z05 Riffgrund +5..8 |
| **R04 Sahrun-Weite** (T4–T7) | Z01 Harrâd-Oase +0..5 · Z02 Mirsaan-Dünen +2..7 · Z03 Glasebene +3..8 · Z04 Sonnenhof-Plateau +4..9 · Z05 Tiefe Weite +6..12 |
| **R05 Ignareth** (T4–T7) | Z01 Aschefelder +0..5 · Z02 Schlackenwehr-Hang +2..7 · Z03 Vorthax-Schlackenstrom +3..8 · Z04 Obsidianklamm +4..9 · Z05 Ignar-Krater +6..12 |
| **R07 Hvitfell** (T4–T7) | Z01 Fjallstad-Tal +0..5 · Z02 Eiðvik-Ruinen +2..7 · Z03 Schweigfels-Pass +3..8 · Z04 Gletscherzunge +4..9 · Z05 Isvaldtind +6..12 |
| **R08 Ael'Dorun** (T6–T7) | Z01 Dorunsruh-Vorstadt +0..5 · Z02 Säulenfeld Thae'Luun +2..7 · Z03 Archontenviertel +4..9 · Z04 Thronstadt +6..12 |
| **R09 Prismtiefen** (fest) | Z01 Glanzschacht 50–54 · Z02 Quarzgrund 52–56 · Z03 Prismara-Kaverne 53–57 · Z04 Missklang-Adern 55–60 · Z05 Tiefe Resonanz 58–62 |
| **R10 Nimbara** (fest) | Z01 Windstufen 58–62 · Z02 Lumeya-Inseln 60–64 · Z03 Gärten von Aerion 62–66 · Z04 Kronenwerft 64–68 · Z05 Sternenarena 66–70 |

**Prüfung (automatisiert):** Alle Bänder sind in jeder möglichen Stufe gültig (min ≤ max); die Gesamtkorridore entsprechen CANON §15 (Akt I 5–28, Akt II 25–55, Akt III 50–70).

### 6.3 Sonderregeln

| Regel | Beschreibung |
|---|---|
| Alphatiere & Seltene | +3 bis +8 über Zonenband (K02 §9.3) |
| **Nachhall** (Post-Game) | Jede Zone erhält zusätzliche **Nachhall-Spawns** auf 72–90 (Data Layer, §10.3) – die regulären Bänder bleiben erhalten (Machtgefühl), Endgame-Herausforderung kommt hinzu |
| Prolog-Grenze | R01_Z01 ist bis Ende Prolog durch die Linn begrenzt (Brücke eingestürzt → wird in MQ_A0 repariert) |

---

## 7. Traversal-Gates & Metroidvania-Struktur

Umsetzung von DR-28 (Hauptpfad mit frühester Ausstattung spielbar; spätere Fähigkeiten öffnen Optionales).

| Fähigkeit | Verfügbar ab (CANON §15) | Öffnet (Beispiele) | Anteil optionaler Fläche |
|---|---|---|---|
| Klettern + Ausdauer | Prolog | Felsen, Bäume (nicht Eis/Kristall/nasser Fels) | Basis |
| Gleiter | Prolog-Ende | Abkürzungen von Höhen, Kraterrand-Abstieg (Teile) | – |
| Bodenreiten | nach Akkord 1 | schnelle Wege | – |
| Schwimmreiten | Akt I (Saltrand/Morvenmoor) | Riffgrund (R06_Z05), Tiefsumpf (R03_Z05), Linn-Inseln | ~6 % |
| Kletterreiten | Akt I (Kharsgrat) | Grollhorn-Gipfel (R02_Z05), Klippen-Nester in R06 | ~5 % |
| Grabreiten | Akt II (Sahrun) | Sandhöhlen, verschüttete Ruinen in R08, Erzadern R02/R05 | ~5 % |
| Flugreiten | Akt II, nach 6 Akkorden | Lumeya-Außeninseln (R10), Gipfelhorste aller Regionen | ~4 % |

**Rückkehr-Anreiz:** Jede Region enthält **mindestens 3** POIs, die nur mit einer später erhaltenen Reitfähigkeit erreichbar sind (Validator zählt Gate-Tags an POIs, §10.4).

---

## 8. Resonanzsteine & Schnellreise

| Regel | Wert |
|---|---|
| Anzahl | 80 (CANON §19), davon 10 Stadtsteine, 22 Dorfsteine, 48 Wildsteine (Außenposten haben Wildsteine in ≤ 150 m) |
| Abstand | Kein Punkt des Hauptpfads > **900 m** vom nächsten Stein |
| Aktivierung | Physisch berühren (Resonanzsinn zeigt nicht aktivierte Steine im Radius 300 m) |
| Kosten | Keine (DR-23) |
| Einschränkungen | Nicht im Kampf; Koop-Gäste reisen nur zum Host |
| Nimbara | Nach Akt-III-Ankunft verbinden sich 9 Steine in R10; vorher nur Story-Zugang |
| Prismtiefen-Höhlen | Steine erst nach Aktivierung von unten (Entdeckungsdruck in Akt III) |

---

## 9. POI-Dichte & Level-Design-Metriken

### 9.1 POI-Typen und Verteilung pro Region (Ziel ≈ 1.115 gesamt)

| POI-Typ | Anteil | Beschreibung |
|---|---|---|
| Echo-Habitat (Nest, Bau, Tränke, Schlafplatz) | 25 % | Ökologie-Hotspots (K52) |
| Ressourcenfeld | 15 % | Holz/Erz/Kristall/Kräuter (K41) |
| Ruine / Umwelt-Erzählung | 12 % | inkl. Klangfragmente |
| Klangrätsel | 8 % | Feldfähigkeiten nötig |
| Aussichtspunkt | 5 % | ≥ 3 neue POIs sichtbar (K02 §4.1) |
| Lauscherschrein | 5 % | kleine Buffs (K07 §10) |
| NPC-Begebenheit (Reisende, Händler, Wärter) | 12 % | Mini-Quests, Kämpfe |
| Höhle / Mini-Dungeon | 4 % | Teil der 37 Dungeons (CANON §19) oder Kleinsthöhlen |
| Schatzfund / Cache | 8 % | Klangschriften, Material |
| Traversal-Herausforderung | 6 % | Kletterwand, Gleitparcours |

### 9.2 Metriken (LOCKED für Blockouts)

| Metrik | Wert |
|---|---|
| POI-Abstand | Ø 150–250 m, max. 400 m (K02 DR-26) |
| Klangbrunnen-Abstand Hauptpfad | ≤ 800 m (DR-30) |
| Wegbreite Bundesstraße / Pfad | 6 m / 2,5 m |
| Kampfkreis-Fläche frei | Radius 12–18 m (ADR-013) – Level Design hält auf Pfaden alle 250 m eine ausreichend ebene Fläche frei |
| Sichtachsen | Wahrzeichen jeder Region (Turm, Baum, Krater, Vulkan) aus ≥ 2 km sichtbar |
| Kletterbare Wandhöhe ohne Rast | ≤ 60 m (Ausdauer 100 / 8 pro s ≈ 12,5 s × 1,6 m/s ≈ 20 m pro Ausdauerbalken; Rastvorsprünge alle 20 m) |

---

## 10. Technische Umsetzung: World Partition

### 10.1 Weltaufbau

| Thema | Festlegung |
|---|---|
| Persistentes Level | `L_Aethris_World` (eine Karte für Boden + Himmel) |
| Koordinaten | 1 m = 100 UU. Karten-km (x, y) → UE: `X = (x − 4,0) · 100.000`, `Y = (y − 3,5) · 100.000` (Karten-y zeigt nach Süden); Z = Höhe |
| Landscape | 8,1 × 7,1 km, Komponenten 255 Quads, 1 m Auflösung, Höhe −600 … +2.800 m (Prismtiefen-Krater per Landscape-Loch + Höhlen-Meshes) |
| Himmelinseln | Statische Nanite-Meshes + Level Instances in eigenem Streaming-Gitter |
| Höhlen (Prismtiefen) | Level Instances, Streaming über **eigenes Grid** `Underground` |

### 10.2 Streaming-Gitter

| Grid | Zellgröße | Ladereichweite | Inhalt |
|---|---|---|---|
| `MainGrid` | 128 m | 768 m (PS5/PC), 512 m (Switch 2) | Umgebung, Props, POIs |
| `FarGrid` | 512 m | 3.000 m | Große Landmarken, Wahrzeichen (Nanite), Stadtsilhouetten |
| `Underground` | 64 m | 256 m | Höhlen, Prismara |
| `Sky` | 256 m | 2.000 m | Nimbara |
| HLOD | 3 Ebenen (Instancing → Merged → Simplified) | bis Weltgrenze | Fernsicht |

### 10.3 Data Layers (LOCKED-Struktur)

| Data Layer | Typ | Inhalt |
|---|---|---|
| `DL_Base` | Runtime, immer | Basiswelt |
| `DL_Story_R##_Silence` | Runtime | Stillezonen-Zustand je Region (aktiv bis Lösung) |
| `DL_Story_R##_Healed` | Runtime | Geheilter Zustand (neue Flora, NPCs) |
| `DL_Story_Gates` | Runtime | Sandsturm-/Asche-/Schneesturm-Barrieren, Ruinensiegel |
| `DL_Nachhall` | Runtime | Post-Game-Ergänzungen |
| `DL_Event_*` | Runtime | LiveOps-Events (K68) |
| `DL_Editor_Blockout` | Editor-only | Graybox-Referenzen |

### 10.4 Validatoren (Editor/CI)

| Prüfung | Regel |
|---|---|
| Regionsfläche | Landscape-Regionsmaske ±3 % der Zellfläche aus `MacroRegions.csv` |
| POI-Dichte | Kein Punkt des Hauptpfads > 400 m vom nächsten POI |
| Brunnen/Steine | DR-30 (800 m), Steine 900 m |
| Gates | ≥ 3 Rückkehr-POIs pro Region (§7) |
| Kampfkreis-Flächen | Alle 250 m eines Hauptpfads ≥ 1 Navmesh-Fläche mit Radius 12 m |

---

## 11. Code: Zonenauflösung

Implementiert das Prinzip „einmalig fixiert“ (CANON §15) mit den Daten aus §6. Lebt in `GF_World` (Domain).

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Public/Zones/ZoneTypes.h
/** Zeile aus Data/World/Zones.csv. */
USTRUCT(BlueprintType)
struct GF_WORLD_API FZoneRow : public FTableRowBase
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere) FName RegionId;
	UPROPERTY(EditAnywhere) FText DisplayName;
	UPROPERTY(EditAnywhere) FName Mode;                 // FIXED | SCALED
	UPROPERTY(EditAnywhere) int32 MinTier = 0, MaxTier = 0;
	UPROPERTY(EditAnywhere) int32 MinLevel = 0, MaxLevel = 0;
	UPROPERTY(EditAnywhere) int32 OffMin = 0, OffMax = 0;
};

/** Zeile aus Data/World/ZoneTiers.csv. */
USTRUCT(BlueprintType)
struct GF_WORLD_API FZoneTierRow : public FTableRowBase
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere) int32 Tier = 1;
	UPROPERTY(EditAnywhere) int32 MinLevel = 1, MaxLevel = 1;
};

/** Ergebnis: Level-Band einer Zone. */
USTRUCT(BlueprintType)
struct GF_WORLD_API FLevelBand
{
	GENERATED_BODY()
	UPROPERTY(SaveGame) int32 Min = 1;
	UPROPERTY(SaveGame) int32 Max = 1;
};
```

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Private/Zones/ZoneLevelSubsystem.cpp (Auszug)
FLevelBand UZoneLevelSubsystem::ResolveBand(FName ZoneId)
{
	// 1) Bereits fixiert? → unverändert zurückgeben (Machtgefühl bei Rückkehr, ADR-012).
	if (const FLevelBand* Fixed = FixedBands.Find(ZoneId))
	{
		return *Fixed;
	}

	const FZoneRow* Zone = ZoneTable->FindRow<FZoneRow>(ZoneId, TEXT("ResolveBand"));
	check(Zone);

	FLevelBand Band;
	if (Zone->Mode == TEXT("FIXED"))
	{
		Band = { Zone->MinLevel, Zone->MaxLevel };
	}
	else
	{
		const int32 Akkorde = WorldState()->GetAkkordCount();
		const int32 Tier = FMath::Clamp(Akkorde, Zone->MinTier, Zone->MaxTier);
		const FZoneTierRow& T = *TierTable->FindRow<FZoneTierRow>(*FString::Printf(TEXT("T%d"), Tier), TEXT("Tier"));
		Band.Min = T.MinLevel + Zone->OffMin;
		Band.Max = FMath::Min(T.MaxLevel, T.MinLevel + Zone->OffMax);
	}

	// 2) Fixieren + persistieren (Save-Fragment "World.Zones", ISaveFragmentProvider).
	FixedBands.Add(ZoneId, Band);
	UAethrisEventBus::Get(this).Broadcast(AethrisTags::Event_World_Zone_BandFixed, FZoneBandFixedMsg{ZoneId, Band.Min, Band.Max});
	return Band;
}
```

**Wichtig:** Eine *Region* wird beim ersten Betreten **einer ihrer Zonen** komplett fixiert (alle Zonen derselben Region erhalten dieselbe Stufe), damit Regionen in sich stimmig bleiben. Der Subsystem-Code ruft dazu `ResolveBand` für alle Zonen der Region beim ersten Betreten auf.

---

## 12. Decision Records

### ADR-042 – Makrokarte als generierte, validierte Rasterdatei
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Handgezeichnete Konzeptkarte | Künstlerisch frei | Flächen driften unbemerkt vom Budget weg |
| (b) Rasterdatei aus Skript + Budget | Beweisbar korrekt, diffbar, Grundlage für Validatoren | Grobe Konturen (200 m) |
- **Entscheidung:** (b) als Blockout-Grundlage; Feinkonturen im Landscape mit ±3 %-Toleranz.

### ADR-043 – Welt faltet sich zur Mitte
- **Entscheidung:** Akt I nahe Start, Akt II am Rand + Zentrum, Akt III unter/über dem Zentrum. Vorteil: Das Finale ist von überall sichtbar (Nimbara am Himmel ab Minute 1, Gleitpanorama im Onboarding). Nachteil: Zentrum muss lange „geschlossen“ wirken → diegetische Ruinensiegel + Stillezonen-Nebel.

### ADR-044 – Regionsweise Stufenfixierung
- **Entscheidung:** Erste Betretung einer Zone fixiert alle Zonen der Region (§11). Verhindert Level-Sprünge innerhalb einer Region bei zwischenzeitlichem Akkord-Gewinn.

### ADR-045 – Höhen auf ~40 % skaliert
- **Entscheidung:** Gebirge niedriger als realistisch, Größe über Atmosphäre und Skybox inszeniert. Vorteil: Traversal-Tempo; Nachteil: weniger „Gipfel-Epik“ → Mitigation: Wolkenschichten unter Gipfeln, Nimbara über allem.

---

## 13. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §39 | Makrokarte `Data/World/MacroMap.txt` (40×35, 200 m), Generator `tools/gen_macromap.py`, Regionswerte `MacroRegions.csv` | LOCKED |
| §39 | Lage: Hvitfell N, Kharsgrat N-Mitte, Prismtiefen-Krater W-Mitte, Ael'Dorun Zentrum, Ignareth O, Saltrand W-Küste, Verdanthain SW-Mitte (Start), Morvenmoor SO-Mitte, Sahrun S; Nimbara über dem Zentrum (1.400–2.600 m) | LOCKED |
| §39 | Koordinatenabbildung Karte → UE (§10.1) | LOCKED |
| §40 | 50 Zonen (`Zones.csv`), 7 Stufenbänder (`ZoneTiers.csv`), regionsweise Fixierung (ADR-044), Nachhall-Spawns 72–90 | LOCKED |
| §41 | Ortskoordinaten der 10 Städte + Lindwiesen; Prismara unterirdisch (−180 m, Kraterlift), Aerion 1.800 m, Kloster Schweigfels am Pass | LOCKED |
| §41 | Wegenetz (13 Verbindungen), Weltquerung ~29 min joggend / 9 min reitend | LOCKED |
| §42 | Höhenprofil (§4.1), Flüsse Linn/Morve, Ignar-Lavastrom, Kristallsee, Weltgrenzen ohne unsichtbare Wände | LOCKED |
| §42 | Story-Gates: Sandsturm (R04), Ascheschleier (R05), Pass-Schneesturm (R07), Ruinensiegel (R08) | LOCKED |
| §42 | Traversal-Gates, ≥ 3 Rückkehr-POIs pro Region | LOCKED |
| §42 | Resonanzsteine 10 Stadt + 22 Dorf + 48 Wild, max. 900 m Abstand, kostenlos | LOCKED |
| §42 | POI-Typverteilung und LD-Metriken (§9) | LOCKED |
| §43 | World Partition: `L_Aethris_World`, Grids Main 128 m/768 m (Switch 2: 512 m), Far 512 m/3 km, Underground 64 m/256 m, Sky 256 m/2 km; 3 HLOD-Ebenen; Data Layers (§10.3) | LOCKED |
| §10 | ADR-042 – ADR-045 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Generierte, validierte Makrokarte (Boden + Himmel) im Repository
- [x] Regionslage, Flächen, Schwerpunkte, Nachbarschaften, Übergänge
- [x] Höhenprofil, Gewässer, Weltgrenzen ohne unsichtbare Wände
- [x] 11 Hauptorte mit Koordinaten, Wegenetz mit Distanzen und Reisezeiten
- [x] 50 Zonen mit Level-Bändern, 7 Stufenbänder, automatisierte Bandprüfung
- [x] Traversal-Gates und Rückkehr-Struktur
- [x] Resonanzstein-Regeln
- [x] POI-Typverteilung, Level-Design-Metriken
- [x] World Partition: Gitter, HLOD, Data Layers, Validatoren
- [x] Code: Zonen-Datenstrukturen und Band-Auflösung
- [x] ADR-042 – ADR-045, CANON aktualisiert

➡️ **Nächstes Kapitel: K09 – Biome I: Verdanthain, Kharsgrat, Morvenmoor, Sahrun-Weite, Ignareth.**
