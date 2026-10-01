# K30 · Fähigkeiten III – Crescendos und Feldfähigkeiten

| Feld | Wert |
|---|---|
| Dokument | Kapitel 30 von 68 · Combat Guide, Teil III |
| Version | 1.0 |
| Owner | Lead Combat Designer (Crescendo), Lead World Designer (Feld) |
| Mitwirkende | RPG Systems Designer, Cinematics Lead (Crescendo-Inszenierung), Traversal Designer, Level Design, Audio Lead, Technical Designer |
| Baut auf | K28/K29 (CANON §97–§105), CANON §6 (Harmonie, Crescendo), §18 (Crescendo ab Bindungsstufe 2, Feld ab 1), §15 (Traversal-Reihenfolge), DR-24, DR-28 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Abilities/Abilities.csv` (+30 Crescendos, +30 Feld = **330**), `Data/Echos/CrescendoOptions.csv` (814), `Data/Echos/FieldOptions.csv` (240), `tools/authoring/abilities_k30.py`, `tools/gen_learnsets.py` (LS-13/14), `tools/gen_abilities.py validate --final` |
| Neue Kanon-Einträge | CANON §106 (Crescendo-Regeln), §107 (Feldfähigkeiten & Pfad-Tore), §108 (Fähigkeiten-Gesamtbestand) |

---

## Inhalt

1. [Crescendo – der Höhepunkt eines Kampfes](#1-crescendo--der-höhepunkt-eines-kampfes)
2. [Regeln und Kosten](#2-regeln-und-kosten)
3. [Inszenierung](#3-inszenierung)
4. [Die 30 Crescendos](#4-die-30-crescendos)
5. [Crescendo-Optionen der Arten](#5-crescendo-optionen-der-arten)
6. [Feldfähigkeiten – Echos in der Welt](#6-feldfähigkeiten--echos-in-der-welt)
7. [Pfad-Tore und Gating](#7-pfad-tore-und-gating)
8. [Die 30 Feldfähigkeiten](#8-die-30-feldfähigkeiten)
9. [Feldfähigkeiten der Arten](#9-feldfähigkeiten-der-arten)
10. [Der vollständige Fähigkeitenbestand](#10-der-vollständige-fähigkeitenbestand)
11. [Code](#11-code)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Crescendo – der Höhepunkt eines Kampfes

Ein **Crescendo** ist die Ultimate-Ausführung eines Echos: Der Chor hat durch Kombos, Treffer und Klang-Fähigkeiten **Harmonie** aufgebaut (K33), und ein Echo, das seinem Wärter vertraut (Bindungsstufe ≥ 2), entlädt sie in einer großen Geste. Crescendos sind **selten, sichtbar angekündigt und kampfentscheidend** – in einem Arenakampf (8–15 min, DR-11) erwarten wir 2–4 Crescendos pro Seite.

| Designziel | Umsetzung |
|---|---|
| Höhepunkt statt Routine | Harmoniekosten 60–90 von 100; Aufbau ~4–6 Züge |
| Bindung zählt (S2) | Erst ab Bindungsstufe 2 im Kampfset; Bindungsstufe 5+ senkt Kosten um 10 |
| Gegenspiel (DR-07) | Crescendo erscheint 1 Zug vorher als **Ankündigung** auf der Zeitleiste; Leere-Fähigkeiten können Harmonie entziehen, Verstummt blockiert `Sound`-Crescendos |
| Kein toter Zug (DR-10) | Wird der Anwender vor Ausführung verklungen, fließen 50 % der Kosten zurück |
| Typ-Identität (DR-08) | Je Typ ein Schadens- und ein Team-Crescendo, beide mit Identitätsmarken |

---

## 2. Regeln und Kosten

| Regel | Wert |
|---|---|
| Machtbudget | 200–320 MP (AB-08) – etwa das Doppelte einer schweren aktiven Fähigkeit |
| Zeitkosten | immer **200** (Deckel der Zeitkostenformel, K28 §3) – ein Crescendo ist eine volle Zusage |
| Harmoniekosten | clamp(rund10(60 + (V − 200)/3), 60, 100) → 60–90 |
| Ankündigung | Beim Wählen wird das Crescendo als goldener Marker an die Zielposition der Zeitleiste gesetzt; erst dort wird es ausgeführt (K31) |
| Begrenzung | 1 Crescendo pro Echo und Kampf; pro Seite und Runde höchstens 1 |
| Bindung | ab Bindungsstufe 2 wählbar; Stufe 5–6: Harmoniekosten −10 |
| Formate | Duell/Duo/Trio/Raid identisch; im Raid teilen sich Spieler eine Harmonie je Gruppe (K35) |
| PvP | erlaubt; Feldklänge nicht (CANON §103) |

**Harmonie-Ökonomie (Vorgabe für K33):** Treffer +5, sehr effektiver Treffer +8, Kombo +10–20, Klang-Effekte laut Daten, Fehlschlag einer Status-Fähigkeit +5 (DR-10), erlittener Volltreffer +5. Die Leiste fasst 100.

---

## 3. Inszenierung

```
 t=0,0 s  Wahl bestätigt → goldener Ankündigungsmarker auf der Zeitleiste, Chor-Akkord (Audio K55)
 …        andere Züge laufen weiter; Gegner sehen den Marker (Gegenspiel)
 t=0      Ausführung: Kamera-Übernahme (max. 4,0 s, überspringbar ab 2. Sicht / Option „kurz“ 1,5 s)
          ├─ 0,0–0,8 s  Anlauf: Klangmal des Echos leuchtet, Typfarbe füllt den Bildrand
          ├─ 0,8–2,6 s  Entladung: Typ-VFX (K58), Klangsignatur der Art
          └─ 2,6–4,0 s  Nachhall: Treffer-Zahlen, Status-Symbole, Kamera zurück
```

- **Barrierefreiheit:** Option „Crescendo kurz“ (1,5 s) und „ohne Kameraflug“; Ankündigung mit Symbol + Ton (DR-24).
- **Koop/PvP:** Inszenierung läuft lokal, Logik serverseitig; PvP immer Kurzfassung (≤ 1,5 s) zur Einhaltung von DR-11.
- **Signatur:** Arten, deren Katalog-Signaturkonzept ein Crescendo beschreibt, führen ihr bevorzugtes Crescendo (★) mit eigener Variante aus (Kamera, Klangmal, Ruf) – Mechanik identisch.

---

## 4. Die 30 Crescendos

Spalte **Zeit** ist bei allen 200; die Harmoniekosten stehen als `HarmonyCost` in den Tags (Daten: Spalte `Tags`).

### 4.1 Glut · Flut · Stein
| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U001 | **Sonnensturz** | Spez. | 150 | 90 % | Enemies | 200 | 253 | Spezieller Schaden, Stärke 150, gegen alle Gegner; erzeugt Glutboden für 3 Runden. |
| ABL_U002 | **Phönixlied** | Stat. | – | – | Allies | 200 | 204 | Wirkt auf alle Verbündeten; belebt einen verklungenen Verbündeten mit 50 % HP wieder; heilt alle Verbündeten um 30 % der max. HP; ANG +1 für alle Verbündeten; entfernt negative Status von alle Verbündeten; alle Verbündeten rücken 40 Ticks auf der Zeitleiste vor. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U003 | **Weltflut** | Spez. | 140 | 95 % | Enemies | 200 | 259 | Spezieller Schaden, Stärke 140, gegen alle Gegner; stößt das Ziel in die Hinterreihe; ruft Regen für 3 Runden herbei. |
| ABL_U004 | **Gezeitenschoß** | Stat. | – | – | Allies | 200 | 206 | Wirkt auf alle Verbündeten; alle Verbündeten heilt 3 Runden je 10 % der max. HP; entfernt negative Status von alle Verbündeten; Schild für alle Verbündeten (20 % der max. HP); heilt alle Verbündeten um 40 % der max. HP; Harmonie +10. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U005 | **Bergsturz** | Phys. | 160 | 90 % | Row | 200 | 224 | Physischer Schaden, Stärke 160, gegen eine gegnerische Reihe; 50 % Chance auf Erschüttert. |
| ABL_U006 | **Ewiger Fels** | Stat. | – | – | Allies | 200 | 205 | Wirkt auf alle Verbündeten; Schild für alle Verbündeten (35 % der max. HP); VER +2 für alle Verbündeten; SVE +1 für alle Verbündeten; Gegner müssen 1 Runde(n) den Anwender angreifen; heilt alle Verbündeten um 15 % der max. HP; Harmonie +10. |

### 4.2 Sturm · Blüte · Frost
| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U007 | **Himmelszorn** | Spez. | 75 | 90 % | Enemies | 200 | 236 | Spezieller Schaden, Stärke 75, gegen alle Gegner; trifft 2–2-mal; Stärke ×1,5 bei Gewitter. |
| ABL_U008 | **Orkanschwinge** | Stat. | – | – | Allies | 200 | 204 | Wirkt auf alle Verbündeten; alle Verbündeten rücken 100 Ticks auf der Zeitleiste vor; GES +2 für alle Verbündeten; ruft Gewitter für 4 Runden herbei; AUS +1 für alle Verbündeten; Harmonie +20. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U009 | **Urwaldchor** | Stat. | – | – | Allies | 200 | 214 | Wirkt auf alle Verbündeten; heilt alle Verbündeten um 50 % der max. HP; alle Verbündeten heilt 3 Runden je 8 % der max. HP; erzeugt Überwuchs für 5 Runden; entfernt negative Status von alle Verbündeten. |
| ABL_U010 | **Dornenmeer** | Phys. | 130 | 95 % | Enemies | 200 | 229 | Physischer Schaden, Stärke 130, gegen alle Gegner; Ziel kann 2 Runde(n) die Reihe nicht wechseln. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U011 | **Ewiger Winter** | Spez. | 120 | 90 % | Enemies | 200 | 221 | Spezieller Schaden, Stärke 120, gegen alle Gegner; alle Gegner rücken 60 Ticks auf der Zeitleiste zurück. |
| ABL_U012 | **Eiszeit** | Stat. | – | 90 % | Enemies | 200 | 209 | Wirkt auf alle Gegner; 70 % Chance auf Starre; ruft Schneefall für 5 Runden herbei; GES −2 für alle Gegner; PRÄ −1 für alle Gegner; erzeugt Eisfläche für 4 Runden. |

### 4.3 Leere · Licht · Gift
| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U013 | **Weltlöscher** | Spez. | 180 | 85 % | Single | 200 | 218 | Spezieller Schaden, Stärke 180, gegen einen Gegner; entfernt Schilde und positive Stufen von das Ziel; durchdringt Schilde; entzieht dem Gegnerteam 20 Harmonie. |
| ABL_U014 | **Große Leere** | Stat. | – | 95 % | Enemies | 200 | 211 | Wirkt auf alle Gegner; entfernt Schilde und positive Stufen von alle Gegner; entzieht dem Gegnerteam 40 Harmonie; verursacht Entzug; erzeugt Stillefeld für 4 Runden; SAN −1 für alle Gegner. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U015 | **Zenitfeuer** | Spez. | 150 | 100 % | Enemies | 200 | 280 | Spezieller Schaden, Stärke 150, gegen alle Gegner; enthüllt das Ziel (Ausweichen, Täuschung und Tarnung wirkungslos); verfehlt nie. |
| ABL_U016 | **Morgenweihe** | Stat. | – | – | Allies | 200 | 200 | Wirkt auf alle Verbündeten; entfernt negative Status von alle Verbündeten; heilt alle Verbündeten um 40 % der max. HP; Schild für alle Verbündeten (20 % der max. HP); PRÄ +1 für alle Verbündeten; Harmonie +20. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U017 | **Pestwolke** | Spez. | 90 | 95 % | Enemies | 200 | 246 | Spezieller Schaden, Stärke 90, gegen alle Gegner; verursacht Vergiftet (3 Stapel). |
| ABL_U018 | **Säureflut** | Spez. | 130 | 90 % | Row | 200 | 243 | Spezieller Schaden, Stärke 130, gegen eine gegnerische Reihe; VER −2 für das Ziel; SVE −2 für das Ziel. |

### 4.4 Metall · Geist · Kristall
| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U019 | **Schmiedehammer** | Phys. | 180 | 90 % | Single | 200 | 207 | Physischer Schaden, Stärke 180, gegen einen Gegner; verursacht Gebrochen. |
| ABL_U020 | **Eherne Phalanx** | Stat. | – | – | Allies | 200 | 204 | Wirkt auf alle Verbündeten; Schild für alle Verbündeten (30 % der max. HP); VER +2 für alle Verbündeten; kontert den nächsten physischen Angriff mit 100 % Schaden; SVE +1 für alle Verbündeten; Harmonie +20. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U021 | **Geisterheer** | Spez. | 100 | 100 % | Enemies | 200 | 217 | Spezieller Schaden, Stärke 100, gegen alle Gegner; ignoriert Formationsschutz; 50 % Chance auf Furcht. |
| ABL_U022 | **Seelenrückkehr** | Stat. | – | – | Allies | 200 | 204 | Wirkt auf alle Verbündeten; belebt einen verklungenen Verbündeten mit 60 % HP wieder; erschafft ein Trugbild, das den nächsten Angriff abfängt; AUS +1 für alle Verbündeten; heilt alle Verbündeten um 30 % der max. HP; Harmonie +20. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U023 | **Prismenkatarakt** | Spez. | 120 | 90 % | Enemies | 200 | 202 | Spezieller Schaden, Stärke 120, gegen alle Gegner; benötigt eine Aufladerunde (sichtbar auf der Zeitleiste); 50 % Chance auf Gebrochen. |
| ABL_U024 | **Spiegelpalast** | Stat. | – | – | Allies | 200 | 204 | Wirkt auf alle Verbündeten; reflektiert den nächsten speziellen Angriff; reflektiert den nächsten physischen Angriff; Schild für alle Verbündeten (25 % der max. HP); lädt den Anwender auf: nächster Angriff +50 % Stärke; SVE +2 für alle Verbündeten; Harmonie +10. |

### 4.5 Klang · Schwerkraft · Arkan
| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U025 | **Sinfonie der Welt** | Spez. | 110 | 100 % | Enemies | 200 | 239 | Spezieller Schaden, Stärke 110, gegen alle Gegner; alle Gegner rücken 50 Ticks auf der Zeitleiste zurück; Harmonie +20. |
| ABL_U026 | **Großer Takt** | Stat. | – | – | Allies | 200 | 227 | Wirkt auf alle Verbündeten; alle Verbündeten rücken 80 Ticks auf der Zeitleiste vor; Harmonie +40; ANG +1 für alle Verbündeten; SAN +1 für alle Verbündeten; entfernt negative Status von alle Verbündeten; GES +1 für alle Verbündeten. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U027 | **Ereignishorizont** | Spez. | 140 | 90 % | Enemies | 200 | 249 | Spezieller Schaden, Stärke 140, gegen alle Gegner; zieht das Ziel in die Vorderreihe; Ziel kann 2 Runde(n) die Reihe nicht wechseln. |
| ABL_U028 | **Schwerkraftsturz** | Phys. | 190 | 85 % | Single | 200 | 226 | Physischer Schaden, Stärke 190, gegen einen Gegner; vertauscht die gegnerischen Reihen; GES −2 für das Ziel. |

| ID | Name | Kat. | Stärke | Gen. | Ziel | Zeit | MP | Wirkung |
|---|---|---|---|---|---|---|---|---|
| ABL_U029 | **Formel des Ursprungs** | Spez. | 140 | 95 % | Enemies | 200 | 266 | Spezieller Schaden, Stärke 140, gegen alle Gegner; ändert den Typ von das Ziel für 2 Runden zu Arkan. |
| ABL_U030 | **Umkehr der Welt** | Stat. | – | – | Field | 200 | 221 | Kehrt die Typtabelle für 2 Runde(n) um (angekündigt); stiehlt die positiven Stufen des Ziels; kopiert die zuletzt vom Ziel eingesetzte Fähigkeit; erzeugt Glyphenfeld für 4 Runden; SAN +2 für alle Verbündeten. |

**Bemerkenswerte Kombinationen** (bewusst zugelassen, in K63 überwacht):
- *Formel des Ursprungs* (Arkan) verwandelt alle Gegner in Arkan – Arkan ist gegen Arkan sehr effektiv (K17). Zwei Züge Fenster für Arkan-Teams.
- *Ereignishorizont* (Schwerkraft) zieht alle Gegner nach vorn und bindet sie – ideal vor *Bergsturz* (Stein, Reihe).
- *Große Leere* gegen Harmonie-Teams: Entzug 40 + Stillefeld blockiert gegnerische Crescendos für mehrere Runden. Konter: Licht-Reinigen, Klang-Harmonie außerhalb des Stillefelds (K32).

---

## 5. Crescendo-Optionen der Arten

Jede Art kann **alle Crescendos ihrer Typen** lernen (2 bei Einzeltyp, 4 bei Doppeltyp). Eines ist als **bevorzugt (★)** markiert: Schadens-Crescendo des Primärtyps für Striker, Caster und Speed; Team-Crescendo für Tank, Support, Control und AllRound. Das bevorzugte Crescendo ist bei Wildechos und NPC-Wärtern gesetzt und trägt die Signatur-Inszenierung.

| Kennzahl | Wert |
|---|---|
| Optionen gesamt | 814 |
| Arten mit 2 / 4 Optionen | Einzeltyp / Doppeltyp |
| Erwerb | automatisch beim Erreichen von Bindungsstufe 2 (alle Optionen ins Repertoire) |

---

## 6. Feldfähigkeiten – Echos in der Welt

Feldfähigkeiten machen Echos zu **Partnern in der offenen Welt** (Säule S1/S2). Ein Echo im Chor mit Bindungsstufe ≥ 1 kann seine Feldfähigkeit über das Begleiter-Rad (K54) einsetzen. Sie ersetzen klassische „Schlüssel-Items“: Wer ein Frost-Echo mitführt, überquert den See über eine Eisbrücke – wer ein Flut-Echo dabei hat, watet durch das Flachwasser. Mehrere Lösungen pro Hindernis sind Pflicht.

| Regel | Wert |
|---|---|
| Verfügbarkeit | ab Bindungsstufe 1 (CANON §18), Echo im aktiven Chor |
| Kosten | Echo-Ausdauer (K40): Traversal 25, Sinne 10, Sammeln 10, Rätsel 15, Sozial 10; regeneriert 5/s außerhalb des Kampfes |
| Kategorien (Tag) | `Field.Traversal` · `Field.Sense` · `Field.Gather` · `Field.Puzzle` · `Field.Social` |
| Bedingung | Art muss Typ der Fähigkeit tragen **und** Merkmal/Größe erfüllen (z. B. Glutschmelze: Größe ≥ M) |
| Je Art | 0–1 Feldfähigkeit (CANON §18), festgelegt in `FieldOptions.csv` |
| Reittiere | Reitarten (Boden/Klettern/Schwimm/Grab/Flug) sind **keine** Feldfähigkeiten, sondern Art-Eigenschaft `Mount` (K40) |

---

## 7. Pfad-Tore und Gating

Die Welt nutzt **Pfad-Tore** – markierte Hindernisse mit festem Typ. DR-28 verlangt, dass der Hauptpfad jeder Region mit der frühesten Traversal-Ausstattung spielbar ist; Pfad-Tore liegen daher nur auf **Nebenpfaden** (Schätze, Abkürzungen, Nebenquests, Kodex).

| Tor-Typ | Lösungen (Feldfähigkeit · Alternative) | Regionen-Schwerpunkt |
|---|---|---|
| Eis/Dorn | Glutschmelze · Giftschneise (Dorn) · Werkzeug „Klinge“ (K40) | R07, R01, R03 |
| Geröll | Felsbrecher · Schwebelast | R02, R05 |
| Spalt | Rankenbrücke · Eisbrücke (über Wasserspalt) · Gleiter | R01, R08 |
| Wasser | Wasserlauf · Eisbrücke · Schwimmreittier | R03, R06 |
| Gestrüpp | Giftschneise · Glutschmelze | R03, R01 |
| Dunkel | Fackelschein · Leuchtfeuer · Laterne (Item) | R09, R05 |
| Mechanik | Mechanik · Schwebelast (Gegengewicht) | R08, R10 |
| Ahnen | Seelenpfad · Geistersicht (zeigt Lösungsweg) | R07, R08 |
| Prisma | Lichtlenker · Leuchtfeuer (schwächer, längerer Weg) | R09, R04 |
| Glyphe | Glyphenlesen · Kodex-Hinweis (Skill Forschung, K43) | R08, R04 |
| Siegel | Siegelöffner · Fraktions-Schlüssel (K47) | alle |
| Last | Schwebelast · Felsbrecher (zerstört statt verschiebt) | R10, R02 |

**Regel PT-1:** Jedes Pfad-Tor hat ≥ 2 Lösungen, davon ≥ 1 ohne bestimmten Typ (Item, Skill, Umweg). **PT-2:** Kein Pfad-Tor auf dem Hauptpfad (Validator in K40 über Level-Daten). **PT-3:** Pro Region mindestens 6 Pfad-Tor-Typen (Vielfalt).

---

## 8. Die 30 Feldfähigkeiten

Spalte **Auslöser** enthält hier die **Bedingung** (Merkmal oder Größe).

| ID | Name | Auslöser | Wirkung | Tags |
|---|---|---|---|---|
| ABL_F001 | **Fackelschein** | Trait:Glowing|Trait:Thermal | Erhellt dunkle Höhlen (Radius 12 m) und verscheucht lichtscheue Wildechos. | Field.Sense |
| ABL_F002 | **Glutschmelze** | Size:M+ | Schmilzt Eisbarrieren und brennt Dornengestrüpp nieder (Pfad-Tor Typ „Eis/Dorn“, K40). | Field.Traversal |
| ABL_F003 | **Quellsucher** | Trait:Swimmer|Trait:Filterer | Findet Süßwasserquellen und Muschelbänke; +1 Wasser-/Perlen-Ressource je Fundstelle. | Field.Gather |
| ABL_F004 | **Wasserlauf** | Size:M+ | Trägt den Wärter über flaches Wasser (≤ 1,2 m) ohne Schwimmreittier; Gezeitenpfade bei Ebbe. | Field.Traversal |
| ABL_F005 | **Felsbrecher** | Size:M+ | Zerschlägt rissige Felsblöcke (Pfad-Tor „Geröll“). | Field.Traversal |
| ABL_F006 | **Erzspur** | Trait:Lithophage|Trait:Burrower | Markiert Erzadern im Resonanzsinn (Radius 40 m); +1 Erz je Abbau. | Field.Gather |
| ABL_F007 | **Aufwind** | Trait:Flier|Trait:Drifter | Erzeugt eine Thermiksäule für den Gleiter (+18 m Höhe, 1× je 60 s). | Field.Traversal |
| ABL_F008 | **Wetterwitterung** | Trait:Migratory|Trait:Flier | Zeigt das Wetter der nächsten 2 Wetterblöcke an (Vorhersage K14 §11). | Field.Sense |
| ABL_F009 | **Rankenbrücke** | Size:S+ | Lässt Ranken über Spalten bis 6 m wachsen (Pfad-Tor „Spalt“, 3 min). | Field.Traversal |
| ABL_F010 | **Kräuterkunde** | Trait:Pollinator|Trait:Grazer | Findet Heilkräuter; +1 Kräuter je Sammelpunkt, seltene Kräuter sichtbar. | Field.Gather |
| ABL_F011 | **Eisbrücke** | Size:S+ | Friert Wasserflächen zu begehbarem Eis (Radius 8 m, 90 s). | Field.Traversal |
| ABL_F012 | **Frischhalter** | Trait:Hunter|Trait:Collector | Kühlt Proviant: Lager-Gerichte halten einen Spieltag länger (K41). | Field.Gather |
| ABL_F013 | **Stillesinn** | Any | Zeigt Stillezonen und Stillsteine im Umkreis von 150 m an (Hauptquest-Relevanz, K44). | Field.Sense |
| ABL_F014 | **Schattenschritt** | Trait:Camouflaged|Trait:Ambusher | Wärter wird 20 s lang von Wildechos und Wachen schwer bemerkt (Schleichen, K53). | Field.Social |
| ABL_F015 | **Leuchtfeuer** | Trait:Glowing | Erhellt Umgebung (Radius 20 m) und markiert versteckte Kisten/Fragmente. | Field.Sense |
| ABL_F016 | **Lichtsignal** | Any | Sendet ein Signal an Koop-Partner und NPC-Wachen (Ping, Hilferuf, Händlerruf). | Field.Social |
| ABL_F017 | **Giftschneise** | Size:S+ | Zersetzt Moorgestrüpp und Pilzwände (Pfad-Tor „Gestrüpp“). | Field.Traversal |
| ABL_F018 | **Ködermischer** | Trait:Ambusher|Trait:Hunter | Verbessert eigene Lockmittel: +20 % Wirkung auf Bindungs-Köder (K36). | Field.Gather |
| ABL_F019 | **Erzwitterung** | Trait:Collector|Trait:ToolUser | Findet Metallteile und Relikte im Boden (Grab-Punkte im Resonanzsinn). | Field.Gather |
| ABL_F020 | **Mechanik** | Trait:ToolUser | Bedient dorunische Mechanismen und Kontor-Winden (Rätsel-Tor „Mechanik“). | Field.Puzzle |
| ABL_F021 | **Geistersicht** | Any | Macht Geisterspuren, Klangfragmente und verborgene Echos sichtbar (Radius 30 m). | Field.Sense |
| ABL_F022 | **Seelenpfad** | Trait:Drifter|Trait:Singer | Folgt Ahnenpfaden in Ruinen; öffnet Geister-Tore (Rätsel-Tor „Ahnen“). | Field.Puzzle |
| ABL_F023 | **Kristallklang** | Trait:Lithophage|Trait:Collector|Trait:Glowing | Findet Kristallknoten; +1 Kristall je Abbau. | Field.Gather |
| ABL_F024 | **Lichtlenker** | Any | Lenkt Lichtstrahlen über Kristallspiegel (Rätsel-Tor „Prisma“). | Field.Puzzle |
| ABL_F025 | **Echolot** | Trait:Echolocator|Trait:Singer | Kartiert Höhlen und Innenräume im Umkreis von 60 m auf der Karte. | Field.Sense |
| ABL_F026 | **Lockruf** | Any | Lockt Wildechos der eigenen Linie und verwandter Arten an (+1 Spawn-Chance, K52). | Field.Social |
| ABL_F027 | **Schwebelast** | Size:M+ | Hebt und verschiebt schwere Objekte bis 2 t (Rätsel-Tor „Last“). | Field.Puzzle |
| ABL_F028 | **Leichtschritt** | Any | Halbiert die Schwerkraft des Wärters für 15 s (Sprunghöhe ×1,6, Fallschaden aus). | Field.Traversal |
| ABL_F029 | **Glyphenlesen** | Any | Liest dorunische Inschriften (Lore, Kodex-Hinweise, Rätsel-Tor „Glyphe“). | Field.Puzzle |
| ABL_F030 | **Siegelöffner** | Trait:ToolUser|Trait:Collector|Trait:Guardian | Öffnet magisch versiegelte Truhen und Türen (Rätsel-Tor „Siegel“). | Field.Puzzle |

---

## 9. Feldfähigkeiten der Arten

240 von 256 Arten besitzen eine Feldfähigkeit (LS-14: ≥ 75 %); jede Feldfähigkeit ist mindestens dreimal vergeben, die häufigsten bis zwölfmal. Arten ohne Feldfähigkeit sind vor allem kleine Erstformen, deren Endform sie erhält – das ist ein bewusster Evolutionsanreiz.

### 9.1 Übersicht aller Arten

| # | Art | Typen | Crescendo ★ | weitere Crescendos | Feldfähigkeit |
|---|---|---|---|---|---|
| 001 | Fernlit | Bloom | Urwaldchor | Dornenmeer | Rankenbrücke |
| 002 | Fernwyn | Bloom/Storm | Urwaldchor | Himmelszorn, Orkanschwinge, Dornenmeer | Rankenbrücke |
| 003 | Verdrath | Bloom/Sound | Urwaldchor | Dornenmeer, Sinfonie der Welt, Großer Takt | Rankenbrücke |
| 004 | Brokk | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 005 | Brokkar | Stone | Ewiger Fels | Bergsturz | Felsbrecher |
| 006 | Torgrath | Stone/Gravity | Ewiger Fels | Bergsturz, Ereignishorizont, Schwerkraftsturz | Felsbrecher |
| 007 | Wisplet | Storm | Himmelszorn | Orkanschwinge | Aufwind |
| 008 | Galewix | Storm | Himmelszorn | Orkanschwinge | Aufwind |
| 009 | Zephyrion | Storm/Light | Himmelszorn | Orkanschwinge, Zenitfeuer, Morgenweihe | Lichtsignal |
| 010 | Chimkin | Sound | Großer Takt | Sinfonie der Welt | Lockruf |
| 011 | Chimbal | Sound | Großer Takt | Sinfonie der Welt | Echolot |
| 012 | Cantaroth | Sound/Bloom | Großer Takt | Urwaldchor, Dornenmeer, Sinfonie der Welt | Rankenbrücke |
| 013 | Lorncant | Spirit/Sound | Seelenrückkehr | Geisterheer, Sinfonie der Welt, Großer Takt | Geistersicht |
| 014 | Mossling | Bloom | Urwaldchor | Dornenmeer | Kräuterkunde |
| 015 | Myrthorn | Bloom | Urwaldchor | Dornenmeer | Kräuterkunde |
| 016 | Vernaune | Bloom/Light | Urwaldchor | Dornenmeer, Zenitfeuer, Morgenweihe | Leuchtfeuer |
| 017 | Glyphaune | Arcane/Bloom | Umkehr der Welt | Urwaldchor, Dornenmeer, Formel des Ursprungs | Glyphenlesen |
| 018 | Lumpip | Light | Zenitfeuer | Morgenweihe | Leuchtfeuer |
| 019 | Lumow | Light/Spirit | Zenitfeuer | Morgenweihe, Geisterheer, Seelenrückkehr | Lichtsignal |
| 020 | Phantalume | Spirit/Light | Geisterheer | Zenitfeuer, Morgenweihe, Seelenrückkehr | Seelenpfad |
| 021 | Rillo | Tide | Weltflut | Gezeitenschoß | Quellsucher |
| 022 | Rillward | Tide/Bloom | Weltflut | Gezeitenschoß, Urwaldchor, Dornenmeer | Wasserlauf |
| 023 | Sporlet | Venom | Pestwolke | Säureflut | – |
| 024 | Sporix | Venom/Spirit | Pestwolke | Säureflut, Geisterheer, Seelenrückkehr | Giftschneise |
| 025 | Skirmote | Storm | Himmelszorn | Orkanschwinge | Aufwind |
| 026 | Skirrow | Storm/Sound | Himmelszorn | Orkanschwinge, Sinfonie der Welt, Großer Takt | Aufwind |
| 027 | Thornkin | Bloom | Dornenmeer | Urwaldchor | Rankenbrücke |
| 028 | Thorncoil | Bloom/Venom | Dornenmeer | Urwaldchor, Pestwolke, Säureflut | Ködermischer |
| 029 | Pebi | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 030 | Orbeloth | Gravity/Stone | Bergsturz | Ewiger Fels, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 031 | Rivetkin | Metal | Eherne Phalanx | Schmiedehammer | Erzwitterung |
| 032 | Cindrel | Ember | Sonnensturz | Phönixlied | Fackelschein |
| 033 | Craglet | Stone | Ewiger Fels | Bergsturz | – |
| 034 | Cragar | Stone | Ewiger Fels | Bergsturz | Felsbrecher |
| 035 | Kraggoth | Stone/Metal | Ewiger Fels | Bergsturz, Schmiedehammer, Eherne Phalanx | Felsbrecher |
| 036 | Anchrex | Gravity/Stone | Bergsturz | Ewiger Fels, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 037 | Tetri | Gravity | Ereignishorizont | Schwerkraftsturz | Leichtschritt |
| 038 | Tetrel | Gravity/Stone | Bergsturz | Ewiger Fels, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 039 | Ponderath | Gravity | Ereignishorizont | Schwerkraftsturz | Schwebelast |
| 040 | Ferrkin | Metal | Schmiedehammer | Eherne Phalanx | – |
| 041 | Ferrow | Metal/Stone | Schmiedehammer | Bergsturz, Ewiger Fels, Eherne Phalanx | Erzspur |
| 042 | Forgoth | Metal/Stone | Schmiedehammer | Bergsturz, Ewiger Fels, Eherne Phalanx | Erzspur |
| 043 | Gratkin | Storm | Himmelszorn | Orkanschwinge | Wetterwitterung |
| 044 | Gratwyn | Storm | Himmelszorn | Orkanschwinge | Wetterwitterung |
| 045 | Gratrex | Storm/Metal | Himmelszorn | Orkanschwinge, Schmiedehammer, Eherne Phalanx | Wetterwitterung |
| 046 | Kiesi | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 047 | Kiesward | Stone/Sound | Ewiger Fels | Bergsturz, Sinfonie der Welt, Großer Takt | Lockruf |
| 048 | Lithi | Stone | Ewiger Fels | Bergsturz | – |
| 049 | Lithshell | Stone/Tide | Ewiger Fels | Weltflut, Gezeitenschoß, Bergsturz | Wasserlauf |
| 050 | Rimlet | Frost | Ewiger Winter | Eiszeit | Eisbrücke |
| 051 | Rimpaw | Frost/Storm | Ewiger Winter | Himmelszorn, Orkanschwinge, Eiszeit | Eisbrücke |
| 052 | Quarling | Crystal | Prismenkatarakt | Spiegelpalast | Lichtlenker |
| 053 | Quarcoil | Crystal/Stone | Prismenkatarakt | Bergsturz, Ewiger Fels, Spiegelpalast | Kristallklang |
| 054 | Emblit | Ember | Sonnensturz | Phönixlied | Fackelschein |
| 055 | Dawnix | Light/Ember | Zenitfeuer | Sonnensturz, Phönixlied, Morgenweihe | Fackelschein |
| 056 | Memoro | Spirit | Seelenrückkehr | Geisterheer | Geistersicht |
| 057 | Resonix | Sound | Sinfonie der Welt | Großer Takt | Echolot |
| 058 | Runkar | Arcane/Stone | Umkehr der Welt | Bergsturz, Ewiger Fels, Formel des Ursprungs | Siegelöffner |
| 059 | Mirepip | Venom | Pestwolke | Säureflut | – |
| 060 | Mirel | Venom/Tide | Weltflut | Gezeitenschoß, Pestwolke, Säureflut | Giftschneise |
| 061 | Toxmire | Venom/Tide | Weltflut | Gezeitenschoß, Pestwolke, Säureflut | Giftschneise |
| 062 | Undling | Tide | Gezeitenschoß | Weltflut | Quellsucher |
| 063 | Undfin | Tide | Gezeitenschoß | Weltflut | Quellsucher |
| 064 | Undrath | Tide/Spirit | Gezeitenschoß | Weltflut, Geisterheer, Seelenrückkehr | Geistersicht |
| 065 | Irrlit | Spirit | Geisterheer | Seelenrückkehr | Seelenpfad |
| 066 | Irrel | Spirit/Light | Geisterheer | Zenitfeuer, Morgenweihe, Seelenrückkehr | Leuchtfeuer |
| 067 | Irraune | Spirit/Light | Geisterheer | Zenitfeuer, Morgenweihe, Seelenrückkehr | Seelenpfad |
| 068 | Sigilaune | Arcane/Spirit | Umkehr der Welt | Geisterheer, Seelenrückkehr, Formel des Ursprungs | Glyphenlesen |
| 069 | Blossi | Bloom | Dornenmeer | Urwaldchor | – |
| 070 | Blossar | Bloom/Venom | Dornenmeer | Urwaldchor, Pestwolke, Säureflut | Ködermischer |
| 071 | Blossmire | Bloom/Venom | Dornenmeer | Urwaldchor, Pestwolke, Säureflut | Giftschneise |
| 072 | Virmote | Venom | Pestwolke | Säureflut | – |
| 073 | Virwyn | Venom/Storm | Pestwolke | Himmelszorn, Orkanschwinge, Säureflut | Ködermischer |
| 074 | Blightkin | Venom | Pestwolke | Säureflut | Ködermischer |
| 075 | Blightar | Venom/Tide | Weltflut | Gezeitenschoß, Pestwolke, Säureflut | Wasserlauf |
| 076 | Brinlet | Tide | Gezeitenschoß | Weltflut | Quellsucher |
| 077 | Brinshell | Tide/Bloom | Gezeitenschoß | Weltflut, Urwaldchor, Dornenmeer | Wasserlauf |
| 078 | Umbrling | Void | Weltlöscher | Große Leere | Stillesinn |
| 079 | Umbracoil | Void/Tide | Weltlöscher | Weltflut, Gezeitenschoß, Große Leere | Schattenschritt |
| 080 | Weidlit | Bloom | Urwaldchor | Dornenmeer | – |
| 081 | Weiduna | Spirit/Bloom | Seelenrückkehr | Urwaldchor, Dornenmeer, Geisterheer | Geistersicht |
| 082 | Morhaw | Storm/Tide | Himmelszorn | Weltflut, Gezeitenschoß, Orkanschwinge | Wetterwitterung |
| 083 | Humbog | Sound/Venom | Großer Takt | Pestwolke, Säureflut, Sinfonie der Welt | Lockruf |
| 084 | Torfgor | Stone/Bloom | Ewiger Fels | Bergsturz, Urwaldchor, Dornenmeer | Felsbrecher |
| 085 | Marlit | Tide | Weltflut | Gezeitenschoß | Quellsucher |
| 086 | Marwyn | Tide | Weltflut | Gezeitenschoß | Wasserlauf |
| 087 | Maraune | Tide/Storm | Weltflut | Gezeitenschoß, Himmelszorn, Orkanschwinge | Quellsucher |
| 088 | Tidling | Tide | Gezeitenschoß | Weltflut | – |
| 089 | Tidel | Tide | Gezeitenschoß | Weltflut | Wasserlauf |
| 090 | Tidrex | Tide/Arcane | Gezeitenschoß | Weltflut, Formel des Ursprungs, Umkehr der Welt | Glyphenlesen |
| 091 | Brikin | Storm | Himmelszorn | Orkanschwinge | Aufwind |
| 092 | Brisel | Storm/Tide | Himmelszorn | Weltflut, Gezeitenschoß, Orkanschwinge | Aufwind |
| 093 | Brision | Storm/Tide | Himmelszorn | Weltflut, Gezeitenschoß, Orkanschwinge | Wasserlauf |
| 094 | Aquapip | Tide | Weltflut | Gezeitenschoß | Quellsucher |
| 095 | Aquafin | Tide/Light | Weltflut | Gezeitenschoß, Zenitfeuer, Morgenweihe | Leuchtfeuer |
| 096 | Aquadral | Tide/Light | Weltflut | Gezeitenschoß, Zenitfeuer, Morgenweihe | Lichtsignal |
| 097 | Mystdral | Arcane/Tide | Umkehr der Welt | Weltflut, Gezeitenschoß, Formel des Ursprungs | Siegelöffner |
| 098 | Aerlet | Storm | Orkanschwinge | Himmelszorn | Wetterwitterung |
| 099 | Aerluna | Storm/Light | Orkanschwinge | Himmelszorn, Zenitfeuer, Morgenweihe | Lichtsignal |
| 100 | Stonlet | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 101 | Stonshell | Stone/Tide | Ewiger Fels | Weltflut, Gezeitenschoß, Bergsturz | Wasserlauf |
| 102 | Glimkin | Light | Morgenweihe | Zenitfeuer | Lichtsignal |
| 103 | Glimar | Light/Tide | Morgenweihe | Weltflut, Gezeitenschoß, Zenitfeuer | Quellsucher |
| 104 | Ariette | Sound | Großer Takt | Sinfonie der Welt | Echolot |
| 105 | Ariuna | Sound/Tide | Großer Takt | Weltflut, Gezeitenschoß, Sinfonie der Welt | Lockruf |
| 106 | Tangi | Bloom | Urwaldchor | Dornenmeer | – |
| 107 | Tangix | Venom/Bloom | Urwaldchor | Dornenmeer, Pestwolke, Säureflut | Rankenbrücke |
| 108 | Brassel | Metal/Tide | Eherne Phalanx | Weltflut, Gezeitenschoß, Schmiedehammer | Mechanik |
| 109 | Sheamast | Spirit/Tide | Geisterheer | Weltflut, Gezeitenschoß, Seelenrückkehr | Seelenpfad |
| 110 | Opalisk | Crystal/Tide | Spiegelpalast | Weltflut, Gezeitenschoß, Prismenkatarakt | Lichtlenker |
| 111 | Solkit | Light | Zenitfeuer | Morgenweihe | Lichtsignal |
| 112 | Solvar | Light | Zenitfeuer | Morgenweihe | Lichtsignal |
| 113 | Solaryx | Light/Ember | Zenitfeuer | Sonnensturz, Phönixlied, Morgenweihe | Glutschmelze |
| 114 | Dunkalb | Stone | Ewiger Fels | Bergsturz | Felsbrecher |
| 115 | Dunhorn | Stone | Ewiger Fels | Bergsturz | Felsbrecher |
| 116 | Dunmarsch | Stone/Gravity | Ewiger Fels | Bergsturz, Ereignishorizont, Schwerkraftsturz | Leichtschritt |
| 117 | Skarit | Gravity | Ereignishorizont | Schwerkraftsturz | Leichtschritt |
| 118 | Skaral | Gravity/Stone | Bergsturz | Ewiger Fels, Ereignishorizont, Schwerkraftsturz | Leichtschritt |
| 119 | Skarabon | Gravity/Light | Zenitfeuer | Morgenweihe, Ereignishorizont, Schwerkraftsturz | Leichtschritt |
| 120 | Sengel | Ember | Sonnensturz | Phönixlied | Fackelschein |
| 121 | Sengar | Ember/Stone | Sonnensturz | Phönixlied, Bergsturz, Ewiger Fels | Glutschmelze |
| 122 | Sengrath | Ember/Stone | Sonnensturz | Phönixlied, Bergsturz, Ewiger Fels | Glutschmelze |
| 123 | Stachik | Venom | Pestwolke | Säureflut | Ködermischer |
| 124 | Stacharon | Venom/Stone | Pestwolke | Bergsturz, Ewiger Fels, Säureflut | Giftschneise |
| 125 | Sirrkorn | Storm | Himmelszorn | Orkanschwinge | Wetterwitterung |
| 126 | Sirrsturm | Storm/Stone | Himmelszorn | Bergsturz, Ewiger Fels, Orkanschwinge | Felsbrecher |
| 127 | Mirasel | Arcane | Umkehr der Welt | Formel des Ursprungs | Glyphenlesen |
| 128 | Mirazhar | Arcane/Light | Umkehr der Welt | Zenitfeuer, Morgenweihe, Formel des Ursprungs | Glyphenlesen |
| 129 | Vitrel | Light | Morgenweihe | Zenitfeuer | Lichtsignal |
| 130 | Vitrapha | Light/Crystal | Morgenweihe | Zenitfeuer, Prismenkatarakt, Spiegelpalast | Kristallklang |
| 131 | Mesakil | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 132 | Mesakor | Stone/Ember | Ewiger Fels | Sonnensturz, Phönixlied, Bergsturz | Glutschmelze |
| 133 | Qadrant | Metal/Gravity | Eherne Phalanx | Schmiedehammer, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 134 | Mahrsil | Spirit/Storm | Geisterheer | Himmelszorn, Orkanschwinge, Seelenrückkehr | Seelenpfad |
| 135 | Pyrolm | Ember | Sonnensturz | Phönixlied | Fackelschein |
| 136 | Pyrolax | Ember | Sonnensturz | Phönixlied | Fackelschein |
| 137 | Pyroluth | Ember/Stone | Sonnensturz | Phönixlied, Bergsturz, Ewiger Fels | Glutschmelze |
| 138 | Ambolt | Metal | Eherne Phalanx | Schmiedehammer | Mechanik |
| 139 | Ambrak | Metal/Ember | Eherne Phalanx | Sonnensturz, Phönixlied, Schmiedehammer | Erzwitterung |
| 140 | Ambross | Metal/Ember | Eherne Phalanx | Sonnensturz, Phönixlied, Schmiedehammer | Mechanik |
| 141 | Aschwel | Ember | Sonnensturz | Phönixlied | – |
| 142 | Aschund | Ember | Sonnensturz | Phönixlied | – |
| 143 | Aschgrim | Ember/Void | Sonnensturz | Phönixlied, Weltlöscher, Große Leere | Stillesinn |
| 144 | Obsikin | Stone | Ewiger Fels | Bergsturz | Erzspur |
| 145 | Obsidar | Stone/Crystal | Ewiger Fels | Bergsturz, Prismenkatarakt, Spiegelpalast | Lichtlenker |
| 146 | Obsidrax | Stone/Crystal | Ewiger Fels | Bergsturz, Prismenkatarakt, Spiegelpalast | Kristallklang |
| 147 | Ignavyr | Ember | Sonnensturz | Phönixlied | Glutschmelze |
| 148 | Ignavor | Ember/Gravity | Sonnensturz | Phönixlied, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 149 | Fumel | Void | Große Leere | Weltlöscher | Stillesinn |
| 150 | Fumaroth | Void/Ember | Große Leere | Sonnensturz, Phönixlied, Weltlöscher | Stillesinn |
| 151 | Drusil | Crystal | Spiegelpalast | Prismenkatarakt | Lichtlenker |
| 152 | Drusaro | Crystal/Ember | Spiegelpalast | Sonnensturz, Phönixlied, Prismenkatarakt | Glutschmelze |
| 153 | Volket | Storm | Himmelszorn | Orkanschwinge | Wetterwitterung |
| 154 | Voltarn | Metal/Storm | Schmiedehammer | Himmelszorn, Orkanschwinge, Eherne Phalanx | Aufwind |
| 155 | Bassalt | Sound/Stone | Großer Takt | Bergsturz, Ewiger Fels, Sinfonie der Welt | Echolot |
| 156 | Nucleox | Gravity/Ember | Ereignishorizont | Sonnensturz, Phönixlied, Schwerkraftsturz | Glutschmelze |
| 157 | Snevel | Frost | Ewiger Winter | Eiszeit | – |
| 158 | Snevar | Frost | Ewiger Winter | Eiszeit | Frischhalter |
| 159 | Snevrik | Frost/Light | Ewiger Winter | Eiszeit, Zenitfeuer, Morgenweihe | Frischhalter |
| 160 | Kjalf | Frost | Eiszeit | Ewiger Winter | Eisbrücke |
| 161 | Kjalmur | Frost/Stone | Eiszeit | Bergsturz, Ewiger Fels, Ewiger Winter | Eisbrücke |
| 162 | Kjalgrund | Frost/Stone | Eiszeit | Bergsturz, Ewiger Fels, Ewiger Winter | Eisbrücke |
| 163 | Uvlet | Frost | Ewiger Winter | Eiszeit | – |
| 164 | Uvarn | Frost/Spirit | Ewiger Winter | Eiszeit, Geisterheer, Seelenrückkehr | Frischhalter |
| 165 | Uvalis | Frost/Spirit | Ewiger Winter | Eiszeit, Geisterheer, Seelenrückkehr | Eisbrücke |
| 166 | Uvasil | Void/Frost | Große Leere | Ewiger Winter, Eiszeit, Weltlöscher | Schattenschritt |
| 167 | Lyskin | Light | Morgenweihe | Zenitfeuer | Leuchtfeuer |
| 168 | Lysmara | Light/Frost | Morgenweihe | Ewiger Winter, Eiszeit, Zenitfeuer | Leuchtfeuer |
| 169 | Lysthane | Light/Sound | Morgenweihe | Zenitfeuer, Sinfonie der Welt, Großer Takt | Echolot |
| 170 | Vardlit | Stone | Ewiger Fels | Bergsturz | – |
| 171 | Vardholm | Stone/Frost | Ewiger Fels | Bergsturz, Ewiger Winter, Eiszeit | Eisbrücke |
| 172 | Eidrun | Spirit | Geisterheer | Seelenrückkehr | Seelenpfad |
| 173 | Eidwacht | Spirit/Sound | Geisterheer | Seelenrückkehr, Sinfonie der Welt, Großer Takt | Geistersicht |
| 174 | Hallkid | Sound | Sinfonie der Welt | Großer Takt | Lockruf |
| 175 | Hallbrand | Sound/Stone | Sinfonie der Welt | Bergsturz, Ewiger Fels, Großer Takt | Echolot |
| 176 | Glazil | Crystal | Spiegelpalast | Prismenkatarakt | Kristallklang |
| 177 | Glazvind | Storm/Crystal | Orkanschwinge | Himmelszorn, Prismenkatarakt, Spiegelpalast | Aufwind |
| 178 | Tysvorn | Void/Frost | Weltlöscher | Ewiger Winter, Eiszeit, Große Leere | Schattenschritt |
| 179 | Skriv | Arcane | Formel des Ursprungs | Umkehr der Welt | Siegelöffner |
| 180 | Skrivar | Arcane | Formel des Ursprungs | Umkehr der Welt | Siegelöffner |
| 181 | Skriveth | Arcane/Light | Formel des Ursprungs | Zenitfeuer, Morgenweihe, Umkehr der Welt | Glyphenlesen |
| 182 | Thaelit | Arcane | Umkehr der Welt | Formel des Ursprungs | Glyphenlesen |
| 183 | Thaelon | Spirit/Arcane | Seelenrückkehr | Geisterheer, Formel des Ursprungs, Umkehr der Welt | Siegelöffner |
| 184 | Thaelarch | Spirit/Metal | Seelenrückkehr | Schmiedehammer, Eherne Phalanx, Geisterheer | Geistersicht |
| 185 | Tikkel | Metal | Eherne Phalanx | Schmiedehammer | Erzwitterung |
| 186 | Tikkar | Metal/Arcane | Eherne Phalanx | Schmiedehammer, Formel des Ursprungs, Umkehr der Welt | Erzwitterung |
| 187 | Tikkoran | Metal/Gravity | Eherne Phalanx | Schmiedehammer, Ereignishorizont, Schwerkraftsturz | Mechanik |
| 188 | Sarkel | Spirit | Geisterheer | Seelenrückkehr | Geistersicht |
| 189 | Sarkon | Spirit/Stone | Geisterheer | Bergsturz, Ewiger Fels, Seelenrückkehr | Geistersicht |
| 190 | Sarkothar | Spirit/Arcane | Geisterheer | Seelenrückkehr, Formel des Ursprungs, Umkehr der Welt | Glyphenlesen |
| 191 | Tilgel | Void | Große Leere | Weltlöscher | Schattenschritt |
| 192 | Tilgrath | Void/Arcane | Große Leere | Weltlöscher, Formel des Ursprungs, Umkehr der Welt | Stillesinn |
| 193 | Hymlit | Sound | Großer Takt | Sinfonie der Welt | Lockruf |
| 194 | Hymnora | Sound/Spirit | Großer Takt | Geisterheer, Seelenrückkehr, Sinfonie der Welt | Lockruf |
| 195 | Optil | Light | Zenitfeuer | Morgenweihe | Leuchtfeuer |
| 196 | Optikor | Gravity/Light | Ereignishorizont | Zenitfeuer, Morgenweihe, Schwerkraftsturz | Leuchtfeuer |
| 197 | Menhirok | Stone/Arcane | Ewiger Fels | Bergsturz, Formel des Ursprungs, Umkehr der Welt | Siegelöffner |
| 198 | Kronvaal | Arcane/Metal | Formel des Ursprungs | Schmiedehammer, Eherne Phalanx, Umkehr der Welt | Siegelöffner |
| 199 | Klirrit | Crystal | Prismenkatarakt | Spiegelpalast | Lichtlenker |
| 200 | Klirrflug | Crystal/Sound | Prismenkatarakt | Spiegelpalast, Sinfonie der Welt, Großer Takt | Lockruf |
| 201 | Klirrathan | Crystal/Sound | Prismenkatarakt | Spiegelpalast, Sinfonie der Welt, Großer Takt | Lichtlenker |
| 202 | Klirrnox | Void/Crystal | Weltlöscher | Große Leere, Prismenkatarakt, Spiegelpalast | Stillesinn |
| 203 | Spatling | Crystal | Spiegelpalast | Prismenkatarakt | Kristallklang |
| 204 | Spatwurm | Crystal/Stone | Spiegelpalast | Bergsturz, Ewiger Fels, Prismenkatarakt | Lichtlenker |
| 205 | Spathorn | Crystal/Gravity | Spiegelpalast | Prismenkatarakt, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 206 | Ligrel | Gravity | Ereignishorizont | Schwerkraftsturz | Leichtschritt |
| 207 | Ligrath | Gravity/Void | Weltlöscher | Große Leere, Ereignishorizont, Schwerkraftsturz | Leichtschritt |
| 208 | Ligravor | Gravity/Crystal | Prismenkatarakt | Spiegelpalast, Ereignishorizont, Schwerkraftsturz | Leichtschritt |
| 209 | Facetin | Crystal | Prismenkatarakt | Spiegelpalast | Kristallklang |
| 210 | Facettor | Crystal/Light | Prismenkatarakt | Zenitfeuer, Morgenweihe, Spiegelpalast | Lichtlenker |
| 211 | Mullit | Metal | Schmiedehammer | Eherne Phalanx | Erzwitterung |
| 212 | Mullhorn | Metal/Stone | Schmiedehammer | Bergsturz, Ewiger Fels, Eherne Phalanx | Erzspur |
| 213 | Misslit | Void | Weltlöscher | Große Leere | Stillesinn |
| 214 | Missgrath | Void/Crystal | Weltlöscher | Große Leere, Prismenkatarakt, Spiegelpalast | Stillesinn |
| 215 | Psionit | Arcane | Umkehr der Welt | Formel des Ursprungs | Glyphenlesen |
| 216 | Psioneth | Arcane/Crystal | Umkehr der Welt | Prismenkatarakt, Spiegelpalast, Formel des Ursprungs | Kristallklang |
| 217 | Miasmar | Venom/Void | Weltlöscher | Große Leere, Pestwolke, Säureflut | Ködermischer |
| 218 | Stalakkord | Sound/Crystal | Großer Takt | Prismenkatarakt, Spiegelpalast, Sinfonie der Welt | Echolot |
| 219 | Nimbel | Storm | Orkanschwinge | Himmelszorn | Aufwind |
| 220 | Nimbor | Storm/Sound | Orkanschwinge | Himmelszorn, Sinfonie der Welt, Großer Takt | Wetterwitterung |
| 221 | Nimbaroth | Storm/Gravity | Orkanschwinge | Himmelszorn, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 222 | Cirrel | Storm | Himmelszorn | Orkanschwinge | Aufwind |
| 223 | Cirrhawk | Storm/Light | Himmelszorn | Orkanschwinge, Zenitfeuer, Morgenweihe | Wetterwitterung |
| 224 | Cirrhaven | Storm/Light | Himmelszorn | Orkanschwinge, Zenitfeuer, Morgenweihe | Lichtsignal |
| 225 | Nubi | Light | Morgenweihe | Zenitfeuer | Lichtsignal |
| 226 | Nubilo | Light/Storm | Morgenweihe | Himmelszorn, Orkanschwinge, Zenitfeuer | Leuchtfeuer |
| 227 | Nubiluna | Light/Sound | Morgenweihe | Zenitfeuer, Sinfonie der Welt, Großer Takt | Echolot |
| 228 | Nubisk | Void/Light | Große Leere | Weltlöscher, Zenitfeuer, Morgenweihe | Stillesinn |
| 229 | Harfel | Sound | Großer Takt | Sinfonie der Welt | Lockruf |
| 230 | Harfion | Sound/Storm | Großer Takt | Himmelszorn, Orkanschwinge, Sinfonie der Welt | Wetterwitterung |
| 231 | Tintel | Sound | Sinfonie der Welt | Großer Takt | Echolot |
| 232 | Tintabul | Sound/Light | Sinfonie der Welt | Zenitfeuer, Morgenweihe, Großer Takt | Lockruf |
| 233 | Holmel | Gravity | Ereignishorizont | Schwerkraftsturz | Schwebelast |
| 234 | Holmgard | Gravity/Stone | Bergsturz | Ewiger Fels, Ereignishorizont, Schwerkraftsturz | Schwebelast |
| 235 | Levitel | Gravity | Ereignishorizont | Schwerkraftsturz | Leichtschritt |
| 236 | Levithar | Arcane/Gravity | Umkehr der Welt | Ereignishorizont, Schwerkraftsturz, Formel des Ursprungs | Siegelöffner |
| 237 | Graupel | Frost | Ewiger Winter | Eiszeit | – |
| 238 | Graupix | Crystal/Storm | Prismenkatarakt | Himmelszorn, Orkanschwinge, Spiegelpalast | Lichtlenker |
| 239 | Lumaskiff | Light/Storm | Morgenweihe | Himmelszorn, Orkanschwinge, Zenitfeuer | Aufwind |
| 240 | Astraviel | Arcane/Light | Formel des Ursprungs | Zenitfeuer, Morgenweihe, Umkehr der Welt | Siegelöffner |
| 241 | Sylv'anor | Bloom/Sound | Urwaldchor | Dornenmeer, Sinfonie der Welt, Großer Takt | Kräuterkunde |
| 242 | Orh'gruun | Stone/Gravity | Ewiger Fels | Bergsturz, Ereignishorizont, Schwerkraftsturz | Felsbrecher |
| 243 | Nhael'vesh | Venom/Spirit | Pestwolke | Säureflut, Geisterheer, Seelenrückkehr | Giftschneise |
| 244 | Thal'assyr | Tide/Storm | Weltflut | Gezeitenschoß, Himmelszorn, Orkanschwinge | Aufwind |
| 245 | Ash'kareth | Light/Arcane | Zenitfeuer | Morgenweihe, Formel des Ursprungs, Umkehr der Welt | Lichtsignal |
| 246 | Pyr'thagon | Ember/Metal | Sonnensturz | Phönixlied, Schmiedehammer, Eherne Phalanx | Fackelschein |
| 247 | Isv'aldr | Frost/Light | Eiszeit | Ewiger Winter, Zenitfeuer, Morgenweihe | Eisbrücke |
| 248 | Ka'thurel | Spirit/Arcane | Seelenrückkehr | Geisterheer, Formel des Ursprungs, Umkehr der Welt | Siegelöffner |
| 249 | Prism'aion | Crystal/Sound | Prismenkatarakt | Spiegelpalast, Sinfonie der Welt, Großer Takt | Kristallklang |
| 250 | Aeth'rion | Sound/Light | Großer Takt | Zenitfeuer, Morgenweihe, Sinfonie der Welt | Lichtsignal |
| 251 | Velnox | Void/Gravity | Große Leere | Weltlöscher, Ereignishorizont, Schwerkraftsturz | Schattenschritt |
| 252 | Chronaire | Sound/Arcane | Sinfonie der Welt | Großer Takt, Formel des Ursprungs, Umkehr der Welt | Lockruf |
| 253 | Mirrowisp | Crystal/Spirit | Spiegelpalast | Geisterheer, Seelenrückkehr, Prismenkatarakt | Kristallklang |
| 254 | Ouroveth | Venom/Bloom | Urwaldchor | Dornenmeer, Pestwolke, Säureflut | Kräuterkunde |
| 255 | Zenthrax | Gravity/Metal | Ereignishorizont | Schmiedehammer, Eherne Phalanx, Schwerkraftsturz | Leichtschritt |
| 256 | Aurelune | Light/Void | Zenitfeuer | Weltlöscher, Große Leere, Morgenweihe | Leuchtfeuer |

### 9.2 Beispiele (vollständige Sets inkl. Crescendo und Feld)

**Fernlit** (ECHO_001)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Rankenhieb | Bloom | Physical | 60 |
| Level | 1 | Pollenschuss | Bloom | Special | 60 |
| Level | 10 | Sonnentrunk | Bloom | Status | 90 |
| Level | 18 | Saugwurzel | Bloom | Special | 90 |
| Level | 22 | Betäubungspollen | Bloom | Status | 60 |
| Level | 25 | Strudelzug | Tide | Special | 90 |
| Level | 28 | Dornenranke | Bloom | Physical | 100 |
| Level | 28 | Blütensturm | Bloom | Special | 130 |
| Level | 33 | Erdgrollen | Stone | Special | 140 |
| Egg | – | Prismenpanzer | Crystal | Status | 80 |
| Egg | – | Steinhaut | Stone | Status | 60 |
| Egg | – | Schwelbrand | Ember | Status | 60 |

Passiv: Photosynth, Wurzelkraft, Lichtbrecher (versteckt)

Crescendo: Urwaldchor ★, Dornenmeer · Feld: Rankenbrücke

**Kjalgrund** (ECHO_162)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Kieselwurf | Stone | Physical | 60 |
| Level | 1 | Raureifhauch | Frost | Special | 70 |
| Level | 4 | Frostsplitter | Frost | Physical | 70 |
| Level | 6 | Grundfeste | Stone | Status | 80 |
| Level | 8 | Kältestarre | Frost | Status | 70 |
| Level | 10 | Glutklaue | Ember | Physical | 100 |
| Level | 12 | Felsrammen | Stone | Physical | 80 |
| Level | 14 | Schneeruf | Frost | Status | 50 |
| Level | 30 | Frostbiss | Frost | Physical | 90 |
| Level | 30 | Gletscherdruck | Frost | Physical | 110 |
| Level | 33 | Stahlsturm | Metal | Physical | 120 |
| Level | 35 | Geröllschauer | Stone | Physical | 110 |
| Level | 46 | Eissturz | Frost | Special | 110 |
| Evolution | – | Erdgrollen | Stone | Special | 140 |

Passiv: Sandverbunden, Fundament, Schmiedeglut (versteckt)

Crescendo: Bergsturz, Ewiger Fels, Ewiger Winter, Eiszeit ★ · Feld: Eisbrücke

**Klirrathan** (ECHO_201)

| Weg | Lv. | Fähigkeit | Typ | Kat. | Zeit |
|---|---|---|---|---|---|
| Level | 1 | Kristallsplitter | Crystal | Physical | 70 |
| Level | 1 | Trommelschlag | Sound | Physical | 80 |
| Level | 7 | Klangschlag | Sound | Physical | 70 |
| Level | 8 | Glitzerstrahl | Crystal | Special | 60 |
| Level | 17 | Prismenpanzer | Crystal | Status | 80 |
| Level | 24 | Kristallregen | Crystal | Special | 90 |
| Level | 25 | Wiegenlied | Sound | Status | 60 |
| Level | 26 | Drusenfeld | Crystal | Status | 50 |
| Level | 30 | Facettenschnitt | Crystal | Physical | 90 |
| Level | 30 | Erdanziehung | Gravity | Physical | 110 |
| Level | 44 | Klirrschlag | Crystal | Physical | 110 |
| Level | 44 | Siegelbruch | Arcane | Physical | 130 |
| Level | 51 | Diamantlanze | Crystal | Special | 110 |
| Evolution | – | Fortissimo | Sound | Special | 120 |

Passiv: Chorstimme, Kristallgitter, Resonanzspeicher, Glatte Haut (versteckt)

Crescendo: Prismenkatarakt ★, Spiegelpalast, Sinfonie der Welt, Großer Takt · Feld: Lichtlenker

---

## 10. Der vollständige Fähigkeitenbestand

| Art | Anzahl | Je Typ | Validierung |
|---|---|---|---|
| Aktiv | 180 | 12 | AB-01…AB-13 ✔ |
| Passiv | 90 | 6 (inkl. 16 Feldklänge) | AB-09/11 ✔, LS-08/12 ✔ |
| Crescendo | 30 | 2 | AB-08 ✔ (200–280 MP) |
| Feld | 30 | 2 | AB-10 ✔, LS-14 ✔ |
| **Summe** | **330** | 22 | `gen_abilities.py validate --final`: **0 Verstöße** (AB-14) |

Damit ist das Briefing-Ziel „mindestens 300 Fähigkeiten (passiv, aktiv, ultimative, Feldfähigkeiten)“ erfüllt.

---

## 11. Code

### 11.1 Crescendo-Ankündigung (GF_Combat)

```cpp
bool UCrescendoService::TryAnnounce(FCombatContext& Ctx, FCombatantId User, const UAbilityDefinition& Cresc)
{
    check(Cresc.Kind == EAbilityKind::Crescendo);
    const int32 Cost = HarmonyCost(Cresc, BondTier(Ctx, User));      // 60–90, −10 ab Bindungsstufe 5
    FTeamState& Team = Ctx.Team(User);
    if (Team.Harmony < Cost || Team.bCrescendoThisRound || Ctx.Used(User, Cresc)) return false;
    Team.Harmony -= Cost;
    Team.bCrescendoThisRound = true;
    Ctx.Timeline->InsertAnnouncement(User, Cresc, Cresc.TimeCost);  // goldener Marker, K31
    Ctx.Bus->Broadcast(TAG_Combat_CrescendoAnnounced, FCrescendoMessage{ User, Cresc.GetPrimaryAssetId(), Cost });
    return true;
}

void UCrescendoService::OnUserFainted(FCombatContext& Ctx, FCombatantId User)
{
    if (const FAnnouncement* A = Ctx.Timeline->FindAnnouncement(User))
        Ctx.Team(User).Harmony += A->HarmonyPaid / 2;                // DR-10: halbe Rückerstattung
}
```

### 11.2 Feldfähigkeit (GF_Companion)

```cpp
// Feldfähigkeiten sind Weltaktionen; der Pfad-Tor-Actor fragt die passende Kategorie ab.
UCLASS() class APathGateActor : public AActor
{
    GENERATED_BODY()
    UPROPERTY(EditAnywhere) FGameplayTag GateType;                     // Gate.Ice, Gate.Rubble …
    UPROPERTY(EditAnywhere) FGameplayTagContainer AcceptedFieldAbilities; // aus Data/World/PathGates.csv (K40)
public:
    bool CanResolve(const UAbilityDefinition& Field) const { return AcceptedFieldAbilities.HasTagExact(Field.Tags.First()); }
};
```

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-103 | Crescendos mit fester Zeitkosten 200 und **Ankündigung** auf der Zeitleiste | Lesbarer Höhepunkt, Gegenspiel möglich (DR-07) | Sofortausführung (unkonterbar), Abklingzeit (ADR-094) |
| ADR-104 | Harmoniekosten aus dem Budget (60–90) | Ein Balancing-Hebel; starke Crescendos teurer | Einheitlich 100 (zu starr) |
| ADR-105 | Feldfähigkeiten ersetzen Schlüssel-Items; jedes Pfad-Tor hat ≥ 2 Lösungen, eine typunabhängig | Echos als Partner (S2), keine Sackgassen | HM-artige Pflichtfähigkeiten (Clean-Room, Frust) |
| ADR-106 | Reitarten bleiben Art-Eigenschaft, keine Feldfähigkeit | Reiten ist Kernfortbewegung (K40), nicht Slot-Konkurrenz | Reiten als Feldfähigkeit (blockiert Slot) |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §106 | Crescendo: Budget 200–320, Zeitkosten 200, Harmoniekosten 60–90 (Formel), Ankündigung auf der Zeitleiste, 1 je Echo/Kampf, 1 je Seite/Runde, ab Bindungsstufe 2 (−10 Kosten ab Stufe 5), 50 % Rückerstattung bei Verklingen, Inszenierung ≤ 4 s (kurz 1,5 s, PvP immer kurz); Arten lernen alle Crescendos ihrer Typen, ★ bevorzugt | LOCKED |
| §107 | Feldfähigkeiten: 5 Kategorien, Ausdauerkosten, Bedingung Typ + Merkmal/Größe, 0–1 je Art (`FieldOptions.csv`); Pfad-Tore (12 Typen) mit Regeln PT-1…PT-3 | LOCKED (Tuning → K40) |
| §108 | Fähigkeitenbestand final: 330 (180/90/30/30), Validator `--final` | LOCKED |
| §10 | ADR-103 – ADR-106 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Crescendo-System: Kosten, Ankündigung, Begrenzung, Bindung, Inszenierung, Barrierefreiheit
- [x] 30 Crescendos (2 je Typ) als Daten, Budget validiert
- [x] Crescendo-Optionen für alle 256 Arten (★ bevorzugt)
- [x] Feldfähigkeiten-System mit Kategorien, Kosten, Bedingungen
- [x] 12 Pfad-Tor-Typen mit Mehrfachlösungen (Vorgabe für K40)
- [x] 30 Feldfähigkeiten (2 je Typ) und Zuordnung zu 240 Arten
- [x] Gesamtbestand 330 Fähigkeiten, `--final` ohne Verstöße
- [x] Code: Crescendo-Service, Pfad-Tor-Actor
- [x] ADR-103 – ADR-106, CANON §106–§108

➡️ **Nächstes Kapitel: K31 – Kampfsystem I: Resonanz-Zeitleiste (Initiative, Ticks, Priorität, Reserve-Wechsel) – löst Q1.**
