# K10 · Biome II – Saltrand, Hvitfell, Ael'Dorun, Prismtiefen, Nimbara

| Feld | Wert |
|---|---|
| Dokument | Kapitel 10 von 68 · World Bible, Teil IV |
| Version | 1.0 |
| Owner | Level Designer (Lead World Designer) |
| Mitwirkende | Technical Artist, Environment Art Lead, Audio Director, Narrative, Unreal Senior Dev (Unterwasser, Höhlen, Himmel) |
| Baut auf | K07, K08, K09 (Template, Umweltbelastung, Regionsdaten) – CANON §33–§47 |
| Status | ✅ Freigegeben |
| Neue Kanon-Einträge | CANON §48 (Biome R06–R10), §49 (Siedlungsnamen R06–R10), §50 (Sondermechaniken: Unterwasser, Dunkelheit, Fallrettung, Aufwinde) |

---

## Inhalt

1. [Sondermechaniken dieser Biome](#1-sondermechaniken-dieser-biome)
2. [R06 Saltrand – Küste](#2-r06-saltrand--küste)
3. [R07 Hvitfell – Schnee](#3-r07-hvitfell--schnee)
4. [R08 Ael'Dorun – Ruinen](#4-r08-aeldorun--ruinen)
5. [R09 Prismtiefen – Kristallhöhlen](#5-r09-prismtiefen--kristallhöhlen)
6. [R10 Nimbara – Himmelinseln](#6-r10-nimbara--himmelinseln)
7. [Biom-Vergleich (alle 10)](#7-biom-vergleich-alle-10)
8. [Code](#8-code)
9. [Decision Records](#9-decision-records)
10. [Kanon-Updates](#10-kanon-updates)
11. [Kapitel-Checkliste](#11-kapitel-checkliste)

---

## 1. Sondermechaniken dieser Biome

Die fünf Regionen dieses Kapitels führen vier Mechaniken ein, die in K09 nicht vorkamen. Alle folgen dem Grundsatz „kein Tod des Spielercharakters, kein Frust durch Umwelt“ (ADR-046).

| Mechanik | Region | Regel (LOCKED) |
|---|---|---|
| **Unterwasser** | R06 (Riffgrund), R03 (Tiefsumpf, optional), R09 (Kristallsee) | Tauchen nur mit **Schwimmreiten** (Echo erzeugt eine Luftblase – *Atemkugel*). Ohne Reittier: Oberflächenschwimmen (Ausdauer −6/s; bei 0 treibt der Wärter zum nächsten Ufer). Kein Ertrinken. Unterwasser: eigene Spawns, Ressourcen (Perlmutt), Rätsel. |
| **Dunkelheit** | R09 (Höhlen), R08 (Gewölbe), Nachtszenen überall | Lichtwert 0–100 aus Lumen-Luminanz-Probe + Lichtquellen. Unter 15: eingeschränkte Sicht, **Resonanzsinn** zeigt Umrisse; Lichtquellen: Laterne (Ausrüstung), **Kristall-Leuchten** (aktivierbar), Licht-/Glut-Begleiter (Radius 8 m). Seltene Höhlen-Echos reagieren auf Licht (scheu → Bindungs-Taktik DR-03). |
| **Fallrettung** | R10 (Himmelinseln), R02-Gipfel, Klippen | Fall > 30 m ohne geöffneten Gleiter: Gleiter öffnet automatisch, falls vorhanden (Option, Standard an). Fall über Inselrand ohne Boden darunter: **Resonanzsprung** – Wärter wird nach 2 s Fall zum letzten sicheren Bodenpunkt zurückgesetzt (Klangeffekt, kurze Abblende), keine Strafe. |
| **Aufwinde & Windströme** | R10, R06-Klippen, R02-Grate | Aufwinde (sichtbar als Partikelsäulen) heben den Gleiter 6 m/s; **Windströme** (Röhren aus Wind zwischen Inseln) tragen mit 18 m/s in fester Richtung. Gewitter verstärkt Aufwinde (+50 %), Flugreiten in Gewitter −20 % Steuerbarkeit (Lesbarkeit: Blitzwarnung 1,5 s vorher). |

---

## 2. R06 Saltrand – Küste

### 2.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 3,4 km² · Akt I (frei wählbar) · T1–T3 (10–28) |
| Klangfamilie | Saltisch |
| Ursprungsstimme | Thal'assyr (Flut/Sturm) – Tiefseegrotte vor Saltrand-Hafen |
| Stadt | **Saltrand-Hafen** (Goldklang-Kontor-Hauptsitz) |
| Dörfer | **Tangwerft**, **Möwenhuk**, **Treibdorf Flottholm** (schwimmend, Sonderdorf) |
| Außenposten | **Leuchtfelsen-Wacht**, **Dünenkate**, **Riffposten** |
| Nebenquests | 23 |
| Fantasie | *„Das Meer nimmt und gibt – und erzählt dabei Geschichten.“* |
| Schlüsselwörter | Handel · Fernweh · Gezeiten |

### 2.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Meerblau `#1F5F8B`, Gischtweiß `#EEF4F6`, Sandbeige `#D9C7A3`, Rostrot (Schiffe) `#9B3D2E`, Algengrün `#4E7D5B` |
| Geologie | Steilküste (bis 180 m), Kiesstrände, Gezeitenbecken, Riffe, Felsbögen |
| Flora | Strandhafer, Salzkraut, Krüppelkiefern auf Klippen, Tangwälder unter Wasser |
| Licht | Hell, salzige Luftperspektive, Glitzern auf Wasser; Leuchtturmkegel nachts |
| Stille-Zustand | Wellen erstarren als glasige Wände, Möwen-Echos hängen still in der Luft, Gezeiten stoppen |

### 2.3 Wahrzeichen

**Saltrand-Hafen** (Werften, Kontorhaus mit goldener Glocke) · **Leuchtfelsen** (Leuchtturm auf 180 m Klippe) · **Treibdorf Flottholm** (Floßdorf, das mit der Gezeit seine Position in der Bucht ändert) · **Riffgrund** (Unterwasserzone mit Korallen-artigen Kristallformationen) · **Felsbogen „Thal'assyrs Rippe“**.

### 2.4 Wetter, Gezeiten & Tageszeit

- Klar 45 · Regen 25 · Gewitter 15 · Nebel 15.
- **Gezeiten (LOCKED):** Ebbe/Flut-Zyklus von **12 Spielstunden** (36 Echtzeitminuten). Ebbe legt Gezeitenbecken, Höhlen und Watt-Pfade frei (Spawns, Ressourcen); Flut öffnet Schwimmrouten. Flottholm folgt der Gezeit (2 Positionen).
- **Gewitter:** Sturm-Echos über der Brandung; Wellen höher (Schwimmen gegen Strömung schwerer).
- **Morgen:** Fischerboote laufen aus (NPC-Tagesablauf); **Nacht:** Biolumineszenz im Riff.

### 2.5 Umweltbelastung

Keine regulär. Gewitter an Klippen: **Windstoß** schiebt Gleiter seitlich (Lesbarkeit: sichtbare Böenlinien).

### 2.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Flut 9, Sturm 5, Stein 2, Licht 2, Klang 2, Blüte 1, Gift 1, Metall 1, Geist 1, Kristall 1, Arkan 1 (= 26) |
| Struktur | Seevogel-Kolonien (Klippen, Flugreiten-Horste), Gezeitenbecken-Kleintiere, Riffschwärme, große Meeresräuber (nur aus der Ferne, Unterwasser-Alpha im Riffgrund), Strandaasfresser |
| Seltene Bedingungen | Ebbe + Nacht in den Gezeitenhöhlen · Gewitter + Abenddämmerung am Leuchtfelsen · Nebel + Flut im Riffgrund |

### 2.7 Ressourcen

Treibholz (I), Zinnerz (I), Perlmutt (Kristall II, Unterwasser), Seetang (I), Salzkraut (I).

### 2.8 Bevölkerung & Kultur

Seeleute, Händler (Kontor), Werftarbeiter, Fischer, Leuchtturmwärter, Taucher mit Flut-Echos. Kleidung: Ölzeug, Streifenhemden, Messingknöpfe, Goldklang-Livree (Händler). Architektur: Backstein, Giebelhäuser, Speicher mit Kränen, Stege. **Gezeitenkult** (K07 §10). Rhythmus: Hafenglocke bei Flut; Markt bei Ebbe.

### 2.9 Quest-Themen (23)

Goldklang-Kontor-Einstieg (Fraktionsquests), Schiffbruch-Bergung (Unterwasser), Schmugglerhöhlen (Ebbe), Leuchtturm-Rettung im Sturm, Flottholms verlorene Anker, Wettfahrt mit Schwimm-Echos.

### 2.10 Stillezone-Zustand & Story

Stillezone über einem Teil des Riffs – Thal'assyrs Atem (die Gezeiten) stockt lokal; die Heilung stellt die Gezeiten in der Bucht wieder her (vorher: feste Ebbe → gezielte Story-Inszenierung).

### 2.11 Tech-Art & Audio

Ozean: Water-Plugin mit Gerstner-Wellen, Shoreline-Schaum; Unterwasser-Post-Process + Kaustiken; Gezeiten als animierter Wasserspiegel (Pegel ±1,2 m) mit Data-Layer-Pfaden. Audio: Brandung (distanzgesteuert), Möwen-Echos, Hafenglocke, Takelage; Stadtthema Saltrand-Hafen: Akkordeon-artige Harmonien, Shanty-Rhythmus, Glocke.

---

## 3. R07 Hvitfell – Schnee

### 3.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 3,6 km² · Akt II (frei) · T4–T7 (25–55) |
| Story-Gate | **Pass-Schneesturm** am Schweigfels-Pass – lichtet sich nach MQ |
| Klangfamilie | Hvitnisch |
| Ursprungsstimme | Isv'aldr (Frost/Licht) – Gletscherdom unter Hvitmark |
| Stadt | **Hvitmark** |
| Dörfer | **Fjallstad**, **Eiðvik-Neu** (wiederaufgebaut nach der Klangpest 948) |
| Außenposten | **Gletscherwacht**, **Passhütte**, **Isvaldtind-Biwak** |
| Sonderort | **Kloster Schweigfels** (Ordenssitz, F05) |
| Nebenquests | 20 |
| Fantasie | *„Im Eis bleibt alles erhalten – auch das, was man vergessen will.“* |
| Schlüsselwörter | Erinnerung · Härte · Schweigen |

### 3.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Schneeweiß `#F4F7FA`, Gletscherblau `#7FB6D6`, Nordnacht `#1B2440`, Auroragrün `#4FE3A5`, Holzrot (Häuser) `#8E2F2A` |
| Geologie | Gletscher mit Spalten, Eishöhlen, Basaltfjell, gefrorene Wasserfälle, **Erinnerungseis** (klares Eis, in dem Szenen der Vergangenheit eingefroren erscheinen – Lore-Medium) |
| Flora | Frostkiefern, Polarflechte, Eisblumen (selten, an heißen Quellen) |
| Licht | Tiefstehende Sonne, lange blaue Schatten; Aurora-Nächte; Subsurface Scattering im Eis |
| Stille-Zustand | Schneeflocken stehen still in der Luft; Aurora wird grau |

### 3.3 Wahrzeichen

**Isvaldtind** (2.100 m) · **Hvitmark** (Holzstadt im Gletschertal, Langhäuser) · **Kloster Schweigfels** (am Pass, schwarzer Stein, kein einziges Glockenläuten) · **Eiðvik-Ruinen** (Klangpest-Mahnmal) · **Gletscherdom** (Eiskathedrale unter Hvitmark).

### 3.4 Wetter & Tageszeit

- Klar 30 · Nebel 10 · Schnee 45 · Aurora 15 (nur nachts).
- **Aurora:** Licht- und Klang-Echos tanzen, seltenste Arten der Region; Isv'aldr „singt“ (Lore). **Polarnacht-Effekt:** Hvitfell hat eine um 2 Spielstunden **längere Nacht** als andere Regionen (Lichtsystem K15).
- **Schnee:** Spuren im Schnee (Tracking); Sicht reduziert.

### 3.5 Umweltbelastung

Kälte: mittel (Tal), stark (Gletscher, Nacht), extrem (Isvaldtind bei Schnee). Heiße Quellen und Langhäuser = Schutzzonen. Eis-/Kristallflächen nicht kletterbar (K02).

### 3.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Frost 9, Licht 3, Stein 2, Leere 2, Geist 2, Klang 2, Sturm 1, Kristall 1 (= 22) |
| Struktur | Rentier-artige Herden, Schneefuchs-Rudel, Eisfisch-Schwärme unter dem Eis, Gletscherwürmer, ein Spitzenräuber (Eisbär-Archetyp, Alpha) |
| Seltene Bedingungen | Aurora + Gletscherdom-Eingang · Schnee + Morgendämmerung auf dem Isvaldtind · Nebel + Nacht in Eiðvik (Geist) |

### 3.7 Ressourcen

Frostkiefer (III), Silbererz (III), Gletscherquarz (IV), Eisblume (IV, selten), Polarflechte (III).

### 3.8 Bevölkerung & Kultur

Fischer (Eisfischen), Pelzhändler (nur Wolle/Echo-Haar, kein Fell – Bundesrecht), Gletscherführer, Mönche/Nonnen des Ordens. Kleidung: Wolle mit Runenstickerei, Fellimitate, Schneebrillen aus Horn. Architektur: Langhäuser mit Grasdächern, Stabkonstruktionen. Rhythmus: Gemeinschaftliche Abendfeuer; Klangpest-Gedenktag (LiveOps). **Sensitivity-Review** (nordische Anmutung).

### 3.9 Quest-Themen (20)

Erinnerungseis-Visionen (Lore W3/W7), Klangpest-Überlebende (Ursprung des Ordens, Grauzonen-Moral), Gletscherrettung, Aurora-Fotografie (Kodex-Linse), Ordensnovizen mit Zweifeln.

### 3.10 Stillezone-Zustand & Story

Älteste Stillezonen (seit 990 n.St., CANON §35). Kloster Schweigfels ist Schauplatz der Begegnung mit Sereth Vaun (Akt II) und der Enthüllung von W6 (Verrat) aus Ordenssicht.

### 3.11 Tech-Art & Audio

Schnee: Runtime Virtual Texture-Deformation (Spuren), `M_Snow_Master`, Schneeverwehung per Niagara; Eis: Substrate-Material mit SSS und Refraktion (Switch 2: vereinfachte Variante). Audio: Wind in Böen, knirschender Schnee, Eis-Knacken (gemischt mit tiefen Drones); Stadtthema Hvitmark: Hardanger-artige Fidel-Klangfarbe, Obertongesang; Kloster: **bewusste Stille** – nur Raumklang, Schritte.

---

## 4. R08 Ael'Dorun – Ruinen

### 4.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 2,8 km² · Akt II (nach 2 weiteren Akt-II-Regionen) · T6–T7 (37–55) |
| Story-Gate | **Ruinensiegel** – dorunische Barriere, öffnet sich mit 2 Akt-II-Akkorden + MQ |
| Klangfamilie | Dorunisch (Altsprache) |
| Ursprungsstimme | Ka'thurel (Geist/Arkan) – Thronsaal-Gewölbe unter Dorunsruh |
| Stadt | **Dorunsruh** (Akademie-Hauptsitz am Ruinenrand) |
| Dörfer | **Thae'Luun** (Grabungsdorf), **Säulenrast** |
| Außenposten | **Grabungslager Nord**, **Archontenwacht**, **Ruinenpfad-Posten** |
| Nebenquests | 21 |
| Fantasie | *„Eine Stadt, die sich an alles erinnert – nur nicht daran, warum sie fiel.“* |
| Schlüsselwörter | Mysterium · Größe · Schuld |

### 4.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Alabaster `#E6DFD1`, Patinagrün `#5F8F7F`, Glyphengold `#E3B54C`, Schattenviolett `#3C2F4F`, Stilleschwarz `#141418` |
| Geologie | Tafelland mit Terrassen, eingestürzte Kuppeln, **schwebende Ruinenfragmente** (Ka'thurels Einfluss), Treppenschluchten |
| Flora | Ruinenrebe, Altholz-Bäume, die durch Säulen wachsen, Moos in Glyphenmustern |
| Licht | Gelbliche Nachmittagsstimmung, Glyphen leuchten bei Resonanz; nachts Geisterlicht |
| Stille-Zustand | **Größte Stillezonen der Welt** (Ursprung W3): ganze Viertel grau, Fragmente fallen herab und schweben still über dem Boden |

### 4.3 Wahrzeichen

**Thronstadt** mit der **Archontenkuppel** (Kuppel über dem Thronsaal, halb eingestürzt) · **Säulenfeld Thae'Luun** (Tausende Säulen, Klangrätsel-Hotspot) · **Dorunsruh** (Akademie: moderne Glas-und-Messing-Bauten an alten Mauern) · **Resonanzturm-Stumpf** (Ruine eines der dorunischen Verstärkertürme) · **Treppe der Zehn** (zehn Statuen des Erstchors, eine – Ilen – gesichtslos).

### 4.4 Wetter & Tageszeit

- Klar 50 · Regen 15 · Gewitter 5 · Nebel 30.
- **Nebel:** Geist-Echos „spielen“ Szenen der Vergangenheit nach (Umwelt-Erzählung: Geisterszenen nur bei Nebel, 12 Szenen).
- **Nacht:** Glyphen aktiv; Arkan-Echos ordnen Fragmente zu Mustern (Kodex-Beobachtung).

### 4.5 Umweltbelastung

Stille (mittel–stark) in Stillezonen bis zu deren Lösung; ansonsten keine. Gewölbe: Dunkelheit (§1).

### 4.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Arkan 5, Geist 5, Metall 3, Klang 2, Leere 2, Stein 1, Licht 1, Schwerkraft 1 (= 20) |
| Struktur | Ruinenbewohner (Mauersegler-artige Schwärme), konstruktartige Metall-Echos (**keine Roboter** – Lore: Metall-Obertöne, die sich in dorunischen Bauwerken angesiedelt haben), Geist-Echos als Erinnerungsträger, Leere-Räuber am Zonenrand |
| Seltene Bedingungen | Nebel + Nacht im Archontenviertel · Gewitter über der Kuppel · Resonanzsturm (W10, story) in der Thronstadt |

### 4.7 Ressourcen

Altholz (IV), Dorunstein (IV), Glyphenkristall (IV), Ruinenrebe (III).

### 4.8 Bevölkerung & Kultur

Akademie-Forschende, Ausgräber, Restauratoren, Ordenspilger (Kapelle in Säulenrast), Schatzsucher (zwielichtig). Kleidung: Akademie-Roben (Dunkelblau mit Messingabzeichen), Grabungskleidung. Architektur Dorunsruh: Glas, Messing, Klangwerk-Aufzüge an dorunischen Mauern. Rhythmus: Akademie-Glocke (Vorlesungen), Grabungsschichten tagsüber.

### 4.9 Quest-Themen (21)

Akademie-Forschungsaufträge (Fraktion F01), Glyphen-Übersetzung (Rätselkette, 10 Teile), Geisterszenen sammeln (Fotografie/Kodex), Schatzsucher-Rivalen, die Treppe der Zehn (Erstchor-Lore), Kael als Akademie-Kollege (vor W6).

### 4.10 Stillezone-Zustand & Story

Akt-II-Wende (W6) und -Ende (W7) finden hier statt; Venn öffnet das Thronsaal-Gewölbe mit den Akkorden des Spielers. Heilung: Glyphen erwachen dauerhaft, Fragmente setzen sich teilweise wieder zusammen (Data Layer `DL_Story_R08_Healed`, sichtbare Architekturänderung).

### 4.11 Tech-Art & Audio

Modulares Ruinen-Kit (Nanite, ~180 Module), Zerfall-Varianten per PCG `PCG_R08_Debris`; schwebende Fragmente als Instanced Static Meshes mit WPO-Bob (Mass-tauglich, keine Physik); Glyphen-Emissive via Material Parameter Collection (`MPC_Glyphs`). Audio: Hallräume, Windharfen in Säulen, Geisterflüstern (unverständlich, L-01); Stadtthema Dorunsruh: Cembalo-artige Arpeggien + Streichquartett; Ruinen: Chor-Fragmente.

---

## 5. R09 Prismtiefen – Kristallhöhlen

### 5.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 3,6 km² (Krater-Footprint; Höhlen darunter) · Kraterrand ab Akt I begehbar (Aussichtspunkt), Höhlen **Akt III** · fest 50–62 |
| Klangfamilie | Prismanisch |
| Ursprungsstimme | Prism'aion (Kristall/Klang) – Resonanzkammer unter Prismara |
| Stadt | **Prismara** (unterirdisch, −180 m) |
| Dörfer | **Glanzschacht** (Bergarbeiterdorf), **Quarzgrund** |
| Außenposten | **Liftstation Kraterrand**, **Kristallsee-Lager**, **Missklang-Wacht** |
| Nebenquests | 18 |
| Fantasie | *„Licht wird hier zu Musik – und die Musik erinnert sich an einen Schrei.“* |
| Schlüsselwörter | Pracht · Tiefe · Missklang |

### 5.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Amethyst `#7E57C2`, Quarzrosa `#E9A6C8`, Tiefblau `#14203A`, Kristallcyan `#5ED6E8`, **Missklang-Rot** `#C2185B` (verzerrte Kristalle) |
| Geologie | Krater (−250 m), Kristallkathedralen (bis 80 m hohe Kavernen), Geoden, Kristallsee, **Missklang-Adern** (rot verzerrte Kristalle aus der Zeit der Resonanzkrone, -20 v.St.) |
| Flora | Höhlenpilze, Kristallmoos, leuchtende Flechten |
| Licht | Selbstleuchtende Kristalle (gesteuert: an/aus durch Resonanz), Lichtbrechung als Rätselmechanik |
| Stille-Zustand | Kristalle verlieren Glanz und werden trüb-grau; Licht bricht nicht mehr |

### 5.3 Wahrzeichen

**Kraterrand mit Liftstation** (Panorama, ab Akt I) · **Prismara** (Stadt in einer Geodenkaverne, Häuser aus Kristallglas) · **Kristallsee** (unterirdisch, Unterwasserzone) · **Missklang-Adern** (Endgame-nah, Gefahr) · **Tiefe Resonanz** (Eingang zu den Tiefenresonanzen, K62).

### 5.4 Wetter & Tageszeit

- Höhlenklima (100 % Klar); Wetter der Oberfläche (R08-Tabelle) beeinflusst nur den Kraterrand.
- **Tageszeit unter Tage:** Prismara simuliert sie mit **Lichtkristall-Zyklen** (Stadtbeleuchtung folgt der Oberflächenzeit); Höhlen-Echos folgen *eigenem* Rhythmus („Kristallpuls“ alle 6 Spielstunden: kurz hell, Echos aktiv).
- **Resonanzsturm (W10):** Einzige Wetterwirkung unter Tage – alle Kristalle leuchten, Missklang-Adern pulsieren (Event-Spawns).

### 5.5 Umweltbelastung

Dunkelheit (§1) außerhalb beleuchteter Bereiche; Dunst (stark) in Missklang-Adern; Kälte (schwach) am Kristallsee.

### 5.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Kristall 8, Leere 3, Schwerkraft 3, Arkan 2, Metall 2, Klang 1, Gift 1 (= 20) |
| Struktur | Kristallfresser (Lithophagen), Höhlenflieger-Schwärme, blinde Lauerjäger (Klang-Ortung → reagieren auf Geräusch: Schleichen wichtig), Pilzgärtner-Kolonien |
| Seltene Bedingungen | Kristallpuls + Missklang-Ader · Resonanzsturm · völlige Dunkelheit (alle Lichtquellen aus) im Quarzgrund |

### 5.7 Ressourcen

Prismaerz (V), Resonanzkristall (V, selten), Höhlenpilz (IV), Kristallmoos (V).

### 5.8 Bevölkerung & Kultur

Bergleute, Glasbläser, Kristallstimmer (stimmen Kristalle für Klangwerk-Energie), Akademie-Labore. Kleidung: Lederschürzen, Kristallsplitter-Schmuck, Grubenlampen. Architektur: Kristallglas, Messingstreben, Liftanlagen. Rhythmus: Lichtkristall-Zyklus, Schichtwechsel-Glocken.

### 5.9 Quest-Themen (18)

Verschüttete Kristallstimmer, Lichtbrechungs-Rätsel, Missklang-Forschung (Lore W7), Prismaras Energiekrise (Stillezone dämpft Kristalle), Glasbläser-Meisterwerk (Crafting V).

### 5.10 Stillezone-Zustand & Story

Akt III: Kronensplitter-Versteck; Prism'aion erwacht; die Missklang-Adern zeigen, was die Krone der Welt angetan hat (emotionaler Beleg für die Entscheidung im Finale).

### 5.11 Tech-Art & Audio

Höhlen als Level Instances (`Underground`-Grid, K08 §10.2); Kristall-Material mit Substrate (Dispersion vereinfacht), Licht über Emissive + Lumen (Switch 2: vorgebackene Lichtvarianten pro Zustand an/aus); Lichtbrechungsrätsel über Spline-Strahlen (deterministisch, keine Physik-Raytraces). Audio: Kristall-Klingen (Tonhöhe = Kristallgröße), Tropfen mit langem Hall, Missklang = verstimmte Cluster; Stadtthema Prismara: Glasharmonika, Celesta, Streicher-Flageoletts.

---

## 6. R10 Nimbara – Himmelinseln

### 6.1 Steckbrief

| Feld | Wert |
|---|---|
| Fläche / Akt / Level | 4,0 km² Footprint · Akt III + Finale · fest 58–70 |
| Zugang | Story (Akt III) + Flugreiten; vor Akt III nur sichtbar (Sichtachse ab Minute 1, ADR-043) |
| Klangfamilie | Nimbari |
| Ursprungsstimme | **Aeth'rion** (Klang/Licht, Leitstimme) – Sternenarena von Aerion |
| Stadt | **Aerion** (1.800 m) |
| Dörfer | **Lumeya**, **Wolkenrast** |
| Außenposten | **Kronenwerft-Wacht**, **Sternwarte Oruma**, **Windanker** |
| Nebenquests | 20 |
| Fantasie | *„Über den Wolken klingt das Lied noch – leise, fast vergessen.“* |
| Schlüsselwörter | Erhabenheit · Freiheit · Entscheidung |

### 6.2 Visuelle Identität

| Element | Beschreibung |
|---|---|
| Palette | Himmelsblau `#7EC8F0`, Wolkenweiß `#FFFFFF`, Morgenrosa `#F5B3C6`, Weißgold `#F0D78C`, Sternennacht `#0D1330` |
| Geologie | Schwebende Inseln (von Orh'gruuns Schwerkraft gehoben, ~-250 v.St.), Wasserfälle, die ins Nichts fallen und als Nebel enden, Kristallanker unter den Inseln |
| Flora | Wolkenholz-Bäume (leicht, weiß), Windblüten, Moospolster |
| Licht | Über den Wolken: klares, starkes Sonnenlicht; Wolkenmeer darunter; nachts Sternenpracht, Aurora (15 %) |
| Stille-Zustand | Inseln sinken langsam (Story Akt III: Riegel bricht), Wolken erstarren |

### 6.3 Wahrzeichen

**Aerion** (Himmelsstadt, Terrassen, Klangwerk-Gondeln) · **Sternenarena** (2.600 m, offene Arena über allem, Schlafort Aeth'rions, Finale) · **Kronenwerft** (Ruine der Werkstatt Maedryns, Ort der Resonanzkrone) · **Lumeya-Inseln** (Außeninseln, nur per Flugreiten) · **Wolkenfälle**.

### 6.4 Wetter & Tageszeit

- Klar 45 · Regen 10 · Gewitter 20 · Nebel 10 (Wolkenmeer steigt auf) · Aurora 15 (nachts).
- **Gewitter:** Aufwinde +50 %, Blitze treffen Kristallanker (Licht-Echos laden auf).
- **Tag** länger hell (über den Wolken: Sonnenaufgang 1 Spielstunde früher, Untergang 1 Stunde später – K15).

### 6.5 Umweltbelastung

Kälte (mittel ab 2.000 m, stark nachts bei Gewitter); Fallrettung und Aufwinde (§1).

### 6.6 Ökologie

| Aspekt | Festlegung |
|---|---|
| Typverteilung | Sturm 6, Klang 4, Licht 4, Schwerkraft 3, Arkan 2, Frost 1, Kristall 1, Leere 1 (= 22) |
| Struktur | Wolkenwal-artige Gleiter (Herde in der Luft), Windfalken (Räuber), Inselbewohner (flugunfähige Arten – Inselendemiten!), Sternenfalter |
| Seltene Bedingungen | Aurora + Sternenarena · Gewitter + Kronenwerft · Morgendämmerung über dem Wolkenmeer (Lumeya) |

### 6.7 Ressourcen

Wolkenholz (V), Sternmetall (V, selten), Himmelsglas (V), Windblüte (V).

### 6.8 Bevölkerung & Kultur

Nachfahren nimbarischer Baumeister (kleines, abgeschiedenes Volk, ~800 Einwohner in Aerion – haben die Stille überdauert, bewahren Wissen über den Erstchor), Sternkundige, Windsegler. Kleidung: Weiß und Gold, leichte Stoffe, Federn (Echo-Mauser), Windbänder. Architektur: Filigrane Bögen, Klangwerk-Gondeln, Windharfen. Rhythmus: Begrüßung der Sonne (Morgenzeremonie), Sternenlesen nachts.

### 6.9 Quest-Themen (20)

Nimbarische Vorbehalte gegenüber Bodenbewohnern, die Kronenwerft-Archive (Lore W8/W9), Rennen in Windströmen, Inselendemiten schützen (Wildwacht), Sternwarten-Rätsel (Mondphasen, Q15), letzte Bitten vor dem Finale (Atemzug-Fenster DR-29).

### 6.10 Stillezone-Zustand & Story

Finale (Akt III): Venn in der Sternenarena, Riegel bricht, Velnox frei; Entscheidung zwischen „Neues Lied“ und „Sanfte Stille“ (CANON §38). Nach dem Finale: Inseln stabilisiert (Neues Lied) bzw. sanft gesunken auf niedrigere, aber stabile Höhe (Sanfte Stille – rein optisch, alle Inhalte bleiben erreichbar).

### 6.11 Tech-Art & Audio

Inseln: Nanite-Meshes mit Unterseiten-Detail (sichtbar vom Boden aus), Wolkenmeer: Volumetric Clouds (UE Sky Atmosphere + Volumetric Cloud; Switch 2: vorgebackene Wolkenkarten + Billboard-Layer); Aufwinde/Windströme als Spline-Volumes mit Niagara-Visualisierung. Audio: Wind (hoch, offen), Windharfen (in Tonart der Musik), entfernte Wolkenwal-Rufe; Stadtthema Aerion: Frauen-/Kinderchor, Harfe, Glocken – Leitmotiv des Weltlieds in voller Form erst hier.

---

## 7. Biom-Vergleich (alle 10)

| Region | Akt | Level | Haupttyp | Belastung | Sondermechanik | Tagesrhythmus | Nebenq. |
|---|---|---|---|---|---|---|---|
| R01 Verdanthain | Prolog/I | 2–14 | Blüte | – | Glockenblüten | normal | 24 |
| R02 Kharsgrat | I | T1–3 | Stein | Kälte | Schwebefelsen, Klettern | Schichten | 22 |
| R03 Morvenmoor | I | T1–3 | Gift | Dunst | Wasserstand, Nebel | Nachtmärkte | 21 |
| R06 Saltrand | I | T1–3 | Flut | – | Gezeiten (12 h), Unterwasser | Hafenglocke | 23 |
| R04 Sahrun | II | T4–7 | Stein/Licht | Hitze/Kälte | Sandsturm-Navigation, Wanderdorf | nachtaktiv | 22 |
| R05 Ignareth | II | T4–7 | Glut | Hitze/Asche | Ausbrüche (3 Tage) | Schmiedeglocken | 19 |
| R07 Hvitfell | II | T4–7 | Frost | Kälte | Erinnerungseis, längere Nacht | Abendfeuer | 20 |
| R08 Ael'Dorun | II | T6–7 | Arkan/Geist | Stille | Geisterszenen bei Nebel, Glyphen | Akademie-Glocke | 21 |
| R09 Prismtiefen | III | 50–62 | Kristall | Dunkelheit/Dunst | Lichtbrechung, Kristallpuls | Lichtkristall-Zyklus | 18 |
| R10 Nimbara | III | 58–70 | Sturm | Kälte | Aufwinde, Windströme, Fallrettung | längerer Tag | 20 |
| **Σ** | | | | | | | **210** |

**Prüfung:** Jede Region erfüllt alle Template-Blöcke (Briefing: Wetter ✔, Tageszeit ✔, NPCs ✔, Quests ✔, seltene Kreaturen ✔, Ressourcen ✔).

---

## 8. Code

### 8.1 Gezeiten (GF_World)

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Public/Tides/TideSubsystem.h
/**
 * Gezeiten in Saltrand (K10 §2.4): 12-Spielstunden-Zyklus, Pegel ±1,2 m.
 * Pegel ist eine reine Funktion der Spielzeit → in Koop automatisch synchron (Spielzeit wird repliziert, K59).
 */
UCLASS()
class GF_WORLD_API UTideSubsystem : public UWorldSubsystem
{
	GENERATED_BODY()
public:
	/** Pegel in cm relativ zum Mittelwasser, abhängig von der Spielzeit in Minuten seit Tagesbeginn. */
	static float GetTideOffsetCm(float GameMinutesOfDay)
	{
		constexpr float PeriodMinutes = 12.f * 60.f;     // 12 Spielstunden
		constexpr float AmplitudeCm   = 120.f;           // ±1,2 m
		return AmplitudeCm * FMath::Sin(2.f * PI * GameMinutesOfDay / PeriodMinutes);
	}

	/** true bei Ebbe-Phase (Pegel < −60 cm): Gezeitenpfade-Data-Layer aktiv. */
	static bool IsLowTide(float GameMinutesOfDay) { return GetTideOffsetCm(GameMinutesOfDay) < -60.f; }

	/** Wird von der Tageszeit (K15) bei jeder Spielminute aufgerufen; schaltet Data Layers um. */
	void OnGameMinute(float GameMinutesOfDay);
};
```

### 8.2 Fallrettung (AethrisGame, Spielercharakter)

```cpp
// AethrisGame/Private/Player/WardenFallRescueComponent.cpp (Auszug)
// Merkt sich regelmäßig einen sicheren Bodenpunkt und setzt bei „Fall ins Nichts“ zurück (K10 §1).
void UWardenFallRescueComponent::OnMovementUpdate(const FVector& Velocity, bool bGrounded, bool bGliding)
{
	if (bGrounded && IsSafeGround())                    // begehbarer Navmesh-Boden, keine Lava/Wasser-Tiefe
	{
		LastSafeLocation = GetOwner()->GetActorLocation();
		FallStartZ.Reset();
		return;
	}
	if (bGliding) { FallStartZ.Reset(); return; }

	if (!FallStartZ) { FallStartZ = GetOwner()->GetActorLocation().Z; FallTime = 0.f; }
	FallTime += GetWorld()->GetDeltaSeconds();

	const float Dropped = (*FallStartZ - GetOwner()->GetActorLocation().Z) / 100.f;   // m
	if (Dropped > 30.f && Settings->bAutoGlide && HasGlider())
	{
		OpenGlider();                                    // Standard an (Option)
	}
	else if (FallTime > 2.f && !HasGroundBelow(/*MaxDistM*/ 400.f))
	{
		TriggerResonanceJump(LastSafeLocation);          // Abblende + Klangeffekt, keine Strafe
	}
}
```

### 8.3 Lichtwert für Dunkelheit

```cpp
// GF_World: Lichtwert 0..100 aus Szenen-Probe + Lichtquellen in der Nähe (K10 §1).
int32 UDarknessSubsystem::ComputeLightLevel(const FVector& Location) const
{
	const int32 Ambient = SampleAmbientLuminance(Location);          // vorgebackene Licht-Probe-Gitter (kein GPU-Readback)
	int32 Sources = 0;
	for (const FLightContributor& L : NearbyLightContributors(Location, 1200.f))  // Laternen, Kristalle, Begleiter
	{
		Sources += L.Strength * FMath::Max(0.f, 1.f - FVector::Dist(Location, L.Location) / L.RadiusCm);
	}
	return FMath::Clamp(Ambient + Sources, 0, 100);
}
```

*Designnotiz:* Kein GPU-Readback der Lumen-Szene (teuer, plattformabhängig) – stattdessen ein vorgebackenes Lichtproben-Gitter (2 m Auflösung in Höhlen) plus dynamische Lichtquellen aus Gameplay-Daten. Deterministisch und günstig.

---

## 9. Decision Records

### ADR-050 – Unterwasser ohne Ertrinken, nur mit Schwimm-Echo
- **Entscheidung:** Tauchen setzt Schwimmreiten voraus (Atemkugel). Vorteil: Echo-Partnerschaft im Zentrum (S2), kein Luftmanagement-Frust. Nachteil: Unterwasserinhalte erst ab Schwimmreiten → diese zählen zu den optionalen Rückkehr-POIs (DR-28).

### ADR-051 – Resonanzsprung statt Fallschaden
- **Entscheidung:** Kein Fallschaden, kein Tod; Fallrettung durch Auto-Gleiter oder Resonanzsprung. Vorteil: Himmelinseln können mutig vertikal designt werden. Nachteil: geringeres Risiko-Gefühl → Spannung entsteht durch Zeitverlust und Windströme, nicht durch Strafe.

### ADR-052 – Lichtwert ohne GPU-Readback
- **Entscheidung:** Vorgebackenes Lichtproben-Gitter + Gameplay-Lichtquellen (§8.3). Deterministisch, plattformgleich (Switch 2), billig.

### ADR-053 – Regionale Tageslängen-Abweichungen
- **Entscheidung:** Hvitfell +2 h Nacht, Nimbara +2 h Tag (je 1 h früher/später). Wird im Lichtsystem K15 als regionaler Offset der Sonnenkurve umgesetzt; Spielzeit selbst bleibt global (Koop-Synchronität).

---

## 10. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §48 | Biome R06–R10 nach Template inkl. Wahrzeichen, Paletten, Rhythmen, Quest-Themen, Story-Orten, Tech-Art/Audio | LOCKED |
| §48 | Saltrand: Gezeiten 12-Spielstunden-Zyklus, Pegel ±1,2 m, Ebbe < −60 cm schaltet Pfade; Flottholm 2 Positionen | LOCKED |
| §48 | Hvitfell: Erinnerungseis (Lore-Medium), Nacht +2 h; Kloster Schweigfels = Ordenssitz und Schauplatz W6 aus Ordenssicht | LOCKED |
| §48 | Ael'Dorun: 12 Geisterszenen bei Nebel, Treppe der Zehn, Metall-Echos sind keine Roboter; Ort von W6/W7 | LOCKED |
| §48 | Prismtiefen: Kraterrand ab Akt I, Höhlen Akt III; Kristallpuls alle 6 Spielstunden; Missklang-Adern; Eingang Tiefenresonanzen | LOCKED |
| §48 | Nimbara: Aerion (~800 Einwohner, Nachfahren der Baumeister), Sternenarena 2.600 m (Finale), Kronenwerft; Tag +2 h; nach „Sanfte Stille“ Inseln niedriger, Inhalte unverändert | LOCKED |
| §49 | Siedlungsnamen R06–R10 (§2–§6) | LOCKED |
| §50 | Unterwasser (Atemkugel, kein Ertrinken), Dunkelheit (Lichtwert 0–100, Schwelle 15), Fallrettung (> 30 m Auto-Gleiter, Resonanzsprung nach 2 s), Aufwinde 6 m/s, Windströme 18 m/s, Gewitter +50 % Aufwind | LOCKED |
| §10 | ADR-050 – ADR-053 | LOCKED |

---

## 11. Kapitel-Checkliste

- [x] Vier Sondermechaniken (Unterwasser, Dunkelheit, Fallrettung, Aufwinde/Windströme)
- [x] Saltrand, Hvitfell, Ael'Dorun, Prismtiefen, Nimbara vollständig nach Template
- [x] Namen von 11 Dörfern (inkl. Treibdorf) und 15 Außenposten → alle 22 Dörfer und 30 Außenposten benannt
- [x] Vergleichstabelle aller 10 Biome (Nebenquests Σ 210)
- [x] Code: Gezeiten, Fallrettung, Lichtwert
- [x] ADR-050 – ADR-053, CANON aktualisiert

➡️ **Nächstes Kapitel: K11 – Städte I (Eichenhall, Kharsholm, Morvenfurt, Saltrand-Hafen, Qasr Sahrun).**
