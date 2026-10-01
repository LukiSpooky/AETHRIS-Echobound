# K14 · Wettersystem

| Feld | Wert |
|---|---|
| Dokument | Kapitel 14 von 68 |
| Version | 1.0 |
| Owner | Technical Artist (Weather Lead) + Gameplay Programmer (Weather Systems) |
| Mitwirkende | Combat Designer (Typ-Resonanz), AI Engineer (Spawns, NPC-Reaktionen), Audio Director, Network Engineer, Level Designer |
| Baut auf | CANON §4.4 (10 Wetterzustände), §29 (Seed-Hierarchie), §44–§45 (Belastung, Regionsgewichte), §50 (Aufwinde), K08 (Zonen) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/World/WeatherDefinitions.csv`, `WeatherSelectionWeights.csv` (kalibriert), `WeatherTypeResonance.csv`, `WeatherSpawnModifiers.csv`, `ZoneWeatherRemap.csv`, `tools/sim_weather.py` |
| Neue Kanon-Einträge | CANON §61 (Wetterzustände & Planer), §62 (Wetterwirkungen), §63 (Resonanzsturm), §64 (Tagesphasen-Grenzen) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Die zehn Wetterzustände](#2-die-zehn-wetterzustände)
3. [Tagesphasen-Grenzen (Vorgabe für K15)](#3-tagesphasen-grenzen-vorgabe-für-k15)
4. [Der Wetterplaner](#4-der-wetterplaner)
5. [Mikroklima & Zonen](#5-mikroklima--zonen)
6. [Wirkung auf den Kampf: Typ-Resonanz](#6-wirkung-auf-den-kampf-typ-resonanz)
7. [Wirkung auf Spawns](#7-wirkung-auf-spawns)
8. [Wirkung auf NPCs](#8-wirkung-auf-npcs)
9. [Wirkung auf Traversal & Erkundung](#9-wirkung-auf-traversal--erkundung)
10. [Resonanzsturm (W10)](#10-resonanzsturm-w10)
11. [Wettervorhersage](#11-wettervorhersage)
12. [Präsentation: Visuell & Audio](#12-präsentation-visuell--audio)
13. [Technik & Code](#13-technik--code)
14. [Performance-Budgets](#14-performance-budgets)
15. [Decision Records](#15-decision-records)
16. [Kanon-Updates](#16-kanon-updates)
17. [Kapitel-Checkliste](#17-kapitel-checkliste)

---

## 1. Ziele

Das Briefing verlangt: „Wetter beeinflusst Spawn, Fähigkeiten, Schaden, NPCs.“ Darüber hinaus gilt DR-13 (jedes Weltsystem beeinflusst ≥ 2 andere). Wetter in AETHRIS wirkt auf **sieben** Systeme:

```
                          ┌──────────────┐
           ┌──────────────│    WETTER    │───────────────┐
           │              └──────┬───────┘               │
           ▼                     ▼                       ▼
     SPAWNS (K52)          KAMPF (K32)              NPCs (K53)
     Typ-Gewichte,         Typ-Resonanz,            Unterstände,
     seltene Arten         Sonderregeln             Händler, Feste
           │                     │                       │
           ▼                     ▼                       ▼
     EVOLUTION (K19)       TRAVERSAL (K40)          BELASTUNG (K09)
     Wetterauslöser        Klettern, Gleiten,       Hitze, Kälte,
                           Sicht                    Dunst, Asche
                                 │
                                 ▼
                          AUDIO/MUSIK (K55)
```

**Qualitätsziele:**
- **Glaubwürdig:** Wetter folgt Regionsklima (CANON §45) und Mikroklima (Zonen), Übergänge sind sichtbar und hörbar (Wolken ziehen auf, bevor es regnet).
- **Planbar:** Spieler können Wetter verstehen und nutzen (Vorhersage, Zeit vorspulen) – DR-15 (Seltenheit = erlernbare Bedingungen).
- **Deterministisch & synchron:** In Koop sehen alle dasselbe Wetter, ohne dass Wetter repliziert werden muss (§4.4).
- **Fair:** Wetter verändert Kampfwerte moderat (±10–30 %) und ist auf der Zeitleiste/HUD immer sichtbar (DR-06).

---

## 2. Die zehn Wetterzustände

Daten: `Data/World/WeatherDefinitions.csv`.

| ID | Tag | Dauer (Spielstunden) | Startfenster | Sicht | Wind | Nasser Fels | Belastung | Charakter |
|---|---|---|---|---|---|---|---|---|
| W01 | `Weather.Clear` | 4–10 | jederzeit | unbegrenzt | 1 m/s | – | – | Grundzustand |
| W02 | `Weather.Rain` | 2–6 | jederzeit | 350 m | 3 m/s | ✔ | – | Pfützen, Nässe-Shader, Bachpegel +10 cm |
| W03 | `Weather.Thunderstorm` | 1–3 | jederzeit | 250 m | 8 m/s | ✔ | – | Blitze, Böen, Aufwind +50 % (CANON §50) |
| W04 | `Weather.Fog` | 2–5 | jederzeit (Präferenz Morgen/Nacht) | 60 m | 0 | – | Dunst schwach | Geisterstimmung |
| W05 | `Weather.Snow` | 3–8 | jederzeit | 120 m | 4 m/s | ✔ (vereist) | Kälte mittel | Spuren im Schnee |
| W06 | `Weather.Heatwave` | 4–8 | nur Tag | unbegrenzt (Flimmern) | 1 m/s | – | Hitze stark | Siesta |
| W07 | `Weather.Sandstorm` | 1–3 | jederzeit | 40 m | 12 m/s | – | Hitze mittel | Navigation per Resonanzsinn |
| W08 | `Weather.Aurora` | 2–4 | nur Nacht | unbegrenzt | 1 m/s | – | – | Licht-/Klang-Echos, Fotografie |
| W09 | `Weather.Ashfall` | 2–6 | jederzeit | 80 m | 2 m/s | – | Asche mittel | Grauer „Schnee“, Spuren |
| W10 | `Weather.ResonanceStorm` | 1–2 | jederzeit | 200 m | 6 m/s | – | – | Global, Story/Endgame (§10) |

---

## 3. Tagesphasen-Grenzen (Vorgabe für K15)

Da Wetterstartfenster und die Simulation (§4.3) Tagesphasen brauchen, werden die Grenzen hier festgelegt (löst CANON-Q9); K15 baut das Lichtsystem darauf auf.

| Phase | Tag | Spielstunden (Standard) | Hvitfell (Nacht +2 h) | Nimbara (Tag +2 h) |
|---|---|---|---|---|
| Morgendämmerung | `TimeOfDay.Dawn` | 05:00–07:00 | 06:00–08:00 | 04:00–06:00 |
| Tag | `TimeOfDay.Day` | 07:00–19:00 | 08:00–18:00 | 06:00–20:00 |
| Abenddämmerung | `TimeOfDay.Dusk` | 19:00–21:00 | 18:00–20:00 | 20:00–22:00 |
| Nacht | `TimeOfDay.Night` | 21:00–05:00 | 20:00–06:00 | 22:00–04:00 |

1 Spielstunde = 3 Echtzeitminuten (CANON §4.3) → Tag = 36 min, Nacht = 24 min, Dämmerungen je 6 min (Standardregion).

---

## 4. Der Wetterplaner

### 4.1 Prinzip: Wetter als Funktion von (Weltseed, Region, Spielzeit)

Wetter wird **nicht** ständig zufällig gewürfelt und repliziert, sondern als **Fahrplan** pro Region aus dem Wetter-Strom des Weltseeds (CANON §29: Fork(1)) berechnet. Der Fahrplan ist eine Folge von Blöcken `(Startzeit, Wetter, Dauer)`.

```
 Weltseed ──Fork(1)──► Wetter-Strom ──Fork(RegionHash)──► Region-RNG
                                                            │
  Spielzeit t ──► Block, der t enthält  ◄── Fahrplan wird blockweise fortgeschrieben
                                            (Seed eines Blocks = Hash(Region-RNG, Blockindex))
```

**Folgen:**
- **Koop-Synchronität ohne Replikation:** Host und Gäste kennen Weltseed (beim Beitritt übertragen) und Spielzeit (repliziert) → identisches Wetter.
- **Zeit vorspulen** (K03 §3) springt auf eine spätere Zeit im Fahrplan → „neues Wetter“, aber deterministisch; Save-Scumming durch Laden erzeugt **kein** anderes Wetter (bewusst: DR-15 verlangt erlernbare Bedingungen, nicht Glück).
- **Vorhersage** ist trivial korrekt: zukünftige Blöcke sind bereits definiert (§11).

### 4.2 Auswahlregel eines neuen Blocks

```
 Kandidaten = { w | Auswahlgewicht(Region, w) > 0  ∧  Startfenster(w) passt zur Startstunde
                    ∧  w ≠ aktuelles Wetter }               (Wiederholung nur, wenn keine Alternative)
 P(w) ∝ Auswahlgewicht(Region, w) / mittlere Dauer(w) × Fensterkorrektur(w)
        Fensterkorrektur = 24 / Länge des Startfensters (Nacht: 24/8, Tag: 24/12, sonst 1)
 Dauer  = gleichverteilt ganzzahlig in [MinHours, MaxHours]
 Übergang = 10–20 Spielminuten Überblendung (Wolken/Licht/Partikel/Audio), Gameplay-Wirkung ab Mitte der Überblendung
```

### 4.3 Kalibrierung (warum die Gewichte in einer eigenen Datei stehen)

Die **Zielanteile** je Region (CANON §45, `RegionWeather.csv`) beschreiben, wie viel *Zeit* ein Wetter einnimmt. Wegen Dauerunterschieden, Startfenstern und der Nicht-Wiederholungsregel ergeben die Zielanteile als Auswahlgewichte verzerrte Zeitanteile (erste Simulation: bis 8 Prozentpunkte Abweichung, z. B. Hvitfell Klar 38 % statt 30 %).

`tools/sim_weather.py` **kalibriert** deshalb die Auswahlgewichte iterativ (multiplikative Korrektur, 40 Runden à 2.500 simulierte Tage) und validiert mit einem **anderen Seed** über 6.000 Tage. Ergebnis (Auszug):

| Region | Ziel → erreicht (Zeitanteil %) | Max. Abweichung |
|---|---|---|
| R01 | Klar 50→50 · Regen 30→30 · Gewitter 5→5 · Nebel 15→15 | 0.3 pp |
| R02 | Klar 45→45 · Regen 10→11 · Gewitter 20→20 · Nebel 10→10 · Schnee 15→15 | 0.5 pp |
| R03 | Klar 25→25 · Regen 35→35 · Gewitter 5→5 · Nebel 35→35 | 0.1 pp |
| R04 | Klar 55→55 · Hitzewelle 25→25 · Sandsturm 20→20 | 0.4 pp |
| R05 | Klar 35→35 · Gewitter 5→5 · Hitzewelle 25→25 · Asche 35→35 | 0.2 pp |
| R06 | Klar 45→45 · Regen 25→25 · Gewitter 15→15 · Nebel 15→15 | 0.4 pp |
| R07 | Klar 30→32 · Nebel 10→9 · Schnee 45→46 · Aurora 15→13 | 1.8 pp |
| R08 | Klar 50→50 · Regen 15→15 · Gewitter 5→5 · Nebel 30→30 | 0.3 pp |
| R09 | Klar 100→100 | 0.0 pp |
| R10 | Klar 45→45 · Regen 10→10 · Gewitter 20→20 · Nebel 10→10 · Aurora 15→15 | 0.3 pp |

Akzeptanzkriterium: ≤ 3 pp je Wetter und Region – **erfüllt**. Die kalibrierten Gewichte stehen in `Data/World/WeatherSelectionWeights.csv` (generiert, nicht von Hand ändern; Pre-Submit führt das Tool aus, wenn `RegionWeather.csv` oder `WeatherDefinitions.csv` sich ändern).

### 4.4 Netzwerk & Speichern

| Thema | Regel |
|---|---|
| Koop | Weltseed beim Beitritt an Gäste; Spielzeit vom Host repliziert (1 Hz + Korrektur); Wetter lokal berechnet |
| Resonanzsturm | Globaler Override wird als Ereignis repliziert (Start, Dauer) – nicht aus dem Fahrplan |
| Save | Nur Override-Zustände (aktiver Resonanzsturm, Story-erzwungenes Wetter); Fahrplan ist rekonstruierbar |
| Story-Override | Quests können Wetter für eine Region erzwingen (`ForceWeather(Region, Weather, Duration)`), z. B. Prolog-Regen, Finale-Gewitter |

---

## 5. Mikroklima & Zonen

Daten: `Data/World/ZoneWeatherRemap.csv`.

| Regel | Zonen | Ersetzung | Grund |
|---|---|---|---|
| REMAP_R02_LOWSNOW | R02_Z01–Z03 | Schnee → Regen | Schnee nur in Gipfelzonen (K09 §5.4) |
| REMAP_R02_HIGHRAIN | R02_Z05 | Regen → Schnee | Gipfel: Niederschlag als Schnee |
| REMAP_R07_VALLEYSNOW | R07_Z01 | Schnee → Nebel | Tal mit warmen Quellen |
| REMAP_R09_UNDERGROUND | R09 alle Zonen | alles → Klar (**außer Resonanzsturm**) | Höhlenklima (K10 §5.4) |
| REMAP_R10_CLOUDSEA | R10_Z01 | Regen → Nebel | Windstufen liegen in der Wolkenschicht |

**Übergänge zwischen Regionen:** An Regionsgrenzen werden Wettereffekte über 150 m räumlich überblendet (Wetter-Volumen mit Blend-Radius); Gameplay-Wirkung gilt nach der Region, in der sich der Spieler (bzw. der Kampfkreis-Mittelpunkt) befindet.

---

## 6. Wirkung auf den Kampf: Typ-Resonanz

Daten: `Data/World/WeatherTypeResonance.csv`. Einbindung in die Schadensformel: K32 (Faktor `WeatherFactor` des **angreifenden** Fähigkeitstyps).

| Wetter | Verstärkt (Schaden des Fähigkeitstyps) | Geschwächt | Sonderregel |
|---|---|---|---|
| Klar | – | – | – |
| Regen | Flut ×1,2 · Blüte ×1,1 | Glut ×0,8 | – |
| Gewitter | Sturm ×1,2 · Flut ×1,1 | Glut ×0,9 | **Blitzschlag:** Am Ende jedes 4. Zuges trifft ein Blitz das Echo mit der höchsten Metall-/Sturm-Affinität (Typ Metall oder Sturm, sonst niemand): Metall erhält 6 % Max-HP Schaden, Sturm erhält +10 Harmonie |
| Nebel | Geist ×1,2 · Leere ×1,1 | Licht ×0,9 | **Nebelsicht:** Fernkampf-Fähigkeiten gegen die Hinterreihe −1 Präzisionsstufe |
| Schnee | Frost ×1,2 | Blüte ×0,9 · Glut ×0,9 | **Schneefall:** Nicht-Frost-Echos −5 % Geschwindigkeit (Zeitleiste) |
| Hitzewelle | Glut ×1,2 · Licht ×1,1 | Frost ×0,8 · Flut ×0,9 | – |
| Sandsturm | Stein ×1,2 · Schwerkraft ×1,1 | – | **Sandschliff:** Echos ohne Typ Stein/Metall/Schwerkraft verlieren am Zugende 4 % Max-HP |
| Aurora | Licht ×1,2 · Klang ×1,2 · Arkan ×1,1 | Leere ×0,8 | **Aurora-Harmonie:** +5 Harmonie pro Zug für beide Seiten |
| Aschefall | Leere ×1,2 · Glut ×1,1 | Blüte ×0,8 | **Aschesicht:** −1 Präzisionsstufe für alle außer Glut/Leere |
| Resonanzsturm | **alle ×1,1**, Klang ×1,3 | – | **Resonanzflut:** Harmonie-Gewinn ×2, Crescendo-Kosten −25 % |

**Balancing-Regeln (LOCKED):**
- Maximaler Wetterfaktor 1,3 (nur Klang im Resonanzsturm), minimaler 0,8.
- Kein Wetter macht einen Typ wirkungslos (DR-07/DR-10).
- Wetter ist auf dem Kampf-HUD permanent sichtbar; Sonderregeln erscheinen als Ereignis auf der Zeitleiste (DR-06).
- **PvP Ranked:** Wetter = Klar (neutral), außer in saisonalen Sonderregeln (K61).
- Fähigkeiten können Wetter für N Züge **lokal im Kampf** ändern (Wetter-Fähigkeiten, K28–K30) – das Oberweltwetter bleibt unverändert.

---

## 7. Wirkung auf Spawns

Daten: `Data/World/WeatherSpawnModifiers.csv` (Multiplikatoren je Wetter × Primärtyp, Promille). Die Spawnlogik (K52) multipliziert das Basisgewicht einer Art mit dem Faktor ihres Primärtyps und prüft zusätzlich art-spezifische `SpawnConditions` (DR-15).

**Auszug (Faktor):**

| Wetter | stark erhöht (≥ ×2) | erhöht (×1,3–1,8) | stark gesenkt (≤ ×0,5) |
|---|---|---|---|
| Regen | Flut 2,0 | Blüte 1,5 · Gift 1,5 | Glut 0,3 |
| Gewitter | Sturm 2,5 | Flut 1,3 · Metall 1,3 | Glut 0,5 |
| Nebel | Geist 2,2 | Leere 1,8 · Gift 1,3 · Arkan 1,3 | – |
| Schnee | Frost 2,5 | – | Glut 0,4 · Blüte 0,5 |
| Hitzewelle | Glut 2,0 | Licht 1,5 | Frost 0,3 · Flut 0,5 |
| Sandsturm | Stein 2,0 | Schwerkraft 1,8 · Metall 1,3 | Flut 0,3 · Blüte 0,4 · Frost 0,5 |
| Aurora | Licht 2,5 · Klang 2,0 | Kristall 1,5 · Arkan 1,5 · Frost 1,3 | Leere 0,5 |
| Aschefall | Leere 2,2 | Glut 1,6 · Metall 1,3 | Blüte 0,4 · Flut 0,5 |
| Resonanzsturm | Klang 2,5 | Arkan 1,8 · alle anderen 1,3 | – |

**Ökologische Folgen (Vorgabe K52):** Wechselt das Wetter, werden Spawns nicht sofort ausgetauscht: Vorhandene Echos reagieren (Unterschlupf suchen, aktiver werden), neue Spawns folgen den neuen Gewichten. Ein Gewitter „bringt“ Sturm-Echos von den Graten in die Täler (Wanderbewegung, sichtbar).

---

## 8. Wirkung auf NPCs

| Wetter | Ambient-NPCs (Mass) | Benannte NPCs | Händler | Ereignisse |
|---|---|---|---|---|
| Regen | 60 % gehen in Unterstände/Häuser; Rest mit Regenschutz | Tagesablauf mit Indoor-Alternativen (StateTree-Zweig) | Marktstände **im Freien** schließen | Wetterschaden-Ereignis möglich (K13 §6) |
| Gewitter | 85 % drinnen; Fenster werden geschlossen (Animation) | wie Regen; Wachen bleiben draußen | wie Regen | Blitzeinschlag-Inszenierung an Türmen |
| Nebel | normal, Laternen an | Barks über Geister, Unheimliches | normal | Geisterszenen (Ael'Dorun), Laternennacht wird intensiver |
| Schnee | Schneeschaufeln, Kinder bauen Schneefiguren | Kälte-Animationen | normal | – |
| Hitzewelle | Siesta 11–16 Uhr (Straßen leer) | Schatten-Präferenz | Außenstände schließen 11–16 | – |
| Sandsturm | alle drinnen, Stadttore geschlossen | drinnen | nur Innenhändler | Verirrte Karawane (Quest-Trigger) |
| Aurora | strömen nach draußen, schauen nach oben | Lore-Gespräche | normal | Spontanes Fest (Hvitmark/Aerion) |
| Aschefall | Masken, Kehrbesen | Masken | normal | – |
| Resonanzsturm | Unruhe, Gruppen bilden sich, manche beten (Lauscherglaube), Ordensmitglieder halten Mahnwache | Story-Reaktionen | geöffnet, „Sturmpreise“ +10 % (K42) | – |

Umsetzung: Wetter-Tag wird als **Kontext** an StateTrees übergeben (K53); jede Tagesablauf-Aktivität deklariert Wetter-Alternativen (`IndoorAlternative`).

---

## 9. Wirkung auf Traversal & Erkundung

| Wetter | Klettern | Gleiten | Reiten | Sicht/Erkundung |
|---|---|---|---|---|
| Regen | Nasser Fels nicht kletterbar (markiert durch Glanz-Shader); sonst Ausdauer +25 % Verbrauch | – | Bodenreiten −10 % auf Schlamm | Pfützen spiegeln, Spuren verwischen |
| Gewitter | wie Regen | Aufwind +50 %, Böen; Blitzwarnung 1,5 s → Treffer erzwingt Landung (kein Schaden) | – | Blitze erhellen Nacht kurz |
| Nebel | normal | Sicht 60 m | – | Resonanzsinn-Reichweite **+50 %** (Klang dringt durch Nebel – S2) |
| Schnee | Vereiste Flächen nicht kletterbar | Wind 4 m/s | Schlittenwege +20 % (Hvitmark) | **Spuren** sichtbar (Tracking) |
| Hitzewelle | Ausdauer +20 % Verbrauch (Fels heiß) | Thermik +20 % | – | Hitzeflimmern, Fata-Morgana-Effekte |
| Sandsturm | nicht möglich (Wind) | nicht möglich | Reiten −30 % | Sicht 40 m; Resonanzsinn zeigt Siedlungen/Steine immer |
| Aurora | normal | normal | normal | Kodex-Linse-Bonus (Licht/Pose, K39) |
| Aschefall | normal | Sicht 80 m | – | Spuren in Asche |
| Resonanzsturm | normal | Aufwinde überall | – | Resonanzsinn zeigt **alle** Echos im Radius 300 m |

---

## 10. Resonanzsturm (W10)

Der Resonanzsturm ist kein reguläres Wetter, sondern ein **globales Ereignis**: Das Weltlied schwillt kurz an (CANON §33).

| Aspekt | Regel |
|---|---|
| Auslöser | (1) **Story:** Akt-II-Wende (W6) und Finale (Akt III) erzwingen Resonanzstürme. (2) **Post-Game (offline):** Item **Sturmstimmgabel** (Belohnung der Post-Game-Quest „Nachhall“) löst einen Resonanzsturm aus, Abklingzeit 3 Spieltage (DR-19: Aurelune solo erreichbar). (3) **Online-Event (LiveOps):** global zu angekündigten Echtzeit-Terminen (K68). |
| Dauer | 1–2 Spielstunden (3–6 Echtzeitminuten); bei Story-Auslösung skriptgesteuert |
| Wirkung | Überall gleichzeitig (auch unter Tage); Typ-Resonanz §6; Spawns §7; seltene Event-Arten; Aurelune (#256) nur bei **Nacht + Resonanzsturm** |
| Darstellung | Himmel pulsiert in Klangfarben, schwebende Notenlinien aus Licht, Gras/Wasser vibrieren im Takt der Musik, Echos singen (Chor aller Rufe) |
| Musik | Alle Stadtmotiv-Fragmente überlagern sich (Vorahnung des Finales, CANON §56) |
| Gefahr | Keine direkte; Wildechos sind aufgewühlt (Aggressionsstufe +1, K52) – Erinnerung an die Klangpest (Lore) |

---

## 11. Wettervorhersage

| Stufe | Quelle | Anzeige |
|---|---|---|
| 0 | Himmel lesen | Wolkenaufzug 10–20 Spielminuten vor Wechsel sichtbar; Echos zeigen Vorahnung (z. B. Vögel fliegen tief vor Gewitter) |
| 1 | **Wetterhäuschen** in Städten/Dörfern (NPC oder Gerät) | Nächster Block der Region (Wetter + ungefähre Startzeit) |
| 2 | Skilltree *Forschung* „Wetterkunde I“ (K43) | Nächster Block jeder besuchten Region auf der Karte |
| 3 | Skilltree „Wetterkunde II“ | Nächste 2 Blöcke + Hinweis auf seltene Spawn-Bedingungen, die dadurch entstehen (Kodex-Verknüpfung) |
| Sonder | Kraterrand-Posten (R05) | Ausbruchsprognose 1 Spieltag vorher (K13) |

Da der Fahrplan deterministisch ist, sind Vorhersagen **immer korrekt** (keine „falschen“ Vorhersagen – Lesbarkeit vor Realismus, DR-24-Geist).

---

## 12. Präsentation: Visuell & Audio

### 12.1 Visuelle Bausteine

| Baustein | Technik | Anmerkung Switch 2 |
|---|---|---|
| Himmel & Wolken | Sky Atmosphere + Volumetric Clouds, Wetterprofile als Data Assets (`DA_WeatherVisual_W##`) | Wolkentexturen vorgebacken, 2 Schichten Billboard |
| Niederschlag | Niagara GPU (Regen, Schnee, Asche, Sand) – kamerafolgendes Volumen 60 m | CPU-Fallback, halbe Partikeldichte |
| Nässe/Schnee/Asche/Sand auf Oberflächen | Runtime Virtual Texture-Layer (K09 §9), globale Parameter `MPC_Weather` (Wetness, SnowCover, AshCover, SandCover) | identisch, niedrigere RVT-Auflösung |
| Nebel | Exponential Height Fog + Volumetric Fog; lokale Nebelvolumen | ohne Volumetric Fog |
| Blitze | Niagara + kurzzeitige Directional-Light-Spitze + Light Function | ohne Light Function |
| Aurora | Material auf Sky-Dome-Layer + Lumen-Emissive-Beitrag (schwach) | nur Sky-Material |
| Resonanzsturm | Post-Process-Pulse (synchron zur Musik via Quartz), Niagara-Notenlinien | reduzierte Partikel |

### 12.2 Audio

| Wetter | Ambient-Layer | Musikreaktion (K55) |
|---|---|---|
| Regen | Regen auf Material (Blätter, Dach, Wasser) – materialabhängig per Oberflächen-Trace | Musik −3 dB, wärmere Filter |
| Gewitter | Donner mit Distanzverzögerung (Blitz → Donner = Distanz/343 m/s) | Spannungsschicht (tiefe Streicher) |
| Nebel | Gedämpftes Ambient (Tiefpass), entfernte Rufe mit Hall | Solo-Instrument-Variante |
| Schnee | Stille-Verstärkung (Ambient −6 dB), knirschende Schritte | Glas-/Celesta-Schicht |
| Hitzewelle | Zikaden-Echos, Flirren als hohes Rauschen | ausgedünnt |
| Sandsturm | Böen, Prasseln, alles andere stark gedämpft | Perkussions-Puls |
| Aurora | Schimmerndes Pad (in Tonart), Echo-Rufe harmonisiert | Chor-Schicht |
| Aschefall | Rieseln, gedämpfte Glut | tiefer Drone |
| Resonanzsturm | Alle Echo-Rufe im Umkreis werden auf die Musiktonart quantisiert | Fragment-Überlagerung (§10) |

---

## 13. Technik & Code

### 13.1 Klassen (GF_World)

| Klasse | Aufgabe |
|---|---|
| `UWeatherDefinition` (Data Asset) | Ein Wetterzustand (aus `WeatherDefinitions.csv`) inkl. Visual-/Audio-Profil |
| `UWeatherScheduler` (pure C++, testbar) | Berechnet Blöcke aus (Seed, Region, Blockindex) |
| `UWeatherSubsystem` (World Subsystem) | Aktuelles Wetter je Region, Overrides, Events, `IWorldStateService`-Anteil |
| `AWeatherPresentationManager` | Steuert Visuals/Audio-Überblendung für die Spielerposition |
| `FWeatherOverride` | Story-/Event-Override (Region oder global) – im Save |

### 13.2 Fahrplan (deterministisch)

```cpp
// Plugins/GameFeatures/GF_World/Source/GF_World/Public/Weather/WeatherScheduler.h
/** Ein Wetterblock im Fahrplan einer Region. Zeiten in Spielminuten seit Spielbeginn. */
struct FWeatherBlock
{
	int64 StartMinute = 0;
	int32 DurationMinutes = 0;
	int32 WeatherIndex = 0;     // Index in WeatherDefinitions (W01 = 0)
};

/**
 * Reine Funktion von (Seed, Region, Blockindex) – keine Engine-Abhängigkeit, unit-testbar
 * und bitgleich zur Python-Simulation tools/sim_weather.py (gleicher RNG: FAethrisRandom).
 */
class GF_WORLD_API FWeatherScheduler
{
public:
	FWeatherScheduler(uint64 WorldWeatherSeed, int32 RegionIndex, TConstArrayView<int32> SelectionWeightsPermille,
	                  TConstArrayView<FWeatherDefRow> Defs);

	/** Liefert den Block, der die gegebene Spielminute enthält (Blöcke werden lazy erzeugt und gecacht). */
	const FWeatherBlock& BlockAt(int64 GameMinute);

	/** Die nächsten N Blöcke ab dem aktuellen (Vorhersage, §11). */
	void Forecast(int64 GameMinute, int32 Count, TArray<FWeatherBlock>& Out);

private:
	FWeatherBlock MakeNext(const FWeatherBlock& Prev);
	bool GateAllows(int32 Weather, int32 StartHour) const;

	FAethrisRandom Rng;                  // Fork(1).Fork(RegionHash)
	TArray<int32> Weights;               // kalibriert (Promille)
	TArray<FWeatherDefRow> Defs;
	TArray<FWeatherBlock> Blocks;        // Cache (älteste werden nach 48 Spielstunden verworfen)
};
```

```cpp
// Private/Weather/WeatherScheduler.cpp (Auszug)
FWeatherBlock FWeatherScheduler::MakeNext(const FWeatherBlock& Prev)
{
	const int64 Start = Prev.StartMinute + Prev.DurationMinutes;
	const int32 StartHour = static_cast<int32>((Start / 60) % 24);

	// Gewichte in Ganzzahl-Arithmetik (Determinismus): W' = Gewicht * Fensterkorrektur * 1000 / mittlereDauer
	TArray<TPair<int32, int64>, TInlineAllocator<10>> Cands;
	int64 Total = 0;
	for (int32 W = 0; W < Defs.Num(); ++W)
	{
		if (Weights[W] <= 0 || W == Prev.WeatherIndex || !GateAllows(W, StartHour)) { continue; }
		const int64 MeanX2 = Defs[W].MinHours + Defs[W].MaxHours;                // 2 × mittlere Dauer
		const int64 Window = Defs[W].GateHours();                                // 24, 12 oder 8
		const int64 Wt = int64(Weights[W]) * 24 * 2000 / (Window * MeanX2);
		Cands.Emplace(W, Wt);
		Total += Wt;
	}
	if (Cands.IsEmpty()) { Cands.Emplace(Prev.WeatherIndex, 1); Total = 1; }

	int64 Roll = int64(Rng.NextBounded(static_cast<uint32>(FMath::Min<int64>(Total, MAX_uint32))));
	int32 Chosen = Cands.Last().Key;
	for (const auto& C : Cands) { if ((Roll -= C.Value) < 0) { Chosen = C.Key; break; } }

	const int32 Hours = Rng.RangeInclusive(Defs[Chosen].MinHours, Defs[Chosen].MaxHours);
	return FWeatherBlock{ Start, Hours * 60, Chosen };
}
```

### 13.3 Wetter abfragen (für Kampf, Spawns, NPCs)

```cpp
// GF_World: IWorldStateService-Implementierung (Auszug)
FGameplayTag UWeatherSubsystem::GetWeatherAt(FName ZoneId) const
{
	if (ActiveGlobalOverride.IsSet()) { return ActiveGlobalOverride->Weather; }        // Resonanzsturm
	const int32 Region = RegionIndexOf(ZoneId);
	if (const FWeatherOverride* O = RegionOverrides.Find(Region)) { return O->Weather; } // Story
	const FWeatherBlock& B = Schedulers[Region].BlockAt(GameClock()->GetGameMinute());
	return ApplyZoneRemap(ZoneId, Defs[B.WeatherIndex].Tag);                            // Mikroklima §5
}
```

### 13.4 Ereignisse

`Event.World.WeatherChanged` (CANON §30) mit `FWeatherChangedMsg { RegionId, OldWeather, NewWeather, bIsOverride }` – gesendet bei Blockwechsel **in Regionen mit Spieler- oder Kampfpräsenz** (sonst nur intern), um Event-Last zu begrenzen.

### 13.5 Tests

| Test | Inhalt |
|---|---|
| `Aethris.Unit.World.WeatherScheduler.Determinism` | Gleicher Seed → identische 1.000 Blöcke; unterschiedliche Regionen → unterschiedliche Folgen |
| `Aethris.Unit.World.WeatherScheduler.Gates` | Aurora nie mit Startstunde außerhalb der Nacht; Hitzewelle nie nachts |
| `Aethris.Unit.World.WeatherScheduler.PythonParity` | Erste 200 Blöcke je Region identisch mit `tools/sim_weather.py`-Export |
| `Aethris.Functional.World.WeatherCoopSync` | Host + 3 Clients 2 Spielstunden: identisches Wetter je Region |

---

## 14. Performance-Budgets

| Bereich | PS5 / XSX | Switch 2 |
|---|---|---|
| Niederschlag Niagara | ≤ 0,5 ms GPU, ≤ 40 k Partikel | ≤ 0,3 ms, ≤ 12 k |
| Volumetric Clouds | ≤ 1,2 ms | vorgebacken |
| Wetter-Logik (alle Regionen) | ≤ 0,05 ms Game Thread | gleich |
| Überblendung | keine Hitches; Profile vorgeladen (Soft-Refs, Asset-Bundles `World`) | gleich |

---

## 15. Decision Records

### ADR-066 – Deterministischer Wetterfahrplan statt replizierten Zufallswetters
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Server würfelt, repliziert | Einfach | Netzlast gering, aber Save/Load ändert Wetter (Save-Scumming), Vorhersage nur unscharf |
| (b) Fahrplan aus (Seed, Region, Zeit) | Koop-synchron ohne Replikation, Vorhersage exakt, kein Save-Scumming | Kalibrierung nötig (§4.3) |
- **Entscheidung:** (b).

### ADR-067 – Kalibrierte Auswahlgewichte als generierte Daten
- **Entscheidung:** Designer pflegen nur Zielanteile; das Tool erzeugt Auswahlgewichte. Vorteil: Designer-Intention bleibt lesbar, Ergebnis nachweisbar. Nachteil: Tool-Schritt im Pre-Submit (≈ 20 s).

### ADR-068 – Wetter-Typresonanz moderat (0,8–1,3) und Ranked neutral
- **Entscheidung:** Siehe §6. Vorteil: Wetter ist taktisch relevant, aber nie entscheidend allein; Ranked fair. Nachteil: Wetter-Teams sind in der Story stärker als im Ranked → bewusst (Säule S1 vs. S3).

### ADR-069 – Resonanzsturm offline per Sturmstimmgabel
- **Entscheidung:** Post-Game-Item mit 3-Spieltage-Abklingzeit. Vorteil: DR-19 (Aurelune solo), keine Echtzeit-Abhängigkeit (DR-23). Online-Events bleiben zusätzlich.

---

## 16. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §61 | Wetterzustände mit Dauer, Startfenster, Sicht, Wind, Nässe, Belastung (`WeatherDefinitions.csv`) | LOCKED |
| §61 | Wetterfahrplan: deterministisch aus Weltseed Fork(1) × Region × Blockindex; Auswahl ∝ Gewicht / mittlere Dauer × Fensterkorrektur, keine direkte Wiederholung; Überblendung 10–20 Spielminuten | LOCKED |
| §61 | Kalibrierte Auswahlgewichte `WeatherSelectionWeights.csv` (generiert durch `tools/sim_weather.py`, Toleranz ≤ 3 pp) | LOCKED |
| §61 | Mikroklima-Remaps (`ZoneWeatherRemap.csv`), Regionsgrenzen-Überblendung 150 m | LOCKED |
| §62 | Typ-Resonanz je Wetter (0,8–1,3) + Sonderregeln Blitzschlag, Nebelsicht, Schneefall, Sandschliff, Aurora-Harmonie, Aschesicht, Resonanzflut; Ranked = Klar | LOCKED |
| §62 | Spawn-Multiplikatoren je Wetter × Typ (`WeatherSpawnModifiers.csv`) | LOCKED |
| §62 | NPC-Reaktionen (§8), Traversal-Wirkungen (§9), Resonanzsinn +50 % im Nebel | LOCKED |
| §63 | Resonanzsturm: Story (W6, Finale), Post-Game **Sturmstimmgabel** (Abklingzeit 3 Spieltage), LiveOps; 1–2 Spielstunden; Aurelune nur Nacht + Resonanzsturm; Wildechos Aggression +1 | LOCKED |
| §63 | Wettervorhersage-Stufen 0–3 (Himmel, Wetterhäuschen, Wetterkunde I/II), immer korrekt | LOCKED |
| §64 | Tagesphasen: Dämmerung 5–7, Tag 7–19, Abend 19–21, Nacht 21–5 (Hvitfell Nacht 20–6; Nimbara Tag 6–20) – löst Q9 | LOCKED |
| §10 | ADR-066 – ADR-069 | LOCKED |

---

## 17. Kapitel-Checkliste

- [x] Zehn Wetterzustände mit Gameplay-Parametern (Daten)
- [x] Tagesphasen-Grenzen festgelegt (Q9 gelöst)
- [x] Deterministischer Wetterfahrplan inkl. Kalibrierung und Simulationsnachweis (alle Regionen ≤ 2 pp)
- [x] Mikroklima und Regionsgrenzen
- [x] Wirkung auf Kampf (Typ-Resonanz + Sonderregeln), Spawns, NPCs, Traversal
- [x] Resonanzsturm als globales Ereignis inkl. Offline-Zugang
- [x] Vorhersagesystem
- [x] Visuelle und akustische Präsentation inkl. Switch-2-Fallbacks
- [x] Code: Scheduler (Ganzzahl, deterministisch), Abfrage, Events; Tests
- [x] Performance-Budgets
- [x] ADR-066 – ADR-069, CANON aktualisiert

➡️ **Nächstes Kapitel: K15 – Tageszyklus & Beleuchtung.**
