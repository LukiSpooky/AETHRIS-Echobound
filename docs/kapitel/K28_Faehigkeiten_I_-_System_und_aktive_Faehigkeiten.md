# K28 · Fähigkeiten I – System und aktive Fähigkeiten

| Feld | Wert |
|---|---|
| Dokument | Kapitel 28 von 68 · Combat Guide, Teil I |
| Version | 1.0 |
| Owner | Lead Combat Designer |
| Mitwirkende | RPG Systems Designer, Lead Gameplay Programmer, Technical Designer (Daten-Pipeline), VFX Lead (Lesbarkeit), Audio Lead (Klang-Tags), Balancing Analyst |
| Baut auf | CANON §6 (Begriffe), §18 (Kampfset 4+1+1, Repertoire, Klangschriften), §75–§78 (Typen, Eigenklang, Identitäten), §79 (Stufen, Treffer), DR-06/07/08/10/25 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Abilities/Abilities.csv` (180 aktive Fähigkeiten), `Data/Abilities/StatusEffects.csv` (15), `tools/abilities/abl.py` (DSL, Budget, Beschreibung), `tools/abilities/abl_write.py`, `tools/gen_abilities.py` (Validator AB-01…AB-14, Renderer), `tools/authoring/abilities_active.py`, `Source/AethrisCore/Public/Data/AbilityDefinition.h` |
| Neue Kanon-Einträge | CANON §97 (Fähigkeitsarten & IDs), §98 (Machtbudget & Zeitkosten), §99 (Effekt-DSL), §100 (Status-Effekte, Startwerte), §101 (Aktive Fähigkeiten ABL_A001–A180) |

---

## Inhalt

1. [Rolle der Fähigkeiten](#1-rolle-der-fähigkeiten)
2. [Fähigkeitsarten, IDs und Kampfset](#2-fähigkeitsarten-ids-und-kampfset)
3. [Machtbudget und Zeitkosten](#3-machtbudget-und-zeitkosten)
4. [Die Effekt-Sprache](#4-die-effekt-sprache)
5. [Status-Effekte](#5-status-effekte)
6. [Kategorien, Ziele, Genauigkeit, Tags](#6-kategorien-ziele-genauigkeit-tags)
7. [Slot-Schema und Typ-Identität](#7-slot-schema-und-typ-identität)
8. [Die 180 aktiven Fähigkeiten](#8-die-180-aktiven-fähigkeiten)
9. [Erwerb und Verteilung (Vorschau K29)](#9-erwerb-und-verteilung-vorschau-k29)
10. [Validierung](#10-validierung)
11. [Code](#11-code)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Rolle der Fähigkeiten

Fähigkeiten sind die **Sprache des Kampfes**. Jede Aktion eines Echos ist eine Fähigkeit; jede Fähigkeit besitzt eine Klangfarbe (es gibt keine typlosen Schadensfähigkeiten, CANON §77) und kostet **Zeit** auf der Resonanz-Zeitleiste (K31). Daraus folgen die drei Leitfragen, an denen jede der 330 Fähigkeiten gemessen wird:

1. **Was kostet sie?** – Zeit ist die einzige Ressource im Zug. Starke Fähigkeiten verschieben den nächsten Zug weiter nach hinten. Damit ersetzt das Zeitleistensystem klassische „Aktionspunkte“ und „Abklingzeiten“: Es gibt **keine Abklingzeiten** auf aktiven Fähigkeiten (ADR-094).
2. **Was erzählt sie?** – Jede Fähigkeit transportiert die Mechanik-Identität ihres Typs (CANON §78, DR-08). Ein Spieler, der Frost-Fähigkeiten kennt, weiß, dass Frost Gegner auf der Zeitleiste zurückdrängt – noch bevor er die Beschreibung liest.
3. **Ist sie lesbar?** – Jede Fähigkeit hat eine generierte, eindeutige Regelbeschreibung (aus der Effekt-Sprache, §4), ein visuelles und akustisches Signal (DR-24) und erscheint mit Zeitkosten in der Vorschau, bevor der Spieler bestätigt (DR-06).

### 1.1 Designziele

| Ziel | Messgröße | Umsetzung |
|---|---|---|
| Kein toter Zug (DR-10) | Jede Fähigkeit hat mindestens eine Wirkung, auch bei Fehlschlag | Status-Fähigkeiten mit Genauigkeit < 100 % erzeugen bei Fehlschlag +5 Harmonie (K33) |
| Fairer Zufall (DR-07) | Trefferchance gedeckelt 50–100 %, Statuschancen sichtbar | Genauigkeit 500–1000 ‰; Statuschancen in 10-%-Schritten, Vorschau zeigt beides |
| Tiefe ohne Komplexität | ≤ 3 Effekte pro aktive Fähigkeit | Validator AB-03; 99 % der Aktiven haben ≤ 2 Effekte, keine mehr als 3 |
| Kein Content ohne Daten (DR-25) | Neue Fähigkeit = neue CSV-Zeile | Effekt-Primitiva im Code, Kombination in Daten |
| Balancierbarkeit | Ein Rechenmodell für alle Fähigkeiten | Machtbudget (§3), Zeitkosten aus dem Budget berechnet |

### 1.2 Zielzahlen

| Art | Anzahl | Je Typ | IDs | Kapitel |
|---|---|---|---|---|
| Aktiv | 180 | 12 | ABL_A001–ABL_A180 | K28 |
| Passiv | 90 | 6 | ABL_P001–ABL_P090 | K29 |
| Crescendo | 30 | 2 | ABL_U001–ABL_U030 | K30 |
| Feld | 30 | 2 | ABL_F001–ABL_F030 | K30 |
| **Summe** | **330** | 22 | – | Briefing: ≥ 300 ✔ |

---

## 2. Fähigkeitsarten, IDs und Kampfset

Das Kampfset ist seit K03 gesperrt (CANON §18): **4 aktive + 1 passive + 1 Crescendo (+ 0–1 Feldfähigkeit)**. Alle jemals gelernten aktiven Fähigkeiten bleiben im **Repertoire** und können außerhalb des Kampfes (und an Klangbrunnen, Lager-Momenten, im Hain) frei gewechselt werden – es gibt kein „Vergessen“.

```
 ┌──────────────────────── KAMPFSET EINES ECHOS ─────────────────────────┐
 │  Aktiv 1   Aktiv 2   Aktiv 3   Aktiv 4  │  Passiv  │  Crescendo │ Feld │
 │  ABL_A…    ABL_A…    ABL_A…    ABL_A…   │  ABL_P…  │  ABL_U…    │ABL_F…│
 │  Zeitkosten 50–200 je Einsatz           │ Auslöser │ Harmonie   │ Welt │
 └─────────────────────────────────────────┴──────────┴────────────┴──────┘
          ▲ wechselbar aus dem Repertoire (alle gelernten Aktiven)
```

| Art | Wann verfügbar | Wie eingesetzt | Kosten |
|---|---|---|---|
| Aktiv | ab Lernen | Spielerwahl im Zug | Zeitkosten (§3) |
| Passiv | 1–3 art-spezifische Optionen + 1 versteckte; Wechsel mit **Wandelklang** | Automatisch bei Auslöser | keine |
| Crescendo | ab **Bindungsstufe 2** | Spielerwahl, wenn Harmonie reicht | Harmonie (K33) + Zeitkosten |
| Feld | ab **Bindungsstufe 1** | In der Welt (Begleiter-Aktion, K37/K40) | Ausdauer des Echos (K40) |

**ID-Schema** (CANON §23 erweitert): `ABL_<Art><Nummer>` mit Art A/P/U/F und dreistelliger Nummer; IDs sind ewig (Retire-Regel K04 §7 via `Data/Meta/RetiredIds.csv`). Anzeigenamen sind global eindeutig und dürfen nicht mit Echo-Namen kollidieren (AB-01).

---

## 3. Machtbudget und Zeitkosten

Das Herz des Systems ist **ein einziges Rechenmodell**. Jede Fähigkeit erhält einen Wert in **Machtpunkten (MP)**, aus dem ihre **Zeitkosten** berechnet werden. Designer setzen Stärke, Genauigkeit, Ziel und Effekte – nie die Zeitkosten.

### 3.1 Formeln

```
V (Machtpunkte)  =  Schaden  +  Σ Effektwerte

Schaden          =  Stärke × Genauigkeit/1000 × Zielfaktor/1000 × mittlere Treffer/1000
                    (ganzzahlig, in dieser Reihenfolge abgerundet)

Zeitkosten       =  clamp( rund10( 20 + V ), 50, 200 )        (100 = Standardzug)
```

| Ziel | Zielfaktor (‰) | Begründung |
|---|---|---|
| Single / AnySingle | 1000 | Referenz |
| Row (eine Reihe, bis 3 Ziele im Trio) | 1400 | Reihen sind selten voll besetzt |
| Enemies (alle Gegner) | 1700 | Deckel gegen Flächen-Dominanz |
| Self, Ally, AllyRow, Allies, Field | 0 | kein Schaden; Wert nur aus Effekten |

Die **Verzögerung** auf der Zeitleiste ergibt sich in K31 aus Zeitkosten und Geschwindigkeit (Startformel: Verzögerung = Zeitkosten × 200 / (GES + 100)). Damit sind Zeitkosten **geschwindigkeitsunabhängig vergleichbar**: Eine 120er-Fähigkeit kostet jedes Echo 20 % mehr Zeit als eine 100er.

### 3.2 Effektwerte

| Effekt | Wert (MP) | Anmerkung |
|---|---|---|
| Status(X, Chance) | Statuswert(X) × Chance/1000 × Stapel | Statuswerte §5 (20–60) |
| Stage(Wer, Wert, ±n, Chance) | 20 × |n| × Wer-Faktor × Chance | positiv für eigene Seite, negativ als Nachteil |
| Delay / Haste (Ticks) | 0,4 × Ticks × Wer-Faktor | Frost/Klang-Kern |
| Push / Pull | 15 | Flut/Schwerkraft |
| SwapRows | 25 | Schwerkraft |
| MoveSelf | 10 | Reihenwechsel ohne Zeitkosten |
| Heal(Wer, %) | 1,2 × % × Wer-Faktor | Blüte |
| Regen(Wer, %, Runden) | % × Runden × Wer-Faktor | Flut/Blüte |
| Shield(Wer, %) | % × Wer-Faktor | Stein/Metall |
| Drain(‰) | 0,3 × Stärke × ‰/1000 | Lebensentzug |
| Recoil(‰) | −0,3 × Stärke × ‰/1000 | Nachteil |
| Priority(n) | 15 × n | Sturm |
| Crit(n) | 10 × n | – |
| Terrain(X, Runden) | 8 × Runden | Feldwirkung → K32 |
| Weather(X, Runden) | 6 × Runden | lokales Kampfwetter → K32 |
| Harmony(n) / HarmonyDrain(n) | n | Klang / Leere |
| Cleanse | 25 (Gruppe 40) | Licht |
| Reveal | 15 | Licht |
| Dispel(Wer) | 30 × Wer-Faktor | Leere |
| Charge | −0,15 × Stärke | sichtbare Aufladerunde (Kristall) |
| Exhaust | −0,30 × Stärke | Aussetzen danach |
| IgnoreFormation / IgnoreShield / SureHit | 10 / 15 / 10 | Geist / Leere / Licht |
| Reflect / Counter | 35 / 40 | Kristall / Metall |
| TypeChange / InvertChart / Copy | 40 / 50 / 40 | Arkan (Regelbruch) |
| StealBuffs / Decoy / Trap | 35 / 35 / 30 | – |
| Bind(n) / Taunt(n) | 10 × n / 15 × n | – |
| Charged | 20 | nächster Angriff +50 % |
| WeatherBoost / TerrainBoost | 10 | Stärke ×1,5 unter Bedingung |

**Wer-Faktor:** Einzelziel 1000 ‰ · Reihe 1300 ‰ · Gruppe/alle Gegner 1600 ‰. Bei **Status-Fähigkeiten** werden feindgerichtete Effekte zusätzlich mit der Genauigkeit gewichtet; Statusverursachung auf Reihen/alle Gegner mit dem Zielfaktor.

### 3.3 Rechenbeispiele

| Fähigkeit | Rechnung | V | Zeitkosten |
|---|---|---|---|
| Funkenbiss (Glut, 40, 100 %, 10 % Brand) | 40 + 45×0,1 = 44 | 44 | 60 |
| Feueratem (95, 90 %, 30 % Brand) | 85 + 13 = 98 | 98 | 120 |
| Esseneruption (100, 85 %, alle Gegner, Aussetzen) | 100×0,85×1,7 = 144 − 30 = 114 | 114 | 130 |
| Kältestarre (Status, 85 %, Starre sicher) | 60 × 0,85 = 51 | 51 | 70 |
| Böenchor (alle Verbündeten +50 Ticks) | 0,4×50×1,6 = 32 | 32 | 50 |
| Geisterzug (110, 85 %, Aufladung, ignoriert Formation) | 93 − 16 + 10 = 87 | 87 | 110 |

### 3.4 Effizienzkurve

Die additive Konstante 20 sorgt dafür, dass **große Fähigkeiten etwas effizienter pro Zeit** sind (Stärke 40 → 0,67 Schaden/Zeit; Stärke 120 → 0,86). Das ist gewollt: Große Fähigkeiten binden das Echo länger, sind anfälliger für Frost-Verzögerung, Klang-Unterbrechung und Fehlschläge – sie sind **Zusagen**, kleine Fähigkeiten sind **Antworten**.

```
Schaden pro Zeiteinheit (Einzelziel, 100 % Genauigkeit)
 0.90 ┤                                       ●  (130, 150)
 0.85 ┤                              ●  (120, 140)
 0.80 ┤                     ●  (90/100, 110/120)
 0.75 ┤            ●  (70, 90)
 0.70 ┤
 0.67 ┤   ●  (40, 60)
      └──┴────────┴────────┴────────┴────────┴──── Stärke
         40       70       90      120      130
```

Die **Zeitkosten-Verteilung** der 180 Aktiven ist breit (50–150); die häufigsten Werte sind 50–60 (schnelle Antworten, Statuszüge) und 110 (Standard-Hauptangriffe).

---

## 4. Die Effekt-Sprache

Fähigkeiten werden nicht programmiert, sondern **komponiert** (DR-25). Der Effekt-String in der CSV ist eine flache Liste von Primitiva:

```
Effektliste := Effekt ( ";" Effekt )*
Effekt      := Name "(" [ Arg ( "," Arg )* ] ")"
Arg         := Zahl | Bezeichner | ±Zahl
Wer         := Self | Ally | Allies | AllyRow | Target | Row | Enemies
```

Beispiele aus den Daten:

```
Status(Brand,300)                         30 % Chance auf Brand
Stage(Self,Defense,+1);Stage(Self,SpDefense,+1);Heal(Self,15)
Delay(Target,80);Stage(Target,Speed,-1)
Pull(Target);Stage(Target,Evasion,-1)
TypeChange(Target,Arcane,2)
```

**Laufzeit:** Der Editor-Import zerlegt die Zeichenkette in `FAbilityEffectSpec { Op, Args }`. `GF_Combat` besitzt eine Registry `Op → UCombatEffectPrimitive`; jedes Primitiv ist eine kleine, getestete C++-Klasse (K32). Neue Fähigkeiten brauchen damit **keinen Code**, neue Primitiva sind die einzige Ausnahme (DR-25). Die Beschreibungstexte werden aus derselben Liste generiert (`abl.describe`) und in die Lokalisierung exportiert – Regeltext und Regel können nicht auseinanderlaufen.

| Primitiv-Gruppe | Primitiva |
|---|---|
| Schaden-Modifikatoren | Multi, Crit, Drain, Recoil, Priority, SureHit, IgnoreFormation, IgnoreShield, Charge, Exhaust, Charged, WeatherBoost, TerrainBoost |
| Status & Stufen | Status, Stage, Cleanse, Dispel, StealBuffs |
| Zeitleiste | Delay, Haste |
| Position | Push, Pull, SwapRows, MoveSelf, Bind |
| Heilung & Schutz | Heal, Regen, Shield, Revive, Decoy, Taunt |
| Reaktiv | Reflect, Counter, Trap |
| Feld | Terrain, Weather |
| Team | Harmony, HarmonyDrain |
| Regelbruch (Arkan) | TypeChange, InvertChart, Copy |

---

## 5. Status-Effekte

Die 15 Status-Effekte tragen die Arbeitsnamen aus K17 (CANON §78). Jeder Typ ist gegen **genau einen** Status immun. Hier werden Quellen, Dauer und Startwerte festgelegt; die exakte Formelintegration (Runden- vs. Tick-Basis, Interaktionen) folgt in **K32**.

| DisplayName | ImmuneType | MainSources | Duration | Stacking | StartEffect | CounterPlay |
|---|---|---|---|---|---|---|
| Brand | Ember | Ember | 3 Runden | nein | 6 % max. HP Schaden je eigener Runde; ANG ×0,75 | Flut-Treffer oder Regen löschen; Reinigen |
| Ausgetrocknet | Tide | Ember|Storm|Light | 3 Runden | nein | erhaltene Heilung −50 %; Flut-Fähigkeiten +20 Zeitkosten | Regen hebt auf; Flutfeld |
| Rückstoß | Stone | Gravity|Tide|Storm | sofort | nein | Ziel wird in die Hinterreihe gestoßen; nächster Reihenwechsel +30 Zeitkosten | Bind/Wurzeln verhindern; Stein immun |
| Verlangsamt | Storm | Frost|Tide|Gravity | 3 Runden | nein | Zeitkosten aller Aktionen ×1,3 | Haste-Effekte heben auf |
| Welke | Bloom | Venom|Void|Ember | 3 Runden | nein | Regeneration/Heilung über Zeit wirkungslos; VER −1 bei Anwendung | Überwuchs-Terrain heilt Welke |
| Starre | Frost | Frost | 1 Aktion | nein | nächste Aktion entfällt; Glut-Treffer löst sofort; danach 2 Runden immun | Glut-Treffer; Reinigen |
| Entzug | Void | Void | 3 Runden | nein | keine Harmonie-Erzeugung; positive Stufen können nicht steigen | Licht-Reinigen; Klang-Harmonie |
| Geblendet | Light | Light|Crystal | 3 Runden | nein | PRÄ −2 Stufen (wirksam) | Leere-/Nebelfeld hebt auf; Reinigen |
| Vergiftet | Venom | Venom | bis Kampfende/Reinigung | 1–5 Stapel | 3 % max. HP je Stapel und Runde | Reinigen; Wechsel in Reserve halbiert Stapel |
| Erschüttert | Metal | Stone|Storm|Sound|Metal | sofort | nein | nächste Aktion +50 Ticks verzögert | Stein-Schild verhindert |
| Furcht | Spirit | Spirit|Void | 2 Runden | nein | 25 % Chance, die Aktion zu verlieren; ANG/SAN −1 | Klang-Harmonie +20 beendet |
| Gebrochen | Crystal | Metal|Crystal|Stone | 3 Runden | nein | VER/SVE −2 Stufen; aktive Schilde zerbrechen | Schild erneut aufbauen |
| Verstummt | Sound | Sound|Void | 2 Runden | nein | keine Fähigkeiten mit Tag Sound, keine Status-Fähigkeiten, kein Crescendo | Reinigen; Ablauf |
| Schwebend | Gravity | Storm|Gravity | 2 Runden | nein | kein Reihenwechsel; Boden-Angriffe (Erdgrollen u. a.) verfehlen; AUS +1, PRÄ −1 | Schwerefeld beendet |
| Verflucht | Arcane | Arcane|Spirit | 3 Runden | nein | Zeitkosten +20; positive Effekte auf das Ziel halbiert | Licht-Reinigen; Arkan immun |

**Regeln (LOCKED):**
- Ein Echo trägt höchstens **einen Haupt-Status** (Brand, Ausgetrocknet, Verlangsamt, Welke, Starre, Entzug, Geblendet, Furcht, Gebrochen, Verstummt, Schwebend, Verflucht) und zusätzlich **Vergiftet** (stapelbar) – Gift ist bewusst parallel, weil es die Typ-Identität „stapelnde Schwächung“ trägt.
- **Sofort-Effekte** (Rückstoß, Erschüttert) sind keine Dauer-Status und blockieren keinen Haupt-Status.
- Nach Starre ist ein Echo 2 Runden immun (Anti-Kette, DR-07).
- Status-Chancen werden **nicht** durch Präzision erhöht; nur durch Fähigkeiten/Passive mit explizitem Effekt.

---

## 6. Kategorien, Ziele, Genauigkeit, Tags

| Kategorie | Angriff gegen | Anzahl (Aktiv) |
|---|---|---|
| Physisch | ANG vs. VER | 48 |
| Speziell | SAN vs. SVE | 63 |
| Status | keine Schadensformel | 69 |

- **Genauigkeit** 500–1000 ‰ oder 0 (kein Wurf: Selbst, Verbündete, Feld). Die Trefferformel aus K18 deckelt das Ergebnis auf 50–100 %.
- **Tags:** `Contact` (Kontakt; löst Gegen-Effekte wie Giftkleid aus), `Sound` (blockiert durch *Verstummt*; Klang- und manche Geist-Fähigkeiten), `Ground` (verfehlt *Schwebend*-Ziele). Weitere Tags (z. B. `Projectile`, `Beam`) sind für K32 reserviert.
- **Ziele:** Single, Row, Enemies, Self, Ally, AllyRow, Allies, Field, AnySingle. Im **Duell** fallen Row/Enemies auf Single zusammen (Zielfaktor bleibt, Schaden ×0,8 in K32 – Flächenfähigkeiten sind im Duell schwächer, im Trio stärker).

---

## 7. Slot-Schema und Typ-Identität

Jeder Typ erhält genau **12 aktive Fähigkeiten** mit einem gemeinsamen Gerüst, damit jede Klangfarbe vollständig spielbar ist (auch Mono-Typ-Teams, K61 Saison-Regel):

| Slot | Rolle | Typische Werte |
|---|---|---|
| 1–2 | Einstieg (Lernset Lv. 1–10) – je eine physische und spezielle Variante | Stärke 40–45, Zeit 50–60 |
| 3–5 | Mittelklasse mit Typ-Effekt | Stärke 55–75, Zeit 70–100 |
| 6 | Schwere Fähigkeit mit Nachteil (Rückschlag, Aufladung, Aussetzen, Werteverlust) | Stärke 100–120, Zeit 110–150 |
| 7–12 | Status, Unterstützung, Feld (Terrain/Wetter), Flächenangriff, Identitäts-Sonderfähigkeit | Zeit 50–110 |

Validator **AB-12** verlangt mindestens drei Fähigkeiten je Typ, die eine Identitätsmarke aus CANON §78 tragen; **AB-13** verlangt ≥ 2 physische, ≥ 2 spezielle und ≥ 3 Status-Fähigkeiten pro Typ. Ergebnis: Jede Klangfarbe kann physisch *und* speziell gespielt werden – Arten mit hohem ANG sind nicht auf „physische Typen“ eingeschränkt.

| Typ | Identitätsmarken (CANON §78) | Beispiel-Fähigkeiten |
|---|---|---|
| Glut | Brand, Glutboden | Schwelbrand, Feuersaat |
| Flut | Push/Pull, Regen, Flutfeld | Strudelzug, Quellbad, Ebbe und Flut |
| Stein | Schilde, VER | Felswall, Steinhaut, Bergrücken |
| Sturm | Haste, Mehrfachtreffer, Priorität | Böenchor, Flatterschlag, Böenhieb |
| Blüte | Heilung, Regen, Überwuchs | Heiltau, Keimsegen, Wuchern |
| Frost | Verzögerung, Präzision, Starre | Gletscherdruck, Weißer Atem, Kältestarre |
| Leere | Entzug von Harmonie/Buffs/Schilden | Hohlklang, Abgrundwelle, Lichtschlucker |
| Licht | Enthüllen, Reinigen, Blendung | Prismenstrahl, Läuterung, Blendschein |
| Gift | stapelndes Gift | Schleichendes Gift (3 Stapel), Toxinwelle |
| Metall | Rüstung, Konter | Konterhieb, Panzerplatten, Rüstwerk |
| Geist | Formation ignorieren, Täuschung, Furcht | Seelenpfeil, Doppelgänger, Albdruck |
| Kristall | Reflexion, Laden | Spiegelwand, Aufladen, Diamantlanze |
| Klang | Zeitleiste, Harmonie | Taktbruch, Taktgeber, Kampflied |
| Schwerkraft | Ziehen, Stoßen, Reihentausch | Massezug, Gravistoß, Umkehrfeld |
| Arkan | Regelbruch | Umkehrrune, Wandlungsglyphe, Spiegelformel |

---

## 8. Die 180 aktiven Fähigkeiten

Spalten: **Kat.** Physisch/Speziell/Status · **Gen.** Genauigkeit · **Zeit** Zeitkosten · **MP** Machtbudget. Alle Werte sind aus `Data/Abilities/Abilities.csv` generiert.

### 8.1 Glut (ABL_A001–A012)
Glut ist der Typ der **anhaltenden Zerstörung**: Brand als Schadens-über-Zeit, Glutboden als Feldkontrolle, Hitzewelle als Wetter. Der Preis sind Zusagen – Esseneruption trifft alle Gegner, setzt den Anwender danach aber aus; Lodernder Ansturm ist schnell, aber schmerzhaft.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A001 | **Funkenbiss** | Phys. | 40 | 100 % | Single | 60 | 44 | Physischer Schaden, Stärke 40, gegen einen Gegner; 10 % Chance auf Brand. |
| ABL_A002 | **Glutfunke** | Spez. | 40 | 100 % | Single | 60 | 44 | Spezieller Schaden, Stärke 40, gegen einen Gegner; 10 % Chance auf Brand. |
| ABL_A003 | **Aschewirbel** | Spez. | 60 | 95 % | Single | 80 | 63 | Spezieller Schaden, Stärke 60, gegen einen Gegner; 30 % Chance: PRÄ −1 für das Ziel. |
| ABL_A004 | **Glutklaue** | Phys. | 70 | 95 % | Single | 100 | 75 | Physischer Schaden, Stärke 70, gegen einen Gegner; 20 % Chance auf Brand. |
| ABL_A005 | **Feuersaat** | Spez. | 55 | 100 % | Row | 120 | 101 | Spezieller Schaden, Stärke 55, gegen eine gegnerische Reihe; erzeugt Glutboden für 3 Runden. |
| ABL_A006 | **Schmelzhieb** | Phys. | 90 | 90 % | Single | 110 | 91 | Physischer Schaden, Stärke 90, gegen einen Gegner; Volltrefferstufe +1. |
| ABL_A007 | **Feueratem** | Spez. | 95 | 90 % | Single | 120 | 98 | Spezieller Schaden, Stärke 95, gegen einen Gegner; 30 % Chance auf Brand. |
| ABL_A008 | **Esseneruption** | Spez. | 100 | 85 % | Enemies | 130 | 114 | Spezieller Schaden, Stärke 100, gegen alle Gegner; Anwender muss danach eine Runde aussetzen. |
| ABL_A009 | **Hitzeflimmern** | Stat. | – | – | Self | 60 | 40 | AUS +1 für sich selbst; GES +1 für sich selbst. |
| ABL_A010 | **Schwelbrand** | Stat. | – | 90 % | Single | 60 | 40 | Wirkt auf einen Gegner; verursacht Brand. |
| ABL_A011 | **Sonnenesse** | Stat. | – | – | Field | 50 | 30 | Ruft Hitzewelle für 5 Runden herbei. |
| ABL_A012 | **Lodernder Ansturm** | Phys. | 80 | 100 % | Single | 110 | 88 | Physischer Schaden, Stärke 80, gegen einen Gegner; Priorität +1; Rückschlag: Anwender erleidet 33 % des Schadens. |

### 8.2 Flut (ABL_A013–A024)
Flut ist **Bewegung**: Ziehen, Stoßen, Regenerieren. Strudelzug holt ein Echo aus der schützenden Hinterreihe; Gezeitenwelle drückt eine ganze Reihe zurück. Flut ist der beste Typ, um Formationen (K33) aufzubrechen, ohne selbst zu riskieren.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A013 | **Spritzer** | Spez. | 40 | 100 % | Single | 60 | 40 | Spezieller Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A014 | **Strudelzug** | Spez. | 50 | 100 % | Single | 90 | 65 | Spezieller Schaden, Stärke 50, gegen einen Gegner; zieht das Ziel in die Vorderreihe. |
| ABL_A015 | **Brandungsschlag** | Phys. | 65 | 100 % | Single | 100 | 80 | Physischer Schaden, Stärke 65, gegen einen Gegner; stößt das Ziel in die Hinterreihe. |
| ABL_A016 | **Gezeitenwelle** | Spez. | 60 | 95 % | Row | 110 | 94 | Spezieller Schaden, Stärke 60, gegen eine gegnerische Reihe; stößt das Ziel in die Hinterreihe. |
| ABL_A017 | **Quellbad** | Stat. | – | – | Ally | 50 | 24 | Wirkt auf einen Verbündeten; einen Verbündeten heilt 3 Runden je 8 % der max. HP. |
| ABL_A018 | **Tiefenstrom** | Spez. | 90 | 95 % | Single | 110 | 85 | Spezieller Schaden, Stärke 90, gegen einen Gegner. |
| ABL_A019 | **Sturzflut** | Spez. | 110 | 85 % | Single | 90 | 73 | Spezieller Schaden, Stärke 110, gegen einen Gegner; SAN −1 für sich selbst. |
| ABL_A020 | **Ebbe und Flut** | Stat. | – | – | Field | 50 | 32 | Erzeugt Flutfeld für 4 Runden. |
| ABL_A021 | **Nebelschleier** | Stat. | – | – | Allies | 50 | 32 | Wirkt auf alle Verbündeten; AUS +1 für alle Verbündeten. |
| ABL_A022 | **Wasserpeitsche** | Phys. | 35 | 100 % | Single | 100 | 76 | Physischer Schaden, Stärke 35, gegen einen Gegner; trifft 2–2-mal; 30 % Chance: GES −1 für das Ziel. |
| ABL_A023 | **Regenruf** | Stat. | – | – | Field | 50 | 30 | Ruft Regen für 5 Runden herbei. |
| ABL_A024 | **Schaumwall** | Stat. | – | – | AllyRow | 50 | 32 | Wirkt auf eigene Reihe; Schild für die eigene Reihe (15 % der max. HP); die eigene Reihe heilt 2 Runden je 5 % der max. HP. |

### 8.3 Stein (ABL_A025–A036)
Stein **hält**. Schilde für eine Reihe (Felswall), Spott mit Schild (Bergrücken) und die Falle Splitterfalle geben Stein-Echos die Rolle des Ankers. Erdgrollen trifft alle Gegner, ist aber als einzige `Ground`-Fähigkeit gegen *Schwebend* wirkungslos.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A025 | **Kieselwurf** | Phys. | 40 | 100 % | Single | 60 | 40 | Physischer Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A026 | **Felsrammen** | Phys. | 60 | 95 % | Single | 80 | 64 | Physischer Schaden, Stärke 60, gegen einen Gegner; 20 % Chance auf Erschüttert. |
| ABL_A027 | **Sandschleuder** | Spez. | 50 | 95 % | Single | 80 | 57 | Spezieller Schaden, Stärke 50, gegen einen Gegner; 50 % Chance: PRÄ −1 für das Ziel. |
| ABL_A028 | **Geröllschauer** | Phys. | 25 | 90 % | Row | 110 | 90 | Physischer Schaden, Stärke 25, gegen eine gegnerische Reihe; trifft 2–4-mal. |
| ABL_A029 | **Erdgrollen** | Spez. | 70 | 100 % | Enemies | 140 | 119 | Spezieller Schaden, Stärke 70, gegen alle Gegner. |
| ABL_A030 | **Monolithstoß** | Phys. | 110 | 85 % | Single | 120 | 103 | Physischer Schaden, Stärke 110, gegen einen Gegner; 30 % Chance auf Erschüttert. |
| ABL_A031 | **Steinhaut** | Stat. | – | – | Self | 60 | 40 | VER +2 für sich selbst. |
| ABL_A032 | **Felswall** | Stat. | – | – | AllyRow | 50 | 26 | Wirkt auf eigene Reihe; Schild für die eigene Reihe (20 % der max. HP). |
| ABL_A033 | **Bergrücken** | Stat. | – | – | Self | 60 | 40 | Schild für sich selbst (25 % der max. HP); Gegner müssen 1 Runde(n) den Anwender angreifen. |
| ABL_A034 | **Splitterfalle** | Stat. | – | – | Field | 50 | 30 | Legt eine Falle (Splitter) auf die gegnerische Seite. |
| ABL_A035 | **Gerölllawine** | Phys. | 95 | 90 % | Row | 150 | 125 | Physischer Schaden, Stärke 95, gegen eine gegnerische Reihe; 30 % Chance: GES −1 für das Ziel. |
| ABL_A036 | **Grundfeste** | Stat. | – | – | Self | 80 | 58 | VER +1 für sich selbst; SVE +1 für sich selbst; heilt sich selbst um 15 % der max. HP. |

### 8.4 Sturm (ABL_A037–A048)
Sturm ist **Tempo**: Priorität, Mehrfachtreffer, Rückenwind für das Team. Böenchor beschleunigt alle Verbündeten um 50 Ticks – die stärkste Tempo-Unterstützung im Spiel, dafür ohne eigenen Schaden.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A037 | **Böenhieb** | Phys. | 40 | 100 % | Single | 80 | 55 | Physischer Schaden, Stärke 40, gegen einen Gegner; Priorität +1. |
| ABL_A038 | **Klingenwind** | Spez. | 45 | 100 % | Single | 80 | 55 | Spezieller Schaden, Stärke 45, gegen einen Gegner; Volltrefferstufe +1. |
| ABL_A039 | **Flatterschlag** | Phys. | 20 | 95 % | Single | 90 | 66 | Physischer Schaden, Stärke 20, gegen einen Gegner; trifft 2–5-mal. |
| ABL_A040 | **Rückenwindschlag** | Phys. | 60 | 100 % | Single | 100 | 76 | Physischer Schaden, Stärke 60, gegen einen Gegner; sich selbst rückt 40 Ticks auf der Zeitleiste vor. |
| ABL_A041 | **Blitzbogen** | Spez. | 90 | 90 % | Single | 110 | 88 | Spezieller Schaden, Stärke 90, gegen einen Gegner; 20 % Chance auf Erschüttert. |
| ABL_A042 | **Donnerkeil** | Spez. | 115 | 80 % | Single | 120 | 102 | Spezieller Schaden, Stärke 115, gegen einen Gegner; Stärke ×1,5 bei Gewitter. |
| ABL_A043 | **Wirbelsturm** | Spez. | 60 | 90 % | Enemies | 120 | 102 | Spezieller Schaden, Stärke 60, gegen alle Gegner; 20 % Chance auf Schwebend. |
| ABL_A044 | **Böenchor** | Stat. | – | – | Allies | 50 | 32 | Wirkt auf alle Verbündeten; alle Verbündeten rückt 50 Ticks auf der Zeitleiste vor. |
| ABL_A045 | **Sturmlauf** | Stat. | – | – | Self | 60 | 40 | GES +2 für sich selbst. |
| ABL_A046 | **Gewitterruf** | Stat. | – | – | Field | 50 | 30 | Ruft Gewitter für 5 Runden herbei. |
| ABL_A047 | **Kettenblitz** | Spez. | 30 | 90 % | Row | 110 | 92 | Spezieller Schaden, Stärke 30, gegen eine gegnerische Reihe; trifft 2–3-mal. |
| ABL_A048 | **Zyklonsprung** | Phys. | 75 | 100 % | Single | 120 | 97 | Physischer Schaden, Stärke 75, gegen einen Gegner; sich selbst rückt 30 Ticks auf der Zeitleiste vor; Anwender wechselt die Reihe ohne Zeitkosten. |

### 8.5 Blüte (ABL_A049–A060)
Blüte ist **Wachstum**: Einzel- und Gruppenheilung, Überwuchs-Terrain und Lebensentzug. Dornenranke bindet Gegner an ihre Reihe – Blüte hält Gegner fest, während sie sich selbst erholt.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A049 | **Rankenhieb** | Phys. | 40 | 100 % | Single | 60 | 40 | Physischer Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A050 | **Pollenschuss** | Spez. | 40 | 100 % | Single | 60 | 44 | Spezieller Schaden, Stärke 40, gegen einen Gegner; 20 % Chance: PRÄ −1 für das Ziel. |
| ABL_A051 | **Saugwurzel** | Spez. | 60 | 100 % | Single | 90 | 69 | Spezieller Schaden, Stärke 60, gegen einen Gegner; heilt den Anwender um 50 % des Schadens. |
| ABL_A052 | **Dornenranke** | Phys. | 65 | 95 % | Single | 100 | 81 | Physischer Schaden, Stärke 65, gegen einen Gegner; Ziel kann 2 Runde(n) die Reihe nicht wechseln. |
| ABL_A053 | **Blütensturm** | Spez. | 85 | 95 % | Row | 130 | 112 | Spezieller Schaden, Stärke 85, gegen eine gegnerische Reihe. |
| ABL_A054 | **Urwaldzorn** | Phys. | 110 | 85 % | Single | 110 | 85 | Physischer Schaden, Stärke 110, gegen einen Gegner; Rückschlag: Anwender erleidet 25 % des Schadens. |
| ABL_A055 | **Heiltau** | Stat. | – | – | Ally | 70 | 48 | Wirkt auf einen Verbündeten; heilt einen Verbündeten um 40 % der max. HP. |
| ABL_A056 | **Keimsegen** | Stat. | – | – | Allies | 50 | 28 | Wirkt auf alle Verbündeten; alle Verbündeten heilt 3 Runden je 6 % der max. HP. |
| ABL_A057 | **Wuchern** | Stat. | – | – | Field | 60 | 40 | Erzeugt Überwuchs für 5 Runden. |
| ABL_A058 | **Betäubungspollen** | Stat. | – | 90 % | Single | 60 | 36 | Wirkt auf einen Gegner; GES −2 für das Ziel. |
| ABL_A059 | **Sonnentrunk** | Stat. | – | – | Self | 90 | 70 | Heilt sich selbst um 50 % der max. HP; Stärke ×1,5 bei Klar. |
| ABL_A060 | **Wurzelgriff** | Stat. | – | – | Self | 70 | 52 | Sich selbst heilt 4 Runden je 8 % der max. HP; VER +1 für sich selbst. |

### 8.6 Frost (ABL_A061–A072)
Frost **verlangsamt**. Verzögerung auf der Zeitleiste (Raureifhauch, Gletscherdruck, Winterstille), Präzisionssenkung (Weißer Atem) und Starre. Frost gewinnt Kämpfe, indem der Gegner seltener handelt.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A061 | **Raureifhauch** | Spez. | 40 | 100 % | Single | 70 | 48 | Spezieller Schaden, Stärke 40, gegen einen Gegner; das Ziel rückt 20 Ticks auf der Zeitleiste zurück. |
| ABL_A062 | **Frostsplitter** | Phys. | 40 | 100 % | Single | 70 | 50 | Physischer Schaden, Stärke 40, gegen einen Gegner; Volltrefferstufe +1. |
| ABL_A063 | **Frostbiss** | Phys. | 60 | 95 % | Single | 90 | 69 | Physischer Schaden, Stärke 60, gegen einen Gegner; 30 % Chance auf Verlangsamt. |
| ABL_A064 | **Gletscherdruck** | Phys. | 85 | 90 % | Single | 110 | 92 | Physischer Schaden, Stärke 85, gegen einen Gegner; das Ziel rückt 40 Ticks auf der Zeitleiste zurück. |
| ABL_A065 | **Firnwind** | Spez. | 60 | 95 % | Row | 110 | 85 | Spezieller Schaden, Stärke 60, gegen eine gegnerische Reihe; 30 % Chance: PRÄ −1 für das Ziel. |
| ABL_A066 | **Eissturz** | Spez. | 100 | 85 % | Single | 110 | 94 | Spezieller Schaden, Stärke 100, gegen einen Gegner; 15 % Chance auf Starre. |
| ABL_A067 | **Kältestarre** | Stat. | – | 85 % | Single | 70 | 51 | Wirkt auf einen Gegner; verursacht Starre. |
| ABL_A068 | **Weißer Atem** | Stat. | – | 90 % | Enemies | 50 | 28 | Wirkt auf alle Gegner; PRÄ −1 für alle Gegner. |
| ABL_A069 | **Schneeruf** | Stat. | – | – | Field | 50 | 30 | Ruft Schneefall für 5 Runden herbei. |
| ABL_A070 | **Eisspiegel** | Stat. | – | – | Field | 50 | 32 | Erzeugt Eisfläche für 4 Runden. |
| ABL_A071 | **Frostpanzer** | Stat. | – | – | Self | 60 | 40 | Schild für sich selbst (20 % der max. HP); SVE +1 für sich selbst. |
| ABL_A072 | **Winterstille** | Spez. | 50 | 90 % | Enemies | 120 | 95 | Spezieller Schaden, Stärke 50, gegen alle Gegner; alle Gegner rückt 30 Ticks auf der Zeitleiste zurück. |

### 8.7 Leere (ABL_A073–A084)
Leere **nimmt**: Harmonie, Stufen, Schilde. Nullpunkt gehört mit 120 Stärke zu den drei stärksten Einzeltreffern unter den Aktiven – auf Kosten von zwei SAN-Stufen. Leerer Raum erzeugt ein Stillefeld (K32: Harmonie-Gewinn blockiert).

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A073 | **Dunkelgriff** | Phys. | 40 | 100 % | Single | 70 | 45 | Physischer Schaden, Stärke 40, gegen einen Gegner; entzieht dem Gegnerteam 5 Harmonie. |
| ABL_A074 | **Leerstoß** | Spez. | 45 | 100 % | Single | 70 | 45 | Spezieller Schaden, Stärke 45, gegen einen Gegner. |
| ABL_A075 | **Hohlklang** | Spez. | 60 | 100 % | Single | 110 | 90 | Spezieller Schaden, Stärke 60, gegen einen Gegner; entfernt Schilde und positive Stufen von das Ziel. |
| ABL_A076 | **Seelenzehrer** | Spez. | 70 | 95 % | Single | 100 | 76 | Spezieller Schaden, Stärke 70, gegen einen Gegner; heilt den Anwender um 50 % des Schadens. |
| ABL_A077 | **Schweigeschnitt** | Phys. | 80 | 95 % | Single | 110 | 88 | Physischer Schaden, Stärke 80, gegen einen Gegner; 30 % Chance auf Entzug. |
| ABL_A078 | **Abgrundwelle** | Spez. | 95 | 90 % | Row | 150 | 129 | Spezieller Schaden, Stärke 95, gegen eine gegnerische Reihe; entzieht dem Gegnerteam 10 Harmonie. |
| ABL_A079 | **Nullpunkt** | Spez. | 120 | 80 % | Single | 80 | 56 | Spezieller Schaden, Stärke 120, gegen einen Gegner; SAN −2 für sich selbst. |
| ABL_A080 | **Verschlingen** | Stat. | – | 90 % | Single | 50 | 31 | Wirkt auf einen Gegner; stiehlt die positiven Stufen des Ziels. |
| ABL_A081 | **Leerer Raum** | Stat. | – | – | Field | 50 | 24 | Erzeugt Stillefeld für 3 Runden. |
| ABL_A082 | **Entzugsfluch** | Stat. | – | 90 % | Single | 60 | 36 | Wirkt auf einen Gegner; verursacht Entzug. |
| ABL_A083 | **Lichtschlucker** | Stat. | – | 90 % | Enemies | 60 | 43 | Wirkt auf alle Gegner; entfernt Schilde und positive Stufen von alle Gegner. |
| ABL_A084 | **Stille Klinge** | Phys. | 65 | 100 % | Single | 100 | 80 | Physischer Schaden, Stärke 65, gegen einen Gegner; durchdringt Schilde. |

### 8.8 Licht (ABL_A085–A096)
Licht **enthüllt und reinigt**. Prismenstrahl und Enthüllung heben Ausweichen und Täuschung auf; Läuterung entfernt Status von allen Verbündeten. Zenitstoß ist der Licht-Hammer mit sichtbarer Aufladung.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A085 | **Lichtnadel** | Spez. | 40 | 100 % | Single | 70 | 50 | Spezieller Schaden, Stärke 40, gegen einen Gegner; verfehlt nie. |
| ABL_A086 | **Sonnenhieb** | Phys. | 45 | 100 % | Single | 70 | 45 | Physischer Schaden, Stärke 45, gegen einen Gegner. |
| ABL_A087 | **Blendschein** | Spez. | 55 | 100 % | Single | 90 | 67 | Spezieller Schaden, Stärke 55, gegen einen Gegner; 30 % Chance auf Geblendet. |
| ABL_A088 | **Prismenstrahl** | Spez. | 75 | 95 % | Single | 110 | 86 | Spezieller Schaden, Stärke 75, gegen einen Gegner; enthüllt das Ziel (Ausweichen, Täuschung und Tarnung wirkungslos). |
| ABL_A089 | **Morgenrot** | Phys. | 80 | 95 % | Single | 110 | 86 | Physischer Schaden, Stärke 80, gegen einen Gegner; Stärke ×1,5 bei Klar. |
| ABL_A090 | **Zenitstoß** | Spez. | 120 | 90 % | Single | 110 | 90 | Spezieller Schaden, Stärke 120, gegen einen Gegner; benötigt eine Aufladerunde (sichtbar auf der Zeitleiste). |
| ABL_A091 | **Läuterung** | Stat. | – | – | Allies | 60 | 40 | Wirkt auf alle Verbündeten; entfernt negative Status von alle Verbündeten. |
| ABL_A092 | **Sonnenwehr** | Stat. | – | – | AllyRow | 50 | 26 | Wirkt auf eigene Reihe; Schild für die eigene Reihe (20 % der max. HP). |
| ABL_A093 | **Strahlenkranz** | Spez. | 65 | 95 % | Enemies | 140 | 116 | Spezieller Schaden, Stärke 65, gegen alle Gegner; 20 % Chance auf Geblendet. |
| ABL_A094 | **Enthüllung** | Stat. | – | – | Enemies | 70 | 47 | Wirkt auf alle Gegner; enthüllt das Ziel (Ausweichen, Täuschung und Tarnung wirkungslos); AUS −1 für alle Gegner. |
| ABL_A095 | **Lichtung** | Stat. | – | – | Field | 50 | 32 | Erzeugt Lichtfeld für 4 Runden. |
| ABL_A096 | **Heilschein** | Stat. | – | – | Ally | 90 | 67 | Wirkt auf einen Verbündeten; heilt einen Verbündeten um 35 % der max. HP; entfernt negative Status von einen Verbündeten. |

### 8.9 Gift (ABL_A097–A108)
Gift **stapelt**. Bis zu fünf Gift-Stapel (je 3 % HP/Runde) machen Gift zum stärksten Langzeit-Typ, schwach in kurzen Kämpfen. Giftkleid kontert physische Angreifer.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A097 | **Nesselstich** | Phys. | 40 | 100 % | Single | 70 | 46 | Physischer Schaden, Stärke 40, gegen einen Gegner; 30 % Chance auf Vergiftet. |
| ABL_A098 | **Säurespritzer** | Spez. | 40 | 100 % | Single | 60 | 44 | Spezieller Schaden, Stärke 40, gegen einen Gegner; 20 % Chance: SVE −1 für das Ziel. |
| ABL_A099 | **Nesselpeitsche** | Phys. | 55 | 95 % | Single | 90 | 72 | Physischer Schaden, Stärke 55, gegen einen Gegner; verursacht Vergiftet. |
| ABL_A100 | **Miasma** | Spez. | 50 | 95 % | Row | 100 | 79 | Spezieller Schaden, Stärke 50, gegen eine gegnerische Reihe; 50 % Chance auf Vergiftet. |
| ABL_A101 | **Ätzklaue** | Phys. | 75 | 95 % | Single | 100 | 81 | Physischer Schaden, Stärke 75, gegen einen Gegner; 50 % Chance: VER −1 für das Ziel. |
| ABL_A102 | **Toxinwelle** | Spez. | 90 | 90 % | Single | 120 | 101 | Spezieller Schaden, Stärke 90, gegen einen Gegner; 50 % Chance auf Vergiftet (2 Stapel). |
| ABL_A103 | **Fäulnisbiss** | Phys. | 100 | 85 % | Single | 120 | 95 | Physischer Schaden, Stärke 100, gegen einen Gegner; Stärke ×1,5 auf Sumpf. |
| ABL_A104 | **Giftnebel** | Stat. | – | – | Field | 50 | 32 | Erzeugt Sumpf für 4 Runden. |
| ABL_A105 | **Schleichendes Gift** | Stat. | – | 90 % | Single | 70 | 54 | Wirkt auf einen Gegner; verursacht Vergiftet (3 Stapel). |
| ABL_A106 | **Korrosion** | Stat. | – | 90 % | Single | 60 | 36 | Wirkt auf einen Gegner; VER −2 für das Ziel. |
| ABL_A107 | **Giftkleid** | Stat. | – | – | Self | 80 | 55 | Schild für sich selbst (15 % der max. HP); kontert den nächsten physischen Angriff mit 30 % Schaden. |
| ABL_A108 | **Verwesung** | Spez. | 70 | 100 % | Enemies | 150 | 130 | Spezieller Schaden, Stärke 70, gegen alle Gegner; 20 % Chance auf Welke. |

### 8.10 Metall (ABL_A109–A120)
Metall **pariert**. Zwei Konter-Haltungen (Spiegelstahl gegen Spezial, Konterhieb gegen Physisch) und Rüstung für die Reihe; Schmiedeschlag zerbricht Verteidigungen (*Gebrochen*).

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A109 | **Erzfaust** | Phys. | 40 | 100 % | Single | 60 | 40 | Physischer Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A110 | **Klingenwurf** | Phys. | 45 | 100 % | Single | 80 | 55 | Physischer Schaden, Stärke 45, gegen einen Gegner; Volltrefferstufe +1. |
| ABL_A111 | **Hammerschlag** | Phys. | 65 | 95 % | Single | 90 | 67 | Physischer Schaden, Stärke 65, gegen einen Gegner; 30 % Chance: VER −1 für das Ziel. |
| ABL_A112 | **Stahlwirbel** | Phys. | 30 | 95 % | Row | 100 | 78 | Physischer Schaden, Stärke 30, gegen eine gegnerische Reihe; trifft 2–2-mal. |
| ABL_A113 | **Magnetpuls** | Spez. | 60 | 100 % | Single | 90 | 67 | Spezieller Schaden, Stärke 60, gegen einen Gegner; 20 % Chance auf Erschüttert. |
| ABL_A114 | **Schmiedeschlag** | Phys. | 100 | 85 % | Single | 110 | 94 | Physischer Schaden, Stärke 100, gegen einen Gegner; 20 % Chance auf Gebrochen. |
| ABL_A115 | **Spiegelstahl** | Stat. | – | – | Self | 60 | 40 | Kontert den nächsten speziellen Angriff mit 100 % Schaden. |
| ABL_A116 | **Konterhieb** | Stat. | – | – | Self | 60 | 40 | Kontert den nächsten physischen Angriff mit 150 % Schaden. |
| ABL_A117 | **Panzerplatten** | Stat. | – | – | Self | 60 | 40 | VER +2 für sich selbst. |
| ABL_A118 | **Rüstwerk** | Stat. | – | – | AllyRow | 60 | 39 | Wirkt auf eigene Reihe; VER +1 für die eigene Reihe; Schild für die eigene Reihe (10 % der max. HP). |
| ABL_A119 | **Schrapnell** | Spez. | 70 | 90 % | Enemies | 130 | 107 | Spezieller Schaden, Stärke 70, gegen alle Gegner. |
| ABL_A120 | **Stahlsturm** | Phys. | 85 | 95 % | Single | 120 | 95 | Physischer Schaden, Stärke 85, gegen einen Gegner; Schild für sich selbst (15 % der max. HP). |

### 8.11 Geist (ABL_A121–A132)
Geist **ignoriert Ordnung**. Fast alle Geist-Angriffe übergehen Formationsschutz; Doppelgänger fängt einen Angriff ab; Albdruck versetzt in Furcht.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A121 | **Geisterhauch** | Spez. | 40 | 100 % | Single | 70 | 50 | Spezieller Schaden, Stärke 40, gegen einen Gegner; ignoriert Formationsschutz. |
| ABL_A122 | **Spukgriff** | Phys. | 40 | 100 % | Single | 60 | 44 | Physischer Schaden, Stärke 40, gegen einen Gegner; 20 % Chance: ANG −1 für das Ziel. |
| ABL_A123 | **Schreckensschrei** | Spez. | 60 | 95 % | Single | 90 | 70 | Spezieller Schaden, Stärke 60, gegen einen Gegner; 30 % Chance auf Furcht. |
| ABL_A124 | **Seelenpfeil** | Spez. | 70 | 100 % | Single | 110 | 90 | Spezieller Schaden, Stärke 70, gegen einen Gegner; ignoriert Formationsschutz; verfehlt nie. |
| ABL_A125 | **Phantomklaue** | Phys. | 80 | 95 % | Single | 120 | 96 | Physischer Schaden, Stärke 80, gegen einen Gegner; ignoriert Formationsschutz; Volltrefferstufe +1. |
| ABL_A126 | **Totenklage** | Spez. | 95 | 90 % | Row | 150 | 131 | Spezieller Schaden, Stärke 95, gegen eine gegnerische Reihe; 20 % Chance auf Furcht. |
| ABL_A127 | **Doppelgänger** | Stat. | – | – | Self | 60 | 35 | Erschafft ein Trugbild, das den nächsten Angriff abfängt. |
| ABL_A128 | **Albdruck** | Stat. | – | 90 % | Single | 60 | 40 | Wirkt auf einen Gegner; verursacht Furcht. |
| ABL_A129 | **Ahnenwacht** | Stat. | – | – | Allies | 50 | 32 | Wirkt auf alle Verbündeten; SVE +1 für alle Verbündeten. |
| ABL_A130 | **Seelenband** | Stat. | – | – | Ally | 80 | 56 | Wirkt auf einen Verbündeten; heilt einen Verbündeten um 30 % der max. HP; AUS +1 für einen Verbündeten. |
| ABL_A131 | **Verschwinden** | Stat. | – | – | Self | 70 | 50 | AUS +2 für sich selbst; Anwender wechselt die Reihe ohne Zeitkosten. |
| ABL_A132 | **Geisterzug** | Spez. | 110 | 85 % | Single | 110 | 87 | Spezieller Schaden, Stärke 110, gegen einen Gegner; benötigt eine Aufladerunde (sichtbar auf der Zeitleiste); ignoriert Formationsschutz. |

### 8.12 Kristall (ABL_A133–A144)
Kristall **speichert und spiegelt**. Aufladen und Resonanzprisma bereiten große Treffer vor; Spiegelwand und Prismenpanzer werfen Angriffe zurück. Diamantlanze ist die stärkste Kristall-Fähigkeit (120) mit Aufladerunde.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A133 | **Kristallsplitter** | Phys. | 40 | 100 % | Single | 70 | 50 | Physischer Schaden, Stärke 40, gegen einen Gegner; Volltrefferstufe +1. |
| ABL_A134 | **Glitzerstrahl** | Spez. | 40 | 100 % | Single | 60 | 40 | Spezieller Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A135 | **Facettenschnitt** | Phys. | 65 | 95 % | Single | 90 | 70 | Physischer Schaden, Stärke 65, gegen einen Gegner; 20 % Chance auf Gebrochen. |
| ABL_A136 | **Resonanzprisma** | Spez. | 70 | 100 % | Single | 110 | 90 | Spezieller Schaden, Stärke 70, gegen einen Gegner; lädt den Anwender auf: nächster Angriff +50 % Stärke. |
| ABL_A137 | **Kristallregen** | Spez. | 55 | 90 % | Row | 90 | 68 | Spezieller Schaden, Stärke 55, gegen eine gegnerische Reihe. |
| ABL_A138 | **Diamantlanze** | Spez. | 120 | 90 % | Single | 110 | 90 | Spezieller Schaden, Stärke 120, gegen einen Gegner; benötigt eine Aufladerunde (sichtbar auf der Zeitleiste). |
| ABL_A139 | **Spiegelwand** | Stat. | – | – | Self | 60 | 35 | Reflektiert den nächsten speziellen Angriff. |
| ABL_A140 | **Prismenpanzer** | Stat. | – | – | Self | 80 | 55 | Reflektiert den nächsten physischen Angriff; VER +1 für sich selbst. |
| ABL_A141 | **Aufladen** | Stat. | – | – | Self | 60 | 40 | Lädt den Anwender auf: nächster Angriff +50 % Stärke; SAN +1 für sich selbst. |
| ABL_A142 | **Drusenfeld** | Stat. | – | – | Field | 50 | 32 | Erzeugt Kristallfeld für 4 Runden. |
| ABL_A143 | **Prismenfächer** | Spez. | 65 | 95 % | Enemies | 120 | 103 | Spezieller Schaden, Stärke 65, gegen alle Gegner. |
| ABL_A144 | **Klirrschlag** | Phys. | 90 | 90 % | Single | 110 | 94 | Physischer Schaden, Stärke 90, gegen einen Gegner; 30 % Chance auf Gebrochen. |

### 8.13 Klang (ABL_A145–A156)
Klang **dirigiert den Takt**: Gegner zurück (Taktbruch, Wiegenlied), Verbündete vor (Taktgeber), Harmonie für Crescendos (Summton, Kampflied, Fortissimo). Alle Klang-Fähigkeiten tragen den Tag `Sound` und sind durch *Verstummt* blockierbar – die Schwäche des Dirigenten.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A145 | **Summton** | Spez. | 40 | 100 % | Single | 70 | 45 | Spezieller Schaden, Stärke 40, gegen einen Gegner; Harmonie +5. |
| ABL_A146 | **Klangschlag** | Phys. | 40 | 100 % | Single | 70 | 48 | Physischer Schaden, Stärke 40, gegen einen Gegner; das Ziel rückt 20 Ticks auf der Zeitleiste zurück. |
| ABL_A147 | **Trommelschlag** | Phys. | 30 | 100 % | Single | 80 | 60 | Physischer Schaden, Stärke 30, gegen einen Gegner; trifft 2–2-mal. |
| ABL_A148 | **Dissonanz** | Spez. | 70 | 95 % | Single | 100 | 75 | Spezieller Schaden, Stärke 70, gegen einen Gegner; 20 % Chance auf Verstummt. |
| ABL_A149 | **Taktbruch** | Spez. | 60 | 100 % | Single | 100 | 80 | Spezieller Schaden, Stärke 60, gegen einen Gegner; das Ziel rückt 50 Ticks auf der Zeitleiste zurück. |
| ABL_A150 | **Schallwand** | Stat. | – | – | AllyRow | 50 | 29 | Wirkt auf eigene Reihe; Schild für die eigene Reihe (15 % der max. HP); Harmonie +10. |
| ABL_A151 | **Donnerhall** | Spez. | 100 | 85 % | Enemies | 130 | 114 | Spezieller Schaden, Stärke 100, gegen alle Gegner; Anwender muss danach eine Runde aussetzen. |
| ABL_A152 | **Kampflied** | Stat. | – | – | Allies | 60 | 42 | Wirkt auf alle Verbündeten; ANG +1 für alle Verbündeten; Harmonie +10. |
| ABL_A153 | **Taktgeber** | Stat. | – | – | Ally | 50 | 24 | Wirkt auf einen Verbündeten; einen Verbündeten rückt 60 Ticks auf der Zeitleiste vor. |
| ABL_A154 | **Wiegenlied** | Stat. | – | 85 % | Single | 60 | 44 | Wirkt auf einen Gegner; das Ziel rückt 80 Ticks auf der Zeitleiste zurück; GES −1 für das Ziel. |
| ABL_A155 | **Resonanzkreis** | Stat. | – | – | Field | 50 | 32 | Erzeugt Klangfeld für 4 Runden. |
| ABL_A156 | **Fortissimo** | Spez. | 90 | 95 % | Single | 120 | 95 | Spezieller Schaden, Stärke 90, gegen einen Gegner; Harmonie +10. |

### 8.14 Schwerkraft (ABL_A157–A168)
Schwerkraft **ordnet das Feld neu**: Ziehen, Stoßen, Reihentausch (Umkehrfeld), Fesseln. Singularität zieht ein Ziel nach vorn und nimmt ihm Ausweichen – die Vorbereitung für jeden Physisch-Angreifer.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A157 | **Schwerefaust** | Phys. | 40 | 100 % | Single | 60 | 40 | Physischer Schaden, Stärke 40, gegen einen Gegner. |
| ABL_A158 | **Massezug** | Spez. | 45 | 100 % | Single | 80 | 60 | Spezieller Schaden, Stärke 45, gegen einen Gegner; zieht das Ziel in die Vorderreihe. |
| ABL_A159 | **Gravistoß** | Spez. | 60 | 100 % | Single | 100 | 75 | Spezieller Schaden, Stärke 60, gegen einen Gegner; stößt das Ziel in die Hinterreihe. |
| ABL_A160 | **Erdanziehung** | Phys. | 70 | 95 % | Single | 110 | 86 | Physischer Schaden, Stärke 70, gegen einen Gegner; Ziel kann 2 Runde(n) die Reihe nicht wechseln. |
| ABL_A161 | **Umkehrfeld** | Stat. | – | 90 % | Enemies | 50 | 25 | Wirkt auf alle Gegner; vertauscht die gegnerischen Reihen. |
| ABL_A162 | **Meteorsturz** | Phys. | 110 | 85 % | Single | 100 | 77 | Physischer Schaden, Stärke 110, gegen einen Gegner; benötigt eine Aufladerunde (sichtbar auf der Zeitleiste). |
| ABL_A163 | **Schwerkraftfeld** | Stat. | – | – | Field | 50 | 32 | Erzeugt Schwerefeld für 4 Runden. |
| ABL_A164 | **Bahnbrecher** | Spez. | 85 | 95 % | Row | 150 | 127 | Spezieller Schaden, Stärke 85, gegen eine gegnerische Reihe; stößt das Ziel in die Hinterreihe. |
| ABL_A165 | **Schwebe** | Stat. | – | – | Self | 50 | 30 | AUS +1 für sich selbst; Anwender wechselt die Reihe ohne Zeitkosten. |
| ABL_A166 | **Gewichtslast** | Stat. | – | 95 % | Single | 60 | 38 | Wirkt auf einen Gegner; GES −2 für das Ziel. |
| ABL_A167 | **Singularität** | Spez. | 95 | 90 % | Single | 140 | 120 | Spezieller Schaden, Stärke 95, gegen einen Gegner; zieht das Ziel in die Vorderreihe; AUS −1 für das Ziel. |
| ABL_A168 | **Implosion** | Spez. | 70 | 95 % | Enemies | 140 | 122 | Spezieller Schaden, Stärke 70, gegen alle Gegner; Ziel kann 1 Runde(n) die Reihe nicht wechseln. |

### 8.15 Arkan (ABL_A169–A180)
Arkan **bricht Regeln**: Typtabelle umkehren (Umkehrrune, angekündigt), Typ des Gegners ändern (Wandlungsglyphe), Fähigkeiten kopieren (Spiegelformel), Stufen stehlen (Formelraub). Arkan hat die meisten Status-Fähigkeiten (7) – Arkan ist ein Typ für Planer.

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_A169 | **Runenpfeil** | Spez. | 40 | 100 % | Single | 70 | 50 | Spezieller Schaden, Stärke 40, gegen einen Gegner; verfehlt nie. |
| ABL_A170 | **Glyphenschlag** | Phys. | 45 | 100 % | Single | 70 | 45 | Physischer Schaden, Stärke 45, gegen einen Gegner. |
| ABL_A171 | **Bannzeichen** | Spez. | 60 | 95 % | Single | 90 | 67 | Spezieller Schaden, Stärke 60, gegen einen Gegner; 20 % Chance auf Verflucht. |
| ABL_A172 | **Spiegelformel** | Stat. | – | 100 % | Single | 60 | 40 | Wirkt auf einen Gegner; kopiert die zuletzt vom Ziel eingesetzte Fähigkeit. |
| ABL_A173 | **Wandlungsglyphe** | Stat. | – | 100 % | Single | 60 | 40 | Wirkt auf einen Gegner; ändert den Typ von das Ziel für 2 Runden zu Arkan. |
| ABL_A174 | **Umkehrrune** | Stat. | – | – | Field | 70 | 50 | Kehrt die Typtabelle für 1 Runde(n) um (angekündigt). |
| ABL_A175 | **Siegelbruch** | Phys. | 80 | 95 % | Single | 130 | 106 | Physischer Schaden, Stärke 80, gegen einen Gegner; entfernt Schilde und positive Stufen von das Ziel. |
| ABL_A176 | **Formelraub** | Stat. | – | 90 % | Single | 50 | 31 | Wirkt auf einen Gegner; stiehlt die positiven Stufen des Ziels. |
| ABL_A177 | **Arkansturm** | Spez. | 100 | 85 % | Row | 140 | 119 | Spezieller Schaden, Stärke 100, gegen eine gegnerische Reihe. |
| ABL_A178 | **Glyphenkreis** | Stat. | – | – | Field | 50 | 24 | Erzeugt Glyphenfeld für 3 Runden. |
| ABL_A179 | **Mantra** | Stat. | – | – | Self | 60 | 40 | SAN +1 für sich selbst; SVE +1 für sich selbst. |
| ABL_A180 | **Fluchwort** | Stat. | – | 90 % | Single | 70 | 45 | Wirkt auf einen Gegner; verursacht Verflucht. |

---

## 9. Erwerb und Verteilung (Vorschau K29)

| Weg | Anteil an aktiven Fähigkeiten | Regel |
|---|---|---|
| Lernset (Level) | alle 180 erreichbar | 8–14 Einträge je Art; Einstiegsslots 1–2 des eigenen Typs ab Lv. 1 |
| Klangschriften | 90 von 180 | wiederverwendbar, nicht handelbar (CANON §18); je Typ 6 |
| Tutoren | 30 | an Fraktionen/Arenen gebunden (K47) |
| Vererbung | Ei-Fähigkeiten aus den Elternlernsets (K38) | – |
| Evolution | je Linie 1 Evolutionsfähigkeit beim Stufenwechsel | CANON §86 |

**Lernset-Regeln (Vorgabe für K29):** Jede Art lernt ≥ 60 % Fähigkeiten ihrer eigenen Typen, ≥ 2 Fähigkeiten eines Fremdtyps (Abdeckung, DR-08), mindestens eine Status-Fähigkeit bis Lv. 20 und die schwere Fähigkeit (Slot 6) ihres Primärtyps nicht vor Lv. 36. Signaturkonzepte aus dem Katalog (K20–K27) werden in K29/K30 auf konkrete Fähigkeiten abgebildet.

---

## 10. Validierung

`tools/gen_abilities.py validate` prüft:

| Regel | Inhalt |
|---|---|
| AB-01 | Anzeigename global eindeutig, keine Kollision mit Echo-Namen |
| AB-02 | Typ gültig (keine typlosen Fähigkeiten) |
| AB-03 | Effekt-DSL parsebar, Status existiert in `StatusEffects.csv` |
| AB-04 | Kategorie konsistent mit Stärke |
| AB-05 | Stärke ≤ 150 (Crescendo ≤ 200), Genauigkeit 500–1000 oder 0 |
| AB-06 | Ziel gültig |
| AB-07 | Budget und Zeitkosten entsprechen der Formel (keine Handwerte), Zeitkosten 50–200 |
| AB-08 | Crescendo-Budget 200–320 (K30) |
| AB-09 | Passive mit Auslöser (K29) |
| AB-10 | Feldfähigkeiten mit `Field.*`-Tag (K30) |
| AB-11 | Exakte Anzahl je Typ (12 / 6 / 2 / 2) |
| AB-12 | ≥ 3 Identitäts-Fähigkeiten je Typ (aktiv) |
| AB-13 | Kategorienmix je Typ (≥ 2 P, ≥ 2 S, ≥ 3 Status) |
| AB-14 | Endzahlen 180/90/30/30 (`--final`, ab K30) |

**Ergebnis K28:** 180 aktive Fähigkeiten, **0 Verstöße**. Kennzahlen: Ø Stärke der 111 Schadensfähigkeiten 66; Zielverteilung Single 101 · Row 14 · Enemies 14 · Self 19 · Field 16 · Ally/AllyRow/Allies 16.

---

## 11. Code

### 11.1 Daten (Core)

`UAbilityDefinition` (Primary Asset Type `Ability`) trägt Art, Typ-Tag, Kategorie, Stärke, Genauigkeit, Ziel, Zeitkosten, Budget, Effektliste (`FAbilityEffectSpec`), Auslöser (Passive) und Tags. Die Budgetformel ist als `constexpr` in `Aethris::Abilities` hinterlegt und per `static_assert` gegen Datenbeispiele geprüft (Funkenbiss 44 → 60, Esseneruption 114 → 130).

```cpp
namespace Aethris::Abilities
{
    constexpr int32 TimeCostFromBudget(int32 Budget)
    {
        const int32 Raw = (20 + Budget + 5) / 10 * 10;
        return Raw < 50 ? 50 : (Raw > 200 ? 200 : Raw);
    }
}
```

### 11.2 Ausführung (GF_Combat, Vorgabe für K31/K32)

```cpp
// Pseudocode – Ausführung einer aktiven Fähigkeit
void UCombatAbilityExecutor::Execute(const FCombatContext& Ctx, const UAbilityDefinition& A, FCombatantId User,
                                     const FTargetSet& Targets)
{
    Ctx.Timeline->Commit(User, A.TimeCost);                       // K31: Verzögerung aus Zeitkosten
    for (FCombatantId T : Targets)
    {
        const bool bHit = A.AccuracyPermille == 0 || Ctx.Rng.RollPermille(HitChance(Ctx, A, User, T));
        if (!bHit) { Ctx.Harmony->Add(User.Team, 5); continue; }   // DR-10: kein toter Zug
        if (A.Power > 0) Ctx.Damage->Apply(Ctx, A, User, T);        // K32: Faktorreihenfolge CANON §77
        for (const FAbilityEffectSpec& E : A.Effects)
            Ctx.Effects->Get(E.Op).Apply(Ctx, E, User, T);          // Primitiv-Registry (DR-25)
    }
    Ctx.Bus->Broadcast(TAG_Combat_AbilityResolved, FAbilityResolvedMessage{ User, A.GetPrimaryAssetId() });
}
```

### 11.3 Werkzeuge

| Datei | Zweck |
|---|---|
| `tools/abilities/abl.py` | DSL-Parser, Effektwerte, Budget, deutsche Regeltexte |
| `tools/abilities/abl_write.py` | schreibt eine Fähigkeitsart idempotent (IDs, Budget, Zeitkosten, Text) |
| `tools/authoring/abilities_active.py` | Quelle der 180 Aktiven (kompakt, je Typ 12) |
| `tools/gen_abilities.py` | Validator AB-01…14, Renderer, Kennzahlen |
| `tools/authoring/build_doc.py` | baut dieses Kapitel aus Vorlage + Daten |

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Alternativen verworfen |
|---|---|---|---|
| ADR-093 | Zeitkosten werden aus einem **Machtbudget** berechnet, nie handgesetzt | Ein Balancing-Hebel statt 330 Einzelwerte; Validator erkennt Abweichungen | Handgepflegte Kosten (driftet), feste Kostenklassen (zu grob) |
| ADR-094 | **Keine Abklingzeiten** auf aktiven Fähigkeiten | Zeitkosten tragen die Kosten; Abklingzeiten wären doppelte Bestrafung und schwer lesbar auf der Zeitleiste | Abklingzeiten (MMO-Gefühl), PP-artige Nutzungszähler (Clean-Room, Grind) |
| ADR-095 | Effekte als **Effekt-DSL** mit Primitiv-Registry | DR-25: Content ohne Code; Regeltexte aus derselben Quelle | Blueprint je Fähigkeit (nicht prüfbar), GAS-Effekt-Assets pro Fähigkeit (unübersichtlich) |
| ADR-096 | Jeder Typ besitzt 12 Aktive mit ≥ 2 physischen und ≥ 2 speziellen | Typwahl hängt nicht an ANG/SAN-Profil; Mono-Typ spielbar | Typen mit fester Kategorie (verengt Teambau) |
| ADR-097 | Ein Haupt-Status + Gift parallel; Starre mit 2 Runden Immunität | Lesbarkeit, Anti-Kette (DR-07), Gift-Identität | Beliebig viele Status (unlesbar) |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §97 | Fähigkeitsarten Aktiv 180 / Passiv 90 / Crescendo 30 / Feld 30 (= 330); IDs `ABL_A/P/U/F###`; Kampfset 4+1+1(+1); Repertoire ohne Vergessen; keine Abklingzeiten | LOCKED |
| §98 | Machtbudget V = Schaden + Σ Effektwerte; Zeitkosten = clamp(rund10(20+V), 50, 200); Zielfaktoren 1000/1400/1700; Effektwerttabelle K28 §3.2 | LOCKED (Effektwerte: Tuning in K63) |
| §99 | Effekt-DSL (Grammatik K28 §4), Primitiv-Registry in GF_Combat, generierte Regeltexte | LOCKED |
| §100 | 15 Status-Effekte mit Immunität je Typ (`StatusEffects.csv`); 1 Haupt-Status + Gift; Starre-Immunität 2 Runden | LOCKED (Zahlen PROVISIONAL → K32) |
| §101 | Aktive Fähigkeiten ABL_A001–A180, 12 je Typ, Slot-Schema, Validator AB-01…AB-14 | LOCKED |
| §10 | ADR-093 – ADR-097 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Fähigkeitssystem: Arten, IDs, Kampfset, Repertoire
- [x] Machtbudget und Zeitkosten als ein Rechenmodell (Python + C++ constexpr, bitgleich)
- [x] Effekt-DSL mit 42 Primitiva, generierte Regeltexte
- [x] 15 Status-Effekte mit Immunitäten, Quellen, Startwerten
- [x] 180 aktive Fähigkeiten (12 je Typ) als Daten, validiert (0 Verstöße)
- [x] Typ-Identität je Typ abgesichert (AB-12), Kategorienmix (AB-13)
- [x] Erwerbswege und Lernset-Regeln als Vorgabe für K29
- [x] Code: `UAbilityDefinition`, Budget-constexpr, Ausführungs-Pseudocode
- [x] ADR-093 – ADR-097, CANON §97–§101

➡️ **Nächstes Kapitel: K29 – Fähigkeiten II: Passive (ABL_P001–P090) und Lernsets aller 256 Arten.**
