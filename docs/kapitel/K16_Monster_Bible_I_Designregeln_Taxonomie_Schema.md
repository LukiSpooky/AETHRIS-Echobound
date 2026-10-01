# K16 · Monster Bible I – Kreaturendesign-Regeln, Taxonomie, Datenschema

| Feld | Wert |
|---|---|
| Dokument | Kapitel 16 von 68 · Monster Bible, Teil I |
| Version | 1.0 |
| Owner | Creative Director |
| Mitwirkende | Creature Design Lead, RPG Systems Designer, Technical Artist (Rigging), Animation Lead, Legal (Clean-Room), Narrative |
| Baut auf | CANON §5 (Echos), §22 (Namen), §29 (Datenmodell), §33 (Kosmologie), §45 (Typverteilung), §67 (Aktivitätsmuster), DR-02/05/15/16/22 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Echos/Archetypes.csv`, Schema-Köpfe `Data/Echos/Species.csv` + `SpeciesLore.csv`, `tools/gen_catalog.py` (Validator + Kataloggenerator) |
| Neue Kanon-Einträge | CANON §69 (Designregeln CD), §70 (Taxonomie: Archetypen, Größen, Kategorien), §71 (Seltenheit & Basiswert-Spannen), §72 (Datenschema & Katalogpipeline), §73 (Klangmal), §74 (Starter-Verfügbarkeit) |

---

## Inhalt

1. [Was ein Echo ausmacht](#1-was-ein-echo-ausmacht)
2. [Kreaturendesign-Regeln (CD-01 – CD-20)](#2-kreaturendesign-regeln-cd-01--cd-20)
3. [Das Klangmal](#3-das-klangmal)
4. [Taxonomie](#4-taxonomie)
5. [Seltenheit](#5-seltenheit)
6. [Basiswert-Spannen (Vorgabe für K18/K20–K27)](#6-basiswert-spannen-vorgabe-für-k18k20k27)
7. [Lore-Struktur je Art](#7-lore-struktur-je-art)
8. [Design-Pipeline: Vom Brief zum Echo im Spiel](#8-design-pipeline-vom-brief-zum-echo-im-spiel)
9. [Datenschema](#9-datenschema)
10. [Katalogpipeline & Validierung](#10-katalogpipeline--validierung)
11. [Beispiel: #001 Fernlit vollständig](#11-beispiel-001-fernlit-vollständig)
12. [Decision Records](#12-decision-records)
13. [Kanon-Updates](#13-kanon-updates)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Was ein Echo ausmacht

> Ein Echo ist ein **Oberton des Weltlieds** (CANON §33): ein Lebewesen, dessen Körper, Verhalten und Kräfte von einer Stimme (Region) und einer oder zwei Klangfarben (Typen) geformt sind.

Daraus folgen drei Gestaltungsachsen, die **jedes** Echo-Design beantworten muss:

| Achse | Frage | Beispiel Fernlit |
|---|---|---|
| **Ort** (Stimme) | Welche Landschaft hat es geformt? Was davon trägt es am Körper? | Lindwald → Farnwedel als Ohren und Schwanz, moosiges Fell |
| **Klang** (Typ) | Wie äußert sich seine Klangfarbe sichtbar, hörbar, im Verhalten? | Blüte → Glockenblüten-Knospen am Hals, die bei Freude läuten; Heilung |
| **Leben** (Ökologie) | Was frisst es, wann schläft es, wie lebt es mit anderen? | Dämmerungsaktiv, frisst Tau und Blütennektar, lebt in kleinen Familien |

---

## 2. Kreaturendesign-Regeln (CD-01 – CD-20)

Format wie DR-Regeln (K02): Regel · Prüffrage. Alle **LOCKED**; Ausnahmen nur mit Creative-Director-Freigabe, protokolliert im Design-Review.

### 2.1 Eigenständigkeit (Clean-Room, DR-22)

| ID | Regel | Prüffrage |
|---|---|---|
| CD-01 | **Silhouetten-Abstand:** Jede Silhouette wird gegen die Referenzdatenbank (Legal, ~5.000 Kreaturen anderer Franchises) geprüft; Ähnlichkeit ≥ 0,80 (Formvektor-Metrik, §8.3) → Redesign. | Ist die schwarze Silhouette in 3 Ansichten eindeutig *unsere*? |
| CD-02 | **Kein Tier-plus-Element-Klischee:** Kein Design darf nur „reales Tier + Elementfarbe“ sein. Jedes Echo hat ≥ 2 Gestaltungsachsen (§1) sichtbar am Körper. | Was unterscheidet es von „blauer Fuchs mit Wasser“? |
| CD-03 | **Keine Genre-Signaturen:** Keine Blitz-Schwänze an Nagern, keine Flammen-Schwanzspitzen an Echsen, keine Kugel-Bäuche mit Symbol etc. Liste in der Legal-Datenbank, Prüfung im Review. | Erinnert ein Merkmal an eine bekannte Ikone? |
| CD-04 | **Eigene Farbsprache:** Typfarben aus der Art Bible (K56), Primärpalette eines Echos max. 3 Farben + 1 Akzent (Klangmal). | Passt die Palette zur Typfarbe *unserer* Bibel? |

### 2.2 Lesbarkeit

| ID | Regel | Prüffrage |
|---|---|---|
| CD-05 | **30-Meter-Lesbarkeit:** Art und Typ sind auf 30 m (Oberwelt-Standardkamera) über Silhouette + Farbe + Bewegung erkennbar. | Erkennt ein Tester die Art auf 30 m ohne UI? |
| CD-06 | **Typ-Merkmal:** Jeder Typ hat ein *Leitmerkmal* (z. B. Klang: Resonanzringe/Hohlorgane; Kristall: Facetten; Schwerkraft: schwebende Körperteile; Leere: Negativraum-Öffnungen). Mindestens eines je Typ des Echos ist sichtbar. | Sieht man beide Typen? |
| CD-07 | **Evolutionslinien teilen ein Formmotiv** (analog Namensregel N4), ändern aber Proportion und Haltung deutlich (Stufe 3 ≥ 2× Größe von Stufe 1, außer Sonderfälle). | Erkennt man Verwandtschaft *und* Fortschritt? |
| CD-08 | **Gesicht & Emotion:** Jedes Echo hat einen klaren Ausdrucksträger (Augen, Ohren, Kamm, Leuchtorgan), der die 6 Begleiter-Emotionen (K37) zeigen kann. Bei gesichtslosen Arten: Klangmal und Körperhaltung. | Kann es Freude, Angst, Neugier zeigen? |

### 2.3 Glaubwürdigkeit (S1)

| ID | Regel | Prüffrage |
|---|---|---|
| CD-09 | **Ökologische Plausibilität:** Jede Art hat Nahrung, Schlafplatz, Fortpflanzungsart, Fressfeinde/Beute (Ökologie-Fragment, K52). | Wovon lebt es, wer jagt es? |
| CD-10 | **Bewegung folgt Körperbau:** Archetyp (§4.1) bestimmt Fortbewegung; Ausnahmen (Schweben) nur mit Typ-Begründung (Schwerkraft, Geist, Leere, Sturm). | Kann dieser Körper so laufen/fliegen? |
| CD-11 | **Größe und Gewicht konsistent:** Dichte im Bereich 0,1–4 kg/dm³ (Ausnahmen: Geist, Kristall, Metall, Schwerkraft, Sturm – Begründung im Lore). Validator prüft. | Passt das Gewicht zur Größe? |
| CD-12 | **Lebensraum passt zur Region** (Typverteilung CANON §45, Biom K09/K10). | Würde es in diesem Biom überleben? |

### 2.4 Spiel (S2/S3)

| ID | Regel | Prüffrage |
|---|---|---|
| CD-13 | **Nische (DR-05):** Jede Art erfüllt mindestens eine Nische (`Niche.Combat/Field/Breeding/Research/Mount`). | Warum behält man es auf Lv. 60? |
| CD-14 | **Drei beobachtbare Merkmale (DR-02):** mind. 3 `Behavior.*`-Traits, davon genau 1 Aktivitätsmuster (CANON §67). | Was lernt man in 60 s Beobachtung? |
| CD-15 | **Bindungspersönlichkeit:** Jede Art hat ein Unruhe-Profil und eine Vorliebe (Köder, Klang, Futter) für die Resonanzbindung (K36). | Was mag es, was erschreckt es? |
| CD-16 | **Kampfrolle:** Basiswertverteilung + Typen ergeben eine erkennbare Rolle (Vorderreihe-Tank, Hinterreihe-Fernkampf, Tempo, Unterstützung, Kontrolle, Allrounder). | Wofür setzt man es im Kampf ein? |
| CD-17 | **Reitbarkeit nur mit Körperlogik:** Reitbare Echos (Größe ≥ L, Ausnahme Schwimmen ≥ M) haben einen sichtbaren Sitzbereich. | Wo sitzt der Wärter? |

### 2.5 Ton (PEGI 7, ADR-007)

| ID | Regel | Prüffrage |
|---|---|---|
| CD-18 | **Kein Blut, keine Wunden, keine Knochen offen.** „Schaden“ wird über Klangmal-Flackern, Staub, Lichtsplitter dargestellt. | Ist es für 7-Jährige geeignet? |
| CD-19 | **Unheimlich ja, grausam nein:** Leere-/Geist-/Gift-Echos dürfen gruselig sein (Schatten, Leere, Nebel), nie verstümmelt oder leidend. | Ist es gruselig *schön*? |
| CD-20 | **Niedlich ist keine Pflicht:** Mischung im Kodex: ~40 % niedlich/freundlich, ~35 % majestätisch/cool, ~25 % fremdartig/unheimlich (Messung im Art-Review). | Hat der Kodex Vielfalt? |

---

## 3. Das Klangmal

**Jedes Echo trägt ein Klangmal** (LOCKED): eine leuchtende Körpermarkierung (Muster aus Linien, Ringen oder Punkten), die die **Grundfrequenz** des Echos sichtbar macht. Das Klangmal ist das wichtigste Alleinstellungsmerkmal der Echo-Gestaltung und verbindet Design mit Mechanik:

| Verwendung | Wirkung |
|---|---|
| **Resonanzbindung** (K36) | Das Klangmal pulsiert im Rhythmus der Frequenzwelle; der perfekte Anschlag fällt mit dem hellsten Puls zusammen → visuelles Timing-Signal (DR-24: visueller Kanal des Klangs) |
| **Emotion** (K37) | Farbe/Pulsrate zeigen Stimmung (ruhig = langsamer, gleichmäßiger Puls) |
| **Kampf** | Treffer lassen das Klangmal flackern (statt Blut, CD-18); Erschöpfung = Klangmal erlischt langsam |
| **Genetik** (K38) | Klangmal-Muster und -Farbe sind erblich (Locus `GEN_SOUNDMARK_PATTERN`, `GEN_SOUNDMARK_COLOR`) → sichtbare Individualität |
| **Stillezone** | Verstummte Echos: Klangmal erloschen und grau |
| **Kodex/Fotografie** | Klangmal im Bild = Bewertungsbonus „Resonanzmoment“ (K39) |

**Technik:** Klangmal als Emissive-Maske (`T_Echo_###_SoundMark`, R = Muster, G = Pulsphase-Offset, B = Intensität) + Materialparameter `SoundMarkPulse`, gespeist von der Frequenzsimulation des Echos (Rate in BPM, abhängig von Art und Stimmung).

---

## 4. Taxonomie

### 4.1 Archetypen (Körperbaupläne) – Grundlage der Rig- und Animationspipeline

Daten: `Data/Echos/Archetypes.csv`. Jeder Archetyp hat ein Basis-Skelett (`SKEL_Archetype_*`), ein Basis-Animation-Blueprint und einen Basis-Animationssatz für die 9 Pflichtzustände (CANON §5). Arten werden auf den Archetyp gerigt und per Retargeting animiert; nur Signaturbewegungen werden individuell animiert (Risiko R-03).

| ID | Archetyp | Skelett | Fortbewegung | Größen | Reitbar möglich | Typische Typen |
|---|---|---|---|---|---|---|
| A01 | Vierbeiner leicht | `SKEL_Arch_QuadLight` | laufen, springen, klettern (leicht) | XS–M | – | Blüte, Sturm, Licht |
| A02 | Vierbeiner schwer | `SKEL_Arch_QuadHeavy` | laufen, stampfen | M–XL | Boden | Stein, Glut, Metall |
| A03 | Huftier | `SKEL_Arch_Ungulate` | laufen, galoppieren | M–XL | Boden | Blüte, Frost, Licht |
| A04 | Zweibeiner | `SKEL_Arch_Biped` | gehen, laufen, greifen | S–L | – | Metall, Kristall, Arkan |
| A05 | Vogel | `SKEL_Arch_Avian` | fliegen, hüpfen | XS–L | Flug (≥ L) | Sturm, Licht, Klang |
| A06 | Gleitschwimmer (Rochen/Wal) | `SKEL_Arch_Glider` | gleiten in Luft/Wasser | M–XXL | Flug/Schwimmen | Flut, Sturm, Schwerkraft |
| A07 | Schlange/Wurm | `SKEL_Arch_Serpent` | schlängeln, graben | S–XXL | Graben (≥ L) | Gift, Stein, Leere |
| A08 | Fisch | `SKEL_Arch_Fish` | schwimmen, springen | XS–L | Schwimmen (≥ M) | Flut, Kristall |
| A09 | Amphib | `SKEL_Arch_Amphib` | hüpfen, schwimmen | XS–M | – | Flut, Gift, Klang |
| A10 | Gliederfüßer (6/8 Beine) | `SKEL_Arch_Arthropod` | krabbeln, klettern an Wänden | XS–L | Klettern (≥ L) | Gift, Metall, Kristall |
| A11 | Panzerträger | `SKEL_Arch_Shell` | langsam laufen, einigeln | S–XXL | Boden | Stein, Flut, Metall |
| A12 | Schwebend amorph | `SKEL_Arch_Floater` | schweben | XS–L | – | Geist, Leere, Arkan |
| A13 | Konstrukt/Elementar | `SKEL_Arch_Construct` | gehen, schweben (Teile) | S–XL | – | Stein, Kristall, Metall, Glut |
| A14 | Pflanzenwesen | `SKEL_Arch_Plant` | wurzeln, langsam gehen | XS–L | – | Blüte, Gift |
| A15 | Drache | `SKEL_Arch_Dragon` | laufen + fliegen | L–XXL | Flug | Glut, Kristall, Sturm (oft Endstufen/Legendäre) |
| A16 | Schwarm (mehrere Körper) | `SKEL_Arch_Swarm` (Niagara + Mini-Rigs) | schwärmen | XS (Einzelne) / M (Schwarm) | – | Sturm, Gift, Licht, Leere |
| A17 | Kopffüßer/Tentakel | `SKEL_Arch_Tentacle` | kriechen, schwimmen | S–XL | Schwimmen (≥ L) | Flut, Arkan, Geist |
| A18 | Kletterer/Primat | `SKEL_Arch_Climber` | klettern, schwingen | S–L | Klettern (L) | Blüte, Klang, Stein |

**Regel:** Jede Art gehört zu genau einem Archetyp. Ziel-Verteilung: kein Archetyp > 12 % der 256 Arten (Vielfalt), keiner < 2 % (Rig-Kosten amortisieren).

### 4.2 Größenklassen

| Klasse | Höhe/Länge | Beispiel | Kampfdarstellung | Begleiter |
|---|---|---|---|---|
| XS | < 0,3 m | Insekt, Maus | skaliert auf min. 0,5 m Kampfdarstellung | Schulter/Tasche |
| S | 0,3–0,8 m | Kitz, Fuchs | 1:1 | folgt |
| M | 0,8–1,6 m | Wolf, Reh | 1:1 | folgt |
| L | 1,6–3,0 m | Pferd, Bär | 1:1 | folgt (Reittier möglich) |
| XL | 3–8 m | Elefant, Riesenschlange | Kampfkreis +4 m | folgt nicht (Hain/Reittier) |
| XXL | > 8 m | Ursprungsstimmen, Leviathane | Sonderarena/Kampfkreis +8 m | nie Begleiter (Ausnahme Post-Game-Flugreittier) |

### 4.3 Kategorie (Briefing-Feld)

Die **Kategorie** ist ein kurzer, lokalisierter Beiname der Art im Kodex, gebildet als „*‹Bild›-Echo*“ (z. B. „Farnkitz-Echo“, „Glockenhirsch-Echo“). Regeln: 1–2 Wörter + „-Echo“, kein Realtiername allein (CD-02), keine Namen aus anderen Franchises.

### 4.4 Wissenschaftliche Ordnung (Aethrisch-Latein, K04 §5)

```
 Reich        Resonantia (alle Echos)
 Stamm        nach Archetyp-Gruppe:   Quadrupedia (A01–A03), Bipedia (A04, A18), Volantia (A05, A06, A15),
                                        Serpentia (A07), Aquatica (A08, A09, A17), Articulata (A10),
                                        Testudinia (A11), Spectralia (A12, A16), Elementia (A13), Botanica (A14)
 Familie      nach Primärtyp:         -idae-Endung an Typwurzel (z. B. Bloomidae → „Floridae“, Soundidae → „Sonidae“)
 Gattung      Linie (gemeinsam für alle Stufen einer Evolutionslinie)
 Art          Stufe/Form
```

**Familiennamen je Typ (LOCKED):** Ignidae (Glut), Undidae (Flut), Lithidae (Stein), Procellidae (Sturm), Floridae (Blüte), Glacidae (Frost), Vacuidae (Leere), Lucidae (Licht), Venenidae (Gift), Ferridae (Metall), Animidae (Geist), Crystallidae (Kristall), Sonidae (Klang), Gravidae (Schwerkraft), Arcanidae (Arkan).

---

## 5. Seltenheit

| Stufe | `EEchoRarity` | Basis-Spawngewicht (‰) | Bedingungen | Anteil am Kodex (Ziel) |
|---|---|---|---|---|
| Häufig | Common | 1000 | optional | 40 % |
| Ungewöhnlich | Uncommon | 400 | optional | 28 % |
| Selten | Rare | 120 | **Pflicht** (DR-15): ≥ 1 Bedingung (Wetter, Tageszeit, Mond, Zone, Verhalten) | 18 % |
| Sehr selten | VeryRare | 30 | **Pflicht**: ≥ 2 kombinierte Bedingungen | 8 % |
| Legendär | Legendary | gescriptet | Story/Quest (CANON §34) | 10 Arten |
| Mythisch | Mythical | gescriptet | Endgame (CANON §34) | 6 Arten |

Die Seltenheit gilt für das **Wildvorkommen** der Art. Evolutionsstufen, die wild selten vorkommen, aber durch Entwicklung erreichbar sind, tragen ihre Wildseltenheit (z. B. Stufe 3: oft VeryRare oder „nicht wild“ = `Rare` mit Bedingung `Spawn.None`). `Spawn.None` ist als Bedingung zulässig (Art nur durch Evolution/Zucht) und erfüllt DR-15.

---

## 6. Basiswert-Spannen (Vorgabe für K18/K20–K27)

Summe der sechs Kernwerte (**Kernsumme**, `FEchoStats::CoreTotal`). Präzision und Ausweichen sind **Sekundärwerte** mit Basis 80–120 (100 = neutral) und zählen nicht zur Kernsumme. Formeln: K18.

| Klasse | Kernsumme | Einzelwert-Spanne | Anmerkung |
|---|---|---|---|
| Stufe 1 einer 3er-Linie | 280–340 | 25–80 | Starter 300–315 |
| Stufe 2 einer 3er-Linie | 400–460 | 40–110 | |
| Stufe 3 einer 3er-Linie | 500–560 | 50–140 | Starter-Endstufen 530 |
| Stufe 1 einer 2er-Linie | 320–380 | 30–90 | |
| Stufe 2 einer 2er-Linie | 470–530 | 45–130 | |
| Ohne Evolution | 430–520 | 40–130 | Nischen-Spezialisten oben, Häufige unten |
| Spezialformen (Zweige) | wie Stufe, aus der sie hervorgehen | | |
| Ursprungsstimmen | 640–680 | 70–160 | |
| Mythische | 600–660 | 60–160 | |
| Sekundärwerte PRÄ/AUS | je 80–120 | | Summe PRÄ+AUS 190–210 |

Validator prüft alle Spannen (§10).

---

## 7. Lore-Struktur je Art

Das Briefing verlangt pro Kreatur **Herkunft, Verhalten, Mythologie, Beziehung zu Menschen**. Jede Art erhält diese vier Lore-Felder (je 1–3 Sätze, ≤ 320 Zeichen) plus drei Kodex-Texte, die mit Forschungsstufen freigeschaltet werden (K39).

| Feld | Inhalt | Kodex-Stufe |
|---|---|---|
| `LoreOrigin` | Welcher Oberton, welche Landschaft; Entstehungsgeschichte | 2 |
| `LoreBehavior` | Leben, Ernährung, Sozialverhalten, Besonderheiten | 1 |
| `LoreMyth` | Volksglaube, Sagen, Lauscherglauben-Bezug | 3 |
| `LoreHumans` | Nutzung, Zusammenleben, Konflikte | 3 |
| `KodexL4` | Akademie-Notiz mit mechanischem Hinweis (z. B. Evolutionsbedingung) | 4 |

Texte liegen in `Data/Echos/SpeciesLore.csv` (Quelle für String Tables `ST_Echos`, K04 §11) – getrennt von Spieldaten, damit Lokalisierung und Daten unabhängig versionierbar sind.

---

## 8. Design-Pipeline: Vom Brief zum Echo im Spiel

### 8.1 Ablauf

```
 1 BRIEF (Systems + Creative)          Typen, Region, Rolle, Nische, Linie, Stufe, Größenklasse, Archetyp
        │
 2 THUMBNAILS (Konzept, 20–40 Stück)   Silhouetten in Schwarz, 3 Ansichten
        │
 3 SILHOUETTEN-CHECK (Legal, CD-01)  ──► fail → zurück zu 2
        │
 4 FARBSKIZZEN (3–5)                   Palette, Klangmal-Muster, Typ-Leitmerkmale (CD-06)
        │
 5 DESIGN-REVIEW (Creative Director, Art Director, Systems, Legal)  CD-01–CD-20 Checkliste
        │
 6 TURNAROUND + EXPRESSION SHEET       6 Emotionen, Größenvergleich zum Wärter
        │
 7 NAME (NameGuard, K04 §6) + Daten-CSV-Zeile + Lore-Zeile
        │
 8 3D: Sculpt (ZBrush) → Retopo/UV (Blender) → Texturen (Substance) → Rig auf Archetyp (K57)
        │
 9 ANIMATION: Retarget Basissatz + Signaturbewegungen (Spezialangriff, Idle-Variante)
        │
10 IN-ENGINE-REVIEW (30-m-Lesbarkeit CD-05, Kampf, Begleiter, Fotomodus)
        │
11 FREIGABE → Status „Ship“ im Kreaturen-Tracker
```

### 8.2 Durchsatz & Aufwand (Planung, Detail K57/K67)

| Phase | Aufwand je Art (Ø) | 256 Arten |
|---|---|---|
| Konzept bis Freigabe (1–7) | 1,5 Personenwochen | 384 PW |
| 3D + Texturen | 3 PW (Endstufen/Legendäre 5 PW) | ~830 PW |
| Rig auf Archetyp | 0,5 PW | 128 PW |
| Animation (Retarget + Signatur) | 2 PW | 512 PW |
| Audio-Rufe (K55) | 0,3 PW | 77 PW |
| **Summe** | | **~1.930 PW (~44 Personenjahre)** – mit Outsourcing für 3D/LODs |

### 8.3 Silhouetten-Metrik (CD-01)

Für jede Ansicht (vorne, Seite, ¾) wird die Silhouette in ein 128×128-Binärbild gerendert; daraus ein Formvektor (Hu-Momente + Fourier-Konturdeskriptor, 64 Werte). Ähnlichkeit = Kosinus über den gemittelten Vektor. Schwelle 0,80 auf der Referenzdatenbank. Werkzeug: `Tools/SilhouetteCheck` (Python, Blender-Export der Silhouetten). Grenzfälle (0,70–0,80) gehen an Legal zur manuellen Prüfung.

---

## 9. Datenschema

### 9.1 `Data/Echos/Species.csv` (Spieldaten, Quelle der `UEchoSpeciesDefinition`)

| Spalte | Typ | Pflicht | Beschreibung | Validierung |
|---|---|---|---|---|
| `Name` (Id) | `ECHO_###` | ✔ | Stabile ID | K04 §7 |
| `KodexNumber` | int | ✔ | 1–256 | = Zahl in Id; lückenlos |
| `DisplayName` | Text | ✔ | Echo-Name | N1–N8 (NameGuard) |
| `ScientificName` | Text | ✔ | *Genus epitheton* | Gattung je Linie gleich |
| `Category` | Text | ✔ | „‹Bild›-Echo“ | endet auf „-Echo“ |
| `Line` | `L###` | ✔ | Evolutionslinie | Linienstruktur §10 |
| `Stage` | 1–3 | ✔ | Stufe in der Linie (Zweigformen: Stufe der Abzweigung + 1) | |
| `LineKind` | `Three`/`Two`/`Single`/`Branch`/`Legendary`/`Mythical` | ✔ | Linientyp | Zählung 40/45/22/8/10/6 |
| `Archetype` | `A##` | ✔ | Körperbau | Archetypes.csv |
| `SizeClass` | XS…XXL | ✔ | Größenklasse | Höhe passt zur Klasse |
| `HeightM` | dezimal | ✔ | Höhe/Länge | |
| `WeightKg` | dezimal | ✔ | Gewicht | Dichte (CD-11) |
| `PrimaryType` | `Type.*` | ✔ | Primärtyp | Typverteilung CANON §45 |
| `SecondaryType` | `Type.*` / leer | – | Sekundärtyp | ≠ Primärtyp |
| `Region` | `R##` | ✔ | Erstvorkommen | Kodex-Bereich CANON §20 |
| `Habitat` | Text | ✔ | Lebensraum (kurz) | |
| `Zones` | `R##_Z##`-Liste | – | Spawnzonen (leer = nur Evolution/Zucht) | Zones.csv |
| `Rarity` | `EEchoRarity` | ✔ | Wildseltenheit | §5 |
| `SpawnConditions` | Tag-Liste | ab Rare | `Weather.*`, `TimeOfDay.*`, `Moon.*`, `Spawn.None`, `Story.*` | DR-15 |
| `Activity` | `Behavior.Activity.*` | ✔ | Aktivitätsmuster | CANON §67 |
| `Traits` | `Behavior.*`-Liste | ✔ | weitere Verhaltensmerkmale (≥ 2) | DR-02 (mit Activity ≥ 3) |
| `Niches` | `Niche.*`-Liste | ✔ | ≥ 1 | DR-05 |
| `Role` | Tank/Striker/Caster/Speed/Support/Control/AllRound | ✔ | Kampfrolle | CD-16 |
| `Mount` | `Mount.*` / leer | – | Reitart | CD-17 |
| `GrowthRate` | Kurven-Id | ✔ | EP-Kurve (K18) | |
| `HP,Attack,Defense,SpAttack,SpDefense,Speed` | int | ✔ | Basiswerte | §6 |
| `Precision,Evasion` | int | ✔ | Sekundärwerte 80–120 | §6 |
| `EvolvesTo` | `ECHO_###`-Liste | – | Folgestufen | Linienkonsistenz |
| `EvoCondition` | Ausdruck (K19) | wenn EvolvesTo | Bedingung | Parser K19 |
| `BondRate` | 1–255 | ✔ | Bindungsgrundrate (K36) | |
| `BondLure` | Item/Tag | ✔ | Vorliebe (CD-15) | |
| `SignatureConcept` | Text | ✔ | Konzept der Signaturfähigkeit (IDs in K28–K30 nachgetragen) | |
| `SoundMark` | Text | ✔ | Klangmal-Beschreibung (§3) | |

### 9.2 `Data/Echos/SpeciesLore.csv` (Textquelle)

`Name,LoreOrigin,LoreBehavior,LoreMyth,LoreHumans,KodexL4`

### 9.3 Laufzeitklasse – Ergänzungen zu `UEchoSpeciesDefinition`

```cpp
// AethrisCore/Public/Data/EchoSpeciesDefinition.h – Ergänzungen K16 (zusätzlich zu den Feldern aus K06)
UENUM(BlueprintType)
enum class EEchoLineKind : uint8 { Three, Two, Single, Branch, Legendary, Mythical };

UENUM(BlueprintType)
enum class EEchoSizeClass : uint8 { XS, S, M, L, XL, XXL };

UENUM(BlueprintType)
enum class EEchoCombatRole : uint8 { Tank, Striker, Caster, Speed, Support, Control, AllRound };

// in UEchoSpeciesDefinition:
	UPROPERTY(EditDefaultsOnly, Category="Taxonomy") FText Category;            // „Farnkitz-Echo“
	UPROPERTY(EditDefaultsOnly, Category="Taxonomy") FName LineId;              // L###
	UPROPERTY(EditDefaultsOnly, Category="Taxonomy", meta=(ClampMin=1, ClampMax=3)) int32 Stage = 1;
	UPROPERTY(EditDefaultsOnly, Category="Taxonomy") EEchoLineKind LineKind = EEchoLineKind::Three;
	UPROPERTY(EditDefaultsOnly, Category="Taxonomy") FName Archetype;           // A##
	UPROPERTY(EditDefaultsOnly, Category="Body") EEchoSizeClass SizeClass = EEchoSizeClass::S;
	UPROPERTY(EditDefaultsOnly, Category="Body") float HeightM = 0.5f;          // Präsentation, keine Kampflogik
	UPROPERTY(EditDefaultsOnly, Category="Body") float WeightKg = 5.f;
	UPROPERTY(EditDefaultsOnly, Category="Ecology", meta=(Categories="Behavior.Activity")) FGameplayTag Activity;
	UPROPERTY(EditDefaultsOnly, Category="Combat") EEchoCombatRole Role = EEchoCombatRole::AllRound;
	UPROPERTY(EditDefaultsOnly, Category="Combat", meta=(Categories="Mount")) FGameplayTag Mount;
```

---

## 10. Katalogpipeline & Validierung

`tools/gen_catalog.py` liest `Species.csv` + `SpeciesLore.csv` und

1. **validiert** (Exitcode ≠ 0 bei Fehlern):
   - IDs, Kodexnummern lückenlos bis zum aktuellen Stand; Kodex-Bereich je Region (CANON §20)
   - Typverteilung der Erstvorkommen je Region **exakt** gegen `RegionTypeDistribution.csv` (geprüft, sobald eine Region vollständig ist)
   - Basiswert-Spannen §6, Sekundärwerte, Größenklasse/Höhe, Dichte (CD-11)
   - DR-02 (≥ 3 Verhaltensmerkmale inkl. Aktivität), DR-05 (Nische), DR-15 (Bedingungen ab Rare)
   - Linienkonsistenz: Stufen 1…n, `EvolvesTo` zeigt auf existierende Stufe+1 derselben Linie, Gattung gleich
   - Linienstruktur am Ende (#240): 40 × Three, 45 × Two, 22 × Single, 8 × Branch (CANON §20)
   - Namensregeln über `tools/nameguard` (N1–N8, N6 linienübergreifend)
   - Archetyp-Anteile (≤ 12 %, am Ende ≥ 2 %)
2. **erzeugt** den Markdown-Katalog für ein Kodex-Intervall (`--range 1-32 --out docs/kapitel/K20_…md`), einheitlich formatiert.

Die Katalogkapitel K20–K27 sind damit **aus Daten generiert** – Kapiteltext und Spieldaten können nicht auseinanderlaufen (ADR-075).

---

## 11. Beispiel: #001 Fernlit vollständig

Dieses Beispiel ist **kanonisch** (Eintrag #001 in K20 wird daraus generiert).

| Feld | Wert |
|---|---|
| Id / Kodex | `ECHO_001` / #001 |
| Name | **Fernlit** |
| Wissenschaftlich | *Pteridolis cantans* Vael, 812 n.St. |
| Kategorie | Farnkitz-Echo |
| Linie / Stufe | L001 · Stufe 1 von 3 (Starterlinie Blüte) |
| Archetyp | A01 Vierbeiner leicht |
| Größe / Gewicht | S · 0,45 m · 6,2 kg |
| Typen | **Blüte** |
| Region / Lebensraum | R01 Verdanthain · Farnunterholz an Waldrändern und Bachläufen |
| Seltenheit (wild) | VeryRare (Starter; wild erst nach Akt I im Uralthain bei **Regen + Morgendämmerung**) |
| Aktivität | Dämmerungsaktiv |
| Merkmale | `Behavior.Shy` (scheu), `Behavior.Singer` (läutet Halsknospen), `Behavior.FamilyGroup` (Familienverband 2–4) |
| Nischen | Kampf, Feld (Feldfähigkeit: Pflanzen zum Wachsen bringen – Ranken-Brücken) |
| Rolle | Support (Heilung, Kontrolle) |
| Basiswerte | HP 48 · ANG 42 · VER 50 · SAN 55 · SVE 58 · GES 47 = **300** · PRÄ 100 · AUS 105 |
| Wachstumsrate | „Stetig“ (K18) |
| Entwicklung | → Fernwyn (#002) ab Level 16 |
| Bindung | Rate 45 · Vorliebe: Lindblüten-Honig; erschrickt bei lauten Schritten |
| Signaturkonzept | „Glockenblüte“: heilt Verbündeten in der Reihe und läutet (Harmonie +) |
| Klangmal | Spiralmuster aus Lindgold auf Stirn und Flanken; pulsiert wie ein langsamer Herzschlag (52 BPM in Ruhe) |
| **Herkunft** | Ein Oberton Sylv'anors, entstanden dort, wo Farn und Glockenblume im Morgenwind gemeinsam schwingen. |
| **Verhalten** | Lebt in kleinen Familien im Farnunterholz; trinkt Tau und Nektar, läutet bei Freude leise mit den Halsknospen und erstarrt bei Gefahr zwischen den Wedeln. |
| **Mythologie** | Im Lauscherglauben läutet ein Fernlit über jeder Wiege, deren Kind einmal Wärter wird. |
| **Beziehung zu Menschen** | Gilt in Verdanthain als Glücksbringer; Imker sehen es gern, weil es Blüten bestäubt. Wird nie gejagt – es zu erschrecken, bringt nach altem Glauben ein Jahr Stille. |
| Kodex L4 | „Die Halsknospen öffnen sich vollständig, wenn das Echo dem Wärter tief vertraut – manche Gelehrte vermuten darin den Beginn eines Tonartwechsels.“ |

---

## 12. Decision Records

### ADR-074 – 18 Archetypen als Rig-Grundlage
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) Individuelles Rig je Art | maximale Freiheit | 256 Rigs, Animationskosten explodieren (R-03) |
| (b) 18 Archetypen + Retargeting + Signaturanimationen | Wiederverwendung (~70 % der Animationen), konsistente Bewegungsqualität | Formen müssen in Archetypen passen → Proportions-Spielraum über Skalierungs-Bones und Zusatz-Bones (Flügel, Schwanz, Tentakel) |
- **Entscheidung:** (b).

### ADR-075 – Kreaturenkatalog aus Daten generiert
- **Entscheidung:** K20–K27 werden aus `Species.csv` + `SpeciesLore.csv` erzeugt und validiert. Vorteil: Konsistenz Daten ↔ Doku, maschinelle Prüfung aller Kanon-Vorgaben. Nachteil: Prosa im Katalog ist strukturierter, weniger frei → Lore-Felder geben Raum.

### ADR-076 – Klangmal als universelles Gestaltungselement
- **Entscheidung:** Jedes Echo trägt ein Klangmal (§3). Vorteil: Wiedererkennbare Markenidentität („Echos leuchten im Takt“), verbindet Fang-Timing, Emotion, Genetik, Kampf-Feedback ohne Blut. Nachteil: Material- und Designaufwand pro Art → Maskenvorlagen pro Archetyp.

### ADR-077 – Andere Starter solo erhältlich (DR-19)
- **Entscheidung:** Die zwei nicht gewählten Starterlinien erscheinen nach Abschluss von Akt I als **sehr seltene** Wildvorkommen im Uralthain (R01_Z06) unter festen Bedingungen: Fernlit Regen + Morgendämmerung; Brokk Klar + Mittag an Felsen; Wisplet Gewitter. Zusätzlich über Zucht. Vorteil: 100 % Kodex offline; Wert der Starterwahl bleibt (früher Zugriff).

### ADR-078 – Präzision/Ausweichen als Sekundärwerte außerhalb der Kernsumme
- **Entscheidung:** Kernsumme zählt nur 6 Werte; PRÄ/AUS liegen eng um 100. Vorteil: Genre-vertraute Balancing-Kennzahl, DR-07 (Zufall gedeckelt). Nachteil: Briefing-Werte PRÄ/AUS wirken „kleiner“ → sie werden durch Stufen, Fähigkeiten und Wetter relevant (K18/K32).

---

## 13. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §69 | Designregeln CD-01–CD-20 (Silhouette ≥ 0,80 → Redesign, Palette ≤ 3 + Akzent, 30-m-Lesbarkeit, Typ-Leitmerkmal, Linien-Formmotiv, Emotionsträger, Dichte 0,1–4 kg/dm³, Ton PEGI 7, Mix 40/35/25) | LOCKED |
| §70 | 18 Archetypen A01–A18 (`Archetypes.csv`), Anteil 2–12 % je Archetyp | LOCKED |
| §70 | Größenklassen XS < 0,3 · S 0,3–0,8 · M 0,8–1,6 · L 1,6–3 · XL 3–8 · XXL > 8 m; Begleiter bis L; Reiten ab L (Schwimmen ab M) | LOCKED |
| §70 | Kategorie = „‹Bild›-Echo“; Taxonomie Reich *Resonantia*, Stämme je Archetypgruppe, Familien je Typ (Ignidae, Undidae, Lithidae, Procellidae, Floridae, Glacidae, Vacuidae, Lucidae, Venenidae, Ferridae, Animidae, Crystallidae, Sonidae, Gravidae, Arcanidae), Gattung je Linie | LOCKED |
| §71 | Seltenheit: Spawngewichte 1000/400/120/30 ‰, Bedingungen ab Rare (≥ 1) bzw. VeryRare (≥ 2), `Spawn.None` zulässig; Zielanteile 40/28/18/8 % | LOCKED |
| §71 | Kernsummen-Spannen §6; PRÄ/AUS 80–120 (Summe 190–210) außerhalb der Kernsumme | LOCKED |
| §72 | Schema `Species.csv` + `SpeciesLore.csv` (§9), Enums `EEchoLineKind`, `EEchoSizeClass`, `EEchoCombatRole`; Katalog generiert durch `tools/gen_catalog.py` mit Validierung (§10) | LOCKED |
| §72 | Lore-Felder Herkunft/Verhalten/Mythologie/Menschen + Kodex L4 (≤ 320 Zeichen je Feld) | LOCKED |
| §73 | **Klangmal**: leuchtende Grundfrequenz-Markierung jedes Echos; Timing-Signal der Bindung, Emotion, Treffer-Feedback, erblich (`GEN_SOUNDMARK_PATTERN/COLOR`), erloschen bei Verstummung | LOCKED |
| §74 | Starter #001 Fernlit vollständig (§11); nicht gewählte Starter wild im Uralthain nach Akt I (VeryRare) + Zucht | LOCKED |
| §10 | ADR-074 – ADR-078 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Gestaltungsachsen Ort/Klang/Leben
- [x] 20 Kreaturendesign-Regeln mit Prüffragen (Clean-Room, Lesbarkeit, Glaubwürdigkeit, Spiel, Ton)
- [x] Klangmal als Kern-Designelement mit Mechanik-Anbindung
- [x] Taxonomie: 18 Archetypen, 6 Größenklassen, Kategorie, wissenschaftliche Ordnung inkl. Familien je Typ
- [x] Seltenheitsstufen mit Spawngewichten und Bedingungspflichten
- [x] Basiswert-Spannen je Linienstufe
- [x] Lore-Struktur gemäß Briefing (Herkunft, Verhalten, Mythologie, Menschen)
- [x] Design-Pipeline inkl. Silhouetten-Metrik und Aufwandsschätzung (~1.930 PW)
- [x] Vollständiges Datenschema + Laufzeit-Ergänzungen
- [x] Katalogpipeline mit automatischer Validierung (Tool im Repo)
- [x] Vollständiges Beispiel #001 Fernlit
- [x] ADR-074 – ADR-078, CANON aktualisiert

➡️ **Nächstes Kapitel: K17 – Typensystem & Effektivitätstabelle.**
