# K58 · VFX

| Feld | Wert |
|---|---|
| Dokument | Kapitel 58 von 68 · Präsentation V |
| Version | 1.0 |
| Owner | Lead VFX Artist, Technical Art Director |
| Mitwirkende | VFX Artists (Kampf, Welt, Story), Technical Artist, Rendering Programmer, Combat Designer, Audio Lead, Accessibility Lead, Cinematics Lead |
| Baut auf | K15 (Wetter, Tageszeit), K17 (Typen), K28–K33 (Kampf, Fähigkeiten, Crescendo-Inszenierung K30 §3, Status/Terrain K32, Bindung K33), K44–K46 (Story-Momente), K54 (Barrierefreiheit), K55 (Quartz, Rufe), K56 (Art Bible: Typfarben, Formsprache, Stille-Bildsprache), K57 (Master-Materialien, MPCs, Asset-Pipeline) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/VFX/TypeVfx.csv`, `StatusVfx.csv`, `VfxBudgets.csv`, `StoryVfx.csv`; Prüfer `tools/ref/aethris_vfx.py` (VFX-01–VFX-06); Modul `Plugins/GameFeatures/GF_VFX` (`UAethrisVfxSubsystem`, Blitzbegrenzer); neue Option `ACC_VFX_INTENSITY` in `Data/UI/AccessibilityOptions.csv` |
| Neue Kanon-Einträge | CANON §227 (VFX-Säulen und Bildsprache), §228 (Fähigkeiten-, Status-, Terrain-VFX), §229 (Welt- und Story-VFX), §230 (Budgets, Barrierefreiheit, Technik); CR-007 (Modul GF_VFX in Schicht Presentation) |

---

## Inhalt

1. [VFX-Säulen](#1-vfx-säulen)
2. [Bildsprache](#2-bildsprache)
3. [VFX-Sprache der 15 Typen](#3-vfx-sprache-der-15-typen)
4. [Fähigkeiten und Crescendos](#4-fähigkeiten-und-crescendos)
5. [Status, Terrain und Kampfwetter](#5-status-terrain-und-kampfwetter)
6. [Welt- und Story-VFX](#6-welt--und-story-vfx)
7. [Barrierefreiheit und Photosensitivität](#7-barrierefreiheit-und-photosensitivität)
8. [Budgets und Performance](#8-budgets-und-performance)
9. [Technik: Niagara-Architektur und GF_VFX](#9-technik-niagara-architektur-und-gf_vfx)
10. [Produktion, Benennung, Review](#10-produktion-benennung-review)
11. [Prüfregeln](#11-prüfregeln)
12. [Anforderungen an andere Abteilungen](#12-anforderungen-an-andere-abteilungen)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. VFX-Säulen

Visuelle Effekte sind in AETHRIS **sichtbar gemachter Klang**. Jede Fähigkeit ist ein Ruf, jede Stillezone eine fehlende Stimme, jede Heilung ein zurückkehrender Ton. Daraus folgen fünf Säulen, die jede VFX-Entscheidung prüfen:

| Säule | Bedeutung | Gegenbeispiel (verboten) |
|---|---|---|
| **V-1 Klang wird Licht** | Effekte folgen Rhythmus und Takt (Quartz, Ruf-Tempo); Wellen, Ringe, Schwingungen sind die Grundformen | Effekte ohne Bezug zum Ton, zufällig getaktet |
| **V-2 Lesbar vor prächtig** | Spielende erkennen in 0,5 s Typ, Ziel und Wirkung einer Fähigkeit – auch in Farbenblind-Modi und bei 40 % Effektdichte | Bildschirmfüllende Partikelwände, die das Ziel verdecken |
| **V-3 Form trägt Typ, Farbe bestätigt** | Jeder Typ hat eine farbunabhängige Form (Zungen, Sechsecke, Ringe …); die Typfarbe ist Zusatz (K56 §3.2) | Typ nur an der Farbe erkennbar |
| **V-4 Würde** | Kein Blut, keine Wunden, keine Zerstörung von Körpern (CD-18); Treffer zeigen Energie, nicht Verletzung | Spritzer, Fleisch, Zerfall |
| **V-5 Stille ist ein Effekt** | Die Abwesenheit von Partikeln, Licht und Bewegung ist bewusst gestaltet (Stillezonen, Velnox, Verstummt) | Stille als „einfach nichts“ ohne Inszenierung |

---

## 2. Bildsprache

### 2.1 Die drei Phasen jedes Effekts

Jeder Kampfeffekt folgt dem Muster **Antizipation – Wirkung – Nachhall**. Das entspricht dem musikalischen Auftakt, dem Schlag und dem Ausklingen und deckt sich mit der Crescendo-Inszenierung aus K30 §3.

| Phase | Anteil | Inhalt | Lesbarkeitsziel |
|---|---|---|---|
| Antizipation (Auftakt) | 20–30 % | Sammeln: Partikel ziehen zum Wirker, Klangmal leuchtet auf, Typform erscheint am Körper | „Wer wirkt welchen Typ?“ |
| Wirkung (Schlag) | 10–20 % | Entladung: Projektil/Welle/Strahl; Treffer exakt auf dem Trefferframe (`AN_HitFrame`) bzw. Quartz-Schlag | „Wen trifft es?“ |
| Nachhall (Ausklang) | 50–70 % | Ringe, Funken, Rauch klingen aus; Status-Onset, Trefferzahl | „Was hat es bewirkt?“ |

### 2.2 Form, Farbe, Wert

| Ebene | Regel |
|---|---|
| Form | Typ-Form (§3) ist auf jeder Effektdichte sichtbar; bei 40 % bleiben die Formträger, Füllpartikel entfallen |
| Farbe | Typfarbe aus `TypeColors.csv` für den aktiven Farbmodus (Normal/Protan/Deutan/Tritan); Treffer und Leuchten heller, Rauch und Staub entsättigt (Spalte `Smoke`) |
| Helligkeitswert | Höchster Wert nur im Schlag; Nachhall ≤ 60 % davon; Bildschirmanteil heller Flächen im Kampf ≤ 25 % außer Crescendo (≤ 40 %) |
| Bewegung | Bewegungscharakter je Typ (§3), damit Typen auch in Graustufen unterscheidbar sind |
| Größe | Skalierung nach Stärke (`0,6 + Stärke/150`, max. 1,6) – stärkere Fähigkeiten sind sichtbar größer, nicht greller |

### 2.3 Synchron mit Klang

Klang-Typ-Fähigkeiten und alle Crescendos setzen ihren Schlag auf einen **Quartz-Schlag** (K55). Andere Typen sind frei getaktet, ihre Treffer-Sounds sind aber an das Treffer-Ereignis gebunden. Klangmale pulsieren in ihrem Ruf-Tempo (K57 §6.5). Dadurch entsteht im Kampf ein gemeinsamer Puls aus Musik, Rufen und Licht – die Kernidee „gesungene Welt“.

---

## 3. VFX-Sprache der 15 Typen

Die Typ-Sprache erweitert die Formsprache der Art Bible (K56 §2) um Partikelmotive, Bewegung und Feldwirkung. Die Spalte **Form** ist das farbunabhängige Merkmal (Farbenblind-Lesbarkeit, Prüfregel VFX-02: paarweise verschieden).

| DisplayName | Motif | Shape | Motion | Cast | Impact | FieldLook | Smoke |
|---|---|---|---|---|---|---|---|
| Glut | Funken, Glutzungen, Hitzeflimmern | Zungen nach oben | aufsteigend, flackernd | Glut sammelt sich in den Fugen | Funkenstern + Glutring | glimmende Risse im Boden | 300 |
| Flut | Wasserschleier, Tropfen, Gischt | Bögen/Wellenkämme | fließend, schwappend | Wasser steigt spiralförmig auf | Gischtkrone | spiegelnde Pfützen, Wellenringe | 100 |
| Stein | Splitter, Staub, Plattenbruch | Blöcke/Facetten | schwer, fallend | Steinplatten heben sich | Bruchkrater mit Brocken | Geröllfelder, Plattenkanten | 450 |
| Sturm | Böen, Federn, Blitzbögen | Spiralen | wirbelnd, schnell | Wirbel um den Körper | Spiralknall | Windwirbel, Laubfahnen | 150 |
| Blüte | Blätter, Pollen, Ranken | Blattformen | wachsend, sanft | Knospen öffnen sich | Blütenregen | sprießende Ranken, Pollenschweben | 50 |
| Frost | Reif, Eisnadeln, Schneekristalle | Sechsecke | knisternd, erstarrend | Reif kriecht über die Haut | Eisnadelstern | Eisplatten, Reifmuster | 100 |
| Leere | Negativraum, Ringe, Löcher | Ringe/Lücken | einziehend (nach innen) | Licht wird eingesogen | Implosion mit Ring | dunkle Löcher, gedämpfte Farben | 0 |
| Licht | Strahlen, Kränze, Glanz | Strahlenkranz | strahlend, ruhig | Lichtkranz hinter dem Kopf | Strahlenstern | Lichtsäulen, Glanzpunkte | 0 |
| Gift | Blasen, Tropfen, Sporen | Tropfen/Blasen | blubbernd, zäh | Drüsen glimmen auf | Blasenplatzer + Tropfen | Pfützen mit Blasen, Sporennebel | 200 |
| Metall | Funkenflug, Klingen, Nieten | Kanten/Dreiecke | schneidend, klirrend | Platten verschieben sich | Klingen-Funkenkreuz | Metallsplitter, Reflexe | 250 |
| Geist | Schleier, Halbmonde, Irrlichter | Halbmonde | schwebend, unscharf | Schleier löst sich vom Körper | Halbmondwelle | Nebelschleier, Irrlichter | 350 |
| Kristall | Prismen, Lichtbrechung, Rauten | Rauten | klirrend, brechend | Kristalle wachsen aus dem Boden | Prismensplitter mit Spektrum | Kristallsprossen, Regenbogenkanten | 0 |
| Klang | Schallringe, Membranen, Notenlinien | Konzentrische Bögen | pulsierend im Takt | Schallringe im Ruf-Tempo | Resonanzring (Quartz-Schlag) | schwingende Linien am Boden | 0 |
| Schwerkraft | Orbits, schwebende Splitter, Verzerrung | Orbits/Kreisbahnen | kreisend, verlangsamt | Splitter beginnen zu kreisen | Verzerrungsblase + Orbit | schwebende Steine, Raumkrümmung | 150 |
| Arkan | Glyphen, Kanons, Spiegelungen | Glyphen | gespiegelt, kanonisch | Glyphenkreis unter dem Echo | Glyphensiegel bricht | leuchtende Glyphenbahnen | 0 |

**Hinweise zur Umsetzung:**

- **Leere** ist der einzige Typ mit nach innen gerichteter Bewegung: Partikel werden eingesogen, Licht verschwindet. Rauchanteil 0, weil Leere nichts hinterlässt (V-5).
- **Klang** nutzt keine Partikel als Hauptträger, sondern Ringe aus Mesh-Partikeln mit Verzerrung (Refraction) – die Schallwelle bleibt dadurch auch bei 40 % Effektdichte vollständig.
- **Kristall** bricht die Typfarbe in ein Spektrum; das Spektrum ist in allen Farbmodi aus den Modus-Farben aufgebaut, damit Kristall nicht mit Licht verwechselt wird.
- **Geist** ist der einzige Typ mit absichtlicher Unschärfe (Tiefenunschärfe auf Partikelebene) – Halbmondformen bleiben aber scharf.
- **Schwerkraft** verlangsamt die Partikelzeit in seinem Wirkradius (Zeitskala 0,4) und erzeugt dadurch die Wirkung „Raum wird zäh“.

### 3.1 Duale Typen und Sekundärtyp

Fähigkeiten haben genau einen Typ. Echos mit zwei Typen zeigen den Sekundärtyp nur im **Klangmal-Akzent** (Oberton, K55) und als dünne zweite Partikelspur im Nachhall von Crescendos. Fähigkeits-VFX sind nie gemischt – Lesbarkeit vor Detail (V-2).

---

## 4. Fähigkeiten und Crescendos

### 4.1 Vorlagensystem

330 Fähigkeiten bekommen **keine 330 eigenen Effekte**. Stattdessen gibt es Vorlagen je Kategorie (Physisch/Spezial/Status) und Zielform; Typ, Größe, Farbe und Takt sind Parameter. `aethris_vfx.py` ordnet jede Fähigkeit aus `Abilities.csv` einer Vorlage zu:

| Vorlage | Fähigkeiten | Inhalt |
|---|---|---|
| `NS_Abl_Phys_Line` | 3 | Wirken → Linienwelle über eine Reihe |
| `NS_Abl_Phys_Melee` | 40 | Kontakt: Ausholen, Schlagspur, Treffer am Ziel |
| `NS_Abl_Phys_Projectile` | 5 | Wirken → Projektil → Treffer |
| `NS_Abl_Spec_Area` | 10 | Wirken → Flächenwelle über alle Gegner |
| `NS_Abl_Spec_Line` | 11 | Wirken → Linienwelle über eine Reihe |
| `NS_Abl_Spec_Projectile` | 42 | Wirken → Projektil → Treffer |
| `NS_Abl_Stat_AllyArea` | 6 | Welle über alle Verbündeten |
| `NS_Abl_Stat_AllyBeam` | 5 | Strahl zu einem Verbündeten |
| `NS_Abl_Stat_AllyLine` | 5 | Welle über eine eigene Reihe |
| `NS_Abl_Stat_Area` | 4 | Wirken → Flächenwelle über alle Gegner |
| `NS_Abl_Stat_Field` | 16 | Wirken → Feld-/Terrain-Aufbau |
| `NS_Abl_Stat_Projectile` | 14 | Wirken → Projektil → Treffer |
| `NS_Abl_Stat_Self` | 19 | Aura am Wirker |
| `NS_Abl_PassiveTrigger` | 90 | Passiv-Auslöser: Puls + Typ-Motiv am Echo (0,5 s) |
| `NS_Abl_FieldUse` | 30 | Feldfähigkeit in der Welt: Typ-Motiv am Ziel (Fels, Wasser, Licht …) |
| `NS_Cresc_ABL_U###` | 30 | je Crescendo eine Signatur auf dem Grundgerüst |
| **Σ** | **330** | **15 Vorlagen + 30 Signaturen** |

Die Vorlage entscheidet über Ablauf und Raum (Projektil fliegt, Welle läuft eine Reihe entlang, Aura bleibt am Wirker), das Typ-Modul (Niagara-Modul `NM_Type_<Typ>`) über Aussehen. Kombiniert ergeben sich 13 aktive Vorlagen × 15 Typmodule = 195 Varianten aus 28 Bausteinen.

**Beispiele (jede 15. aktive Fähigkeit):**

| Fähigkeit | Typ | Kategorie | Ziel | Vorlage | Größe | Motiv |
|---|---|---|---|---|---|---|
| Funkenbiss | Glut | Physical | Single | `NS_Abl_Phys_Melee` | 0,87 | Funken |
| Gezeitenwelle | Flut | Special | Row | `NS_Abl_Spec_Line` | 1,00 | Wasserschleier |
| Steinhaut | Stein | Status | Self | `NS_Abl_Stat_Self` | 0,80 | Splitter |
| Gewitterruf | Sturm | Status | Field | `NS_Abl_Stat_Field` | 0,80 | Böen |
| Raureifhauch | Frost | Special | Single | `NS_Abl_Spec_Projectile` | 0,87 | Reif |
| Seelenzehrer | Leere | Special | Single | `NS_Abl_Spec_Projectile` | 1,07 | Negativraum |
| Läuterung | Licht | Status | Allies | `NS_Abl_Stat_AllyArea` | 0,80 | Strahlen |
| Korrosion | Gift | Status | Single | `NS_Abl_Stat_Projectile` | 0,80 | Blasen |
| Geisterhauch | Geist | Special | Single | `NS_Abl_Spec_Projectile` | 0,87 | Schleier |
| Resonanzprisma | Kristall | Special | Single | `NS_Abl_Spec_Projectile` | 1,07 | Prismen |
| Donnerhall | Klang | Special | Enemies | `NS_Abl_Spec_Area` | 1,27 | Schallringe |
| Gewichtslast | Schwerkraft | Status | Single | `NS_Abl_Stat_Projectile` | 0,80 | Orbits |

### 4.2 Zeitablauf einer aktiven Fähigkeit

```
 Kampf-Tick (K28) ──► Zug beginnt
   AM_Echo_Cast_<Kat> startet (Animation K57)                         ┐
   ├─ 0,00 s  NS_Abl_<Kat>_<Form>: Antizipation (Typform am Körper)    │ Dauer abhängig von
   ├─ 0,35 s  Wirkung: Projektil/Welle startet (Root-Bone-Socket)      │ ACC_ANIM_SPEED
   ├─ AN_HitFrame: Treffer-VFX am Ziel (Impact je Typ), Kamerastoß*    │ (100/150/200 %)
   ├─ +0,10 s Trefferzahl (UI), Status-Onset (§5)                      │
   └─ +0,60 s Nachhall klingt aus, Zug endet logisch (Kampf wartet     ┘
              nicht auf das Ende des Nachhalls)
   * Kamerastoß entfällt bei ACC_MOTION.
```

Bei **Kampfanimation 200 %** (ACC_ANIM_SPEED) wird der Nachhall auf 40 % gekürzt und die Antizipation auf 0,2 s; Treffer bleiben unverändert lesbar.

### 4.3 Kontakt-Fähigkeiten

Physische Kontakt-Fähigkeiten (`Contact`-Tag) nutzen `NS_Abl_Phys_Melee`: eine **Schlagspur** (Ribbon entlang des Angriffsknochens), ein Typ-Impact am Kontaktpunkt (Motion Warping, K57 §6.3) und einen kurzen Rückstoß-Ring am Boden. Treffer zeigen Energie (Funken, Ringe, Splitter), nie Verletzung (V-4).

### 4.4 Crescendos

Die 30 Crescendos (K30) bekommen je eine **Signatur** auf einem gemeinsamen Grundgerüst. Das Grundgerüst setzt die Inszenierung aus K30 §3 um:

| Phase (K30) | Zeit | VFX | Licht/Post | Audio-Kopplung |
|---|---|---|---|---|
| Ankündigung | Zug vorher | Goldener Marker auf der Zeitleiste, Klangmal des Echos pulsiert doppelt | – | Chor-Akkord |
| Anlauf | 0,0–0,8 s | Typfarbe füllt den Bildrand (Vignette in Typfarbe, 15 %), Partikel strömen zum Echo, Typform wächst | Szene dimmt auf 60 % | Auftakt auf Quartz |
| Entladung | 0,8–2,6 s | Signatur (je Crescendo), maximale Ausdehnung, Treffer auf Schlag 1 des Taktes | Bloom-Spitze (1×, Blitzbegrenzer) | Typ-Ton + Weltlied-Fragment |
| Nachhall | 2,6–4,0 s | Ringe klingen aus, Status-Symbole, Typform zerfällt in Funken | Szene zurück auf 100 % | Ausklang |
| Kurzfassung (Option/PvP) | 1,5 s | Anlauf 0,3 s, Entladung 0,8 s, Nachhall 0,4 s; Signatur ohne Kameraflug | wie oben | gekürzt |

**Signaturen der Arten:** Arten, deren Signaturkonzept ein Crescendo beschreibt (★, K30), legen eine **Variante** über die Crescendo-Signatur: eigenes Klangmal-Muster im Anlauf, eigener Ruf, eigene Kamera. Die Mechanik und die Grundstruktur bleiben identisch. Diese Varianten sind die 61 Crescendo-Signatur-Clips aus K57 §6 und werden als Niagara-Modul-Overrides umgesetzt, nicht als eigene Systeme.

### 4.5 Kombos und Akkorde

| Element | Darstellung |
|---|---|
| Kombo (K33, `Combos.csv`) | Zwischen dem ersten und zweiten Treffer verbindet ein **Resonanzfaden** beide Ziele; beim zweiten Treffer verschmelzen beide Typmotive im Impact (z. B. Dampfstoß: Gischtkrone + Funkenstern = Dampfring). Kombo-Name als UI-Einblendung. |
| Akkord (Chords.csv) | Steht ein Akkord-Team auf dem Feld, zeigt der Boden unter den drei Echos ein **Dreieck aus Notenlinien** in ihren drei Typfarben; bei Harmoniegewinn läuft ein Puls entlang der Linien. |
| Harmonie-Leiste | UI (K54); im Weltbild nur das gemeinsame Pulsieren der Klangmale (Takt = Musik-Tempo) ab 80 Harmonie. |

---

## 5. Status, Terrain und Kampfwetter

### 5.1 Status

Status (K32) werden am Echo als **Loop** gezeigt und zusätzlich als Symbol in der UI. Jeder Status hat eine farbunabhängige Form (VFX-02). Pro Echo sind höchstens **zwei** Status-Loops gleichzeitig sichtbar (Priorität: zuletzt erhaltener, dann stärkster); weitere nur als UI-Symbol.

| DisplayName | Loop | Shape | Onset | End |
|---|---|---|---|---|
| Brand | Glutfunken steigen aus Fugen, Hitzeflimmern | Zungen nach oben | Aufflammen | Erlöschen mit Rauchfaden |
| Ausgetrocknet | Risse in der Oberfläche, Staubrieseln | Risslinien | Haut wird matt | Feuchter Glanz kehrt zurück |
| Rückstoß | Kurzer Schub-Schleier hinter dem Echo | Pfeil nach hinten | Stoßwelle | – |
| Verlangsamt | Nachzieh-Bilder (Ghosting) bei Bewegung | Doppelkontur | Zeitlupen-Ring | Ring springt auf |
| Welke | Fallende graue Blätter, Farbverlust an Rändern | Fallende Blätter | Ränder ergrauen | Farbe kehrt zurück |
| Starre | Eisschale um den Körper | Sechseck-Panzer | Einfrieren (0,6 s) | Eis springt ab |
| Entzug | Dünne Fäden ziehen zum Gegner | Fäden | Faden spannt sich | Faden reißt |
| Geblendet | Glanzpunkte vor den Augen, Kopf abgewandt | Sternchen am Kopf | Lichtblitz (gedämpft, ≤ 1 Blitz) | Blinzeln |
| Vergiftet | Blasen steigen auf, Drüsen glimmen | Blasen | Tropfen trifft | Blasen platzen |
| Erschüttert | Zittern, Staub fällt ab | Zickzack-Linien | Stoßwelle | Abschütteln |
| Furcht | Schatten wächst hinter dem Echo, Körper geduckt | Schatten-Halbmond | Schatten fällt | Schatten zieht ab |
| Gebrochen | Feine Risse leuchten, Splitter lösen sich | Bruchlinien | Knacken | Risse schließen sich |
| Verstummt | Klangmal erlischt, Schallringe fehlen | Durchgestrichener Ring | Klangmal blendet aus (1,5 s) | Erster Puls kehrt zurück |
| Schwebend | Echo hebt 0,5 m ab, Orbit-Splitter | Orbit unter den Füßen | Abheben | Landung mit Staub |
| Verflucht | Glyphe über dem Kopf, dreht sich | Glyphe | Glyphe brennt sich ein | Glyphe zerfällt |

**Verstummt** ist der wichtigste Status für die Bildsprache: Das Klangmal blendet über 1,5 s aus (Material-Parameter `Silenced`, K57 §8.2), Schallringe des Echos fehlen, und der Ruf entfällt. Die Rückkehr („Erster Puls kehrt zurück“) ist ein bewusst schöner Moment – ein kleiner Vorgriff auf die Heilung der Welt.

### 5.2 Terrain

Terrains (K32, `Terrains.csv`) liegen als **Decal + Bodennebel** über dem Kampfplatz (Radius des Kampfrings, K28). Jedes Terrain nutzt die Feldwirkung seines Typs:

| Terrain | Typ | Overlay (Decal + Bodennebel) | Form |
|---|---|---|---|
| Glutboden | Glut | glimmende Risse im Boden | Zungen nach oben |
| Glutsand | Glut | glimmende Risse im Boden | Zungen nach oben |
| Überwuchs | Blüte | sprießende Ranken, Pollenschweben | Blattformen |
| Sumpf | Gift | Pfützen mit Blasen, Sporennebel | Tropfen/Blasen |
| Flutfeld | Flut | spiegelnde Pfützen, Wellenringe | Bögen/Wellenkämme |
| Eisfläche | Frost | Eisplatten, Reifmuster | Sechsecke |
| Sturmfeld | Sturm | Windwirbel, Laubfahnen | Spiralen |
| Kristallfeld | Kristall | Kristallsprossen, Regenbogenkanten | Rauten |
| Klangfeld | Klang | schwingende Linien am Boden | Konzentrische Bögen |
| Schwerefeld | Schwerkraft | schwebende Steine, Raumkrümmung | Orbits/Kreisbahnen |
| Glyphenfeld | Arkan | leuchtende Glyphenbahnen | Glyphen |
| Stillefeld | Leere | dunkle Löcher, gedämpfte Farben | Ringe/Lücken |
| Lichtfeld | Licht | Lichtsäulen, Glanzpunkte | Strahlenkranz |
| Nebelfeld | Geist | Nebelschleier, Irrlichter | Halbmonde |
| Missklang-Terrain | Leere | dunkle Löcher, gedämpfte Farben | Ringe/Lücken |

Terrains sind auf Hängen und in Wasser als Decal projiziert (DBuffer, `M_Decal_Master`) und nie heller als 50 % der Treffer-Helligkeit, damit Fähigkeiten auf dem Feld lesbar bleiben. Das **Stillefeld** und **Missklang** (beide Leere) unterscheiden sich in der Form: Stillefeld = stehende Staubkörner (keine Bewegung), Missklang = zitternde, gebrochene Linien.

### 5.3 Kampfwetter

Der Kampf übernimmt das Weltwetter (K32); Fähigkeiten können es für N Runden ändern. Kampfwetter nutzt dieselben Systeme wie das Weltwetter (§6.3), aber mit einem **Kampfring-Fokus**: Partikeldichte im Ring + 20 %, außerhalb − 30 %, damit der Raum des Kampfes sichtbar bleibt. Der Blitzschlag im Gewitter (alle 4 Runden) ist ein angekündigter Effekt: 1,5 s vorher bildet sich ein Lichtkreis am Ziel (Blitzwarnung 1,5 s wie in der Welt, K14), dann Schlag über den Blitzbegrenzer (§7).

---

## 6. Welt- und Story-VFX

### 6.1 Klangmale in der Welt

Klangmale sind die häufigsten Effekte des Spiels: Jedes sichtbare Echo trägt eines. Sie sind deshalb **Material-Effekte** (`MF_Klangmal`, K57 §8.2) und keine Partikel. Partikel kommen nur hinzu bei:

| Anlass | Partikel | Budget-Kategorie |
|---|---|---|
| Ruf | 1 Schallring je Schlag (Mesh-Partikel), max. 4 | Echo |
| Emotion Freude | Funken in Klangmal-Farbe (8–12) | Echo |
| Begleiter streicheln | Herzschlag-Ring + 6 Funken | Echo |
| Nacht, < 15 m | Leuchtstaub um das Klangmal (Lumen-Emissive trägt zur Beleuchtung bei) | Echo |
| Ferne (> 40 m) | keine Partikel, nur Material | – |

### 6.2 Ambiente

Ambiente-Effekte (Insekten, Pollen, Staub, Glühwürmchen, Funkenflug, Gischt) werden über **Significance** gesteuert: Kamera-nahe Zellen (≤ 60 m) bekommen volle Dichte, bis 150 m die Hälfte, darüber nur noch statische Lichtpunkte (Sprites, gebacken in HLOD-Imposter). Jede Region hat einen Ambiente-Satz in ihrer Signaturfarbe (K56 §3.3):

| Region | Ambiente-Signatur |
|---|---|
| R01 Verdanthain | Lindgold-Pollen, Glockenblüten-Tonringe im Wind |
| R02 Kharsgrat | Flechtenstaub, schwebende Kiesel um Ahnenfelsen |
| R03 Morvenmoor | Irrlichter (cyan), Nebelschwaden, Laternenmotten |
| R04 Sahrun-Weite | Sandschleier, Hitzeflimmern, nachts Sternfunkeln über Glasebene |
| R05 Ignareth | Ascheflocken, Glutfunken, Lavaglühen am Horizont |
| R06 Saltrand | Gischt, Salzfunkeln, Biolumineszenz der Brandung nachts |
| R07 Hvitfell | Schneekristalle, Auroraband, Atemhauch |
| R08 Ael'Dorun | Glyphenstaub (gold), schwebende Schriftzeichen in Archiven |
| R09 Prismtiefen | Kristallfunken, Spektrallinien in Höhlen |
| R10 Nimbara | Wolkenfetzen, Morgenrosa-Lichtstreifen, Windfahnen |

In **Stillezonen** ist die Ambiente-Dichte 0 – außer den stehenden Staubkörnern (`SVFX_SILENCE`), deren Zeit-Skala auf 0 steht. Das Fehlen aller Bewegung ist der Effekt (V-5).

### 6.3 Wetter

| Wetter | Niagara-System | Besonderheit | Kollision |
|---|---|---|---|
| Regen | `NS_Weather_Rain` | Tropfen + Spritzer auf Oberflächen (Depth-Buffer-Kollision), Pfützen über `MPC_Weather.Wetness` | Depth Buffer |
| Gewitter | `NS_Weather_Rain` + `NS_Weather_Lightning` | Blitze ≤ 1 je 3 s (Blitzbegrenzer), Wetterleuchten weich | – |
| Nebel | Volumetric Fog + `NS_Weather_FogWisps` | Nebelschwaden nur Nahbereich | – |
| Schnee | `NS_Weather_Snow` | Flocken, Schneeauflage über `MPC_Weather.Snow` | Depth Buffer |
| Hitzewelle | Post-Process-Flimmern + `NS_Weather_HeatShimmer` | Flimmern nur an Horizont und über Felsen | – |
| Sandsturm | `NS_Weather_Sand` | Sichtweite 40–80 m, Sandfahnen; Resonanzsinn wird zur Navigation (K10) | – |
| Aurora | Himmels-Material + `NS_Weather_AuroraMotes` | Aurora-Bänder im Himmelsmaterial, Lichtpartikel steigen auf | – |
| Ascheregen | `NS_Weather_Ash` | graue Flocken, Glutpartikel vereinzelt | Depth Buffer |
| Resonanzsturm | `SVFX_STORM` | Himmel in Notenlinien, Blitze auf Quartz-Schläge (≤ 2 Hz) | – |

Wetter-Partikel sind **kameragebunden** (ein Volumen von 40 × 40 × 30 m um die Kamera), nicht weltweit. Fernwetter (Regenschleier am Horizont, Sandwände) sind Himmels- und Nebelmaterialien.

### 6.4 Traversal und Resonanzsinn

| Aktion | VFX |
|---|---|
| Gleiten | Luftspuren an den Gleiterspitzen, bei Aufwind aufsteigende Partikel (Aufwinde sichtbar machen, K14) |
| Reiten (Boden/Fly/Swim/Climb/Dig) | Staub/Gischt/Wolkenspuren/Steinsplitter/Erdauswurf je Reitart; Klangmal des Reittiers im Lauftakt |
| Klettern | Kleine Staubwolken an Griffpunkten; Kletterflächen haben keine VFX-Markierung (Lesbarkeit über Material, K56 §8) |
| Resonanzsinn | Schallwelle läuft vom Spieler aus (40 m/s, Radius 120 m); Echos erscheinen als Klangmal-Konturen in Typform; Resonanzsteine und Schätze als Ringe (`SVFX_RESONANCE_SENSE`) |
| Schnellreise | Resonanzstein-Säule aus Notenlinien, Spieler löst sich in Schallringe auf (Ankunft umgekehrt) |

### 6.5 Story-Momente

| DisplayName | Chapter | Look | Technique | FlashHz |
|---|---|---|---|---|
| Stillezone | K10, K44 | Graue Schleier, stehende Staubkörner, verstummte Klangmale | MPC_Silence + NS_Silence_Dust (Partikel stehen still, Zeit-Skala 0) | 0 |
| Heilungswelle | K44–K46 | Farbwelle vom Resonanzstein, 2.000 m in 4 s, Blüten öffnen sich in der Front | MF_Healing + NS_Heal_Front (GPU, Ring-Emitter, Lumen-Emissive) | 0.25 |
| Evolution | K19 | Lichtkokon in Typfarbe, Klangmal-Ringe, heller Höhepunkt verdeckt Mesh-Wechsel | NS_Evolution + MF_DitherFade, Bloom-Spitze 1× | 1 |
| Crescendo-Grundgerüst | K30 | Szene dimmt, Typ-Motiv baut sich in drei Phasen auf (Sammeln, Entladen, Nachhall) | NS_Crescendo_<Typ> + Signatur-Modul je Art | 2 |
| Resonanzsturm | K15, K55 | Himmel in Notenlinien, Blitze quantisiert auf den Takt | NS_ResonanceStorm (Himmel), Blitze auf Quartz-Schläge (≤ 2 Hz) | 2 |
| Krone | K45, K46 | Kalte Symmetrie, Kristallgitter breitet sich aus, alle Partikel exakt synchron | NS_Crown_Lattice (Mesh-Partikel, deterministisch) | 0.5 |
| Velnox-Negativraum | K46, K62 | Formen aus fehlendem Licht; Partikel schwarz ohne Rand, Ton fehlt | NS_Velnox_Void (subtraktiv über Custom Depth, Stencil-Maske) | 0 |
| Neues Lied (Ende) | K46 | Aurora in zehn Regionsfarben, Klangmale aller Echos leuchten im Takt | NS_Aurora_TenColors + MPC_Resonance.CrownPulse | 0.5 |
| Sanfte Stille (Ende) | K46 | Silberschleier, langsames Schneefallen aus Licht | NS_SilverVeil, Sättigung −15 % | 0 |
| Bindung (Einstimmen) | K33 | Resonanzfäden zwischen Resonator und Echo, Anschlag-Ringe | NS_Bond_Threads + NS_Bond_Strike (gut/perfekt/daneben) | 2 |
| Resonanzsinn | K14 | Schallwellen über die Landschaft, Echos als Klangmal-Konturen | Post-Process (Kantenerkennung) + NS_Sense_Wave | 1 |
| Resonanzstein | K08 | Ruhiges Pulsieren, beim Aktivieren Säule aus Notenlinien | NS_Stone_Idle + NS_Stone_Activate | 1 |
| Dorun-Glyphen | K12, K45 | Glyphen leuchten in Leserichtung auf | MF_Glyph, Material-Animation | 1 |
| Ignar-Ausbruch | K09 | Ascheregen, Lavafontänen, Glutlicht am Himmel | NS_Eruption + Lava-Layer-Wechsel | 0.5 |

**Heilungswelle im Detail:** Die Welle ist eine Kombination aus Material (`MF_Healing` hebt die Entsättigung auf, K57 §8.4), einem GPU-Ring-Emitter an der Wellenfront (Blüten, Lichtpunkte, aufsteigende Schallringe) und dem Data-Layer-Wechsel `DL_Story_R##_Silence` → `DL_Story_R##_Healed`, den die Welle verdeckt. Die Front läuft in 4 s 2.000 m weit (CANON §220) – das ist schneller als Streaming; deshalb werden die „Healed“-Zellen 30 s vorher vorgeladen.

**Velnox-Negativraum:** Velnox (K46, K62) besteht aus Formen, an denen *nichts* ist. Technisch: Velnox-Meshes schreiben in Custom Depth/Stencil; ein Post-Process-Material setzt dort den Bildinhalt auf Schwarz ohne Rand und unterdrückt Bloom, Nebel und Lumen-Beiträge. Partikel um Velnox sind ebenfalls subtraktiv (schwarze, randlose Punkte). Ton fehlt im selben Bereich (K55). So entsteht die einzige Figur des Spiels, die durch Abwesenheit gezeichnet wird.

**Krone:** Alle Partikel der Krone sind deterministisch (feste Saat, keine Zufallsbewegung) und exakt synchron – kalte Symmetrie als Gegenteil des lebendigen Takts der Welt.

**Neues Lied / Sanfte Stille:** Die beiden Enden haben eigene Abschluss-Effekte; beide liegen auf dem Data Layer `DL_Nachhall` und bleiben nach dem Abspann in der Welt (Aurora in zehn Farben bzw. Silberschleier mit Lichtschnee), damit die Entscheidung im Nachspiel sichtbar ist.

---

## 7. Barrierefreiheit und Photosensitivität

### 7.1 Regeln

| Regel | Inhalt | Umsetzung |
|---|---|---|
| **Blitz-Grenze** | Höchstens 3 Helligkeitsspitzen pro Sekunde, Mindestabstand 1/3 s, auf allen Plattformen und in allen Modi | `Aethris::Vfx::AllowFlash` im `UAethrisVfxSubsystem` (Blitzbegrenzer); Prüfregel VFX-04 für Klangmal-Pulse und Story-VFX |
| **Rote Blitze** | Keine großflächigen gesättigt roten Wechsel (Glut nutzt Orange `#E8562A`, nie reines Rot) | Art-Review |
| **Flächenanteil** | Helle Flächen im Kampf ≤ 25 % des Bildes (Crescendo ≤ 40 %) | Automatischer Helligkeits-Histogramm-Test im Review-Build |
| **Muster** | Keine hochkontrastigen Streifenmuster > 5 Linienpaare über ≥ 25 % des Bildes (Klang-Ringe sind weich) | Art-Review |
| **Bewegungsreduktion** (`ACC_MOTION`) | Kamerastöße aus, Helligkeitsspitzen auf 40 %, Bewegungsunschärfe aus, Wetterpartikel −50 % | `FlashIntensity`, Kamera-Modifier |
| **Effektdichte** (`ACC_VFX_INTENSITY`, neu) | 100 % / 70 % / 40 %: Partikelanzahl und Helligkeitsspitzen; Formträger (Typform) bleiben; UI-Markierungen unverändert | `ScaleSpawnCount` |
| **Farbenblind** (`ACC_COLORBLIND`) | Typfarben aus der Modus-Palette (K56); Formen (§3, §5) tragen die Information | Parameter `User.TypeColor` |
| **Visuelle Klangsignale** (`ACC_VISUAL_SOUND`) | Rufe außerhalb des Bildes als Schallring am Bildrand in Richtung der Quelle | UI3D-Kategorie (immer 100 %) |

Die Blitz-Grenze orientiert sich an verbreiteten Richtlinien zur Vermeidung photosensitiver Anfälle (höchstens drei Blitze pro Sekunde, besondere Vorsicht bei Rot). Vor der Zertifizierung prüft QA alle Story-Momente und Crescendos zusätzlich mit einem automatischen Analysewerkzeug auf Basis von Bildschirmaufnahmen (K66).

### 7.2 Klangmal-Puls

Der schnellste Ruf im Katalog hat 104 BPM. Bei Angst steigt das Tempo um 30 % (K57 §6.4) – das ergibt 2,25 Hz und liegt unter der Grenze. Neue Arten mit mehr als 138 BPM würden VFX-04 verletzen; der Katalog-Validator (K16) übernimmt diese Grenze.

### 7.3 Neue Option `ACC_VFX_INTENSITY`

Die Option ergänzt die Barrierefreiheits-Liste aus K54 (Bereich Sehen) und ist in `Data/UI/AccessibilityOptions.csv` eingetragen. Sie wirkt nicht auf Gameplay; Ankündigungen (Crescendo-Marker, Blitzwarnung) bleiben vollständig.

---

## 8. Budgets und Performance

### 8.1 Budgets je Kategorie

| DisplayName | PS5Particles | Switch2Particles | PS5GpuMs | Switch2GpuMs | MaxOverdraw | Notes |
|---|---|---|---|---|---|---|
| Welt-Ambiente (Insekten, Pollen, Staub, Klangmale der Umgebung) | 60000 | 15000 | 0.6 | 0.9 | 4 | Significance-gesteuert, 0 in Stillezonen |
| Wetter (Regen, Schnee, Asche, Sand, Aurora) | 80000 | 20000 | 0.7 | 1.0 | 3 | Kamera-gebunden, Kollision per Depth Buffer |
| Klangmale und Emotionen der Echos in Nahdistanz | 20000 | 6000 | 0.3 | 0.5 | 2 | bis 40/16 Echo-Actors |
| Fähigkeiten (Wirken, Projektil, Treffer) | 40000 | 12000 | 0.9 | 1.4 | 6 | max. 2 gleichzeitig plus Nachglühen |
| Crescendo (eins zur Zeit) | 60000 | 18000 | 1.2 | 1.8 | 8 | Kamera-Inszenierung, Rest der Szene gedimmt |
| Status-Loops (bis 6 Echos) | 12000 | 4000 | 0.2 | 0.3 | 2 | je Echo max. 2 sichtbare Status |
| Terrain-Overlay (Kampf) | 15000 | 5000 | 0.3 | 0.4 | 2 | Decal + Bodennebel |
| Story-Setpieces (Heilungswelle, Krone, Velnox …) | 120000 | 30000 | 2.0 | 2.8 | 8 | nur in gescripteten Momenten, andere Kategorien halbiert |
| Traversal (Gleiten, Reiten, Klettern, Resonanzsinn) | 15000 | 5000 | 0.3 | 0.4 | 3 | Spieler + Reittier |
| Weltgebundene UI (Markierungen, Kodex-Linse) | 5000 | 2000 | 0.1 | 0.15 | 2 | unabhängig von ACC_VFX_INTENSITY |

### 8.2 Worst-Case-Szene

Die teuerste reguläre Szene ist ein **Trio-Kampf (3+3)** im Gewitter auf einem Terrain, in dem ein Crescendo ausgelöst wird, während eine weitere Fähigkeit nachhallt und alle sechs Echos zwei Status tragen. `aethris_vfx.py` rechnet die Kategorien mit ihren Anteilen zusammen (Crescendo 100 %, Fähigkeit 50 %, Status 100 %, Terrain 100 %, Wetter 100 %, Echo 30 %, Ambiente 50 %, UI 100 %):

| Plattform | Partikel (Worst Case) | Grenze | GPU ms | Grenze | Ergebnis |
|---|---|---|---|---|---|
| PS5 | 228.000 | 300.000 | 3,34 | 4,0 | ✅ |
| Switch 2 | 64.300 | 90.000 | 4,95 | 5,5 | ✅ |

Die Gesamtgrenzen (PS5 300.000 Partikel / 4,0 ms, Switch 2 90.000 / 5,5 ms) sind der VFX-Anteil am GPU-Budget aus K65. Story-Setpieces haben ein eigenes, höheres Budget und halbieren dafür alle anderen Kategorien (`SetStorySetpieceActive`).

### 8.3 Techniken

| Technik | Einsatz |
|---|---|
| GPU-Simulation | Standard für alle Emitter > 200 Partikel; CPU nur für Emitter mit Gameplay-Rückmeldung (z. B. Event-Auslöser) |
| Significance Manager | Effekte nach Distanz/Bildgröße priorisiert; unsichtbare Effekte pausieren |
| Pooling | `ENCPoolMethod::AutoRelease` für alle Kampf- und Ambiente-Effekte; Vorwärmen der Kampfvorlagen beim Kampfstart |
| Skalierbarkeit | Niagara Effect Types je Kategorie (`ET_Ambient`, `ET_Ability` …) mit Plattform-Skalierungsprofilen (PS5/XSX/PC/Switch 2) |
| Lichter | Partikel-Lichter nur im Schlag (≤ 4 gleichzeitig, ohne Schatten); sonst Emissive mit Lumen |
| Overdraw | Max. Overdraw je Kategorie (Tabelle); große Flächen als Mesh-Partikel statt gestapelter Sprites |
| Transluzenz | Separate Translucency für Kampf-VFX; Story-Setpieces dürfen Lumen-Translucency nutzen |
| Fern | Ab 150 m Partikel durch gebackene Sprites/Flipbooks ersetzt; ab 500 m nur Lichtpunkte |

### 8.4 Switch 2

Auf Switch 2 gelten eigene Profile: Partikel etwa 30 % der PS5-Werte, keine Partikel-Lichter außer Crescendo-Schlag, Refraction durch Normal-Map-Verzerrung ersetzt, Volumetric Fog in halber Auflösung, Kampfwetter im Ring −40 %. Die Typform bleibt in jedem Profil erhalten (V-2).

---

## 9. Technik: Niagara-Architektur und GF_VFX

### 9.1 Baukasten

```
NS_Abl_<Kat>_<Form>            (13 Vorlagen + PassiveTrigger + FieldUse)
 ├── Emitter Antizipation   ── NM_Type_<Typ>.Cast        (Modul je Typ, 15)
 ├── Emitter Wirkung        ── NM_Shape_<Form>           (Projektil/Welle/Strahl/Aura …)
 ├── Emitter Treffer        ── NM_Type_<Typ>.Impact
 ├── Emitter Nachhall       ── NM_Type_<Typ>.Linger + NM_Smoke (Smoke-Anteil)
 └── User-Parameter         User.TypeColor, User.SpawnScale, User.Smoke, User.QuartzBeat, User.Target
NS_Cresc_ABL_U###             (30, Grundgerüst NS_Cresc_Base + Signatur-Emitter)
NS_Status_<Status>            (15 Loops + Onset/End)
NS_Terrain_<Typ>              (Decal + Bodennebel je Typ)
NS_Weather_*, NS_Echo_*, NS_Amb_R##_*, NS_Story_*
```

**Niagara Data Channels** verbinden Gameplay und VFX ohne direkte Referenzen: Der Kampf schreibt Treffer-Ereignisse (Position, Typ, Stärke, Effektivität) in den Kanal `NDC_CombatHits`; ein einziges Sammel-System liest den Kanal und erzeugt Treffer-Funken. Dadurch skaliert die Zahl der Systeme nicht mit der Zahl der Treffer.

### 9.2 Modul GF_VFX (CR-007)

Bisher kannte CANON §26 in der Schicht Presentation nur GF_UI und GF_Audio. VFX bekommt ein eigenes Modul **GF_VFX** (Schicht Presentation), damit Budgets, Blitzbegrenzung und Vorlagenzuordnung zentral und testbar sind. Es hängt von Core, Domain (GF_Monsters, GF_World) und dem Feature GF_Combat (Ereignisse) ab – nie umgekehrt. `tools/check_layers.py` prüft das (0 Verstöße).

```cpp
// GF_VFX/Public/Vfx/AethrisVfxTypes.h (Auszug)
namespace Aethris::Vfx
{
    inline constexpr double MinFlashIntervalSec = 1.0 / 3.0;          // VFX-04: ≤ 3 Spitzen/s
    GF_VFX_API bool  AllowFlash(double NowSec, double LastFlashSec);
    GF_VFX_API float FlashIntensity(bool bReduceMotion);              // 1,0 bzw. 0,4 (ACC_MOTION)
    GF_VFX_API int32 ScaleSpawnCount(int32 BaseCount, int32 IntensityPercent,
                                     float BudgetFill01, bool bMandatory);
}
```

```
ScaleSpawnCount(Basis, Dichte%, Füllung, Pflicht):
    f_dichte = clamp(Dichte, 40, 100) / 100
    wenn Füllung ≥ 1,0:     f_budget = Pflicht ? 0,25 : 0
    sonst wenn Füllung > 0,8: f_budget = lerp(1,0 → 0,25) über 0,8…1,0
    sonst:                  f_budget = 1
    n = floor(Basis × f_dichte × f_budget)
    Rückgabe Pflicht ? max(n, 1) : n
```

Pflicht-Effekte sind: Treffer-Impact, Status-Onset, Crescendo-Schlag, Blitzwarnung, Resonanzsinn-Konturen. Sie werden unter Last reduziert, aber nie gestrichen – Lesbarkeit hat Vorrang vor Budget (V-2).

### 9.3 Netzwerk

VFX sind rein lokal. Im Koop (K59/K60) werden nur die Gameplay-Ereignisse repliziert (Fähigkeit X trifft Ziel Y zum Tick T); jeder Client erzeugt die Effekte selbst. Crescendos laufen im PvP immer als Kurzfassung (K30).

---

## 10. Produktion, Benennung, Review

| Asset | Muster | Menge (Ziel) |
|---|---|---|
| Fähigkeits-Vorlagen | `NS_Abl_<Kat>_<Form>` | 15 |
| Typ-Module | `NM_Type_<Typ>` | 15 |
| Form-Module | `NM_Shape_<Form>` | 9 |
| Crescendos | `NS_Cresc_ABL_U###` | 30 (+ 61 Art-Varianten als Overrides) |
| Status | `NS_Status_<Status>` | 15 |
| Terrains | `NS_Terrain_<Typ>` | 15 |
| Wetter | `NS_Weather_*` | 12 |
| Ambiente je Region | `NS_Amb_R##_*` | 10 × 4–6 |
| Story | `NS_Story_*` (`StoryVfx.csv`) | 14 |
| Echo-Effekte | `NS_Echo_*` (Ruf, Emotion, Streicheln, Evolution, Fang, Freilassen) | 12 |

**Aufwand:** Vorlagen und Module ≈ 140 Personentage, Crescendos 30 × 6 = 180 PT, Story-Setpieces 14 × 10 = 140 PT, Welt/Wetter/Ambiente ≈ 160 PT, Optimierung und Plattformprofile ≈ 120 PT – zusammen ≈ 740 PT (≈ 3,4 Personenjahre). Das Team: 1 Lead, 3 VFX Artists, 1 Technical Artist (anteilig) über P2 bis Beta.

**Review-Ablauf:**

```
Brief (Typ-Sprache §3, Fähigkeit/Story) → Blockout-Effekt (graue Formen, Timing auf Animation)
 → Lesbarkeitstest (Graustufen + 3 Farbenblind-Modi + 40 % Dichte) → Look-Pass (Farbe, Licht)
 → Budget-Test (Worst-Case-Szene, Switch-2-Profil) → Blitz-Analyse (Story, Crescendo) → Final
```

---

## 11. Prüfregeln

`tools/ref/aethris_vfx.py validate` prüft die Daten bei jedem Commit:

| Regel | Inhalt |
|---|---|
| VFX-01 | Jede Fähigkeit hat eine Vorlage; jedes Crescendo eine eindeutige Signatur |
| VFX-02 | Jeder Typ und jeder Status hat eine farbunabhängige Form; Formen paarweise verschieden |
| VFX-03 | Worst-Case-Kampfszene im Budget (PS5, Switch 2) |
| VFX-04 | Helligkeitswechsel ≤ 3 Hz (Klangmal-Puls bei Angst, alle Story-VFX) |
| VFX-05 | Jede Typfarbe in allen vier Farbmodi vorhanden |
| VFX-06 | Jedes Terrain und jeder Status hat eine Darstellung |

**Ergebnis:** Prüfregeln VFX-01–VFX-06 über 330 Fähigkeiten, 15 Typen, 15 Status, 15 Terrains, 14 Story-VFX: **0 Verstöße**. Schnellster Klangmal-Puls 104 BPM → bei Angst (+30 %) 2,25 Hz < 3 Hz.

---

## 12. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Kampf-Programmierung | Treffer-Ereignisse in `NDC_CombatHits`; `AN_HitFrame` als einzige Treffer-Zeitquelle; Crescendo-Phasen als Ereignisse | K28, K30 |
| Animation | Sockets `fx_cast`, `fx_mouth`, `fx_root`, `fx_klangmal` an allen Archetyp-Skeletten | K57 |
| Audio | Quartz-Schläge für Klang-Typ und Crescendos an GF_VFX melden; Ton fehlt im Velnox-Bereich | K55 |
| UI | Option `ACC_VFX_INTENSITY` im Barrierefreiheits-Menü; Schallring-Richtungsanzeige (`ACC_VISUAL_SOUND`) | K54 |
| Plattformen | GPU-Anteil VFX 4,0 ms (PS5) / 5,5 ms (Switch 2) im Frame-Budget | K65 |
| QA | Photosensitivitäts-Analyse aller Story-Momente und Crescendos vor Zertifizierung | K66 |
| Katalog | Ruf-Tempo ≤ 138 BPM (VFX-04) im Katalog-Validator | K16 |

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-229 | Fähigkeits-VFX als Vorlagen je Kategorie und Zielform + Typ-Module statt Einzeleffekten | 330 Fähigkeiten mit 28 Bausteinen, einheitliche Lesbarkeit | 330 Einzelsysteme |
| ADR-230 | Jeder Typ und Status hat eine farbunabhängige Form | Farbenblind-Lesbarkeit, Graustufen-Test | Farbe als einziger Träger |
| ADR-231 | Blitzbegrenzer zentral im Code (≤ 3 Spitzen/s), nicht nur als Review-Regel | Garantie für alle Effekte, auch dynamische Kombinationen | reine Art-Review |
| ADR-232 | Neue Option `ACC_VFX_INTENSITY` (100/70/40 %), Formträger und Pflicht-Effekte bleiben | Visuelle Überlastung reduzieren ohne Informationsverlust | nur An/Aus |
| ADR-233 | Eigenes Modul GF_VFX in der Schicht Presentation (CR-007) | Budgets und Blitzbegrenzung testbar, keine VFX-Logik in Features | VFX-Logik verteilt in GF_Combat/GF_UI |
| ADR-234 | Velnox als Negativraum über Custom Depth/Stencil | Einzigartige Figur aus Abwesenheit, günstig | Schwarze Partikelwolke |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §227 | VFX-Säulen V-1–V-5; Phasen Antizipation/Wirkung/Nachhall; Größe = 0,6 + Stärke/150 (max. 1,6); Klang-Typ und Crescendos auf Quartz-Schlag | LOCKED |
| §228 | Typ-VFX-Sprache (`TypeVfx.csv`) mit Form je Typ; Vorlagen `NS_Abl_<Kat>_<Form>` + `NM_Type_<Typ>`; Crescendo-Grundgerüst nach K30 §3 + Signatur je Crescendo + Art-Varianten; Status-Loops (`StatusVfx.csv`, max. 2 sichtbar je Echo); Terrain als Decal + Bodennebel | LOCKED |
| §229 | Welt-VFX: Klangmale als Material, Ambiente je Region in Signaturfarbe, Wetter kameragebunden, Resonanzsinn 40 m/s / 120 m, Story-VFX (`StoryVfx.csv`), Velnox als Negativraum, Abschluss-Effekte auf `DL_Nachhall` | LOCKED |
| §230 | Budgets (`VfxBudgets.csv`), Worst Case Trio im Budget (PS5 300 k / 4,0 ms, Switch 2 90 k / 5,5 ms); Blitzgrenze ≤ 3 Hz im Code; `ACC_VFX_INTENSITY`; Pflicht-Effekte; Modul GF_VFX; VFX nicht repliziert | LOCKED |
| §26 | CR-007: GF_VFX in Schicht Presentation (neben GF_UI, GF_Audio) | LOCKED (ändert §26) |
| §210 | Option `ACC_VFX_INTENSITY` ergänzt | LOCKED (ergänzt §210) |
| §10 | ADR-229 – ADR-234 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] VFX-Säulen, Bildsprache (Phasen, Form/Farbe/Wert, Klang-Synchronität)
- [x] VFX-Sprache aller 15 Typen mit farbunabhängiger Form
- [x] Vorlagensystem für alle 330 Fähigkeiten (berechnet), Crescendo-Inszenierung, Kombos/Akkorde
- [x] Status (15), Terrain (15), Kampfwetter
- [x] Klangmale, Ambiente je Region, Wetter, Traversal, Resonanzsinn, Story-Momente (14)
- [x] Barrierefreiheit: Blitzgrenze, Bewegungsreduktion, Effektdichte (neu), Farbenblind
- [x] Budgets, Worst-Case-Rechnung PS5/Switch 2, Techniken, Switch-2-Profil
- [x] Niagara-Baukasten, Data Channels, Modul GF_VFX mit Blitzbegrenzer und Budget-Skalierung
- [x] Produktion, Aufwand, Review; Prüfregeln VFX-01–VFX-06 (0 Verstöße)
- [x] Anforderungen, ADR-229 – ADR-234, CANON §227–§230, CR-007

➡️ **Nächstes Kapitel: K59 – Multiplayer-Architektur.**
