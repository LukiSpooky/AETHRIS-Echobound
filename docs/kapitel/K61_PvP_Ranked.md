# K61 · PvP und Ranked

| Feld | Wert |
|---|---|
| Dokument | Kapitel 61 von 68 · Online III |
| Version | 1.0 |
| Owner | Lead Combat Designer, Lead Online Designer |
| Mitwirkende | Balancing Analyst, Backend Engineer (Ranked-Dienst), Data Scientist, UX Lead, Community Manager, Esports/Events Producer, QA Online |
| Baut auf | K02 (DR-11 Kampfdauer, DR-21 Fairness), K17 (Typen), K18 (Statusformeln, Anlagen, Schliff, CANON §79/§80), K28–K33 (Kampf, Formate, Crescendo kurz), K34 (Kampf-KI), K40 (Halteitems), K43 §8 (Skills im Ranked), K59 (Server-Autorität, Replays, Matchmaking), K60 (Geister-Teams, Gesten) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/PvP/Rulesets.csv`, `RankTiers.csv`, `SeasonCalendar.csv`; Referenzmodell `tools/ref/aethris_pvp.py` (Normalisierung, Glicko-2, Simulation, PV-01–PV-06); `GF_PvP/…/Ranked/AethrisRankedTypes.h/.cpp` (Glicko-2, Klangstufen) |
| Neue Kanon-Einträge | CANON §240 (Q5 Normalisierung), §241 (Regelsätze), §242 (Ranked: Wertung, Stufen, Saisons), §243 (Fair Play, Meta-Pflege, Zuschauen); Q5 geschlossen |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Level-Normalisierung – Entscheidung Q5](#2-level-normalisierung--entscheidung-q5)
3. [Regelsätze](#3-regelsätze)
4. [Ranked](#4-ranked)
5. [Arena-Halle frei, Freundeskampf, Geister-Teams](#5-arena-halle-frei-freundeskampf-geister-teams)
6. [Zuschauen, Replays, Turniere](#6-zuschauen-replays-turniere)
7. [Meta-Pflege](#7-meta-pflege)
8. [Fair Play](#8-fair-play)
9. [UX](#9-ux)
10. [Technik](#10-technik)
11. [Telemetrie](#11-telemetrie)
12. [Prüfregeln](#12-prüfregeln)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Ziele

PvP in AETHRIS ist **Taktik auf der Zeitleiste**: Wer die Verzögerungen, Kombos, Formationen und die Harmonie besser liest, gewinnt. Ziele:

| Ziel | Bedeutung | Messbar an |
|---|---|---|
| **PZ-1 Fair (DR-21)** | Serverautoritativ, levelnormalisiert, nur geprüfte Echos | 0 Client-Zustände (K59 NET-05), Legalität 100 % |
| **PZ-2 Lesbar** | Jede Entscheidung des Gegenübers ist auf der Zeitleiste sichtbar; kein verdeckter Zufall außer Trefferchance (gedeckelt 500–1000 ‰) und Gleichstand-PCG | Zuschauer verstehen Züge |
| **PZ-3 Kurz genug** | Ranked-Trio ≤ 20 min (DR-11), Duell ≤ 15 min | Zeitlimit, Schachuhr |
| **PZ-4 Vielfalt** | Viele Arten sind spielbar; kein „Pflicht-Team“ | Nutzungsanteil der Top-Art ≤ 40 % (Signal, §7) |
| **PZ-5 Respekt** | Gruß-Gesten, kein Freitext, Melden einfach | Meldungen ≤ 2/1.000 Kämpfe |
| **PZ-6 Kein Machtkauf** | Belohnungen kosmetisch, keine Echos, kein Sol aus PvP (CANON Wirtschaft) | PV-06 |

---

## 2. Level-Normalisierung – Entscheidung Q5

**Frage (Q5):** Wie wird im Ranked normalisiert?

### 2.1 Optionen

| Option | Beschreibung | Vorteile | Nachteile |
|---|---|---|---|
| A Keine | Echte Level (max. 100) | „Mein Echo, wie es ist“ | Level-Grind als Pflicht, Neuzugänge chancenlos (widerspricht DR-21) |
| B Norm 50 | Alle auf Level 50 | Kleinere Zahlen | Unter dem Story-Endstand (~68–70); Echos wirken „geschrumpft“, Evolutionsstufen jenseits Level 50 fühlen sich falsch an |
| **C Norm 70** | Alle auf Level 70 (= Story-Ende, Ranked ab Wärterrang 28) | Entspricht dem Stand beim Freischalten; neue Echos sofort spielbar; Endgame-Level bringen keinen Vorteil | Echos über 70 verlieren sichtbar Werte (Hinweis in der UI) |
| D Norm 100 | Alle auf Level 100 | Maximale Zahlen | Große Zahlen ohne Mehrwert; Schliff wirkt relativ schwächer |
| E Spielerwahl | Jeder wählt | Freiheit | Fragmentiert Matchmaking-Pools |

### 2.2 Entscheidung: Option C – Normstufe 70

Im Ranked (und standardmäßig in der freien Arena-Halle) werden alle Echos mit den Formeln aus K18 (CANON §79) **auf Level 70 umgerechnet**. Ihre echten **Anlagen** (0–15), **Schliff**-Punkte (0–80 je Kernwert, Σ ≤ 240), Persönlichkeit, Fähigkeiten und Halteitems bleiben. Das Level selbst wird nie verändert; die Umrechnung gilt nur für den Kampf.

Beispiele (Anlage 10, Schliff 0, Werte aus `Species.csv`):

| Art | Level (echt) | HP | Angriff | Spez.-Angr. | Geschw. | → Norm 70: HP | Angriff | Spez.-Angr. | Geschw. |
|---|---|---|---|---|---|---|---|---|---|
| Verdrath | 52 | 227 | 91 | 114 | 93 | 293 | 118 | 147 | 120 |
| Anchrex | 61 | 244 | 99 | 143 | 123 | 275 | 112 | 161 | 139 |
| Maraune | 70 | 247 | 155 | 140 | 195 | 247 | 155 | 140 | 195 |
| Pyroluth | 78 | 281 | 93 | 214 | 184 | 255 | 84 | 195 | 168 |
| Skriveth | 88 | 312 | 103 | 245 | 199 | 255 | 84 | 200 | 163 |
| Cirrhaven | 100 | 341 | 215 | 195 | 275 | 249 | 156 | 142 | 200 |

**Was Investition bewirkt:** Anlagen und Schliff zählen auch im Ranked – sie sind erreichbar ohne Geld (Zucht K38, Training/Kämpfe K18, Klangstimmung im Endgame) und belohnen Pflege. Ihre Wirkung bei Norm 70 am Beispiel eines Kernwerts mit Basis 100:

| Anlage | Schliff | Kernwert (Basis 100, Norm 70) | Δ ggü. Anlage 0 / Schliff 0 |
|---|---|---|---|
| 0 | 0 | 145 | +0,0 % |
| 7 | 0 | 155 | +6,9 % |
| 15 | 0 | 167 | +15,2 % |
| 0 | 80 | 185 | +27,6 % |
| 15 | 80 | 207 | +42,8 % |

Die größte Spanne (+42,8 % zwischen „unbearbeitet“ und „vollendet“) ist bewusst: Sie macht Zucht und Schliff zu einem sinnvollen Langzeitziel. Damit Neueinsteigende nicht chancenlos sind, bietet die freie Arena-Halle (§5) einen **Gleichklang-Regelsatz** im Freundeskampf an (alle Anlagen 15, Schliff ignoriert), und das Matchmaking trennt über die Wertung ohnehin nach Erfahrung.

### 2.3 Warum genau 70?

Drei Rechnungen stützen die Wahl:

1. **Evolutionsstufen sind erreicht.** Alle Evolutionen mit Levelschwelle liegen unter 70; die höchste Schwelle ist Level 44. Eine Normstufe unterhalb mancher Schwellen (z. B. 40) würde Endformen „unter ihrem Entwicklungslevel“ kämpfen lassen – das fühlt sich falsch an und wirft Fragen zur Legalität auf.

| Evolutions-Levelschwelle | Anzahl Evolutionen |
|---|---|
| 1–20 | 34 |
| 21–30 | 45 |
| 31–40 | 40 |
| 41–50 | 3 |
| 51–60 | 0 |
| 61–70 | 0 |
| 71–100 | 0 |
| ohne Levelschwelle (Bindung, Item, Ort, Zeit …) | 3 |
| **höchste Schwelle** | **44** |

2. **Gehorsam ist kein Thema.** Die Gehorsamsgrenze mit allen 10 Akkorden ist 100 (CANON §18); Ranked setzt Wärterrang 28 voraus, also das Story-Ende mit allen Akkorden. Bei Norm 70 gehorchen alle Echos – auch getauschte.

3. **Werte sind „fertig“, Zahlen bleiben lesbar.** Bei Level 70 liegen HP typischerweise zwischen 200 und 350 und Kernwerte zwischen 80 und 250. Damit sind Schadensprozente auf der Zeitleiste gut abschätzbar; Schliff (bis +40 auf einen Kernwert) bleibt spürbar, ohne alles zu überdecken.

### 2.4 Der Ranked-Pool

240 Arten sind zulässig. Die Verteilung nach Primärtyp und die durchschnittliche Kernsumme der Endformen zeigen, dass kein Typ strukturell benachteiligt ist – die Kernsummen der Endformen liegen eng beieinander (K18-Bänder):

| Primärtyp | zulässige Arten | davon Endformen | Ø Kernsumme Endformen |
|---|---|---|---|
| Stein | 25 | 11 | 510 |
| Sturm | 24 | 10 | 511 |
| Licht | 18 | 7 | 506 |
| Klang | 17 | 10 | 491 |
| Geist | 16 | 10 | 506 |
| Flut | 16 | 6 | 515 |
| Schwerkraft | 16 | 8 | 511 |
| Arkan | 15 | 10 | 507 |
| Metall | 15 | 8 | 501 |
| Kristall | 15 | 7 | 505 |
| Blüte | 13 | 4 | 517 |
| Gift | 13 | 7 | 495 |
| Glut | 13 | 5 | 518 |
| Frost | 12 | 4 | 523 |
| Leere | 12 | 8 | 508 |

Auch Nicht-Endformen sind zulässig. Manche Stufe-2-Arten bringen Utility-Fähigkeiten mit, die ihre Endform nicht mehr lernt, und sind dadurch in bestimmten Teams lohnend; die Saisonregel „Kleine Stimmen“ stellt sie gezielt ins Rampenlicht.

### 2.5 Weitere Ranked-Grundsätze

| Grundsatz | Festlegung | Quelle |
|---|---|---|
| Zulässige Arten | 240 (keine Ursprungsstimmen, keine Mythischen) | CANON §34; PV-01 |
| Art-Klausel | jede Art höchstens 1× im Team | K61 |
| Halteitems | erlaubt, keine Duplikate; Komfort-Items wirkungslos | CANON Ausrüstung |
| Verbrauchsgüter | keine | CANON Wirtschaft |
| Wetter | Klar (Fähigkeitswetter erlaubt) | CANON §61 |
| Skills | nur Informations- und Komfort-Skills | K43 §8 |
| Crescendo | immer Kurzfassung (1,5 s) | K30 |
| Gehorsam | im Ranked immer voll (Normstufe ≤ Gehorsamsgrenze mit 10 Akkorden = 100) | CANON §18 |
| Legalität | nur signierte Echos (K59 §9) | DR-21 |

---

## 3. Regelsätze

| DisplayName | Format | Level | NormLevel | Team | Preview | Items | Weather | Timer | MatchLimitMin | Restrictions |
|---|---|---|---|---|---|---|---|---|---|---|
| Ranked Trio | Trio 3+3 | Norm | 70 | 6/6/3 | Arten der Gegenseite, 90 s Aufstellung | Halteitems ohne Duplikate; keine Verbrauchsgüter | Klar (Fähigkeitswetter erlaubt) | 30 s + 90 s Bank | 20 | Keine Ursprungsstimmen, keine Mythischen, keine Leih-Echos, Art höchstens 1×, nur signierte Echos, nur Informations-/Komfort-Skills |
| Ranked Duell (Saison-Rotation) | Duell 1+5 | Norm | 70 | 6/6/1 | Arten der Gegenseite, 60 s Reihenfolge | Halteitems ohne Duplikate; keine Verbrauchsgüter | Klar | 30 s + 90 s Bank | 15 | Keine Ursprungsstimmen, keine Mythischen, keine Leih-Echos, Art höchstens 1×, nur signierte Echos, nur Informations-/Komfort-Skills |
| Arena-Halle frei – Duell | Duell 1+5 | Norm | 70 | 6/6/1 | Arten, 60 s | Halteitems | Klar | 30 s + 90 s Bank | 15 | Ursprungsstimmen/Mythische erlaubt, Art höchstens 1× |
| Arena-Halle frei – Duo | Duo 2+4 | Norm | 70 | 6/6/2 | Arten, 75 s | Halteitems | Klar | 30 s + 90 s Bank | 18 | wie frei Duell |
| Arena-Halle frei – Trio | Trio 3+3 | Norm | 70 | 6/6/3 | Arten, 90 s | Halteitems | Klar | 30 s + 90 s Bank | 20 | wie frei Duell |
| Freundeskampf | Duell/Duo/Trio | Norm oder Eigen | 70 | frei | frei | frei | frei (inkl. Weltwetter) | frei (Standard 60 s) | 0 | frei; ungewertet |
| Geister-Teams (offline) | Duell/Duo/Trio | Norm | 70 | 6/6/x | Arten | Halteitems | Klar | ohne | 0 | Gegner = gespeicherte Teams + Kampf-KI (AI_NPC_VETERAN, mit der aufgezeichneten Aufstellung) |
| Saisonregel (Beispiel „Kleine Stimmen“) | Trio 3+3 | Norm | 50 | 6/6/3 | Arten, 90 s | Halteitems ohne Duplikate | Klar | 30 s + 90 s Bank | 20 | nur Stufe-1-Arten oder Einzelarten mit Kernsumme ≤ 430; ungewertet für den Hauptrang, eigene Rangliste |

**Team, Vorschau, Aufstellung:** Für Ranked registriert man ein Team aus 6 Echos (ein Chor). Vor dem Kampf sehen beide Seiten die **Arten** des Gegenübers (nicht Fähigkeiten, Items, Werte) und haben 90 s (Trio) bzw. 60 s (Duell) für Aufstellung und Formation (Vorder-/Hinterreihe, K33). Alle 6 kommen mit; aktiv sind 3 (Trio) bzw. 1 (Duell), die übrigen bilden die Reserve. Wechsel aus der Reserve kostet Zeitleisten-Zeit (CANON Kampf).

---

## 4. Ranked

### 4.1 Ablauf eines Kampfes

```
Matchmaking (Glicko-2, Region, Crossplay) ─► Server zugeteilt (K59 §7)
 ─► Teamvorschau 90 s (Arten) ─► Aufstellung ─► Gruß (optional, Geste)
 ─► Kampf: Zeitleiste, gleichzeitiges Planen bei gleichem Tick, Zugtimer 30 s + Bank 90 s
 ─► Ende: alle gegnerischen Echos verklungen · Aufgabe · Zeitlimit (20 min)
 ─► Wertung (Glicko-2) ─► Stufe/Fortschritt ─► Gruß (optional) ─► Replay gespeichert (90 Tage)
```

### 4.2 Zeit

| Element | Wert | Wirkung |
|---|---|---|
| Zugtimer | 30 s je Entscheidung | danach wird die Bank verbraucht |
| Reservebank | 90 s je Kampf und Person | leer → automatisch „Abwarten“; 3× hintereinander → Aufgabe |
| Zeitlimit | 20 min (Trio) / 15 min (Duell) | Ende nach Tiebreak |
| Animationen | zählen nicht zur Zeit der Person | Crescendo immer kurz |

**Tiebreak beim Zeitlimit:** (1) mehr nicht verklungene Echos, (2) höherer Anteil verbleibender HP am Gesamt-Max-HP des Teams (Promille, ganzzahlig), (3) mehr verbleibende Bankzeit, (4) Gleichstand (Wertung 0,5). Die Reihenfolge belohnt aktives Spiel und bestraft Hinhalten.

**Beispiel Tiebreak:** Nach 20 Minuten hat Seite A noch 2 Echos (HP 180/290 und 40/260), Seite B noch 2 Echos (HP 250/250 und 10/300). Gleich viele Echos → HP-Anteil am Gesamt-Max-HP des Teams (6 Echos): A = (180 + 40) / Σ Max-HP A, B = (250 + 10) / Σ Max-HP B. Bei Σ Max-HP A = 1.620 und Σ Max-HP B = 1.580 ergibt das A = 135 ‰, B = 164 ‰ → **B gewinnt**. Alle Werte sind ganzzahlig (‰, abgerundet), damit Server und Replay identisch rechnen.

### 4.3 Ein Ranked-Kampf, Zug für Zug (Beispiel)

Die folgende Erzählung zeigt, wie die Systeme im Ranked zusammenspielen. Seite A bringt ein Harmonie-Team (Klang-Striker vorn, Licht-Unterstützung hinten, Sturm-Tempo-Echo), Seite B ein Kontroll-Team (Frost vorn, Gift und Leere).

1. **Vorschau (90 s):** A sieht eine Leere-Art bei B und weiß: Harmonie wird entzogen werden. A stellt das Licht-Echo nach vorn, um Reinigen früh verfügbar zu haben. B sieht drei Klang-/Licht-Arten und plant, das Stillefeld früh zu legen.
2. **Runde 1:** Das Sturm-Echo von A handelt zuerst (hohe Geschwindigkeit, Startzug-Formel CANON Kampf) und senkt die eigenen Zeitkosten. B antwortet mit einem Frost-Hauch auf den Sturm (Verlangsamt, ×1,3 Kosten) – auf der Zeitleiste rutscht das Sturm-Echo sichtbar nach hinten.
3. **Runde 2:** A baut über eine Kombo (Klang → Licht) 25 Harmonie auf. B legt das Stillefeld (Leere-Terrain, 1100 ‰); Klang-Fähigkeiten verlieren an Wirkung, Crescendos von Klang-Arten sind blockiert, solange Verstummt anliegt.
4. **Runde 3:** A reinigt mit dem Licht-Echo (Status weg) und legt ein Lichtfeld als Gegen-Terrain: Das Stillefeld endet (EndedBy). Die Zeitleiste zeigt, dass das Gift-Echo von B in zwei Zügen dran ist – A nutzt den Zug davor für eine Schild-Fähigkeit.
5. **Runde 4–6:** Beide Seiten tauschen Reserve-Echos (Wechsel kostet Zeitleisten-Zeit). A erreicht 100 Harmonie; das Crescendo wird angekündigt (goldener Marker, ein Zug Vorlauf). B hat genau einen Zug, um zu reagieren, und entzieht mit der Leere 30 Harmonie – das Crescendo fällt aus, weil die Leiste unter die Schwelle sinkt.
6. **Runde 7–9:** A baut erneut auf, diesmal mit dem Sturm-Echo als Tempo-Motor, und löst das Crescendo aus, als die Leere-Art in der Reserve ist. Zwei Echos von B verklingen.
7. **Ende (Minute 14):** B gibt nach einem weiteren Verlust auf und wählt die Verbeugung; A erwidert. Glicko-2 verschiebt beide Wertungen; das Replay ist 1,7 KB groß.

Jede Entscheidung war für beide Seiten sichtbar: die Verzögerungen, der Crescendo-Marker, das Terrain, die Harmonie. Genau diese Lesbarkeit macht Ranked in AETHRIS zu einem Spiel des Vorausdenkens statt der Reflexe (PZ-2).

### 4.4 Wertung: Glicko-2

Die Wertung nutzt **Glicko-2** (Glickman 2012): Jede Person hat eine Wertung R, eine Abweichung RD (Unsicherheit) und eine Volatilität σ. Jeder Kampf ist eine Bewertungsperiode. Neue Konten starten bei R 1500, RD 350. Wer eine Woche nicht spielt, bekommt RD-Zuwachs wie eine leere Periode (max. 350) – die sichtbare Stufe sinkt dadurch leicht, bis wieder gespielt wird; es gibt keinen harten Verfall.

```
Glicko-2 (ein Kampf gegen Gegner j, Ergebnis s ∈ {1; 0,5; 0}), Skala 173,7178:
  μ = (R − 1500)/173,7178     φ = RD/173,7178      μj, φj analog
  g(φj) = 1 / √(1 + 3φj²/π²)
  E = 1 / (1 + exp(−g(φj)·(μ − μj)))                    erwartetes Ergebnis
  v = 1 / (g(φj)² · E · (1 − E))                         Varianz
  Δ = v · g(φj) · (s − E)                                 Verbesserung
  σ' aus f(x) = eˣ(Δ² − φ² − v − eˣ) / (2(φ² + v + eˣ)²) − (x − ln σ²)/τ² = 0   (Illinois-Verfahren, τ = 0,5)
  φ* = √(φ² + σ'²)      φ' = 1/√(1/φ*² + 1/v)      μ' = μ + φ'² · g(φj) · (s − E)
  R' = 173,7178·μ' + 1500      RD' = 173,7178·φ'
```

Die Implementierung steht zweimal im Repository und wird gegeneinander getestet: als Referenz in Python (`aethris_pvp.glicko2_update`) und als C++ im Ranked-Dienst (`Aethris::Ranked::Update`). Der Test vergleicht 10.000 zufällige Kämpfe; Abweichungen > 10⁻⁶ sind Fehler.

Die **sichtbare Klangstufe** ergibt sich aus der konservativen Wertung **R − 2·RD**. So steigt man durch Spielen und Gewinnen; eine Glückssträhne mit hoher Unsicherheit hebt die Stufe nicht übermäßig.

| DisplayName | MinConservative | Subdivisions | Reward |
|---|---|---|---|
| Summen | 0 | 3 | Titel „Summende Stimme“ |
| Ruf | 1150 | 3 | Arena-Halle-Banner (Saisonfarbe) |
| Lied | 1350 | 3 | Geste „Saisonverbeugung“ |
| Chor | 1550 | 3 | Resonator-Muster der Saison |
| Hymne | 1750 | 3 | Gleiter-Muster der Saison |
| Weltakkord | 2050 | 1 | Titel „Weltakkord S#“ + Rahmen; Top 500 je Region mit Platzierung |

Unterstufen (I–III) teilen die Spanne bis zur nächsten Grenze gleichmäßig. Die höchste Stufe **Weltakkord** zeigt zusätzlich die Platzierung (Top 500 je Region).

### 4.5 Simulation

`aethris_pvp.py sim` simuliert 2.000 Personen mit normalverteilter „echter Stärke“ (Elo-Skala, σ 300), Matchmaking nach ähnlicher Wertung (bester aus 24 Kandidaten) und Glicko-2-Aktualisierung (deterministische Saat). Gemessen wird, wie gut die Wertung die echte Stärke wiedergibt (Rangkorrelation nach Spearman) und wie sich die Stufen verteilen:

| Kämpfe je Person (Ø) | Spearman (echte Stärke ↔ Wertung) | Ø RD |
|---|---|---|
| 5 | 0,760 | 182 |
| 10 | 0,879 | 128 |
| 20 | 0,946 | 90 |
| 40 | 0,977 | 69 |
| 60 | 0,984 | 63 |

| Klangstufe | Grenze (R − 2·RD) | Anteil nach 60 Kämpfen |
|---|---|---|
| Summen | 0 | 23,9 % |
| Ruf | 1150 | 22,9 % |
| Lied | 1350 | 24,4 % |
| Chor | 1550 | 17,4 % |
| Hymne | 1750 | 10,3 % |
| Weltakkord | 2050 | 1,0 % |

**Lesart:** Nach 5 Kämpfen (Platzierung) ist die Reihenfolge grob richtig (ρ ≈ 0,76), nach 20 Kämpfen sehr gut, nach 40 Kämpfen stabil (ρ > 0,97). Die Verteilung legt die Stufen so, dass die mittleren Stufen (Ruf, Lied, Chor) die meisten Spielenden tragen und Weltakkord etwa 1 % erreicht. Die Grenzen werden nach der Vorsaison (S0) mit echten Daten nachjustiert (K63).

### 4.6 Platzierung, Matchmaking, Pools

| Thema | Festlegung |
|---|---|
| Platzierung | 5 Kämpfe ohne sichtbare Stufe; danach Stufe aus R − 2·RD |
| Suche | Wertungsfenster ± 100 (RD-gewichtet), alle 15 s um 50 erweitert, max. ± 400; Region nach RTT ≤ 80 ms, nach 60 s Nachbarregion |
| Wiederholung | dieselbe Paarung höchstens 2× in 24 h (Schutz gegen Absprachen) |
| Crossplay | Standard; Filter Konsole/PC optional (verlängert die Suche) |
| Pools | Ranked Trio (Hauptliste), Saison-Nebenliste (Duell oder Saisonregel) |
| Mindestvoraussetzung | Wärterrang 28, 6 signierte, zulässige Echos |

### 4.7 Saisons

| Name | Start | End | Format | Special | Note |
|---|---|---|---|---|---|
| S0 | W3 | W14 | RS_RANKED_TRIO | – | Vorsaison: Ränge ohne Endbelohnung außer Titel |
| S1 | W16 | W27 | RS_RANKED_TRIO | RS_SEASON_SPECIAL | Zirkel-Chronik startet (K60) |
| S2 | W29 | W40 | RS_RANKED_TRIO | RS_RANKED_DUEL | Duell als Nebenrangliste |
| S3 | W42 | W53 | RS_RANKED_TRIO | RS_SEASON_SPECIAL | Jahresabschluss-Turnier (K68) |

Saisons dauern 12 Wochen mit einer Woche Pause (Saisonregel-Event). Zum Saisonende werden Wertungen **weich zurückgesetzt**: R' = 1500 + 0,5 × (R − 1500), RD' = max(RD, 150). Wer oben war, startet weiter oben, muss die Stufe aber bestätigen.

### 4.8 Team-Archetypen und Konter

Die Kampfsysteme aus K28–K33 ergeben mehrere tragfähige Team-Strategien. Keine davon ist ohne Konter – das ist eine Designvorgabe für das Balancing (K63) und ein Prüfstein für Meta-Signale (§7):

| Archetyp | Kernidee | Typische Werkzeuge | Konter |
|---|---|---|---|
| **Tempo** | Mehr Züge als die Gegenseite; Sturm-Zeitkosten senken, Haste | Sturm, Klang (Harmonie), schnelle Striker | Frost (Gegner-Zeitkosten +), Verlangsamt, Erschüttert/Starre (Fremdverzögerung bis 100 Ticks) |
| **Kontrolle** | Status und Verzögerung, Gegner kommt nicht zum Zug | Frost, Gift, Geist (Furcht), Schwerkraft | Licht (Reinigen), Status-Anti-Lock, Immunitäten je Typ, schnelle Einzelangriffe |
| **Harmonie/Crescendo** | Kombos und Harmonie aufbauen, Crescendo entscheidet | Klang, Kombo-Paare, Akkord-Teams | Leere (Harmonie-Entzug), Stillefeld, Verstummt blockiert Klang-Crescendos |
| **Terrain** | Eigenes Terrain legen und halten (Boost 1200 ‰) | Glutboden, Überwuchs, Kristallfeld | Gegen-Terrain (EndedBy), Flutfeld löscht Glut, Wetterwechsel |
| **Bollwerk** | Schilde, Heilung, Zeitlimit-Tiebreak über HP-‰ | Stein (Schilde), Blüte (Heilung), Tank-Rollen | Leere (Schilde entziehen), Gebrochen, Durchschlag; Tiebreak zählt verklungene Echos zuerst |
| **Formation** | Vorderreihe schützt Hinterreihe, Reihenwellen | Reihen-Fähigkeiten, Rückstoß, Positionswechsel | Rückstoß/Flut-Positionsverschiebung, Flächenangriffe |

Die Teamvorschau (nur Arten) ist das wichtigste Werkzeug gegen festgefahrene Strategien: Wer sieht, dass die Gegenseite drei Klang-Arten bringt, kann die Leere-Spezialistin nach vorn stellen.

### 4.9 Belohnungen

Belohnungen sind **ausschließlich kosmetisch** (DR-20, PV-06) und richten sich nach der **höchsten** in der Saison erreichten Stufe – kein Verlustdruck am Saisonende. Dazu kommen Teilnahme-Belohnungen (10/50/100 Ranked-Kämpfe: Gesten, Fotorahmen). Es gibt **kein Sol, keine Echos, keine Siegel** aus PvP (CANON Wirtschaft).

---

## 5. Arena-Halle frei, Freundeskampf, Geister-Teams

| Modus | Inhalt | Wertung |
|---|---|---|
| Arena-Halle frei | Duell, Duo, Trio; Norm 70; Ursprungsstimmen/Mythische erlaubt; verdeckte Glicko-2-Wertung nur für Matchmaking | keine sichtbare |
| Freundeskampf | alle Regeln frei wählbar: Norm/Eigen, Format, Wetter (auch Weltwetter), Items, Timer, „Gleichklang“ (alle Anlagen 15, Schliff ignoriert) | keine |
| Geister-Teams | Offline-Übung gegen gespeicherte Teams anderer Spielender (Freunde, Zirkel, Top-Teams der Woche) mit Kampf-KI-Profil Veteran (K34) | keine |
| Saisonregel | wechselnde Sonderregeln (z. B. „Kleine Stimmen“: nur Stufe-1-Arten, Norm 50) | eigene Rangliste |

**Geister-Teams** machen PvP auch ohne Verbindung erlebbar (NZ-1): Das Backend sammelt registrierte Ranked-Teams (anonymisiert, nur Arten, Fähigkeiten, Items, Aufstellung) und liefert wöchentlich 30 Teams in den Spielstand. Gespielt wird lokal gegen die Kampf-KI; die KI nutzt das Profil „Veteran“ mit der Aufstellung des Teams.

---

## 6. Zuschauen, Replays, Turniere

| Funktion | Festlegung |
|---|---|
| Zuschauen | Freunde und Zirkelmitglieder können laufende Kämpfe ansehen, **1 Zug Verzögerung** (kein Mitlesen in Echtzeit); im Ranked nur, wenn beide Spielenden es erlauben |
| Replays | Seed + Startzustand + Befehle (< 2 KB); Ranked 90 Tage, frei 30 Tage; teilen per Code (8 Zeichen); Zeitleiste vor/zurück, Perspektive wechseln |
| Analyse | Replay zeigt nach dem Kampf die vollständige Zeitleiste beider Seiten, verpasste Kombos, Effektivitäten |
| Turniere (LiveOps, K68) | Schweizer System im Spiel (5–7 Runden), danach K.-o.-Phase der Top 8; Regelsätze aus `Rulesets.csv`; Ausrichtung durch Studio oder Zirkel (ab Saison 2) |
| Übertragungsmodus | Für Events: Zuschauer-Kamera, beide Zeitleisten, Typ-Effektivitäten, Kommentar-freundliche Pausen |

---

## 7. Meta-Pflege

AETHRIS verzichtet zum Launch auf eine Bannliste. Die Meta wird über Daten beobachtet und mit **Saison-Patches** gepflegt (Balance-Werte nur per Patch, K59 §7.3).

| Signal | Schwelle | Reaktion |
|---|---|---|
| Nutzungsanteil einer Art (Ranked-Teams) | > 40 % über 2 Wochen | Prüfung (K63): Werte, Fähigkeiten, Konter |
| Siegquote einer Art (nutzungsgewichtet) | > 56 % bei Nutzung > 10 % | Prüfung |
| Kampfdauer Median | > 16 min (Trio) | Prüfung Defensiv-Strategien, Tiebreak |
| Anteil Zeitlimit-Enden | > 8 % | Prüfung „Hinhalte“-Strategien |
| Typ-Verteilung | ein Typ < 2 % der Teams | Prüfung Typ-Werkzeuge |
| Crescendo-Anteil an Siegen | > 50 % | Prüfung Harmonie-Ökonomie (K33) |

**Reihenfolge der Eingriffe:** (1) Konter stärken (andere Arten/Fähigkeiten), (2) Fähigkeit anpassen, (3) Basiswerte anpassen, (4) nur als letztes Mittel Saisonbeschränkung. Echos von Spielenden werden nie entwertet, ohne dass ihre Pflege (Anlagen, Schliff) erhalten bleibt.

---

## 8. Fair Play

| Verhalten | Erkennung | Folge |
|---|---|---|
| Kampf verlassen / Verbindung trennen | Server: kein Wiederverbinden in 60 s | Niederlage; ab 3 in 24 h Wartezeit 15 min, dann 1 h |
| Bewusstes Hinhalten | Bank leer + 3× Abwarten | automatische Aufgabe |
| Absprachen (Win-Trading) | gleiche Paarung, unplausible Muster (Sofort-Aufgaben) | Wertung zurückgesetzt, Sperre Ranked |
| Zweitkonten zum Absenken | Konto-Verknüpfung, Verhaltensmuster | Sperre Ranked |
| Manipulierte Echos | Legalität (K59 §9.3) | Echo nicht zulässig; wiederholte Versuche → Online-Sperre |
| Belästigung (Namen, Gesten-Spam) | Meldung + Prüfung; Gesten im Kampf max. 1 je Zug | Kommunikationssperre |

Gesten sind die einzige Kommunikation im Ranked: Gruß vor und nach dem Kampf, eine Geste je Zug. Spielende können Gesten der Gegenseite ausblenden.

---

## 9. UX

```
ARENA-HALLE (Menü „Online“ oder Arena-Terminal in jeder Stadt)
 ├─ Ranked Trio   [Stufe: Lied II · Saison S1 · Woche 5/12]  ▸ Team wählen ▸ Suchen (≈ 30 s)
 ├─ Saison-Nebenliste
 ├─ Frei: Duell · Duo · Trio
 ├─ Freundeskampf ▸ Regeln ▸ Einladen
 ├─ Geister-Teams (offline)
 ├─ Replays · Zuschauen
 └─ Rangliste (Region/Freunde/Zirkel)

TEAMVORSCHAU (90 s)
 ┌ Eigenes Team (6) ───────────────┐   ┌ Gegenseite (6 Arten, Typsymbole) ┐
 │ ▣ Vorderreihe  ▣ Hinterreihe    │   │ ◆ ◆ ◆ ● ● ●                     │
 │ Norm 70: Werte-Vorschau je Echo │   │ Typ-Effektivität (Wort + Symbol) │
 └─────────────────────────────────┘   └──────────────────────────────────┘
```

| UX-Regel | Umsetzung |
|---|---|
| Norm-Hinweis | Echos über/unter Level 70 zeigen in der Teamwahl „Im Ranked: Werte bei Level 70“ mit Vorschau |
| Zeit | Zugtimer als Kreis um das aktive Echo; Bank als Leiste; 10 s vorher Ton + Pulsieren |
| Lesbarkeit | Gegnerische Fähigkeiten werden erst bei Nutzung enthüllt; danach im Kampf sichtbar |
| Barrierefreiheit | Zugtimer im Freundeskampf abschaltbar; im Ranked fest (Fairness), aber Zeitleisten-Erklärmodus (ACC_TIMELINE_EXPLAIN) bleibt aktiv |
| Nach dem Kampf | Wertungsänderung, Stufenfortschritt, Replay-Knopf, Gruß |

---

## 10. Technik

| Baustein | Umsetzung |
|---|---|
| Kampfserver | `AethrisServer` mit GF_Combat + GF_PvP; Befehle/Ergebnisse (K59 §5) |
| Normalisierung | beim Laden des Teams auf dem Server: `Aethris::Stats::ComputeHP/ComputeCore` mit `Aethris::Ranked::NormLevel` |
| Ranked-Dienst | Glicko-2 (`Aethris::Ranked::Update`), Stufen (`TierFor`), Saisons, Ranglisten (Redis-Sorted-Sets je Region) |
| Replays | Objektspeicher; Abspielen im Client mit identischem GF_Combat-Code (Determinismus-Test, K59 §12) |
| Geister-Teams | wöchentlicher Export aus registrierten Teams, im Spielstand als Fragment `Player.GhostTeams` (K64) |

```
Server: Kampfende (Ranked)
  ergebnis ← Sieg | Niederlage | Tiebreak(verklungen, HP-‰, Bank) | Aufgabe
  für beide Seiten: neu ← Aethris::Ranked::Update(selbst, gegner, score)
  speichere neu, Replay-ID, Dauer, Teams (für Meta-Statistik, anonymisiert)
  sichtbare Stufe ← TierFor(neu.Conservative()) (erst nach 5 Kämpfen)
  höchste Saisonstufe aktualisieren (für Belohnungen)
```

---

## 11. Telemetrie

| Kennzahl | Ziel | Zweck |
|---|---|---|
| Wartezeit Median (Ranked) | ≤ 45 s | Matchmaking |
| Kampfdauer Median (Trio) | 10–15 min | DR-11 |
| Zeitlimit-Enden | ≤ 5 % | Tiebreak, Hinhalten |
| Verlassen-Quote | ≤ 3 % | Fair Play |
| Unterschiedliche Arten in Top-1.000-Teams | ≥ 80 | Vielfalt (PZ-4) |
| Anteil Spielender mit ≥ 10 Ranked-Kämpfen je Saison | ≥ 15 % der Online-Aktiven | Beteiligung |

---

## 12. Prüfregeln

`tools/ref/aethris_pvp.py validate`:

| Regel | Inhalt |
|---|---|
| PV-01 | 240 Arten Ranked-zulässig (ohne Ursprungsstimmen, Mythische) |
| PV-02 | Normalisierung = Formeln K18 |
| PV-03 | Stufengrenzen steigend; höchste Stufe ≤ 2 % |
| PV-04 | Spearman ≥ 0,90 nach 40 Kämpfen |
| PV-05 | Ranked: Norm, ≤ 20 min, Klar, keine Verbrauchsgüter |
| PV-06 | Belohnungen kosmetisch |

**Ergebnis:** Prüfregeln PV-01–PV-06: **0 Verstöße**. Ranked-zulässig: 240 Arten; Normstufe 70; Simulation 2000 Personen × 60 Kämpfe: Spearman nach 40 Kämpfen 0,977, höchste Stufe 1,0 %.

**Hinweis an K63 (erledigt):** Die erste Fassung dieses Kapitels zeigte, dass zwei Arten (Pyroluth #137 und Skriveth #181) identische Basiswerte hatten. K63 hat alle 54 solcher Gruppen über Identitätsakzente aufgelöst (`Data/Balance/StatAccents.csv`, Prüfregel BL-01); die Tabelle in §2.2 zeigt bereits die neuen Werte.

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Balancing | Stufengrenzen nach S0 nachjustieren; Meta-Signale §7; Basiswert-Dubletten (in K63 behoben) | K63 |
| Kampf-KI | Profil Veteran mit fester Aufstellung für Geister-Teams | K34 |
| UI | Arena-Halle, Teamvorschau, Norm-Hinweis, Replay-Ansicht, Ranglisten | K54 |
| Backend | Ranked-Dienst, Saison-Reset, Ranglisten, Geister-Team-Export | K59 |
| LiveOps | Saisonkalender, Saisonregeln, Turniere | K68 |
| Save | `Player.GhostTeams`, Profil: Saisonstufen, Titel | K64 |
| QA | Tiebreak-Fälle, Zeitlimit, Verbindungsabbruch, Determinismus Replays | K66 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-249 | Q5: Normstufe 70 mit echten Anlagen/Schliff | Story-Endstand, kein Grind, Pflege zählt | keine Normalisierung; Norm 50/100; Spielerwahl |
| ADR-250 | Glicko-2 mit sichtbarer Stufe aus R − 2·RD | Unsicherheit berücksichtigt, kein Punkte-Grind, schnelle Konvergenz (ρ 0,977 nach 40) | Elo; Punktesystem mit Verlustschutz |
| ADR-251 | Schachuhr (30 s + 90 s Bank) und Tiebreak verklungen → HP-‰ → Bank | DR-11, belohnt aktives Spiel | festes Rundenlimit; Sudden Death |
| ADR-252 | Keine Bannliste zum Launch, Meta-Pflege über Signale und Saison-Patches | Vielfalt durch Daten, Konter zuerst | Bannliste ab Tag 1 |
| ADR-253 | Belohnungen nach höchster Saisonstufe, nur kosmetisch | Kein Verlustdruck, DR-20 | Endstand-Belohnung; Echos/Sol |
| ADR-254 | Geister-Teams als Offline-PvP | NZ-1, Übung ohne Druck | nur Online-PvP |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §240 | Q5: Normstufe 70 (Ranked, freie Arena standard), Anlagen/Schliff/Persönlichkeit zählen; Gehorsam voll; 240 zulässige Arten; Art-Klausel; Halteitems ohne Duplikate; keine Verbrauchsgüter; Klar; Crescendo kurz | LOCKED (schließt Q5) |
| §241 | Regelsätze `Rulesets.csv` (Ranked Trio/Duell, frei Duell/Duo/Trio, Freundeskampf inkl. Gleichklang, Geister-Teams, Saisonregel); Teamvorschau Arten 90/60 s | LOCKED |
| §242 | Ranked: Glicko-2 (Start 1500/350/0,06, τ 0,5), sichtbare Klangstufe aus R − 2·RD (`RankTiers.csv`: Summen 0, Ruf 1150, Lied 1350, Chor 1550, Hymne 1750, Weltakkord 2050), Platzierung 5, Wochen-RD-Zuwachs, Saisons 12 + 1 Wochen (`SeasonCalendar.csv`), weicher Reset R' = 1500 + 0,5(R − 1500), RD' ≥ 150; Schachuhr 30 s + 90 s; Zeitlimit 20/15 min; Tiebreak; Belohnung nach höchster Stufe, kosmetisch | LOCKED |
| §243 | Fair Play (Verlassen, Hinhalten, Absprachen, Zweitkonten), Gesten als einzige Kommunikation, Zuschauen mit 1 Zug Verzögerung, Replays 90/30 Tage, Turniere (Schweizer System), Meta-Signale und Eingriffsreihenfolge, keine Bannliste zum Launch | LOCKED |
| Q-Liste | Q5 geschlossen (→ §240) | – |
| §10 | ADR-249 – ADR-254 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Ziele PZ-1–PZ-6
- [x] Q5 entschieden (Optionen, Normstufe 70, Beispielrechnung, Investitionswirkung)
- [x] Regelsätze, Teamvorschau, Aufstellung
- [x] Ranked: Ablauf, Zeit, Tiebreak, Glicko-2, Stufen, Simulation, Matchmaking, Saisons, Belohnungen
- [x] Freie Arena, Freundeskampf, Geister-Teams, Zuschauen, Replays, Turniere
- [x] Meta-Pflege, Fair Play, UX, Technik (C++ Glicko-2), Telemetrie
- [x] Prüfregeln PV-01–PV-06 (0 Verstöße), Hinweis an K63 (erledigt)
- [x] Anforderungen, ADR-249 – ADR-254, CANON §240–§243

➡️ **Nächstes Kapitel: K62 – Endgame.**
