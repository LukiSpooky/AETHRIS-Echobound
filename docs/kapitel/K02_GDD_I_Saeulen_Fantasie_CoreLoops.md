# K02 · GDD I – Design-Säulen, Spielerfantasie, Core Loops

| Feld | Wert |
|---|---|
| Dokument | Kapitel 02 von 68 · Game Design Document, Teil I |
| Version | 1.0 |
| Owner | Game Director |
| Mitwirkende | Creative Director, Combat Designer, RPG Systems Designer, Level Designer, UI/UX Designer, Sound Designer, QA Lead |
| Baut auf | K01 (CANON §1–§10) |
| Status | ✅ Freigegeben |
| Neue Kanon-Einträge | CANON §13 (Design-Regeln), §14 (Onboarding & Starter), §15 (Progression), §16 (Schwierigkeit), §6 ergänzt (Akkorde, Sol, Rückklang) |

---

## Inhalt

1. [Zweck dieses Kapitels](#1-zweck-dieses-kapitels)
2. [Von Säulen zu Design-Regeln](#2-von-säulen-zu-design-regeln)
3. [Säulen × Systeme-Matrix](#3-säulen--systeme-matrix)
4. [Experience Goals – das Gefühl jeder Kernaktivität](#4-experience-goals--das-gefühl-jeder-kernaktivität)
5. [Steuerung & Kamera (Grundsatz)](#5-steuerung--kamera-grundsatz)
6. [Core Loops im Detail](#6-core-loops-im-detail)
7. [Belohnungsrhythmus](#7-belohnungsrhythmus)
8. [Onboarding: Die ersten drei Stunden](#8-onboarding-die-ersten-drei-stunden)
9. [Makro-Progression](#9-makro-progression)
10. [Intensitäts- und Pacing-Kurve](#10-intensitäts--und-pacing-kurve)
11. [Schwierigkeit, Fehlerzustände & Zugänglichkeit](#11-schwierigkeit-fehlerzustände--zugänglichkeit)
12. [Design-Validierung: Playtest-Protokoll](#12-design-validierung-playtest-protokoll)
13. [Datenstrukturen & Pseudocode](#13-datenstrukturen--pseudocode)
14. [Decision Records](#14-decision-records)
15. [Kanon-Updates](#15-kanon-updates)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Zweck dieses Kapitels

K01 hat **was** wir bauen festgelegt. K02 legt fest, **wie es sich anfühlen muss** und **nach welchen Regeln** jedes Team Entscheidungen trifft, wenn der Game Director nicht im Raum ist. Ein AAA-Team mit 200 Personen trifft täglich Hunderte Mikro-Entscheidungen; dieses Kapitel ist das Werkzeug, mit dem diese Entscheidungen konsistent bleiben.

Das Kapitel liefert:

- **Design-Regeln (DR-xx)**: überprüfbare Sätze, abgeleitet aus den fünf Säulen. Jeder Content-Review referenziert sie.
- **Experience Goals**: konkrete Gefühls- und Timing-Ziele für Erkundung, Bindung und Kampf, inklusive erster Tuning-Werte.
- **Core Loops** mit Belohnungsfrequenzen.
- **Onboarding-Skript** der ersten 180 Minuten.
- **Makro-Progression**: Akte, Regionen, Level-Korridore, Freischaltungen.
- **Schwierigkeits- und Fehlerzustandsmodell**.

---

## 2. Von Säulen zu Design-Regeln

Format jeder Regel: **ID · Regel · Begründung · Prüffrage im Review · Anti-Beispiel**. Regeln sind **LOCKED** und in CANON §13 indexiert.

### 2.1 S2 – Bindung durch Verstehen (Priorität 1)

| ID | Regel | Begründung | Prüffrage | Anti-Beispiel |
|---|---|---|---|---|
| DR-01 | **Wissen schlägt Items.** Jede Bindungschance muss durch Spielerwissen stärker steigerbar sein als durch teurere Verbrauchsgüter. | Verhindert „Kauf dich zum Erfolg“; belohnt Kodex-Forschung. | „Kann ein Spieler mit Kodex-Stufe 3 und Basis-Siegel mindestens so gut binden wie mit Kodex-Stufe 0 und Top-Siegel?“ | Ein Premium-Siegel mit 100 % Erfolg. |
| DR-02 | **Jedes Echo hat ein lesbares Verhalten.** Mindestens drei beobachtbare Verhaltensmerkmale (Tagesrhythmus, Vorliebe, Reaktion auf Bedrohung) pro Art. | Verstehen braucht etwas zu verstehen. | „Welche drei Dinge lernt ein aufmerksamer Spieler durch 60 s Beobachtung?“ | Echo steht nur im Idle herum. |
| DR-03 | **Bindung ist ein Dialog, kein Wurf.** Jede Bindung hat mindestens eine Spielerentscheidung *vor* dem Timing-Moment (Annäherung, Lockmittel, Beruhigung, Falle, Kampf). | Differenzierung (ADR-006). | „Gibt es vor dem Timing eine Wahl, die das Ergebnis messbar beeinflusst?“ | Knopf drücken → Zufallswurf. |
| DR-04 | **Echos reagieren auf den Spieler.** Jede Interaktion (Streicheln, Füttern, Ignorieren, Niederlage) hat eine sichtbare Reaktion und eine Wirkung auf den Bindungswert. | Partner-Fantasie. | „Merkt der Spieler ohne UI, dass sein Echo zufrieden/unzufrieden ist?“ | Bindung nur als Zahl im Menü. |
| DR-05 | **Kein Echo ist wertlos.** Jede Art hat mindestens eine Nische: Kampfrolle, Feldfähigkeit, Zuchtwert, Forschungswert oder Reitbarkeit. | Sammelmotivation über das „Meta-Team“ hinaus. | „Warum würde ein Spieler dieses Echo auf Level 60 behalten?“ | Reines Füll-Echo ohne Funktion. |

### 2.2 S3 – Taktische Harmonie (Priorität 2)

| ID | Regel | Begründung | Prüffrage | Anti-Beispiel |
|---|---|---|---|---|
| DR-06 | **Alles Kampfrelevante ist vorhersehbar sichtbar.** Die Zeitleiste zeigt mindestens die nächsten 8 Züge; jede Aktion zeigt ihre Zeitkosten vor Bestätigung. | „Leicht zu lesen“. | „Kann der Spieler die Konsequenz seiner Wahl auf die Zugfolge vor dem Bestätigen sehen?“ | Versteckte Initiative-Würfel. |
| DR-07 | **Zufall nur mit Gegenspiel.** Jeder RNG-Effekt (Kritisch, Ausweichen, Statuschance) hat eine Spieleraktion, die ihn beeinflusst, und eine harte Ober-/Untergrenze. | Kompetitive Fairness (Persona Mara). | „Welche Gegenaktion existiert, und ist die Varianz gedeckelt?“ | 30 % Einschlafen ohne Gegenmittel, 1–5 Züge. |
| DR-08 | **Jeder Typ hat eine Identität jenseits der Tabelle.** Jeder der 15 Typen besitzt eine typische Mechanik (z. B. Klang = Rhythmus/Zeitleisten-Manipulation, Schwerkraft = Positionierung). | Tiefe ohne mehr Typen. | „Was kann *nur* dieser Typ besonders gut?“ | Typen unterscheiden sich nur durch Farbe und Tabelle. |
| DR-09 | **Einfache Grundschicht, optionale Tiefe.** Ein Kampf muss mit nur „Fähigkeit wählen + Ziel wählen“ gewinnbar sein (Story auf Standard). Formation, Combos und Wetter sind Verstärker. | Persona Lina. | „Gewinnt ein Spieler, der Formation/Combos ignoriert, die Story auf Standard?“ | Story-Boss, der Combos zwingend voraussetzt. |
| DR-10 | **Kein Zug ist verschwendet.** Jede Aktion hat mindestens einen Nutzen (auch Verfehlen erzeugt Harmonie, Wechsel erzeugt Formationsvorteil). | Frustvermeidung. | „Was bekommt der Spieler, wenn seine Aktion scheitert?“ | Verfehlen = nichts passiert, Zug verloren. |
| DR-11 | **Kämpfe sind kurz.** Wildkampf Ziel 60–120 s, Trainerkampf 3–6 min, Arenameister 8–15 min, Ranked-Trio max. 20 min. | Session-Fluss. | „Liegt der Median im Playtest im Zielkorridor?“ | 25-minütiger Wildkampf durch Heil-Spam. |

### 2.3 S1 – Lebendige Resonanz (Priorität 3)

| ID | Regel | Begründung | Prüffrage | Anti-Beispiel |
|---|---|---|---|---|
| DR-12 | **Die Welt läuft ohne Zuschauer.** Echos, NPCs und Wetter folgen ihren Regeln auch außerhalb des Spielerblicks (in reduzierter Simulations-LOD). | Glaubwürdigkeit. | „Was hat sich verändert, wenn ich nach 1 Spieltag zurückkehre?“ | Herde respawnt beim Hinsehen an exakt gleicher Stelle. |
| DR-13 | **Systeme sprechen miteinander.** Jedes Weltsystem (Wetter, Tageszeit, Ökologie, NPC, Wirtschaft) beeinflusst mindestens zwei andere. | Emergenz. | „Welche zwei anderen Systeme reagieren auf diese Variable?“ | Regen ist nur Optik. |
| DR-14 | **Sichtbare Begegnungen, freie Wahl.** Wilde Echos sind in der Welt sichtbar; der Spieler entscheidet, ob er kämpft, bindet, beobachtet oder ausweicht. Ausnahme: gescriptete Hinterhalte (max. 1 pro Quest, angekündigt durch Klangsignal). | Respekt vor Spielerzeit (Persona Jonas). | „Kann der Spieler dieser Begegnung ausweichen?“ | Unsichtbare Zufallskämpfe. |
| DR-15 | **Seltenheit hat Bedingungen, nicht nur Zufall.** Jedes seltene Echo hat eine erlernbare Bedingungskombination (Wetter × Zeit × Ort × Verhalten). Reiner Zufall nur für Morphs. | Verstehen statt Grinden (S2). | „Kann der Kodex dem Spieler sagen, *wann* und *wo*?“ | 0,1 % Spawn ohne Bedingung. |

### 2.4 S4 – Erbe & Einzigartigkeit (Priorität 4)

| ID | Regel | Begründung | Prüffrage | Anti-Beispiel |
|---|---|---|---|---|
| DR-16 | **Jedes Echo trägt eine Geschichte.** Jede Instanz speichert Herkunft (Ort, Wetter, Datum, Wärter, Stammbaum) und zeigt sie an. | Emotionale Bindung, Fälschungsschutz. | „Kann ich sehen, wo und wann ich es gebunden habe?“ | Anonyme Instanz. |
| DR-17 | **Optik ist Erbe, nicht Shop.** Farbvarianten und Morphs entstehen nur durch Genetik, Fundort oder Leistung. | CANON §8.2. | „Ist diese Optik irgendwie käuflich?“ | Morph im Kosmetik-Shop. |
| DR-18 | **Perfektion ist erreichbar, aber teuer an Zeit, nicht an Geld.** Kompetitiv perfekte Echos müssen in ≤ 15 h gezieltem Spiel züchtbar sein (Endgame-Spieler). | Kompetitiver Zugang ohne Ausschluss. | „Wie lange braucht ein erfahrener Züchter für ein Ranked-taugliches Echo?“ | 200-h-Zuchtroulette. |

### 2.5 S5 – Gemeinsamer Chor (Priorität 5)

| ID | Regel | Begründung | Prüffrage | Anti-Beispiel |
|---|---|---|---|---|
| DR-19 | **Allein vollständig.** Kein Story-, Kodex- oder Legendären-Inhalt erfordert Mitspieler. Tausch-exklusive Echos gibt es **nicht**; Raids sind Abkürzung, nicht Pflicht. | CANON §8.3/§8.5. | „Kann ein Offline-Spieler 100 % Kodex erreichen?“ | Version-exklusive Arten. |
| DR-20 | **Zusammen macht es mehr Spaß, nicht mehr Pflicht.** Koop-Boni sind sozial/kosmetisch oder Zeitersparnis, nie Machtvorteile, die Solo unerreichbar sind. | Kein sozialer Zwang. | „Verliert ein Solo-Spieler Macht?“ | +20 % Werte nur in Gilden. |
| DR-21 | **Fairness online ist nicht verhandelbar.** Alles Kompetitive ist serverautoritativ und levelnormalisiert. | Risiko R-10. | „Kann der Client das Ergebnis manipulieren?“ | Client-seitige Schadensberechnung im Ranked. |

### 2.6 Querschnittsregeln

| ID | Regel |
|---|---|
| DR-22 | **Clean-Room** (CANON §8.1) hat Vorrang vor jeder anderen Regel. |
| DR-23 | **Respektiere die Spielerzeit:** Keine Pflicht-Wartezeiten > 30 s, keine Echtzeit-Timer für Kernfortschritt (Zuchtdauer läuft in **Spielzeit**, nicht Echtzeit). |
| DR-24 | **Lesbarkeit vor Realismus:** Jedes Gameplay-relevante Signal hat einen visuellen **und** einen akustischen Kanal (Zugänglichkeit). |
| DR-25 | **Daten statt Code für Content:** Neuer Content (Echo, Fähigkeit, Quest, Item) darf keinen neuen C++-Code erfordern, außer für neue Mechanik-Primitiva. |

---

## 3. Säulen × Systeme-Matrix

Stärke: ●●● Kernträger · ●● wichtig · ● unterstützend · – kein Beitrag. Ein System ohne ●● in mindestens einer Säule steht beim nächsten Scope-Review auf der Streichliste.

| System | S1 Lebendige Resonanz | S2 Bindung | S3 Taktik | S4 Erbe | S5 Chor |
|---|---|---|---|---|---|
| Ökologie-KI / Schwärme | ●●● | ●● | ● | – | ● |
| Wetter | ●●● | ●● | ●● | ● | – |
| Tageszyklus | ●●● | ●● | ● | – | – |
| NPC-Tagesabläufe | ●●● | – | – | – | – |
| Resonanzbindung | ●● | ●●● | ● | ● | – |
| Begleitersystem | ●● | ●●● | ● | ●● | ● |
| Resonanzhain | ●● | ●●● | – | ●● | ●● |
| Echo-Kodex | ●● | ●●● | ●● | ● | ● |
| Fotografie | ●● | ●● | – | ●● | ●● |
| Zeitleisten-Kampf | – | ● | ●●● | – | ●● |
| Typen & Fähigkeiten | ● | ● | ●●● | ● | ● |
| Evolution | ●● | ●●● | ●● | ●● | – |
| Zucht & Genetik | – | ●● | ●● | ●●● | ●● |
| Crafting | ●● | ●● | ● | ● | ● |
| Wirtschaft | ●● | ● | – | ● | ●● |
| Skilltree | – | ●● | ●● | ● | – |
| Reittiere & Traversal | ●●● | ●● | – | ● | ●● |
| Story & Quests | ●● | ●● | ● | ● | ● |
| Fraktionen | ●● | ● | – | – | ● |
| Koop | ●● | ● | ● | – | ●●● |
| Tausch | – | ● | – | ●● | ●●● |
| PvP / Ranked | – | – | ●●● | ●● | ●●● |
| Raids | ● | – | ●●● | ● | ●●● |
| Gilden | – | – | – | ● | ●●● |

**Befund:** Alle Systeme haben mindestens ein ●●. Kein System wird gestrichen. Gilden tragen nur S5 (Priorität 5) → bleiben auf **Could** (K01 §8.7).

---

## 4. Experience Goals – das Gefühl jeder Kernaktivität

Alle Zahlen in diesem Abschnitt sind **Starttuning (PROVISIONAL)**; finale Werte entstehen in den angegebenen Kapiteln und Playtests. Sie sind hier, damit Prototypen ab Tag 1 mit denselben Zahlen arbeiten.

### 4.1 Erkundung – „Neugier, die belohnt wird“

**Gefühlsziel:** *Ich sehe etwas am Horizont, will hin, und auf dem Weg passieren drei Dinge, die ich nicht geplant habe.*

| Aspekt | Spezifikation | Wert (Start) | Final in |
|---|---|---|---|
| Gehen / Joggen / Sprinten | 3 Stufen, analog | 1,8 / 4,2 / 7,0 m/s | K40 |
| Ausdauer | Sprint, Klettern, Gleiten | 100 Einheiten, Sprint −12/s, Regeneration +25/s nach 1 s | K40 |
| Klettern | Fast jede natürliche Oberfläche (außer markierte „glatte“ Flächen: Eis, Kristall, nasser Fels bei Regen) | 1,6 m/s, −8 Ausdauer/s | K40 |
| Gleiter | Ab Prolog-Ende | Sinkrate 1,8 m/s, Vorwärts 9 m/s | K40 |
| Reiten | Ab Akt I (Bodenreiten), Fähigkeiten gestaffelt | Boden 14 m/s | K40 |
| **„Neugier-Dichte“** | Abstand zwischen bemerkenswerten Punkten (POI) | Ø 150–250 m, kein Punkt > 400 m vom nächsten | K08 |
| Sichtachsen | Jeder Hügel/Turm zeigt ≥ 3 neue POIs | – | K08 |
| Resonanzsinn | Halten L2/LT: Welt entsättigt, Frequenzen als Klangwellen sichtbar | Radius 60 m (Rang 1) → 150 m (Skilltree), Abklingzeit 4 s | K36/K43 |

**Die „Drei-Ding-Regel“ (DR-26):** Auf einem Weg von 300 m Luftlinie soll der Spieler im Median mindestens **drei** ungeplante Interaktionsangebote erhalten (Echo-Verhalten, Ressource, NPC-Begebenheit, Ruine, Klangrätsel, Wetterumschwung, Fund). Gemessen durch Telemetrie in Playtests und durch die POI-Dichte-Validierung im Editor (K08).

### 4.2 Bindung – „Der Moment des Einklangs“

**Gefühlsziel:** *Ich habe mich angeschlichen, das Echo beruhigt, und dann – der perfekte Ton. Ich habe es nicht gefangen, wir haben uns gefunden.*

Ablauf (vollständig in K36):

```
 ┌───────────┐   ┌───────────────────┐   ┌──────────────────┐   ┌──────────────┐
 │ 1. LAUSCHEN│──►│ 2. ANNÄHERN       │──►│ 3. EINSTIMMEN    │──►│ 4. ANSCHLAG  │
 │ Resonanz-  │   │ Schleichen, Wind, │   │ Beruhigen (Lied, │   │ Timing-Fenster│
 │ sinn: Fre- │   │ Deckung; Falle    │   │ Futter, Lock-    │   │ auf Echo-     │
 │ quenz & Stim│  │ legen; Lockmittel │   │ mittel) ODER     │   │ frequenz; Sie-│
 │ mung lesen │   │                   │   │ Kampf→Erschöpfung│   │ gel verankert │
 └───────────┘   └───────────────────┘   └──────────────────┘   └──────┬───────┘
                                                                      │
                     ┌────────────────────────────┬───────────────────┤
                     ▼                            ▼                   ▼
              PERFEKT (Einklang)            GUT (Bindung)       VERFEHLT
              +Bindungsstart-Bonus,         Standard-Bindung    Echo reagiert gemäß
              Kodex-Fortschritt,                                Temperament: flieht,
              Musik-Stinger                                     greift an, bleibt
```

| Aspekt | Spezifikation | Wert (Start) |
|---|---|---|
| Timing-Fenster „Gut“ | Abhängig von Echo-Unruhe | 400 ms (ruhig) → 160 ms (aufgewühlt) |
| Timing-Fenster „Perfekt“ | Kern des Gut-Fensters | 25 % des Gut-Fensters, min. 60 ms |
| Versuche bis Abbruch | Abhängig vom Temperament | 2–4 |
| Feedback | Controller-Haptik in Echo-Frequenz (adaptive Trigger PS5), Ton-Pitch steigt zum Fenster | – |
| Zugänglichkeit | Option „Großzügiges Timing“ (Fenster × 1,75), Option „Auto-Einklang“ (Timing ersetzt durch Halten) | – |
| Dauer gesamt | Oberwelt-Bindung ohne Kampf | Ziel 20–60 s |

### 4.3 Kampf – „Ich sehe die Zukunft und forme sie“

**Gefühlsziel:** *Ich sehe auf der Zeitleiste, dass der Gegner in zwei Zügen seinen großen Angriff macht. Ich verzögere ihn mit einem Klang-Stoß, stelle mein Stein-Echo nach vorn, und als der Angriff kommt, hat mein Team genug Harmonie für ein Crescendo.*

| Aspekt | Spezifikation | Wert (Start) | Final in |
|---|---|---|---|
| Übergang Oberwelt → Kampf | **Nahtlos am Ort** (kein Szenenwechsel); Kampfarena = lokaler Kreis, Terrain wird übernommen | Übergang < 1,5 s | K31 |
| Zeitleiste sichtbar | Nächste Züge | 8 (UI), intern unbegrenzt | K31 |
| Entscheidungszeit (Solo) | Unbegrenzt | – | K31 |
| Entscheidungszeit (PvP) | Zugtimer | 30 s/Zug + 90 s Reservebank | K61 |
| Animationstempo | Option 1×/1,5×/2× + Skip | – | K54 |
| Harmonie-Leiste | Teamweit | 0–100 | K33 |
| Kampfende | Erschöpfung aller aktiven + Reserve-Echos einer Seite, Flucht, Bindung | – | K31 |

**Kampfgefühl-Regeln (Combat Feel Checklist, gilt für jede Fähigkeit):**

1. **Antizipation** (Wind-up) ≤ 0,6 s, **Impact** mit Hit-Stop 60–120 ms, **Recovery** ≤ 0,5 s.
2. Jede Fähigkeit hat einen eigenen **Klangakzent**, der auf den Kampfmusik-Takt quantisiert wird (Quartz, K55).
3. Effektivität ist **dreifach** kommuniziert: Zahl + Farbe + Klang (sehr effektiv = aufsteigender Akkord; resistent = gedämpfter Ton).
4. Kamera: automatische Kamerafahrt pro Aktion, abschaltbar („Taktische Kamera“: statische Draufsicht).

### 4.4 Begleiter – „Mein Freund, nicht mein Werkzeug“

| Aspekt | Spezifikation |
|---|---|
| Folgende Echos | Bis zu 1 (Konsole/PC Standard), optional 2 auf PS5/XSX/PC (Performance-Option, K65) |
| Interaktionen | Streicheln, Füttern, Spielen (Wurfspiel, Klangspiel), Trainieren, Loben, Tadeln (DR-04) |
| Echo-Initiative | Echos zeigen eigenständig Dinge: wittern Ressourcen, warnen vor Gefahren, reagieren auf Wetter |
| Lager | **Lager-Moment** an jedem Rastplatz: Kochen, Fütterung, Interaktion mit dem ganzen Chor (≤ 2 min, optional) |

### 4.5 Siedlungen – „Ankommen“

| Aspekt | Spezifikation |
|---|---|
| Ankunft | Musik-Übergang (Ambient → Stadtthema in 8–12 s, K55), Kamerafahrt beim Erstbesuch (≤ 6 s, überspringbar) |
| Funktionen | Heilung (Klangbrunnen), Händler, Arena, Fraktionsbüro, Resonanzhain-Zugang, Questbrett |
| Leben | Einwohner mit Tagesablauf (K53); Stadt nachts sichtbar anders (Händlerwechsel, andere Echos) |

---

## 5. Steuerung & Kamera (Grundsatz)

Detaillierte Belegung, Remapping und Maus/Tastatur in K54. Grundsatz-Belegung Gamepad (Xbox-Notation / PS-Notation):

| Eingabe | Oberwelt | Kampf | Bindung (Anschlag-Phase) |
|---|---|---|---|
| Linker Stick | Bewegen | Menü-Navigation | – |
| Rechter Stick | Kamera | Kamera (taktisch) | – |
| A / ✕ | Interagieren / Springen | Bestätigen | **Anschlag** (Timing) |
| B / ◯ | Ducken / Schleichen | Zurück | Abbrechen |
| X / ▢ | Echo-Befehl (Gehe dorthin, Sammle) | Formation | – |
| Y / △ | Reittier rufen | Detailansicht Ziel | Lockmittel wechseln |
| LB / L1 | Radial: Werkzeuge | Zeitleiste vorschauen | – |
| RB / R1 | Radial: Chor | Echo wechseln | – |
| LT / L2 (halten) | **Resonanzsinn** | Analyse (Kodex-Overlay) | Fokus (verlangsamt Frequenzwelle, kostet Ausdauer) |
| RT / R2 | Resonator ziehen / Kodex-Linse | Crescendo (wenn Harmonie 100) | Siegel wählen |
| Steuerkreuz | Schnellzugriff Items | Schnellzugriff Items | – |
| Menü | Pausemenü | Pausemenü | – |

**Kamera-Grundsatz (LOCKED):** Third-Person-Schulterkamera in der Oberwelt (FOV 70°, Distanz 3,2 m, beim Reiten 5,5 m). Im Kampf: dynamische Kamera mit optionaler taktischer Draufsicht. Kodex-Linse: First-Person.

---

## 6. Core Loops im Detail

### 6.1 Die drei Primär-Loops und ihre Kopplung

AETHRIS hat **drei gleichwertige Primär-Loops**, die über gemeinsame Ressourcen gekoppelt sind. Das ist bewusst: Ein Spieler, der nur einen Loop mag (z. B. Bindung), soll trotzdem in die anderen hineingezogen werden – aber nie gezwungen.

```
                         ┌──────────────────────────┐
                         │      ERKUNDUNGS-LOOP     │
                         │ Reisen → Entdecken →     │
                         │ Freischalten (Traversal) │
                         └────────────┬─────────────┘
              Ressourcen, Fundorte    │     Neue Gebiete, Wetterlagen
                     ┌────────────────┼────────────────┐
                     ▼                                 ▼
     ┌──────────────────────────┐          ┌──────────────────────────┐
     │      BINDUNGS-LOOP       │          │       KAMPF-LOOP         │
     │ Beobachten → Verstehen → │◄────────►│ Kämpfen → Leveln →       │
     │ Binden → Pflegen → Ent-  │  Echos,  │ Fähigkeiten → Taktik →   │
     │ wickeln → Züchten        │  Erfahrung│ stärkere Gegner         │
     └──────────────────────────┘          └──────────────────────────┘
                     ▲                                 ▲
                     └──────────── WÄRTER-LOOP ────────┘
                         Wärterrang → Skillpunkte → Crafting →
                         Ausrüstung → Ruf → Story-Fortschritt
```

### 6.2 Kopplungsressourcen

| Ressource | Erzeugt durch | Verbraucht durch | Koppelt |
|---|---|---|---|
| **Echo-Erfahrung (EP)** | Kampf, Training, Erkundung (Entdeckungs-EP), Bindung | Level-Up | Kampf ↔ Bindung ↔ Erkundung |
| **Kodex-Forschung** | Beobachten, Kämpfen, Fotografieren, Binden, Züchten | Forschungsstufen (schaltet Infos, Bindungsboni, Evolutionshinweise) | Bindung ↔ Kampf ↔ Erkundung |
| **Wärter-EP** | Alles (Quests, Entdeckungen, Kodex, Arenen) | Wärterrang → Skillpunkte | Alle |
| **Materialien** | Sammeln (Holz, Erz, Kristalle, Kräuter), Echo-Materialien (Schuppen, Federn – **nur** abgeworfen/gefunden/gepflegt, nie durch Erschöpfung „geerntet“) | Crafting | Erkundung ↔ Wärter |
| **Sol** (Währung) | Quests, Verkauf, Kämpfe gegen Wärter, Aufträge | Händler, Dienstleistungen | Wärter ↔ alle |
| **Ruf** | Fraktionsquests, Entscheidungen | Fraktionsbelohnungen | Story ↔ Wärter |
| **Harmonie** (nur im Kampf) | Aktionen, Combos | Crescendo | Kampf intern |

> **Kanon-Notiz:** Die Währung heißt **Sol** (Singular und Plural, Symbol `◎`). Die Wirtschaft wird in K42 spezifiziert. → CANON §6.

### 6.3 Loop-Durchlaufzeiten (Ziel)

| Loop | Mikro-Zyklus | Makro-Zyklus |
|---|---|---|
| Erkundung | POI zu POI: 30–90 s | Region „durchdrungen“ (alle Resonanzsteine): 4–7 h |
| Bindung | Echo binden: 20–120 s | Kodex-Stufe 4 für eine Art: 1–3 h verteilt |
| Kampf | Wildkampf: 60–120 s | Arena: 2–4 h Vorbereitung + 8–15 min Kampf |
| Wärter | Questschritt: 3–10 min | Wärterrang-Aufstieg: 45–90 min (Story-Phase) |

---

## 7. Belohnungsrhythmus

### 7.1 Belohnungspyramide

```
                         ▲  SELTEN, GROSS
                        ╱ ╲   Akt-Abschluss, Ursprungsstimme, Morph,
                       ╱   ╲  Arenameister-Akkord, Reittier-Fähigkeit
                      ╱─────╲          (alle 3–8 h)
                     ╱       ╲  Evolution, neue Region, Fraktionsrang,
                    ╱         ╲ seltenes Echo, Skillpunkt-Meilenstein
                   ╱───────────╲        (alle 30–90 min)
                  ╱             ╲  Level-Up, neue Fähigkeit, Kodex-Stufe,
                 ╱               ╲ Quest-Abschluss, Crafting-Rezept
                ╱─────────────────╲      (alle 3–10 min)
               ╱                   ╲  Ressource, Echo-Reaktion, Kodex-Notiz,
              ╱                     ╲ Fund, Klangfragment, EP-Tick
             ╱───────────────────────╲   (alle 20–60 s)
                                    HÄUFIG, KLEIN
```

### 7.2 Belohnungstypen und Gewichtung

| Typ | Beispiele | Psychologische Funktion | Anteil am Belohnungsstrom (Ziel) |
|---|---|---|---|
| Macht | EP, Level, Fähigkeiten, Ausrüstung | Kompetenz | 30 % |
| Sammlung | Neue Echos, Kodex-Einträge, Morphs, Fotos | Vollständigkeit | 25 % |
| Wissen | Lore, Evolutionshinweise, Spawn-Bedingungen | Neugier | 15 % |
| Zugang | Neue Regionen, Traversal, Rezepte | Autonomie | 15 % |
| Beziehung | Bindungsstufen, Echo-Reaktionen, Fraktionsruf | Verbundenheit | 10 % |
| Ausdruck | Kosmetik, Hain-Deko, Titel | Identität | 5 % |

**Regel DR-27:** Kein Belohnungsstrom darf in einem 30-Minuten-Fenster Playtest-Telemetrie zu > 50 % aus einem einzigen Typ bestehen (Monotonie-Alarm).

---

## 8. Onboarding: Die ersten drei Stunden

### 8.1 Onboarding-Prinzipien

1. **Spielen vor Lesen:** Keine Tutorialbox länger als 2 Zeilen; Mechaniken werden in Situationen eingeführt.
2. **Ein neues Verb pro Szene:** Nie zwei Kernmechaniken gleichzeitig einführen.
3. **Emotion zuerst:** Das erste Echo wird gebunden, bevor das erste Menü erklärt wird.
4. **Erstes Spielziel nach ≤ 5 min, erste Freiheit nach ≤ 45 min, offene Welt (Region) nach ≤ 90 min.**
5. **Tutorial-Abschluss Kampf ≤ 12 min Spielzeit** (Säulen-Messkriterium S3).

### 8.2 Starter-Konzept: „Die Erstresonanz“ (ADR-011)

Statt aus drei angebotenen Kreaturen zu wählen, **hört** der Spieler im Prolog drei Echos im Wald, die vor einer aufziehenden Stillezone fliehen. Er folgt einem davon – diese Wahl ist die Starterwahl. Die Wahl ist **diegetisch** (durch Folgen einer Klangspur), nicht menübasiert, mit einer Bestätigung vor dem Einklang.

| Starter-Linie | Typ | Basisform (Arbeitsname) | Klangspur im Prolog | Spielgefühl |
|---|---|---|---|---|
| A | Blüte | *Fernlit* | Rascheln + Glockenton, führt durchs Unterholz | Ausdauernd, Heilung/Kontrolle |
| B | Stein | *Brokk* | Tiefes Brummen, führt über Felsen | Schutz, Vorderreihe |
| C | Sturm | *Wisplet* | Pfeifen, führt über Baumwipfel/Wind | Schnell, Zeitleisten-Tempo |

**Starter-Zyklus (LOCKED, bindend für K17):** **Blüte > Stein > Sturm > Blüte** (Wurzeln sprengen Stein · Stein erdet Sturm · Sturm entwurzelt Blüte).

*Begründung:* Der Genre-Standarddreiklang (Feuer/Wasser/Pflanze) wird bewusst vermieden (Clean-Room §4.3 Regel 3). Der Blüte-Stein-Sturm-Zyklus passt zur Startregion Verdanthain (Wald, Felsen, Wind in den Kronen) und gibt allen drei Startern im Akt I eine thematische Region (Verdanthain/Morvenmoor für Blüte, Kharsgrat für Stein, Saltrand für Sturm).

*Namen sind PROVISIONAL → K04 (Morphem-Lexikon) und K20 (Katalog #001–#009).*

### 8.3 Minute-für-Minute-Skript (Ziel-Timing für Median-Spieler)

**Kanon-Festlegungen für den Prolog:** Startdorf **Lindwiesen** (Verdanthain, eines der 22 Dörfer). Mentorin **Ysolde Varn**, Wildwacht-Wärterin, ehemalige Arenameisterin von Eichenhall. Rivale **Kael Duran**, Jugendfreund des Spielers, Akademie-Anwärter. (Charaktertiefe in K44.)

| Zeit | Szene | Neues Verb / System | Ort | Emotion | Ende-Bedingung |
|---|---|---|---|---|---|
| 0:00–0:03 | **Kalte Eröffnung:** Schwarzbild, ein Ton – das Weltlied. Kurze Vision (Nimbara, ein riesiges Echo, das verstummt). Erwachen. | – (Cinematic, überspringbar) | Lindwiesen, Haus | Mysterium | Spieler erwacht |
| 0:03–0:10 | **Charakter-Editor** (eingebettet: Spiegel im Haus) | Editor | Haus | Identifikation | Editor bestätigt |
| 0:10–0:16 | Morgen im Dorf. Ein kleines wildes Echo stiehlt Brot. Verfolgung. | **Bewegen, Sprinten, Springen** | Lindwiesen | Leichtigkeit, Humor | Echo verschwindet im Wald |
| 0:16–0:22 | Ysolde trifft den Spieler am Waldrand, testet ihn: „Was hörst du?“ | **Resonanzsinn** (erstmals) | Waldrand | Staunen | 3 Frequenzen gefunden |
| 0:22–0:30 | Kael kommt dazu. Gemeinsamer Waldgang. Klettern über umgestürzten Baum. | **Klettern, Ausdauer** | Lindwald | Freundschaft | Lichtung erreicht |
| 0:30–0:38 | **Stillezone bricht aus**: Farben schwinden, Ton verstummt, Echos fliehen. Drei Klangspuren. | **Spurwahl** (Starterwahl, diegetisch) | Lichtung | Bedrohung, Dringlichkeit | Spieler folgt einer Spur |
| 0:38–0:46 | Verfolgung durch die zerfallende Zone; das Starter-Echo ist verletzt und verängstigt. | **Annähern, Schleichen** | Verfolgungsweg | Spannung | Spieler beim Echo |
| 0:46–0:52 | **Die Erstresonanz:** Beruhigen (Summen = Halten der Taste), dann Anschlag im Timing. Kann nicht scheitern (Fenster großzügig, Fehlversuche → Echo kommt näher). | **Beruhigen, Anschlag (Bindung)** | Versteck | **Emotionaler Höhepunkt 1** | Echo gebunden |
| 0:52–1:02 | Die Stillezone erreicht sie. Erster **Kampf** gegen ein „verstummtes“ Echo (erstarrt, grau). Zeitleiste wird eingeführt: nur Angriff + Zeitleiste lesen. | **Kampf: Fähigkeit wählen, Zeitleiste** | Versteck → Lichtung | Mut | Sieg |
| 1:02–1:08 | Ysolde rettet beide, versiegelt die Zone provisorisch. Erkenntnis: Der Spieler hat die **Grundfrequenz** gehört. Ysolde schenkt den **Resonator**. | Erzählung (Resonator offiziell) | Lichtung | Bestimmung | Rückkehr nach Lindwiesen |
| 1:08–1:20 | Lindwiesen: Ankunft, **Begleitersystem** (Streicheln, Füttern), Heilen am Klangbrunnen, Kael zeigt sein Echo (Typ mit Vorteil gegen den Spieler-Starter, siehe Zyklus). | **Begleiter, Heilen** | Lindwiesen | Wärme | Gespräch mit Ysolde |
| 1:20–1:32 | **Erster Rivalenkampf** gegen Kael (1v1). Einführung **Typ-Effektivität**: Kael hat Typvorteil; da der Spieler nur 1 Echo besitzt, lernt er, den Nachteil mit **Zeitleisten-Verzögerung** durch seine zweite Fähigkeit auszugleichen. Verlieren erlaubt: Story läuft weiter (DR-09). | **Typen, Zeitkosten** | Dorfplatz | Ehrgeiz | Kampf beendet |
| 1:32–1:45 | Ysoldes Auftrag: drei Echos im Lindwald beobachten und eins binden. **Erste freie Zone** (~0,8 km², begrenzt durch Flusslauf). | **Bindung frei, Kodex** | Lindwald | **Erste Freiheit** | 1 Echo gebunden + 3 beobachtet |
| 1:45–1:55 | Erste Wilde-Herde mit Alpha; Wetterumschwung zu Regen → neue Echos erscheinen. | **Wetter beeinflusst Spawns** | Lindwald | Entdeckung | Spieler betritt Regenzone (passiv) |
| 1:55–2:10 | Lager-Moment am Rastplatz: **Crafting** (Heiltrank aus Kräutern), Kochen, Chor-Interaktion. **Reserve & Wechsel** im nächsten Kampf eingeführt (jetzt 2 Echos; Wechsel kostet Zeitleisten-Zeit). Formation folgt mit dem Duo-Format ab Wärterrang 5. | **Crafting, Wechsel** | Rastplatz Lindwald | Ruhe | Erster Crafting-Gegenstand |
| 2:10–2:25 | Ruine im Wald: **Klangrätsel** (Echo-Feldfähigkeit nutzen, um Mechanismus zu aktivieren). Fund: **Gleiter** (Prolog-Ende-Belohnung). | **Feldfähigkeit, Gleiter** | Ruine Lindwald | Clevernes Gefühl | Gleiter erhalten |
| 2:25–2:40 | Gleitflug vom Ruinenturm: **Panorama über Verdanthain** – Eichenhall am Horizont, Kharsgrat-Gipfel, Küste. Resonanzstein aktivieren (**Schnellreise**). | **Gleiten, Schnellreise, Karte** | Ruinenturm | **Emotionaler Höhepunkt 2: Weite** | Resonanzstein aktiviert |
| 2:40–3:00 | Reise nach Eichenhall (frei wählbare Route, ~1,5 km). Erste **Harmonie/Combo** in einem Trainerkampf unterwegs. Ankunft in der ersten Stadt, Questbrett, Arena-Ankündigung. | **Harmonie, Combo**, Stadt | Weg → Eichenhall | Aufbruch | Ankunft Eichenhall = Ende Onboarding |

### 8.4 Onboarding-KPIs (Playtest-Gates)

| KPI | Ziel | Abbruchkriterium für Redesign |
|---|---|---|
| Zeit bis erste Bindung | 46–55 min | > 65 min |
| Spieler, die Resonanzsinn ohne Hinweis nach Prolog nutzen | ≥ 60 % | < 40 % |
| Rivalenkampf-Niederlagen (Standard) | 20–40 % | > 60 % (zu schwer) / < 5 % (bedeutungslos) |
| „Was ist dein Lieblingsmoment?“ nennt Erstresonanz oder Gleitpanorama | ≥ 50 % | < 25 % |
| Abbruch (Spieler hört auf) in den ersten 3 h | ≤ 8 % | > 15 % |

---

## 9. Makro-Progression

### 9.1 Struktur: „Gestaffelte Offenheit“ (ADR-012)

| Akt | Regionen | Offenheit | Hauptziel | Level-Korridor (Wild) | Akkorde |
|---|---|---|---|---|---|
| Prolog | R01 (Lindwald) | Linear | Erstresonanz | 2–5 | 0 |
| **Akt I – Der erste Riss** | R01 Verdanthain → dann frei: **R02 Kharsgrat, R03 Morvenmoor, R06 Saltrand** | Halb-offen: nach Eichenhall 3 Regionen in beliebiger Reihenfolge | Ursache der Stillezonen ergründen | 5–28 | 4 (Eichenhall + 3 frei wählbar) |
| **Akt II – Das Echo der Ruinen** | **R04 Sahrun-Weite, R05 Ignareth, R07 Hvitfell, R08 Ael'Dorun** | Offen: 4 Regionen beliebig, R08 als Story-Knoten nach 2 weiteren | Orden der Stille, Wahrheit über die Große Stille | 25–55 | 4 (insg. 8) |
| **Akt III – Das letzte Lied** | **R09 Prismtiefen, R10 Nimbara** | Fokussiert | Finale, Entscheidung | 50–70 | 2 (insg. 10) |
| **Endgame** | Alle + Tiefenresonanzen | Offen | Legendäre, Ranked, Raids | 70–100 | – |

### 9.2 Akkorde (Arena-Fortschritt)

- Jede der 10 Stadt-Arenen wird von einem **Arenameister** geführt. Ein Sieg verleiht einen **Akkord** (Arena-Abzeichen, 10 insgesamt, zusammen der *Weltakkord*). **LOCKED.**
- **Akt I:** Arena-Stufe ist fest an die Region gebunden (Eichenhall immer zuerst). Die drei frei wählbaren Arenen in Akt I **skalieren** nach Anzahl gehaltener Akkorde (Stufe 2/3/4).
- **Akt II:** dasselbe Prinzip für Stufe 5–8.
- **Akt III:** feste Stufen 9 (Prismara) und 10 (Aerion).

**Arena-Stufen-Tabelle (PROVISIONAL → K63):**

| Stufe | Ass-Level Arenameister | Chorgröße Arenameister | Format |
|---|---|---|---|
| 1 | 12 | 3 | Duell |
| 2 | 17 | 4 | Duell |
| 3 | 22 | 4 | Duo |
| 4 | 27 | 5 | Duell |
| 5 | 33 | 5 | Duo |
| 6 | 39 | 5 | Trio |
| 7 | 45 | 6 | Duell |
| 8 | 51 | 6 | Duo |
| 9 | 59 | 6 | Trio |
| 10 | 67 | 6 | Trio |

*Begründung für skalierte Arenen:* Freie Reihenfolge (S1) ohne Level-Brüche. *Nachteil:* Spieler empfinden Skalierung manchmal als „Strafe für Erkundung“. *Mitigation:* Skaliert wird nur die **Arena**, nicht die Welt; wilde Echos behalten regionale Korridore, sodass Überleveln in der Welt spürbar belohnt.

### 9.3 Level-Korridore & Skalierungsmodell

```
 Level
 100 ┤                                                         ░░░░ Endgame (Tiefenresonanzen, Raids)
  90 ┤                                                    ░░░░░
  80 ┤                                               ░░░░░
  70 ┤                                         ████▓▓  ← Story-Finale (~68–70)
  60 ┤                                   ██████
  50 ┤                           ████████          Akt III (R09/R10)
  40 ┤                   ████████                  Akt II (R04/R05/R07/R08, skaliert in Stufen)
  30 ┤           ████████
  20 ┤     ██████                                  Akt I (R01/R02/R03/R06)
  10 ┤ ████
   1 ┼─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────► Spielstunden (Story-Fokus)
     0     5    10    15    20    25    30    35    40    45
```

**Wildlevel-Modell (LOCKED Prinzip, Formel → K63):**
- Jede Region hat **Zonen** mit festen Basiskorridoren (z. B. Kharsgrat-Ausläufer 12–16, Gipfel 22–28).
- Regionen von Akt I/II, deren Reihenfolge frei ist, nutzen **Zonen-Stufen**: Beim ersten Betreten wird der Korridor anhand des Story-Fortschritts (Anzahl Akkorde) einmalig festgelegt und **danach fixiert** (keine dynamische Nachskalierung). So bleibt Rückkehr zu alten Regionen sichtbar „leichter“ (Machtgefühl).
- Alphatiere/seltene Echos: Korridor +3 bis +8.

### 9.4 Wärterrang (Spielerprogression)

| Rang | Erreicht ca. | Skillpunkte kumuliert | Freischaltung (Auswahl) |
|---|---|---|---|
| 1 | Start | 0 | – |
| 5 | Ende Onboarding (3 h) | 4 | Chorgröße 4 |
| 10 | Mitte Akt I | 10 | Chorgröße 5, Trio-Kämpfe |
| 14 | Ende Akt I | 15 | Chorgröße 6, Zucht freigeschaltet |
| 22 | Ende Akt II | 25 | Raids (Online) |
| 28 | Story-Ende | 33 | Ranked |
| 40 | Max (Endgame) | 50 | – |

**Chorgröße wächst** von 2 (Prolog) über 3 (Eichenhall) bis 6 (Ende Akt I) – vereinbar mit CANON ADR-009 (Chor = maximal 6). Details K43.

### 9.5 Freischaltungs-Roadmap (Traversal & Systeme)

| Freischaltung | Wann | Quelle |
|---|---|---|
| Resonanzsinn, Bindung, Kampf | Prolog | Story |
| Gleiter | Prolog-Ende (~2:20 h) | Ruine Lindwald |
| Bodenreiten | Akt I, nach Akkord 1 | Reitfähiges Echo + Sattel (Crafting) |
| Schwimmreiten | Akt I, Saltrand oder Morvenmoor | Reitbares Flut-Echo |
| Kletterreiten | Akt I, Kharsgrat | Reitbares Stein-Echo |
| Zucht | Ende Akt I | Resonanzhain-Ausbau |
| Grabreiten | Akt II, Sahrun-Weite | Reitbares Echo (Wüste) |
| Flugreiten | Akt II, nach 6 Akkorden | Story-Quest Hvitfell/Nimbara-Vorbereitung |
| Kodex-Linse Stufe 2 (Teleobjektiv) | Akt II | Akademie-Ruf |
| Tiefenresonanzen | Post-Story | Story-Ende |

**Regel DR-28:** Jede Region muss mit der Traversal-Ausstattung, die zum *frühestmöglichen* Betretungszeitpunkt verfügbar ist, vollständig für den Hauptpfad spielbar sein. Spätere Traversal-Fähigkeiten öffnen **optionale** Bereiche (Metroidvania-Rückkehranreiz).

---

## 10. Intensitäts- und Pacing-Kurve

### 10.1 Akt-Intensität (Story-Fokus-Spieler)

```
 Intensität
  10 ┤                                                            ▲Finale
   9 ┤                         ▲Ruinen-Wende                    ╱ ╲
   8 ┤            ▲Arena 4    ╱ ╲                ▲Verrat        ╱   ╲
   7 ┤           ╱ ╲  ▲     ╱   ╲     ▲        ╱ ╲  ▲         ╱     ╲
   6 ┤  ▲Erst-  ╱   ╲╱ ╲   ╱     ╲   ╱ ╲      ╱   ╲╱ ╲       ╱       ╲
   5 ┤ ╱ ╲reso.╱       ╲ ╱       ╲ ╱   ╲    ╱        ╲     ╱         ╲▁ Epilog
   4 ┤╱   ╲  ╱         ╲╱         ╲╱     ╲  ╱          ╲   ╱
   3 ┤     ╲╱                              ╲╱            ╲ ╱
   2 ┤
     └────────────────────────────────────────────────────────────────────►
      Prolog │      AKT I        │           AKT II           │  AKT III
```

**Regel DR-29 („Atemzug-Regel“):** Nach jedem Intensitätsgipfel ≥ 7 folgt ein Ruhefenster von ≥ 20 Minuten mit Erkundung, Begleiterpflege oder Stadtleben, bevor der nächste Gipfel kommt. Die Story-Quest-Struktur (K44–K46) muss diese Fenster explizit ausweisen.

### 10.2 Session-Pacing

| Session-Länge | Gestaltungsziel |
|---|---|
| 20 min (Handheld, Switch 2) | Mindestens 1 abgeschlossenes Ziel (Quest-Schritt, Bindung, Arena-Training). Autosave alle 5 min + bei jedem Zielabschluss. |
| 60–90 min | Ein vollständiger Session-Loop (K01 §7.2) mit ≥ 1 Belohnung der Ebene „30–90 min“. |
| 3 h+ | Fortschritt auf Makro-Ebene (Akkord, Evolution, Region). |

---

## 11. Schwierigkeit, Fehlerzustände & Zugänglichkeit

### 11.1 Schwierigkeitsgrade (LOCKED-Struktur, Werte → K63)

| Grad | Name | Zielgruppe | Wild-KI | Trainer-KI | Fehlerstrafe | EP-Rate |
|---|---|---|---|---|---|---|
| 1 | **Entspannt** | Lina, Story-Fokus | Passiv | Einfach (K34 Stufe 1) | Keine | 1,25× |
| 2 | **Wärter** (Standard) | Breite Masse | Normal | Taktisch (Stufe 2–3) | Keine Sol-Strafe | 1,0× |
| 3 | **Meister** | Mara | Aggressiv, Alphas koordinieren | Experten-KI (Stufe 4), Arenameister mit Gegenkonter-Logik | 10 % Sol | 1,0× |
| Option | **Eiserner Wärter** (Modifikator, kombinierbar mit Meister) | Challenge-Runner | – | – | Erschöpfte Echos ziehen in den Resonanzhain und sind für die laufende Region gesperrt | – |

Wechsel jederzeit erlaubt (außer Eiserner Wärter: nur deaktivierbar, dann dauerhaft vermerkt).

### 11.2 Fehlerzustand: Rückklang (LOCKED)

Wenn alle Echos des Chors erschöpft sind, löst der **Rückklang** aus:

1. Kurze Sequenz: Die Echos des Chors bilden einen Klangschild, der Wärter wird zum zuletzt aktivierten **Resonanzstein** oder **Klangbrunnen** (näherer von beiden) zurückgetragen.
2. Echos werden geheilt.
3. Bindungswert sinkt **nicht** (Niederlage ist kein Pflegeversagen, DR-04 Ausnahme).
4. Quest-Fortschritt bleibt erhalten; bei Bosskämpfen Rückkehr direkt vor die Arena („Erneut versuchen“-Option).
5. Strafe nur auf **Meister**: 10 % des Sol-Bestands (gedeckelt auf 5.000 ◎).

### 11.3 Zugänglichkeit (Grundsatz, vollständig in K54)

| Bereich | Optionen |
|---|---|
| Motorik | Großzügiges Timing, Auto-Einklang, Halten statt Hämmern, vollständiges Remapping, Ein-Hand-Profil |
| Sehen | Farbenblind-Modi (3), Typ-Symbole immer zusätzlich zu Farbe, Textgröße 4 Stufen, Hochkontrast-Resonanzsinn |
| Hören | Untertitel mit Sprecher und Richtung, **visuelle Klangsignale** für alle Frequenz-Mechaniken (Pflicht wegen Klang-Thema: DR-24) |
| Kognition | Questziel-Erinnerung, Kampf-Empfehlungen (optional), Zeitleisten-Erklärmodus |
| Tempo | Kampfanimation 1×/1,5×/2×/Skip, Dialog-Autoplay |

**Kritische Designbeobachtung:** Ein Spiel über *Hören* muss für gehörlose und schwerhörige Spieler vollständig spielbar sein. Jede Frequenz hat daher ein **visuelles Wellenmuster** (Form + Farbe + Rhythmus), das das Audio-Signal 1:1 abbildet. Das ist kein Zusatz, sondern Teil des Kerndesigns (Art Bible K56, Audio Bible K55).

---

## 12. Design-Validierung: Playtest-Protokoll

| Phase | Testform | Teilnehmende | Fokus | Frequenz |
|---|---|---|---|---|
| P1 Preproduction | Paper-/Graybox-Prototyp | Intern | Zeitleiste, Bindungs-Timing | wöchentlich |
| P2 Vertical Slice | Fokusgruppen (n = 12 je Persona) | Extern, NDA | Onboarding-KPIs (§8.4) | monatlich |
| P3 Core Systems | Großtest (n = 60) mit Telemetrie | Extern | Belohnungsrhythmus (§7), Kampfdauer (DR-11) | alle 6 Wochen |
| P4 Content | Langzeittest (n = 30, 40 h) | Extern | Pacing (§10), Drei-Ding-Regel (DR-26) | quartalsweise |
| P5 Polishing | Closed Beta Online | ~5.000 | Ranked, Raids, Server | einmalig, 4 Wochen |

**Telemetrie-Events für dieses Kapitel (Auszug; Schema in K06):**

| Event | Payload | Validiert |
|---|---|---|
| `onb.step.complete` | step_id, t_session, deaths | §8.3 Timings |
| `world.poi.discovered` | poi_id, distance_from_last, t_since_last | DR-26 |
| `combat.end` | format, duration_s, turns, result, difficulty | DR-11 |
| `bond.attempt` | species_id, kodex_level, seal_tier, result, window_ms | DR-01 |
| `reward.granted` | reward_type, magnitude, source | DR-27 |

---

## 13. Datenstrukturen & Pseudocode

Die folgenden Strukturen sind Vorgriffe auf K06; Namen sind verbindlich (CANON §9), Felder können in K06 ergänzt werden.

### 13.1 Design-Regel-Validator (Editor-Tool, `AethrisEditor`)

Viele Design-Regeln sind automatisch prüfbar. Der Validator läuft beim Speichern von Data Assets und im nächtlichen Build.

```cpp
// AethrisEditor/Validation/EchoDesignRuleValidator.h
// Prüft Spezies-Definitionen gegen die Design-Regeln aus K02.
// Läuft über das UE Data Validation Plugin (UEditorValidatorBase).

UCLASS()
class AETHRISEDITOR_API UEchoDesignRuleValidator : public UEditorValidatorBase
{
    GENERATED_BODY()
protected:
    virtual bool CanValidateAsset_Implementation(const FAssetData& InAssetData,
        UObject* InAsset, FDataValidationContext& InContext) const override
    {
        return InAsset && InAsset->IsA<UEchoSpeciesDefinition>();
    }

    virtual EDataValidationResult ValidateLoadedAsset_Implementation(
        const FAssetData& InAssetData, UObject* InAsset,
        FDataValidationContext& Context) override
    {
        const auto* Species = CastChecked<UEchoSpeciesDefinition>(InAsset);
        bool bOk = true;

        // DR-02: mindestens drei beobachtbare Verhaltensmerkmale.
        if (Species->ObservableTraits.Num() < 3)
        {
            AssetFails(InAsset, FText::FromString(
                TEXT("DR-02: Weniger als 3 ObservableTraits definiert.")));
            bOk = false;
        }

        // DR-05: mindestens eine Nische.
        if (Species->Niches.IsEmpty())
        {
            AssetFails(InAsset, FText::FromString(
                TEXT("DR-05: Keine Nische (Kampfrolle/Feld/Zucht/Forschung/Reiten).")));
            bOk = false;
        }

        // DR-15: seltene Arten brauchen erlernbare Spawn-Bedingungen.
        if (Species->Rarity >= EEchoRarity::Rare && Species->SpawnConditions.IsEmpty())
        {
            AssetFails(InAsset, FText::FromString(
                TEXT("DR-15: Seltene Art ohne SpawnConditions.")));
            bOk = false;
        }

        if (bOk) { AssetPasses(InAsset); }
        return bOk ? EDataValidationResult::Valid : EDataValidationResult::Invalid;
    }
};
```

*Hinweis:* `ObservableTraits`, `Niches`, `Rarity`, `SpawnConditions` werden damit als Pflichtfelder von `UEchoSpeciesDefinition` festgelegt (Typdefinition in K16).

### 13.2 Progressionsdaten (Data Table-Zeile)

```cpp
// AethrisCore/Progression/WardenRankRow.h
/** Eine Zeile der Wärterrang-Tabelle (DT_WardenRank). Quelle: Data/Progression/WardenRank.csv */
USTRUCT(BlueprintType)
struct AETHRISCORE_API FWardenRankRow : public FTableRowBase
{
    GENERATED_BODY()

    /** Rang 1..40 (ADR-008). */
    UPROPERTY(EditAnywhere, meta=(ClampMin=1, ClampMax=40)) int32 Rank = 1;

    /** Kumulative Wärter-EP, um diesen Rang zu erreichen. */
    UPROPERTY(EditAnywhere) int64 RequiredWardenXP = 0;

    /** Skillpunkte, die beim Erreichen dieses Rangs vergeben werden. */
    UPROPERTY(EditAnywhere) int32 SkillPointsGranted = 1;

    /** Maximale Chorgröße ab diesem Rang (nie > 6, ADR-009). */
    UPROPERTY(EditAnywhere, meta=(ClampMin=2, ClampMax=6)) int32 ChorCapacity = 2;

    /** Freischaltungen (z. B. Feature.Breeding, Feature.Ranked). */
    UPROPERTY(EditAnywhere) FGameplayTagContainer Unlocks;
};
```

```csv
# Data/Progression/WardenRank.csv  (Auszug, Werte PROVISIONAL → K43/K63)
Name,Rank,RequiredWardenXP,SkillPointsGranted,ChorCapacity,Unlocks
R01,1,0,0,2,"()"
R02,2,400,1,3,"()"
R05,5,2600,1,4,"(Feature.Combat.Duo)"
R10,10,11000,1,5,"(Feature.Combat.Trio)"
R14,14,21500,2,6,"(Feature.Breeding)"
R22,22,52000,1,6,"(Feature.Raid)"
R28,28,86000,2,6,"(Feature.Ranked)"
R40,40,190000,2,6,"()"
```

### 13.3 Zonen-Stufen-Fixierung (Pseudocode, DR aus §9.3)

```text
FUNKTION ResolveZoneLevelBand(zone, saveState):
    // Einmal fixiert → immer gleich (Machtgefühl bei Rückkehr)
    WENN saveState.FixedZoneBands enthält zone.Id:
        RÜCKGABE saveState.FixedZoneBands[zone.Id]

    WENN zone.ScalingMode == FIXED:
        band ← zone.BaseBand
    SONST:  // SCALED_BY_AKKORDE (Akt I/II frei wählbare Regionen)
        stufe ← Clamp(saveState.AkkordCount, zone.MinTier, zone.MaxTier)
        band  ← zone.TierBands[stufe]

    saveState.FixedZoneBands[zone.Id] ← band      // persistiert (Save-Schema K64)
    EventBus.Broadcast("World.Zone.BandFixed", {zone.Id, band})
    RÜCKGABE band
```

### 13.4 Rückklang (State-Machine-Skizze, Implementierung K06/K31)

```
 [Kampf aktiv] ──(alle Chor-Echos erschöpft)──► [Rückklang.Sequenz]
                                                   │ 4–6 s Cinematic, Input gesperrt
                                                   ▼
                                          [Rückklang.Teleport]
                                                   │ Ziel = nächster aktivierter
                                                   │ Resonanzstein/Klangbrunnen
                                                   ▼
                                          [Rückklang.Heilung]
                                                   │ Meister: Sol −10 % (max 5.000)
                                                   │ Eiserner Wärter: Sperre setzen
                                                   ▼
                              ┌──── Boss? ──ja──► [Retry-Dialog vor Arena]
                              │
                              └──── nein ───────► [Oberwelt, Autosave]
```

---

## 14. Decision Records

### ADR-010 – Design-Regeln als überprüfbares Regelwerk
- **Kontext:** Säulen allein sind zu abstrakt für tägliche Entscheidungen.
- **Entscheidung:** 29 Design-Regeln (DR-01 – DR-29) mit Prüffragen; automatisierbare Regeln werden als Editor-Validatoren umgesetzt.
- **Vorteile:** Konsistenz, Review-Geschwindigkeit, Onboarding neuer Teammitglieder.
- **Nachteile:** Regelwerk kann Kreativität bremsen. **Mitigation:** Jede Regel darf per begründeter Ausnahme (im Content-Review protokolliert) gebrochen werden, außer DR-19, DR-21, DR-22 (unverhandelbar).

### ADR-011 – Diegetische Starterwahl („Erstresonanz“)
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Menüwahl aus 3 | Klar, vertraut | Genre-Klischee, kein emotionaler Kontext |
| (b) Diegetisch durch Spurwahl | Emotional, eigenständig, führt Resonanzsinn ein | Spieler könnten nicht merken, dass sie wählen → **Mitigation:** Bestätigungsmoment („Diesem Klang folgen?“) mit Vorschau des Echos |
| (c) Zufälliger Starter | Überraschend | Frust, Kontrollverlust |
- **Entscheidung:** (b).

### ADR-012 – Gestaffelte Offenheit mit Akkord-skalierten Arenen
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Lineare Route | Kontrolliertes Balancing | Widerspricht Open World |
| (b) Komplett offen, volle Weltskalierung | Maximale Freiheit | Kein Machtgefühl, „Gummiband“-Welt |
| (c) Gestaffelt: frei innerhalb eines Akts, Arenen skaliert, Wildzonen einmalig fixiert | Freiheit + Machtgefühl + planbares Story-Balancing | Komplexere Datenpflege |
- **Entscheidung:** (c).

### ADR-013 – Nahtloser Kampf am Ort
- **Kontext:** Klassisch erfolgt ein Szenenwechsel in eine Kampfarena.
- **Entscheidung:** Kämpfe finden **am Ort** statt; ein Kampfkreis (Radius 12–18 m, Formatabhängig) wird aus der Umgebung abgeleitet, Hindernisse werden per Navmesh-Query geprüft und ggf. das Zentrum verschoben. Terrain und Wetter werden übernommen.
- **Vorteile:** S1 (Welt bleibt präsent), Terrain/Wetter natürlich im Kampf.
- **Nachteile:** Kamera- und Kollisionsprobleme an engen Orten; andere Echos/NPCs können „hineinlaufen“. **Mitigation:** Kampfkreis-Solver mit Fallback-Verschiebung bis 25 m; Ökologie-KI meidet aktive Kampfkreise (K52); als letzte Stufe „Klangblase“ (stilisierte Abschirmung).

### ADR-014 – Rückklang ohne Bindungsverlust
- **Entscheidung:** Niederlage bestraft auf Standard nicht. Begründung: DR-04 verbindet Bindung mit Pflege, nicht mit Kampferfolg; eine Strafe würde Spieler von schweren Kämpfen abhalten.

### ADR-015 – Spielzeit statt Echtzeit für Wartezeiten
- **Entscheidung:** Alle zeitbasierten Prozesse (Zucht, Crafting-Reifung, Händler-Rotation) laufen in **Spielzeit** (CANON §4.3: 1 Spieltag = 72 min). Ausnahme: Online-Saisons und Events (Echtzeit-Kalender). Begründung: DR-23, kein Druck zum Einloggen.

---

## 15. Kanon-Updates

Folgende Einträge werden in `CANON.md` übernommen:

| Bereich | Eintrag | Status |
|---|---|---|
| §6 Begriffe | **Akkord** (Arena-Abzeichen, 10 = Weltakkord) | LOCKED |
| §6 Begriffe | **Sol** (Währung, Symbol ◎) | LOCKED (Wirtschaft → K42) |
| §6 Begriffe | **Rückklang** (Fehlerzustand) | LOCKED |
| §6 Begriffe | **Klangbrunnen** (Heilpunkt in Siedlungen) | LOCKED |
| §6 Begriffe | **Lager-Moment** (Rastplatz-Interaktion) | LOCKED |
| §13 | Design-Regeln DR-01 – DR-29 | LOCKED |
| §14 | Starter-Zyklus Blüte > Stein > Sturm > Blüte | LOCKED (bindend für K17) |
| §14 | Starter-Arbeitsnamen Fernlit / Brokk / Wisplet | PROVISIONAL → K04/K20 |
| §14 | Startdorf Lindwiesen (R01), Lindwald | LOCKED |
| §14 | Figuren: Ysolde Varn (Mentorin, Wildwacht), Kael Duran (Rivale, Akademie-Anwärter) | LOCKED (Tiefe → K44) |
| §15 | Akt-/Regionsstruktur „Gestaffelte Offenheit“ | LOCKED |
| §15 | Level-Korridore: Prolog 2–5, Akt I 5–28, Akt II 25–55, Akt III 50–70, Endgame 70–100 | LOCKED (Feinwerte → K63) |
| §15 | Arena-Stufentabelle (10 Stufen) | PROVISIONAL → K63 |
| §15 | Wärterrang-Meilensteine, Chorgröße 2→6 | PROVISIONAL → K43 |
| §15 | Freischaltungs-Roadmap Traversal | LOCKED (Reihenfolge) |
| §16 | Schwierigkeitsgrade Entspannt / Wärter / Meister + Eiserner Wärter | LOCKED (Struktur) |
| §16 | Rückklang-Regeln | LOCKED |
| §9 Technik | Pflichtfelder `UEchoSpeciesDefinition`: ObservableTraits, Niches, Rarity, SpawnConditions | LOCKED |
| §9 Technik | `FWardenRankRow`, Data Table `DT_WardenRank` | LOCKED |
| §10 ADR | ADR-010 – ADR-015 | LOCKED |
| §12 Offen | Q11: Bewegungs-/Ausdauer-Tuning → K40; Q12: Bindungs-Timingfenster → K36 | PROVISIONAL |

---

## 16. Kapitel-Checkliste

### Abgeschlossene Systeme / Entscheidungen in K02

- [x] 29 Design-Regeln (DR-01 – DR-29) mit Begründung, Prüffrage und Anti-Beispiel
- [x] Säulen × Systeme-Matrix – alle 24 Systeme bestätigt, Gilden bleiben „Could“
- [x] Experience Goals mit Starttuning: Erkundung, Bindung, Kampf, Begleiter, Siedlungen
- [x] Combat-Feel-Checkliste (Antizipation, Hit-Stop, Klangakzent, dreifache Effektivitätskommunikation)
- [x] Gamepad-Grundbelegung und Kamera-Grundsatz
- [x] Drei gekoppelte Primär-Loops + Kopplungsressourcen (inkl. Währung **Sol**)
- [x] Belohnungspyramide und -verteilung (DR-27)
- [x] Onboarding-Skript 0:00–3:00 h, Minute für Minute, mit KPIs
- [x] Diegetische Starterwahl „Erstresonanz“ + Starter-Zyklus Blüte > Stein > Sturm
- [x] Startdorf Lindwiesen, Mentorin Ysolde Varn, Rivale Kael Duran
- [x] Makro-Progression „Gestaffelte Offenheit“, Akkorde, Arena-Stufen, Level-Korridore, Zonen-Fixierung
- [x] Wärterrang-Meilensteine und Chorgrößen-Wachstum
- [x] Traversal-Freischaltungsreihenfolge (DR-28)
- [x] Intensitätskurve und Atemzug-Regel (DR-29), Session-Pacing
- [x] Schwierigkeitsgrade, Rückklang, Zugänglichkeitsgrundsatz (visuelle Frequenzen)
- [x] Playtest-Protokoll und Telemetrie-Events
- [x] Code: Design-Regel-Validator, `FWardenRankRow` + CSV, Zonen-Fixierung, Rückklang-State-Machine
- [x] ADR-010 – ADR-015
- [x] CANON aktualisiert

### Übergabe an K03

K03 (**GDD II – Spielstruktur, Progression, Feature-Matrix**) definiert die vollständige Spielstruktur (Spielmodi, Hub-Struktur, Menü- und Spielzustände als globale State Machine), alle Progressionssysteme im Zusammenspiel (Echo-Level-Kurve, Wärter-EP-Quellen, Ruf, Kodex-Stufen – noch ohne finale Mathematik), die vollständige Feature-Abhängigkeitsmatrix für die Produktion und die Content-Verteilung pro Region (Echos, Quests, Siedlungen, POIs).

➡️ **Schreibe „Weiter“, um mit Kapitel 03 zu beginnen.**
