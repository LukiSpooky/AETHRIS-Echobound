# K56 · Art Bible

| Feld | Wert |
|---|---|
| Dokument | Kapitel 56 von 68 · Präsentation III |
| Version | 1.0 |
| Owner | Creative Director, Art Director |
| Mitwirkende | Lead Concept Artist, Lead Creature Artist, Lead Environment Artist, Character Artist, Technical Art Director, UI Artist, Lighting Artist |
| Baut auf | K07 (Kosmologie), K09/K10 (Biome, Regionspaletten, CANON §46/§48), K11–K13 (Siedlungen), K15 §6–§9 (Licht), K16 (Kreaturendesign CD-01–CD-19, Klangmal), K17 §9 (Typfarben Arbeitsstand, Symbole), K54 (UI-Tokens, Farbenblind-Modi), K55 (Klang ↔ Bild), CANON §69, §73, §78, DR-17, DR-22, DR-24 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Art/TypeColors.csv` (final, inkl. Farbenblind-Paletten), `RegionPalettes.csv`, `AssetBudgets.csv`, Prüfer `tools/ref/aethris_palette.py` (AR-01, AR-02) |
| Neue Kanon-Einträge | CANON §217 (Art-Säulen und Stil), §218 (Typfarben final), §219 (Kreaturen, Menschen, Architektur), §220 (Licht, Stille, Enden), §221 (Asset-Regeln) |

---

## Inhalt

1. [Art-Säulen](#1-art-säulen)
2. [Stil](#2-stil)
3. [Farbe](#3-farbe)
4. [Licht, Wetter, Tageszeit](#4-licht-wetter-tageszeit)
5. [Kreaturen](#5-kreaturen)
6. [Menschen und Kleidung](#6-menschen-und-kleidung)
7. [Architektur und Kulturen](#7-architektur-und-kulturen)
8. [Umwelt und Lesbarkeit](#8-umwelt-und-lesbarkeit)
9. [Stille, Sturm, Enden](#9-stille-sturm-enden)
10. [Asset-Regeln und Budgets](#10-asset-regeln-und-budgets)
11. [Clean-Room und Referenzen](#11-clean-room-und-referenzen)
12. [Review-Prozess](#12-review-prozess)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Art-Säulen

| Säule | Bedeutung | Beispiel |
|---|---|---|
| **Gesungene Welt** | Formen folgen Klang: Schwingungen, Wellen, Resonanzringe, Obertonreihen als Gestaltungsmotiv in Natur, Architektur und Echos | Rinden mit Jahresringen wie Wellen; Kharsk-Türme als Orgelpfeifen; Klangmale |
| **Staunen vor Nähe** | Weite Panoramen, aber die schönsten Dinge sind klein und nah (ein Klangmal, ein Moos, ein Glas) | Gleitpanorama (K44) → Lichtung → Kodex-Linse |
| **Wärme mit Wehmut** | Warme Grundtöne, gesättigte Akzente; Wehmut über Patina, Ruinen, Pausen | Dorisch in Farbe: Gold + Violett |
| **Lesbar zuerst** | Gameplay-Information ist sofort erkennbar (Art und Typ auf 30 m, CD-05; Kletterflächen; Gefahren) | Typ-Leitmerkmale, Silhouetten |
| **Würde statt Grausamkeit** | Kein Blut, keine Wunden (CD-18), unheimlich ja, grausam nein (CD-19) | Erschöpfung = erlöschendes Klangmal |

---

## 2. Stil

**Stilisierter Realismus:** Materialien glaubwürdig (PBR, Lumen), Formen bewusst überhöht. Proportionen: Echos leicht vergrößerte Köpfe/Augen nur bei Stufe 1 (Zuneigung), Stufe 3 erwachsen und markant (CD-07: ≥ 2× Stufe 1). Menschen realistisch proportioniert, Kleidung mit großen, lesbaren Formen.

| Ebene | Detailgrad | Regel |
|---|---|---|
| Groß (Silhouette, 30 m) | Formsprache, Typ-Leitmerkmal, Größe | CD-01 Silhouetten-Ähnlichkeit < 0,80; CD-05 |
| Mittel (5–10 m) | Klangmal, Musterung, Kleidung | Max. 3 Farben + Klangmal-Akzent (CD-04) |
| Klein (< 2 m, Kodex-Linse) | Materialien, Schuppen, Fell, Gravuren | Detail für Fotografie (K39) |

**Formsprache je Typ (CD-06, Leitmerkmal):**

| Typ | Formsprache | Leitmerkmal (sichtbar) |
|---|---|---|
| Glut | Zungen, Spitzen nach oben | Glimmende Fugen |
| Flut | Wellen, Flossen, fließende Kurven | Wasserschleier oder Flossenkämme |
| Stein | Blöcke, Facetten, Schwere | Gesteinsplatten |
| Sturm | Spiralen, Federn, Schwung | Wirbelmuster |
| Blüte | Blätter, Ranken, Knospen | Wachsende Teile |
| Frost | Nadeln, Sechsecke, Kristallflächen | Reif an Kanten |
| Leere | Negativraum, Ringe, Lücken | „Fehlende“ Körperteile als Löcher |
| Licht | Strahlen, Kränze, Transparenz | Leuchtende Säume |
| Gift | Tropfen, Blasen, Pilzformen | Schimmernde Drüsen |
| Metall | Platten, Nieten, Kanten | Metallische Reflexe |
| Geist | Schleier, Halbmonde, Unschärfe | Ausgefranste Ränder |
| Kristall | Facetten, Prismen, Rauten | Lichtbrechung |
| Klang | Bögen, Membranen, Resonanzkörper | Schwingende Membranen |
| Schwerkraft | Orbits, schwebende Teile | Kreisende Splitter |
| Arkan | Glyphen, Kanons, Spiegelungen | Leuchtende Glyphen |

---

## 3. Farbe

### 3.1 Typfarben (final)

K17 legte einen Arbeitsstand fest (CANON §78). K56 prüft ihn rechnerisch und legt ihn fest: Abstand jedes Farbpaars nach **CIEDE2000**, simuliert für Protanopie, Deuteranopie und Tritanopie (Machado 2009, Schweregrad 1,0). Für jeden Farbenblind-Modus (K54 `ACC_COLORBLIND`) erzeugt `aethris_palette.py` eine Palette, deren Helligkeiten die engsten Paare spreizen.

| Modus | Engstes Paar vorher (Arbeitsstand K17) | ΔE2000 | Engstes Paar final | ΔE2000 | Schwelle |
|---|---|---|---|---|---|
| Normal | Sturm / Frost | 9,4 | Sturm / Frost | 11,2 | 10 |
| Protan | Gift / Schwerkraft | 1,7 | Blüte / Klang | 6,7 | 6 |
| Deutan | Metall / Arkan | 1,3 | Kristall / Arkan | 6,4 | 6 |
| Tritan | Blüte / Arkan | 8,5 | Blüte / Arkan | 8,5 | 6 |

| Typ | Normal | Protan | Deutan | Tritan | Symbol | Kontrast zu UI-Grund |
|---|---|---|---|---|---|---|
| Glut | `#E8562A` | `#E8562A` | `#E8562A` | `#E8562A` | Flamme in Dreieck | 4,7 : 1 |
| Flut | `#2E8BC0` | `#2E8BC0` | `#3690C6` | `#2E8BC0` | Welle in Kreis | 4,5 : 1 |
| Stein | `#8C7B65` | `#8C7B65` | `#8C7B65` | `#8C7B65` | Sechseck, gefüllt | 4,2 : 1 |
| Sturm | `#7FD1E8` | `#7FD1E8` | `#85D7EE` | `#7FD1E8` | Spirale | 9,9 : 1 |
| Blüte | `#5DAA4C` | `#5DAA4C` | `#5DAA4C` | `#5DAA4C` | Blatt in Tropfen | 5,9 : 1 |
| Frost | `#C9EEF7` | `#C9EEF7` | `#C9EEF7` | `#C9EEF7` | Sechszackiger Stern | 13,8 : 1 |
| Leere | `#4A3A6E` | `#4A3A6E` | `#4A3A6E` | `#4A3A6E` | Ring (Negativraum) | 1,7 : 1 |
| Licht | `#F6D86B` | `#F6D86B` | `#F6D86B` | `#F6D86B` | Strahlenkranz | 12,1 : 1 |
| Gift | `#8E4FB0` | `#9859BB` | `#8E4FB0` | `#8E4FB0` | Drei Tropfen | 3,2 : 1 |
| Metall | `#9AA3AD` | `#9AA3AD` | `#9099A3` | `#9AA3AD` | Quadrat mit Niet | 6,7 : 1 |
| Geist | `#B7A4E0` | `#BDA9E6` | `#B19FDA` | `#B7A4E0` | Halbmond mit Schleier | 7,6 : 1 |
| Kristall | `#E28FC6` | `#DC8AC0` | `#DC8AC0` | `#E28FC6` | Raute mit Facette | 7,3 : 1 |
| Klang | `#F2A93B` | `#F2A93B` | `#F2A93B` | `#F2A93B` | Drei Bögen (Schall) | 8,5 : 1 |
| Schwerkraft | `#4B5BA6` | `#3F519C` | `#4556A1` | `#4B5BA6` | Kreis mit Punkt (Orbit) | 2,7 : 1 |
| Arkan | `#3FB8A8` | `#3FB8A8` | `#53CAB7` | `#3FB8A8` | Glyphe (Achtstern) | 7,0 : 1 |

**Änderungen gegenüber K17:** Leere aufgehellt (`#2B2240` → `#4A3A6E`, damit das Symbol auf dem dunklen UI-Grund `#1C1B24` sichtbar bleibt), Frost kühler und heller (`#BFE6F5` → `#C9EEF7`, Abstand zu Sturm ≥ 10). Alle anderen Werte unverändert. Typen bleiben **immer** Symbol + Name (K17, UX-07); die Farbe ist zusätzliche Information.

### 3.2 Nutzung der Typfarben

| Ort | Regel |
|---|---|
| UI | Typ-Chips, Effektivitätsanzeigen, Kodex – volle Sättigung |
| Echos | Typfarbe nur als **Akzent** (Klangmal, Leitmerkmal); Grundfarben aus Lebensraum und Herkunft (CD-02: kein „Tier + Elementfarbe“) |
| VFX | Fähigkeiten in Typfarbe, Treffer/Leuchten heller, Rauch/Partikel desaturiert (K58) |
| Welt | Typfarben erscheinen nicht großflächig in Umgebungen (Verwechslungsgefahr) |

### 3.3 Regionspaletten

Die Paletten aus K09/K10 (LOCKED) gebündelt:

| DisplayName | C1 | C2 | C3 | C4 | C5 | Light |
|---|---|---|---|---|---|---|
| Verdanthain | Moosgrün #4F7A3A | Lindgold #D9B44A | Rindenbraun #5B4632 | Himmelsdunst #A9C6D9 | Glockenblütenviolett #8C6FB8 | Warmes, gefiltertes Waldlicht; goldene Stunde lang |
| Kharsgrat | Granitgrau #6E6E73 | Flechtengelb #C8B560 | Eisenrot #8A3B2A | Gipfelweiß #E8EEF2 | Kiefernblaugrün #2F5A55 | Hartes, klares Höhenlicht; lange Schatten |
| Morvenmoor | Moorgrün #3E4F2C | Torfbraun #4A3424 | Nebelgrau #9BA59A | Irrlichtcyan #6FD3C2 | Sumpfblüten-Magenta #B0457D | Diffus, Nebel als Lichtträger; Irrlichter als Akzente |
| Sahrun-Weite | Dünengold #E0B46A | Terrakotta #B5653B | Himmelstürkis #3FA7B5 | Glasweiß #F3EBDD | Abendviolett #5E3B6E | Gleißend am Tag, violette Nächte; Glas spiegelt |
| Ignareth | Basaltschwarz #1E1C1F | Lavaorange #F05A1A | Glutrot #A3201B | Schwefelgelb #D8C23A | Aschegrau #7A7470 | Licht von unten (Lava); Asche dämpft den Himmel |
| Saltrand | Meerblau #1F5F8B | Gischtweiß #EEF4F6 | Sandbeige #D9C7A3 | Rostrot #9B3D2E | Algengrün #4E7D5B | Salzige Helligkeit; Glitzern auf Wasser |
| Hvitfell | Schneeweiß #F4F7FA | Gletscherblau #7FB6D6 | Nordnacht #1B2440 | Auroragrün #4FE3A5 | Holzrot #8E2F2A | Niedrige Sonne (Max. 30°), Polarlicht als zweite Lichtquelle |
| Ael'Dorun | Alabaster #E6DFD1 | Patinagrün #5F8F7F | Glyphengold #E3B54C | Schattenviolett #3C2F4F | Stilleschwarz #141418 | Heller Stein, tiefe Schatten; Glyphen glühen |
| Prismtiefen | Amethyst #7E57C2 | Quarzrosa #E9A6C8 | Tiefblau #14203A | Kristallcyan #5ED6E8 | Missklang-Rot #C2185B | Kein Himmel; Licht aus Kristallen, gebrochen in Farben |
| Nimbara | Himmelsblau #7EC8F0 | Wolkenweiß #FFFFFF | Morgenrosa #F5B3C6 | Weißgold #F0D78C | Sternennacht #0D1330 | Licht von allen Seiten; Wolken als Reflektoren; Sonne 05–21 Uhr |

**Regel:** Jede Region hat **eine Signaturfarbe**, die sonst nirgends großflächig vorkommt (Lindgold, Flechtengelb, Irrlichtcyan, Himmelstürkis, Lavaorange, Meerblau, Auroragrün, Glyphengold, Kristallcyan, Morgenrosa). Spielende erkennen die Region an der Farbe – auch im Gleitpanorama.

### 3.4 Farbskript der Story

| Abschnitt | Farbstimmung |
|---|---|
| Prolog | Warmes Grün und Gold, eine graue Wunde (Stillezone) |
| Akt I | Regionen in voller Sättigung; Grau wächst an den Rändern |
| Akt II | Wärmere, härtere Kontraste (Wüste, Lava, Eis); Akademie-Gewölbe in kaltem Weiß (Krone) |
| Akt III | Gebrochenes Licht (Prismtiefen), dann reiner Himmel (Nimbara); Finale: Welt entsättigt bis auf Spieler und Chor |
| Neues Lied | Alle Regionspaletten gleichzeitig, Aurora in zehn Farben |
| Sanfte Stille | Silber über allem, Farben 15 % entsättigt, warme Lichter bleiben |

---

## 4. Licht, Wetter, Tageszeit

Die Sonnenkurven und Lichtwerte stehen in K15 (CANON §68). Art-Regeln:

| Situation | Regel |
|---|---|
| Goldene Stunde | Dämmerungen sind die schönsten Momente: warme Seitenlichter, lange Schatten, Klangmale leuchten stärker (+20 %) |
| Nacht | Mondlicht (0–0,25 lx nach Phase) + **Klangmale als Lichtquellen** – Echos machen die Nacht lesbar |
| Regen | Nasse Materialien (Wetness), weichere Schatten, Pfützenreflexe |
| Nebel | Volumetrischer Nebel, Sichtweite 40–120 m, Silhouetten statt Details |
| Gewitter | Blitze als Lichtereignis (Lumen-Update), keine Bildschirmblitze bei Bewegungsreduktion |
| Sandsturm/Ascheregen | Partikelvolumen, Farbstich (Gelb/Grau), Sichtweite 30 m |
| Polarlicht | Grünes/violettes Himmelslicht als zweite Lichtquelle (Hvitfell) |
| Resonanzsturm | Himmel pulsiert in den Typfarben der Region im Rhythmus des Sturms; Klangmale aller Echos synchron |

---

## 5. Kreaturen

### 5.1 Regeln (Zusammenfassung K16, CANON §69)

CD-01 Silhouettentest · CD-02 zwei Gestaltungsachsen (Ort/Klang/Leben) · CD-03 keine Genre-Signaturen · CD-04 ≤ 3 Farben + Klangmal · CD-05 Art und Typ auf 30 m · CD-06 Typ-Leitmerkmal · CD-07 Linienmotiv, Stufe 3 ≥ 2× Stufe 1 · CD-08 sechs Emotionen · CD-09 Ökologie (K52) · CD-10 Bewegung folgt Körperbau · CD-11 Dichte plausibel · CD-12 Lebensraum · CD-13 Nische · CD-14 Merkmale · CD-15 Unruhe-Profil · CD-16 Kampfrolle · CD-17 Reiten ab L · CD-18 kein Blut · CD-19 unheimlich ja, grausam nein.

### 5.2 Das Klangmal

Das Klangmal ist das wichtigste visuelle Element des Spiels (CANON §73): Timing-Signal der Bindung, Emotionsanzeige, Treffer-Flackern statt Blut, Erlöschen bei Erschöpfung.

| Eigenschaft | Regel |
|---|---|
| Lage | Immer sichtbar aus der Standard-Kameraperspektive (Kopf, Nacken, Rücken oder Brust) |
| Form | Je Linie ein Grundmuster; Evolution erweitert das Muster (gleiche Grundform) |
| Farbe | Typfarbe als Akzent; erblich über `GEN_SOUNDMARK_COLOR` (K38) |
| Puls | Tempo = Rufprofil (K55 §5, `EchoCalls.csv`); Emotion verändert Tempo und Helligkeit |
| Technik | Emissive-Maske `T_Echo_###_SoundMark` (R Muster, G Phasen-Offset, B Intensität), Parameter `SoundMarkPulse` |
| Morph (1/1024) | Klangmal in Komplementärfarbe + Schimmer; nie Shop (DR-17) |

### 5.3 Emotionen (CD-08)

| Emotion | Körper | Klangmal |
|---|---|---|
| Freude | Offene Haltung, Hüpfer | Schneller, heller |
| Neugier | Kopf schräg, Annäherung | Pulsiert unregelmäßig |
| Angst | Geduckt, Rückzug | Flackert schnell |
| Wut | Aufgerichtet, Drohgebärde | Hell, langsam-stark |
| Trauer | Gesenkter Kopf | Gedimmt |
| Ruhe/Schlaf | Eingerollt | Langsam, schwach |


### 5.4 Gestaltungsbriefe je Region

Die Briefe für das Concept-Team entstehen aus dem Artenkatalog (K20–K27): je Linie die Endstufe mit Klangmal und Signaturkonzept. Die Akzentfarbe ist die finale Typfarbe (§3.1). Auszug (sechs Linien je Region):

**Verdanthain**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Verdrath | Haingeweih-Echo | L (2,2 m) | Blüte `#5DAA4C` / Klang | Geweih aus Ästen mit Glockenblüten; Klangmal als goldenes Rankenmuster, 44 BPM | Hainchor: Crescendo – heilt alle Verbündeten und lässt für 3 Züge Überwuchs wachsen |
| Torgrath | Bergbollwerk-Echo | XL (3,2 m) | Stein `#8C7B65` / Schwerkraft | Schwebende Steinsplitter kreisen um das Klangmal am Nacken; 40 BPM | Bergherz: Crescendo – zieht alle Gegner in die Vorderreihe und senkt ihre Geschwindigkeit |
| Zephyrion | Himmelsfalken-Echo | L (1,9 m) | Sturm `#7FD1E8` / Licht | Klangmal wie ein Kranz aus Windlinien um die Augen, leuchtet im Sonnenlicht; 88 BPM | Himmelssturz: Crescendo – trifft alle Gegner und verschiebt sie auf der Zeitleiste nach hinten |
| Cantaroth | Dirigentenaffen-Echo | L (1,8 m) | Klang `#F2A93B` / Blüte | Lange Arme mit Ringmustern; das Klangmal am Brustkorb dirigiert den Puls der Gruppe | Waldkonzert: Crescendo – synchronisiert alle Verbündeten auf der Zeitleiste (handeln direkt nacheinander) |
| Vernaune | Frühlingshirsch-Echo | XL (3,1 m) | Blüte `#5DAA4C` / Licht | Geweih trägt leuchtende Blütenknospen, die sich im Sonnenlicht öffnen | Frühlingserwachen: Crescendo – entfernt alle Status der eigenen Seite und heilt 25 % |
| Phantalume | Seelenfalter-Echo | M (1,2 m) | Geist `#B7A4E0` / Licht | Der ganze Körper ist ein Klangmal aus Licht; im Nebel verschwimmt er | Seelenleuchten: Crescendo – trifft alle Gegner, Geist-Ziele doppelt geblendet |

**Kharsgrat**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Kraggoth | Bergkrabben-Echo | L (2,8 m) | Stein `#8C7B65` / Metall | Erzadern durchziehen den Panzer und pulsieren rot im Takt | Bergpanzer: Crescendo – Schild für die ganze Seite, Gegner in der Vorderreihe werden zurückgestoßen |
| Ponderath | Schwerkern-Echo | L (2,4 m) | Schwerkraft `#4B5BA6` | Ein dunkler Kern im Inneren, um den Lichtlinien kreisen | Gravitationskern: Crescendo – alle Gegner verlieren 2 GES-Stufen und werden in die Vorderreihe gezogen |
| Forgoth | Ambossdachs-Echo | L (1,8 m) | Metall `#9AA3AD` / Stein | Rücken wie ein Amboss; Klangmal schlägt Funken bei jedem Schritt | Ambossschlag: Crescendo – massiver Metall-Angriff, Ziel erhält 2 Züge Erschüttert |
| Gratrex | Donneradler-Echo | L (2,1 m) | Sturm `#7FD1E8` / Metall | Metallisch glänzende Schwungfedern leiten Blitze; das Klangmal knistert | Donnersturz: Crescendo – trifft alle Gegner, Metall-Ziele erleiden Blitzschlag-Bonus |
| Kiesward | Almwächter-Echo | M (0,9 m) | Stein `#8C7B65` / Klang | Felsplatten am Hals vibrieren sichtbar beim Rufen | Grat-Echo: Klang-Angriff, verzögert Ziel und gibt Verbündeten Harmonie |
| Lithshell | Spiralberg-Echo | L (1,8 m) | Stein `#8C7B65` / Flut | Die Spirale hat sieben Windungen, jede leuchtet in eigenem Takt | Strudelschild: Schild für die Reihe, reflektiert einen Teil des Flut-Schadens |

**Morvenmoor**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Toxmire | Moorkönigs-Echo | M (1,3 m) | Gift `#8E4FB0` / Flut | Krone aus Warzen auf dem Kopf leuchtet in Wellen | Moorkrone: Crescendo – Sumpf-Terrain auf allen Reihen, alle Gegner erhalten 2 Gift-Stapel |
| Undrath | Deltariesen-Echo | L (2,8 m) | Flut `#2E8BC0` / Geist | Barteln wie Geisterlaternen; das Klangmal schimmert durch trübes Wasser | Deltaflut: Crescendo – alle Gegner werden in die Hinterreihe gespült, eigene Seite heilt |
| Irraune | Laternengeist-Echo | M (1,3 m) | Geist `#B7A4E0` / Licht | Ein Kranz aus Laternenlichtern um eine durchscheinende Gestalt | Laternenreigen: Crescendo – trifft alle Gegner, blendet und reinigt die eigene Seite |
| Blossmire | Moorrosen-Echo | L (2,2 m) | Blüte `#5DAA4C` / Gift | Riesige Blüte, deren Blätter wie ein Herz pulsieren | Moorrosenblüte: Crescendo – greift alle Gegner an, heilt um den verursachten Schaden |
| Virwyn | Fieberschwarm-Echo | S (0,7 m) | Gift `#8E4FB0` / Sturm | Der Schwarm formt flügelartige Schleier mit leuchtenden Adern | Fieberwolke: Gift auf eine Reihe, getroffene Gegner verlieren Präzision |
| Blightar | Sumpftentakel-Echo | M (1,4 m) | Gift `#8E4FB0` / Flut | Lange Arme mit Leuchtringen, die im Nebel pulsieren | Tentakelnetz: hält zwei Ziele fest (Zeitleiste +) und vergiftet |

**Sahrun-Weite**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Solaryx | Sonnenkronen-Echo | M (1,3 m) | Licht `#F6D86B` / Glut | Eine Mähne aus Strahlen, die zur Mittagszeit eine Krone bildet | Zenitstrahl: Crescendo – mächtiger Licht-Angriff, bei Sonnenwetter ohne Abklingzeit |
| Dunmarsch | Wüstenkoloss-Echo | XL (3,6 m) | Stein `#8C7B65` / Schwerkraft | Rücken trägt einen Felsgrat, um den Sandkörner schweben | Erdlast: Crescendo – erhöht Schwerkraft auf dem Feld, alle Gegner werden langsamer |
| Skarabon | Sonnenträger-Echo | M (1,2 m) | Schwerkraft `#4B5BA6` / Licht | Zwischen den Vorderbeinen schwebt eine leuchtende Kugel | Sonnenkugel: Crescendo – erzeugt eine schwebende Lichtkugel, die 3 Züge lang Gegner trifft |
| Sengrath | Sandleviathan-Echo | XXL (9,0 m) | Glut `#E8562A` / Stein | Ein Maul aus glühenden Ringen, das beim Auftauchen tief brummt | Glutschlund: Crescendo – verschlingt das Feld, Terrain wird Glutsand (3 Züge) |
| Stacharon | Wüstenskorpion-Echo | M (1,4 m) | Gift `#8E4FB0` / Stein | Steinplatten mit grünen Leuchtadern, Stachel wie ein Glaskolben | Giftzange: hält das Ziel fest; Gift stapelt sich jede Runde |
| Sirrsturm | Sandteufel-Echo | M (1,5 m) | Sturm `#7FD1E8` / Stein | Eine wirbelnde Säule mit zwei glühenden Augenkörnern | Sandteufel: ruft Sandsturm herbei; im Sturm Ausweichen +2 |

**Ignareth**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Pyroluth | Lavamolch-Echo | M (1,4 m) | Glut `#E8562A` / Stein | Haut aus erkaltender Lava, durch deren Risse Glut pulsiert | Lavaflut: Crescendo – Glut-Welle auf alle Gegner, Terrain Glutboden 3 Züge |
| Ambross | Schmiedeherr-Echo | L (2,6 m) | Metall `#9AA3AD` / Glut | Hammerarme, deren Schläge einen tiefen Glockenton erzeugen | Weltamboss: Crescendo – Schild auf alle Verbündeten, Gegner, die ihn treffen, erleiden Rückstoß |
| Aschgrim | Glutwolf-Echo | M (1,2 m) | Glut `#E8562A` / Leere | Rauchmähne, durch die rote Augen glühen | Schattenglut: Crescendo – verschwindet in Rauch und trifft alle Gegner nacheinander |
| Obsidrax | Obsidianfürst-Echo | L (2,4 m) | Stein `#8C7B65` / Kristall | Ein Panzer wie eine Kathedrale aus schwarzem Glas | Obsidianwall: Crescendo – Kristallmauer schützt die eigene Reihe 2 Züge |
| Ignavor | Kraterdrachen-Echo | XL (4,5 m) | Glut `#E8562A` / Schwerkraft | Hörner, um die Schlackebrocken kreisen wie kleine Monde | Kraterlast: Crescendo – Glut-Meteor aus der Höhe, Schwerkraft zieht Gegner nach vorn |
| Fumaroth | Schlotgeist-Echo | M (1,5 m) | Leere `#4A3A6E` / Glut | Rauchmantel mit glimmenden Rändern und einem stummen, offenen Mund | Erstickender Schlot: Gegner können 1 Zug keine Klang-Fähigkeiten nutzen |

**Saltrand**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Maraune | Himmelsrochen-Echo | XL (4,5 m) | Flut `#2E8BC0` / Sturm | Riesige Flossen mit Wellenlinien aus Licht, die im Flug pulsieren | Sturmflut: Crescendo – trifft alle Gegner und spült die Hinterreihe nach vorn |
| Tidrex | Tiefenkraken-Echo | L (2,8 m) | Flut `#2E8BC0` / Arkan | Arme mit Mustern, die an dorunische Glyphen erinnern | Tiefsog: Crescendo – zieht alle Gegner in die Vorderreihe und verlangsamt sie |
| Brision | Albatros-Echo | L (2,0 m) | Sturm `#7FD1E8` / Flut | Spannweite mit Klangmal-Bändern, die im Gegenwind singen | Weltumsegler: Crescendo – alle Verbündeten handeln sofort hintereinander (Zeitleiste) |
| Aquadral | Tiefenlaternen-Echo | L (2,0 m) | Flut `#2E8BC0` / Licht | Dutzende Leuchtpunkte wie ein Sternbild auf dem Körper | Tiefenleuchten: Crescendo – trifft alle Gegner, enthüllt sie (Ausweichen ignoriert) 2 Züge |
| Aerluna | Sturmquallen-Echo | S (0,75 m) | Sturm `#7FD1E8` / Licht | Tentakel aus Licht, die bei Blitzen aufleuchten | Blitzschirm: lädt sich im Gewitter auf, entlädt auf alle Gegner |
| Stonshell | Strandpanzer-Echo | L (1,7 m) | Stein `#8C7B65` / Flut | Riesiger Panzer mit Muscheln, die das Klangmal säumen | Wattpanzer: Schild für die Reihe, Flut-Schaden halbiert |

**Hvitfell**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Snevrik | Firnluchs-Echo | M (1,2 m) | Frost `#C9EEF7` / Licht | Eine Mähne, in der Polarlichtbänder fließen | Polarlichtsprung: Crescendo – springt durch Lichtschleier und trifft jeden Gegner einmal |
| Kjalgrund | Gletscherriesen-Echo | XL (4,2 m) | Frost `#C9EEF7` / Stein | Ein Rücken aus Gletschereis, in dem alte Luftblasen tönen | Gletscherschritt: Crescendo – Eiswall vor der eigenen Reihe, Gegner rutschen nach hinten |
| Uvalis | Ahneneulen-Echo | L (1,7 m) | Frost `#C9EEF7` / Geist | Gefieder, in dem Gesichter von Ahnen schimmern | Ahnenruf: Crescendo – ruft die Stimme eines besiegten Verbündeten zurück (Wiederbelebung 30 %) |
| Lysthane | Himmelsvorhang-Echo | XL (4,8 m) | Licht `#F6D86B` / Klang | Ein Himmelsvorhang, der beim Gleiten hörbar singt | Himmelschor: Crescendo – volle Heilung der Reihe, Harmonie +20 |
| Vardholm | Steinwarten-Echo | L (2,6 m) | Stein `#8C7B65` / Frost | Ein Turm aus Steinen mit einem Eiskern, der nachts blau glimmt | Lawinenschild: schützt die Hinterreihe vor dem nächsten Flächenangriff |
| Eidwacht | Ahnenchor-Echo | M (1,55 m) | Geist `#B7A4E0` / Klang | Mehrere Stimmen gleichzeitig, als sänge ein ganzer Chor | Totenchor: Klang-Angriff, stärker je mehr Verbündete besiegt wurden |

**Ael'Dorun**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Skriveth | Glyphenmeister-Echo | L (2,0 m) | Arkan `#3FB8A8` / Licht | Ein Mantel aus leuchtenden Zeilen, die sich ständig neu schreiben | Weltschrift: Crescendo – schreibt ein Feldzeichen: Arkan-Fähigkeiten aller Verbündeten +1 Stufe |
| Thaelarch | Säulenarchonten-Echo | L (2,8 m) | Geist `#B7A4E0` / Metall | Eine Rüstung aus Bronze und Licht mit einem leeren Helm, aus dem ein Chor tönt | Archontenwall: Crescendo – die eigene Reihe ist 1 Zug unverwundbar gegen Geist und Arkan |
| Tikkoran | Zeitwerk-Echo | M (1,3 m) | Metall `#9AA3AD` / Schwerkraft | Ein Pendel unter dem Körper, das die Luft um sich verlangsamt | Zeitbremse: Crescendo – alle Gegner rücken auf der Zeitleiste um 300 nach hinten |
| Sarkothar | Grabfürsten-Echo | XL (3,4 m) | Geist `#B7A4E0` / Arkan | Eine Krone aus Geisterflammen und ein Siegel auf der Stirn | Fürstenurteil: Crescendo – trifft den stärksten Gegner, Schaden steigt mit dessen Basiswerten |
| Tilgrath | Vergessens-Echo | M (1,4 m) | Leere `#4A3A6E` / Arkan | Tentakel aus schwarzer Leere, über die blasse Buchstaben laufen und verschwinden | Großes Vergessen: alle Gegner verlieren ihre Werteveränderungen |
| Hymnora | Chorlilien-Echo | S (0,75 m) | Klang `#F2A93B` / Geist | Ein Kranz aus Blüten, die mehrstimmig singen | Chorblüte: heilt alle Verbündeten, entfernt einen negativen Status |

**Prismtiefen**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Klirrathan | Kristallschwingen-Echo | L (1,8 m) | Kristall `#E28FC6` / Klang | Schwingen aus Kristallplatten, die wie eine Orgel klingen | Prismenschrei: Crescendo – Klang-Kristall-Welle, alle Gegner −1 Präzision und Ausweichen |
| Spathorn | Geodenwurm-Echo | XL (4,5 m) | Kristall `#E28FC6` / Schwerkraft | Ein Körper wie eine aufgebrochene Geode, innen voller leuchtender Kristalle | Geodenkern: Crescendo – hüllt die eigene Reihe in eine Geode (Schild, VER/SVE +1) |
| Ligravor | Schachtweberinnen-Echo | L (2,2 m) | Schwerkraft `#4B5BA6` / Kristall | Ein Netz aus Kristallfäden über dem Rücken, das bei Bewegung klingt | Schwerenetz: Crescendo – alle Gegner gebunden, ihre Geschwindigkeit sinkt um 2 Stufen |
| Facettor | Prismakatzen-Echo | S (0,7 m) | Kristall `#E28FC6` / Licht | Ein Fell aus Kristallfacetten, das Licht wie ein Kronleuchter streut | Prismastrahl: teilt einen Licht-Angriff auf bis zu 3 Ziele |
| Mullhorn | Bohrmull-Echo | M (0,9 m) | Metall `#9AA3AD` / Stein | Ein spiralförmiges Metallhorn auf der Schnauze | Bohrhorn: durchdringender Angriff, ignoriert VER-Erhöhungen |
| Missgrath | Riss-Echo | M (1,5 m) | Leere `#4A3A6E` / Kristall | Ein Kristallsplitter mit einem schwarzen Riss, aus dem kein Ton dringt | Weltriss: ändert das Feld zu Missklang-Terrain (Harmonie-Gewinn halbiert, 3 Züge) |

**Nimbara**

| Art | Kategorie | Größe | Typ (Akzentfarbe) | Klangmal | Signaturkonzept |
|---|---|---|---|---|---|
| Nimbaroth | Himmelswal-Echo | XXL (12,0 m) | Sturm `#7FD1E8` / Schwerkraft | Ein Körper so groß wie eine Insel, auf dessen Rücken Gärten wachsen | Himmelslast: Crescendo – senkt die Schwerkraft des Feldes, Verbündete +2 GES |
| Cirrhaven | Sturmfalken-Echo | L (1,9 m) | Sturm `#7FD1E8` / Licht | Schwingen, die Lichtbahnen in die Wolken schneiden | Himmelsschnitt: Crescendo – drei Sturzflüge auf zufällige Gegner, jeder kritisch bei Gewitter |
| Nubiluna | Himmelsherden-Echo | M (1,5 m) | Licht `#F6D86B` / Klang | Ein strahlender Wolkenleib, der ein Wiegenlied summt | Wiegenlied der Wolken: Crescendo – volle Heilung aller Verbündeten, Gegner schläfrig |
| Harfion | Windharfner-Echo | M (1,0 m) | Klang `#F2A93B` / Sturm | Ein Federfächer wie eine Windharfe, der im Sturm volle Akkorde spielt | Äolsakkord: Verbündete erhalten Harmonie +10, Gegner −1 Präzision |
| Tintabul | Glockenqualle-Echo | M (1,5 m) | Klang `#F2A93B` / Licht | Ein Glockenschirm aus Licht, dessen Läuten man im Brustkorb spürt | Großes Geläut: Klang-Angriff auf alle Gegner, erweckt schlafende Verbündete |
| Holmgard | Inselschildkröten-Echo | XL (3,5 m) | Schwerkraft `#4B5BA6` / Stein | Ein Panzer wie eine kleine Insel mit eigenem Baum | Inselgewicht: erhöht die Schwerkraft; Flug-Echos verlieren ihren Ausweichbonus |

---

## 6. Menschen und Kleidung

| Gruppe | Silhouette | Materialien | Farbe | Erkennungszeichen |
|---|---|---|---|---|
| Wildwacht | Kapuzenmantel, Gürteltaschen | Wolle, Leder | Moosgrün `#4F7A3A` + Braun | Wappen (Blatt im Ring) |
| Akademie | Lange Roben, Kragen | Leinen, Seide | Tiefblau `#3D5A99` | Messinstrumente, Glyphen-Spangen |
| Goldklang-Kontor | Westen, Ärmelschoner | Brokat, Baumwolle | Gold `#C9A227` | Waagen-Brosche |
| Freie Stimmen | Gewickelte Tücher, Schichten | Flicken, Leinen | Rostrot `#A0442E` | Echo-Halstücher (befreite Echos) |
| Orden der Stille | Schweigegewand, Schleier | Grauer Filz | Grau `#8A8F99` | Schiefertafel am Gürtel |
| Regionale Tracht | je Region (§7) | regional | Regionspalette | – |

Die Fraktionsfarben stammen aus `Factions.csv` (K47). **Spieler-Charakter:** Wärterausrüstung (K40) prägt die Silhouette (Resonator am Gürtel, Gleiter als Rucksack), Kleidung wechselt mit Ausrüstungsstufen; Kosmetik nur aus Spiel (Ruf, Quests) – DR-17.

**Gesichter:** stilisiert-realistisch, große Mimik-Lesbarkeit (Dialogkamera), vielfältige Ethnien ohne Abbild realer Kulturen; Sensitivity-Review für R04/R07 (CANON §22).

---

## 7. Architektur und Kulturen

| Region | Kultur | Architektur | Klangmotiv |
|---|---|---|---|
| Verdanthain | Linnisch | Fachwerk um lebende Bäume, Wurzelarena unter der Riesenlinde | Holzresonanz, Windspiele |
| Kharsgrat | Kharsk | Steintürme wie Orgelpfeifen, Kettenbrücken, Ahnenfelsen | Pfeifen im Wind |
| Morvenmoor | Morvisch | Stelzenhäuser, Laternenstege, Unterstadt | Wasserglocken |
| Sahrun-Weite | Sahrunisch | Sonnenhöfe, Glasdächer, Lehm, Treppen der tausend Stufen | Glas, das in der Sonne singt |
| Ignareth | Ignar | Terrassen, Essen, Schlackenmauern, Zunfthallen | Ambosse, Glocken |
| Saltrand | Saltisch | Hafenkontore, Schleusen, Leuchttürme | Tauwerk, Bojenglocken |
| Hvitfell | Hvitnisch | Langhäuser, Holzrot, Kloster aus grauem Stein | Stille, Schnee |
| Ael'Dorun | Dorunisch (alt) | Säulenstädte, Glyphenwände, Thronsaal | Hall, Kanon |
| Prismtiefen | Prismanisch | Glasstadt im Krater, Lichtschächte | Licht = Ton |
| Nimbara | Nimbari | Schwebende Werften, Windanker, Gärten | Wind, Chöre |

**Regel:** Jede Kultur hat einen **Modulsatz** (Wände, Dächer, Fenster, Türen, Requisiten, Trim-Sheets) und **ein** wiederkehrendes Klangmotiv in der Architektur (Resonanzringe, Pfeifen, Glocken, Glas) – „Gesungene Welt“.

---

## 8. Umwelt und Lesbarkeit

| Element | Regel |
|---|---|
| Kletterflächen | Natürliche Markierung durch Flechten/Kanten in Flechtengelb-ähnlichem Ton; nie Farbstreifen |
| Grabbare Böden | Lockere Textur, kleine Sandfälle (Grabreiten, K40) |
| Gleitstarts | Windfahnen, Felsnasen, aufsteigende Blätter |
| Interaktion | Leichter Glanz + Glyphe bei Annäherung (K54 HUD_INTERACT) |
| Gefahr | Lava, Abgründe, Stillezonen: Farbe + Form + Klang (DR-24) |
| Drei-Ding-Regel | Je 300 m drei ungeplante Angebote (DR-26) – Art setzt Blickfänger (Landmarken, Licht, Bewegung) |
| Wegfindung | Landmarken je Region (Riesenlinde, Grollhorn, Versunkener Turm, Sonnenhof, Krater, Leuchtfelsen, Isvaldtind, Thronstadt, Kraterrand, Kronenwerft) aus jeder Zone sichtbar |
| PCG | Schichten `PCG_R##_<Layer>` (CANON §46), Editorzeit gebacken; Handarbeit für Pfade und Landmarken |

---

## 9. Stille, Sturm, Enden

| Zustand | Bild |
|---|---|
| Stillezone | Entsättigung bis 90 % (`MPC_Silence`), Partikel erstarrt, Echos grau mit erloschenem Klangmal; Ränder als graue Adern im Boden |
| Heilung | Farbe kehrt in einer Welle vom Zentrum zurück (4 s), Klangmale entzünden sich nacheinander |
| Orte der Pause | Kreisrunde Fläche, in der Staub in der Luft stillsteht, im Takt der 1-s-Stille (K55 §8) |
| Resonanzsturm | Himmel pulsiert, Klangmale synchron, leichte chromatische Aberration (abschaltbar) |
| Krone | Unnatürliche Symmetrie, kaltes Weiß, alle Klangmale gleich (Unisono) |
| Velnox | Negativraum: Bereiche, in denen Licht „aufhört“ (Lumen-Ausschluss), Ränder mit feinem Glanz |
| Neues Lied | Grün geheilte Zonen, Aurora in zehn Farben, Klangmale heller |
| Sanfte Stille | Silberner Schleier, befriedete Zonen silbern statt grau, Klangmale ruhig |

---

## 10. Asset-Regeln und Budgets

| Name | Kind | TrisLOD0 | Nanite | Textures | LOD | Notes |
|---|---|---|---|---|---|---|
| Echo Stufe 1 (XS–M) | Skeletal | 18.000 | Nanite nein (Skinned) | 2× 2K (Basis, Klangmal-Maske) | LOD 4 | Klangmal als Emissive-Maske (K16 §3) |
| Echo Stufe 3 / L–XL | Skeletal | 45.000 | nein | 2× 4K | LOD 5 | Reitbar ab L (CD-17) |
| Ursprungsstimme / Mythisch | Skeletal | 90.000 | nein | 3× 4K | LOD 6 | Nur in eigenen Arenen/Begegnungen gleichzeitig |
| Benannter NPC | Skeletal (MetaHuman-ähnlich, eigener Stil) | 60.000 | nein | Körper 4K, Gesicht 4K | LOD 5 | Kleidung modular (Fraktion, Region) |
| Ambient-NPC (Mass) | Skeletal + Vertex-Animation | 12.000 | nein | 1× 2K Atlas | LOD 3 + Impostor | Crowd-Varianten 12 je Region |
| Architektur-Modul | Statisch | beliebig | Nanite ja | Material-Layering, 4K Trim-Sheets | Nanite | Je Kultur ein Modulsatz (§7) |
| Vegetation | Statisch/Foliage | Nanite Foliage | ja (UE 5.6) | 2K Atlas | Nanite + WPO | Budget K09: PS5 ≤ 1,6 Mio. Instanzen |
| Requisite klein | Statisch | Nanite | ja | 1K–2K | Nanite | Trim-Sheets bevorzugt |
| Hain-Dekor | Statisch | 20.000 | ja | 2K | Nanite | Decor.csv (K49–K51) |

| Regel | Inhalt |
|---|---|
| Texeldichte | Welt 10,24 px/cm (Nahbereich 20,48 für Hero-Assets); Echos 20,48 |
| Materialien | Master-Materialien je Kategorie (Echo, Umwelt, Architektur, Charakter); Instanzen statt neuer Shader; Klangmal-Funktion als Material Function |
| Benennung | Präfixe CANON §23 (SM_, SK_, SKEL_, M_/MI_, T_ mit _D/_N/_ORM/_E/_M, NS_, PCG_) |
| Nanite | Statische Geometrie und Foliage; Skeletal ohne Nanite |
| Lumen | Kein vorgebackenes Licht in der offenen Welt; Innenräume mit Lumen + lokalen Lichtern |
| Switch 2 | Eigenes Profil: Lumen-Ersatz (SSGI + Lightprobes), reduzierte Foliage (≤ 400 k Instanzen), Texturen eine Stufe kleiner (K65) |

---

## 11. Clean-Room und Referenzen

DR-22 (unverhandelbar) und CD-03 verlangen eigene Gestaltung:

| Erlaubt | Verboten |
|---|---|
| Natur, Tiere, Pflanzen, Mineralien, Musikinstrumente, Architekturgeschichte als **allgemeine** Referenz | Nachbildung von Figuren, Kreaturen, Logos, Symbolen anderer Spiele/Medien |
| Eigene Fotos, Exkursionen, Museen | Moodboards mit Screenshots anderer Monstersammelspiele |
| Musiktheorie, Akustik, Wellenbilder | „Element-Tier“-Muster (Feuerfuchs, Wassertaube …) ohne zweite Gestaltungsachse |

Jedes Konzept durchläuft den **Ähnlichkeitstest** (CD-01-Formvektor gegen den eigenen Katalog) und eine **Clean-Room-Erklärung** der Konzeptkünstlerin bzw. des Konzeptkünstlers (keine fremden Vorlagen genutzt). Konzeptdateien werden mit Quellenvermerk archiviert.

---

## 12. Review-Prozess

```
Brief (Datenblatt K16) → Thumbnails (12–20 Silhouetten) → Silhouettentest CD-01 → Farbskizze (≤ 3 + Klangmal)
  → Art-Review (Säulen, Lesbarkeit, Clean-Room) → Modell/Blockout → In-Engine-Test (30 m, Nacht, Nebel, Farbenblind)
  → Animation-Review (Emotionen, Ruf-Sync) → Final → Kodex-Fotografie-Test (K39)
```

**Automatische Prüfungen:** `aethris_palette.py` (AR-01 Mindestabstände aller Typfarben je Modus, AR-02 Kontrast zum UI-Grund) – **0 Verstöße**; Silhouetten-Formvektoren (CD-01) im Katalog-Validator (K16).

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Technical Art | Master-Materialien, Klangmal-Function, `MPC_Silence`, Heilungswelle, Velnox-Negativraum | K57, K58 |
| Animation | Emotionen (6), Rufe synchron zum Klangmal, Erschöpfung (Klangmal erlischt) | K57 |
| UI | Typfarben und Farbenblind-Paletten aus `TypeColors.csv` als Token-Sätze | K54 |
| Audio | Klangmotiv je Kultur (Architektur) und Klangmal-Tempo abgestimmt | K55 |
| Level Design | Landmarken-Sichtachsen, Signaturfarbe je Region, Lesbarkeitsregeln §8 | K57 |
| Plattformen | Switch-2-Profil (§10) | K65 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-216 | Typfarben final nach CIEDE2000-Prüfung; Leere und Frost angepasst | Messbare Unterscheidbarkeit, Lesbarkeit auf UI-Grund | Arbeitsstand unverändert |
| ADR-217 | Farbenblind-Paletten werden generiert (Helligkeitsspreizung), nicht handgemalt | Nachweisbare Mindestabstände je Modus, reproduzierbar | Handpaletten ohne Messung |
| ADR-218 | Typfarbe an Echos nur als Akzent; Grundfarben aus Lebensraum | CD-02, Vielfalt, kein „Element-Tier“ | Typfarbe als Körperfarbe |
| ADR-219 | Jede Region hat eine exklusive Signaturfarbe | Orientierung, Regionsidentität | geteilte Paletten |
| ADR-220 | Klangmale sind Lichtquellen der Nacht | Lesbarkeit bei Nacht ohne künstliche Aufhellung; Thema „Klang = Licht“ | hellere Nächte |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §217 | Art-Säulen (Gesungene Welt, Staunen vor Nähe, Wärme mit Wehmut, Lesbar zuerst, Würde statt Grausamkeit); stilisierter Realismus; Formsprache je Typ | LOCKED |
| §218 | Typfarben final (`TypeColors.csv`): wie CANON §78, außer Leere `#4A3A6E`, Frost `#C9EEF7`; Farbenblind-Paletten Protan/Deutan/Tritan generiert; ΔE2000 ≥ 10 (normal), ≥ 6 (simuliert) | LOCKED (ersetzt Arbeitsstand §78) |
| §219 | Kreaturen (CD-Regeln, Klangmal-Spezifikation, Emotionen), Menschen/Kleidung (Fraktionsfarben), Architektur je Kultur mit Klangmotiv, Regionspaletten mit Signaturfarbe | LOCKED |
| §220 | Licht- und Wetterregeln, Klangmale als Nachtlicht; Bildsprache für Stille, Heilung, Sturm, Krone, Velnox, Enden | LOCKED |
| §221 | Asset-Budgets (`AssetBudgets.csv`), Texeldichte, Material- und Benennungsregeln, Clean-Room-Verfahren, Review-Prozess | LOCKED |
| §10 | ADR-216 – ADR-220 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Art-Säulen, Stil, Formsprache je Typ
- [x] Typfarben final mit Messung, Farbenblind-Paletten, Nutzung
- [x] Regionspaletten mit Signaturfarbe, Farbskript der Story
- [x] Licht, Wetter, Tageszeit
- [x] Kreaturen, Klangmal, Emotionen
- [x] Menschen, Kleidung, Architektur je Kultur
- [x] Umwelt-Lesbarkeit, Stille/Sturm/Enden
- [x] Asset-Budgets, Clean-Room, Review-Prozess, Prüfer (0 Verstöße)
- [x] Anforderungen, ADR-216 – ADR-220, CANON §217–§221

➡️ **Nächstes Kapitel: K57 – Asset-Pipeline, Animation und Technical Art.**
