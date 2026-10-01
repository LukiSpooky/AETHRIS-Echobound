# K32 · Kampfsystem II – Schaden, Status, Terrain und Kampfwetter

| Feld | Wert |
|---|---|
| Dokument | Kapitel 32 von 68 · Combat Guide, Teil V |
| Version | 1.0 |
| Owner | Lead Combat Designer |
| Mitwirkende | Balancing Analyst, Lead Gameplay Programmer, VFX Lead (Status-/Terrain-Lesbarkeit), Audio Lead, UX Lead (Schadensvorschau) |
| Baut auf | K17 (Typtabelle, Eigenklang, Faktorreihenfolge CANON §77), K18 (Werte, Stufen, Treffer CANON §79), K14 (Kampfwetter CANON §62), K28–K31 (Fähigkeiten, Status, Zeitleiste) |
| Status | ✅ Freigegeben |
| Im Repository | `tools/ref/aethris_combat.py` (`damage_chain`, Beispiele), `Plugins/GameFeatures/GF_Combat/…/Damage/DamageCalculator.h`, `Data/Combat/Terrains.csv` (15), `Data/Abilities/StatusEffects.csv` (final), `Data/World/WeatherTypeResonance.csv` |
| Neue Kanon-Einträge | CANON §114 (Schadensformel), §115 (Auflösungsreihenfolge), §116 (Status final), §117 (Terrain), §118 (Kampfwetter) |

---

## Inhalt

1. [Die Auflösung eines Treffers](#1-die-auflösung-eines-treffers)
2. [Die Schadensformel](#2-die-schadensformel)
3. [Beispielrechnungen](#3-beispielrechnungen)
4. [Treffer, Ausweichen, Volltreffer](#4-treffer-ausweichen-volltreffer)
5. [Status-Effekte – endgültige Regeln](#5-status-effekte--endgültige-regeln)
6. [Terrain](#6-terrain)
7. [Kampfwetter](#7-kampfwetter)
8. [Schilde, Heilung, Entzug, Rückschlag, Konter, Reflexion](#8-schilde-heilung-entzug-rückschlag-konter-reflexion)
9. [Vorschau und Lesbarkeit](#9-vorschau-und-lesbarkeit)
10. [Balancing-Prüfung](#10-balancing-prüfung)
11. [Code](#11-code)
12. [Tests](#12-tests)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Die Auflösung eines Treffers

Jede Fähigkeit wird pro Ziel in einer **festen Reihenfolge** aufgelöst. Die Reihenfolge ist Teil der Regeln (CANON §115), weil sie entscheidet, ob ein Konter vor oder nach einem Schild greift, ob Lebensentzug den vollen Schaden oder nur den HP-Schaden heilt usw.

```
 Fähigkeit gewählt (K31 §5)
   │
   ├─ 1 Zielbestimmung        Formation, Spott (Taunt), Trugbild (Decoy fängt ab), Reihenauflösung
   ├─ 2 Reflexionsprüfung     Reflect(Kategorie) des Ziels? → Fähigkeit trifft den Anwender (einmal)
   ├─ 3 Trefferwurf           Treffer‰ = clamp(Gen × PRÄ_eff / AUS_eff, 500, 1000); SureHit/Reveal
   │      └─ Fehlschlag → +5 Harmonie (DR-10), Ende
   ├─ 4 Volltreffer-Wurf      Stufe 0–3: 42 / 125 / 250 / 500 ‰
   ├─ 5 Schaden               Basis × Eigenklang × Typ × Wetter × Krit × Formation × Sonstige
   ├─ 6 Schild                Schaden zuerst auf Schild (außer IgnoreShield); Gebrochen zerstört Schild
   ├─ 7 HP                    Rest auf HP; HP ≤ 0 → verklungen (nach Schritt 10)
   ├─ 8 Effekte               DSL-Effekte in Datenreihenfolge (Status, Stufen, Delay, Push …)
   ├─ 9 Anwender-Folgen       Drain (aus HP+Schild-Schaden), Recoil, Exhaust, Charged verbraucht
   ├─ 10 Reaktionen           Konter des Ziels, Passive (HitTaken, ContactTaken, LowHP), Starre-Bruch durch Glut
   └─ 11 Harmonie & Kombo     Harmonie-Gewinn, Kombo-Prüfung (K33), Ereignis Combat.AbilityResolved
```

**Mehrfachtreffer** (`Multi`) durchlaufen die Schritte 3–8 je Treffer; Volltreffer werden je Treffer gewürfelt; Reaktionen (Schritt 10) lösen nur einmal nach dem letzten Treffer aus. **Flächenfähigkeiten** lösen Ziele in Zeitleisten-Reihenfolge auf (vorderstes zuerst).

---

## 2. Die Schadensformel

```
Basis       = ⌊ Stärke × A_eff × (L + 10) / (V_eff × 180) ⌋ + 2
Schaden     = Basis × Eigenklang × Typfaktor × Wetter × Volltreffer × Formation × Sonstige   (je ⌊…⌋, Promille)
Mindestwert = 1
```

| Größe | Bedeutung |
|---|---|
| A_eff / V_eff | physisch: ANG/VER; speziell: SAN/SVE; mit Stufenfaktor (CANON §79); Brand: ANG ×0,75 (nur physisch) |
| L | Level des Anwenders (1–100) |
| Eigenklang | ×1,25, wenn der Fähigkeitstyp einem Typ des Anwenders entspricht; Boni (Passive „Strahlkraft“ u. a.) bis ×1,4 |
| Typfaktor | Produkt der Zieltypen aus `TypeChart.csv` (2560 … 250 ‰) |
| Wetter | `WeatherTypeResonance.csv` (800–1300 ‰) |
| Volltreffer | ×1,5; ignoriert ungünstige Stufen (eigene negative A-Stufen, positive V-Stufen des Ziels) |
| Formation | Hinterreihen-Schutz (K33) |
| Sonstige | Produkt aus Passiven (TypePower, Resist), Terrain-Boost, Charged (×1,5), WeatherBoost/TerrainBoost (×1,5), Duell-Fläche (×0,8) |

### 2.1 Herleitung des Divisors 180

Der Divisor bestimmt, wie viele Treffer ein Echo aushält. Ziel aus DR-11: Ein Wildkampf zweier gleichstufiger Echos soll als reiner Schlagabtausch ~8 Züge dauern (mit Bindung und Statuszügen 60–120 s). Die Simulation in K31 §13 (400 Duelle je Level, echte Katalogwerte) liefert mit 180 im Mittel 7,6–8,6 Züge auf allen Leveln. Kontrollrechnung (Lv. 50, Kernwerte 87, Stärke 80, neutral, ohne Eigenklang): Basis 28 = 15 % von 190 HP; mit Eigenklang 35 = 18 %; sehr effektiv mit Eigenklang 56 = 29 %.

| Divisor | Ø Züge 1v1 (Lv. 50) | Bewertung |
|---|---|---|
| 84 (Entwurf) | 4,3 | zu kurz: Zeitleiste und Status wären bedeutungslos |
| 140 | 6,3 | knapp |
| **180** | **8,2** | Zielband, Status/Position lohnen sich |
| 220 | ~10 | zu zäh in Wildkämpfen |

### 2.2 Keine Schadensstreuung

AETHRIS würfelt **keinen Schadensbereich**. Der Schaden ist deterministisch; Zufall gibt es nur beim Treffer (gedeckelt 50–100 %), beim Volltreffer und bei Status-Chancen (DR-07). Folgen:

- Die **Vorschau zeigt exakte Zahlen** (K32 §9) – „Diese Fähigkeit verursacht 42 Schaden (63 bei Volltreffer)“.
- Planung über mehrere Züge ist verlässlich („zwei Treffer und Brand reichen“) – Säule S3 „schwer zu meistern“ entsteht aus Planung, nicht aus Würfelglück.
- Ranked-Kämpfe sind weniger varianzgetrieben (Elo-Streuung, K61).

### 2.3 Sonderfälle

| Fall | Regel |
|---|---|
| Duell und Flächenfähigkeit | Row/Enemies treffen das einzige Ziel mit ×0,8 |
| Mehrfachtreffer | Stärke gilt je Treffer; Volltreffer je Treffer |
| Typwechsel (TypeChange, Wandelhaut) | Typfaktor nutzt den aktuellen Typ; Eigenklang nutzt den aktuellen Typ des Anwenders |
| Tabellenumkehr (Umkehrrune, Glyphenfeld) | 1600 → 625, 625 → 1600, 400 → 1600, 1000 bleibt (CANON §77) |
| Feldklang „Finsternis“ | Licht- und Leere-Zeilen der Typtabelle getauscht |
| Fester Schaden | Status-Ticks, Wetter-/Terrain-Runden-Schaden und Meteore (Sternensturz) rechnen in Promille der Max-HP, nicht über die Formel |
| Verwirrende Selbsttreffer | existieren nicht (keine Verwirrung im Spiel, DR-07) |

---

## 3. Beispielrechnungen

Alle Werte mit Anlage 7, ohne Schliff, Persönlichkeit neutral; erzeugt aus den Katalog- und Fähigkeitsdaten (`aethris_combat.example_table()`).

| Angreifer → Ziel (Lv.) | Fähigkeit (Stärke, Kat.) | Basis | ×Eigenklang | ×Typ | ×Wetter | ×Krit | ×Formation | ×Sonstige | Schaden | % Ziel-HP |
|---|---|---|---|---|---|---|---|---|---|---|
| Fernwyn → Brokkar (20) | Saugwurzel (60, Spec.) | 11 | → 13 | 1600‰ → 20 | 1000‰ → 20 | → 20 | 1000‰ → 20 | → 20 | **20** | 19 % |
| Torgrath → Zephyrion (36) | Felsrammen (60, Phys.) | 20 | → 25 | 1600‰ → 40 | 1000‰ → 40 | → 40 | 1000‰ → 40 | → 40 | **40** | 28 % |
| Sengrath → Kjalmur (50) | Esseneruption (100, Spec.) | 26 | → 32 | 1000‰ → 32 | 1200‰ → 38 | → 38 | 1000‰ → 38 | → 38 | **38** | 18 % |
| Klirrathan → Uvasil (60) | Prismenfächer (65, Spec.) | 27 | → 33 | 1600‰ → 52 | 1000‰ → 52 | → 78 | 1000‰ → 78 | → 78 | **78** | 33 % |
| Nimbaroth → Ignavor (70) | Himmelszorn (75, Spec.) | 30 | → 37 | 1000‰ → 37 | 1200‰ → 44 | → 44 | 1000‰ → 44 | → 44 | **44** | 17 % |
| Snevrik → Solaryx (45) | Frostbiss (60, Phys.) | 24 | → 30 | 625‰ → 18 | 1200‰ → 21 | → 21 | 750‰ → 15 | → 15 | **15** | 8 % |
| Tilgrath → Thaelarch (55) | Hohlklang (60, Spec.) | 23 | → 28 | 1000‰ → 28 | 1100‰ → 30 | → 30 | 1000‰ → 30 | → 30 | **30** | 11 % |
| Pyroluth → Nubiluna (40) | Feueratem (95, Spec.) | 33 | → 41 | 1000‰ → 41 | 800‰ → 32 | → 32 | 1000‰ → 32 | → 25 | **25** | 13 % |

### 3.1 Referenztabelle Stärke × Faktor

Schaden gegen ein durchschnittliches Echo gleicher Stufe (alle Basiswerte 75, Anlage 7, Lv. 50) – die Faustregel für Designer und für die Fähigkeits-Tooltips im Erklärmodus:

| Stärke | neutral | +Eigenklang | sehr eff. | Eigenkl.+sehr eff. | Eigenkl.+×2,56 | resistiert | gedämpft |
|---|---|---|---|---|---|---|---|
| 40 | 15 (8 %) | 18 (9 %) | 24 (13 %) | 28 (15 %) | 46 (25 %) | 9 (4 %) | 6 (3 %) |
| 55 | 20 (10 %) | 25 (13 %) | 32 (17 %) | 40 (21 %) | 64 (35 %) | 12 (6 %) | 8 (4 %) |
| 70 | 25 (13 %) | 31 (17 %) | 40 (21 %) | 49 (26 %) | 79 (43 %) | 15 (8 %) | 10 (5 %) |
| 85 | 30 (16 %) | 37 (20 %) | 48 (26 %) | 59 (32 %) | 94 (51 %) | 18 (9 %) | 12 (6 %) |
| 100 | 35 (19 %) | 43 (23 %) | 56 (30 %) | 68 (37 %) | 110 (60 %) | 21 (11 %) | 14 (7 %) |
| 120 | 42 (23 %) | 52 (28 %) | 67 (36 %) | 83 (45 %) | 133 (73 %) | 26 (14 %) | 16 (8 %) |
| 150 | 52 (28 %) | 65 (35 %) | 83 (45 %) | 104 (57 %) | 166 (91 %) | 32 (17 %) | 20 (10 %) |
| 180 | 62 (34 %) | 77 (42 %) | 99 (54 %) | 123 (67 %) | 197 (108 %) | 38 (20 %) | 24 (13 %) |

Referenz-Echo Lv. 50: HP 182, Kernwerte 87.

Faustregeln: Eine 70er-Fähigkeit mit Eigenklang nimmt einem gleichwertigen Gegner etwa ein Fünftel seiner HP; ein sehr effektiver Treffer mit Eigenklang etwa ein Drittel; erst der Vierfach-Schwachpunkt (×2,56) mit schweren Fähigkeiten erlaubt Ein-Treffer-Ergebnisse.

### 3.2 Lesehilfe zu den Beispielen

**Lesehilfe:**
- *Fernwyn → Brokkar:* Blüte gegen Stein ist sehr effektiv; trotzdem kostet ein Treffer nur 19 % – auf Lv. 20 entscheidet ein Typvorteil keinen Kampf in einem Zug.
- *Sengrath → Kjalmur:* Glut gegen Frost/Stein ergibt 1600 × 625 = 1000 ‰ – Doppeltypen neutralisieren sich. Die Hitzewelle (×1,2) macht den Unterschied.
- *Klirrathan → Uvasil:* Kristall gegen Leere/Frost = 1600 × 1000; Volltreffer ×1,5 → 32 % HP mit einer Flächenfähigkeit.
- *Nimbaroth → Ignavor:* Himmelszorn trifft zweimal (je 44); insgesamt 35 % der HP aller Gegner – ein Crescendo, das ein Trio-Team spürbar schwächt, aber nicht auslöscht.
- *Snevrik → Solaryx:* Frost gegen Licht/Glut ist resistiert (625 ‰); Solaryx steht in der Hinterreihe (Formation 750 ‰) → 8 %. Positionierung und Typ wirken zusammen.
- *Pyroluth → Nubiluna:* Regen schwächt Glut (×0,8), Nubilunas Passive (Resist, hier ×0,8 angenommen) halbiert fast den Schaden.

---

## 4. Treffer, Ausweichen, Volltreffer

| Regel | Wert |
|---|---|
| Treffer (‰) | clamp(Genauigkeit × PRÄ_eff / AUS_eff, 500, 1000) (CANON §79) |
| Genauigkeit 0 | kein Wurf (Selbst, Verbündete, Feld) |
| SureHit | ignoriert Wurf und Ausweichen; nicht gegen Decoy (Trugbild fängt dennoch) |
| Reveal (Licht) | AUS-Stufen des Ziels für 2 Züge 0; Tarnung/Trugbild enden |
| Geblendet | PRÄ −2 Stufen |
| Fehlschlag | +5 Harmonie für die eigene Seite (DR-10); Anzeige „verfehlt“ mit Ton |
| Volltreffer-Stufen | 0: 42 ‰ · 1: 125 ‰ · 2: 250 ‰ · 3: 500 ‰ (max.) |
| Volltreffer-Quellen | Crit(n) in Fähigkeiten, Passive, Items (K40) – Summe auf Stufe 3 gedeckelt |
| Volltreffer-Wirkung | ×1,5; ignoriert ungünstige Stufen; nicht gegen Schild-Effekte (Schild absorbiert normal) |

---

## 5. Status-Effekte – endgültige Regeln

K28 hat die 15 Status mit Startwerten eingeführt; hier werden sie mit Zahlen festgeschrieben. Dauern zählen **eigene Züge des Betroffenen** (CANON §109).

| DisplayName | ImmuneType | DurationTurns | Stacking | TickDamagePermilleMaxHP | StatMod | TimeCostMod | ExtraRule | CounterPlay |
|---|---|---|---|---|---|---|---|---|
| Brand | Ember | 3 | nein | 60 | Attack×750 (nur physisch) |  | Flut-Treffer löscht | Reinigen; Regen; Flutfeld |
| Ausgetrocknet | Tide | 3 | nein | 0 |  | Flut-Fähigkeiten +20 | erhaltene Heilung ×500 | Regen; Flutfeld; Reinigen |
| Rückstoß | Stone | 0 | nein | 0 |  |  | Sofort: in die Hinterreihe; nächster Reihenwechsel +30 Zeitkosten | Bind/Wurzelgriff; Stein immun |
| Verlangsamt | Storm | 3 | nein | 0 |  | ×1300 | – | Haste hebt auf; Reinigen |
| Welke | Bloom | 3 | nein | 0 | Defense −1 Stufe bei Anwendung |  | Regen/Heilung über Zeit wirkungslos | Überwuchs; Reinigen |
| Starre | Frost | 1 | nein | 0 |  |  | Nächster Zug entfällt (+100 Ticks); Glut-Treffer löst sofort; danach 2 Züge immun | Glut-Treffer; Reinigen |
| Entzug | Void | 3 | nein | 0 |  |  | Keine Harmonie-Erzeugung durch dieses Echo; positive Stufen steigen nicht | Licht-Reinigen |
| Geblendet | Light | 3 | nein | 0 | Precision −2 Stufen |  | – | Nebel-/Stillefeld; Reinigen |
| Vergiftet | Venom | 0 | 1–5 Stapel | 30 je Stapel |  |  | Dauer bis Kampfende oder Reinigung; Reservewechsel halbiert Stapel (abgerundet) | Reinigen; Wechsel |
| Erschüttert | Metal | 0 | nein | 0 |  |  | Sofort: +50 Ticks (zählt in Fremdverzögerungs-Deckel) | Schild verhindert |
| Furcht | Spirit | 2 | nein | 0 | Attack/SpAttack −1 Stufe |  | Aktion gegen den Verursacher kostet +30 Zeitkosten | Klang-Harmonie ≥ +20 beendet; Reinigen |
| Gebrochen | Crystal | 3 | nein | 0 | Defense/SpDefense −2 Stufen |  | Aktive Schilde zerbrechen sofort | Neuer Schild nach Ablauf; Reinigen |
| Verstummt | Sound | 2 | nein | 0 |  |  | Keine Sound-Fähigkeiten, keine Status-Fähigkeiten, kein Crescendo; Sound-Ankündigungen brechen ab | Reinigen; Ablauf |
| Schwebend | Gravity | 2 | nein | 0 | Evasion +1 / Precision −1 |  | Kein Reihenwechsel; Ground-Fähigkeiten verfehlen | Schwerefeld; Ablauf |
| Verflucht | Arcane | 3 | nein | 0 |  | +20 | Positive Effekte auf das Ziel (Heilung, Stufen, Schilde) halbiert | Licht-Reinigen |

### 5.1 Anwendungsregeln

1. **Haupt-Status:** Ein Echo trägt höchstens einen Haupt-Status (alle außer Vergiftet und den Sofort-Effekten Rückstoß/Erschüttert). Ein neuer Haupt-Status ersetzt den alten **nicht** – er schlägt fehl (Anzeige „hat bereits Brand“). Ausnahme: Starre ersetzt Verlangsamt (Frost-Steigerung).
2. **Vergiftet** stapelt bis 5 und läuft parallel zum Haupt-Status (Gift-Identität, ADR-097).
3. **Immunität:** Typ-Immunität (je Typ ein Status), Passive `Immune(X)`, Nach-Starre-Immunität (2 Züge).
4. **Chancen:** Status-Chancen der Fähigkeiten sind absolute Promille; Passive „Giftdrüsen“ (×1,5) und Glutboden (+100 ‰ für Brand) modifizieren; Deckel 1000 ‰.
5. **Reinigen** entfernt Haupt-Status und alle Gift-Stapel; nicht Stufen.
6. **Wechsel in die Reserve** beendet Haupt-Status **nicht** (anders als Stufen) – Ausnahme Furcht und Schwebend; Gift-Stapel halbieren sich.
7. **Kampfende:** Alle Status enden, außer im Eisernen Wärter (Status bleiben bis Klangbrunnen, K16).

### 5.2 Wert eines Status (Kontrolle des Machtbudgets)

| Status | Erwartete Wirkung bei 100 % | MP-Wert (K28) | Bewertung |
|---|---|---|---|
| Brand | 3 × 6 % HP + ANG ×0,75 für 3 Züge ≈ 18 % HP + ~20 % weniger physischer Schaden | 45 | angemessen (ein 70er-Treffer ≈ 15–18 % HP) |
| Vergiftet (1 Stapel) | 3 % HP je Zug bis Kampfende (Ø 6 Züge) ≈ 18 % | 20 je Stapel | günstig, aber durch Wechsel/Reinigen konterbar |
| Starre | ein ganzer Zug (+100 Ticks) | 60 | teuerster Status, Anti-Kette |
| Furcht | ANG/SAN −1 (×0,8) für 2 Züge + Zeitkosten-Strafe | 45 | angemessen |
| Verstummt | Status/Sound/Crescendo gesperrt für 2 Züge | 45 | stark gegen Support/Klang |

### 5.3 Status-Wechselwirkungen

| Kombination | Ergebnis |
|---|---|
| Brand + Flut-Treffer | Brand endet sofort (vor Schaden des Flut-Treffers) |
| Starre + Glut-Treffer | Starre endet sofort, Schaden normal; 2 Züge Starre-Immunität beginnen |
| Verlangsamt → Starre | Starre ersetzt Verlangsamt (Frost-Steigerung) |
| Gebrochen + Schild-Fähigkeit | Schild entsteht nicht, solange Gebrochen wirkt |
| Welke + Regen/Überwuchs | Überwuchs-Terrain beendet Welke; Regen-Effekte bleiben wirkungslos, bis Welke endet |
| Verstummt + Ankündigung (Sound) | Ankündigung bricht ab; bei Crescendo 50 % Harmonie zurück |
| Schwebend + Erdgrollen/Bergsturz (Ground) | verfehlt automatisch |
| Schwebend + Schwerefeld | Schwebend endet beim Feldbeginn |
| Furcht + Angriff auf Verursacher | +30 Zeitkosten; Angriffe auf andere Ziele ohne Strafe |
| Vergiftet + Fäulniskreis (Passive) | neue Stapel springen auf den nächsten Gegner |
| Geblendet + Reveal des Gegners | heben sich nicht auf: Reveal senkt Ausweichen des Ziels, Geblendet die eigene Präzision |
| Entzug + Kombo | Kombos dieses Echos zählen, erzeugen aber keine Harmonie |
| Verflucht + Heilung | Heilung halbiert (vor HealPower) |

---

## 6. Terrain

Ein Terrain belegt das **ganze Kampffeld**. Es entsteht durch Fähigkeiten (`Terrain(X,n)`), Arena-Mechaniken (CANON §51) oder Feldklänge; Dauer in **Runden** (100 Ticks).

| DisplayName | Type | BoostType | BoostPermille | MalusType | MalusPermille | RoundEffect | SpecialRule | EndedBy |
|---|---|---|---|---|---|---|---|---|
| Glutboden | Ember | Ember | 1200 |  | 1000 | Nicht-Glut-Echos der Vorderreihe −3 % Max-HP je Runde | Brand-Chancen +100 ‰ (absolut) | Regen, Flutfeld |
| Glutsand | Ember | Ember | 1200 | Frost | 900 | Nicht-Glut/Stein-Echos bodennah −3 % Max-HP je Runde | Grabende Echos (Burrower) AUS +1 Stufe | Regen, Flutfeld |
| Überwuchs | Bloom | Bloom | 1200 |  | 1000 | Bodennahe Echos heilen 4 % Max-HP je Runde | Welke wirkungslos; Bind-Dauer +1 | Glutboden, Glutsand |
| Sumpf | Venom | Venom | 1200 |  | 1000 | – | Bodennahe Nicht-Gift/Flut-Echos GES −1 Stufe; Gift-Treffer +1 Stapel | Überwuchs, Sonne (Hitzewelle) |
| Flutfeld | Tide | Tide | 1200 | Ember | 800 | Brand endet bei Feldbeginn | Reihenwechsel −20 Zeitkosten; Push/Pull-Fähigkeiten verfehlen nie | Glutboden (verdampft beides) |
| Eisfläche | Frost | Frost | 1200 |  | 1000 | – | Kontakt-Fähigkeiten PRÄ −1 Stufe (rutschig); Push stößt 1 Reihe weiter | Glutboden, Glutsand, Hitzewelle |
| Sturmfeld | Storm | Storm | 1200 |  | 1000 | – | Haste-Effekte +20 Ticks; Schwebend-Dauer +1 | Schwerefeld |
| Kristallfeld | Crystal | Crystal | 1200 | Light | 900 | – | Reflect-Effekte wirken zweimal; Charged-Bonus ×1,25 statt ×1,5 gegen Kristall-Ziele | Schwerefeld, Missklang |
| Klangfeld | Sound | Sound | 1200 |  | 1000 | Harmonie +3 je Runde für beide Seiten | Harmonie-Gewinn ×1,5 | Stillefeld, Missklang |
| Schwerefeld | Gravity | Gravity | 1200 |  | 1000 | – | Schwebend unmöglich (endet); Flier verlieren AUS-Bonus; Reihenwechsel +20 Zeitkosten | Sturmfeld |
| Glyphenfeld | Arcane | Arcane | 1200 |  | 1000 | – | In der letzten Runde des Feldes ist die Typtabelle umgekehrt (angekündigt, CANON §77) | Stillefeld |
| Stillefeld | Void | Void | 1100 | Sound | 800 | – | Kein Harmonie-Gewinn; Feldklänge ruhen; Crescendo-Ankündigungen nicht möglich | Klangfeld, Lichtfeld |
| Lichtfeld | Light | Light | 1200 | Spirit | 900 | – | Positive AUS-Stufen wirkungslos; Decoy/Trugbilder enden | Nebelfeld, Stillefeld |
| Nebelfeld | Spirit | Spirit | 1200 | Light | 900 | – | Hinterreihe AUS +1 Stufe; Fernkampf auf Hinterreihe PRÄ −1 Stufe | Lichtfeld, Sturmfeld |
| Missklang-Terrain | Void | Void | 1100 | Crystal | 900 | – | Harmonie-Gewinn halbiert; Klang-Fähigkeiten +20 Zeitkosten | Klangfeld |

### 6.1 Terrain-Regeln

| Regel | Wert |
|---|---|
| Gleichzeitig | genau ein Terrain; ein neues ersetzt das alte (gleiches Terrain: Dauer wird erneuert) |
| Beendet durch | Ablauf, gegnerisches Terrain der Spalte „EndedBy“ endet sofort und **legt sich nicht** (Neutralisation) |
| Bodennah | Echos ohne Schwebend und ohne Merkmal Flier |
| Runden-Effekte | zu Beginn jeder globalen Runde (Tick-Vielfache von 100), in Zeitleisten-Reihenfolge |
| Arena-Terrains | dauerhaft (Arenen-Mechanik), können durch Fähigkeiten für deren Dauer überlagert werden; danach kehrt das Arena-Terrain zurück |
| Darstellung | Bodentextur-Overlay (Niagara-Decal, K58), Rand-Symbol, eigener Ambient-Layer (K55) |

### 6.2 Terrain und Wetter

| Wetter | Terrain | Wechselwirkung |
|---|---|---|
| Regen | Glutboden, Glutsand | Terrain endet bei Wetterbeginn bzw. kann nicht gelegt werden |
| Regen | Flutfeld | Flutfeld-Dauer +1 Runde |
| Hitzewelle | Eisfläche, Sumpf | Terrain endet bei Wetterbeginn |
| Hitzewelle | Glutboden | Runden-Schaden 4 % statt 3 % |
| Schnee | Eisfläche | Eisfläche kann von Glutboden nicht neutralisiert werden, solange es schneit |
| Gewitter | Sturmfeld | Blitzschlag alle 3 statt 4 Runden |
| Nebel | Nebelfeld | Hinterreihe AUS +2 statt +1 |
| Nebel | Lichtfeld | Lichtfeld-Dauer −1 Runde |
| Aurora | Klangfeld | Harmonie +8 statt +3 je Runde |
| Aschefall | Stillefeld | Stillefeld unbeendbar durch Klangfeld |
| Resonanzsturm | jedes Terrain | Terrain-Boost 1300 statt 1200 ‰ |
| Sandsturm | Glutsand | Runden-Schaden der beiden Effekte addiert (max. 7 %) |

Diese Wechselwirkungen sind in `Terrains.csv`/`WeatherTypeResonance.csv` nicht als Freitext, sondern als benannte Regel-Primitiva hinterlegt (`Terrain.Rule.*`, `Weather.Rule.*`), damit sie testbar bleiben.

---

## 7. Kampfwetter

Ein Kampf übernimmt das **aktuelle Weltwetter** der Zone (K14, deterministischer Fahrplan). Wetterfähigkeiten (`Weather(X,n)`) überschreiben es lokal für n Runden; danach kehrt das Weltwetter zurück.

| Wetter | Typ-Resonanz (Angreifer) | Sonderregel im Kampf (je Runde) |
|---|---|---|
| Klar (W01) | – | – |
| Regen (W02) | Flut 1,2 · Blüte 1,1 · Glut 0,8 | Brand-Dauer zusätzlich −1 je Runde (Regen löscht, ohne Zufall) |
| Gewitter (W03) | Sturm 1,2 · Flut 1,1 · Glut 0,9 | alle 4 Runden Blitzschlag: Metall-Echos −6 % Max-HP, Sturm-Seite +10 Harmonie |
| Nebel (W04) | Geist 1,2 · Leere 1,1 · Licht 0,9 | Fernkampf (Nicht-Kontakt) auf Hinterreihe PRÄ −1 Stufe |
| Schnee (W05) | Frost 1,2 · Blüte/Glut 0,9 | Nicht-Frost GES −5 % |
| Hitzewelle (W06) | Glut 1,2 · Licht 1,1 · Frost 0,8 · Flut 0,9 | Ausgetrocknet-Chancen +100 ‰ |
| Sandsturm (W07) | Stein 1,2 · Schwerkraft 1,1 | Nicht Stein/Metall/Schwerkraft −4 % Max-HP je Runde |
| Aurora (W08) | Licht/Klang 1,2 · Arkan 1,1 · Leere 0,8 | +5 Harmonie je Runde beide Seiten |
| Aschefall (W09) | Leere 1,2 · Glut 1,1 · Blüte 0,8 | PRÄ −1 Stufe außer Glut/Leere |
| Resonanzsturm (W10) | alle 1,1 · Klang 1,3 | Harmonie-Gewinn ×2, Crescendo-Kosten −25 % |

**Ranked:** immer Klar (CANON §62); Wetterfähigkeiten wirken normal. **Unter Tage** (R09, Höhlen): nur Resonanzsturm und Fähigkeitswetter. Die „pro Zug“-Formulierungen aus K14 gelten als **pro Runde** (CANON §109).

---

## 8. Schilde, Heilung, Entzug, Rückschlag, Konter, Reflexion

| Mechanik | Regel |
|---|---|
| Schild | Wert in % Max-HP des Trägers; absorbiert Schaden vor HP; mehrere Schilde addieren sich bis 50 % Max-HP; Dauer bis verbraucht oder 3 eigene Züge |
| Heilung | % Max-HP × HealPower; Verflucht halbiert; Ausgetrocknet ×0,5; kann Max-HP nicht überschreiten |
| Regen | zu Beginn jedes eigenen Zuges; Welke blockiert |
| Drain | heilt Anteil des verursachten Schadens (HP + Schild) |
| Recoil | Anteil des verursachten Schadens; kann den Anwender verklingen lassen |
| Counter | löst nach dem Treffer aus (Schritt 10), Schaden = Anteil des erlittenen Schadens, Typ der Konter-Fähigkeit, ignoriert Ausweichen; einmal je Runde |
| Reflect | Schritt 2: Fähigkeit trifft den Anwender mit dessen Werten; danach verbraucht |
| Revive | nur auf Reserve- oder verklungene Echos der Seite; HP-Anteil wie angegeben; 1× je Echo und Kampf |
| Decoy | fängt den nächsten Einzelziel-Angriff vollständig ab; Flächen treffen Trugbild nicht |

---

## 9. Vorschau und Lesbarkeit

Weil Schaden deterministisch ist, zeigt die Fähigkeitsauswahl **genaue Werte**:

```
┌─ Feueratem ─────────────────── Glut · Speziell · Zeit 120 ─┐
│ Ziel: Kjalmur          Treffer 90 %                         │
│ Schaden 42  (Volltreffer 63)        Kjalmur HP ███████░░ 61 %│
│ ×1,25 Eigenklang · ×1,0 Typ (●○) · ×1,2 Hitzewelle           │
│ 30 % Brand · Kjalmur: nicht immun                           │
│ Zeitleiste: nächster Zug nach Uvlet (Geisterposition)       │
└─────────────────────────────────────────────────────────────┘
```

- Typfaktor-Anzeige ab Kodex-Stufe 2 der Zielart (Entspannt: immer) – sonst „?“ (CANON §78).
- Bei unbekannten Passiven des Ziels zeigt die Vorschau den Schaden **ohne** sie und markiert „± unbekannt“.
- Status-Symbole sind Form + Farbe + Kurzname; Ticks zeigen fliegende Zahlen in Statusfarbe (DR-24).

---

## 10. Balancing-Prüfung

| Prüfung | Ergebnis | Kapitel |
|---|---|---|
| Kampflänge 1v1, Level 5–100 | 7,6–8,6 Züge, levelunabhängig | K31 §13 |
| Stärkster Einzeltreffer (Lv. 50, Stärke 120, Eigenklang, ×2,56, Krit, +4 SAN gegen −4 SVE) | > 100 % HP – absichtlich möglich, aber nur mit 4+ Vorbereitungszügen | K63 |
| Typischer sehr effektiver Treffer (Eigenklang) | 25–35 % HP | §3 |
| Status-Wert vs. MP | Brand, Gift, Starre im Band 0,8–1,2 eines gleichteuren Treffers | §5.2 |
| Terrain-Boost 1,2 | entspricht etwa einer +1-Stufe für einen Typ; bewusst schwächer als Wetter-Extreme (1,3) | §6 |

---

## 11. Code

### 11.1 `Aethris::Damage` (constexpr)

```cpp
namespace Aethris::Damage
{
    constexpr int32 Base(int32 Power, int32 Attack, int32 Defense, int32 Level)
    {
        return int32(int64(Power) * Attack * (Level + 10) / (int64(Defense > 0 ? Defense : 1) * 180)) + 2;
    }
    constexpr int32 Compute(const FChainInput& In); // Basis → Eigenklang → Typ → Wetter → Krit → Formation → Sonstige
    static_assert(Base(80, 87, 87, 50) == 28);
}
```

### 11.2 Auflösungs-Pipeline (GF_Combat)

```cpp
void UCombatAbilityExecutor::ResolveOnTarget(FCombatContext& Ctx, const UAbilityDefinition& A, FCombatant& User, FCombatant& Target)
{
    FCombatant* T = Ctx.Targeting->Redirect(User, Target, A);                 // 1 Taunt, Decoy
    if (T->ConsumeReflect(A.Category)) { T = &User; }                          // 2 Reflexion
    if (A.AccuracyPermille && !A.HasEffect(TEXT("SureHit")) &&
        !Ctx.Rng.ChancePermille(HitChance(Ctx, A, User, *T))) { Ctx.Harmony->Add(User.Side, 5); return; }  // 3
    const int32 Hits = Ctx.Effects->HitCount(A, Ctx.Rng);
    int32 Dealt = 0;
    for (int32 H = 0; H < Hits; ++H)
    {
        const bool bCrit = Ctx.Rng.ChancePermille(Aethris::Damage::CritChancePermille[CritStage(A, User)]);  // 4
        const int32 Dmg = Aethris::Damage::Compute(Ctx.BuildChain(A, User, *T, bCrit));                     // 5
        Dealt += Ctx.Health->ApplyDamage(*T, Dmg, A.HasEffect(TEXT("IgnoreShield")));                       // 6–7
        Ctx.Effects->ApplyOnHit(Ctx, A, User, *T);                                                          // 8
    }
    Ctx.Effects->ApplyUserConsequences(Ctx, A, User, Dealt);                                                // 9
    Ctx.Reactions->Fire(Ctx, A, User, *T, Dealt);                                                           // 10
    Ctx.Harmony->OnResolved(Ctx, A, User, *T, Dealt);                                                       // 11 (K33)
}
```

### 11.3 Daten-Import

`Terrains.csv` → `UTerrainDefinition` (Primary Asset `Terrain`), `StatusEffects.csv` → `UStatusEffectDefinition` (`Status`). Die Sonderregeln in den Spalten `SpecialRule`/`ExtraRule` verweisen auf benannte Primitiva im Combat-Registry (`Terrain.Rule.*`, `Status.Rule.*`); der Import scheitert, wenn ein Name keinem Primitiv entspricht.

---

## 12. Tests

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Combat.Damage.Base` | Formel-Stützstellen (static_assert + 200 Tabellenwerte) |
| `…Damage.PythonParity` | 50.000 Zufallsketten gegen `damage_chain` |
| `…Damage.Order` | Faktorreihenfolge verändert Rundung erwartungsgemäß (Regressionsschutz) |
| `…Status.Exclusive` | Haupt-Status ersetzt sich nicht; Starre ersetzt Verlangsamt |
| `…Status.PoisonStacks` | 1–5 Stapel, Wechsel halbiert |
| `…Terrain.Neutralize` | Gegen-Terrain beendet ohne zu legen |
| `…Weather.Override` | Fähigkeitswetter überschreibt Weltwetter n Runden, dann Rückkehr |
| `Aethris.Func.Combat.PreviewExact` | Vorschau-Zahl = tatsächlicher Schaden ohne Krit in 1.000 Fällen |

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-112 | **Keine Schadensstreuung**; exakte Vorschau | Planbarkeit (S3), weniger Varianz im Ranked, DR-07 | 85–100 %-Würfel (Genre-Konvention, unlesbar) |
| ADR-113 | Divisor 180 (aus Simulation) | ~8 Züge im 1v1 auf allen Leveln | 84 (zu kurz), 220 (zu zäh) |
| ADR-114 | Volltreffer ×1,5, ignoriert ungünstige Stufen, Stufen 42/125/250/500 ‰ | Gegenmittel gegen Stufen-Stacking, gedeckelter Zufall | ×2 (zu swingy) |
| ADR-115 | Ein Haupt-Status, kein Überschreiben (außer Starre über Verlangsamt) | Lesbarkeit; Status-Wahl wird taktisch | Letzter gewinnt (Status-Ping-Pong) |
| ADR-116 | Gegen-Terrains neutralisieren statt ersetzen | Konterspiel ohne Terrain-Wettrüsten | Einfaches Überschreiben |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §114 | Basis = ⌊Stärke × A × (L+10)/(V × 180)⌋ + 2; Kette Eigenklang 1250 (≤ 1400) × Typ × Wetter × Krit 1500 × Formation × Sonstige; Mindestschaden 1; keine Streuung; Brand ANG ×0,75; Duell-Fläche ×0,8; Krit-Stufen 42/125/250/500 ‰ | LOCKED |
| §115 | Auflösungsreihenfolge 11 Schritte (K32 §1); Mehrfachtreffer je Treffer, Reaktionen einmal | LOCKED |
| §116 | Status final (`StatusEffects.csv`): Dauern in eigenen Zügen, Tick-Schaden Brand 60 ‰, Gift 30 ‰/Stapel; Anwendungsregeln K32 §5.1 | LOCKED |
| §117 | 15 Terrains (`Terrains.csv`), eines gleichzeitig, Neutralisation, Runden-Effekte, Arena-Terrains dauerhaft | LOCKED |
| §118 | Kampfwetter = Weltwetter der Zone; Fähigkeitswetter überschreibt n Runden; Sonderregeln je Runde; Ranked Klar; unter Tage nur Resonanzsturm/Fähigkeitswetter | LOCKED |
| §10 | ADR-112 – ADR-116 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Auflösungsreihenfolge eines Treffers
- [x] Schadensformel mit Herleitung (Simulation), Faktorkette, Sonderfälle
- [x] Beispielrechnungen aus echten Katalog- und Fähigkeitsdaten
- [x] Treffer, Ausweichen, Volltreffer
- [x] Status final mit Zahlen und Anwendungsregeln
- [x] 15 Terrains als Daten mit Regeln
- [x] Kampfwetter aus Weltwetter, Überschreiben, Sonderregeln
- [x] Schilde, Heilung, Entzug, Rückschlag, Konter, Reflexion, Wiederbelebung, Trugbild
- [x] Exakte Schadensvorschau (UI)
- [x] Code (constexpr, Pipeline), Tests, ADR-112 – ADR-116, CANON §114–§118

➡️ **Nächstes Kapitel: K33 – Kampfsystem III: Formation, Positionierung, Harmonie, Kombos und Synergien; Formate 1v1/2v2/3v3.**
