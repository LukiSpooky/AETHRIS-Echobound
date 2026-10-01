# K12 · Städte II – Schlackenwehr, Hvitmark, Dorunsruh, Prismara, Aerion

| Feld | Wert |
|---|---|
| Dokument | Kapitel 12 von 68 · World Bible, Teil VI |
| Version | 1.0 |
| Owner | Level Designer (City Lead) |
| Mitwirkende | Narrative Writer, Quest Designer, Audio Director, AI Engineer, Economy Designer, Combat Designer |
| Baut auf | K11 (Stadt-Template, Arena-System, Bevölkerungsmodell), K07, K08, K10 |
| Status | ✅ Freigegeben |
| Im Repository ergänzt | `Data/Economy/Merchants.csv` (+26 Händler → 54 gesamt) |
| Neue Kanon-Einträge | CANON §54 (Städte II), §55 (Sonderort Kloster Schweigfels), §56 (Städte-Gesamtübersicht) |

---

## Inhalt

1. [Schlackenwehr (R05)](#1-schlackenwehr-r05)
2. [Hvitmark (R07)](#2-hvitmark-r07)
3. [Dorunsruh (R08)](#3-dorunsruh-r08)
4. [Prismara (R09)](#4-prismara-r09)
5. [Aerion (R10)](#5-aerion-r10)
6. [Sonderort: Kloster Schweigfels](#6-sonderort-kloster-schweigfels)
7. [Gesamtübersicht aller 10 Städte](#7-gesamtübersicht-aller-10-städte)
8. [Musik-Leitmotivsystem der Städte](#8-musik-leitmotivsystem-der-städte)
9. [Code](#9-code)
10. [Decision Records](#10-decision-records)
11. [Kanon-Updates](#11-kanon-updates)
12. [Kapitel-Checkliste](#12-kapitel-checkliste)

---

## 1. Schlackenwehr (R05)

### 1.1 Steckbrief

| Feld | Wert |
|---|---|
| Lage | R05 Ignareth, 6,7 / 3,5 km – Festungsstadt hinter der **Lavawehr** (Umlenkmauer) |
| Einwohner | 5.500 · Benannte NPCs 40 · Mass 170 · sichtbar 110 / 55 |
| Regierung | **Zunftrat der Schmiede**; Vorsitz = Arenameister (Tradition) |
| Fraktionen | Kontor (Erzhandel), Freie-Stimmen-Zelle (Minen), Wildwacht-Lavawächter |
| Arena | ARN_05, **Kaldrex Vorn** (Glut/Metall), Akt-II-Stufe 5–8 |
| Ursprungsstimme | Pyr'thagon – Kraterherz unter der Stadt |
| Fantasie | *„Hier ist jeder Hammerschlag ein Gebet und jede Mauer ein Versprechen an den Berg.“* |

### 1.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ 300 n.St. | Erste Schmiedelager an den Lavaströmen |
| 591 n.St. | Bau der **Lavawehr** – die Stadt lenkt den Ignar-Strom um sich herum |
| 702–709 n.St. | Rüstungsschmiede der Siegelkriege; danach Gelübde der Zunft: „Wir schmieden Werkzeug, keine Waffen“ (Gründungsmythos des Waffenverbots, CANON §36) |
| 880 n.St. | Arena in der **Großen Esse** |
| 1004 n.St. | Stillezone um das Kraterherz – die Esse kühlt ab, die Zünfte bangen um ihre Existenz |

### 1.3 Architektur & Layout

Stil: **Ignar-Basaltbau** – schwarze Basaltquader, Bronzebeschläge, Kühlkanäle mit Dampf, Glutfenster; Gebäude terrassiert am Hang; Dachgärten aus feuerfesten Pflanzen.

```
            IGNAR-KRATER (oben, Kraterherz darunter)
                 ║  Lavastrom
   ══════ LAVAWEHR (Umlenkmauer, begehbar) ══════════════
   │ OBERE TERRASSE: Zunfthalle · GROSSE ESSE (ARENA)    │
   │─────────────────────────────────────────────────────│
   │ MITTLERE TERRASSE: Wehrmarkt · Erzwaage · Klangbrunnen│
   │─────────────────────────────────────────────────────│
   │ UNTERE TERRASSE: Thermen Seraphe · Wohnviertel       │
   │              · Kühlkanal-Gassen (Dampf)              │
   └──────── Tor zur Straße nach Morvenfurt / Dorunsruh ─┘
```

**Wahrzeichen:** Große Esse (Arena um ein offenes Lavabecken), Lavawehr (Mauerweg mit Blick auf den Strom), sechs Schmiedeglocken.
**Traversal:** Mauerweg, Dampfaufzüge, Kettenkrane; Kühlkanäle zum Schwimmen (warm, sicher).

### 1.4 Dienste & Händler

Alle Stadtdienste (K03 §3); Schmiede-Station mit **Meisterschmiede** (Ausrüstung IV, Crafting K41).

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_SCHL_01 | Wehrmarkt Ithren | Allgemein | 6–20 | Hitzeschutz-Salben |
| MER_SCHL_02 | Zunfthalle der Schmiede | Ausrüstung | 0–24 | Ausrüstung III–IV, Schmiedeprüfungen |
| MER_SCHL_03 | Thermen Seraphe | Nahrung/Dienst | 8–24 | Thermalbad setzt Asche-Belastung zurück |
| MER_SCHL_04 | Erzwaage Volk | Material | 6–18 | Schlackenstahl, Obsidian |
| MER_SCHL_05 | Glutnarben-Tutorin Asha | Tutor | 10–18 | Glut/Metall |

### 1.5 Arena: Große Esse (ARN_05)

| Feld | Wert |
|---|---|
| Meister | **Kaldrex Vorn** (47), Glut/Metall, Zunftmeister |
| Stufe | skaliert 5–8 |
| Feldregel | **Schmiedeglut** |
| Dramaturgie | Kaldrex verlangt vorher eine **Schmiedeprobe** (Crafting-Minispiel: Rhythmus-Hämmern im Takt der Arena-Musik, 3 Schläge × 4 Runden); Ergebnis gibt dem Spieler einen kleinen Kampfbonus (+1 Buff-Stufe VER für 3 Züge) – nie Pflicht (DR-09) |

### 1.6 Quests

Hauptquest Akt II: Erkaltetes Kraterherz, erster persönlicher Auftritt **Sereth Vaun** (falls erste Akt-II-Region, CANON §46). Nebenquests: „Das Gelübde der Zunft“ (Waffenschmuggel aufdecken), „Sechs Glocken“ (Sammelquest), „Lavawächter in Not“, „Echos in den Minen“ (Freie Stimmen vs. Kontor, Entscheidung).

### 1.7 Musik

Tag: Blechbläser-Fanfaren-Motiv, Ambosse auf dem Takt, Kesselpauken; Glocken markieren Stunden. Nacht: Glutknistern, gedämpfte Hörner, Subbass. Arena: 5/4-Takt mit Hammer-Perkussion, Spieler-Treffer auf Schlag quantisiert (K55).

### 1.8 Einwohner & Feste

| NPC | Rolle | Muster |
|---|---|---|
| Kaldrex Vorn | Arenameister, Zunftvorsitz | Tagwerk; 6 Uhr Esse anheizen (Zeremonie) |
| Seraphe | Therme | Tagwerk spät (8–24) |
| Ithren | Händler | Tagwerk |
| Ambient | Schmiede, Lavawächter | Schichten (Esse läuft 24 h) |

**Fest:** *Glockenguss* – jeder 12. Spieltag: neue Glocke wird gegossen, Feuerwerk aus Lavafunken.

---

## 2. Hvitmark (R07)

### 2.1 Steckbrief

| Feld | Wert |
|---|---|
| Lage | R07 Hvitfell, 4,1 / 0,7 km – Gletschertal |
| Einwohner | 4.200 · Benannte NPCs 36 · Mass 140 · sichtbar 100 / 50 |
| Regierung | **Thing** (Volksversammlung, alle 10 Spieltage), Sprecherin gewählt |
| Fraktionen | Orden der Stille (stark präsent, Kloster am Pass), Wildwacht (Gletscherrettung), Kontor (Wolle, Silber) |
| Arena | ARN_07, **Sigrun Fjall** (Frost), Stufe 5–8 |
| Ursprungsstimme | Isv'aldr – Gletscherdom unter der Stadt |
| Fantasie | *„Hier erinnert man sich an alles. Das macht die Menschen sanft – und manche hart.“* |

### 2.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ 350 n.St. | Fischer- und Hirtensiedlung im Gletschertal |
| 760 n.St. | Silberfunde; Handel mit Kharsholm |
| 880 n.St. | Arena auf dem **Spiegelsee** (gefroren) |
| 948 n.St. | **Klangpest**: Resonanzsturm treibt Echos zur Raserei, Eiðvik wird zerstört; Hvitmark nimmt Überlebende auf |
| 951 n.St. | Überlebende gründen den **Orden der Stille** im Kloster Schweigfels |
| 990 n.St. | Erste Stillezonen – viele Hvitmarker sehen darin den Beweis der Ordenslehre |

### 2.3 Architektur & Layout

Stil: **Hvitnische Langhäuser** – Holz, Grasdächer, geschnitzte Giebel, Runenbalken; Steinfundamente gegen Gletscherwasser; heiße Quellen als Gemeinschaftsbäder.

```
              GLETSCHERZUNGE (N)  ── Gletscherdom (unter der Stadt, W4)
   ┌────────────────────────────────────────────────┐
   │  SPIEGELSEE (gefroren) = ARENA                  │
   │      │                                          │
   │  THINGPLATZ ── Langhaus der Sprecherin          │
   │      │                                          │
   │  HEISSE QUELLEN (Klangbrunnen im Badehaus)      │
   │      │                                          │
   │  WOLLSTUBE · SILBERSCHMIEDE · EISFISCHER-STEG    │
   │      │                                          │
   │  KLANGPEST-MAHNMAL (Gedenkstein, Namen der Toten)│
   └──────┴──── Passweg → Kloster Schweigfels (SW) ───┘
```

**Wahrzeichen:** Spiegelsee-Arena, Klangpest-Mahnmal, Badehaus über den heißen Quellen (Schutzzone, CANON §44).
**Traversal:** Schlittenwege (Bodenreiten +20 % auf Schnee), Eisfischer-Löcher (Unterwasser nur mit Schwimm-Echo).

### 2.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_HVIT_01 | Langhaus-Handel Haldor | Allgemein | 7–19 | Kälteschutz |
| MER_HVIT_02 | Wollstube Ylva | Ausrüstung | 8–18 | Kleidung III–IV (Kälte) |
| MER_HVIT_03 | Eisfischer Askel | Nahrung | 4–10 | Eisfisch-Eintopf |
| MER_HVIT_04 | Runa die Erinnernde | Selten | 18–2 | Erinnerungseis-Splitter (Lore) |
| MER_HVIT_05 | Silberschmied Eirik | Material | 7–17 | Silbererz, Gletscherquarz |

### 2.5 Arena: Spiegelsee (ARN_07)

| Feld | Wert |
|---|---|
| Meisterin | **Sigrun Fjall** (44), Frost; verlor Eltern und Bruder in der Klangpest |
| Stufe | skaliert 5–8 |
| Feldregel | **Spiegeleis** |
| Dramaturgie | Sigrun ist innerlich zerrissen zwischen Ordenslehre und Wärterberuf; nach dem Sieg Gespräch über Verlust – ihre Haltung beeinflusst einen Epilog-Satz (nicht die Endenwahl) |

### 2.6 Quests

Hauptquest Akt II: Pass-Schneesturm-Gate, Kloster Schweigfels, Sereth Vaun, Enthüllung W6 aus Ordenssicht. Nebenquests: „Namen auf dem Stein“ (Klangpest-Gedenken, Erinnerungseis), „Thing-Streit“ (Ordensanhänger vs. Wärter, Entscheidung), „Eiðvik-Neu baut auf“, „Aurora-Fotografie“.

### 2.7 Musik

Tag: Fidel mit Resonanzsaiten-Klang, Obertongesang, Holzflöte; viel Stille zwischen den Phrasen (thematisch). Nacht/Aurora: Glasharmonika-Schimmer + Chor. Arena: 3/4-Walzer, verlangsamt, Frost-Motive (gläserne Perkussion).

### 2.8 Einwohner & Feste

| NPC | Rolle | Muster |
|---|---|---|
| Sigrun Fjall | Arenameisterin | Tagwerk; abends am Mahnmal |
| Sprecherin Astrid Eiðsen | Thing | Tagwerk; Thing jeden 10. Spieltag |
| Runa | Händlerin, Erinnerungs-Hüterin | Nachtvolk |
| Ambient | Fischer, Hirten, Novizen des Ordens (graue Kutten) | Abendfeuer 18–22 |

**Fest/Gedenken:** *Tag der Stimmen* – Klangpest-Gedenktag (LiveOps-Echtzeit-Datum, einmal jährlich) – Schweigeminute, alle Musik verstummt.

---

## 3. Dorunsruh (R08)

### 3.1 Steckbrief

| Feld | Wert |
|---|---|
| Lage | R08 Ael'Dorun, 4,8 / 3,3 km – am Ruinenrand |
| Einwohner | 6.000 (davon ~1.400 Akademie-Angehörige) · Benannte NPCs 46 · Mass 190 · sichtbar 120 / 60 |
| Regierung | **Stadtkuratorium** – formal städtisch, faktisch von der Akademie dominiert (Rektor Venn hat Sitz und Stimme) |
| Fraktionen | **Akademie der Resonanz – Hauptsitz** (F01), Orden-Pilger (Kapelle in Säulenrast), Kontor (Grabungsfinanzierung) |
| Arena | ARN_08, **Aevrin Thal** (Arkan), Stufe 5–8 (praktisch meist 7–8, da R08 als letzte Akt-II-Region zugänglich wird) |
| Ursprungsstimme | Ka'thurel – Thronsaal-Gewölbe unter der Stadt |
| Fantasie | *„Die klügste Stadt der Welt steht auf den Ruinen der klügsten Stadt, die je fiel.“* |

### 3.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -600 v.St. | Ael'Dorun gegründet; Dorunsruh liegt auf dem einstigen Vorhof |
| 455 n.St. | **Gründung der Akademie der Resonanz** in einem restaurierten dorunischen Bau (*Altes Kolleg*) |
| 812 n.St. | Vael veröffentlicht die Taxonomie (Kodex-Grundlage) |
| 880 n.St. | Arena im **Glyphenhof** (dorunischer Innenhof) |
| 981 n.St. | **Aldric Venn** wird Rektor; Ausbau der Grabungen, neuer Glasbau *Neues Kolleg* |
| 1004 n.St. | Größte Stillezonen der Welt in den Ruinen; Akademie im Krisenmodus |

### 3.3 Architektur & Layout

Stil: **Zweischichtig** – dorunische Alabastermauern und Säulen (alt) + akademische Glas-/Messingbauten mit Klangwerk-Aufzügen (neu). Kontrast ist Programm: Wissen auf den Schultern der Vergangenheit.

```
   RUINEN (Thronstadt, N-O) ◄── Ruinensiegel (Story-Gate) ──┐
   ┌──────────────────────────────────────────────────────┴──┐
   │ NEUES KOLLEG (Glas, Messing) · REKTORAT (Venns Büro)     │
   │ Observatorium · Bibliothek der Resonanz (3 Ebenen)       │
   │─────────────────────────────────────────────────────────│
   │ ALTES KOLLEG (dorunisch) · GLYPHENHOF = ARENA             │
   │─────────────────────────────────────────────────────────│
   │ STUDENTENVIERTEL: Mensa · Buchhandlung Pell · Klangbrunnen│
   │ Grabungsbedarf Mira · Hehler Grave (Hinterhof)           │
   └───────── Straße nach Kharsholm (N) / Morvenfurt (S) ─────┘
```

**Wahrzeichen:** Glyphenhof-Arena, Bibliothek der Resonanz (Lore-Hub, 40 Bücher), Rektorat mit Blick auf die Ruinen, Observatorium (Sternwarten-Rätsel, Mondphasen).
**Traversal:** Klangwerk-Aufzüge, Dachgalerien aus Glas, Mauerkronen der alten Stadtmauer.

### 3.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_DORU_01 | Akademie-Buchhandlung Pell | Klangschriften | 8–20 | Klangschriften gegen Akademie-Ruf |
| MER_DORU_02 | Grabungsbedarf Mira | Allgemein | 6–18 | Laternen, Grabwerkzeug |
| MER_DORU_03 | Akademie-Kammer | Fraktion | 8–18 | Rufwaren, **Kodex-Linse II** |
| MER_DORU_04 | Hehler Grave | Selten | 21–3 | Grabungsfunde (Entscheidung: melden oder kaufen) |
| MER_DORU_05 | Mensa der Akademie | Nahrung | 7–21 | Ausdauer-Snacks |
| MER_DORU_06 | Prof. Thal (Sprechstunde) | Tutor | 14–16 | Arkan-Tutor |

### 3.5 Arena: Glyphenhof (ARN_08)

| Feld | Wert |
|---|---|
| Meister | **Aevrin Thal** (61), Arkan, Professor für Dorunistik |
| Stufe | skaliert 5–8 |
| Feldregel | **Glyphenfeld** (Tabellenumkehr alle 5 Züge) |
| Dramaturgie | Aevrin ist Venns ältester Kollege. **Nach** W6 (Verrat) wird er zur Schlüsselfigur: Er öffnet dem Spieler Venns Aufzeichnungen. Wird die Arena **vor** W6 bestritten, testet er „Regelverständnis“; danach kämpft er „für die Akademie, die sie sein sollte“ – zwei Dialogsätze, gleicher Kampf |

### 3.6 Quests

Hauptquest Akt II: Ruinensiegel, Venns Rektorat, **W6 Verrat** im Thronsaal-Gewölbe, **W7** (Wahrheit über Ilen). Nebenquests: „Glyphen-Übersetzung“ (10-teilige Rätselkette), „Der Hehler“ (Moral), „Kaels Forschungsarbeit“ (Rivalen-Arc vor W6), „Die Bibliothek der Resonanz“ (Lore-Sammlung), „Studentenstreik“ (Akademie-intern, Fraktionsruf).

### 3.7 Musik

Tag: Cembalo-artige Arpeggien + Streichquartett, Fugen-Anmutung (Ordnung, Intellekt). Nacht: Solo-Cello, Klangwerk-Ticken. Ruinennähe: Chor-Fragmente mischen sich ein (Ka'thurel). Arena: Kanon-Struktur (Thema verschoben in Stimmen), bei Tabellenumkehr kehrt sich die Melodie um (Spiegelumkehrung – musikalisches Feedback der Feldregel).

### 3.8 Einwohner & Feste

| NPC | Rolle | Muster |
|---|---|---|
| Aldric Venn | Rektor, Hauptantagonist | Gelehrt; 9 Uhr Kuratorium, 20 Uhr Observatorium (Begegnungen vor W6 möglich – charmant, hilfsbereit) |
| Aevrin Thal | Arenameister, Professor | Gelehrt; Sprechstunde 14–16 |
| Kael Duran | Rivale | Gelehrt; Labor 14–18 (vor W6), danach abwesend (Akt II/III-Arc) |
| Pell | Buchhändler | Tagwerk |
| Ambient | Studierende, Ausgräber, Pilger | Vorlesungsglocke 8/10/14 Uhr – Ströme über den Campus |

**Fest:** *Tag des Kodex* – jeder 15. Spieltag: Akademie-Ausstellung, Fotowettbewerb (Kodex-Linse), Bonusforschung.

---

## 4. Prismara (R09)

### 4.1 Steckbrief

| Feld | Wert |
|---|---|
| Lage | R09 Prismtiefen, 2,9 / 3,0 km – **unterirdisch** (−180 m) in einer Geodenkaverne, Zugang über Kraterlift |
| Einwohner | 3.800 · Benannte NPCs 34 · Mass 130 · sichtbar 100 / 50 |
| Regierung | **Stimmergilde** (Kristallstimmer-Älteste) |
| Fraktionen | Akademie-Labore, Kontor (Kristallexport), Wildwacht (Höhlenrettung) |
| Arena | ARN_09, **Ilyx Brannoc** (Kristall), **fest Stufe 9** |
| Ursprungsstimme | Prism'aion – Resonanzkammer unter der Stadt |
| Zugang | Stadt erst ab Akt III; der Kraterrand mit Liftstation ist ab Akt I Aussichtspunkt (Lift außer Betrieb – „Stillezone im Schacht“) |
| Fantasie | *„Eine Stadt aus Licht, das unter der Erde gefangen ist – und das jemand befreien möchte.“* |

### 4.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -20 v.St. | Missklang: Resonanzkrone verzerrt Kristalle tief im Krater (Missklang-Adern) |
| 520 n.St. | Glasbläser entdecken den Krater; erste Gruben |
| 610–700 n.St. | Aufstieg zur Kristallhauptstadt; Klangwerk-Energie für ganz Aethris |
| 880 n.St. | Arena in der **Prismenhalle** |
| 1004 n.St. | Stillezone dämpft Kristalle → Energiekrise in ganz Aethris (Hintergrundgeräusch der Story: Lichter flackern in anderen Städten ab Akt II) |

### 4.3 Architektur & Layout

Stil: **Prismanischer Kristallbau** – Häuser aus geschliffenem Kristallglas mit Messingrahmen, an Kavernenwänden „aufgehängt“; Licht kommt aus gestimmten Lichtkristallen (Lichtkristall-Zyklus, K10 §5.4).

```
   Kraterlift ▼ (−180 m)
   ┌───────────── GEODENKAVERNE (Ø 400 m, Höhe 120 m) ─────────────┐
   │   Decke: Lichtkristall-Kranz (Tageszyklus)                    │
   │                                                               │
   │   WANDHÄUSER (Ebenen 1–4, Hängebrücken)                       │
   │                                                               │
   │   PRISMENHALLE = ARENA (Zentrum, freistehender Kristall)      │
   │   Kristallmarkt · Stimmwerkstatt · Klangbrunnen               │
   │                                                               │
   │   KRISTALLSEE-UFER (W) ── Fähre zum Kristallsee-Lager         │
   │   Akademie-Labore (O) ── Tunnel zu den Missklang-Adern        │
   └───────────────── Abstieg zur Resonanzkammer (W4/Akt III) ─────┘
```

**Wahrzeichen:** Prismenhalle (Arena im Inneren eines riesigen Kristalls), Lichtkristall-Kranz, Kristallsee.
**Traversal:** Hängebrücken, Kristallaufzüge, Kletterwände aus Geodenkristall (Ausnahme der Kletterregel: *raue* Geodenwand kletterbar, glatte Kristalle nicht – Lesbarkeit über Materialfarbe, K56).

### 4.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_PRIS_01 | Kristallmarkt Seren | Allgemein | 0–24 | Grubenlampen |
| MER_PRIS_02 | Stimmwerkstatt Brannoc | Ausrüstung | 6–22 | Ausrüstung V, Laternen V |
| MER_PRIS_03 | Glasbläserin Quill | Material | 8–20 | Resonanzkristall (rotierend) |
| MER_PRIS_04 | Pilzküche Delve | Nahrung | 6–24 | Dunkelsicht-Gerichte |
| MER_PRIS_05 | Kristall-Tutorin (Ilyx) | Tutor | 10–18 | Kristall/Klang |

### 4.5 Arena: Prismenhalle (ARN_09)

| Feld | Wert |
|---|---|
| Meisterin | **Ilyx Brannoc** (26), Kristall – jüngste Arenameisterin, Nachfahrin Brannocs der Lauscherin |
| Stufe | fest 9 (Ass Lv. 59, Chor 6, Trio) |
| Feldregel | **Lichtbrechung** |
| Dramaturgie | Ilyx hört wie der Spieler Spuren von Grundfrequenzen (schwächer) – „Echo-Geschwister“-Moment; sie wird Verbündete im Finale (Nebenrolle) |

### 4.6 Quests

Hauptquest Akt III: Kronensplitter in den Missklang-Adern, Prism'aion erwacht, Energiekrise. Nebenquests: „Licht für die Oberwelt“ (Energiekrise lindern), „Verschüttete Stimmer“, „Brannocs Erbe“ (Ilyx und der Spieler), „Glasbläser-Meisterwerk“ (Crafting V).

### 4.7 Musik

Tag-Zyklus: Glasharmonika, Celesta, Streicher-Flageoletts, Arpeggien in Kristall-Tonleiter. Lichtkristall-„Nacht“: nur einzelne Kristallklänge. Missklang-Nähe: verstimmte Cluster mischen sich ein (Leitmotiv der Krone in Verzerrung). Arena: helle Perkussion, Brechungs-Effekte (Töne springen zwischen Stereo-Kanälen).

### 4.8 Einwohner & Feste

| NPC | Rolle | Muster |
|---|---|---|
| Ilyx Brannoc | Arenameisterin, Stimmerin | Tagwerk |
| Gildenälteste Seren Quarz | Regierung | Tagwerk |
| Ambient | Bergleute, Stimmer, Glasbläser | Schichtglocken; Stadt folgt Lichtkristall-Zyklus |

**Fest:** *Kristallpuls-Nacht* – bei jedem dritten Kristallpuls (≈ 18 Spielstunden) ein kurzes Lichtfest.

---

## 5. Aerion (R10)

### 5.1 Steckbrief

| Feld | Wert |
|---|---|
| Lage | R10 Nimbara, 4,1 / 3,1 km, 1.800 m Höhe |
| Einwohner | ~800 · Benannte NPCs 30 · Mass 60 · sichtbar 70 / 40 |
| Regierung | **Rat der Baumeister** (erbliche Hüterlinien, Vorsitz: Hüterin Oruma Siyel) |
| Fraktionen | Keine Fraktion präsent (bewusste Isolation) – nach Akt III: Akademie-Delegation, Wildwacht-Kontakt |
| Arena | ARN_10, **Oruma Siyel** (Klang/Licht), **fest Stufe 10** |
| Ursprungsstimme | **Aeth'rion** (Leitstimme) – Sternenarena über der Stadt |
| Fantasie | *„Die letzte Stadt, die das Lied nie ganz vergessen hat.“* |

### 5.2 Geschichte

| Jahr | Ereignis |
|---|---|
| ~ -250 v.St. | Nimbara gehoben; Aerion als Werft- und Sternwartenstadt |
| ~ -20 v.St. | Kronenwerft: Maedryn aktiviert die Krone |
| 0 | Große Stille; Aerion überlebt, isoliert sich – Hüterlinien bewahren Ilens Vermächtnis |
| 0–1004 n.St. | Völlige Isolation; Bodenbewohner halten Nimbara für Legende (gesehen, nie erreicht) |
| 880 n.St. | Wendelin Aar erreicht als einzige Bodenbewohnerin Aerion (über einen Resonanzstein, heute erloschen) und richtet mit den Hütern die 10. Arena ein – deshalb gehört Aerion zum Weltakkord |
| 1004 n.St. | Der Spieler kommt an (Akt III) |

### 5.3 Architektur & Layout

Stil: **Nimbarische Filigranarchitektur** – weiße Steinbögen, Goldintarsien, Windharfen, Klangwerk-Gondeln zwischen Inseln; offene Terrassen ohne Geländer (Fallrettung, CANON §50).

```
                    ★ STERNENARENA (2.600 m, schwebende Plattform)
                       ║ Windstrom-Aufstieg
   ┌──────────────── AERION (Hauptinsel, 1.800 m) ────────────────┐
   │ RATSHALLE DER BAUMEISTER · ARCHIV (Erstchor-Lore)            │
   │ Sonnenterrasse (Morgenzeremonie) · Klangbrunnen               │
   │ Windhandel · Federschneiderei · Sternenküche                  │
   └───── Gondel ──────────── Gondel ───────────── Gondel ─────────┘
     LUMEYA (Dorf)       KRONENWERFT (Ruine)        WOLKENRAST (Dorf)
```

**Wahrzeichen:** Sternenarena (Finale), Ratshalle mit der **Wand der Zehn** (Fresko des Erstchors – Ilens Gesicht hier *erhalten*, Gegenstück zur gesichtslosen Statue in Ael'Dorun), Windharfen-Allee.
**Traversal:** Gondeln (Schnellreise intern), Aufwinde, Windströme.

### 5.4 Händler

| ID | Name | Kategorie | Zeiten | Besonderheit |
|---|---|---|---|---|
| MER_AERI_01 | Windhandel Aelia | Allgemein | 5–21 | Gleiter V |
| MER_AERI_02 | Archiv der Baumeister | Klangschriften | 8–20 | Seltene Klangschriften, Erstchor-Lore |
| MER_AERI_03 | Sternenküche | Nahrung | 18–6 | Kälteschutz |
| MER_AERI_04 | Hüterin Oruma | Tutor | 6–8 | nur zur Morgenzeremonie |
| MER_AERI_05 | Federschneiderei Brisk | Ausrüstung | 8–18 | Kleidung V |

### 5.5 Arena: Sternenarena (ARN_10)

| Feld | Wert |
|---|---|
| Meisterin | **Oruma Siyel** (70), Klang/Licht, Hüterin Aeth'rions |
| Stufe | fest 10 (Ass Lv. 67, Chor 6, Trio) |
| Feldregel | **Sternenfall** |
| Dramaturgie | Letzter Akkord vor dem Finale. Oruma erkennt Ilens Nachklang im Spieler und kämpft „um zu prüfen, ob der Nachklang frei gewählt oder nur geerbt ist“. Die Sternenarena ist danach Schauplatz des Finales (Venn, Velnox, Entscheidung) |

### 5.6 Quests

Hauptquest Akt III: Ankunft, Misstrauen der Baumeister, Kronenwerft (W8), Finale (W9). Nebenquests: „Bodenbewohner“ (Vorurteile abbauen), „Inselendemiten“ (Wildwacht-Kontakt), „Windstrom-Rennen“, „Wendelins letzter Stein“ (erloschener Resonanzstein – reaktiviert → Verbindung zu Eichenhall), „Letzte Bitten“ (Atemzug-Fenster vor dem Finale, DR-29).

### 5.7 Musik

Das **Weltlied-Leitmotiv** erklingt hier erstmals vollständig (alle anderen Stadtthemen enthalten Fragmente davon, §8). Tag: Frauen- und Kinderchor, Harfe, Glocken, Windharfen in der Tonart. Nacht: Solo-Stimme, Sternenschimmer. Arena: alle zehn Stadt-Fragmente verschmelzen zum Weltlied-Thema (Finale).

### 5.8 Einwohner & Feste

| NPC | Rolle | Muster |
|---|---|---|
| Oruma Siyel | Hüterin, Arenameisterin | 6–8 Morgenzeremonie, sonst Archiv |
| Aelia | Windhändlerin | Tagwerk |
| Ambient | Baumeister-Familien, Sternkundige | Morgenzeremonie bei Sonnenaufgang – ganze Stadt auf der Sonnenterrasse |

**Fest:** *Sternenlesen* – jede Neumondnacht (Mondphasen, K15): Himmelslichter, Lore-Gespräche mit allen Hütern.

---

## 6. Sonderort: Kloster Schweigfels

| Feld | Wert |
|---|---|
| Lage | R07, am Schweigfels-Pass (≈ 3,3 / 1,1 km), kein Stadtstatus |
| Funktion | **Hauptsitz des Ordens der Stille** (F05), Schauplatz Akt II |
| Bewohner | ~120 Ordensmitglieder; Schweigegelübde (Kommunikation über Gesten und Schiefertafeln – UI: Tafel-Dialoge statt Sprachausgabe) |
| Architektur | Schwarzer Fels, keine Glocken, keine Musikinstrumente; Gänge mit schalldämpfenden Filzwänden; Innenhof mit **Stillstein-Werkstatt** |
| Dienste | Klangbrunnen (verhüllt – „Wir heilen auch ohne Lied“: funktioniert dennoch, Lore-Ironie), Resonanzstein, Questbrett (Orden), kein Händler außer Ordensladen (Ruf F05) |
| Akustik/Musik | **Bewusste Stille**: keine Musik, nur Raumklang (Schritte, Atem, Wind). Erst beim Auftritt Sereths setzt ein einzelner tiefer Ton ein |
| Story | Erste Begegnung mit Sereth (falls nicht bereits in Akt II), Ordenssicht auf W6, Wahl späterer Allianzen (Epilog-Varianten, CANON §38) |
| Echos | Ordensmitglieder halten **verstummte** Echos in Ruhezellen (nicht gequält – schlafend), moralisch verstörend und zugleich zärtlich inszeniert |

---

## 7. Gesamtübersicht aller 10 Städte

| Stadt | Region | Einw. | Regierung | Arena (Meister, Typ, Stufe) | Fest | Musik-Kern |
|---|---|---|---|---|---|---|
| Eichenhall | R01 | 9.000 | Stadtrat + Bundesrat | Maelis Wendt, Blüte, 1 | Lindenfest (7.) | Holzbläser, Harfe |
| Kharsholm | R02 | 6.500 | Klanrat | Torvik Hrall, Stein/Schwerkraft, 2–4 | Schwurnacht (10.) | Brummchor, Ambosse |
| Morvenfurt | R03 | 5.000 | Fährleute-Zunft | Evhe Corrach, Gift/Geist, 2–4 | Laternennacht (5.) | Flöte, Trommel, Fidel |
| Qasr Sahrun | R04 | 7.500 | Rat der Sonnenhöfe | Shirah Harrâd, Licht, 5–8 | Nacht der Gäste (9.) | Laute, Rahmentrommel |
| Schlackenwehr | R05 | 5.500 | Zunftrat | Kaldrex Vorn, Glut/Metall, 5–8 | Glockenguss (12.) | Blech, Ambosse |
| Saltrand-Hafen | R06 | 11.000 | Hafenrat | Beke Tamsen, Flut/Sturm, 2–4 | Glockenflut (6.) | Akkordeon, Shanty |
| Hvitmark | R07 | 4.200 | Thing | Sigrun Fjall, Frost, 5–8 | Tag der Stimmen (jährlich) | Fidel, Obertongesang |
| Dorunsruh | R08 | 6.000 | Stadtkuratorium | Aevrin Thal, Arkan, 5–8 | Tag des Kodex (15.) | Cembalo, Quartett |
| Prismara | R09 | 3.800 | Stimmergilde | Ilyx Brannoc, Kristall, 9 | Kristallpuls-Nacht | Glasharmonika, Celesta |
| Aerion | R10 | ~800 | Rat der Baumeister | Oruma Siyel, Klang/Licht, 10 | Sternenlesen (Neumond) | Chor, Harfe, Weltlied |
| **Σ** | | **~59.300** | | | | |

---

## 8. Musik-Leitmotivsystem der Städte

Jedes Stadtthema enthält ein **Fragment** des Weltlied-Leitmotivs (7 Töne, Details K55). Das Fragment ist der Teil, der zur Ursprungsstimme der Region gehört. In Aerion erklingt das vollständige Motiv; im Finale verschmelzen alle Fragmente.

```
 Weltlied-Leitmotiv (Platzhalter-Notation, Komposition K55):
   Ton:      1    2    3    4    5    6    7
 Eichenhall ████                                  (Sylv'anor: Töne 1–2)
 Kharsholm       ████                             (Orh'gruun: 2–3)
 Morvenfurt           ████                        (Nhael'vesh: 3–4)
 Saltrand                  ████                   (Thal'assyr: 4–5)
 Qasr Sahrun                    ████              (Ash'kareth: 5–6)
 Schlackenwehr                       ████         (Pyr'thagon: 6–7)
 Hvitmark      ██   (Umkehrung 1–2)               (Isv'aldr)
 Dorunsruh        (Krebs aller Töne, fragmentiert)(Ka'thurel)
 Prismara      (Arpeggiert, Töne 1/3/5/7)         (Prism'aion)
 Aerion     ████████████████████████████████████  (Aeth'rion: vollständig)
```

**Design-Absicht:** Spieler, die genau hinhören, erkennen ab Akt II, dass alle Städte „dasselbe Lied“ singen – eine akustische Vorahnung von W4 (Arenen über den Stimmen). Das ist die musikalische Umsetzung von Säule S2 („Verstehen durch Zuhören“).

---

## 9. Code

### 9.1 Schweige-Dialoge (Kloster Schweigfels)

```cpp
// GF_Quests: Dialogzeilen mit Darstellungsmodus. Ordensmitglieder nutzen Tafel-Dialoge (K12 §6).
UENUM(BlueprintType)
enum class EDialoguePresentation : uint8
{
	Voiced,        // vertont, Untertitel
	Barked,        // kurze Umgebungszeile
	SlateWritten,  // Schiefertafel – kein Audio, handschriftliche Schrift (lokalisiert), Kreidegeräusch
	Gesture        // nur Animation + Untertitel in eckigen Klammern (Zugänglichkeit)
};

USTRUCT(BlueprintType)
struct AETHRISCORE_API FDialogueLineSpec
{
	GENERATED_BODY()
	UPROPERTY(EditAnywhere) FName LineId;                         // DLG_<Quest>_##
	UPROPERTY(EditAnywhere) FName SpeakerNpc;
	UPROPERTY(EditAnywhere) FText Text;
	UPROPERTY(EditAnywhere) EDialoguePresentation Presentation = EDialoguePresentation::Voiced;
	UPROPERTY(EditAnywhere) TSoftObjectPtr<USoundBase> VoiceOver;   // leer bei SlateWritten/Gesture
};
```

### 9.2 Stadtthema-Auswahl (GF_Audio, Vorgriff K55)

```cpp
/** Wählt die Variante des Stadtthemas aus Tagesphase, Fest und Story-Zustand (K12 §1–§5). */
FGameplayTag UCityMusicSubsystem::SelectCityVariant(FName SettlementId) const
{
	if (IsFestivalActive(SettlementId))                 return TAG_Music_City_Festival;
	if (IsStillnessActive(SettlementId))                return TAG_Music_City_Muted;   // Stillezone in der Stadt
	const FGameplayTag Phase = WorldState()->GetTimeOfDayTag();
	return Phase == TAG_TimeOfDay_Night ? TAG_Music_City_Night : TAG_Music_City_Day;
}
```

---

## 10. Decision Records

### ADR-058 – Aerion isoliert, Wendelin als einzige Verbindung
- **Entscheidung:** Aerion war 1.004 Jahre isoliert; die 10. Arena wurde 880 n.St. durch Wendelin Aar mit den Hütern eingerichtet. Vorteil: Erklärt, warum Nimbara sichtbar, aber unerreichbar war (ADR-043) und warum es trotzdem eine Arena gibt. Konsequenz: Ein erloschener Resonanzstein in Aerion wird in einer Nebenquest reaktiviert (Schnellreise-Verbindung Eichenhall ↔ Aerion als Belohnung).

### ADR-059 – Schweigegelübde als Präsentationsform
- **Entscheidung:** Kloster-Dialoge als Tafel-/Gestentexte. Vorteil: Starke Identität, spart Vertonung (~2.000 Zeilen), unterstreicht Thema. Nachteil: Textlastiger Ort → kurze Zeilen (≤ 80 Zeichen) und Gesten-Animationen kompensieren.

### ADR-060 – Weltlied-Fragmente in allen Stadtthemen
- **Entscheidung:** Musikalische Vorahnung des Kernmysteriums (§8). Konsequenz für K55: Leitmotiv wird **vor** den Stadtthemen komponiert (Abhängigkeit im Audio-Plan).

### ADR-061 – Energiekrise als Weltzustand ab Akt II
- **Entscheidung:** Die Stillezone in Prismtiefen dämpft Kristallenergie – ab Akt II flackern Lichter in allen Städten (globaler Data Layer `DL_Story_EnergyCrisis`), Händler haben leicht reduzierte Sortimente bei Kristallwaren (K42). Vorteil: Akt III-Region wirkt in die ganze Welt (DR-13). Nach Lösung in Akt III: Lichter strahlen heller als zuvor (Belohnungsgefühl).

---

## 11. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §54 | Städte Schlackenwehr, Hvitmark, Dorunsruh, Prismara, Aerion vollständig (Regierung, Geschichte, Layout, Händler, Arena-Dramaturgie, Quests, Musik, NPCs, Feste) | LOCKED |
| §54 | Neue Figuren: Sprecherin Astrid Eiðsen (Hvitmark), Gildenälteste Seren Quarz (Prismara), Händler gemäß `Merchants.csv` | LOCKED |
| §54 | Dorunsruh: Venn im Rektorat (vor W6 begegenbar), Aevrin Thal öffnet nach W6 Venns Aufzeichnungen; Kael bis W6 im Labor | LOCKED |
| §54 | Aerion: ~800 Einwohner, isoliert seit der Stille, Wand der Zehn (Ilens Gesicht erhalten), Wendelin Aar 880 n.St. einzige Verbindung, erloschener Resonanzstein (Nebenquest) | LOCKED |
| §54 | Prismara: Lift ab Akt I außer Betrieb, Energiekrise ab Akt II (`DL_Story_EnergyCrisis`), Ilyx Brannoc hört schwach Grundfrequenzen | LOCKED |
| §54 | Schlackenwehr: Zunft-Gelübde gegen Waffen (Herkunft des Waffenverbots), Schmiedeprobe vor dem Kampf | LOCKED |
| §55 | Kloster Schweigfels: Ordenssitz, ~120 Mitglieder, Schweigegelübde (Tafel-/Gestendialoge), keine Musik, verstummte Echos in Ruhezellen | LOCKED |
| §56 | Städte-Gesamtübersicht (§7), Gesamtbevölkerung ~59.300 | LOCKED |
| §56 | Weltlied-Leitmotiv (7 Töne) mit Fragmenten je Stadt; vollständig in Aerion; Komposition des Leitmotivs vor den Stadtthemen | LOCKED |
| §29 | `EDialoguePresentation` (Voiced, Barked, SlateWritten, Gesture), `FDialogueLineSpec` | LOCKED |
| §10 | ADR-058 – ADR-061 | LOCKED |

---

## 12. Kapitel-Checkliste

- [x] Schlackenwehr, Hvitmark, Dorunsruh, Prismara, Aerion nach Stadt-Template vollständig
- [x] Händler aller 10 Städte im Repository (54)
- [x] Arena-Dramaturgien der Arenen 05, 07, 08, 09, 10
- [x] Sonderort Kloster Schweigfels
- [x] Gesamtübersicht aller 10 Städte (Briefing-Pflichtblöcke erfüllt)
- [x] Musik-Leitmotivsystem (Weltlied-Fragmente)
- [x] Code: Dialog-Präsentationsmodi, Stadtmusik-Variantenwahl
- [x] ADR-058 – ADR-061, CANON aktualisiert

➡️ **Nächstes Kapitel: K13 – Dörfer & Außenposten.**
