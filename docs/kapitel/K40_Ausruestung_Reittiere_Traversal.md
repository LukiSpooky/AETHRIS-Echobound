# K40 · Ausrüstung, Reittiere und Traversal

| Feld | Wert |
|---|---|
| Dokument | Kapitel 40 von 68 · Systeme, Teil V |
| Version | 1.0 |
| Owner | Lead Traversal Designer |
| Mitwirkende | Lead Gameplay Programmer (Charakterbewegung), Animation Director (Reit-Rigs), Level Design (Pfad-Tore), Economy Designer (Ausrüstung), Creature Design (Reittiere) |
| Baut auf | K02 §4.1 (Starttuning), CANON §15 (Traversal-Reihenfolge), §18 (P8 Ausrüstung I–V), §42 (Gates), §62 (Wetter-Traversal), §107 (Feldfähigkeiten, Pfad-Tore), K20–K27 (50 Reittiere), DR-23, DR-28 |
| Status | ✅ Freigegeben – **löst Q11** (Bewegungs-/Ausdauer-/Gleiter-Tuning) |
| Im Repository | `Data/World/TraversalTuning.csv`, `Data/World/MountKinds.csv`, `Data/World/PathGates.csv` (12), `Data/Items/WardenGear.csv` (50), `Data/Items/HeldItems.csv` (32), `tools/ref/aethris_traversal.py` |
| Neue Kanon-Einträge | CANON §151 (Bewegung & Ausdauer), §152 (Wärter-Ausrüstung), §153 (Reiten), §154 (Pfad-Tore final), §155 (Halteitems) |

---

## Inhalt

1. [Traversal-Fantasie](#1-traversal-fantasie)
2. [Bewegung und Ausdauer (Q11)](#2-bewegung-und-ausdauer-q11)
3. [Wärter-Ausrüstung](#3-wärter-ausrüstung)
4. [Reiten](#4-reiten)
5. [Pfad-Tore](#5-pfad-tore)
6. [Halteitems der Echos](#6-halteitems-der-echos)
7. [Reisezeiten und Weltgröße](#7-reisezeiten-und-weltgröße)
8. [Wetter und Traversal](#8-wetter-und-traversal)
9. [Kamera und Steuerung](#9-kamera-und-steuerung)
10. [Code](#10-code)
11. [Tests und Telemetrie](#11-tests-und-telemetrie)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Traversal-Fantasie

> *Ich gleite vom Glockenturm in Eichenhall, lande auf Cragars Rücken, galoppiere zum Steilhang, wechsle auf Hallbrand und klettere die Wand hinauf. Oben wartet ein Wetterumschwung – und mein Brokkar wittert Erz.*

Traversal ist in AETHRIS **Fortschritt und Ausdruck**: Jede neue Reitart öffnet die Welt anders (Flüsse, Wände, Dünen, Himmel), und weil jede Reitart an konkrete Echos gebunden ist, wird Sammeln zu Mobilität. DR-28 sichert, dass der Hauptpfad jeder Region mit der frühesten Ausstattung spielbar bleibt; neue Fähigkeiten öffnen **Abkürzungen, Geheimnisse und Komfort**.

---

## 2. Bewegung und Ausdauer (Q11)

| Name | Value | Unit | Notes |
|---|---|---|---|
| WalkSpeed | 1.8 | m/s | Analog-Stufe 1 |
| JogSpeed | 4.2 | m/s | Analog-Stufe 2 |
| SprintSpeed | 7.0 | m/s | −12 AE/s |
| StaminaBase | 100 | AE | +10 je Stiefel-Stufe II–V, +20 Skill Überleben (K43); max. 160 |
| StaminaRegen | 25 | AE/s | nach 1,0 s ohne Verbrauch; im Regen 20 |
| SprintDrain | 12 | AE/s |  |
| ClimbSpeed | 1.6 | m/s | −8 AE/s; Sprungklettern 3 m für 15 AE |
| ClimbForbidden | – | – | Eis, Kristall, nasser Fels bei Regen/Gewitter, Sandsturm (CANON §62) |
| SwimSpeed | 1.5 | m/s | −4 AE/s; Tauchen nur mit Atemmaske (Ausrüstung) |
| SwimFastSpeed | 3.0 | m/s | −10 AE/s |
| GliderSink | 1.8 | m/s | Stufe I; −0,15 je Stufe (V: 1,2) |
| GliderForward | 9.0 | m/s | Stufe I; +0,75 je Stufe (V: 12) |
| GliderDrain | 6 | AE/s | Stufe I; −1 je Stufe (V: 2) |
| FallSafeHeight | 12 | m | ohne Gleiter: darüber Abrollen (0,8 s Stillstand) |
| FallRescueHeight | 30 | m | darüber: Resonanz-Fangnetz – Wärter landet sicher, 2 s Benommenheit, kein Schaden |
| JumpHeight | 1.4 | m |  |
| StealthCrouchNoise | 0.5 | Faktor | Geräuschradius beim Ducken |
| WindStealthBonus | 0.7 | Faktor | Entdeckungsradius bei Gegenwind |

**Q11 gelöst:** Die Startwerte aus K02 §4.1 bleiben als Basis bestehen; sie werden über Ausrüstung (§3) und Skilltree (K43) gestaffelt verbessert, nie über Echtgeld (CANON §8).

| Situation | Regel |
|---|---|
| Ausdauer leer beim Klettern | Wärter rutscht kontrolliert bis zum nächsten Vorsprung (kein Absturz) |
| Ausdauer leer beim Schwimmen | Wärter treibt an der Oberfläche, Ausdauer regeneriert mit 10 AE/s, Bewegung 0,8 m/s |
| Ausdauer leer beim Gleiten | Gleiter klappt ein; Fall mit Abrollen bzw. Fangnetz (§2-Tabelle) |
| Kein Tod | Fallschaden existiert nicht; ab 30 m fängt das **Resonanz-Fangnetz** (Resonator-Funktion) den Wärter – diegetisch und ohne Strafe (DR-23) |
| Anheben | Lauf- und Klettertempo +10 % auf Pfaden/Straßen (Weggefühl) |

---

## 3. Wärter-Ausrüstung

Der Wärter trägt **neun Ausrüstungsplätze** mit je fünf Stufen (P8: I–V). Ausrüstung verbessert **Traversal, Komfort und Bindungs-Timing** – nie Kampfwerte, nie Bindungsschwellen (DR-01).

| DisplayName | Slot | Tier | Effect | Sources |
|---|---|---|---|---|
| Resonator I | RESONATOR | 1 | Bindungs-Fenster ×1,00 · Resonanzsinn 60 m | Start/Prolog |
| Resonator II | RESONATOR | 2 | Bindungs-Fenster ×1,03 · Resonanzsinn 75 m | Händler (Akkord 2) · Crafting |
| Resonator III | RESONATOR | 3 | Bindungs-Fenster ×1,06 · Resonanzsinn 90 m | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Resonator IV | RESONATOR | 4 | Bindungs-Fenster ×1,09 · Resonanzsinn 105 m | Crafting (Akt II) · Fraktion Ruf 4 |
| Resonator V | RESONATOR | 5 | Bindungs-Fenster ×1,12 · Resonanzsinn 120 m | Crafting (Endgame) · Fraktion Ruf 6 |
| Gleiter I | GLIDER | 1 | Sinkrate 1,80 m/s · Vorwärts 9,0 m/s · 6 AE/s | Start/Prolog |
| Gleiter II | GLIDER | 2 | Sinkrate 1,65 m/s · Vorwärts 9,75 m/s · 5 AE/s | Händler (Akkord 2) · Crafting |
| Gleiter III | GLIDER | 3 | Sinkrate 1,50 m/s · Vorwärts 10,5 m/s · 4 AE/s | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Gleiter IV | GLIDER | 4 | Sinkrate 1,35 m/s · Vorwärts 11,25 m/s · 3 AE/s | Crafting (Akt II) · Fraktion Ruf 4 |
| Gleiter V | GLIDER | 5 | Sinkrate 1,20 m/s · Vorwärts 12,0 m/s · 2 AE/s | Crafting (Endgame) · Fraktion Ruf 6 |
| Wanderstiefel I | BOOTS | 1 | Ausdauer +0 · Klettern 1,6 m/s | Start/Prolog |
| Wanderstiefel II | BOOTS | 2 | Ausdauer +10 · Klettern 1,7 m/s | Händler (Akkord 2) · Crafting |
| Wanderstiefel III | BOOTS | 3 | Ausdauer +20 · Klettern 1,8 m/s | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Wanderstiefel IV | BOOTS | 4 | Ausdauer +30 · Klettern 1,9 m/s | Crafting (Akt II) · Fraktion Ruf 4 |
| Wanderstiefel V | BOOTS | 5 | Ausdauer +40 · Klettern 2,0 m/s | Crafting (Endgame) · Fraktion Ruf 6 |
| Wettermantel I | CLOAK | 1 | Wetterschutz – (Ausdauer-Regen-Malus/Sandsturm-Ritt −0 %) | Start/Prolog |
| Wettermantel II | CLOAK | 2 | Wetterschutz Regen (Ausdauer-Regen-Malus/Sandsturm-Ritt −10 %) | Händler (Akkord 2) · Crafting |
| Wettermantel III | CLOAK | 3 | Wetterschutz Regen, Schnee (Ausdauer-Regen-Malus/Sandsturm-Ritt −20 %) | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Wettermantel IV | CLOAK | 4 | Wetterschutz Regen, Schnee, Sand (Ausdauer-Regen-Malus/Sandsturm-Ritt −25 %) | Crafting (Akt II) · Fraktion Ruf 4 |
| Wettermantel V | CLOAK | 5 | Wetterschutz alle (Ausdauer-Regen-Malus/Sandsturm-Ritt −30 %) | Crafting (Endgame) · Fraktion Ruf 6 |
| Wärtertasche I | BAG | 1 | Taschenplätze je Kategorie 30 | Start/Prolog |
| Wärtertasche II | BAG | 2 | Taschenplätze je Kategorie 40 | Händler (Akkord 2) · Crafting |
| Wärtertasche III | BAG | 3 | Taschenplätze je Kategorie 50 | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Wärtertasche IV | BAG | 4 | Taschenplätze je Kategorie 60 | Crafting (Akt II) · Fraktion Ruf 4 |
| Wärtertasche V | BAG | 5 | Taschenplätze je Kategorie 80 | Crafting (Endgame) · Fraktion Ruf 6 |
| Kodex-Linse I | LENS | 1 | Zoom 8× · Standard | Start/Prolog |
| Kodex-Linse II | LENS | 2 | Zoom 8× · Makrolinse | Händler (Akkord 2) · Crafting |
| Kodex-Linse III | LENS | 3 | Zoom 10× · Nachtlinse | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Kodex-Linse IV | LENS | 4 | Zoom 12× · Teleobjektiv | Crafting (Akt II) · Fraktion Ruf 4 |
| Kodex-Linse V | LENS | 5 | Zoom 12× · Spiegellinse (Meisterschaft) | Crafting (Endgame) · Fraktion Ruf 6 |
| Wärterwerkzeug I | TOOL | 1 | Klinge/Hacke/Sichel Stufe I · Ertrag +0 % | Start/Prolog |
| Wärterwerkzeug II | TOOL | 2 | Klinge/Hacke/Sichel Stufe II · Ertrag +10 % | Händler (Akkord 2) · Crafting |
| Wärterwerkzeug III | TOOL | 3 | Klinge/Hacke/Sichel Stufe III · Ertrag +20 % | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Wärterwerkzeug IV | TOOL | 4 | Klinge/Hacke/Sichel Stufe IV · Ertrag +30 % | Crafting (Akt II) · Fraktion Ruf 4 |
| Wärterwerkzeug V | TOOL | 5 | Klinge/Hacke/Sichel Stufe V · Ertrag +40 % | Crafting (Endgame) · Fraktion Ruf 6 |
| Laterne I | LANTERN | 1 | Leuchtradius 8 m · Dunkel-Tor ab Stufe III | Start/Prolog |
| Laterne II | LANTERN | 2 | Leuchtradius 12 m · Dunkel-Tor ab Stufe III | Händler (Akkord 2) · Crafting |
| Laterne III | LANTERN | 3 | Leuchtradius 16 m · Dunkel-Tor ab Stufe III | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Laterne IV | LANTERN | 4 | Leuchtradius 20 m · Dunkel-Tor ab Stufe III | Crafting (Akt II) · Fraktion Ruf 4 |
| Laterne V | LANTERN | 5 | Leuchtradius 25 m · Dunkel-Tor ab Stufe III | Crafting (Endgame) · Fraktion Ruf 6 |
| Atemmaske I | MASK | 1 | Tauchzeit 20 s · Tauchtiefe 5 m | Start/Prolog |
| Atemmaske II | MASK | 2 | Tauchzeit 40 s · Tauchtiefe 10 m | Händler (Akkord 2) · Crafting |
| Atemmaske III | MASK | 3 | Tauchzeit 60 s · Tauchtiefe 20 m | Crafting (Akt I-Materialien) · Fraktion Ruf 2 |
| Atemmaske IV | MASK | 4 | Tauchzeit 90 s · Tauchtiefe 30 m | Crafting (Akt II) · Fraktion Ruf 4 |
| Atemmaske V | MASK | 5 | Tauchzeit 120 s · Tauchtiefe 40 m | Crafting (Endgame) · Fraktion Ruf 6 |
| Bodensattel | SADDLE | 1 | Schaltet die Reitart frei (mit Traversal-Freischaltung CANON §15) | Story/Wildwacht |
| Klettersattel | SADDLE | 1 | Schaltet die Reitart frei (mit Traversal-Freischaltung CANON §15) | Story/Wildwacht |
| Schwimmsattel | SADDLE | 1 | Schaltet die Reitart frei (mit Traversal-Freischaltung CANON §15) | Story/Wildwacht |
| Grabsattel | SADDLE | 1 | Schaltet die Reitart frei (mit Traversal-Freischaltung CANON §15) | Story/Wildwacht |
| Flugsattel | SADDLE | 1 | Schaltet die Reitart frei (mit Traversal-Freischaltung CANON §15) | Story/Wildwacht |

| Regel | Wert |
|---|---|
| Erwerb | Stufe I zum Start; II über Händler/Crafting; III–V über Crafting mit Regionsmaterialien und Fraktionsruf (K41, K47) |
| Aufwertung | Stufe n → n+1 behält Verzierungen (Kosmetik) |
| Kosmetik | Aussehen frei wählbar (Transmog), unabhängig von der Stufe; nie verkauft gegen Echtgeld |
| Sättel | Fünf Sättel schalten Reitarten frei (Story-gebunden, CANON §15) |

---

## 4. Reiten

### 4.1 Reitarten

| DisplayName | SpeedM | SpeedL | SpeedXL | SpeedXXL | StaminaDrain | Unlock | Notes |
|---|---|---|---|---|---|---|---|
| Bodenreiten | – | 14 | 15 | 13 | Galopp −6 AE/s | Nach Akkord 1 | Sprung 2,5 m; schwimmt nicht |
| Kletterreiten | – | 9 | 8 | – | −5 AE/s an Wänden | Akt I (Kharsgrat-Quest) | Wände bis 70°; auch an glatten Flächen außer Eis |
| Schwimmreiten | 10 | 12 | 13 | 12 | −3 AE/s; Tauchen −6 AE/s | Akt I (Morvenmoor/Saltrand) | Tauchen bis 30 m mit Atemmaske |
| Grabreiten | – | 10 | 11 | 12 | −6 AE/s unter der Oberfläche | Akt II (Sahrun-Weite) | Durch Sand/Erde/Kristallsand; Sandsturm-sicher |
| Flugreiten | – | 20 | 22 | 18 | −4 AE/s Steigflug, 0 Gleiten | Akt II nach 6 Akkorden | Flughöhe max. 400 m über Gelände; Gewitter: Blitzlandung (CANON §62) |

| Regel | Wert |
|---|---|
| Voraussetzung | Art mit `Mount`-Eigenschaft (K16 CD-17: Größe ≥ L, Schwimmen ≥ M), Sattel der Reitart, Echo im Chor, Bindungsstufe ≥ 1 |
| Aufsteigen | Begleiter-Rad oder Rufen (Taste halten): Echo erscheint in ≤ 2 s aus dem Chor (aus der Ferne laufend/fliegend, nicht teleportiert, außer in Innenräumen) |
| Ausdauer | Reittier-Ausdauer = 100 + 10 je Bindungsstufe ≥ 4 (K37); getrennt von der Wärter-Ausdauer |
| Wechsel im Flug | Absteigen in der Luft → Gleiter; Aufsteigen auf ein Flugreittier aus dem Gleiten möglich (Fangmanöver) |
| Kampf | Reiten endet beim Kampfbeginn; das Reittier kämpft als normales Chor-Echo |
| Begleiter | das Reittier ist zugleich Begleiter (Initiative bleibt aktiv) |
| Koop | Mitspieler können auf XL/XXL-Reittieren mitreiten (Sozialfunktion, kein Tempo-Vorteil) |

### 4.2 Alle Reittiere

| # | Art | Region | Reitart | Größe | Tempo (m/s) | Freischaltung |
|---|---|---|---|---|---|---|
| 003 | Verdrath | Verdanthain | Bodenreiten | L | 14 | Nach Akkord 1 |
| 006 | Torgrath | Verdanthain | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 009 | Zephyrion | Verdanthain | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 012 | Cantaroth | Verdanthain | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 015 | Myrthorn | Verdanthain | Bodenreiten | L | 14 | Nach Akkord 1 |
| 016 | Vernaune | Verdanthain | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 017 | Glyphaune | Verdanthain | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 034 | Cragar | Kharsgrat | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 035 | Kraggoth | Kharsgrat | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 036 | Anchrex | Kharsgrat | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 042 | Forgoth | Kharsgrat | Bodenreiten | L | 14 | Nach Akkord 1 |
| 045 | Gratrex | Kharsgrat | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 049 | Lithshell | Kharsgrat | Bodenreiten | L | 14 | Nach Akkord 1 |
| 063 | Undfin | Morvenmoor | Schwimmreiten | M | 10 | Akt I (Morvenmoor/Saltrand) |
| 064 | Undrath | Morvenmoor | Schwimmreiten | L | 12 | Akt I (Morvenmoor/Saltrand) |
| 077 | Brinshell | Morvenmoor | Bodenreiten | L | 14 | Nach Akkord 1 |
| 082 | Morhaw | Morvenmoor | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 086 | Marwyn | Saltrand | Schwimmreiten | M | 10 | Akt I (Morvenmoor/Saltrand) |
| 087 | Maraune | Saltrand | Flugreiten | XL | 22 | Akt II nach 6 Akkorden |
| 089 | Tidel | Saltrand | Schwimmreiten | M | 10 | Akt I (Morvenmoor/Saltrand) |
| 090 | Tidrex | Saltrand | Schwimmreiten | L | 12 | Akt I (Morvenmoor/Saltrand) |
| 093 | Brision | Saltrand | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 096 | Aquadral | Saltrand | Schwimmreiten | L | 12 | Akt I (Morvenmoor/Saltrand) |
| 101 | Stonshell | Saltrand | Bodenreiten | L | 14 | Nach Akkord 1 |
| 105 | Ariuna | Saltrand | Schwimmreiten | XL | 13 | Akt I (Morvenmoor/Saltrand) |
| 115 | Dunhorn | Sahrun-Weite | Bodenreiten | L | 14 | Nach Akkord 1 |
| 116 | Dunmarsch | Sahrun-Weite | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 121 | Sengar | Sahrun-Weite | Grabreiten | L | 10 | Akt II (Sahrun-Weite) |
| 122 | Sengrath | Sahrun-Weite | Grabreiten | XXL | 12 | Akt II (Sahrun-Weite) |
| 132 | Mesakor | Sahrun-Weite | Bodenreiten | L | 14 | Nach Akkord 1 |
| 146 | Obsidrax | Ignareth | Bodenreiten | L | 14 | Nach Akkord 1 |
| 148 | Ignavor | Ignareth | Flugreiten | XL | 22 | Akt II nach 6 Akkorden |
| 154 | Voltarn | Ignareth | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 161 | Kjalmur | Hvitfell | Bodenreiten | L | 14 | Nach Akkord 1 |
| 162 | Kjalgrund | Hvitfell | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 165 | Uvalis | Hvitfell | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 168 | Lysmara | Hvitfell | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 169 | Lysthane | Hvitfell | Flugreiten | XL | 22 | Akt II nach 6 Akkorden |
| 175 | Hallbrand | Hvitfell | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 189 | Sarkon | Ael'Dorun | Bodenreiten | L | 14 | Nach Akkord 1 |
| 190 | Sarkothar | Ael'Dorun | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 201 | Klirrathan | Prismtiefen | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 204 | Spatwurm | Prismtiefen | Grabreiten | L | 10 | Akt II (Sahrun-Weite) |
| 205 | Spathorn | Prismtiefen | Grabreiten | XL | 11 | Akt II (Sahrun-Weite) |
| 208 | Ligravor | Prismtiefen | Kletterreiten | L | 9 | Akt I (Kharsgrat-Quest) |
| 220 | Nimbor | Nimbara | Flugreiten | XL | 22 | Akt II nach 6 Akkorden |
| 221 | Nimbaroth | Nimbara | Flugreiten | XXL | 18 | Akt II nach 6 Akkorden |
| 224 | Cirrhaven | Nimbara | Flugreiten | L | 20 | Akt II nach 6 Akkorden |
| 234 | Holmgard | Nimbara | Bodenreiten | XL | 15 | Nach Akkord 1 |
| 239 | Lumaskiff | Nimbara | Flugreiten | XL | 22 | Akt II nach 6 Akkorden |

**50 Reittiere** im Grundkatalog.

Jede Region liefert mindestens ein Reittier, die Reitarten sind über die Regionen so verteilt, dass jede Freischaltung mit Echos der Region, in der sie erfolgt, sofort nutzbar ist (Kharsgrat: Klettern mit Cragar/Hallbrand-Vorgänger, Saltrand/Morvenmoor: Schwimmen, Sahrun-Weite: Graben mit Sengar).

### 4.3 Reit-Steuerung

| Eingabe | Boden | Klettern | Schwimmen | Graben | Flug |
|---|---|---|---|---|---|
| Linker Stick | Richtung | Richtung an der Wand | Richtung | Richtung unter der Oberfläche | Richtung/Neigung |
| A/✕ | Sprung | Sprungklettern | Auftauchen | Auftauchen | Steigen |
| B/◯ | Absteigen | Loslassen | Tauchen | Abtauchen | Sinken / Landen |
| R2/RT | Galopp | Schneller klettern | Schnell schwimmen | Schnell graben | Sturzflug |

---

## 5. Pfad-Tore

Die zwölf Pfad-Tore aus K30 §7 werden hier mit ihren Lösungen festgeschrieben (PT-1: ≥ 2 Lösungen, ≥ 1 typunabhängig):

| DisplayName | FieldAbilities | Alternative | RegionFocus |
|---|---|---|---|
| Eis/Dorn | Glutschmelze|Giftschneise | Werkzeug Klinge III | R07|R01|R03 |
| Geröll | Felsbrecher|Schwebelast | Werkzeug Hacke III | R02|R05 |
| Spalt | Rankenbrücke|Eisbrücke | Gleiter / Kletterreiten | R01|R08 |
| Wasser | Wasserlauf|Eisbrücke | Schwimmreiten | R03|R06 |
| Gestrüpp | Giftschneise|Glutschmelze | Werkzeug Sichel II | R03|R01 |
| Dunkel | Fackelschein|Leuchtfeuer | Laterne (Ausrüstung) | R09|R05 |
| Mechanik | Mechanik|Schwebelast | Kontor-Schlüssel (Ruf 3) | R08|R10 |
| Ahnen | Seelenpfad|Geistersicht | Kodex-Hinweis (Skill Forschung) | R07|R08 |
| Prisma | Lichtlenker|Leuchtfeuer | Spiegelscherben-Rätsel (längerer Weg) | R09|R04 |
| Glyphe | Glyphenlesen | Kodex-Hinweis (Skill Forschung) / Akademie-Schlüssel | R08|R04 |
| Siegel | Siegelöffner | Fraktions-Schlüssel (K47) | alle |
| Last | Schwebelast|Felsbrecher | Gegengewicht-Rätsel (Umweg) | R10|R02 |

**Platzierungsregeln (Level Design):**
- **PT-2:** Kein Pfad-Tor auf dem Hauptpfad (Prüfung über die Pfadlinien der Zonen im Editor-Validator `PathGateAudit`).
- **PT-3:** Pro Region ≥ 6 Tor-Typen; pro Zone ≤ 8 Tore (Dichte).
- **PT-4:** Hinter jedem Tor wartet etwas, das zählt: Klangfragment, Kiste der Stufe ≥ 2, Kodex-Gelegenheit, Abkürzung (≥ 30 % Weg) oder Aussichtspunkt.
- **PT-5:** Tore zeigen ihre Lösungen im Resonanzsinn als Symbole (Feldfähigkeiten-Symbol + Werkzeug-Symbol), sobald der Spieler eine Lösung grundsätzlich kennt.

---

## 6. Halteitems der Echos

Jedes Echo kann ein **Halteitem** tragen (`HeldItem`, CANON §29). Halteitems sind kleine Spezialisierungen; Kampf-Halteitems sind auf ×1,1–1,15 gedeckelt.

| DisplayName | Effects | Description |
|---|---|---|
| Stimmstein (Glut) | TypePower(Ember,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Flut) | TypePower(Tide,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Stein) | TypePower(Stone,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Sturm) | TypePower(Storm,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Blüte) | TypePower(Bloom,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Frost) | TypePower(Frost,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Leere) | TypePower(Void,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Licht) | TypePower(Light,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Gift) | TypePower(Venom,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Metall) | TypePower(Metal,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Geist) | TypePower(Spirit,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Kristall) | TypePower(Crystal,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Klang) | TypePower(Sound,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Schwerkraft) | TypePower(Gravity,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Stimmstein (Arkan) | TypePower(Arcane,1100) | Halteitem: {d}-Fähigkeiten ×1,1 |
| Taktring | TimeCost(-5) | Zeitkosten aller Aktiven −5 |
| Schildbrosche | Shield(Self,10) | Schild 10 % beim Einwechseln |
| Fokuslinse | Crit(1) | Volltrefferstufe +1 |
| Atemband | Heal(Self,15) | Bei HP ≤ 33 %: heilt 15 % (einmal) |
| Spiegelschuppe | Reflect(Special) | Reflektiert den ersten speziellen Angriff (einmal) |
| Wurzelamulett | Immune(Rueckstoss) | Immun gegen Rückstoß; kein Reihenwechsel durch Gegner |
| Nebelschal | Mod(Evasion,1100) | AUS ×1,1 bei Nebel/Nebelfeld |
| Glutkern | StatusChance(1200) | Status-Chancen ×1,2 (nur Brand) |
| Reinheitsglocke | Cleanse(Self) | Entfernt den ersten Haupt-Status (einmal) |
| Sturmfeder | Haste(Self,30) | Beim Einwechseln 30 Ticks Vorlauf |
| Schwerstein | Mod(Defense,1150);Mod(Speed,900) | VER ×1,15, GES ×0,9 |
| Harmoniespiel | Harmony(10) | Seite +10 Harmonie beim Einwechseln (einmal je Kampf) |
| Bindungsband | – | Bindungszuwachs +25 % (außerhalb des Kampfes; Ranked ohne Wirkung) |
| Lernamulett | – | EP +20 % für den Träger (Ranked ohne Wirkung) |
| Schliffstein | – | Schliff-Ertrag +1 je Kampf (Ranked ohne Wirkung) |
| Wesensband | – | Zucht: Persönlichkeit sicher vererben (K38) |
| Stimmband | – | Zucht: Temperament sicher vererben (K38) |

| Regel | Wert |
|---|---|
| Anzahl | 1 je Echo |
| Ranked | keine Duplikate je Team; Komfort-Items (Bindung, EP, Schliff) ohne Wirkung (K61) |
| Erwerb | Crafting (K41), Kampf-Beute, Händler (Stimmsteine ab Akkord 3), Fraktionsruf |
| Verbrauch | „einmal“-Effekte erneuern sich nach jedem Kampf (kein Verbrauch – kein Item-Grind) |

---

## 7. Reisezeiten und Weltgröße

Aus `aethris_traversal.travel_table()` (Distanzen aus K08: Welt ≈ 36 km², 10 Regionen, ~50 Zonen):

| Strecke | Joggen | Sprint (mit Pausen, Ø) | Bodenreiten (L) | Grabreiten (XL) | Schwimmreiten (L) | Flugreiten (L) | Gleiter V (von 300 m Höhe) |
|---|---|---|---|---|---|---|---|
| POI-Abstand (Ø 200 m) | 48 s | 36 s | 14 s | 18 s | 17 s | 10 s | 17 s |
| Zone durchqueren (Ø 1,2 km) | 4,8 min | 3,6 min | 86 s | 109 s | 100 s | 60 s | 100 s |
| Region durchqueren (Ø 3,5 km) | 13,9 min | 10,4 min | 4,2 min | 5,3 min | 4,9 min | 2,9 min | 4,9 min |
| Weltdiagonale (≈ 8,5 km) | 33,7 min | 25,3 min | 10,1 min | 12,9 min | 11,8 min | 7,1 min | 11,8 min |

**Bewertung:** Eine Region ist zu Pferd in ~4 Minuten, zu Fuß in ~14 Minuten durchquerbar. Mit 80 Resonanzsteinen (CANON §4) liegt der nächste Schnellreisepunkt nie weiter als ~600 m entfernt. Die Neugier-Dichte (POI alle 150–250 m, DR-26) bedeutet: Zu Pferd begegnet dem Spieler alle 10–15 s ein Angebot – deshalb verlangsamt das Reittier automatisch (×0,7) in der Nähe unentdeckter POIs, damit sie nicht übersehen werden (Option abschaltbar).

---

## 8. Wetter und Traversal

| Wetter | Wirkung (CANON §62 präzisiert) |
|---|---|
| Regen | Klettern an Fels verboten (nasser Fels), Ausdauer-Regeneration 20/s; Wettermantel II hebt den Regenmalus auf |
| Gewitter | wie Regen; Flugreiten: Blitzschlag erzwingt Landung ohne Schaden (alle 3–5 min, angekündigt durch Donnerzählung) |
| Nebel | Resonanzsinn-Reichweite +50 %; Sicht 60 m; Reittiere verlangsamen auf 80 % |
| Schnee | Spuren sichtbar (Kodex-Beobachtung leichter); Bodenreiten −10 % (außer Frost-Reittiere) |
| Hitzewelle | Ausdauer-Regeneration −20 % ohne Wettermantel III (außer Glut/Licht-Begleiter) |
| Sandsturm | kein Klettern/Gleiten; Reiten −30 % (Grabreiten unbeeinflusst); Sicht 40 m |
| Aurora | Gleiter-Auftrieb +20 % (Nimbara-Sage) |
| Resonanzsturm | Echos aggressiver (K52); Reittiere scheuen nicht – Bindungsstufe ≥ 3 nötig, sonst Absteigen |

---

## 9. Kamera und Steuerung

| Aspekt | Vorgabe |
|---|---|
| Kamera | Third-Person, Distanz 3,5 m (Fuß), 6–12 m (Reiten nach Größe), automatische Anhebung beim Klettern |
| Barrierefreiheit | Automatisches Klettern (Halten statt Tasten), Gleiter-Autostabilisierung, Bewegungsunschärfe aus, Kamera-Wackeln aus |
| Leistung | Reiten mit 22 m/s erfordert World-Partition-Streaming-Radius 512 m (Fly) bzw. 256 m (Boden); K65 Budget |

---

## 10. Code

```cpp
// GF_Traversal – Ausdauer und Bewegungsmodi
UENUM() enum class ETraversalMode : uint8 { Walk, Jog, Sprint, Climb, Swim, Glide, Ride };

void UWardenStaminaComponent::Tick(float Dt, ETraversalMode Mode, const FTraversalTuning& T)
{
    const float Drain = Mode == ETraversalMode::Sprint ? T.SprintDrain
                      : Mode == ETraversalMode::Climb  ? T.ClimbDrain
                      : Mode == ETraversalMode::Swim   ? T.SwimDrain
                      : Mode == ETraversalMode::Glide  ? T.GliderDrain(GearTier(EGearSlot::Glider)) : 0.f;
    if (Drain > 0.f) { Stamina = FMath::Max(0.f, Stamina - Drain * Dt); IdleTime = 0.f; }
    else if ((IdleTime += Dt) >= 1.f) { Stamina = FMath::Min(MaxStamina(), Stamina + T.RegenFor(World->Weather()) * Dt); }
    if (Stamina <= 0.f) OnExhausted(Mode);   // rutschen / treiben / einklappen – nie Tod
}

bool UMountService::CanMount(const FEchoInstance& Echo) const
{
    const UEchoSpeciesDefinition& Sp = Species(Echo);
    return Sp.MountKind.IsValid() && Unlocks->HasSaddle(Sp.MountKind) && Echo.Bond.BondTierReached >= 1;
}
```

Charakterbewegung nutzt `UCharacterMovementComponent` mit eigenen Custom-Modes (Climb, Glide, Swim-Surface); Reittiere sind eigenständige Pawns (Mover 2.0 in UE 5.6 für deterministische Netz-Prädiktion im Koop, K59).

---

## 11. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Traversal.Stamina` | Verbrauch/Regeneration je Modus und Wetter |
| `…Traversal.FallRescue` | Fall > 30 m → Fangnetz, kein Schaden |
| `Aethris.Func.Traversal.PathGateAudit` | kein Tor auf Hauptpfad, ≥ 2 Lösungen, ≥ 6 Typen je Region |
| `…Mount.Unlock` | Reitarten nur mit Sattel + Story-Freischaltung |
| `…Mount.Streaming` | Flug 22 m/s ohne Streaming-Hänger (K65) |

**Telemetrie:** Anteil Reisezeit je Modus, Schnellreisequote, Pfad-Tore geöffnet je Spielstunde, Absturz-Fangnetz-Auslösungen (Ziel < 1/Stunde).

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-147 | Kein Fallschaden; Resonanz-Fangnetz ab 30 m | Kein Strafen für Erkundung (DR-23), diegetisch | Fallschaden mit Tod |
| ADR-148 | Ausrüstung ohne Kampfwerte; Bindung nur über Fenster | Kampfbalance von Ausrüstung entkoppelt; DR-01 | Ausrüstung mit Kampfboni |
| ADR-149 | Reitarten an Echos + Sattel + Story-Freischaltung | Sammeln = Mobilität; Pacing (CANON §15) | Generische Reittiere |
| ADR-150 | Halteitems ohne Verbrauch, Kampf-Boni ≤ ×1,15 | Kein Item-Grind; Balance | Verbrauchbare Kampf-Items |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §151 | Bewegung (`TraversalTuning.csv`): 1,8/4,2/7,0 m/s, Ausdauer 100 (max. 160), Sprint −12, Regeneration +25 nach 1 s, Klettern 1,6 m/s −8, Schwimmen 1,5 m/s −4, Gleiter I 1,8/9,0/−6 → V 1,2/12/−2; kein Fallschaden, Fangnetz ab 30 m | LOCKED – **Q11 gelöst** |
| §152 | 9 Ausrüstungsplätze × 5 Stufen + 5 Sättel (`WardenGear.csv`); keine Kampfwerte; Resonator: Fenster ×1,00–1,12, Resonanzsinn 60–120 m | LOCKED |
| §153 | 5 Reitarten (`MountKinds.csv`), Tempo nach Größe (Boden 14/15/13, Klettern 9/8, Schwimmen 10/12/13/12, Graben 10/11/12, Flug 20/22/18 m/s); Voraussetzungen Mount-Art, Sattel, Chor, Bindung ≥ 1; Reit-Ausdauer 100 (+10 ab Stufe 4); 50 Reittiere | LOCKED |
| §154 | 12 Pfad-Tore final (`PathGates.csv`), Regeln PT-1 bis PT-5 | LOCKED |
| §155 | 32 Halteitems (`HeldItems.csv`), 1 je Echo, kein Verbrauch, Kampf-Boni ≤ ×1,15, Ranked keine Duplikate | LOCKED |
| §10 | ADR-147 – ADR-150 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Bewegung und Ausdauer final (Q11), kein Fallschaden
- [x] 9 Ausrüstungsplätze × 5 Stufen + Sättel als Daten
- [x] 5 Reitarten, Regeln, Steuerung, alle 50 Reittiere
- [x] 12 Pfad-Tore mit Lösungen und Platzierungsregeln
- [x] 32 Halteitems als Daten
- [x] Reisezeiten, Wetter-Traversal, Kamera, Code, Tests
- [x] ADR-147 – ADR-150, CANON §151–§155

➡️ **Nächstes Kapitel: K41 – Crafting, Ressourcen und Rezepte.**
