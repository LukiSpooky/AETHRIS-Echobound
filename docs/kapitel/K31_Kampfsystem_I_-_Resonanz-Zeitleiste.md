# K31 · Kampfsystem I – Die Resonanz-Zeitleiste

| Feld | Wert |
|---|---|
| Dokument | Kapitel 31 von 68 · Combat Guide, Teil IV |
| Version | 1.0 |
| Owner | Lead Combat Designer |
| Mitwirkende | Lead Gameplay Programmer, Online-Programmierer (PvP-Autorität), UX Lead (Zeitleisten-UI), Balancing Analyst, QA Lead (Determinismus-Tests) |
| Baut auf | ADR-005 (Zeitleiste statt Runden), DR-06/07/10/11/14/21, CANON §6.1 (Formate), §18 (Gehorsam), §79 (Stufen), §97–§108 (Fähigkeiten, Zeitkosten, Crescendo) |
| Status | ✅ Freigegeben – **löst Q1** (Zeitleisten-Formel, Tick-Größe) |
| Im Repository | `tools/ref/aethris_combat.py` (Referenzmodell + Simulationsbericht), `Plugins/GameFeatures/GF_Combat/…/Timeline/ResonanceTimeline.h/.cpp` |
| Neue Kanon-Einträge | CANON §109 (Zeiteinheiten), §110 (Verzögerungsformel), §111 (Zugablauf & Modifikatoren), §112 (Vorgriff, Ankündigung, Gleichstand), §113 (Wechsel, Flucht, Kampfende) |

---

## Inhalt

1. [Warum eine Zeitleiste](#1-warum-eine-zeitleiste)
2. [Zeiteinheiten: Tick, Zug, Runde](#2-zeiteinheiten-tick-zug-runde)
3. [Die Verzögerungsformel (Q1)](#3-die-verzögerungsformel-q1)
4. [Kampfbeginn](#4-kampfbeginn)
5. [Der Zugablauf](#5-der-zugablauf)
6. [Modifikatoren der Zeit](#6-modifikatoren-der-zeit)
7. [Vorgriff – Priorität auf der Zeitleiste](#7-vorgriff--priorität-auf-der-zeitleiste)
8. [Aufladung und Ankündigung](#8-aufladung-und-ankündigung)
9. [Gleichstand und simultane Planung](#9-gleichstand-und-simultane-planung)
10. [Wechsel, Verklingen, Flucht, Kampfende](#10-wechsel-verklingen-flucht-kampfende)
11. [Formate auf der Zeitleiste](#11-formate-auf-der-zeitleiste)
12. [Darstellung und Bedienung](#12-darstellung-und-bedienung)
13. [Simulation und Kampfdauer](#13-simulation-und-kampfdauer)
14. [Code](#14-code)
15. [Tests](#15-tests)
16. [Decision Records](#16-decision-records)
17. [Kanon-Änderungen](#17-kanon-änderungen)
18. [Kapitel-Checkliste](#18-kapitel-checkliste)

---

## 1. Warum eine Zeitleiste

ADR-005 hat entschieden: AETHRIS kämpft nicht in simultanen Runden, sondern auf einer **Resonanz-Zeitleiste** (Conditional Turn-Based). Jedes Echo handelt, wenn es „an der Reihe“ ist; jede Aktion verschiebt seinen nächsten Zug um eine Zeit, die von den **Zeitkosten der Fähigkeit** (K28) und seiner **Geschwindigkeit** abhängt. Daraus entsteht das Gefühl, das K02 als Kampf-Fantasie beschrieben hat:

> *Ich sehe auf der Zeitleiste, dass der Gegner in zwei Zügen seinen großen Angriff macht. Ich verzögere ihn mit einem Klang-Stoß, stelle mein Stein-Echo nach vorn, und als der Angriff kommt, hat mein Team genug Harmonie für ein Crescendo.*

Die Zeitleiste ist damit gleichzeitig **Initiative-System**, **Ressource** und **Informationsquelle**:

| Funktion | Ausprägung |
|---|---|
| Initiative | Wer schneller ist, handelt öfter – aber nicht absolut: Zeitkosten entscheiden mit |
| Ressource | Zeit ist die Währung jeder Aktion (keine Abklingzeiten, ADR-094) |
| Information | Die nächsten ≥ 8 Züge sind sichtbar; jede Wahl zeigt ihre Folgen vor Bestätigung (DR-06) |
| Typ-Identität | Frost und Klang manipulieren Zeit, Sturm beschleunigt, Kristall lädt über Zeit (CANON §78) |

### 1.1 Eigenständigkeit (Clean-Room, DR-22)

Zeitleisten-Kampfsysteme sind im Genre der Rollenspiele seit Langem bekannt; im Monster-Collecting-Genre dominieren dagegen simultane Runden mit Geschwindigkeitssortierung. AETHRIS kombiniert die Zeitleiste mit drei eigenen strukturellen Achsen, die es so nirgends gibt:

1. **Zeitkosten aus einem Machtbudget** (K28): Die Zeit einer Fähigkeit ist kein Designer-Bauchgefühl, sondern Folge ihrer Wirkung – ein einziges Modell für 330 Fähigkeiten.
2. **Typ-Identitäten als Zeitmechanik**: Frost verzögert, Klang dirigiert, Sturm beschleunigt, Kristall lädt über Ankündigungen, Schwerkraft verschiebt Reihen – die Typtabelle allein entscheidet keinen Kampf.
3. **Harmonie und Crescendo als Teamrhythmus** (K30/K33): Die Zeitleiste ist zugleich eine Partitur, auf der ein Chor seinen Höhepunkt ankündigt.

Damit erfüllt die Zeitleiste die Clean-Room-Regel „mindestens eine eigene strukturelle Achse“ (K01 §4.3) mehrfach.

**Abgrenzung:** Die Zeitleiste ist kein Echtzeitsystem. Zwischen zwei Zügen steht die Kampfzeit; die Weltzeit ist während eines Kampfes angehalten (Solo) bzw. läuft weiter, ohne den Kampf zu beeinflussen (Koop, K03 §3).

---

## 2. Zeiteinheiten: Tick, Zug, Runde

| Einheit | Definition | Verwendung |
|---|---|---|
| **Tick** | kleinste ganzzahlige Zeiteinheit der Zeitleiste | Positionen, Verzögerungen, Vorgriff-Fenster |
| **Zug** | eine Handlung eines Echos (an seiner Position) | Status-Dauern („3 Züge“), Passiv-Auslöser `TurnStart`, PvP-Zugtimer |
| **Runde** | 100 Ticks globaler Kampfzeit | Terrain- und Wetterdauern, Arena-Mechaniken mit „alle 4 Runden“, Rundenzähler im UI |

**Präzisierung zu K28:** Status-Dauern der Datenbank (`StatusEffects.csv`, „3 Runden“) gelten als **eigene Züge des betroffenen Echos** – ein schnelles Echo schüttelt einen Status also schneller ab, ein langsames leidet länger. Terrain- und Wetter-Dauern („Terrain(Glutboden,3)“) gelten in **globalen Runden** (300 Ticks), damit Feldeffekte unabhängig davon enden, wer sie gelegt hat. Arena-Mechaniken mit „alle N Züge“ (CANON §51) werden als „alle N Runden“ gelesen. Die Spalten werden in K32 entsprechend umbenannt (`DurationTurns`).

**Tick-Größe (Q1):** Ein Standardzug (Zeitkosten 100) eines Echos mit GES 100 dauert **100 Ticks**. Diese Normierung macht Zeitkosten, Verzögerungseffekte („rückt 50 Ticks zurück“) und Runden direkt vergleichbar: 50 Ticks Verzögerung entsprechen einem halben Standardzug eines durchschnittlichen Echos.

---

## 3. Die Verzögerungsformel (Q1)

```
Verzögerung (Ticks) = max( 10, ⌊ Zeitkosten_eff × 300 / ( GES_eff + 200 ) ⌋ )

GES_eff         = GES × Stufenfaktor(GES-Stufe)            (CANON §79)
Zeitkosten_eff  = Zeitkosten × 1,3 (Verlangsamt) × 1,4 (Ungehorsam) + 20 (Verflucht)
Nächster Zug    = Jetzt + Verzögerung
```

### 3.1 Warum diese Form

Die Startformel aus K28 (`× 200 / (GES + 100)`) ließ die Geschwindigkeit zu stark wirken: Ein Echo mit GES 300 hätte 3,3 Züge pro Zug eines Echos mit GES 30 erhalten. Die finale Form mit Offset 200 dämpft das:

| Formel | GES 30 | GES 100 | GES 300 | Verhältnis 300 : 30 |
|---|---|---|---|---|
| 100 × 200 / (GES + 100) | 153 | 100 | 50 | 3,1 |
| **100 × 300 / (GES + 200)** | **130** | **100** | **60** | **2,2** |
| 100 (GES ignoriert) | 100 | 100 | 100 | 1,0 |

- **Geschwindigkeit zählt**, aber ein langsames Tank-Echo (GES 30–60) bekommt noch 60–75 % der Züge eines schnellen Angreifers. Damit bleiben Tank- und Support-Rollen spielbar (DR-10).
- **Zeitkosten zählen gleich stark für alle:** Eine Fähigkeit mit Kosten 150 kostet *jedes* Echo genau 1,5 Standardzüge.
- **Ganzzahlig:** Kein Fließkomma in der Kampflogik (Determinismus, CS-14, DR-21).

### 3.2 Verzögerungstabelle

| GES_eff | Verzögerung bei Kosten 50 / 100 / 150 / 200 | Züge je 1.000 Ticks (Kosten 100) |
|---|---|---|
| 30 | 65 / 130 / 195 / 260 | 7,7 |
| 60 | 57 / 115 / 173 / 230 | 8,7 |
| 100 | 50 / 100 / 150 / 200 | 10,0 |
| 150 | 42 / 85 / 128 / 171 | 11,8 |
| 200 | 37 / 75 / 112 / 150 | 13,3 |
| 300 | 30 / 60 / 90 / 120 | 16,7 |
| 394 | 25 / 50 / 75 / 101 | 20,0 |

**Vollständige Matrix** (Verzögerung in Ticks; Zeilen = effektive Zeitkosten, Spalten = effektive GES):

| Zeitkosten \ GES_eff | 30 | 45 | 60 | 80 | 100 | 125 | 150 | 200 | 250 | 300 | 394 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 50 | 65 | 61 | 57 | 53 | 50 | 46 | 42 | 37 | 33 | 30 | 25 |
| 60 | 78 | 73 | 69 | 64 | 60 | 55 | 51 | 45 | 40 | 36 | 30 |
| 70 | 91 | 85 | 80 | 75 | 70 | 64 | 60 | 52 | 46 | 42 | 35 |
| 80 | 104 | 97 | 92 | 85 | 80 | 73 | 68 | 60 | 53 | 48 | 40 |
| 90 | 117 | 110 | 103 | 96 | 90 | 83 | 77 | 67 | 60 | 54 | 45 |
| 100 | 130 | 122 | 115 | 107 | 100 | 92 | 85 | 75 | 66 | 60 | 50 |
| 110 | 143 | 134 | 126 | 117 | 110 | 101 | 94 | 82 | 73 | 66 | 55 |
| 120 | 156 | 146 | 138 | 128 | 120 | 110 | 102 | 90 | 80 | 72 | 60 |
| 130 | 169 | 159 | 150 | 139 | 130 | 120 | 111 | 97 | 86 | 78 | 65 |
| 140 | 182 | 171 | 161 | 150 | 140 | 129 | 120 | 105 | 93 | 84 | 70 |
| 150 | 195 | 183 | 173 | 160 | 150 | 138 | 128 | 112 | 100 | 90 | 75 |
| 160 | 208 | 195 | 184 | 171 | 160 | 147 | 137 | 120 | 106 | 96 | 80 |
| 170 | 221 | 208 | 196 | 182 | 170 | 156 | 145 | 127 | 113 | 102 | 85 |
| 180 | 234 | 220 | 207 | 192 | 180 | 166 | 154 | 135 | 120 | 108 | 90 |
| 190 | 247 | 232 | 219 | 203 | 190 | 175 | 162 | 142 | 126 | 114 | 95 |
| 200 | 260 | 244 | 230 | 214 | 200 | 184 | 171 | 150 | 133 | 120 | 101 |

Lesebeispiel: Ein Stein-Tank mit GES 45 und Felswall (Zeitkosten 70) wartet 85 Ticks; ein Sturm-Echo mit GES 150 und Böenhieb (60) nur 51 Ticks – es handelt in derselben Zeit 1,7-mal.

Die Mindestverzögerung von 10 Ticks verhindert Endlosschleifen bei extremen Kombinationen (z. B. GES-Stufe +4 und Zeitkosten 50).

### 3.3 Geschwindigkeit über das Spiel

Weil GES mit dem Level wächst, werden *alle* Echos über das Spiel schneller – in Ticks gemessen. Relevant ist aber nur das **Verhältnis** zwischen den Kämpfenden. Zwei gleichstufige Echos mit Basis-GES 40 und 120 (typische Spannweite) haben auf Lv. 50 GES 47 bzw. 140 und damit Verzögerungen von 121 bzw. 88 Ticks – Verhältnis 1,4. Das ist der Normalfall; Extreme (Stufen ±4, Persönlichkeit, Schliff) erreichen etwa 2,2.

---

## 4. Kampfbeginn

| Schritt | Regel |
|---|---|
| 1. Aufstellung | Format bestimmt aktive Echos (1/2/3 je Seite, Raid K35); Reihenwahl (K33) |
| 2. Erster Zug | Startposition = Verzögerung(100, GES_eff) × J/1000, J zufällig 850–1000 (gedeckelt, DR-07) |
| 3. Hinterhalt | Bemerkt der Wärter ein Wildecho zuerst (Schleichen, K53) oder greift von hinten an: J − 200 für die eigene Seite; umgekehrt bei Überraschung durch ein Wildecho (max. 1 angekündigter Hinterhalt pro Quest, DR-14) |
| 4. Einwechsel-Passive | `BattleStart`/`SwitchIn`-Passive lösen in Zeitleisten-Reihenfolge aus (Vorschau zeigt sie) |
| 5. Feldklang | Ein Feldklang aktiviert sich beim Einwechseln seines Trägers (K29 §4) |

Der zufällige Anteil ist bewusst klein (max. 15 % eines Standardzugs) und sofort sichtbar: Der Spieler sieht die Startreihenfolge, bevor der erste Zug beginnt.

---

## 5. Der Zugablauf

```
┌──────────────── ZUG EINES ECHOS ────────────────────────────────────────────┐
│ 1 TurnBegin     Jetzt := Tick des Echos; Fremdverzögerungszähler := 0         │
│ 2 Status-Tick   Brand/Gift-Schaden, Regen, Dauer −1 (eigene Züge)              │
│ 3 Passive       Auslöser TurnStart, Weather.X, Terrain.X, RowFront/Back        │
│ 4 Sonderfälle   Starre → Zug entfällt (Delay 100), Ankündigung → Auflösung     │
│ 5 Wahl          Fähigkeit · Wechsel · Bindung (K36) · Item · Flucht            │
│                 Vorschau: Geisterposition jedes Kandidaten auf der Zeitleiste  │
│ 6 Auflösung     Treffer, Schaden (K32), Effekte (DSL), Kombo-Prüfung (K33)     │
│ 7 Commit        Nächster Zug := Jetzt + Verzögerung(Zeitkosten_eff, GES_eff)   │
│ 8 TurnEnd       Ereignis Combat.TurnEnded; Kampfende-Prüfung                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Zustandsmaschine (GF_Combat, `UCombatFlow`):** `Setup → StartOrder → [TurnBegin → StatusTick → Passives → AwaitChoice → Resolve → Commit → TurnEnd]* → Outcome`. Jeder Zustand ist ein `FAethrisState` (K06 §7) mit Ein- und Austrittsereignis auf dem Event-Bus; UI, Audio und Kamera hören ausschließlich auf diese Ereignisse (Schichtenregel CANON §26).

**Items im Kampf:** Ein Item (Trank, Siegel-Vorbereitung, Lockmittel) kostet Zeitkosten 60 für das handelnde Echo; Items sind im PvP-Ranked deaktiviert (K61).

---

## 6. Modifikatoren der Zeit

| Modifikator | Wirkung | Quelle | Deckel / Regel |
|---|---|---|---|
| GES-Stufen | GES_eff = GES × 500…2000 ‰ | Stage(…,Speed,±n) | −4…+4 (CANON §79) |
| Verlangsamt | Zeitkosten × 1,3 | Status (Frost, Flut, Schwerkraft) | 3 eigene Züge |
| Verflucht | Zeitkosten + 20 | Status (Arkan, Geist) | 3 eigene Züge |
| Ungehorsam | Zeitkosten × 1,4 | getauschte Echos über Gehorsamsgrenze (CANON §18) | deterministisch, nie Verweigerung |
| Delay(x) | nächster Zug des Ziels +x Ticks | Frost, Klang | **Fremdverzögerung ≤ 100 Ticks** zwischen zwei eigenen Zügen des Ziels |
| Haste(x) | nächster Zug −x Ticks | Sturm, Klang | frühestens Jetzt + 1 |
| Erschüttert | +50 Ticks Verzögerung (Sofort-Effekt) | Stein, Sturm, Klang, Metall | zählt in den Fremdverzögerungs-Deckel |
| Starre | nächster Zug entfällt: +100 Ticks | Frost | danach 2 Züge immun (ADR-097); zählt in den Deckel |
| Passive TimeCost(±n) | Zeitkosten ±n | Windläufer, Taktgefühl, Regelbrecher | ≥ −10 (K29) |

### 6.1 Der Fremdverzögerungs-Deckel

Ohne Deckel könnten zwei Frost-Echos ein Ziel dauerhaft am Handeln hindern („Lock“). Der Deckel begrenzt **alle fremden Verzögerungen**, die ein Echo zwischen zwei eigenen Zügen erleidet, auf **100 Ticks** – also einen Standardzug. Überschüssige Verzögerung verfällt und wird in der Vorschau grau angezeigt („gedeckelt“). Damit bleibt Frost stark (ein Gegner verliert bis zu einen Zug pro Zyklus), aber nie dominant.

```
Ziel Z, nächster Zug bei 340, Jetzt 300
  Frost-Echo:  Gletscherdruck  Delay 40  → 380  (Zähler 40)
  Klang-Echo:  Taktbruch       Delay 50  → 430  (Zähler 90)
  Frost-Echo:  Raureifhauch    Delay 20  → 440  (Zähler 100, 10 Ticks verfallen)
  Z handelt bei 440 → Zähler 0
```

---

## 7. Vorgriff – Priorität auf der Zeitleiste

Fähigkeiten mit `Priority(n)` erlauben einen **Vorgriff**: Ein Echo, dessen nächster Zug höchstens **25 × n Ticks** entfernt ist, darf eine Prioritätsfähigkeit *sofort* einsetzen – zu Beginn des Zuges eines anderen Kämpfers. Sein Folgezug wird danach **von seiner ursprünglichen Position** aus berechnet.

```
Jetzt 500: Gegner G beginnt seinen Zug (Ankündigung „Diamantlanze“ wäre möglich)
Eigenes Sturm-Echo S: nächster Zug bei 520 (Abstand 20 ≤ 25 × 1)
  → Vorgriff-Hinweis: „Böenhieb jetzt?“
  → S handelt bei 500; Folgezug = 520 + Verzögerung(60) statt 500 + …
```

| Regel | Wert |
|---|---|
| Fenster | 25 Ticks je Prioritätsstufe (aktive Fähigkeiten: Stufe 1) |
| Zeitpunkt | nur zu Beginn eines fremden Zuges (vor dessen Wahl) |
| Häufigkeit | 1 Vorgriff je Echo zwischen zwei eigenen Zügen |
| Mehrere Vorgriffe | Reihenfolge nach Abstand zum eigenen Zug, dann GES |
| PvP | Vorgriff-Entscheidung im 5-s-Fenster; ohne Eingabe verfällt er |
| Gegenspiel | Vorgriff ist auf der Zeitleiste als blinkender Rand sichtbar (Gegner wissen, dass er möglich ist) |

Der Vorgriff ist der Grund, warum Priorität im Machtbudget (+15 MP je Stufe) *Zeit kostet*: Das Echo bezahlt mit höheren Zeitkosten für das Recht, im richtigen Moment zuzuschlagen – etwa gegen eine Aufladung.

---

## 8. Aufladung und Ankündigung

Fähigkeiten mit `Charge()` und alle **Crescendos** werden **angekündigt**:

| Schritt | Regel |
|---|---|
| Wahl | Ankündigungsmarker bei Jetzt + Verzögerung(Zeitkosten) (Crescendo: Zeitkosten 200) |
| Warten | Das Echo hat keine Züge bis zum Marker; es ist „sammelnd“ (Symbol) |
| Störung | Fremdverzögerung verschiebt den Marker (Deckel gilt); **Starre** bricht ab; **Verstummt** bricht `Sound`-Fähigkeiten ab; Verklingen bricht ab (Crescendo: 50 % Harmonie zurück, K30) |
| Auflösung | Am Marker wird die Fähigkeit ausgeführt |
| Nachklang | Folgezug bei Marker + Verzögerung(50) |

Eine Aufladung ist damit eine **sichtbare Drohung** – genau die Situation, die K02 als Kampf-Fantasie beschreibt. Gegenspiel: Verzögern (Frost/Klang), Vorgriff, Schild (Stein), Reflexion (Kristall), Rückzug in die Hinterreihe (K33) oder Wechsel.

---

## 9. Gleichstand und simultane Planung

Fallen zwei Züge auf denselben Tick:

1. höhere **GES_eff** handelt zuerst;
2. bei gleicher GES: die Seite, die **zuletzt nicht** gehandelt hat;
3. sonst PCG-Zufall unter den verbleibenden (seeded, reproduzierbar).

**PvP und Koop:** Haben zwei Spieler auf demselben Tick einen Zug, **planen beide gleichzeitig** (ADR-005: „gleichzeitige Planung bei gleichem Tick“). Die Auflösung folgt der Gleichstandsregel. So wartet niemand doppelt (DR-23).

**Determinismus:** Jeder Kampf erhält einen Seed aus `Fork(5)` der Weltsaat (Seed-Hierarchie: 1 Wetter, 2 Spawn, 3 Zucht, 4 Beute, **5 Kampf**) und der Begegnungs-ID; PvP-Kämpfe erhalten ihren Seed vom Server. Replays (K61) speichern nur Seed + Eingaben.

---

## 10. Wechsel, Verklingen, Flucht, Kampfende

| Aktion | Zeitkosten / Regel |
|---|---|
| **Wechsel** (Reserve → aktiv) | Aktion des ausgehenden Echos; das eingehende Echo erhält seinen ersten Zug bei Jetzt + Verzögerung(60, GES_ein). Stufen und Status (außer Gift-Hälfte, K28) werden beim ausgehenden zurückgesetzt |
| **Ersatz nach Verklingen** | Eingehendes Echo bei Jetzt + Verzögerung(100) × 500 ‰ („halber Start“) – Verklingen wird nicht zusätzlich bestraft (DR-10) |
| **Bindung** | Aktion des Wärters über ein aktives Echo (Zeitkosten 100, K36) |
| **Flucht** | Rückzugsmarker bei Jetzt + Verzögerung(100) des schnellsten eigenen Echos; erreicht die Zeitleiste den Marker, endet der Kampf. Gegner erhalten bis dahin ihre Züge. Gegen Arenen, Bosse, PvP nicht möglich. Kein Zufall (DR-07) |
| **Kampfende** | Alle aktiven + Reserve-Echos einer Seite verklungen, Flucht, erfolgreiche Bindung (K02 §5) |

**Reserve-Grenzen:** Duell 1 aktiv + bis zu 5 Reserve; Duo 2 + 4; Trio 3 + 3 (Chor 6, CANON §6). Wildkämpfe: Reserve des Wärters steht immer zur Verfügung; Wildechos haben keine Reserve (außer Herden-Begegnungen, K52).

---

## 11. Formate auf der Zeitleiste

| Format | Aktive je Seite | Zeitleiste | Steuerung | Besonderheit |
|---|---|---|---|---|
| Duell 1v1 | 1 | eine Leiste, 2 Spuren | 1 Spieler je Seite | Flächenfähigkeiten treffen 1 Ziel (Schaden ×0,8, K32) |
| Duo 2v2 | 2 | 4 Spuren | 1 Spieler (Solo) oder 2 (Koop) | Formation Vorder/Hinter ab hier relevant (K33) |
| Trio 3v3 | 3 | 6 Spuren | 1–3 Spieler | Standardformat Arena und Ranked |
| Raid | 4 Spieler × 1–2 Echos vs. Boss | Boss mit Mehrfachspuren (Phasen, K35) | 4 Spieler | gemeinsame Harmonie je Gruppe (K30) |

In Koop-Kämpfen steuert jeder Spieler seine eigenen Echos; die Zeitleiste zeigt Spielerfarben am Markerrand.

---

## 12. Darstellung und Bedienung

```
 JETZT ▼
 ├─[S Wisplet]──[G Kharspinne]──[S Brokkar]──[G Kharspinne ✦]──[S Wisplet]──[G Uvlet]──[S Brokkar]──[G Kharspinne]─▶
   220            236               251            284 (Ankündigung)    291           310          340         352
                    ▲ Geisterposition „Taktbruch“: Kharspinne → 286 (gedeckelt 0)
```

| Element | Darstellung (DR-24: Symbol + Ton) |
|---|---|
| Marker | Porträt im Typ-Rahmen (Seitenfarbe Blau/Rot + Form ◆/●), Tick-Zahl optional |
| Vorschau | ≥ 8 Züge (DR-06); intern unbegrenzt; Scrollen bis 16 |
| Geisterposition | Beim Fokus auf eine Fähigkeit: neue eigene Position + verschobene Gegnerpositionen (Delay/Haste) |
| Ankündigung | Goldener Stern ✦, pulsierend; Crescendo mit Chor-Akkord |
| Vorgriff möglich | Blinkender Rand am eigenen Marker + kurzer Glockenton |
| Gedeckelt | Graue Schraffur am Ziel, Tooltip „Fremdverzögerung gedeckelt“ |
| Barrierefreiheit | Zahlenmodus (Ticks anzeigen), Farbenblind-Formen, Vorlesen der nächsten 3 Züge |

**Eingabe (Controller):** Fähigkeit wählen → Ziel wählen → Vorschau prüfen → Bestätigen. `LB/L1` hält die Zeitleisten-Vorschau offen (K02 §6).

---

## 13. Simulation und Kampfdauer

`tools/ref/aethris_combat.py report` simuliert 400 zufällige 1v1-Duelle je Level zwischen Arten des Katalogs (Anlage 7, Standardfähigkeit Stärke 70 / Kosten 100, Eigenklang, Typtabelle, 5 % Fehlschlag, Volltreffer 4,2 %). Ergebnis mit der finalen Schadensformel aus K32:

| Level | Ø Züge gesamt (1v1) | Median | P90 | Ø Ticks | Ø Dauer bei 7 s/Zug |
|---|---|---|---|---|---|
| 5 | 7,8 | 7 | 13 | 555 | 54 s |
| 10 | 7,8 | 7 | 12 | 536 | 54 s |
| 20 | 8,0 | 7 | 13 | 519 | 56 s |
| 35 | 8,7 | 7 | 15 | 512 | 61 s |
| 50 | 8,5 | 7 | 14 | 461 | 60 s |
| 70 | 8,6 | 8 | 13 | 423 | 60 s |
| 100 | 8,3 | 8 | 14 | 361 | 58 s |

**Bewertung gegen DR-11** (Wildkampf 60–120 s): Ein reiner Schlagabtausch gleichstufiger Echos dauert ~8 Züge ≈ 1 min. Reale Wildkämpfe enthalten zusätzlich Bindungsversuche, Status- und Positionszüge (+3–6 Züge), Wildechos liegen im Schnitt 1–3 Level unter dem Spieler-Chor → **Zielband 60–120 s erreicht**. Trainer- (Duo, 3–6 min) und Arenakämpfe (Trio mit 6 Echos je Seite, 8–15 min) skalieren über Anzahl der Echos; K63 kalibriert mit vollständigen Fähigkeitssets.

### 13.1 Levelunabhängigkeit

**Levelunabhängigkeit:** Die Zahl der Züge bleibt über alle Level stabil (7,6–8,6) – Kämpfe auf Lv. 100 fühlen sich nicht zäher an als auf Lv. 10.


### 13.2 Durchgerechnetes Beispiel (Duo)

Wisplet (Sturm, GES 74) und Brokkar (Stein, GES 41) gegen Uvlet (Frost, GES 58) und Ligrel (Schwerkraft, GES 52). Seed `0xC31`. Die Tabelle stammt direkt aus `aethris_combat.sample_log()`:

| # | Tick | Echo | Aktion (Kosten) | Wirkung auf die Zeitleiste | Nächster Zug |
|---|---|---|---|---|---|
| 1 | 103 | Uvlet | Raureifhauch (60) | Wisplet +20 Ticks → 128 | 172 |
| 2 | 112 | Ligrel | Massezug (90) | Brokkar in die Vorderreihe (K33) | 219 |
| 3 | 113 | Brokkar | Steinhaut (60) | – | 187 |
| 4 | 128 | Wisplet | Böenhieb (60) | – | 193 |
| 5 | 172 | Uvlet | Frostbiss (80) | – | 265 |
| 6 | 187 | Brokkar | Felsrammen (80) | Uvlet erschüttert: +50 → 315 | 286 |
| 7 | 193 | Wisplet | Klingenwind (60) | – | 258 |
| 8 | 219 | Ligrel | Gewichtslast (60) | – | 290 |
| 9 | 258 | Wisplet | Böenchor (50) | Brokkar −50 Ticks → 259 | 312 |
| 10 | 259 | Brokkar | Kieselwurf (60) | – | 333 |
| 11 | 290 | Ligrel | Schwerefaust (60) | – | 361 |
| 12 | 312 | Wisplet | Böenhieb (60) | – | 377 |
| 13 | 315 | Uvlet | Raureifhauch (60) | Brokkar +20 Ticks → 353 | 384 |
| 14 | 353 | Brokkar | Steinhaut (60) | – | 427 |

**Lesart:**
- **Zug 1:** Uvlet beginnt (beste Startposition nach Zufallsanteil) und verzögert Wisplet um 20 Ticks – Frost tut, was Frost tut.
- **Zug 2–3:** Ligrel zieht Brokkar nach vorn (Formation, K33); Brokkar antwortet mit Steinhaut – der Tank nimmt die Vorderreihe an.
- **Zug 6:** Brokkars Felsrammen erschüttert Uvlet (+50 Ticks). Uvlets nächster Zug rutscht von 265 auf 315 – Stein bestraft Frost mit dessen eigener Waffe.
- **Zug 9:** Wisplets Böenchor zieht Brokkar um 50 Ticks vor; Brokkar handelt sofort danach (Tick 259) – eine „Doppelaktion“ des Teams, sichtbar geplant.
- **Zug 13:** Uvlet verzögert Brokkar erneut; der Deckel (100) ist nicht erreicht.

Nach 14 Zügen hat das langsame Stein-Echo dank Teamtempo genauso oft gehandelt (4×) wie das Frost-Echo – Geschwindigkeit ist eine Teamressource, nicht nur ein Artwert.

### 13.3 Sonderfälle

| Situation | Regel |
|---|---|
| Delay auf ein Echo mit Ankündigung | verschiebt den Ankündigungsmarker (Deckel gilt) |
| Haste auf ein Echo mit Ankündigung | wirkungslos (Ankündigungen sind fest nach vorn) |
| Starre während Ankündigung | Ankündigung bricht ab; Crescendo erstattet 50 % Harmonie |
| Wechsel während eigener Ankündigung | nicht möglich (Echo „sammelt“) |
| Erzwungener Wechsel (Rückstoß, Gezeitenwende) | Ausgehendes behält seine Ankündigung nicht; eingehendes nach Wechselregel |
| GES-Stufe ändert sich zwischen zwei Zügen | Verzögerung ist bereits festgelegt; neue GES gilt ab dem nächsten Commit |
| Zwei Vorgriffe auf denselben fremden Zug | Reihenfolge nach Abstand zum eigenen Zug, dann GES |
| Vorgriff gegen eine Ankündigung | erlaubt zu Beginn jedes fremden Zuges, also auch kurz vor der Auflösung |
| Verlangsamt + Verflucht | (Kosten × 1,3) + 20 |
| Ungehorsam + Verlangsamt | Kosten × 1,3 × 1,4 |
| Minimalverzögerung erreicht | 10 Ticks; weitere Verkürzungen verfallen |
| Gleichstand mit Ankündigung | Ankündigungen lösen vor normalen Zügen desselben Ticks auf |
| Feldklang Taktwechsel (Chronaire) | Gleichstandsregel und Verzögerung invertiert: langsamstes Echo zuerst (K29) |
| Kampfende während einer Ankündigung | Ankündigung verfällt; Harmonie-Erstattung irrelevant |
| Ein Echo verklingt durch eigenen Rückschlag | Ersatzregel wie bei Fremdeinwirkung |
| Bindung gelingt während gegnerischer Ankündigung | Kampf endet sofort; Ankündigung verfällt |
| Wildecho flieht (K52) | Fluchtmarker analog zur Spielerflucht, sichtbar |
| Koop-Spieler trennt Verbindung | Seine Echos werden 60 s lang von der KI im Modus „vorsichtig“ geführt, danach vom Host |

### 13.4 Einführung im Spiel

| Spielzeit | Schritt | Gezeigt |
|---|---|---|
| 0:52 | Erster Kampf (verstummtes Echo) | nur Zeitleiste lesen + eine Fähigkeit; Marker bewegt sich sichtbar |
| 1:20 | Rivalenkampf Kael | Zeitkosten-Vergleich zweier Fähigkeiten, Geisterposition |
| 1:55 | Zweites Echo | Wechsel kostet Zeit; Reserve-Spur |
| Rang 5 | Duo-Format | Formation (K33), Delay/Haste zwischen Verbündeten |
| Akkord 1 | Arena Eichenhall | Ankündigung eines Gegners, Gegenspiel per Verzögerung |
| Akkord 2–3 | erstes Crescendo | Harmonie-Leiste, goldener Marker |

Ein optionaler **Zeitleisten-Erklärmodus** (K02 §11) blendet zu jeder Geisterposition einen Satz ein („Dein nächster Zug kommt nach Uvlets Zug“).

### 13.5 Telemetrie

Für das Balancing (K63, K66) werden je Kampf anonymisiert erfasst: Züge je Seite, Ø Zeitkosten gewählter Fähigkeiten, Anteil gedeckelter Verzögerung, Zahl der Vorgriffe, abgebrochene Ankündigungen, Kampfdauer in Ticks und Sekunden. Zielwerte: gedeckelte Verzögerung < 5 % aller Delay-Ticks, Vorgriff in ≥ 10 % der Arena-Kämpfe genutzt.

### 13.6 Glossar der Zeitleiste

| Begriff | Bedeutung |
|---|---|
| Marker | Position eines Echos auf der Zeitleiste (nächster Zug) |
| Geisterposition | Vorschau, wo der Marker nach einer Wahl landet |
| Fremdverzögerung | Delay/Erschüttert/Starre, die ein Echo zwischen zwei eigenen Zügen erleidet (gedeckelt 100) |
| Vorgriff | vorgezogene Prioritätsfähigkeit innerhalb des Fensters 25 × Stufe |
| Ankündigung | goldener Marker einer Aufladung oder eines Crescendos |
| Nachklang | Verzögerung 50 nach einer Ankündigung |
| Runde | 100 Ticks globaler Zeit (Feld-Dauern) |
| Zug | eine Handlung eines Echos (Status-Dauern) |
| Rückzugsmarker | Fluchtzeitpunkt, sichtbar für alle |
| Startfenster | 850–1000 ‰ einer Standardverzögerung für den ersten Zug |

---

## 14. Code

### 14.1 Formel (constexpr, Python-Parität)

```cpp
namespace Aethris::Timeline
{
    constexpr int32 Delay(int32 TimeCost, int32 SpeedEff)
    {
        const int32 D = TimeCost * 300 / ((SpeedEff > 0 ? SpeedEff : 1) + 200);
        return D < 10 ? 10 : D;
    }
    static_assert(Delay(100, 100) == 100);
    static_assert(Delay(100, 394) == 50);
}
```

### 14.2 `FResonanceTimeline`

Die Klasse (`GF_Combat/Public/Timeline/ResonanceTimeline.h`) kapselt `Join`, `PopNext` (Gleichstandsregel mit `StableSort` + PCG), `Commit`, `PushBack` (mit Deckel), `PullForward`, `CanVorgriff`, `Announce` (Aufladung/Crescendo) und `Preview` (DR-06, auch mit hypothetischer Aktion für die Geisterposition). Sie hat keine Abhängigkeit zu UObject – sie läuft identisch auf Client (Vorschau) und Server (Autorität).

### 14.3 Kampffluss (Pseudocode)

```cpp
void UCombatFlow::RunTurn()
{
    const int32 Id = Timeline.PopNext();
    FCombatant& C = Combatants[Id];
    Bus->Broadcast(TAG_Combat_TurnBegin, FTurnMessage{ Id, Timeline.Now() });
    Status->TickOwnTurn(C);                              // Brand, Gift, Regen, Dauer −1
    Passives->Fire(C, TAG_Trigger_TurnStart);
    if (C.HasPendingResolve()) { Executor->ResolveAnnounced(C); Timeline.Commit(Id, 50); return EndTurn(C); }
    if (Status->ConsumeStarre(C)) { Timeline.Commit(Id, 100); return EndTurn(C); }
    Offer(C);                                            // UI oder KI (K34) – mit Preview(HypotheticalCost)
}

void UCombatFlow::OnChoice(const FCombatChoice& Choice)
{
    FCombatant& C = Current();
    const int32 Cost = Aethris::Timeline::EffectiveCost(Choice.TimeCost(), C.Is(Status_Slowed), C.Is(Status_Cursed), C.bDisobedient);
    if (Choice.IsAnnounced()) { Timeline.Announce(C.Id, Choice.TimeCost()); return EndTurn(C); }
    Executor->Execute(Ctx, Choice);                      // K28 §11.2, K32
    Timeline.Commit(C.Id, Cost);
    EndTurn(C);
}
```

---

## 15. Tests

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Combat.Timeline.Delay` | Formel gegen Tabelle §3.2 (alle 28 Werte) |
| `…Timeline.PythonParity` | 10.000 zufällige Szenarien (Seed, GES, Kosten, Delay/Haste) gegen `aethris_combat.py` – identische Zugfolge |
| `…Timeline.Cap` | Fremdverzögerung > 100 zwischen zwei Zügen wird gedeckelt |
| `…Timeline.Tie` | Gleichstand: GES, Seitenwechsel, PCG reproduzierbar |
| `…Timeline.Vorgriff` | Fenster 25 × n, Folgezug von Originalposition |
| `…Timeline.Announce` | Marker verschiebbar, Abbruch durch Starre/Verstummt/Verklingen, Nachklang 50 |
| `Aethris.Func.Combat.ReplayDeterminism` | Replay eines aufgezeichneten Trio-Kampfes auf allen Plattformen bitgleich |

---

## 16. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-107 | Verzögerung = ⌊Kosten × 300 / (GES + 200)⌋, 100 Ticks = Standardzug bei GES 100 | Geschwindigkeit zählt, dominiert aber nicht (Verhältnis ≤ 2,2); ganzzahlig | ×200/(GES+100) (zu steil), feste Zugreihenfolge (keine Tiefe) |
| ADR-108 | Fremdverzögerung ≤ 100 Ticks zwischen zwei eigenen Zügen | Anti-Lock (DR-07, DR-10) | Abnehmende Wirkung pro Anwendung (schwer lesbar) |
| ADR-109 | Priorität als **Vorgriff** (25 Ticks je Stufe) statt Sortierschlüssel | Priorität wird auf der Zeitleiste sichtbar und taktisch (Konter gegen Aufladung) | Priorität nur bei Gleichstand (bedeutungslos) |
| ADR-110 | Status-Dauern in eigenen Zügen, Feld-Dauern in Runden (100 Ticks) | Schnelligkeit hilft gegen Status; Feldeffekte enden unabhängig vom Leger | Alles in Runden (Status wirken auf langsame Echos zu kurz) |
| ADR-111 | Flucht ohne Zufall über Rückzugsmarker | DR-07; Flucht wird Entscheidung statt Würfel | Fluchtchance nach GES (Frust) |

---

## 17. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §109 | Tick (ganzzahlig; 100 Ticks = Standardzug bei GES 100), Zug (Handlung, Status-Dauern), Runde (100 Ticks, Feld-Dauern); Kampf-Seed `Fork(5)` | LOCKED – **Q1 gelöst** |
| §110 | Verzögerung = max(10, ⌊Kosten_eff × 300/(GES_eff + 200)⌋); Kosten_eff: Verlangsamt ×1,3, Ungehorsam ×1,4, Verflucht +20 | LOCKED |
| §111 | Zugablauf (8 Schritte), Startzug 850–1000 ‰ einer Standardverzögerung, Hinterhalt −200 ‰; Fremdverzögerungs-Deckel 100; Starre = +100 Ticks; Erschüttert = +50 Ticks; Haste frühestens Jetzt+1; Items Zeitkosten 60 | LOCKED |
| §112 | Vorgriff 25 Ticks × Priorität, 1× je Zyklus, Folgezug ab Originalposition; Ankündigung (Charge/Crescendo) mit Marker, Abbruchregeln, Nachklang 50; Gleichstand GES → Seitenwechsel → PCG; simultane Planung im PvP/Koop | LOCKED |
| §113 | Wechsel Kosten 60 (Eingang Jetzt+Verzögerung(60)); Ersatz nach Verklingen 500 ‰ Startverzögerung; Flucht per Rückzugsmarker (nicht vs. Arena/Boss/PvP); Kampfende-Bedingungen | LOCKED |
| §12 | Q1 ✅ gelöst | – |
| §10 | ADR-107 – ADR-111 | LOCKED |

---

## 18. Kapitel-Checkliste

- [x] Zeiteinheiten und Tick-Größe (Q1)
- [x] Verzögerungsformel mit Begründung, Tabelle, Python- und C++-Referenz (bitgleich)
- [x] Kampfbeginn, Hinterhalt, Zugablauf als Zustandsmaschine
- [x] Zeit-Modifikatoren inkl. Anti-Lock-Deckel
- [x] Priorität als Vorgriff, Aufladung/Ankündigung, Gleichstand, simultane Planung
- [x] Wechsel, Ersatz, Flucht, Kampfende, Formate
- [x] UI-Spezifikation der Zeitleiste (DR-06, DR-24, Barrierefreiheit)
- [x] Simulation: Kampfdauer levelunabhängig, DR-11-Zielband
- [x] Code + Tests, ADR-107 – ADR-111, CANON §109–§113

➡️ **Nächstes Kapitel: K32 – Kampfsystem II: Schaden, Status, Terrain und Wetter im Kampf.**
