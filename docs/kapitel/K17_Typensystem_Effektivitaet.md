# K17 · Typensystem & Effektivitätstabelle

| Feld | Wert |
|---|---|
| Dokument | Kapitel 17 von 68 · Combat Guide, Teil I |
| Version | 1.0 |
| Owner | Combat Designer |
| Mitwirkende | RPG Systems Designer, Creative Director (Weltbedeutung), UI/UX (Lesbarkeit), QA (Balancing-Tests) |
| Baut auf | CANON §5.1 (15 Typen), §14 (Starter-Zyklus), §33 (Typ-Identitäten), §62 (Wetter-Typresonanz), ARN_08 Glyphenfeld (§51) |
| Status | ✅ Freigegeben |
| Im Repository | `tools/build_typechart.py` (Design-Quelle + Balance-Bericht), `Data/Combat/TypeChart.csv` (generiert) |
| Neue Kanon-Einträge | CANON §75 (Effektivitätsstufen), §76 (Typtabelle), §77 (Typregeln: Doppeltyp, Eigenklang, Umkehr, Immunitäten-Prinzip), §78 (Typ-Identitäten & Darstellung) |

---

## Inhalt

1. [Designziele](#1-designziele)
2. [Effektivitätsstufen (löst Q2)](#2-effektivitätsstufen-löst-q2)
3. [Die Typtabelle](#3-die-typtabelle)
4. [Begründungen je Typ (Weltlogik)](#4-begründungen-je-typ-weltlogik)
5. [Balance-Nachweis](#5-balance-nachweis)
6. [Doppeltypen & Eigenklang](#6-doppeltypen--eigenklang)
7. [Typ-Identitäten jenseits der Tabelle](#7-typ-identitäten-jenseits-der-tabelle)
8. [Sonderregeln: Tabellenumkehr, Wetter, Typwechsel](#8-sonderregeln-tabellenumkehr-wetter-typwechsel)
9. [Darstellung & Zugänglichkeit](#9-darstellung--zugänglichkeit)
10. [Code](#10-code)
11. [Decision Records](#11-decision-records)
12. [Kanon-Updates](#12-kanon-updates)
13. [Kapitel-Checkliste](#13-kapitel-checkliste)

---

## 1. Designziele

| Ziel | Messgröße | Ergebnis (§5) |
|---|---|---|
| **Jeder Typ ist gleich wertvoll** (Klang ohne mechanische Überlegenheit, CANON §5.1) | Offensiver/defensiver Erwartungswert je Typ innerhalb ±5 % | offensiv 0,980–1,070 · defensiv 0,990–1,070 ✔ |
| **Klare, lernbare Logik** | Jede Beziehung ist aus der Weltlogik begründbar (§4) | ✔ |
| **Kein Typ ist wirkungslos** (DR-07, DR-10) | Keine Immunität (Faktor 0) | Minimum 0,4 je Einzeltyp, 0,25 bei Doppeltyp ✔ |
| **Starter-Zyklus** (CANON §14) | Blüte > Stein > Sturm > Blüte, Rückrichtung resistiert | ✔ (automatisch geprüft) |
| **Eigenständigkeit** (Clean-Room) | Eigene Typen, eigene Relationen, eigene Stufen (1,6 / 0,625 / 0,4) | ✔ |
| **Teambau-Vielfalt** | Keine Zwei-Typ-Angriffskombination deckt alles sehr effektiv ab | beste Kombination trifft 67 von 120 Zieltyp-Kombinationen sehr effektiv ✔ |

---

## 2. Effektivitätsstufen (löst Q2)

| Stufe | Faktor | Promille | Symbol | Feedback (DR-06, DR-24) |
|---|---|---|---|---|
| **Sehr effektiv** | ×1,6 | 1600 | ● | Zahl gold, aufsteigender Akkord, Kamera-Akzent |
| **Neutral** | ×1,0 | 1000 | · | Standard |
| **Resistent** | ×0,625 | 625 | ○ | Zahl grau, gedämpfter Ton |
| **Gedämpft** | ×0,4 | 400 | ◌ | Zahl grau-blau, „Verschluckt“-Klang (sehr kurzer Ton) |

**Warum 1,6 / 0,625 statt 2 / 0,5?** 1,6 × 0,625 = 1,0 – eine Stärke und eine Resistenz heben sich bei Doppeltypen exakt auf. Die Extreme bei Doppeltypen sind gemäßigter (max. 2,56 statt 4,0), was Kämpfe weniger zu Einschlagslotterie macht (DR-07) und Taktik (Formation, Zeitleiste, Combos) wichtiger als reine Typwahl (Säule S3). **Gedämpft** ersetzt Immunitäten: thematisch starke Paare (Stein erdet Sturm, Leere verschluckt Klang) bleiben spürbar, aber nie wirkungslos.

---

## 3. Die Typtabelle

Zeile = Typ der **Fähigkeit** (Angreifer), Spalte = Typ des **Ziels**. Daten: `Data/Combat/TypeChart.csv` (generiert aus `tools/build_typechart.py`, LOCKED).

### 3.1 Symbolmatrix

```
              ZIEL →
 FÄHIGKEIT ↓  Glu Flu Ste Stu Blü Fro Lee Lic Gif Met Gei Kri Kla Sch Ark
 Glut          ○   ○   ○   ·   ●   ●   ·   ·   ·   ●   ·   ·   ·   ·   ·
 Flut          ●   ○   ●   ·   ○   ○   ·   ·   ●   ·   ·   ·   ·   ·   ·
 Stein         ●   ·   ·   ●   ○   ●   ·   ·   ·   ○   ○   ·   ·   ○   ·
 Sturm         ·   ●   ◌   ○   ●   ○   ·   ·   ·   ·   ·   ○   ●   ·   ·
 Blüte         ○   ●   ●   ○   ·   ·   ●   ·   ○   ·   ·   ·   ·   ·   ·
 Frost         ○   ·   ·   ●   ●   ○   ·   ·   ●   ○   ·   ·   ○   ·   ·
 Leere         ·   ·   ·   ·   ○   ·   ◌   ●   ·   ·   ·   ·   ●   ○   ●
 Licht         ·   ·   ·   ·   ·   ·   ●   ○   ●   ○   ●   ○   ·   ·   ·
 Gift          ·   ●   ○   ○   ●   ·   ·   ·   ○   ●   ○   ○   ·   ·   ·
 Metall        ·   ○   ●   ·   ·   ●   ·   ·   ·   ○   ·   ●   ·   ·   ·
 Geist         ·   ·   ○   ·   ·   ·   ○   ○   ·   ·   ●   ·   ·   ●   ●
 Kristall      ·   ·   ·   ·   ·   ·   ●   ●   ·   ○   ●   ○   ·   ·   ·
 Klang         ·   ·   ●   ·   ○   ·   ◌   ·   ○   ●   ·   ●   ○   ·   ○
 Schwerkraft   ·   ·   ·   ●   ·   ·   ·   ·   ·   ●   ◌   ●   ·   ○   ○
 Arkan         ·   ·   ○   ·   ·   ·   ○   ·   ·   ○   ·   ●   ·   ●   ●

 ● 1,6 sehr effektiv · · 1,0 neutral · ○ 0,625 resistent · ◌ 0,4 gedämpft
```

### 3.2 Listenform (offensiv)

| Fähigkeitstyp | Sehr effektiv gegen | Resistiert von | Gedämpft von |
|---|---|---|---|
| **Glut** | Blüte, Frost, Metall | Glut, Flut, Stein | – |
| **Flut** | Glut, Stein, Gift | Flut, Blüte, Frost | – |
| **Stein** | Glut, Sturm, Frost | Blüte, Metall, Geist, Schwerkraft | – |
| **Sturm** | Flut, Blüte, Klang | Sturm, Frost, Kristall | Stein |
| **Blüte** | Flut, Stein, Leere | Glut, Sturm, Gift | – |
| **Frost** | Sturm, Blüte, Gift | Glut, Frost, Metall, Klang | – |
| **Leere** | Licht, Klang, Arkan | Blüte, Schwerkraft | Leere |
| **Licht** | Leere, Gift, Geist | Licht, Metall, Kristall | – |
| **Gift** | Flut, Blüte, Metall | Stein, Sturm, Gift, Geist, Kristall | – |
| **Metall** | Stein, Frost, Kristall | Flut, Metall | – |
| **Geist** | Geist, Schwerkraft, Arkan | Stein, Leere, Licht | – |
| **Kristall** | Leere, Licht, Geist | Metall, Kristall | – |
| **Klang** | Stein, Metall, Kristall | Blüte, Gift, Klang, Arkan | Leere |
| **Schwerkraft** | Sturm, Metall, Kristall | Schwerkraft, Arkan | Geist |
| **Arkan** | Kristall, Schwerkraft, Arkan | Stein, Leere, Metall | – |

### 3.3 Listenform (defensiv)

| Zieltyp | Schwach gegen (×1,6) | Widersteht (×0,625) | Dämpft (×0,4) |
|---|---|---|---|
| Glut | Flut, Stein | Glut, Blüte, Frost | – |
| Flut | Sturm, Blüte, Gift | Glut, Flut, Metall | – |
| Stein | Flut, Blüte, Metall, Klang | Glut, Gift, Geist, Arkan | Sturm |
| Sturm | Stein, Frost, Schwerkraft | Sturm, Blüte, Gift | – |
| Blüte | Glut, Sturm, Frost, Gift | Flut, Stein, Leere, Klang | – |
| Frost | Glut, Stein, Metall | Flut, Sturm, Frost | – |
| Leere | Blüte, Licht, Kristall | Geist, Arkan | Leere, Klang |
| Licht | Leere, Kristall | Licht, Geist | – |
| Gift | Flut, Frost, Licht | Blüte, Gift, Klang | – |
| Metall | Glut, Gift, Klang, Schwerkraft | Stein, Frost, Licht, Metall, Kristall, Arkan | – |
| Geist | Licht, Geist, Kristall | Stein, Gift | Schwerkraft |
| Kristall | Metall, Klang, Schwerkraft, Arkan | Sturm, Licht, Gift, Kristall | – |
| Klang | Sturm, Leere | Frost, Klang | – |
| Schwerkraft | Geist, Arkan | Stein, Leere, Schwerkraft | – |
| Arkan | Leere, Geist, Arkan | Klang, Schwerkraft | – |

*Beide Listen sind aus `Data/Combat/TypeChart.csv` generiert.*

---

## 4. Begründungen je Typ (Weltlogik)

Jede Beziehung ist erzählerisch begründet – Spieler sollen sie *erraten* können (Säule S2: Verstehen). Die Kodex-Akademie-Notizen (K39) zitieren diese Begründungen.

| Typ | Stark gegen, weil … | Resistiert, weil … |
|---|---|---|
| Glut | verbrennt Pflanzen, schmilzt Frost, macht Metall weich | Wasser löscht, Stein hält stand, Feuer nährt Feuer |
| Flut | löscht Feuer, höhlt Stein, verdünnt Gift | Pflanzen trinken, Frost erstarrt das Wasser |
| Stein | erstickt Glut, erdet den Sturm (Starter-Zyklus), zerschlägt Eis | Wurzeln sprengen Steinschläge ab, Metall ist härter, Geister weichen aus, Masse zieht Steine an |
| Sturm | peitscht Wellen, entwurzelt Pflanzen (Zyklus), zerreißt Klang | Stein **erdet** den Sturm (gedämpft), Kälte bremst, Kristall leitet ab |
| Blüte | trinkt Wasser, sprengt Stein (Zyklus), füllt Leere mit Leben | Feuer verbrennt, Wind knickt, Gift welkt |
| Frost | lähmt Flügel im Sturm, erfriert Blüten, verlangsamt Gift | Glut taut, Metall leitet ab, Klang trägt durch Kälte |
| Leere | verschluckt Licht, Klang und Muster | Leben füllt Leere, Masse verankert, **Leere gegen Leere verpufft** (gedämpft) |
| Licht | enthüllt die Leere, läutert Gift, vertreibt Geister | Spiegel (Metall, Kristall) werfen Licht zurück |
| Gift | verseucht Wasser, welkt Pflanzen, **zersetzt Metall** (Korrosion – AETHRIS-eigene Regel) | Stein ist unverdaulich, Wind verweht, Geister haben keinen Körper |
| Metall | spaltet Stein, zerbricht Eis, schneidet Kristall | Wasser lässt rosten, gleiches Metall prallt ab |
| Geist | Geister erkennen Geister, schweben über der Schwerkraft, entwirren Muster | Stein ist zu dicht, Leere hat nichts zu erinnern, Licht vertreibt |
| Kristall | füllt Leere, bündelt Licht (Brechung), bannt Geister | Metall schneidet, Kristall spiegelt Kristall |
| Klang | sprengt Stein durch Resonanz, lässt Metall und Kristall zerspringen | weiche Blüten dämpfen, Schlamm schluckt, **Leere verschluckt Klang** (gedämpft) |
| Schwerkraft | zieht Flieger herab, zerdrückt Metall und Kristall | Geister haben keine Masse (gedämpft), Muster brechen Regeln |
| Arkan | entschlüsselt Kristallgitter, bricht die Regeln der Schwerkraft, liest Arkanes | „Kaltes Eisen“ (Metall), Stein, Leere negieren Magie |

**Gegensatzpaar Licht ↔ Leere:** Beide sind gegeneinander sehr effektiv – das spiegelt den Kernkonflikt der Welt (Lied vs. Pause, CANON §33) und macht diese Duelle explosiv.

---

## 5. Balance-Nachweis

Berechnet von `tools/build_typechart.py` (läuft im Pre-Submit, wenn sich die Tabelle ändert).

| Typ | offensiv ● | offensiv ○/◌ | defensiv schwach | defensiv widersteht | Offensiv-EV | Defensiv-EV (niedriger = robuster) |
|---|---|---|---|---|---|---|
| Glut | 3 | 3 | 2 | 3 | 1,045 | 1,005 |
| Flut | 3 | 3 | 3 | 3 | 1,045 | 1,045 |
| Stein | 3 | 4 | 4 | 5 | 1,020 | 1,020 |
| Sturm | 3 | 4 | 3 | 3 | 1,005 | 1,045 |
| Blüte | 3 | 3 | 4 | 4 | 1,045 | 1,060 |
| Frost | 3 | 4 | 3 | 3 | 1,020 | 1,045 |
| Leere | 3 | 3 | 3 | 4 | 1,030 | 0,990 |
| Licht | 3 | 3 | 2 | 2 | 1,045 | 1,030 |
| Gift | 3 | 5 | 3 | 3 | 0,995 | 1,045 |
| Metall | 3 | 2 | 4 | 6 | 1,070 | 1,010 |
| Geist | 3 | 3 | 3 | 3 | 1,045 | 1,030 |
| Kristall | 3 | 2 | 4 | 4 | 1,070 | 1,060 |
| Klang | 3 | 5 | 2 | 2 | 0,980 | 1,030 |
| Schwerkraft | 3 | 3 | 2 | 3 | 1,030 | 1,005 |
| Arkan | 3 | 3 | 3 | 2 | 1,045 | 1,070 |

*EV = durchschnittlicher Faktor gegen alle 15 Typen (gleichverteilt).*

**Bewertung:**
- Jeder Typ ist gegen **genau 3** Typen sehr effektiv (Gleichheit der Grundangebote).
- Spannen: offensiv **0,980–1,070**, defensiv **0,990–1,070** → alle innerhalb ±4,5 % des Mittels.
- **Klang** ist offensiv der schwächste Typ (0,980) – bewusst: Klang erhält seine Stärke über die Zeitleisten-Manipulation (§7), nicht über die Tabelle (CANON §5.1: erzählerische Sonderrolle, keine mechanische Überlegenheit).
- **Metall/Kristall** sind offensiv am stärksten, defensiv mittel; ihre Gegenspieler (Klang, Schwerkraft) sind dafür offensiv schwächer → Dreiecksdynamik.

**Doppeltypen (105 Kombinationen):**
- 39 (37 %) haben mindestens eine Schwäche ×2,56; 10 haben einen Widerstand ≤ ×0,25.
- Spanne aller Doppeltyp-Faktoren: **0,25–2,56** (keine Immunitäten).
- Beste Zwei-Typ-Angriffsabdeckung (Kristall + Schwerkraft) trifft 67 von 120 Zieltyp-Kombinationen sehr effektiv und alle mindestens neutral – stark, aber nicht alles abdeckend; schwächste (Sturm + Gift) trifft 39 sehr effektiv. → Teambau bleibt eine echte Entscheidung.

**Weiterführende Prüfung:** Der Balancing-Simulator (K63) testet die Tabelle mit realen Basiswerten und Fähigkeiten (Monte-Carlo, 10⁶ Kämpfe); Akzeptanz: Siegrate jedes Monotyp-Teams gegen ein Zufallsfeld 45–55 %.

---

## 6. Doppeltypen & Eigenklang

### 6.1 Doppeltyp-Berechnung (LOCKED)

```
 Typfaktor = Tabelle[Fähigkeitstyp][Zieltyp1] × Tabelle[Fähigkeitstyp][Zieltyp2] / 1000      (Promille, ganzzahlig)
 Mögliche Werte: Einzeltyp 1600, 1000, 625, 400 · Doppeltyp 2560, 1600, 1000, 640, 625, 400, 391, 250
```

Ganzzahlige Promille-Arithmetik mit Rundung zur nächsten ganzen Zahl (Determinismus-Zone, CS-14). Beispiel: Glut gegen Blüte/Frost = 1600 × 1600 / 1000 = **2560**.

### 6.2 Eigenklang (Typgleichheitsbonus)

Setzt ein Echo eine Fähigkeit eines seiner **eigenen** Typen ein, klingt sie in seiner Grundfrequenz: **Eigenklang ×1,25** (Promille 1250). Begründung: Ein Oberton schwingt am stärksten in seiner eigenen Klangfarbe. Mehrere Quellen (Passive, Crescendo) können den Eigenklang auf max. ×1,4 erhöhen (K28/K32).

### 6.3 Fähigkeiten ohne Typ

Es gibt **keine typlosen Schadensfähigkeiten**. Jede Schadensfähigkeit hat einen der 15 Typen. Unterstützungsfähigkeiten (Heilung, Buffs) haben einen Typ für Eigenklang-Effekte (z. B. Heilung +25 %), aber keinen Tabellenfaktor.

---

## 7. Typ-Identitäten jenseits der Tabelle

DR-08 verlangt für jeden Typ eine eigene Mechanik. Die Tabelle ist nur die halbe Wahrheit; die andere Hälfte sind **Typ-Mechaniken**, die in K28–K33 ausgestaltet werden. Hier verbindlich festgelegt:

| Typ | Kernmechanik (Primitiv) | Statusbezug (Immunität, K32) | Feld-/Terrain-Bezug |
|---|---|---|---|
| Glut | Schaden über Zeit (Brand), Terrain *Glutboden* | immun gegen *Brand* | Glutboden |
| Flut | Positionsverschiebung (Ziel in andere Reihe spülen), Heilung über Zeit | immun gegen *Ausgetrocknet* | Pfütze/Strömung |
| Stein | Schilde (absorbieren Schaden), Rückstoß-Resistenz, Vorderreihen-Bonus | immun gegen *Rückstoß* | Geröll |
| Sturm | **Zeitleisten-Beschleunigung** (eigene Zeitkosten −), Mehrfachtreffer | immun gegen *Verlangsamt* | Wind |
| Blüte | Heilung, Terrain *Überwuchs*, Ausdauer (Regeneration) | immun gegen *Welke* | Überwuchs |
| Frost | **Gegner verlangsamen** (Zeitkosten +), Präzisionsboni | immun gegen *Starre* | Eisfläche |
| Leere | **Entzug**: Harmonie, Buffs, Schilde löschen/stehlen | immun gegen *Entzug* | Stillefeld |
| Licht | Enthüllen (Ausweichen ignorieren), Statusreinigung | immun gegen *Geblendet* | Lichtung |
| Gift | Stapelnde Schwächung (Werte sinken pro Stapel), Schaden über Zeit | immun gegen *Vergiftet* | Sumpf |
| Metall | Rüstung (flache Schadensreduktion), Konter | immun gegen *Zersetzt*? **nein** – Metall ist anfällig für Gift (§4); immun gegen *Erschüttert* | Schrottfeld |
| Geist | Täuschung (Zielumleitung), Formation ignorieren (trifft Hinterreihe) | immun gegen *Furcht* | Nebel |
| Kristall | Reflexion, Laden & Freisetzen (Ladeangriffe über 2 Züge) | immun gegen *Gebrochen* | Kristallfeld |
| Klang | **Zeitleisten-Manipulation** (Gegner verzögern, Verbündete synchronisieren), Harmonie-Erzeugung | immun gegen *Verstummt (Kampfstatus)* | Resonanzfeld |
| Schwerkraft | Positionierung erzwingen (Ziehen/Stoßen, Reihentausch) | immun gegen *Schwebend* | Schwerefeld |
| Arkan | Regelbruch (Typ ändern, Tabelle umkehren, Effekte tauschen) | immun gegen *Verflucht* | Glyphenfeld |

*Statusnamen sind Arbeitsnamen; die finale Statusliste und Wirkungen definiert K32.*

---

## 8. Sonderregeln: Tabellenumkehr, Wetter, Typwechsel

### 8.1 Tabellenumkehr (Glyphenfeld ARN_08, Arkan-Fähigkeiten)

| Normal | Umgekehrt |
|---|---|
| 1600 | 625 |
| 1000 | 1000 |
| 625 | 1600 |
| 400 | 1600 |

Arkan-Echos des Spielers sind von der Glyphenfeld-Umkehr ausgenommen (CANON §51). Umkehr wirkt 1 Zug und ist auf der Zeitleiste angekündigt (DR-06).

### 8.2 Reihenfolge der Faktoren (Vorgabe für K32)

```
 Schaden = Basis(Fähigkeit, Werte, Level) × Eigenklang × Typfaktor (Doppeltyp) × Wetter (CANON §62) × Kritisch × Formation × Sonstige
```

Die vollständige Formel und Rundungsregeln legt K32 fest; die Faktoren dieses Kapitels sind dort unverändert zu verwenden.

### 8.3 Typwechsel

- **Arkan-Fähigkeiten** können den Typ eines Ziels für 2 Züge ändern (z. B. „Musterwechsel“).
- **Evolution** kann Typen ändern (z. B. Zweittyp hinzufügen); im Kampf nie.
- **Morphs** ändern nie den Typ (DR-17: Optik ≠ Mechanik).

---

## 9. Darstellung & Zugänglichkeit

### 9.1 Typfarben & -symbole (vorläufig; final in K56 Art Bible)

| Typ | Farbe (Hex, Arbeitsstand) | Symbolform (farbunabhängig) |
|---|---|---|
| Glut | `#E8562A` | Flamme in Dreieck |
| Flut | `#2E8BC0` | Welle in Kreis |
| Stein | `#8C7B65` | Sechseck, gefüllt |
| Sturm | `#7FD1E8` | Spirale |
| Blüte | `#5DAA4C` | Blatt in Tropfen |
| Frost | `#BFE6F5` | Sechszackiger Stern |
| Leere | `#2B2240` | Ring (Negativraum) |
| Licht | `#F6D86B` | Strahlenkranz |
| Gift | `#8E4FB0` | Drei Tropfen |
| Metall | `#9AA3AD` | Quadrat mit Niet |
| Geist | `#B7A4E0` | Halbmond mit Schleier |
| Kristall | `#E28FC6` | Raute mit Facette |
| Klang | `#F2A93B` | Drei Bögen (Schall) |
| Schwerkraft | `#4B5BA6` | Kreis mit Punkt (Orbit) |
| Arkan | `#3FB8A8` | Glyphe (Achtstern) |

**Zugänglichkeit (DR-24, K02 §11.3):** Typen werden **immer** mit Symbol + Name dargestellt, nie nur mit Farbe. Farbenblind-Modi verschieben die Paletten so, dass benachbarte Typpaare (Sturm/Frost, Glut/Klang, Leere/Schwerkraft) unterscheidbar bleiben – Prüfung mit Simulationsfiltern im UI-Review (K54).

### 9.2 Effektivitäts-Vorschau

Vor dem Bestätigen einer Fähigkeit zeigt das Kampf-UI je Ziel ein Symbol (●/·/○/◌) und den kombinierten Faktor (z. B. „×2,56“). **Ab Kodex-Stufe 2 der Zielart** (K39) – vorher „?“ bei unbekannten Arten. *Design-Absicht:* Wissen belohnen (DR-01-Geist), Kodex motivieren. Im Schwierigkeitsgrad *Entspannt* immer sichtbar.

---

## 10. Code

```cpp
// AethrisCore/Public/Combat/TypeChart.h  (Core, damit Combat, KI und UI denselben Zugriff haben)
/**
 * Typtabelle aus Data/Combat/TypeChart.csv (K17). Ganzzahlige Promille, deterministisch (CS-14).
 * Indizes 0..14 in der Reihenfolge T01..T15 (Ember … Arcane).
 */
class AETHRISCORE_API FAethrisTypeChart
{
public:
	static constexpr int32 NumTypes = 15;

	/** Lädt die Tabelle aus der Data Table (beim Start, validiert). */
	bool LoadFrom(const UDataTable& Table);

	/** Faktor einer Fähigkeit gegen ein Ziel mit 1–2 Typen (Promille). SecondType = INDEX_NONE bei Einzeltyp. */
	int32 GetFactorPermille(int32 AbilityType, int32 TargetType1, int32 TargetType2, bool bInverted = false) const
	{
		int32 F = Lookup(AbilityType, TargetType1, bInverted);
		if (TargetType2 != INDEX_NONE)
		{
			// Rundung zur nächsten ganzen Promille (K17 §6.1)
			F = (F * Lookup(AbilityType, TargetType2, bInverted) + 500) / 1000;
		}
		return F;
	}

	/** Eigenklang ×1,25 (+ Boni, gedeckelt ×1,4). */
	static int32 GetSameTypePermille(int32 BonusPermille = 0) { return FMath::Min(1250 + BonusPermille, 1400); }

private:
	int32 Lookup(int32 A, int32 D, bool bInverted) const
	{
		const int32 V = Chart[A][D];
		if (!bInverted) { return V; }
		return V == 1600 ? 625 : (V == 1000 ? 1000 : 1600);   // Umkehr §8.1
	}
	int32 Chart[NumTypes][NumTypes] = {};
};
```

```cpp
// GF_Combat/Tests/TypeChartSpec.cpp (Auszug)
It("erfüllt den Starter-Zyklus", [this]()
{
	TestEqual(TEXT("Blüte→Stein"), Chart.GetFactorPermille(Bloom, Stone, INDEX_NONE), 1600);
	TestEqual(TEXT("Stein→Sturm"), Chart.GetFactorPermille(Stone, Storm, INDEX_NONE), 1600);
	TestEqual(TEXT("Sturm→Blüte"), Chart.GetFactorPermille(Storm, Bloom, INDEX_NONE), 1600);
	TestEqual(TEXT("Sturm→Stein gedämpft"), Chart.GetFactorPermille(Storm, Stone, INDEX_NONE), 400);
});
It("hat keine Immunitäten", [this]()
{
	for (int32 A = 0; A < 15; ++A) for (int32 D1 = 0; D1 < 15; ++D1) for (int32 D2 = 0; D2 < 15; ++D2)
		if (D1 != D2) TestTrue(TEXT(">0"), Chart.GetFactorPermille(A, D1, D2) >= 250);
});
```

**Python-Parität:** `tools/build_typechart.py` ist die Design-Quelle; der Pre-Submit vergleicht die generierte CSV mit dem Data-Table-Import (Hash).

---

## 11. Decision Records

### ADR-079 – Effektivitätsstufen 1,6 / 1,0 / 0,625 / 0,4
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) 2,0 / 1,0 / 0,5 / 0 | Genre-vertraut | Immunitäten (DR-10), Extremwerte ×4 bei Doppeltypen, Nähe zu bestehenden Systemen |
| (b) 1,6 / 1,0 / 0,625 / 0,4 | Stärke × Resistenz = 1, gemäßigte Extreme, keine Immunität, eigenständig | Weniger „dramatische“ Einzeltreffer → Drama über Combos/Crescendo (K33) |
- **Entscheidung:** (b).

### ADR-080 – Tabelle als generierte Daten mit Balance-Bericht
- **Entscheidung:** Design-Absicht in Python-Dicts (lesbar, kommentierbar), CSV generiert, Bericht im Pre-Submit. Änderungen an der Tabelle sind `[DATA]`-Changelists mit Pflicht-Review durch den Combat Designer.

### ADR-081 – Gift schlägt Metall (Korrosion)
- **Entscheidung:** Bewusste Abweichung von Genre-Gewohnheiten; weltlogisch begründet (Korrosion), stärkt Clean-Room-Eigenständigkeit und gibt Gift ein Ziel gegen das robuste Metall.

### ADR-082 – Licht und Leere gegenseitig sehr effektiv
- **Entscheidung:** Spiegelt den Kernkonflikt (Lied ↔ Pause). Vorteil: erzählerisches Gewicht im Kampf (Finale: Velnox Leere/Schwerkraft vs. Aeth'rion Klang/Licht). Nachteil: Glaskanonen-Duelle → beide Typen erhalten defensiv sonst robuste Profile (Leere-EV 0,990, Licht 1,030).

### ADR-083 – Effektivitätsvorschau an Kodex-Stufe 2 gekoppelt
- **Entscheidung:** Siehe §9.2. Vorteil: Forschung lohnt sich im Kampf (S2 × S3). Nachteil: Neue Spieler sehen „?“ → *Entspannt* zeigt immer; Kodex-Stufe 2 wird durch einen Kampf gegen die Art meist schon erreicht (K39).

---

## 12. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §75 | Effektivitätsstufen sehr effektiv 1600 · neutral 1000 · resistent 625 · gedämpft 400 ‰; keine Immunität; Symbole ●·○◌ – löst Q2 | LOCKED |
| §76 | Vollständige Typtabelle (`Data/Combat/TypeChart.csv`, generiert aus `tools/build_typechart.py`) gemäß §3; jeder Typ 3× sehr effektiv; gedämpfte Paare: Sturm→Stein, Leere→Leere, Klang→Leere, Schwerkraft→Geist | LOCKED |
| §76 | Balance: Offensiv-EV 0,980–1,070, Defensiv-EV 0,990–1,070; Doppeltyp-Spanne 0,25–2,56 | LOCKED |
| §77 | Doppeltyp = Produkt in Promille mit Rundung; **Eigenklang ×1,25** (max. ×1,4); keine typlosen Schadensfähigkeiten; Tabellenumkehr 1600↔625, 400→1600; Faktor-Reihenfolge (Vorgabe K32) | LOCKED |
| §77 | Typwechsel: Arkan-Fähigkeiten (2 Züge), Evolution; Morphs nie | LOCKED |
| §78 | Typ-Kernmechaniken und Status-Immunitäts-Prinzip (je Typ eine Immunität, Namen final in K32) | LOCKED |
| §78 | Typfarben (Arbeitsstand, final K56) + Symbolformen; Darstellung immer Symbol + Name; Effektivitätsvorschau ab Kodex-Stufe 2 (Entspannt immer) | LOCKED |
| §29 | `FAethrisTypeChart` (AethrisCore) | LOCKED |
| §12 | Q2 erledigt | – |
| §10 | ADR-079 – ADR-083 | LOCKED |

---

## 13. Kapitel-Checkliste

- [x] Designziele mit Messgrößen
- [x] Effektivitätsstufen (Q2 gelöst) inkl. Begründung
- [x] Vollständige 15×15-Typtabelle (Matrix, offensiv, defensiv), generiert und im Repo
- [x] Weltlogische Begründung aller Beziehungen
- [x] Balance-Nachweis (Einzel- und Doppeltypen, Abdeckungsanalyse)
- [x] Doppeltyp-Berechnung, Eigenklang, Fähigkeiten ohne Typ
- [x] Typ-Kernmechaniken und Immunitätsprinzip
- [x] Sonderregeln (Umkehr, Faktor-Reihenfolge, Typwechsel)
- [x] Farben, Symbole, Zugänglichkeit, Vorschau-Regel
- [x] Code + Tests
- [x] ADR-079 – ADR-083, CANON aktualisiert

➡️ **Nächstes Kapitel: K18 – Statuswerte, Persönlichkeit, Temperament, Wachstumsraten.**
