# K09 · Biome I – Verdanthain, Kharsgrat, Morvenmoor, Sahrun-Weite, Ignareth

| Feld | Wert |
|---|---|
| Dokument | Kapitel 09 von 68 · World Bible, Teil III |
| Version | 1.0 |
| Owner | Level Designer (Lead World Designer) |
| Mitwirkende | Technical Artist, Environment Art Lead, Audio Director, Narrative, AI Engineer, Economy Designer |
| Baut auf | K07 (Kosmologie, Kulturen), K08 (Karte, Zonen) – CANON §33–§43 |
| Status | ✅ Freigegeben |
| Im Repository angelegt | `Data/World/RegionTypeDistribution.csv`, `Data/World/RegionWeather.csv`, `Data/Items/Resources.csv` (gelten für K09 **und** K10) |
| Neue Kanon-Einträge | CANON §44 (Biom-Template & Umweltbelastung), §45 (Typverteilung, Wetter, Ressourcen je Region), §46 (Biome R01–R05), §47 (Dörfer & Außenposten-Namen R01–R05) |

---

## Inhalt

1. [Biom-Template](#1-biom-template)
2. [Querschnittssystem: Umweltbelastung](#2-querschnittssystem-umweltbelastung)
3. [Querschnittsdaten: Typverteilung, Wetter, Ressourcen](#3-querschnittsdaten-typverteilung-wetter-ressourcen)
4. [R01 Verdanthain – Wälder](#4-r01-verdanthain--wälder)
5. [R02 Kharsgrat – Gebirge](#5-r02-kharsgrat--gebirge)
6. [R03 Morvenmoor – Sümpfe](#6-r03-morvenmoor--sümpfe)
7. [R04 Sahrun-Weite – Wüste](#7-r04-sahrun-weite--wüste)
8. [R05 Ignareth – Vulkan](#8-r05-ignareth--vulkan)
9. [Technische Kunst: gemeinsame Pipeline](#9-technische-kunst-gemeinsame-pipeline)
10. [Code & Daten](#10-code--daten)
11. [Decision Records](#11-decision-records)
12. [Kanon-Updates](#12-kanon-updates)
13. [Kapitel-Checkliste](#13-kapitel-checkliste)

---

## 1. Biom-Template

Jedes Biom (K09, K10) wird mit demselben Template spezifiziert – so ist garantiert, dass das Briefing-Kriterium („Jedes Gebiet besitzt Wetter, Tageszeit, NPCs, Quests, seltene Kreaturen, Ressourcen“) für alle zehn Regionen vollständig erfüllt ist.

| Block | Inhalt | Liefert an |
|---|---|---|
| **Steckbrief** | Fläche, Akt, Level, Klangfamilie, Stimme, Stadt, Dörfer, Außenposten | K11–K13 |
| **Fantasie & Ton** | Ein Satz Spielergefühl, drei Schlüsselwörter | alle |
| **Visuelle Identität** | Farbpalette (Hex), Geologie, Flora, Licht | K56 Art Bible |
| **Wahrzeichen** | 3–5 Landmarken (Sichtachsen ≥ 2 km) | LD |
| **Wetter & Tageszeit** | Gewichte (CSV), Besonderheiten je Tagesphase | K14/K15 |
| **Umweltbelastung** | Art und Stärke | §2, K40 |
| **Ökologie** | Typverteilung der Erstvorkommen, trophische Struktur, seltene Bedingungen | K16–K27, K52 |
| **Ressourcen** | IDs aus `Resources.csv` | K41/K42 |
| **Bevölkerung & Kultur** | Berufe, Kleidung, Tagesrhythmus | K53 |
| **Quest-Themen** | Nebenquest-Anzahl (CANON §19) und Leitmotive | K49–K51 |
| **Stillezone-Zustand** | Was verstummt, was heilt | K44–K46 |
| **Tech-Art & Audio** | PCG-Graphen, Shader, Ambient-Brief | K55/K57 |

---

## 2. Querschnittssystem: Umweltbelastung

Das Briefing verlangt einen Skillast „Überleben“. Dafür braucht die Welt **Belastungen**, die Ausrüstung, Nahrung und Echo-Begleiter sinnvoll machen – ohne Frust (DR-23) und ohne Tod des Spielercharakters.

### 2.1 Belastungsarten (LOCKED)

| Art | Tag | Vorkommen | Quelle |
|---|---|---|---|
| **Hitze** | `Exposure.Heat` | Sahrun (Tag, Hitzewelle), Ignareth (Lavanähe) | Wetter/Zone |
| **Kälte** | `Exposure.Cold` | Hvitfell, Kharsgrat-Gipfel, Nimbara-Höhen | Zone/Nacht/Schnee |
| **Dunst** | `Exposure.Miasma` | Morvenmoor (Tiefsumpf, Nebelnacht), Prismtiefen (Missklang-Adern) | Zone/Nebel |
| **Asche** | `Exposure.Ash` | Ignareth bei Aschefall | Wetter |
| **Stille** | `Exposure.Silence` | Stillezonen (alle Regionen, storyabhängig) | Story-Data-Layer |

### 2.2 Mechanik

```
 Belastungswert B (0–100) je Art, steigt mit Rate r = Basisrate(Zone, Wetter, Tagesphase) − Schutz
 Schutz = Kleidung (0–60 %) + Nahrung/Trank (0–30 %, zeitlich) + Echo-Aura (0–25 %) + Skilltree (0–20 %)  → max. 100 %

  B  0–49  │ keine Wirkung, HUD-Symbol erscheint ab 25
  B 50–79  │ Ausdauer-Regeneration −40 %, Kodex-Linse verwackelt (Hitze), Atemwolken/Zittern (Kälte)
  B 80–99  │ Sprint deaktiviert, Klettern −30 % Tempo, Echo-Begleiter zeigt Sorge (DR-04)
  B = 100  │ „Rückzug“: Nach 10 s Warnung bringt sich der Wärter automatisch zum nächsten Rastpunkt
           │ (Lagerfeuer, Klangbrunnen, Höhle) – keine Strafe außer Zeit (DR-23)
 Abbau: in Schutzzonen (Siedlung, Lager, Höhle, Oase) −20/s
```

| Basisrate (pro s) | Schwach | Mittel | Stark | Extrem |
|---|---|---|---|---|
| Wert | 0,5 | 1,0 | 2,0 | 4,0 |
| Zeit bis 100 ohne Schutz | 200 s | 100 s | 50 s | 25 s |

**Echo-Auren:** Echos bestimmter Typen im Begleiterslot schützen passiv: Glut → Kälte 25 %, Frost → Hitze 25 %, Blüte/Licht → Dunst 20 %, Stein → Asche 15 %, Klang → Stille 25 % (storyrelevant: Klang-Begleiter erleichtern Stillezonen). *Design-Absicht:* Begleiterwahl wird zur Erkundungsentscheidung (S2 × S1, DR-13).

**Echos selbst** erleiden keine Umweltbelastung außerhalb des Kampfes (Lesbarkeit). Im Kampf wirken Wetter/Terrain über Typ-Resonanz (K32).

---

## 3. Querschnittsdaten: Typverteilung, Wetter, Ressourcen

### 3.1 Primärtyp-Verteilung der Erstvorkommen (bindend für K20–K27)

Datei: `Data/World/RegionTypeDistribution.csv` – Summe pro Region = Erstvorkommen aus CANON §19 (automatisch geprüft).

| Region | Glut | Flut | Stein | Sturm | Blüte | Frost | Leere | Licht | Gift | Metall | Geist | Krist. | Klang | Schwerk. | Arkan | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | 1 | 2 | 4 | 5 | 8 | – | – | 2 | 2 | 1 | 2 | – | 3 | 1 | 1 | 32 |
| R02 | 1 | – | 7 | 3 | – | 2 | – | 1 | – | 3 | 1 | 2 | 1 | 4 | 1 | 26 |
| R03 | – | 5 | 1 | 1 | 4 | – | 2 | – | 7 | – | 4 | – | 1 | – | 1 | 26 |
| R04 | 3 | – | 5 | 2 | – | – | – | 5 | 2 | 1 | 1 | – | – | 3 | 2 | 24 |
| R05 | 8 | – | 3 | 1 | – | – | 2 | – | – | 4 | – | 2 | 1 | 1 | – | 22 |
| R06 | – | 9 | 2 | 5 | 1 | – | – | 2 | 1 | 1 | 1 | 1 | 2 | – | 1 | 26 |
| R07 | – | – | 2 | 1 | – | 9 | 2 | 3 | – | – | 2 | 1 | 2 | – | – | 22 |
| R08 | – | – | 1 | – | – | – | 2 | 1 | – | 3 | 5 | – | 2 | 1 | 5 | 20 |
| R09 | – | – | – | – | – | – | 3 | – | 1 | 2 | – | 8 | 1 | 3 | 2 | 20 |
| R10 | – | – | – | 6 | – | 1 | 1 | 4 | – | – | – | 1 | 4 | 3 | 2 | 22 |
| **Σ** | **13** | **16** | **25** | **24** | **13** | **12** | **12** | **18** | **13** | **15** | **16** | **15** | **17** | **16** | **15** | **240** |

**Befund:** Kein Typ unter 12, keiner über 25 Primärvorkommen – breite Verfügbarkeit für Teambau (DR-05, DR-09). Stein und Sturm sind am häufigsten (Starter-Typen, Allrounder). Leere und Frost sind am seltensten (thematisch: Pause und Stillstand).

### 3.2 Wetter je Region

Datei: `Data/World/RegionWeather.csv` (Summe 100 % je Region, geprüft). Mechanik, Übergänge, Dauer → K14.

| Region | Klar | Regen | Gewitter | Nebel | Schnee | Hitzewelle | Sandsturm | Aurora* | Aschefall |
|---|---|---|---|---|---|---|---|---|---|
| R01 | 50 | 30 | 5 | 15 | – | – | – | – | – |
| R02 | 45 | 10 | 20 | 10 | 15 | – | – | – | – |
| R03 | 25 | 35 | 5 | 35 | – | – | – | – | – |
| R04 | 55 | – | – | – | – | 25 | 20 | – | – |
| R05 | 35 | – | 5 | – | – | 25 | – | – | 35 |
| R06 | 45 | 25 | 15 | 15 | – | – | – | – | – |
| R07 | 30 | – | – | 10 | 45 | – | – | 15 | – |
| R08 | 50 | 15 | 5 | 30 | – | – | – | – | – |
| R09 | 100 (Höhlenklima) | – | – | – | – | – | – | – | – |
| R10 | 45 | 10 | 20 | 10 | – | – | – | 15 | – |

\* Aurora nur nachts; tagsüber gezogen → Klar. Resonanzsturm (W10) nur global/storygesteuert. Prismtiefen-Kraterrand (Oberfläche) nutzt die Tabelle von R08.

### 3.3 Ressourcen

Datei: `Data/Items/Resources.csv` – 48 Ressourcen in 4 Kategorien (Holz 10, Erz 12, Kristall 11, Kraut 15), Stufe I–V gemäß Ausrüstungsstufe. Echo-Materialien (Federn, Schuppen …) folgen in K41.

---

## 4. R01 Verdanthain – Wälder

### 4.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 4,0 km² · Prolog + Akt I · fest 2–14 |
| Klangfamilie | Linnisch |
| Ursprungsstimme | Sylv'anor (Blüte/Klang) – unter der Arena von Eichenhall |
| Stadt | **Eichenhall** |
| Dörfer | **Lindwiesen** (Start), **Moosgrund** |
| Außenposten | **Farnwacht**, **Linnfurt-Posten**, **Uralthain-Lager** |
| Nebenquests | 24 |
| Fantasie | *„Ein Wald, der dich willkommen heißt – und der etwas verloren hat.“* |
| Schlüsselwörter | Geborgenheit · Staunen · erste Schatten |

### 4.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Moosgrün `#4F7A3A`, Lindgold `#D9B44A`, Rindenbraun `#5B4632`, Himmelsdunst `#A9C6D9`, Glockenblütenviolett `#8C6FB8` |
| Geologie | Sanfte Hügel, Kalkfelsen mit Moosmänteln, Flusskiesel an der Linn |
| Flora | Eichen und **Linden** (riesig im Uralthain, bis 60 m), Farnteppiche, **Glockenblüten**, die bei Wind tönen (Klang-Akzent des Bioms), Pilzringe |
| Licht | Warmes, gefiltertes Licht; volumetrische Lichtstrahlen; nachts biolumineszente Pilze |
| Stille-Zustand | Farben entsättigt auf ~20 %, Glockenblüten verstummt und grau, Blätter erstarrt in der Luft |

### 4.3 Wahrzeichen

| Wahrzeichen | Ort | Funktion |
|---|---|---|
| **Wurzelhain von Eichenhall** – eine Linde mit 120 m Kronendurchmesser, Stadt um und in den Wurzeln | 2,6/4,8 | Stadt, Arena, Stimme |
| **Ruinenturm im Lindwald** | ~2,0/5,4 | Onboarding: Gleiter-Fund, Panorama |
| **Farnschlucht** – 40 m tiefe Klamm mit Wasserfall | R01_Z05 | Kletter-/Gleitparcours |
| **Uralthain** – Baumriesen, Lichtungen mit Steinkreisen | R01_Z06 | Spätzone, Seltenheiten |
| **Linnbrücke** (eingestürzt im Prolog) | Prologgrenze | MQ_A0 |

### 4.4 Wetter & Tageszeit

- Wetter: Klar 50 · Regen 30 · Gewitter 5 · Nebel 15.
- **Morgendämmerung:** Nebel in den Senken, Chorgesang der Vögel-Echos (Klang-Typen aktiv), Tau auf Farnen (Sammelbonus Farnfaser).
- **Tag:** Herdenwanderung zu den Linn-Auen.
- **Abenddämmerung:** Glockenblüten tönen im Abendwind; Licht-Echos sammeln sich an Lichtungen.
- **Nacht:** Pilzleuchten, Geist-Echos in Steinkreisen, Räuber auf Jagd.
- **Regen:** Flut- und Gift-Echos tauchen auf (Onboarding-Moment K02 §8.3, 1:45 h).

### 4.5 Umweltbelastung

Keine (Einsteigerregion). Ausnahme: Stillezone im Prolog (`Exposure.Silence`, schwach, storygesteuert).

### 4.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung (Erstvork.) | Blüte 8, Sturm 5, Stein 4, Klang 3, Flut 2, Licht 2, Gift 2, Geist 2, Glut 1, Metall 1, Schwerkraft 1, Arkan 1 (= 32, inkl. 9 Starter-Linien-Arten) |
| Trophische Struktur | 2 Herdenarten (Grasfresser, Auen) · 3 Schwarmarten (Insekten/Vögel) · 2 Räuber (1 Rudel, 1 Einzelgänger-Alpha) · Aasfresser · Baumbewohner · Bodenwühler |
| Seltene Bedingungen (Beispiele) | Nachtgewitter im Uralthain · Nebelmorgen an der Linn · Regen + Abenddämmerung in der Farnschlucht |
| Ursprungsstimme | Sylv'anor erwacht nach Akkord Eichenhall + MQ der Region (K44) |

### 4.7 Ressourcen

Eichenholz (I), Klangharz (II, selten, Uralthain), Farnfaser (I), Lindblüte (I), Kupfererz (I), Moosperle (Kristall I).

### 4.8 Bevölkerung & Kultur

| Aspekt | Beschreibung |
|---|---|
| Berufe | Förster, Harzsammler, Imker (mit Insekten-Echos), Wildwacht-Ranger, Holzschnitzer |
| Kleidung | Leinen und Wolle in Grün/Ocker, Lindenblatt-Stickerei, Wärterumhänge |
| Architektur | Fachwerk, Rundbögen aus Holz, Moosdächer; in Eichenhall Wurzelbrücken |
| Tagesrhythmus | Früh auf, Mittagsruhe, Abendmusik am Dorfplatz (Lindwiesen-Fest, wöchentlich in Spielzeit) |

### 4.9 Quest-Themen (24 Nebenquests)

Nachbarschaftshilfe (verlorene Echos, Diebische Echos), Einführung in Kodex und Fotografie, Wildwacht-Patrouillen, das Geheimnis der Steinkreise, Rivalität mit Kael (optionale Trainingskämpfe), Glockenblüten-Rätsel.

### 4.10 Stillezone-Zustand

Prolog: Lindwald-Lichtung. Akt I: zwei weitere Zonen (Farnschlucht, Uralthain-Rand). Heilung → `DL_Story_R01_Healed` (blühende Glockenblüten-Wiesen, neue Echo-Nester).

### 4.11 Tech-Art & Audio

| Tech-Art | Audio-Brief |
|---|---|
| PCG: `PCG_R01_Forest_Canopy`, `PCG_R01_Understory`, `PCG_R01_Riverbank`; Nanite-Foliage für Bäume; Wind über **Wind-Volumes** mit Glockenblüten-Klangtrigger | Grundbett: Laub, Vögel-Echos, Linn-Rauschen; Glockenblüten als zufällige, auf Musiktonart quantisierte Klänge; Stadtthema Eichenhall: Holzbläser + Harfe |

---

## 5. R02 Kharsgrat – Gebirge

### 5.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 4,0 km² · Akt I (frei wählbar) · Stufen T1–T3 (10–28) |
| Klangfamilie | Kharsk |
| Ursprungsstimme | Orh'gruun (Stein/Schwerkraft) – unter Kharsholm |
| Stadt | **Kharsholm** |
| Dörfer | **Brakkfels**, **Hrallsted** |
| Außenposten | **Passwacht Nord**, **Erzgrat-Hütte**, **Grollhorn-Biwak** |
| Nebenquests | 22 |
| Fantasie | *„Jeder Grat ist ein Versprechen, jeder Gipfel eine Prüfung.“* |
| Schlüsselwörter | Vertikalität · Beständigkeit · Ahnen |

### 5.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Granitgrau `#6E6E73`, Flechtengelb `#C8B560`, Eisenrot `#8A3B2A`, Gipfelweiß `#E8EEF2`, Kiefernblaugrün `#2F5A55` |
| Geologie | Granit, Basaltsäulen (Grollbasalt), Erzadern sichtbar als rostrote Bänder, Schwebefelsen in Orh'gruuns Nähe (Schwerkraft-Anomalien) |
| Flora | Bergkiefern, Krüppelbirken, Enzianmatten, Flechten |
| Licht | Klar, hart, lange Schatten; Wolken unterhalb der Gipfel |
| Stille-Zustand | Schwebefelsen sinken herab, Wasserfälle gefrieren lautlos in der Bewegung |

### 5.3 Wahrzeichen

**Grollhorn** (1.650 m, Gipfel-Biwak) · **Kharsholm** (in die Felswand gehauene Stadt mit Kettenbrücken über dem Grollschlund) · **Schwebende Ahnenfelsen** (Gravitationsanomalie, Rätsel-POI) · **Erzgrat-Minen** (verlassen, Dungeon) · **Linn-Quelle** (Wasserfall).

### 5.4 Wetter & Tageszeit

- Klar 45 · Regen 10 · Gewitter 20 · Nebel 10 · Schnee 15 (Schnee nur in Z04/Z05; in tieferen Zonen → Regen).
- **Gewitter:** Sturm-Echos fliegen, Blitzeinschläge auf Erzgraten (Metall-Echos werden geladen – Evolutionsbedingung, K19).
- **Morgen:** Wolkenmeer unter den Terrassen (Aussichtspunkte).
- **Nacht:** Schwebefelsen leuchten schwach; Stein-Echos „wandern“ (bewegen sich nachts).

### 5.5 Umweltbelastung

Kälte (mittel) in Z04/Z05; bei Schnee (stark) auf dem Grollhorn.

### 5.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Stein 7, Schwerkraft 4, Sturm 3, Metall 3, Frost 2, Kristall 2, Glut 1, Licht 1, Geist 1, Klang 1, Arkan 1 (= 26) |
| Trophische Struktur | Bergziegen-Herden (Klettern), Greifvogel-Räuber (Horste = Flugreiten-POIs), Höhlenschwärme, Gesteinsfresser (Erzadern) |
| Seltene Bedingungen | Gewitter + Nacht auf dem Erzgrat · Schnee + Morgendämmerung am Grollhorn · Nähe zu Schwebefelsen |

### 5.7 Ressourcen

Bergkiefer (II), Kharseisen (II), Grollbasalt (II), Quarzsplitter (Kristall I), Gipfelenzian (II).

### 5.8 Bevölkerung & Kultur

Klans (Brakk, Hrall, Torv), Bergbau, Schmiedekunst, Säumer mit Last-Echos. Kleidung: Filz, Leder, Pelzkragen, Metallspangen mit Klanzeichen. Architektur: Fels, Basaltsäulen, Gemeinschaftshallen mit Feuerstellen. Rhythmus: Schichtbetrieb der Minen (drei Schichten → NPC-Tagesabläufe auch nachts aktiv).

### 5.9 Quest-Themen (22)

Verschüttete Bergleute, Klanfehden (Ehrenkämpfe), Ahnenfelsen-Rätsel, Schwerkraft-Anomalien erforschen (Akademie), Greifenhorst-Kletterei, die verlassenen Erzgrat-Minen.

### 5.10 Stillezone-Zustand & Story

Zonen im Grollschlund. Erster Fund von **Stillsteinen** des Ordens (W2 – sofern Kharsgrat als erste freie Region gewählt; die Quest-Logik platziert W2 in der *ersten* betretenen Akt-I-Region, K44).

### 5.11 Tech-Art & Audio

PCG: `PCG_R02_Scree`, `PCG_R02_Alpine`; Basaltsäulen als Nanite-Kit; Schwebefelsen mit Niagara-Partikeln + leichter Bob-Animation (World Position Offset). Audio: Wind in Graten (Pfeifen), Kettenbrücken-Knarren, ferne Hämmer; Stadtthema Kharsholm: tiefe Männer-/Frauenchöre, Ambosse auf Taktschlag.

---

## 6. R03 Morvenmoor – Sümpfe

### 6.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 3,2 km² · Akt I (frei wählbar) · T1–T3 |
| Klangfamilie | Morvisch |
| Ursprungsstimme | Nhael'vesh (Gift/Geist) – versunkener Turm unter Morvenfurt |
| Stadt | **Morvenfurt** (Pfahl- und Kanalstadt; Unterstadt = Freie Stimmen) |
| Dörfer | **Fennhaven**, **Duvreth** |
| Außenposten | **Corrach-Stelzenposten**, **Riedwacht**, **Senkenlager** |
| Nebenquests | 21 |
| Fantasie | *„Im Nebel flüstert alles, was einmal war.“* |
| Schlüsselwörter | Geheimnis · Kreislauf · Gemeinschaft im Verborgenen |

### 6.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Moorgrün `#3E4F2C`, Torfbraun `#4A3424`, Nebelgrau `#9BA59A`, Irrlichtcyan `#6FD3C2`, Sumpfblüten-Magenta `#B0457D` |
| Geologie | Torf, Schlick, versunkene Steinmauern, Pfahlwälder |
| Flora | Moorweiden, Mangroven-artige Stelzwurzeln, Riesen-Seerosen (begehbar), Sumpfmyrte, Irrlichtmoos (leuchtet nachts) |
| Licht | Diffus, tiefliegender Nebel, Lichtinseln; nachts Irrlichter |
| Stille-Zustand | Wasser wird spiegelglatt und still, Nebel erstarrt zu Schichten, Irrlichter erlöschen |

### 6.3 Wahrzeichen

**Morvenfurt** (Kanäle, Brückendächer, Laternen) · **Versunkener Turm** (Turmspitze ragt aus dem Wasser – Schlafort der Stimme) · **Nebelwald Corrach** (Mangrovenlabyrinth) · **Riesen-Seerosenfelder** · **Morve-Delta**.

### 6.4 Wetter & Tageszeit

- Klar 25 · Regen 35 · Gewitter 5 · Nebel 35.
- **Nebel + Nacht:** Geist-Echos häufen sich; höchste Dichte seltener Arten der Region.
- **Regen:** Wasserstand +0,4 m (Data-Layer-Variante der Wasseroberfläche → andere Wege, Schwimmreiten-Bedarf).
- **Morgen:** Krötenchor (Klang).

### 6.5 Umweltbelastung

Dunst (mittel) in Z03/Z05, stark bei Nebel + Nacht. Gegenmittel: Sumpfmyrten-Tee (Crafting), Blüte/Licht-Begleiter.

### 6.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Gift 7, Flut 5, Geist 4, Blüte 4, Leere 2, Sturm 1, Klang 1, Arkan 1, Stein 1 (= 26) |
| Struktur | Amphibienkolonien, Schwärme (Mücken-/Leuchtkäfer-Echos), Lauerjäger im Wasser, Aasfresser, Fäulnis-Zersetzer (Gift) als Schlüsselart des Kreislaufs |
| Seltene Bedingungen | Nebel + Nacht in der Versunkenen Senke · Gewitter über dem Delta · Regen + Morgendämmerung bei den Seerosen |

### 6.7 Ressourcen

Moorweide (I), Torfkohle (Erz I – Brennstoff), Nebelperle (Kristall II), Sumpfmyrte (II), Irrlichtmoos (III, selten).

### 6.8 Bevölkerung & Kultur

Moorleute: Fischer, Kräuterkundige („Moorweise“), Torfstecher, Bootsbauer. Kleidung: Wachstuch, Kapuzen, Muschel- und Knochenschmuck. Architektur: Pfahlbauten, Schilfdächer, Laternenstege. Rhythmus: Nachtmärkte (Haupthandelszeit ist nachts!), tagsüber Ruhe.

### 6.9 Quest-Themen (21)

Freie Stimmen (erste Kontakte, Fraktions-Einstieg), Moorweisheit (Gift als Medizin), verlorene Boote im Nebel, Irrlicht-Jagd (Jagd-Quest), Schmuggel in der Unterstadt (Entscheidung Kontor vs. Freie Stimmen).

### 6.10 Stillezone-Zustand & Story

Stillezone im Duvreth-Sumpf; der Spieler trifft hier (oder in der ersten Akt-I-Region) erstmals **Tavesh Amaru**. Heilung bringt Irrlichter zurück, eröffnet Nachtmarkt-Sonderwaren.

### 6.11 Tech-Art & Audio

Wasser: Single-Layer-Water mit Data-Layer-Pegeln; Nebel: Heterogeneous Volumes (PC/PS5), Fallback Exponential Height Fog + Partikel-Karten (Switch 2). Audio: Tropfen, Kröten, Schilfrascheln, dumpfe Unterwasserklänge beim Schwimmen; Stadtthema Morvenfurt: Bodhrán-artige Trommel, Flöte, gezupfte Saiten, Nachtmarkt-Variante.

---

## 7. R04 Sahrun-Weite – Wüste

### 7.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 4,4 km² · Akt II (frei) · T4–T7 (25–55) |
| Story-Gate | **Sandsturmwand** am Nordrand – lichtet sich nach MQ Akt-II-Auftakt |
| Klangfamilie | Sahrunisch |
| Ursprungsstimme | Ash'kareth (Licht/Arkan) – unter dem Sonnenhof von Qasr Sahrun |
| Stadt | **Qasr Sahrun** |
| Dörfer | **Harrâd** (Oase), **Mirsaan**, **Wanderdorf Ashurim** (mobil, Sonderdorf) |
| Außenposten | **Glasebene-Turm**, **Dünenwacht**, **Plateau-Lager** |
| Nebenquests | 22 |
| Fantasie | *„Unter der Sonne gibt es keine Geheimnisse – nur die, die der Sand verbirgt.“* |
| Schlüsselwörter | Weite · Wahrheit · Gastfreundschaft |

### 7.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Dünengold `#E0B46A`, Terrakotta `#B5653B`, Himmelstürkis `#3FA7B5`, Glasweiß `#F3EBDD`, Abendviolett `#5E3B6E` |
| Geologie | Wanderdünen, Salzpfannen, **Glasebene** (durch uralte Lichtblitze verglaster Sand), Tafelberge, Sonnenhof-Plateau |
| Flora | Wüstendorn, Kakteen-artige Sukkulenten, Dattelpalmen-Oasen, Oasenminze |
| Licht | Grell, Hitzeflimmern (Post-Process), extreme Abendfarben, kristallklarer Sternenhimmel |
| Stille-Zustand | Dünen hören auf zu „singen“ (Singende Dünen sind ein Klang-Feature), Sand fällt lautlos wie Schnee |

### 7.3 Wahrzeichen

**Sonnenhof-Plateau** mit Qasr Sahrun · **Glasebene** (spiegelnd, Lichträtsel) · **Singende Dünen** (Mirsaan) · **Harrâd-Oase** · **Wanderdorf Ashurim** (zieht in 3 Spieltagen eine Route über 4 Lagerplätze).

### 7.4 Wetter & Tageszeit

- Klar 55 · Hitzewelle 25 · Sandsturm 20.
- **Tag:** Hitze (mittel, Hitzewelle: stark). Viele Echos ruhen im Schatten – Wüste wirkt tagsüber leer (bewusst).
- **Abenddämmerung/Nacht:** Wüste erwacht; die meisten Arten sind nachtaktiv; Temperatur kippt → Kälte (schwach) nachts.
- **Sandsturm:** Sicht 40 m, Grab-Echos tauchen auf, Navigation per Resonanzsinn (Design-Moment: Hören statt Sehen).

### 7.5 Umweltbelastung

Hitze tagsüber (mittel/stark), Kälte nachts (schwach). Oasen und Schattenzelte = Schutzzonen.

### 7.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Stein 5, Licht 5, Glut 3, Schwerkraft 3, Gift 2, Sturm 2, Arkan 2, Metall 1, Geist 1 (= 24) |
| Struktur | Karawanen-Herden (Lasttiere – reitbar), Sandschwimmer (Grabreiten), Skorpion-artige Gift-Räuber, Lichtfalter-Schwärme (nachts) |
| Seltene Bedingungen | Sandsturm + Nacht auf der Glasebene · Hitzewelle + Mittag am Plateau (Licht) · Neumondnacht (Mondphase → K15) |

### 7.7 Ressourcen

Wüstendornholz (III), Salzkupfer (III), Glutsand (II), Sonnenglas (III), Oasenminze (II).

### 7.8 Bevölkerung & Kultur

Karawanenhändler, Glasbläser, Sterndeuter, Brunnenwächter; Gastrecht ist heilig (Questmechanik: Gastgeschenke). Kleidung: weite Leinengewänder, Schleier gegen Sand, Indigo und Safran, Spiegelschmuck. Architektur: Lehm, Kuppeln, Windtürme, Innenhöfe mit Klangbrunnen. Rhythmus: **umgekehrt** – Mittagsruhe sehr lang, Leben nachts. **Sensitivity-Review Pflicht** (K04 §3).

### 7.9 Quest-Themen (22)

Gastrecht-Ketten, Wahrheitsrätsel (Licht-Rätsel, Sonnenhöfe), verlorene Karawane im Sandsturm, Glasbläserwettbewerb, das wandernde Dorf (zeitabhängige Quests), Akademie-Ausgrabungen unter der Glasebene (Lore W4).

### 7.10 Stillezone-Zustand & Story

Akt II: Venn-Expedition gräbt am Sonnenhof (Kronensplitter #1 der Akt-II-Spur). Heilung: Singende Dünen kehren zurück.

### 7.11 Tech-Art & Audio

Dünen: Landscape + Displacement-Layer, Sandverwehungen per PCG `PCG_R04_DuneRipples`; Hitzeflimmern als Post-Process-Material mit Distanzmaske; Glasebene mit Lumen-Reflexionen (Switch 2: SSR + Reflection Captures). Audio: Wind, singende Dünen (tonal, Grundton der Region), Glöckchen der Karawanen; Stadtthema Qasr Sahrun: Oud-artige Laute, Rahmentrommel, Frauenchor – mit Musikberatung zur Vermeidung von Klischees.

---

## 8. R05 Ignareth – Vulkan

### 8.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 3,0 km² · Akt II (frei) · T4–T7 |
| Story-Gate | **Ascheschleier** an der Westgrenze – lichtet sich nach MQ |
| Klangfamilie | Ignar |
| Ursprungsstimme | Pyr'thagon (Glut/Metall) – Kraterherz unter Schlackenwehr |
| Stadt | **Schlackenwehr** |
| Dörfer | **Vorthax**, **Kaldra** |
| Außenposten | **Aschehütte**, **Obsidianwacht**, **Kraterrand-Posten** |
| Nebenquests | 19 |
| Fantasie | *„Hier wird die Welt neu geschmiedet – jeden Tag.“* |
| Schlüsselwörter | Schöpfung · Gefahr · Handwerk |

### 8.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Basaltschwarz `#1E1C1F`, Lavaorange `#F05A1A`, Glutrot `#A3201B`, Schwefelgelb `#D8C23A`, Aschegrau `#7A7470` |
| Geologie | Lavaströme (aktiv, mit Krustenbrücken), Obsidianklamm, Schwefelfelder, Fumarolen, Basaltorgeln |
| Flora | Ascheholz-Bäume (feuerresistent, schwarz), Feuerlilien an Lavarändern, Flechten |
| Licht | Emissive Lava als Hauptlicht nachts; tagsüber gedämpft durch Rauch; Aschefall wie grauer Schnee |
| Stille-Zustand | Lava erstarrt mitten im Fluss zu schwarzem Glas, Glutfunken hängen still in der Luft |

### 8.3 Wahrzeichen

**Ignar-Krater** (1.150 m, glühender Krater) · **Schlackenwehr** (Festungsstadt hinter einer Lava-Umlenkmauer) · **Obsidianklamm** (spiegelnde Schlucht) · **Vorthax-Schlackenstrom** (Kruste begehbar, zeitweise) · **Schmiedeterrassen**.

### 8.4 Wetter & Tageszeit

- Klar 35 · Gewitter 5 (vulkanische Blitze) · Hitzewelle 25 · Aschefall 35.
- **Aschefall:** Sicht 80 m, Leere- und Glut-Echos aktiv, Spuren im Aschebelag sichtbar (Tracking-Gameplay).
- **Nacht:** Lavaleuchten, Glut-Echos am aktivsten.
- **Ausbrüche** (scriptbar, kein Zufallstod): alle 3 Spieltage ein kleiner Ausbruch → Lavastrom-Änderung (Data-Layer-Zustand A/B), neue Wege.

### 8.5 Umweltbelastung

Hitze (mittel bis extrem an Lavarändern), Asche (mittel bei Aschefall). Lava selbst: Betreten unmöglich (Charakter weicht automatisch aus; Echos können mit Feldfähigkeiten Krusten kühlen).

### 8.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Glut 8, Metall 4, Stein 3, Kristall 2, Leere 2, Sturm 1, Schwerkraft 1, Klang 1 (= 22) |
| Struktur | Mineralfresser (fressen Erz/Schlacke), Glutsalamander-Kolonien, Aschefalter-Schwärme, ein Spitzenräuber in der Obsidianklamm |
| Seltene Bedingungen | Ausbruchstag + Nacht · Aschefall + Kraterrand · Gewitter (vulkanisch) über Schmiedeterrassen |

### 8.7 Ressourcen

Ascheholz (III), Schlackenstahl (IV), Obsidian (III), Schwefelkristall (II), Feuerlilie (III).

### 8.8 Bevölkerung & Kultur

Schmiedezünfte (höchstes Ansehen), Lavawächter, Glasmacher, Thermalbader. Kleidung: Leder, Asbest-freie „Glutwolle“ (fiktiv aus Echo-Fasern), Schutzmasken mit Klangfiltern. Architektur: Basalt, Bronze, Kühlkanäle mit Dampf. Rhythmus: Schmiedeglocken strukturieren den Tag (6 Glocken pro Spieltag).

### 8.9 Quest-Themen (19)

Schmiedeprüfungen (Crafting-Questlinie, Ausrüstung IV), Lavawächter-Rettung, Echo-Ausbeutung in Erzminen (Freie Stimmen vs. Kontor – Entscheidung), Kraterbesteigung, Vorhersage des nächsten Ausbruchs (Akademie).

### 8.10 Stillezone-Zustand & Story

Stillezone um das Kraterherz – Pyr'thagon „erkaltet“. Sereth Vaun tritt hier erstmals persönlich auf (sofern R05 erste Akt-II-Region; Quest-Logik wie §5.10).

### 8.11 Tech-Art & Audio

Lava: Flowmap-Material + Emissive + Light Functions; zwei Data-Layer-Zustände für Lavaströme; Fumarolen per Niagara (GPU-Sim, Budget 0,3 ms). Audio: tiefes Grollen (Subbass, LFE), Zischen, Schmiedehämmer im Musiktakt; Stadtthema Schlackenwehr: Blechbläser, Ambosse, Kesselpauken.

---

## 9. Technische Kunst: gemeinsame Pipeline

| Thema | Festlegung für alle Biome |
|---|---|
| PCG-Graph-Namensschema | `PCG_R##_<Layer>` – Layer: Canopy, Understory, Ground, Rocks, Water, Props, Hazards |
| Generierungszeitpunkt | Editorzeit (gebacken), Shipping ohne Runtime-PCG außer Hain-Deko (K05 §2) |
| Foliage-Budget (PS5, pro sichtbarem Frame) | ≤ 1,6 Mio. Nanite-Instanzen, ≤ 250 k Grass-Instanzen; Switch 2: ≤ 400 k / 60 k (K65) |
| Material-Master | `M_Landscape_Master` (Runtime Virtual Texturing), `M_Foliage_Master`, `M_Water_Master`, `M_Lava_Master`, `M_Snow_Master` (K10) |
| Stille-Zustand | Globaler Material-Parameter `MPC_Silence` (Entsättigung, Bewegungsstopp in WPO, Partikel-Freeze) pro Region über Data Layer + Volumen |
| Wetter-Masken | Nässe, Schnee, Asche, Sand als RVT-Layer, gesteuert durch Wetter-System (K14) |

---

## 10. Code & Daten

### 10.1 Belastungssystem (GF_World, Domain-Logik + Player-Komponente in AethrisGame)

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Public/Exposure/ExposureTypes.h
/** Basisraten je Belastungsart (K09 §2.2). Werte in Promille pro Sekunde (DD-04): 500 = 0,5/s. */
UENUM(BlueprintType)
enum class EExposureSeverity : uint8 { None, Weak, Medium, Strong, Extreme };

USTRUCT(BlueprintType)
struct GF_WORLD_API FExposureSource
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere, meta=(Categories="Exposure")) FGameplayTag Type;  // Exposure.Heat …
	UPROPERTY(EditAnywhere) EExposureSeverity Severity = EExposureSeverity::None;
	/** Optional: nur bei diesem Wetter / dieser Tagesphase aktiv. */
	UPROPERTY(EditAnywhere, meta=(Categories="Weather")) FGameplayTagContainer RequiredWeather;
	UPROPERTY(EditAnywhere, meta=(Categories="TimeOfDay")) FGameplayTagContainer RequiredTimeOfDay;
};

namespace Aethris::Exposure
{
	/** Basisrate in Promille/s. */
	constexpr int32 RatePermille(EExposureSeverity S)
	{
		switch (S)
		{
		case EExposureSeverity::Weak:    return 500;
		case EExposureSeverity::Medium:  return 1000;
		case EExposureSeverity::Strong:  return 2000;
		case EExposureSeverity::Extreme: return 4000;
		default:                         return 0;
		}
	}

	/** Effektive Rate nach Schutz (Schutz in Prozent 0..100, gedeckelt). */
	constexpr int32 EffectiveRatePermille(EExposureSeverity S, int32 ProtectionPercent)
	{
		const int32 P = ProtectionPercent < 0 ? 0 : (ProtectionPercent > 100 ? 100 : ProtectionPercent);
		return RatePermille(S) * (100 - P) / 100;
	}
}
```

```cpp
// AethrisGame/Private/Player/WardenExposureComponent.cpp (Auszug)
// Aktualisiert 4× pro Sekunde (Timer, kein Tick – CS-13).
void UWardenExposureComponent::UpdateExposure()
{
	const float Dt = 0.25f;
	for (FExposureState& State : States)                       // je Belastungsart
	{
		const EExposureSeverity Sev = CurrentSeverity(State.Type); // aus Zone + Wetter + Tagesphase
		const int32 Protection = ComputeProtection(State.Type);  // Kleidung + Nahrung + Echo-Aura + Skilltree
		const bool bSafeZone = IsInSafeZone();

		State.Value += bSafeZone ? -20.f * Dt
		                         : Aethris::Exposure::EffectiveRatePermille(Sev, Protection) / 1000.f * Dt;
		State.Value = FMath::Clamp(State.Value, 0.f, 100.f);
	}
	ApplyThresholdEffects();   // 50/80/100-Stufen (K09 §2.2)
}
```

*Hinweis:* Umweltbelastung liegt außerhalb der Determinismus-Zone (reine Oberwelt, nicht replay-relevant) – `float` ist hier zulässig (CS-14 betrifft nur Kampf/Genetik/Replays).

### 10.2 Daten-Validierung (data_lint, Auszug)

```python
# tools/data_lint.py – Prüfregel für K09/K10-Daten (wird mit K10 vervollständigt)
def check_region_type_distribution(budget, dist):
    for region, row in dist.items():
        total = sum(int(v) for k, v in row.items() if k != "Name")
        assert total == budget[region], f"{region}: Typverteilung {total} ≠ Budget {budget[region]}"

def check_weather(weather):
    for region, row in weather.items():
        assert sum(int(v) for k, v in row.items() if k != "Name") == 100, f"{region}: Wetter ≠ 100 %"
```

---

## 11. Decision Records

### ADR-046 – Umweltbelastung ohne Tod, mit automatischem Rückzug
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Keine Belastung | Einfach | Überleben-Skillast ohne Funktion; Biome austauschbar |
| (b) Survival mit Schaden/Tod | Spannung | Frust, Widerspruch zu Ton und Zielgruppe |
| (c) Belastung mit Stufen und automatischem Rückzug | Biome fühlen sich unterschiedlich an, Ausrüstung/Begleiter zählen, kein Frust | Weniger „Gefahr“ für Hardcore-Spieler → **Meister**: Rückzug kostet zusätzlich 5 % Sol (gedeckelt 2.000 ◎) |
- **Entscheidung:** (c).

### ADR-047 – Typverteilung pro Region als bindende Datenvorgabe
- **Entscheidung:** Die Kataloge K20–K27 müssen die Primärtyp-Verteilung je Region exakt erfüllen (Validator). Vorteil: Regionen haben erkennbare Typ-Identität, Teambau bleibt breit möglich. Nachteil: Kreaturendesign weniger frei → Sekundärtypen sind frei wählbar.

### ADR-048 – Umgekehrte Tagesrhythmen als Biom-Identität
- **Entscheidung:** Sahrun (nachtaktiv) und Morvenmoor (Nachtmärkte) kehren den Tagesrhythmus um. Vorteil: Tageszeit wird zur Erkundungsentscheidung (DR-13, DR-15). Nachteil: Spieler könnten Regionen tagsüber als „leer“ erleben → Mitigation: Gasthäuser mit „Zeit vorspulen“ in jeder Siedlung (K03 §3) und NPC-Hinweise.

### ADR-049 – Ressourcen-Stufen spiegeln Akt-Progression
- **Entscheidung:** Stufe I–II in Akt-I-Regionen, III–IV in Akt-II-Regionen, V in Akt III. Ausnahme: Seltene Ressourcen höherer Stufe in frühen Regionen (Klangharz II in R01) als Erkundungsbelohnung.

---

## 12. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §44 | Biom-Template (§1) – Pflicht für alle 10 Regionen | LOCKED |
| §44 | Umweltbelastung: Hitze, Kälte, Dunst, Asche, Stille (`Exposure.*`); Stufen 50/80/100; Raten 0,5/1/2/4 pro s; Schutzquellen Kleidung ≤ 60 %, Nahrung ≤ 30 %, Echo-Aura ≤ 25 %, Skilltree ≤ 20 %; Rückzug statt Tod; Meister +5 % Sol (max. 2.000 ◎) | LOCKED |
| §44 | Echo-Auren: Glut→Kälte 25 %, Frost→Hitze 25 %, Blüte/Licht→Dunst 20 %, Stein→Asche 15 %, Klang→Stille 25 % | LOCKED |
| §45 | `RegionTypeDistribution.csv` (bindend für K20–K27), `RegionWeather.csv`, `Resources.csv` (48 Ressourcen) | LOCKED |
| §46 | Biome R01–R05: Wahrzeichen, Paletten, Tagesrhythmen, Quest-Themen, Stillezone-Zustände, Tech-Art/Audio-Briefs | LOCKED |
| §46 | Story-Platzierung: W2 (Stillsteine) in der **ersten** betretenen freien Akt-I-Region; Tavesh-Erstkontakt in Morvenmoor oder erster Akt-I-Region; Sereth-Erstauftritt in erster Akt-II-Region | LOCKED |
| §46 | Ignareth: kleiner Ausbruch alle 3 Spieltage (Data-Layer-Zustände A/B); Sahrun: Wanderdorf-Route 4 Lager / 3 Spieltage | LOCKED |
| §47 | Dörfer/Außenposten R01–R05 (Namen, §4–§8) | LOCKED |
| §10 | ADR-046 – ADR-049 | LOCKED |

---

## 13. Kapitel-Checkliste

- [x] Biom-Template (deckt alle Briefing-Kriterien je Gebiet ab)
- [x] Umweltbelastung als Querschnittssystem inkl. Code
- [x] Typverteilung aller 10 Regionen (Summen validiert: 240; je Typ 12–25)
- [x] Wettergewichte aller 10 Regionen (je 100 %)
- [x] 48 Ressourcen aller Regionen (Stufen I–V)
- [x] Verdanthain, Kharsgrat, Morvenmoor, Sahrun-Weite, Ignareth vollständig nach Template
- [x] Namen von 11 Dörfern (inkl. Wanderdorf) und 15 Außenposten
- [x] Gemeinsame Tech-Art-Pipeline (PCG, Foliage-Budget, Master-Materialien, Stille-Parameter)
- [x] ADR-046 – ADR-049, CANON aktualisiert

➡️ **Nächstes Kapitel: K10 – Biome II: Saltrand, Hvitfell, Ael'Dorun, Prismtiefen, Nimbara.**
