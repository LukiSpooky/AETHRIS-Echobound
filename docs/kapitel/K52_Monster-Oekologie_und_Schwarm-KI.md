# K52 · Monster-Ökologie und Schwarm-KI

| Feld | Wert |
|---|---|
| Dokument | Kapitel 52 von 68 · Lebendige Welt I |
| Version | 1.0 |
| Owner | Lead AI Engineer |
| Mitwirkende | Creature Designer, Systems Designer, Gameplay Programmer (Mass), Technical Animator, Level Design |
| Baut auf | K16 (CD-09 Ökologie-Fragment, Verhaltensvokabular), K14/K15 (Wetter, Tageszeit, Mond, Aktivitätskurven), K08 (Zonen), K20–K27 (Arten), K34 (Kampf-KI), K36 (Bindung, Lockmittel, Fallen), CANON §9 (Mass, StateTree), §29 (Seed-Hierarchie, Fork 2), DR-02, DR-12, DR-13, DR-14 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Ecology/` (`GroupBehaviors.csv`, `PopulationTuning.csv`, `PerceptionProfiles.csv`, generiert: `EcologyFragments.csv`, `FoodWeb.csv`), `tools/ref/aethris_ecology.py` (Referenzmodell + Validator EC-01–EC-05), `GF_Monsters/Public/Ecology/EchoEcologyFragment.h`, `GF_AI/Public/Ecology/EchoMassFragments.h` (+ `.cpp`) |
| Neue Kanon-Einträge | CANON §196 (Rollen, Fragment, Nahrungsnetz), §197 (Spawn), §198 (Population), §199 (Gruppen, Verhalten, Wahrnehmung), §200 (Sim-LOD) |

---

## Inhalt

1. [Leitbild](#1-leitbild)
2. [Ökologische Rollen](#2-ökologische-rollen)
3. [Das Ökologie-Fragment](#3-das-ökologie-fragment)
4. [Nahrungsnetz und Klangbiss](#4-nahrungsnetz-und-klangbiss)
5. [Spawn-System](#5-spawn-system)
6. [Populationsdynamik](#6-populationsdynamik)
7. [Gruppen- und Schwarmverhalten](#7-gruppen--und-schwarmverhalten)
8. [Verhaltenszustände](#8-verhaltenszustände)
9. [Wahrnehmung und Begegnung](#9-wahrnehmung-und-begegnung)
10. [Sim-LOD und Mass](#10-sim-lod-und-mass)
11. [Reaktionen auf die Welt](#11-reaktionen-auf-die-welt)
12. [Einfluss des Spielers](#12-einfluss-des-spielers)
13. [Validierung, Debug, Telemetrie](#13-validierung-debug-telemetrie)
14. [Anforderungen an andere Abteilungen](#14-anforderungen-an-andere-abteilungen)
15. [Decision Records](#15-decision-records)
16. [Kanon-Änderungen](#16-kanon-änderungen)
17. [Kapitel-Checkliste](#17-kapitel-checkliste)

---

## 1. Leitbild

> *Die Welt singt, auch wenn niemand zuhört.* (DR-12)

Echos sind keine Spawns, die um den Spieler herum erscheinen, sondern Bewohner mit Nahrung, Schlafplatz, Gruppe und Gewohnheit. Wer früh am Morgen an die Lindwiesen-Auen kommt, sieht Rillos aufbrechen; wer nachts im Morvenmoor wartet, sieht Lauerjäger im Wasser. Vier Grundsätze:

| Grundsatz | Bedeutung | Regel |
|---|---|---|
| **Beobachtbar** | Jedes Verhalten ist sichtbar und lesbar (Kodex, DR-02) | Zustände haben Animation, Laut und Spur |
| **Verbunden** | Jedes System beeinflusst mindestens zwei andere (DR-13) | Wetter → Spawn, Bestand → Spawn, Räuber → Beute, Spieler → Bestand |
| **Deterministisch, wo es zählt** | Gleiche Welt, gleiche Spawns (Koop, Replays, Tests) | Spawnauswahl über Fork(2) je Zone (CANON §29) |
| **Kein Tod** | Echos erschöpfen, verklingen, erholen sich (ADR-007) | Räuber nehmen **Klang**, nicht Leben (§4) |

---

## 2. Ökologische Rollen

Die Rolle einer Art folgt aus ihren Verhaltensmerkmalen (K16 Vokabular, `BehaviorTraits.csv`):

| Rolle | Merkmale | Ernährung | Anteil |
|---|---|---|---|
| **Primärverbraucher** | Grazer, Pollinator, Filterer, Lithophage, Sunbather, Thermal | Pflanzen, Nektar, Schwebstoffe, Erz/Kristall, Licht, Wärme | Basis des Netzes |
| **Räuber** | Hunter, Ambusher | **Klangbiss** bei anderen Echos | Spitze, wenige Individuen |
| **Klangsammler** | Scavenger | Klangreste erschöpfter Echos, Abfälle | Schließt den Kreislauf |
| **Allesverwerter** | alle übrigen | typabhängig (Tau, Insekten, Stille, Erinnerungsklang …) | Breite Mitte |

Verteilung über alle Wildarten (Arten mit Spawnzonen; Ursprungsstimmen und Mythische ausgenommen):

| Region | Primärverbraucher | Räuber | Klangsammler | Allesverwerter | Arten |
|---|---|---|---|---|---|
| R01 | 5 | 2 | 0 | 15 | 22 |
| R02 | 5 | 2 | 0 | 14 | 21 |
| R03 | 2 | 9 | 1 | 8 | 20 |
| R04 | 7 | 5 | 0 | 8 | 20 |
| R05 | 7 | 2 | 2 | 6 | 17 |
| R06 | 5 | 3 | 1 | 11 | 20 |
| R07 | 2 | 3 | 0 | 12 | 17 |
| R08 | 2 | 0 | 2 | 12 | 16 |
| R09 | 2 | 5 | 0 | 9 | 16 |
| R10 | 2 | 1 | 0 | 15 | 18 |
| **Σ** | **39** | **32** | **6** | **110** | **187** |

**Regionale Spitzen** (K09/K10 „trophische Struktur“): In Ael'Dorun stehen keine Jäger an der Spitze, sondern **Leere-Klangsammler am Zonenrand** (Tilgel, Tilgrath, K10 §4) – sie leben von dem, was Stillezonen und Kämpfe zurücklassen. Validator EC-04 verlangt deshalb je Region Räuber **oder** Klangsammler.

---

## 3. Das Ökologie-Fragment

K16 (CD-09) verlangt für jede Art Nahrung, Schlafplatz, Fortpflanzung und Fressfeinde/Beute. K52 liefert dieses Fragment (`UEchoEcologyFragment`, GF_Monsters) und erzeugt es aus den Artdaten, damit 187 Wildarten konsistent sind. Writer und Creature Designer dürfen jeden Wert überschreiben; der Generator füllt nur, was fehlt.

| Feld | Ableitung |
|---|---|
| Rolle | Merkmale (§2) |
| Nahrung | Merkmal (Grazer → Gräser/Moos …); sonst Primärtyp (Glut → Wärme und Glut, Leere → Stille, Geist → Erinnerungsklang …) |
| Schlafplatz | Erstes passendes Merkmal: Gräber → Bau, Nestbauer → Nest, Schwimmer → Unterwasser-Höhle, Flieger → Horst, Kletterer → Baumkrone/Felswand, Getarnt → an Ort und Stelle, Wärmesucher → warmer Stein; sonst geschützte Stelle im Habitat |
| Fortpflanzung | Archetyp (Vogel → Gelege im Nest, Fisch → Laich, Schwebend amorph → Klangteilung, Konstrukt → Resonanzkeim aus Material, Pflanzenwesen → Ableger, Drache → Gelege im Horst …); sonst Resonanzkeim (Wurf 1–3) |
| Gruppe | Erstes Gruppenmerkmal: Schwarm, Herde, Rudel, Familienverband, Einzelgänger; sonst lose Gruppe |
| Tragfähigkeit / Mindestbestand | §6 |
| Beute | Nahrungsnetz §4 |

Beispiel Verdanthain:

| Art | Rolle | Nahrung | Schlafplatz | Fortpflanzung | Gruppe |
|---|---|---|---|---|---|
| Fernlit | Allesverwerter | Pflanzensäfte | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Familienverband |
| Brokk | Allesverwerter | Mineralsalze | Bau im Boden | Resonanzkeim (Wurf von 1–3) | Lose Gruppe |
| Wisplet | Allesverwerter | Insekten im Wind | Horst oder Felsvorsprung | Gelege im Nest | Lose Gruppe |
| Chimkin | Allesverwerter | Klang anderer Lebewesen (ohne zu schaden) | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Lose Gruppe |
| Chimbal | Allesverwerter | Klang anderer Lebewesen (ohne zu schaden) | Baumkrone oder Felswand | Resonanzkeim (Wurf von 1–3) | Lose Gruppe |
| Cantaroth | Allesverwerter | Klang anderer Lebewesen (ohne zu schaden) | Baumkrone oder Felswand | Resonanzkeim (Wurf von 1–3) | Lose Gruppe |
| Mossling | Primärverbraucher | Gräser, Moos, Blätter | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Herde |
| Myrthorn | Primärverbraucher | Gräser, Moos, Blätter | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Herde |
| Lumpip | Primärverbraucher | Gräser, Moos, Blätter | Geschützte Stelle im Habitat | Eier in Kammern | Lose Gruppe |
| Lumow | Primärverbraucher | Nektar, Pollen, Tau | Horst oder Felsvorsprung | Eier in Kammern | Lose Gruppe |
| Phantalume | Allesverwerter | Erinnerungsklang an alten Orten | Geschützte Stelle im Habitat | Klangteilung | Einzelgänger |
| Rillo | Allesverwerter | Algen, Plankton | Unterwasser-Höhle | Laich im Flachwasser | Familienverband |
| Rillward | Allesverwerter | Algen, Plankton | Unterwasser-Höhle | Laich im Flachwasser | Lose Gruppe |
| Sporlet | Allesverwerter | Pilze, Moder | Getarnt an Ort und Stelle | Ableger | Lose Gruppe |

Beispiel Ignareth:

| Art | Rolle | Nahrung | Schlafplatz | Fortpflanzung | Gruppe |
|---|---|---|---|---|---|
| Pyrolm | Primärverbraucher | Wärme (Lava, Quellen) | Warmer Stein, Quelle | Laich im Flachwasser | Lose Gruppe |
| Pyrolax | Primärverbraucher | Wärme (Lava, Quellen) | Unterwasser-Höhle | Laich im Flachwasser | Lose Gruppe |
| Ambolt | Allesverwerter | Erzstaub | Geschützte Stelle im Habitat | Resonanzkeim aus Material | Lose Gruppe |
| Ambrak | Primärverbraucher | Wärme (Lava, Quellen) | Warmer Stein, Quelle | Resonanzkeim aus Material | Lose Gruppe |
| Aschwel | Klangsammler | Klangreste erschöpfter Echos, Abfälle | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Rudel |
| Aschund | Räuber | Klangbiss bei anderen Echos (Resonanz, nie Fleisch) | Geschützte Stelle im Habitat | Resonanzkeim (Wurf von 1–3) | Rudel |
| Obsikin | Primärverbraucher | Erz, Kristall, Schlacke | Getarnt an Ort und Stelle | Gelege im Sand oder Schlamm | Lose Gruppe |
| Obsidar | Primärverbraucher | Erz, Kristall, Schlacke | Getarnt an Ort und Stelle | Gelege im Sand oder Schlamm | Lose Gruppe |
| Ignavyr | Primärverbraucher | Wärme (Lava, Quellen) | Horst oder Felsvorsprung | Gelege im Horst | Lose Gruppe |
| Fumel | Allesverwerter | Stille (Pausen im Klang) | Getarnt an Ort und Stelle | Klangteilung | Lose Gruppe |

---

## 4. Nahrungsnetz und Klangbiss

### 4.1 Der Klangbiss

Echos sind Obertöne des Weltlieds (K07 §3). Räuber-Echos ernähren sich nicht von Körpern, sondern von **Klang**: Ein Klangbiss nimmt der Beute einen Teil ihrer Resonanz. Die Beute ist danach **erschöpft** – sie zieht sich an ihren Schlafplatz zurück, ihr Klangmal glimmt schwächer, nach einer Spielstunde ist sie erholt. Klangsammler finden die Reste. So bleibt das Netz lebendig, sichtbar und gewaltarm (ADR-007, ADR-196).

```
  Primärverbraucher ──(Klangbiss)──► Räuber          Spieler sieht: Jagd, Flucht, Rückzug
          │                            │
          └──── erschöpft, ruht ───────┴──► Klangreste ──► Klangsammler
                       │
                       └── erholt nach 1 Spielstunde (kein Bestandsverlust, nur Verdrängung)
```

### 4.2 Regeln für Räuber und Beute

| Regel | Inhalt |
|---|---|
| Ort | Beute lebt in derselben Zone oder einer **Nachbarzone** derselben Region (Jagdgebiete reichen über Zonengrenzen; z. B. Versunkene Senke) |
| Größe | Beute höchstens eine Größenklasse größer als der Räuber (Rudel jagen größer) |
| Zeit | ≥ 1 gemeinsame Stunde mit Aktivität ≥ 500 ‰ |
| Linie | Keine Jagd innerhalb derselben Evolutionslinie |
| Auswahl | Bis 3 Beutearten, nach Punktwert (gemeinsame Stunden × 10 + gemeinsame Zonen × 5 + Häufigkeit) |

Das Ergebnis steht in `Data/Ecology/FoodWeb.csv` (93 Räuber-Beute-Beziehungen). Ausschnitte:

**Verdanthain**

| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |
|---|---|---|---|
| Thornkin | S | Diurnal | Pebi, Skirmote, Chimkin |
| Thorncoil | M | Diurnal | Pebi, Skirrow, Chimbal |

**Morvenmoor**

| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |
|---|---|---|---|
| Mirel | S | Nocturnal | Irrlit, Undling, Humbog |
| Blossi | XS | Diurnal | Brinlet, Virmote, Irrlit |
| Blossar | S | Diurnal | Brinlet, Virmote, Irrlit |
| Virwyn | S | Crepuscular | Irrlit, Irrel, Humbog |
| Blightkin | S | Nocturnal | Irrlit, Undling, Mirepip |
| Blightar | M | Nocturnal | Irrlit, Irrel |
| Umbrling | S | Nocturnal | Irrlit, Irrel |
| Umbracoil | M | Nocturnal | Irrlit, Irrel |
| Morhaw | L | Crepuscular | Brinlet, Virmote, Undling |

**Sahrun-Weite**

| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |
|---|---|---|---|
| Solvar | S | Diurnal | Sirrkorn, Skarit, Dunkalb |
| Sengel | S | Diurnal | Sirrkorn, Skarit, Dunkalb |
| Sengar | L | Diurnal | Sirrkorn, Skaral, Dunhorn |
| Stachik | XS | Nocturnal | Vitrel, Vitrapha, Skarit |
| Stacharon | M | Nocturnal | Vitrel, Qadrant, Vitrapha |

**Hvitfell**

| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |
|---|---|---|---|
| Snevar | S | Crepuscular | Hallkid, Vardlit, Uvlet |
| Uvarn | S | Nocturnal | Eidrun, Eidwacht, Lyskin |
| Tysvorn | XL | Nocturnal | Lyskin, Lysmara, Glazil |

**Prismtiefen**

| Räuber | Größe | Aktivität | Beute (bis 3, nach Überschneidung) |
|---|---|---|---|
| Klirrflug | S | Nocturnal | Spatling, Mullit, Psionit |
| Ligrel | S | Nocturnal | Mullit, Klirrit, Spatling |
| Ligrath | M | Nocturnal | Spatling, Klirrit, Misslit |
| Facettor | S | Crepuscular | Spatling, Klirrit, Psionit |
| Miasmar | M | Nocturnal | Mullit, Klirrit, Spatling |

### 4.3 Jagd als sichtbares Ereignis

Eine Jagd ist ein kurzes, sichtbares Schauspiel (15–40 s), nie eine Kampfbegegnung mit dem Spieler:

| Phase | Räuber | Beute | Spieler |
|---|---|---|---|
| Anpirschen | Lauerjäger getarnt, Jäger geduckt | grast weiter | Resonanzsinn zeigt Spannung (gelber Puls) |
| Ausbruch | Sprint, Rudel kreist ein | Fluchtruf; Herde flieht gemeinsam | Kodex-Beobachtung „Jagdverhalten“ |
| Klangbiss | kurzer Lichtblitz am Klangmal | glimmt, zieht sich zurück | – |
| Danach | ruht satt | erschöpft am Schlafplatz | Erschöpfte Echos lassen sich leichter einstimmen (Ruhestufe +1, K36) |

Wenn der Spieler eingreift (Pfiff, Ruf, Begleiter-Ruf), bricht der Räuber ab. Das gibt keine Belohnung und keine Strafe – es ist die Entscheidung des Wärters.

---

## 5. Spawn-System

### 5.1 Zellen und Takt

| Begriff | Wert |
|---|---|
| Spawnzelle | 128 m × 128 m (World-Partition-Zelle, CANON §43) |
| Spawntakt | alle 10 Spielminuten je aktiver Zelle |
| Dichte | 4–9 Gruppen je Zelle (Zielwert nach Biom; Wald 6, Wüste 4, Moor 7, Küste 6, Höhle 5, Himmel 4) |
| Respawn einer Art | `RespawnMinutes` nach Seltenheit (`PopulationTuning.csv`) |
| Mindestabstand Spawn ↔ Spieler | 60 m und außerhalb der Sichtlinie (kein „Aufploppen“) |

### 5.2 Gewicht

```
w(Art) = ⌊⌊⌊⌊Seltenheit × max(80, Aktivität(Stunde)) / 1000⌋ × Wetter(Primärtyp) / 1000⌋
                × Mond / 1000⌋ × Bestand / 1000⌋
  Seltenheit: Common 1000 · Uncommon 400 · Rare 120 · VeryRare 30 (CANON §71)
  Aktivität:  ActivityCurves.csv je Stunde (CANON §67); Höhlen-Regel R09: Nachtaktive ≥ 500 ‰
  Wetter:     WeatherSpawnModifiers.csv (CANON §62)
  Mond:       nachtaktive Arten nachts 800–1200 ‰ (MoonPhases.csv), sonst 1000
  Bestand:    1000 × N / K, mindestens 200 (§6)
  Bedingungen (SpawnConditions) nicht erfüllt → w = 0
```

Umsetzung: `Aethris::Ecology::SpawnWeight` (C++) und `spawn_weights` (Referenz, Python) rechnen identisch.

### 5.3 Deterministische Auswahl

```
rng  ← Weltseed → Fork(2) Spawn → Fork(Zonenschlüssel) → Fork(Spieltag·10000 + Stunde·100 + Zelle·7 + Takt)
x    ← rng.NextBounded(Σw)
Art  ← erste Art, deren kumuliertes Gewicht x übersteigt
Größe← SizeMin + rng.NextBounded(SizeMax − SizeMin + 1)   (GroupBehaviors.csv)
```

Gleiche Welt, gleicher Tag, gleiche Stunde → gleiche Spawns, auch im Koop (Host-Seed, K59). Beispielfolge für die Lindwiesen-Auen (zweimal gerechnet, identisch):

| Tick | Stunde | Zelle | Art | Gruppengröße |
|---|---|---|---|---|
| 0 | 06:00 | 0 | Chimkin | 3 |
| 1 | 13:00 | 1 | Chimkin | 2 |
| 2 | 20:00 | 2 | Rillo | 3 |
| 3 | 01:00 | 0 | Lumpip | 1 |
| 4 | 06:00 | 1 | Skirmote | 34 |
| 5 | 13:00 | 2 | Skirmote | 28 |
| 6 | 20:00 | 0 | Chimkin | 3 |
| 7 | 01:00 | 1 | Lumpip | 3 |

### 5.4 Spawnanteile über den Tag

**Lindwiesen-Auen (R01_Z02), klar**

| Art | Seltenheit | Morgen (06) | Tag (13) | Abend (20) | Nacht (01) |
|---|---|---|---|---|---|
| Chimkin | Common | 16,6 % | 30,6 % | 16,6 % | 6,2 % |
| Mossling | Common | 16,6 % | 30,6 % | 16,6 % | 6,2 % |
| Skirmote | Common | 16,6 % | 30,6 % | 16,6 % | 6,2 % |
| Rillo | Common | 33,3 % | 4,8 % | 33,3 % | 9,4 % |
| Lumpip | Common | 16,6 % | 3,2 % | 16,6 % | 71,6 % |

**Lindwiesen-Auen (R01_Z02), Regen**

| Art | Seltenheit | Morgen (06) | Tag (13) | Abend (20) | Nacht (01) |
|---|---|---|---|---|---|
| Mossling | Common | 18,0 % | 37,5 % | 18,0 % | 10,2 % |
| Skirmote | Common | 13,2 % | 27,5 % | 13,2 % | 7,5 % |
| Chimkin | Common | 12,0 % | 25,0 % | 12,0 % | 6,8 % |
| Rillo | Common | 48,1 % | 7,9 % | 48,1 % | 20,5 % |
| Lumpip | Common | 8,4 % | 1,8 % | 8,4 % | 54,7 % |

**Farnschlucht (R01_Z05), klar**

| Art | Seltenheit | Morgen (06) | Tag (13) | Abend (20) | Nacht (01) |
|---|---|---|---|---|---|
| Pebi | Common | 34,0 % | 32,4 % | 34,0 % | 54,6 % |
| Chimbal | Uncommon | 10,4 % | 18,9 % | 10,4 % | 2,8 % |
| Skirrow | Uncommon | 10,4 % | 18,9 % | 10,4 % | 2,8 % |
| Thornkin | Uncommon | 10,4 % | 18,9 % | 10,4 % | 2,8 % |
| Thorncoil | Rare | 3,1 % | 5,6 % | 3,1 % | 0,8 % |
| Rillward | Uncommon | 20,9 % | 2,9 % | 20,9 % | 4,2 % |
| Lumow | Uncommon | 10,4 % | 1,9 % | 10,4 % | 31,9 % |

Die Tabellen zeigen die Wirkung der Aktivitätskurven: Lumpips beherrschen die Nacht, Rillos die Dämmerungen; Regen hebt Flut- und Blüte-Arten (K14 §7).

---

## 6. Populationsdynamik

### 6.1 Modell

Jede (Zone, Art) hat einen Bestand N. Einmal pro Spieltag (bei Spieltagwechsel, CANON §65) rechnet das System ganzzahlig:

```
Zuwachs   = ⌊r × N × (K − N) / (K × 1000)⌋, mindestens 1 solange N < K
Klangbiss = Σ über Räuber p: ⌊a_p × N_p × N / (1000 × K)⌋
Hunger    = für Räuber: −⌊max(0, N − Beutebestand) / 2⌋
Spieler   = − Bindungen (heute) + Freilassungen (heute, Zone der Freilassung)
N'        = clamp(N + Zuwachs − Klangbiss + Hunger + Spieler, Floor, ⌊1,2 × K⌋)
```

| Name | BaseCapacity | GrowthPermille | PredationPermille | FloorPermille | RespawnMinutes |
|---|---|---|---|---|---|
| Common | 24 | 300 | 120 | 250 | 30 |
| Uncommon | 12 | 220 | 100 | 250 | 60 |
| Rare | 5 | 150 | 80 | 400 | 180 |
| VeryRare | 2 | 100 | 60 | 500 | 360 |

**Tragfähigkeit K** = BaseCapacity × Größenfaktor (XS 1,5 · S 1,3 · M 1,0 · L 0,6 · XL 0,35 · XXL 0,2). **Floor** = Mindestbestand – keine Art verschwindet aus einer Zone (DR-05, ADR-197).

### 6.2 Szenario: Erholung nach einer Stillezone

Nach der Heilung starten alle Bestände der Zone am Floor. Farnschlucht (R01_Z05):

| Art | Rolle | K | Tag 0 | Tag 5 | Tag 10 | Tag 15 | Tag 20 | Tag 25 | Tag 30 |
|---|---|---|---|---|---|---|---|---|---|
| Chimbal | Allesverwerter | 12 | 3 | 8 | 12 | 12 | 12 | 12 | 12 |
| Lumow | Primärverbraucher | 15 | 3 | 8 | 13 | 15 | 15 | 15 | 15 |
| Rillward | Allesverwerter | 12 | 3 | 8 | 12 | 12 | 12 | 12 | 12 |
| Skirrow | Allesverwerter | 15 | 3 | 8 | 13 | 15 | 15 | 15 | 15 |
| Thornkin | Räuber | 15 | 3 | 8 | 13 | 15 | 15 | 15 | 15 |
| Thorncoil | Räuber | 5 | 2 | 5 | 5 | 5 | 5 | 5 | 5 |
| Pebi | Allesverwerter | 31 | 7 | 14 | 23 | 24 | 24 | 24 | 24 |

Nach ~10 Spieltagen (≈ 12 Echtzeitstunden Spiel) ist die Zone wieder voll; die Beute des Räubers (Pebi) pendelt sich unter K ein. Spielerisch heißt das: Geheilte Zonen werden **sichtbar lebendiger** – ein Grund, zurückzukehren (K48 QR-05).

### 6.3 Szenario: Bindungsdruck

Ein Spieler bindet jeden Spieltag einen Thorncoil (Rare) in der Farnschlucht:

| Art | Rolle | K | Tag 0 | Tag 5 | Tag 10 | Tag 15 | Tag 20 | Tag 25 | Tag 30 |
|---|---|---|---|---|---|---|---|---|---|
| Chimbal | Allesverwerter | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Lumow | Primärverbraucher | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Rillward | Allesverwerter | 12 | 12 | 12 | 12 | 12 | 12 | 12 | 12 |
| Skirrow | Allesverwerter | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Thornkin | Räuber | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Thorncoil | Räuber | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 |
| Pebi | Allesverwerter | 31 | 31 | 30 | 30 | 30 | 30 | 30 | 30 |

Der Bestand fällt nur um eins und hält – Mindestzuwachs und Floor verhindern Leerfang. Bestand < 50 % von K senkt das Spawngewicht der Art (Bestandsfaktor), was dem Spieler über den Kodex angezeigt wird („selten geworden“).

### 6.4 Zustände außerhalb des Spiels

Nicht geladene Regionen rechnen **beim Betreten** alle verpassten Spieltage nach (geschlossene Schleife, max. 64 Tage, danach Gleichgewicht). Der Save speichert nur Abweichungen von K (`World.Population`, K64).

---

## 7. Gruppen- und Schwarmverhalten

| DisplayName | SizeMin | SizeMax | Leader | SeparationCm | CohesionPermille | AlignmentPermille | SeparationPermille | WanderRadiusM | FleeMode |
|---|---|---|---|---|---|---|---|---|---|
| Herde | 4 | 10 | Alpha | 180 | 600 | 500 | 700 | 120 | Gemeinsam fliehen; Alpha deckt |
| Rudel | 3 | 6 | Leittier | 250 | 500 | 400 | 600 | 250 | Rückzug nach Leittier |
| Schwarm | 12 | 40 | – | 60 | 800 | 800 | 900 | 60 | Schwarm zerstreut sich und sammelt sich nach 8 s |
| Familienverband | 2 | 4 | Elterntier | 120 | 700 | 300 | 600 | 60 | Jungtiere zuerst |
| Einzelgänger | 1 | 1 | – | 0 | 0 | 0 | 0 | 300 | Einzelflucht |
| Lose Gruppe | 1 | 3 | – | 200 | 300 | 200 | 500 | 100 | Einzelflucht |

### 7.1 Steuerung (ganzzahlig)

```
für jedes Mitglied i (Takt 10 Hz bei Actor, 4 Hz MassNear, 1 Hz MassFar):
  sep  = Σ (p_i − p_j) · (Sep_cm − |p_i − p_j|) / Sep_cm      für Nachbarn mit |p_i − p_j| < Sep_cm
  coh  = (Schwerpunkt der Nachbarn − p_i)
  ali  = mittlere Richtung der Nachbarn
  lead = (Position des Anführers − p_i)                         nur Herde, Rudel, Familie
  home = (Heimpunkt − p_i), nur wenn |p_i − Heim| > WanderRadius
  v_i  = Normiere( sep·SepPermille + coh·CohPermille + ali·AliPermille + lead·600 + home·800 ) · Tempo(Zustand)
```

Nachbarsuche über das Mass-Gitter (Zellgröße = 2 × Separation). Schwärme > 24 Individuen simulieren nur jedes zweite Individuum voll, die übrigen folgen per Offset (Kosten halbiert, visuell gleich).

### 7.2 Anführer und Alpha

| Gruppe | Anführer | Wirkung |
|---|---|---|
| Herde | Alpha (eigene Begegnung, Bindungsschwelle 600, K36) | Gibt Richtung vor; flieht zuletzt; verteidigt Junge |
| Rudel | Leittier | Startet Jagd; ruft Rückzug |
| Familie | Elterntier | Verteidigt Junge (Guardian); Jungtiere fliehen zuerst |
| Schwarm | keiner | Emergent; bei Störung zerstreuen und nach 8 s sammeln |

Wird der Anführer gebunden oder erschöpft, übernimmt das nächstälteste Mitglied nach 1 Spielstunde; bis dahin ist die Gruppe unruhig (Fluchtradius +50 %).

---

## 8. Verhaltenszustände

Jedes Wildecho läuft (als Actor) in einem StateTree, in Mass als vereinfachte Zustandsmaschine mit denselben Zuständen:

| Zustand | Eintritt | Verhalten | Austritt |
|---|---|---|---|
| **Ruhen/Schlafen** | Aktivität < 300 ‰ oder erschöpft | Am Schlafplatz; Wahrnehmung −50 % | Aktivität ≥ 300 ‰, Weckreiz |
| **Nahrung** | Aktivität ≥ 300 ‰, Hunger > 300 ‰ | Weiden, Bestäuben, Filtern, Erz kauen | Hunger < 100 ‰ |
| **Wandern** | sonst | Innerhalb WanderRadius, Gruppenbewegung | Reiz |
| **Sozial** | Verspielt/Tänzer/Sänger, Ruhephase der Gruppe | Spielen, Tanzen, Singen (Rhythmus aus Klangmal) | 30–90 s |
| **Jagen** (Räuber) | Hunger > 500 ‰, Beute in Sicht | §4.3 | Klangbiss oder Abbruch |
| **Fliehen** | Bedrohung im Fluchtradius, Jagd, Sturm | Weg vom Reiz, Gruppe folgt Modus | 8–15 s außerhalb Radius |
| **Neugier** | Curious und Spieler ruhig < ApproachM | Nähert sich, schnuppert, folgt kurz | Spieler läuft/ruft |
| **Revier** | Territorial, Eindringling im Revier | Drohgebärde, dann Angriff (sichtbar) | Eindringling verlässt Revier |
| **Schutz suchen** | Gewitter, Sandsturm, Ascheregen | Unterstand im Habitat | Wetterwechsel |
| **Wandern (Zug)** | Migratory + Weltereignis | Folgt Route (z. B. WE_GRATKIN_MIGRATION) | Ziel erreicht |
| **Verstummt** | In Stillezone | Grau, starr, feindlich (CANON §33) | Zone geheilt → Erwachen-Animation |

Zustände sind sichtbar (Animation, Laut, Klangmal-Helligkeit) – Grundlage für Kodex-Beobachtungen (K39, 768 Aufgaben).

---

## 9. Wahrnehmung und Begegnung

| Name | SightM | HearingM | FleeM | ApproachM | AggroM | ConeDeg | Notes |
|---|---|---|---|---|---|---|---|
| Default | 25 | 15 | 0 | 0 | 0 | 120 | Standard |
| Behavior.Shy | 30 | 20 | 15 | 0 | 0 | 140 | Flieht ab 15 m (BehaviorTraits) |
| Behavior.Curious | 25 | 15 | 0 | 8 | 0 | 120 | Nähert sich bis 8 m bei ruhigem Verhalten (kein Laufen |
| Behavior.Aggressive | 30 | 15 | 0 | 0 | 20 | 120 | Greift ab 20 m an (sichtbare Begegnung |
| Behavior.Territorial | 25 | 20 | 0 | 0 | 12 | 160 | Nur innerhalb des Reviers (Radius 25 m um Heimpunkt) |
| Behavior.Ambusher | 10 | 25 | 0 | 0 | 6 | 90 | Getarnt bis 6 m; Resonanzsinn enthüllt (DR-14 angekündigt) |
| Behavior.Echolocator | 5 | 40 | 0 | 0 | 0 | 360 | Reagiert auf Geräusch statt Sicht: Schleichen halbiert Hörradius |
| Behavior.Guardian | 25 | 15 | 0 | 0 | 10 | 180 | Verteidigt Nest/Jungtiere; sonst neutral |
| Behavior.Sleepy | 10 | 8 | 0 | 0 | 0 | 90 | Ruht oft; Einstimmen +1 Ruhestufe (CANON §67) |
| Behavior.Stargazer | 35 | 15 | 0 | 0 | 0 | 120 | Nachts bei klarem Himmel Sicht +10 m |
| Behavior.Camouflaged | 15 | 15 | 0 | 0 | 0 | 120 | Spieler muss Resonanzsinn nutzen |
| Behavior.Flier | 40 | 15 | 0 | 0 | 0 | 180 | Hohe Sicht; flieht nach oben |
| Behavior.Swimmer | 15 | 20 | 0 | 0 | 0 | 120 | Wahrnehmung unter Wasser; über Wasser halbiert |

### 9.1 Spielerlautstärke

| Spielerhandlung | Geräusch (m) |
|---|---|
| Schleichen | 4 |
| Gehen | 10 |
| Laufen | 20 |
| Reiten (Boden) | 30 |
| Ruf/Pfiff | 40 |
| Kampf in der Nähe | 60 |

Ein Echo hört den Spieler, wenn Geräusch ≥ Abstand − Gehörradius. Klangorter halbieren Schleichen nicht (sie hören alles), aber Stillstehen macht unsichtbar für sie.

### 9.2 Begegnung

Eine Kampfbegegnung beginnt nur, wenn (a) ein Aggressives/Territoriales Echo den Spieler angreift (Aggroradius, sichtbar angekündigt durch Drohgebärde ≥ 1,5 s, DR-14), (b) der Spieler ein Echo anspricht/herausfordert, oder (c) ein Lauerjäger aus der Tarnung bricht (höchstens ein angekündigter Hinterhalt je Quest, QR-07; im freien Gelände durch Resonanzsinn-Puls vorgewarnt). Gruppenformat = Gruppengröße bis zum Format-Maximum (K31/K33: Herde = Format nach Anzahl).

---

## 10. Sim-LOD und Mass

| Stufe | Abstand | Darstellung | Simulation | Takt | Budget (PS5 / Switch 2) |
|---|---|---|---|---|---|
| **Actor** | < 150 m oder in Interaktion | Skeletal Mesh, volle Animation | StateTree, Wahrnehmung, Physik | 10 Hz Entscheidung, Bewegung je Frame | 40 / 16 Actors |
| **MassNear** | 150–500 m | ISM + Vertex-Animation | Zustandsmaschine, Gruppensteuerung | 4 Hz | 400 / 120 Entities |
| **MassFar** | 500 m – Streaming-Grenze | keine (nur Klang-Hinweise) | Wanderung, Zustand, Position grob | 1 Hz | 1.500 / 400 |
| **Statistisch** | außerhalb gestreamter Zellen | – | Bestand je (Zone, Art), Tagestakt | 1/Spieltag | – |

**Übergänge:** Mass → Actor über Pool (vorgewärmt, 8 Actors je Archetyp), Fade-in hinter Deckung; Actor → Mass, wenn > 180 m (Hysterese 30 m) und kein Kampf/keine Bindung.

**Mass-Prozessoren (GF_AI):**

| Prozessor | Aufgabe | Takt |
|---|---|---|
| `UEchoSpawnProcessor` | Zellen-Spawns nach §5, Respawn | 10 Spielmin |
| `UEchoPerceptionProcessor` | Sicht/Gehör gegen Spieler und Räuber | 4 Hz |
| `UEchoGroupSteeringProcessor` | Steuerung §7.1 | 4 / 1 Hz |
| `UEchoBehaviorProcessor` | Zustandswechsel §8 | 4 / 1 Hz |
| `UEchoLODProcessor` | Stufenwechsel, Pool | 2 Hz |
| `UEchoPopulationProcessor` | Tagesrechnung §6 | Spieltagwechsel |

**CPU-Budget Ökologie gesamt:** PS5 ≤ 1,6 ms, Switch 2 ≤ 2,2 ms je Frame (Game-Thread + Worker, K65). Mass läuft auf Worker-Threads; nur Actor-StateTrees auf dem Game-Thread.

---

## 11. Reaktionen auf die Welt

| Ereignis | Reaktion | Systeme |
|---|---|---|
| Regen | Flut/Blüte-Arten häufiger; Grazer ruhen unter Bäumen | Spawn §5, Zustand „Schutz“ |
| Gewitter | Sturm-Arten aktiv; andere suchen Schutz; Wisplets tanzen (SQ_006) | Spawn, Zustand |
| Nebel | Sicht −50 %, Gehör unverändert; Lauerjäger +1 Hinterhaltchance | Wahrnehmung |
| Schnee | Fährten sichtbar (Kodex „Spuren“), Kälteeffekte (K14) | Spuren, Spawn |
| Sandsturm, Ascheregen | Fast alle suchen Schutz; nur angepasste Arten aktiv | Zustand |
| Polarlicht | Licht-/Geist-Arten singen (Hvitfell) | Sozial |
| **Resonanzsturm** | Aggression +1 Stufe (Scheu → neutral, neutral → angriffslustig), Rufe tonal quantisiert (CANON §63) | Wahrnehmung, Audio |
| Mondphase | Nachtaktive 0,8–1,2 × (CANON §66) | Spawn |
| Stillezone | Verstummte Echos; Bestand K × 0,3 bis zur Heilung | Population |
| Nachhall (beide Enden) | Nachhall-Spawns Lv. 72–90 zusätzlich (CANON §40); Sanfte Stille: Silber-Variante, gleiche Tabellen (ADR-174) | Spawn |
| Weltereignis (Wanderung) | Migratory-Arten folgen Route; Spawngewicht entlang der Route ×3 | Zustand, Spawn |

---

## 12. Einfluss des Spielers

| Handlung | Wirkung |
|---|---|
| Binden | Bestand −1 (Zone), Gruppe verliert ggf. Anführer (§7.2) |
| Freilassen | Bestand +1 in der Zone der Freilassung (Floor/K beachten), Wildwacht-Ruf (K47) |
| Lockmittel/Fallen | Lokaler Spawn-/Annäherungsbonus nach Merkmal (K36), nie Bestandsänderung |
| Quests | Folgen ändern Spawn-Tabellen (z. B. Rillo-Familie, Gratkin-Wanderung, Pyroluth-Nest; K49–K51 „Population“) |
| Kampf in der Nähe | Geräusch 60 m: Scheue fliehen, Neugierige kommen später |
| Begleiter-Echo im Freien | Artgenossen reagieren (Neugier ×2), Räuber meiden große Begleiter |

---

## 13. Validierung, Debug, Telemetrie

`python3 tools/ref/aethris_ecology.py validate`:

| Regel | Prüfung |
|---|---|
| EC-01 | Jede Wildart hat ein vollständiges Ökologie-Fragment (CD-09) |
| EC-02 | Jeder Räuber hat ≥ 1 Beute |
| EC-03 | Jede Zone hat Basisverbraucher (in der Zone oder einer Nachbarzone) |
| EC-04 | Jede Region hat Räuber oder Klangsammler |
| EC-05 | Jede Region hat in jeder Tagesphase aktive Arten (Höhlen-Regel R09) |

**Ergebnis:** 187 Wildarten, 0 Verstöße. Erzeugte Daten: `EcologyFragments.csv`, `FoodWeb.csv`.

**Debug** (`Cheat.Ecology.*`): Overlay mit Zustand und Rolle je Echo, Spawnzellen und Gewichte, Bestandsbalken je Zone, Zeitraffer der Tagesrechnung, Erzwingen von Wetter/Mond.

**Telemetrie** (K68): Bindungen je Art und Zone, Bestand < 50 % K über > 3 Spieltage (Hinweis auf Farm-Verhalten), Jagd-Sichtungen, Fluchtereignisse durch den Spieler.

---

## 14. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Creature Design | Prüfen und ggf. überschreiben: 187 Ökologie-Fragmente (Nahrung, Schlafplatz, Fortpflanzung) | K16–K27 |
| Animation | Zustandsanimationen je Archetyp (Ruhen, Nahrung, Sozial, Jagd, Flucht, Schutz, Verstummt/Erwachen, Klangbiss-Blitz) | K57 |
| Level Design | Schlafplätze, Nester, Baue, Unterstände je Zone; Spawnzellen-Dichte nach Biom | K57 |
| Audio | Rufe je Zustand, Fluchtrufe, Jagdlaut, getakteter Stille-Ambient der verstummten Echos | K55 |
| Tech | Mass-Prozessoren, Pool, LOD-Übergänge, Budgets | K65 |
| Save | Fragment `World.Population` (Abweichungen von K) | K64 |
| QA | Determinismus-Test Spawnfolge (gleicher Seed = gleiche Folge, Host vs. Gast) | K66 |

---

## 15. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-196 | Räuber ernähren sich vom Klang (Klangbiss), Beute erschöpft statt stirbt | ADR-007, Lore (Echos = Obertöne), dennoch sichtbare Nahrungsketten | Tötung durch Räuber; keine Räuber |
| ADR-197 | Populationen mit Mindestbestand (Floor) – keine Ausrottung | DR-05, kein Frust durch Leerfang, Bindung bleibt ohne Reue | freie Populationen |
| ADR-198 | Spawnauswahl deterministisch je (Zone, Tag, Stunde, Zelle, Takt) über Fork(2) | Koop-Synchronität, Tests, Replays | zufällige Spawns je Client |
| ADR-199 | Ökologie-Fragmente werden aus Artdaten generiert und dürfen überschrieben werden | 187 Arten konsistent, Designer behalten Hoheit | handgeschriebene Fragmente |
| ADR-200 | Vier Sim-Stufen (Actor, MassNear, MassFar, Statistisch) | DR-12 bei Konsolenbudget | nur Actor + Abschalten |

---

## 16. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §196 | Rollen (Primärverbraucher, Räuber, Klangsammler, Allesverwerter), Ökologie-Fragment (`EcologyFragments.csv`), Nahrungsnetz (`FoodWeb.csv`), Klangbiss | LOCKED |
| §197 | Spawn: Zellen 128 m, Takt 10 Spielmin, Gewicht Seltenheit × Aktivität × Wetter × Mond × Bestand, Fork(2)-Auswahl, Mindestabstand 60 m, Höhlen-Regel R09 | LOCKED |
| §198 | Population: Tagesrechnung (logistisch + Klangbiss), K nach Seltenheit × Größe, Floor, Nachrechnen ≤ 64 Tage | LOCKED |
| §199 | Gruppen (`GroupBehaviors.csv`), Zustände, Wahrnehmung (`PerceptionProfiles.csv`), Spielerlautstärke, Begegnungsregeln | LOCKED |
| §200 | Sim-LOD (Actor < 150 m, MassNear 150–500 m, MassFar, Statistisch), Budgets, Prozessoren | LOCKED |
| §10 | ADR-196 – ADR-200 | LOCKED |

---

## 17. Kapitel-Checkliste

- [x] Leitbild und Rollen; Verteilung über alle Wildarten
- [x] Ökologie-Fragment (CD-09) generiert, mit Ableitungsregeln
- [x] Nahrungsnetz mit Klangbiss, Jagd als sichtbares Ereignis
- [x] Spawn-System: Zellen, Formel, deterministische Auswahl, Tagesverläufe
- [x] Populationsdynamik mit Szenarien (Erholung, Bindungsdruck)
- [x] Gruppen-/Schwarmsteuerung, Anführer, Zustände, Wahrnehmung, Begegnung
- [x] Sim-LOD, Mass-Prozessoren, Budgets
- [x] Reaktionen auf Wetter, Sturm, Stillezonen, Nachhall; Einfluss des Spielers
- [x] Validator EC-01–EC-05 (0 Verstöße), Debug, Telemetrie
- [x] Anforderungen, ADR-196 – ADR-200, CANON §196–§200

➡️ **Nächstes Kapitel: K53 – NPC-KI (Tagesabläufe, Reaktionen, Gruppen).**
