# K57 · Asset-Pipeline, Animation und Technical Art

| Feld | Wert |
|---|---|
| Dokument | Kapitel 57 von 68 · Präsentation IV |
| Version | 1.0 |
| Owner | Technical Art Director, Animation Director |
| Mitwirkende | Lead Technical Artist, Lead Animator (Kreaturen), Lead Animator (Menschen), Rigging Lead, Tools Programmer, Build Engineer, Outsourcing Manager, Lead Environment Artist |
| Baut auf | K04 §7–§9 (Benennung, CANON §23), K05 (Repository, Module, CI, CANON §25–§28), K06 §2–§3 (Datenpipeline, CANON §31), K08 §10 (World Partition, CANON §43), K09 (PCG, Foliage-Budget), K16 (Archetypen, Klangmal, ADR-074), K52 (Mass-Ökologie, ADR-200), K53 (NPC-Aktivitäten), K55 (Rufe, Quartz), K56 (Art Bible, Budgets, CANON §217–§221) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Anim/AnimCategories.csv`, `Data/Anim/HumanAnimSets.csv`, Referenzmodell `tools/ref/aethris_anim.py`, Editor-Validator `Source/AethrisEditor/…/Validation/AethrisAssetNamingValidator.h/.cpp` |
| Neue Kanon-Einträge | CANON §222 (Pipeline und Ordner), §223 (Kreatur-Rigs und Animationsumfang), §224 (Menschliche Animation), §225 (Technical Art), §226 (Validierung und Abnahme); CR-006 (erste CSV-Spalte `Name`) |

---

## Inhalt

1. [Ziele und Grundsätze](#1-ziele-und-grundsätze)
2. [Pipeline-Überblick](#2-pipeline-überblick)
3. [Ordner, Benennung, Versionierung](#3-ordner-benennung-versionierung)
4. [Datenpipeline und Importer](#4-datenpipeline-und-importer)
5. [Kreaturen-Pipeline](#5-kreaturen-pipeline)
6. [Kreatur-Animation](#6-kreatur-animation)
7. [Menschliche Animation und Zwischensequenzen](#7-menschliche-animation-und-zwischensequenzen)
8. [Technical Art: Materialien und Shader](#8-technical-art-materialien-und-shader)
9. [Welt-Pipeline: PCG, World Partition, HLOD](#9-welt-pipeline-pcg-world-partition-hlod)
10. [Validierung und Werkzeuge](#10-validierung-und-werkzeuge)
11. [Produktionsumfang und Schätzung](#11-produktionsumfang-und-schätzung)
12. [Externe Partner und Abnahme](#12-externe-partner-und-abnahme)
13. [Risiken](#13-risiken)
14. [Anforderungen an andere Abteilungen](#14-anforderungen-an-andere-abteilungen)
15. [Decision Records](#15-decision-records)
16. [Kanon-Änderungen](#16-kanon-änderungen)
17. [Kapitel-Checkliste](#17-kapitel-checkliste)

---

## 1. Ziele und Grundsätze

AETHRIS hat 256 Echo-Arten, 194 benannte NPCs, eine offene Welt von 8,1 × 7,1 km mit zehn Regionen und rund 70 Zwischensequenzen. Ein Team in der Größe eines mittleren AAA-Studios (K67) kann diesen Umfang nur liefern, wenn die Pipeline drei Dinge leistet: **Wiederverwendung** (Archetyp-Skelette, geteilte Animationssätze, Master-Materialien), **Automatisierung** (Importer, Validatoren, generierte Daten) und **frühe Fehlererkennung** (Prüfungen vor dem Einreichen statt im Playtest).

| Grundsatz | Bedeutung | Messbar an |
|---|---|---|
| **TA-01 Daten zuerst** | Jede Spielinformation (Werte, Zuordnungen, Budgets) liegt in `Data/**/*.csv`; Assets enthalten nur Darstellung | Kein Gameplay-Wert in einem Blueprint-Default (Validator) |
| **TA-02 Wiederverwendung vor Einzelstück** | Neue Art = vorhandenes Archetyp-Skelett + geteilte Clips + Signaturen | ≤ 6 eigene Clips je Art (Crescendo, Ruf-Variante, Spezialbewegung) |
| **TA-03 Ein Weg ins Spiel** | Jedes Asset gelangt über genau einen Importpfad ins Projekt (DCC-Export → Import-Preset → Validator) | 0 manuell importierte Assets in `/Game/Aethris` |
| **TA-04 Prüfen vor dem Einreichen** | Benennung, Budgets, Referenzen, Texturen werden lokal und in CI geprüft | Validator-Verstöße blockieren den Submit |
| **TA-05 Lesbarkeit vor Detail** | Art-Säule „Lesbar zuerst“ (CANON §217) gilt auch technisch: Silhouette und Klangmal bleiben auf jeder LOD-Stufe erhalten | LOD-Test 30 m / 80 m / 150 m |
| **TA-06 Plattform von Anfang an** | Jedes Asset hat ein Switch-2-Profil ab dem ersten Import, nicht erst in der Portierung | Profil-Spalte in `AssetBudgets.csv` |
| **TA-07 Reproduzierbar** | Generierte Inhalte (PCG, Rufprofile, Typfarben) entstehen aus Daten und Saat, nicht von Hand | Neu-Generierung ergibt bitgleiches Ergebnis |

Diese Grundsätze sind keine Stilfragen: Sie bestimmen, ob 1.035 Kreatur-Clips (§6) und rund 1.000 menschliche Clips (§7) im Zeitplan K67 machbar sind.

---

## 2. Pipeline-Überblick

```
                     ┌────────────────────────── Git (P1) / Perforce //Aethris/Main (ab P2, Juli 2027) ──────────────────────────┐
                     │                                                                                                           │
 Konzept (K56) ──► DCC-Quelle (.blend/.ma/.ztl/.spp, Quellordner `Art/Source/…`) ──► Export (FBX/USD, Skript-Preset) ──► Import  │
                     │                                                                                     │                      │
 Data/**/*.csv ──► data_lint.py ──► AethrisCsvImport (Commandlet) ──► Definitionen (DA_, gesperrte Felder) │                      │
                     │                                                         │                           ▼                      │
                     │                                                         └──────► Asset-Referenzen ◄── Validatoren (§10)   │
                     │                                                                         │                                  │
                     │                                                         Cook (Horde, je Plattform) ──► Build-Tests ──► QA │
                     └───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

| Stufe | Werkzeug | Verantwortlich | Prüfung | Ausgabe |
|---|---|---|---|---|
| Konzept | Zeichenprogramm, K56-Brief | Concept Art | Silhouette CD-01, Clean-Room-Erklärung | Konzeptblatt mit Quellenvermerk |
| Sculpt/Modell | ZBrush, Blender, Maya | Creature/Env/Character Art | Formvektor, Proportionen K16 | Hochpoly, Niedrigpoly, UV |
| Textur | Substance Painter/Designer | Texture Art | Texeldichte, Kanalpacking ORM | `T_*_D/_N/_ORM/_E/_M` |
| Rig | Maya (Archetyp-Rig) | Rigging | Skelett = `SKEL_Arch_*`, Zusatzknochen nur in freigegebenen Slots | Rig-Szene |
| Animation | Maya/MotionBuilder, Mocap | Animation | Clipliste je Archetyp (§6), Wurzelbewegung | `AS_*` (FBX) |
| Export | Skript `aethris_export` (DCC-Plugin) | Technical Art | Pfad, Name, Skalierung (1 uu = 1 cm), Achsen | FBX/USD im Austauschordner |
| Import | Interchange-Presets je Asset-Klasse | Technical Art | Präfix, Ordner, LOD-Gruppe, Kompression | Unreal-Assets |
| Integration | Blueprints, Definitionen | Design/Programmierung | DD-01–DD-04 | Spielbar im Testlevel |
| Validierung | Data Validation, Commandlets | alle | §10 | Grün im Pre-Submit |
| Cook | Horde, UAT | Build Engineering | Cook-Fehler, Größenbericht | Paket je Plattform |

**Austauschformat:** FBX für Skeletal Meshes und Animationen (bewährte Tooling-Kette), **USD** für Umgebungsset-Dressing und Kamera-/Layout-Übergaben aus Previs (Sequencer-Import). Alembic nur für vorgerechnete Einzelfälle (Velnox-Negativraum K58, Kristallbruch Krone) – Ausnahmeliste mit Freigabe.

---

## 3. Ordner, Benennung, Versionierung

### 3.1 Inhaltsordner

```
/Game/Aethris/
├── Core/                      Master-Materialien, Material Functions, MPCs, Post-Process, Lichtprofile
├── Echos/
│   ├── _Shared/               SKEL_Arch_* (18), ABP_Echo_Base, geteilte AS_ je Archetyp, Blend Spaces
│   │   └── A01_QuadLight/ …  A18_Climber/
│   └── ECHO_001_Fernlit/      SK_, MI_, T_, AS_ (Signaturen), NS_ (Klangmal-Partikel), DA_ (Darstellung)
├── Characters/
│   ├── Player/                SK_Player_*, Motion-Matching-Datenbank, Garderobe (K42)
│   ├── NPC/                   SK_NPC_Body_* (8 Körper), Köpfe, Kleidungsmodule je Kultur
│   └── Story/                 Hauptfiguren (Kael, Ilen, Sereth, Venn, Tavesh …)
├── World/
│   ├── Regions/R01_Verdanthain/ … R10_Aerion/   Kits, PCG_R##_*, Landmarken
│   ├── Kits/                  Architektur-Kits je Kultur (K56 §7)
│   └── Foliage/               Nanite-Foliage, Gras
├── VFX/                       NS_ (K58)
├── Audio/                     MSS_, SW_ (K55)
├── UI/                        WBP_, Tokens (K54)
├── Cinematics/                LS_ (Level Sequences) je Szene SC_###
└── Data/                      DA_/DT_ aus dem CSV-Import (nicht von Hand bearbeiten)
```

Quelldateien der DCC-Werkzeuge liegen **außerhalb** des Unreal-Projekts in `Art/Source/<gleicher Pfad>` (Perforce, typengesteuert gesperrt, exklusives Auschecken für Binärformate). Damit ist jede `uasset` über den Pfad eindeutig ihrer Quelle zugeordnet.

### 3.2 Benennung

Es gelten die Präfixe aus CANON §23. Ergänzend für die Pipeline:

| Asset-Art | Muster | Beispiel |
|---|---|---|
| Echo-Mesh | `SK_ECHO_###_<Name>` | `SK_ECHO_001_Fernlit` |
| Archetyp-Skelett | `SKEL_Arch_<Archetyp>` | `SKEL_Arch_QuadLight` |
| Geteilter Clip | `AS_Arch_<Archetyp>_<Kategorie>_<Clip>` | `AS_Arch_QuadLight_LOCO_RunLoop` |
| Signatur-Clip | `AS_ECHO_###_<Kategorie>_<Clip>` | `AS_ECHO_001_CRESCENDO_Lindgold` |
| Montage | `AM_<Kontext>_<Name>` | `AM_Echo_Bond_PerfectStrike` |
| Anim Blueprint | `ABP_<Bereich>_<Name>` | `ABP_Echo_Base`, `ABP_Player` |
| Material | `M_<Kategorie>_Master` / `MI_<Asset>_<Variante>` | `M_Echo_Master`, `MI_ECHO_001_Fernlit_Shiny` |
| Material Function | `MF_<Name>` | `MF_Klangmal` |
| Textur | `T_<Asset>_<Suffix>` | `T_ECHO_001_Fernlit_ORM` |
| Partikel | `NS_<Kontext>_<Name>` | `NS_Echo_KlangmalPulse` |
| PCG-Graph | `PCG_R##_<Layer>` | `PCG_R01_Canopy` |
| Level Instance | `LI_<Region>_<Name>` | `LI_R01_Eichenhall_Markt` |
| Level Sequence | `LS_SC_###_<Name>` | `LS_SC_012_Lindenfest` |

Der Editor-Validator `UAethrisAssetNamingValidator` (§10) prüft Präfix je Klasse, Texturen-Suffix und den Ordner `/Game/Aethris`. Abweichungen sind Fehler, nicht Warnungen.

### 3.3 Versionierung und Sperren

| Phase | System | Regel |
|---|---|---|
| P1 (bis Juni 2027) | Git (dieses Repository) + Git LFS für Testassets | Nur Code, Daten, Tools, Dokumente; Art-Prototypen außerhalb |
| ab P2 (Juli 2027) | Perforce `//Aethris/Main`, Streams `Dev-Combat|Echos|World|Story|Online`, `Release-1.0` (CANON §25) | Binärdateien exklusiv gesperrt (`+l`); One File Per Actor für World Partition; Unreal Revision Control Plugin |
| immer | `docs/` bleibt in Git | Spezifikation getrennt vom Inhalt |

**Commit-Marker** (CANON §25) erweitert um `[ART-BULK]` für Massenänderungen (> 200 Assets, z. B. Neu-Import nach Exporter-Update): verlangt Ankündigung im Kanal und Rebuild-Fenster nachts, damit HLOD- und Shader-Caches nicht tagsüber invalidiert werden.

---

## 4. Datenpipeline und Importer

Die Datenpipeline aus K06 (CANON §31) ist für Art und Animation die Brücke zwischen Design und Darstellung: `Species.csv` legt für jede Art Archetyp, Größe, Klangmal-Tempo und Reitart fest; daraus erzeugt der Importer die Darstellungs-Definition (`DA_EchoPresentation_###`) mit Verweisen auf Mesh, Skelett, Clip-Sätze und Materialinstanz.

```
Species.csv ─┬─► UEchoSpeciesDefinition (Spielwerte)
             └─► UEchoPresentationFragment
                    Mesh        = /Game/Aethris/Echos/ECHO_###_<Name>/SK_ECHO_###_<Name>
                    Skeleton    = SKEL_Arch_<Archetyp>          (aus Archetype)
                    AnimSets    = geteilt(Archetyp) + Signaturen (aus SignatureConcept)
                    Material    = MI_ECHO_###_<Name>            (Klangmal-Parameter aus SoundMark)
                    CallProfile = Data/Audio/EchoCalls.csv       (K55)
                    TypeColor   = Data/Art/TypeColors.csv        (K56, nur Akzent)
```

**Klangmal-Parameter aus Daten:** Das Tempo im Feld `SoundMark` (z. B. „52 BPM“) wird zum Materialparameter `KlangmalBPM`; die Pulsfrequenz im Shader ist `BPM/60` Hz. Dieselbe Zahl steuert den Ruf (K55) – Bild und Klang sind dadurch synchron, ohne dass jemand zwei Werte pflegt.

### 4.1 CR-006: erste CSV-Spalte heißt `Name`

CANON §31 schreibt „erste Spalte `Id`“ vor. In allen seit K16 entstandenen Dateien (`Species.csv`, `Abilities`, `Items`, `Quests`, `Npcs`, `Audio`, `Art`, `Anim` …) heißt die erste Spalte jedoch **`Name`** und trägt die stabile ID (`ECHO_###`-Form wird als Kodexnummer separat geführt, Arten tragen ihren internen Namen). `data_lint.py`, die Referenzmodelle und alle generierten Kapitel lesen bereits `Name`. Statt über hundert Dateien umzubenennen, wird der Kanon angepasst:

| Punkt | Festlegung |
|---|---|
| Spaltenname | Erste Spalte heißt `Name` und ist der Primärschlüssel (eindeutig, unveränderlich, nie wiederverwendet → `RetiredIds.csv`) |
| Importer | `AethrisCsvImport` liest Spalte 1 als `PrimaryAssetId`-Namen, unabhängig von der Überschrift; Überschrift `Id` bleibt als Alias gültig |
| Anzeige | Anzeigenamen stehen nie in `Name`, sondern in `DisplayName` bzw. String Tables |
| Prüfung | `data_lint.py` DL-UNQ (Eindeutigkeit Spalte 1), DL-COL (Spaltenanzahl je Zeile) |

### 4.2 Importer-Kette

| Schritt | Commandlet / Werkzeug | Läuft | Fehlerfall |
|---|---|---|---|
| 1 Lint | `tools/data_lint.py` | lokal, Pre-Submit, CI | Abbruch, Zeile und Regel |
| 2 Generatoren | `gen_catalog.py`, `aethris_music.py build`, `aethris_palette.py build`, `aethris_ecology.py build` | bei Datenänderung | Diff in generierten CSVs muss mit eingereicht werden |
| 3 Import | `AethrisCsvImport -Domain=Echos|Abilities|Items|Quests|World|UI|Audio|Art|Anim` | Editor, CI | Definition bleibt alt, Fehlerbericht |
| 4 Referenzauflösung | `AethrisResolveRefs` | nach Import | fehlende Assets als „Platzhalter“ markiert (Testbuild erlaubt, Release nicht) |
| 5 Validierung | Data Validation (alle `UEditorValidatorBase`) | Pre-Submit, nächtlich voll | Submit blockiert |

**Platzhalter-Regel:** Fehlt das Mesh einer Art, setzt der Importer das Archetyp-Grauzeug `SK_Arch_<Archetyp>_Proxy` in der richtigen Größe (aus `HeightM`) ein. So ist jede der 256 Arten ab dem ersten Datenimport spielbar und kampftauglich, lange bevor sie modelliert ist. Der nächtliche Bericht zählt Platzhalter je Region – eine der wichtigsten Fortschrittskurven der Produktion (K67).

---

## 5. Kreaturen-Pipeline

### 5.1 Ablauf je Art

```
Datenblatt (Species.csv, K16) ─► Konzept (12–20 Silhouetten, CD-01) ─► Farbskizze (≤ 3 + Klangmal)
 ─► Proxy im Spiel (Archetyp-Grauzeug, ab Tag 1)
 ─► Sculpt (Hochpoly) ─► Retopologie (Budget §5.3) ─► UV (Texeldichte 20,48 px/cm)
 ─► Skinning auf SKEL_Arch_* (+ max. 12 freigegebene Zusatzknochen) ─► Texturen (D/N/ORM/E/M)
 ─► Geteilte Clips testen (Retargeting-Prüfung) ─► Signaturen animieren ─► Klangmal-Material
 ─► In-Engine-Review (30 m, Nacht, Nebel, Farbenblind) ─► Evolution-Übergang mit Ziel-/Vorform ─► Final
```

| Schritt | Ø Aufwand (Personentage) Stufe 1 | Stufe 2/3 | Legendär/Mythisch |
|---|---|---|---|
| Konzept | 3 | 4 | 8 |
| Sculpt + Retopo + UV | 5 | 7 | 14 |
| Texturen | 3 | 4 | 8 |
| Skinning, Zusatzknochen | 1,5 | 2 | 5 |
| Signaturen + Anpassung geteilter Clips | 3 | 4 | 10 |
| Material, Klangmal, VFX-Anbindung | 1 | 1,5 | 4 |
| Review, Korrekturen | 1,5 | 2 | 4 |
| **Summe** | **18** | **24,5** | **53** |

### 5.2 Archetyp-Skelette und Retargeting

Die 18 Archetypen (CANON §70, ADR-074) sind die Rig-Grundlage. Jede Art nutzt genau ein Archetyp-Skelett; Proportionen werden über **Retarget-Profile** (IK Retargeter, UE 5.6) und Knochen-Skalierung angepasst, nicht über neue Skelette.

| Element | Regel |
|---|---|
| Kernknochen | Fest je Archetyp (z. B. A01: Becken, 3 Wirbel, Hals 2, Kopf, Kiefer, 4 Beine à 4, Schwanz 6) |
| Zusatzknochen | Max. 12 je Art in freigegebenen Slots (`extra_00` – `extra_11`): Ohren, Flossen, Kämme, Klangmal-Organe; Animation über Physik/Control Rig, nicht über geteilte Clips |
| Größenbereich | XS–XXL über Skalierung; Schrittlänge und Wurzelgeschwindigkeit skaliert mit `HeightM` (Stride Warping) |
| IK | Fuß-IK (Boden), Blick-IK (Kopf/Augen), Flügel-IK für A05/A06/A15 |
| Physik | Physics Asset je Art (Kapseln aus Archetyp-Vorlage), Ragdoll **nicht** verwendet (CD-18 Würde: Erschöpfung ist eine Animation, kein Zusammensacken) |
| Control Rig | Gemeinsamer Archetyp-Control-Rig für Prozedurales: Atmen, Klangmal-Puls (Brustkorb), Kopfdrehung zum Ruf |

### 5.3 Mesh-Budgets

Die Budgets aus K56 (`AssetBudgets.csv`) gelten verbindlich. Für Echos wird ergänzt, wie die LOD-Stufen mit dem Ökologie-LOD aus K52 (Actor/MassNear/MassFar) zusammenhängen:

| Darstellungsstufe | Distanz | Darstellung | Tris (Stufe 1 / 3 / XXL) | Animation |
|---|---|---|---|---|
| LOD0 | < 15 m | Skeletal Mesh voll | 18 k / 45 k / 80 k | ABP voll, Control Rig, IK |
| LOD1 | 15–40 m | Skeletal Mesh | 9 k / 22 k / 40 k | ABP, ohne Control Rig |
| LOD2 | 40–80 m | Skeletal Mesh | 4 k / 10 k / 18 k | ABP vereinfacht (kein IK, 15 Hz Update-Rate-Optimierung) |
| LOD3 | 80–150 m | Skeletal Mesh | 1,5 k / 4 k / 8 k | 10 Hz |
| Mass-Instanz | 150–500 m (MassNear) | Instanced Static Mesh + **Animation-to-Texture** (Vertex-Animation) | 1,5 k / 4 k / 8 k | 4 Clips (Idle, Gehen, Laufen, Fressen) in der Textur |
| Impostor | > 500 m (MassFar) | Octahedral Impostor für XL/XXL, Rest unsichtbar | 2 Tris | keine |

Die Grenze Actor ↔ Mass bei 150 m und die Hysterese von 30 m stammen aus CANON §216 (K52). Der Wechsel Mass → Actor ist unsichtbar, weil die Animation-to-Texture-Clips aus denselben Quell-Clips gebacken sind und die Phase (Frame-Index) übergeben wird.

### 5.4 Evolution

Eine Evolution (K19) ist eine geteilte Animation zwischen Vor- und Zielform: Beide Meshes spielen synchron einen Verwandlungsclip auf ihrem jeweiligen Skelett; ein Dither-Übergang (Material-Parameter `EvoBlend`) blendet in der hellsten Phase des Lichts (NS_Evolution, K58) von einem Mesh zum anderen. Verschiedene Archetypen zwischen den Stufen (z. B. A09 → A15) sind erlaubt, weil kein Skelett-Morphing nötig ist.

---

## 6. Kreatur-Animation

### 6.1 Clip-Kategorien

Zwölf Kategorien decken alles ab, was eine Art im Spiel tut. Die Anzahl je Archetyp ergibt sich aus Regeln (z. B. Fortbewegung je Bewegungsart, Reiten je Reitart), nicht aus Einzelentscheidungen:

| Name | DisplayName | Content | Count | Source |
|---|---|---|---|---|
| ANIM_LOCO | Fortbewegung | je Fortbewegungsart des Archetyps: Start, Loop, Stopp, Drehen (4) | Locomotion | K16 §4 |
| ANIM_IDLE | Ruhe | 3 Idle-Varianten + 1 Umschau | fix 4 | K52 §8 |
| ANIM_EMOTION | Emotionen | Freude, Neugier, Angst, Wut, Trauer, Ruhe (additiv) | fix 6 | K56 §5.3 |
| ANIM_ECO | Ökologie | Nahrung, Schlafen (Ein/Loop/Aus), Sozial, Flucht, Jagd (Räuber) oder Wachsam | fix 7 | K52 §8 |
| ANIM_CALL | Ruf | Grundruf, Fluchtruf, Antwort (Klangmal-synchron) | fix 3 | K55 §5 |
| ANIM_COMBAT | Kampf | Phys-/Spez-/Status-Wirken, Treffer leicht/schwer, Ausweichen, Erschöpft, Sieg | fix 8 | K31–K33 |
| ANIM_CRESCENDO | Crescendo | 1 Signatur je Art mit Crescendo-Signatur, sonst Archetyp-Standard | Archetyp 1 + Signaturen | K30 |
| ANIM_BOND | Bindung | Beruhigen, Einstimmen, Anschlag-Reaktion gut/perfekt/daneben, Freilassen | fix 6 | K36 |
| ANIM_RIDE | Reiten | je Reitart: Aufsitzen, Loop, Sprint, Fähigkeit, Absitzen (5) | MountKinds | K40 |
| ANIM_COMPANION | Begleiter | Folgen, Feldfähigkeit, Streicheln (Stirn an Stirn …), Initiative-Geste | fix 4 | K37 |
| ANIM_EVOLUTION | Evolution | Ahnung (Puls), Verwandlung (geteilt mit Zielform) | fix 2 | K19 |
| ANIM_SILENCE | Verstummt | Erstarren, Verstummt-Loop, Erwachen | fix 3 | K07, K52 |

### 6.2 Umfang je Archetyp

`tools/ref/aethris_anim.py` berechnet aus `Archetypes.csv`, `Species.csv` und `AnimCategories.csv` den Umfang. Signaturen entstehen nur dort, wo eine Art eine Crescendo-Signatur besitzt (`SignatureConcept`); alle anderen Arten teilen den Archetyp-Satz.

| Archetyp | Skelett | Arten | Fortbewegung | Reitarten | Clips je Archetyp | davon Signaturen |
|---|---|---|---|---|---|---|
| A01 Vierbeiner leicht | `SKEL_Arch_QuadLight` | 21 | Lauf, Sprung, Klettern | – | 59 | 3 |
| A02 Vierbeiner schwer | `SKEL_Arch_QuadHeavy` | 12 | Lauf, Stampfen | Mount.Ground | 61 | 4 |
| A03 Huftier | `SKEL_Arch_Ungulate` | 8 | Lauf, Galopp | Mount.Ground | 60 | 3 |
| A04 Zweibeiner | `SKEL_Arch_Biped` | 10 | Gehen, Laufen, Greifen | – | 58 | 2 |
| A05 Vogel | `SKEL_Arch_Avian` | 28 | Flug, Hüpfen | Mount.Fly | 63 | 6 |
| A06 Gleitschwimmer | `SKEL_Arch_Glider` | 14 | Gleiten (Luft/Wasser) | Mount.Fly, Mount.Swim | 61 | 3 |
| A07 Schlange/Wurm | `SKEL_Arch_Serpent` | 14 | Schlängeln, Graben | Mount.Dig | 59 | 2 |
| A08 Fisch | `SKEL_Arch_Fish` | 7 | Schwimmen, Springen | Mount.Swim | 59 | 2 |
| A09 Amphib | `SKEL_Arch_Amphib` | 11 | Hüpfen, Schwimmen | – | 54 | 2 |
| A10 Gliederfüßer | `SKEL_Arch_Arthropod` | 22 | Krabbeln, Wandklettern | Mount.Climb | 61 | 4 |
| A11 Panzerträger | `SKEL_Arch_Shell` | 16 | Langsam, Einigeln | Mount.Ground | 58 | 1 |
| A12 Schwebend amorph | `SKEL_Arch_Floater` | 29 | Schweben | – | 52 | 4 |
| A13 Konstrukt/Elementar | `SKEL_Arch_Construct` | 23 | Gehen, Schwebende Teile | – | 55 | 3 |
| A14 Pflanzenwesen | `SKEL_Arch_Plant` | 10 | Wurzeln, Langsam gehen | – | 53 | 1 |
| A15 Drache | `SKEL_Arch_Dragon` | 6 | Lauf, Flug | Mount.Fly | 58 | 1 |
| A16 Schwarm | `SKEL_Arch_Swarm` | 10 | Schwärmen | – | 48 | 0 |
| A17 Kopffüßer/Tentakel | `SKEL_Arch_Tentacle` | 7 | Kriechen, Schwimmen | Mount.Swim | 58 | 1 |
| A18 Kletterer/Primat | `SKEL_Arch_Climber` | 8 | Klettern, Schwingen | Mount.Climb | 58 | 1 |
| **Σ** | 18 Skelette | **256** | | | **1035** | |

Aufgeteilt nach Kategorien:

| Kategorie | Inhalt | Clips gesamt (alle Archetypen) |
|---|---|---|
| Fortbewegung | je Fortbewegungsart des Archetyps: Start, Loop, Stopp, Drehen (4) | 140 |
| Ruhe | 3 Idle-Varianten + 1 Umschau | 72 |
| Emotionen | Freude, Neugier, Angst, Wut, Trauer, Ruhe (additiv) | 108 |
| Ökologie | Nahrung, Schlafen (Ein/Loop/Aus), Sozial, Flucht, Jagd (Räuber) oder Wachsam | 126 |
| Ruf | Grundruf, Fluchtruf, Antwort (Klangmal-synchron) | 54 |
| Kampf | Phys-/Spez-/Status-Wirken, Treffer leicht/schwer, Ausweichen, Erschöpft, Sieg | 144 |
| Crescendo | 1 Signatur je Art mit Crescendo-Signatur, sonst Archetyp-Standard | 61 |
| Bindung | Beruhigen, Einstimmen, Anschlag-Reaktion gut/perfekt/daneben, Freilassen | 108 |
| Reiten | je Reitart: Aufsitzen, Loop, Sprint, Fähigkeit, Absitzen (5) | 60 |
| Begleiter | Folgen, Feldfähigkeit, Streicheln (Stirn an Stirn …), Initiative-Geste | 72 |
| Evolution | Ahnung (Puls), Verwandlung (geteilt mit Zielform) | 36 |
| Verstummt | Erstarren, Verstummt-Loop, Erwachen | 54 |
| **Σ** | | **1035** |

**Bewertung:** 1.035 Clips für 256 Arten sind ≈ 4 Clips je Art. Ohne Archetyp-Teilung (Einzelanimation, ≈ 55 Clips je Art) wären es über 14.000 Clips – das ist der Grund für ADR-074 und für die strikte Regel TA-02.

### 6.3 Animation Blueprint `ABP_Echo_Base`

Alle Echos teilen ein Basis-Animation-Blueprint mit **Linked Anim Layers** je Archetyp. Die Logik ist identisch, nur die eingehängten Clips unterscheiden sich.

```
ABP_Echo_Base
├── Locomotion Layer   (ALI_Echo_Locomotion)   ← ABP_Arch_<Archetyp>_Loco    Blend Space Speed × Richtung, Stride Warping, Orientation Warping
├── Action Layer       (ALI_Echo_Action)       ← Montages: Kampf, Bindung, Ruf, Crescendo (Slot "Action")
├── Ecology Layer      (ALI_Echo_Ecology)      ← Fressen/Schlafen/Sozial aus StateTree-Zustand (K52)
├── Emotion Additive   (ALI_Echo_Emotion)      ← 6 additive Posen, Gewicht aus Emotionsfragment (K16 CD-08)
├── Procedural         Control Rig: Atmung, Klangmal-Puls (BPM), Kopf-/Blick-IK, Fuß-IK
└── Ride Layer         (ALI_Echo_Ride)         ← nur wenn Mount aktiv: Reit-Loops, Fähigkeit, Sprint
```

| Regel | Inhalt |
|---|---|
| Thread-sicher | Alle ABP-Logik im Worker-Thread (`BlueprintThreadSafeUpdateAnimation`); Eingaben über Property Access |
| Update-Rate | URO (Update Rate Optimization) ab LOD2; Echos außerhalb der Kamera ohne Pose-Update außer Wurzel |
| Montages | Ein Slot „Action“, ein Slot „Additive“; Kampf-Montages haben Notifies für Trefferzeitpunkt (synchron mit Kampf-Tick K28) |
| Notifies | `AN_KlangmalPulse`, `AN_CallStart`, `AN_Footstep` (Material-abhängig), `AN_HitFrame`, `AN_FxSpawn` – keine Spiellogik in Notifies außer Treffer-Synchronisierung |
| Root Motion | Nur für Kampf-Ausweichen, Crescendo und Reit-Fähigkeiten; Fortbewegung ohne Root Motion (Geschwindigkeit aus Bewegungskomponente, Clip angepasst) |
| Motion Warping | Für Angriffe auf Ziele unterschiedlicher Größe (XS gegen XXL): Warp-Ziel = Trefferpunkt des Gegners |

### 6.4 Emotionen

Die sechs Emotionen (CD-08: Freude, Neugier, Angst, Wut, Trauer, Ruhe) sind **additive** Posen auf allen Ebenen. Gewicht 0–1 aus dem Emotionszustand (K16/K37). Beispiel: Ein Fernlit läuft (Locomotion), frisst nicht (Ecology aus), ist ängstlich (Angst 0,7): Ohren angelegt, Schwanz unten, Kopf tief – ohne einen eigenen „ängstlich laufen“-Clip.

Ergänzend steuert die Emotion den Klangmal-Puls: Angst +30 % Tempo und flackernd, Ruhe −20 % und weich, Trauer gedimmt (Emissive × 0,5). Diese Werte sind Materialparameter, keine Animation.

### 6.5 Ruf und Klangmal synchron

Jeder Ruf (K55, `EchoCalls.csv`) hat ein Tempo in BPM. Das Klangmal pulst im selben Takt; beim Ruf (`AN_CallStart`) startet ein Quartz-Takt (K55), auf den Animation (Kehle, Brust über Control Rig) und Material (Puls-Spitze) quantisiert werden. Damit gilt:

| Ereignis | Bild | Klang | Synchronisierung |
|---|---|---|---|
| Ruhezustand | Klangmal pulst mit `KlangmalBPM` | Atemgeräusch | Material-Zeit |
| Ruf | Puls-Spitze auf jedem Schlag, Kopf hebt sich | Ruf auf Skalenstufe des Typs | Quartz-Takt, Animation auf Schlag 1 |
| Crescendo | Klangmal maximal, Farbe Typakzent | Typ-Ton + Weltlied-Fragment | Quartz, Kampf-Tick |
| Verstummt | Klangmal erlischt (Emissive → 0 über 1,5 s) | Stille, Rauschen | Material-Kurve |
| Heilung (Stille-Rückkehr) | Klangmal flackert, dann voller Puls | erster Ton nach der Stille | Quest-Ereignis |

### 6.6 Schwärme, Mass und Ferndarstellung

Archetyp A16 (Schwarm) wird nicht als einzelnes Skelett, sondern als **Niagara-Schwarm** mit 12–60 Partikel-Meshes plus einem unsichtbaren „Schwarmkern“-Actor dargestellt. Der Kern trägt Kollision, Kampf-Interaktion und Ruf; die Partikel folgen Boids-Regeln (K52 GroupBehaviors) in Niagara. Die 48 Clips von A16 sind Partikel-Muster (Sammeln, Ausschwärmen, Wirbel, Schild) statt Skelettanimationen.

Für die MassNear-Zone (150–500 m) werden pro Art vier Clips per **Animation-to-Texture** gebacken. Budget je Art: eine Bone-Textur 512 × 256 (RGBA16F), ≈ 1 MB. Bei 256 Arten sind das ≈ 256 MB auf der Festplatte, gestreamt nur für Arten der geladenen Regionen (im Mittel 30–40 Arten aktiv ≈ 40 MB VRAM).

---

## 7. Menschliche Animation und Zwischensequenzen

### 7.1 Sätze

| Name | Who | Content | Clips | Source |
|---|---|---|---|---|
| HUM_PLAYER_LOCO | Spieler | Gehen, Laufen, Schleichen, Springen, Landen, Ducken (Motion Matching, ~180 Clips) | 180 | K02 §5 |
| HUM_PLAYER_TRAVERSAL | Spieler | Klettern (Wand, Kante, Überhang), Gleiten (Start, Loop, Kurven, Sturz, Landung), Schwimmen, Tauchen, Graben (auf Reittier) | 140 | K40 |
| HUM_PLAYER_TOOLS | Spieler | Resonator (ziehen, Resonanzsinn, Anschlag), Kodex-Linse, Werkzeug (Klinge/Hacke/Sichel), Lockmittel werfen, Falle stellen | 70 | K36, K39, K40 |
| HUM_PLAYER_SOCIAL | Spieler | Gesten (12), Streicheln je Archetyp-Größe (6), Lager (Sitzen, Kochen, Schlafen) | 40 | K37, K44 |
| HUM_PLAYER_COMBAT | Spieler | Befehle an den Chor (8), Siegel werfen, Item nutzen, Crescendo-Ruf, Sieg/Niederlage | 30 | K31 |
| HUM_NPC_ACTIVITY | NPC | Je Aktivitätscode (K53 §4): Arbeit je Beruf (12 Berufe), Essen, Gasthaus, Markt, Streife, Vorlesung, Labor, Lesen, Stille Stunde, Fischen, Hüten, Unterricht, Spielen, Reise, Rast | 220 | K53 |
| HUM_NPC_REACTION | NPC | Schutz suchen, Siesta, Zuschauen, Fliehen, Ausweichen, Staunen, Streicheln, Danken, Feiern, Sorge, Laternen anzünden, Himmel zeigen | 60 | K53 §6 |
| HUM_NPC_GESTURE | NPC (Orden) | Schweigegesten-Set (24 Gesten), Schiefertafel schreiben/zeigen | 30 | K53, CANON §55 |
| HUM_DIALOGUE | alle | Dialog-Idles (Haltung je Persönlichkeit, 8), Zuhören, Reaktionen (Freude, Zweifel, Schreck, Trauer), Lip-Sync prozedural | 90 | K48 §10.6 |
| HUM_CINEMATIC | Story | Motion Capture für 70 Zwischensequenzen (K44–K46) | ≈ 95 min | K44–K46 |

### 7.2 Spieler: Motion Matching

Der Spielercharakter nutzt **Motion Matching** (Pose Search, UE 5.6) für Fortbewegung und Traversal: eine Datenbank aus Mocap-Aufnahmen (Gehen, Laufen, Schleichen, Starts, Stopps, Drehungen, Gelände), gewählt über Trajektorie und Pose. Klettern, Gleiten, Schwimmen und Reiten sind eigene Zustände mit eigenen Datenbanken.

| Element | Festlegung |
|---|---|
| Datenbanken | `PSD_Player_Loco` (≈ 180 Clips), `PSD_Player_Traversal`, `PSD_Player_Swim`; Reiten als klassischer Zustandsautomat je Reitart (5 Mount-Arten) |
| Zeitbudget | Pose Search ≤ 0,25 ms (PS5) / 0,45 ms (Switch 2) Game Thread + Worker |
| Garderobe (K42) | Kleidungsmodule auf demselben Skelett `SKEL_Human`; Stoffsimulation über Chaos Cloth nur für Umhänge und Röcke (max. 2 Cloth-Assets je Figur) |
| Körpertypen | Drei Spieler-Körper (schmal, mittel, kräftig) mit gemeinsamem Skelett, Proportionen über Retargeting; Spielerfigur ist geschlechtsneutral wählbar (K02) |
| Streicheln | 6 Varianten nach Archetyp-Größe (XS–XXL), Hand-IK auf Kontaktpunkt `pet_socket` des Echos |

### 7.3 NPCs

NPCs (K53) teilen **ein** Skelett `SKEL_Human` und acht Grundkörper. Ihre Tagesabläufe benötigen Aktivitätsanimationen je Aktivitätscode; die Auswahl erfolgt über Smart Objects (Slot mit Animationstag), die Distanz-LOD über Significance Manager:

| Distanz | NPC-Darstellung | Animation |
|---|---|---|
| < 25 m | volles Skeletal Mesh, Gesicht | ABP voll, Blick-IK, Gesten |
| 25–60 m | Skeletal Mesh LOD1–2 | ABP ohne IK, 15 Hz |
| 60–150 m | Skeletal Mesh LOD3 | 5 Hz, nur Aktivitätsschleife |
| > 150 m | Mass-Crowd (Animation-to-Texture, 6 Clips) | Instanz-Animation |

Gesichtsanimation: Dialog-Gesichter über **Audio-gesteuerte Lippensynchronisierung** (Phonem-Kurven aus der Sprachaufnahme, je Sprache gerechnet: Deutsch, Englisch, Französisch, Spanisch, Japanisch …) für alle Dialoge; handanimierte Gesichter nur in Zwischensequenzen. Für den Orden der Stille (Schweigegesten, CANON §55) entfällt Lippensynchronisierung; dort tragen 24 Gesten und die Schiefertafel den Dialog.

### 7.4 Zwischensequenzen

Rund 70 Zwischensequenzen (K44–K46, ≈ 95 min) werden mit **Motion Capture** (Körper + Gesicht, Performance Capture) aufgenommen und in Sequencer zusammengesetzt.

| Stufe | Inhalt | Werkzeug |
|---|---|---|
| Previs | Kamera, Blocking, Timing mit Proxy-Figuren | Sequencer, USD-Layout |
| Aufnahme | Performance Capture (Körper, Gesicht, Stimme gemeinsam für Hauptrollen) | Externes Studio (§12) |
| Bereinigung | Retargeting auf `SKEL_Human`, Finger, Kontaktkorrekturen | MotionBuilder, Control Rig |
| Kreaturen in Szenen | Handanimation (Echos werden nicht per Mocap aufgenommen) | Maya |
| Licht und Kamera | Cinematic-Lichtrigs, Lumen, keine gebackene Beleuchtung | Sequencer |
| Abnahme | Narrative Director, Animation Director, Lokalisierungs-Timing (Untertitel ≤ 17 Zeichen/s) | Review-Build |

**Spielerfigur in Zwischensequenzen:** Die frei gestaltete Spielerfigur ist in jeder Szene sichtbar. Deshalb laufen alle Sequenzen in Echtzeit (keine vorgerenderten Videos); Kleidung, Körpertyp und das aktive Begleit-Echo werden zur Laufzeit gebunden (Sequencer-Bindings über Spawnable-Ersatz). Echos in Szenen nutzen dieselben Signatur- und Emotionsclips wie im Spiel, damit das gewählte Begleit-Echo glaubwürdig reagiert.

---

## 8. Technical Art: Materialien und Shader

### 8.1 Master-Materialien

| Master | Verwendung | Wichtige Schalter (Static Switches) | Max. Permutationen |
|---|---|---|---|
| `M_Echo_Master` | alle Echos | Fell/Schuppe/Chitin/Kristall/Pflanze/Konstrukt (Oberflächenmodell), Klangmal an, Subsurface, Schillernd (Shiny-Variante) | 48 |
| `M_EchoFX_Master` | Geister-/Leere-/Kristallkörper, Schwarm-Partikel | Transluzent/Maskiert, Verzerrung | 12 |
| `M_Env_Master` | Fels, Erde, Holz, Metall | Layered (bis 3 Ebenen), Nässe, Schnee, Asche, Moos (Welt-Ausrichtung) | 64 |
| `M_Foliage_Master` | Bäume, Büsche, Gras | Nanite-Foliage, Wind, Subsurface-Blätter, Glockenblüten-Ton-Puls | 24 |
| `M_Arch_Master` | Architektur-Kits je Kultur | Patina, Gravur/Glyphen (Emissive), Stille-Grau | 32 |
| `M_Char_Master` | Menschen, Kleidung | Haut (Substrate Skin), Stoff, Leder, Metall, Fraktionsfarbe | 32 |
| `M_Water_Master` | Wasser (Single Layer Water), Seen, Flüsse | Strömung, Schaum, Stille (glatt) | 8 |
| `M_UI_Master` | Weltgebundene UI, Kodex-Linse | – | 4 |
| `M_Decal_Master` | Spuren, Schmutz, Glyphen | DBuffer-Kanäle | 8 |

**Substrate** (UE 5.6) ist für Haut, Schillern und Kristall freigegeben; Switch 2 nutzt den Fallback „Substrate Simple“. Regel: keine neuen Master-Materialien ohne Technical-Art-Freigabe; Künstlerinnen und Künstler arbeiten ausschließlich mit Instanzen. Gesamtbudget Shader-Permutationen ≤ 250 je Plattform (Kompilierzeit, PSO-Cache).

### 8.2 Material Functions

| Funktion | Zweck | Parameter |
|---|---|---|
| `MF_Klangmal` | Emissive-Puls entlang der Klangmal-Maske (`T_*_M`, Kanal R = Form, G = Laufrichtung, B = Intensität) | `KlangmalBPM`, `KlangmalColor`, `EmotionTempo`, `Silenced` (0–1), `CallPeak` |
| `MF_Silence` | Entsättigung, Grauschleier, gedämpfte Emissive in Stille-Zonen | `MPC_Silence.Strength`, Weltposition, Zonenmaske |
| `MF_Healing` | Farbwelle, die von einem Punkt aus die Entsättigung zurücknimmt | `HealOrigin`, `HealRadius`, `HealTime` |
| `MF_WeatherSurface` | Nässe, Pfützen, Schnee, Asche auf Oberflächen | `MPC_Weather.*` |
| `MF_TypeAccent` | Typfarben-Akzent (nur Akzent, ADR-218) | `TypeColor` aus `TypeColors.csv` |
| `MF_Shiny` | Schillernde Variante (seltene Farbvariante): Farbverschiebung + Glitzer, nie Typfarbe | `ShinyHueShift`, `ShinySparkle` |
| `MF_Glyph` | Dorun-Glyphen leuchten bei Resonanz | `GlyphActivation` |
| `MF_DitherFade` | LOD-/Evolution-Übergang | `EvoBlend`, `FadeAmount` |

### 8.3 Material Parameter Collections

| MPC | Parameter | Gesetzt von |
|---|---|---|
| `MPC_Silence` | Strength, ZoneCenter, ZoneRadius, HealProgress | Stille-System (K10), Quest-Ereignisse (K44–K46) |
| `MPC_Weather` | Wetness, Snow, Ash, Sand, WindDir, WindStrength, Storm, NightFactor (Kopie) | Wettersystem (K15) |
| `MPC_TimeOfDay` | SunDir, MoonPhase, NightFactor, AuroraIntensity (Himmel, Wasser) | Tageszyklus (K15) |
| `MPC_Resonance` | StormPhase, QuantizeStrength, CrownPulse | Resonanzsturm, Krone (K55, K46) |
| `MPC_Player` | PlayerPos, ResonanceSenseActive, LensActive | Spieler (Resonanzsinn, Kodex-Linse) |

Regel: höchstens 2 MPCs je Material (Engine-Grenze). Umwelt-, Foliage- und Architektur-Masters lesen `MPC_Silence` + `MPC_Weather`; Tageszeit-Werte, die sie brauchen (Nachtfaktor für Glyphen), stehen als Kopie in `MPC_Weather.NightFactor`. `M_Echo_Master` liest `MPC_Silence` + `MPC_Resonance`; Himmel und Wasser lesen `MPC_TimeOfDay` + `MPC_Weather`.

### 8.4 Stille in der Darstellung

Die Stille (CANON §220) ist das wichtigste wiederkehrende Bildelement. Technisch wirkt sie auf drei Ebenen:

| Ebene | Umsetzung | Kosten (PS5) |
|---|---|---|
| Materialien | `MF_Silence` in Env/Foliage/Arch/Echo: Sättigung × (1 − 0,9 × Strength) (bis 90 %, CANON §220), Emissive × (1 − Strength) | im Material, ≈ 0 |
| Post-Process | Volumen `PPV_Silence_R##` mit Entsättigung, leichter Vignette, gedämpftem Bloom | 0,1 ms |
| Leben | Ökologie-Dichte −80 % (K52), Wind-Animation der Foliage × 0,2, keine Partikel-Insekten | spart Zeit |

Die Heilung einer Region (Akt-Ende) spielt `MF_Healing` als Welle vom Resonanzstein aus (Radius 0 → 2.000 m in 4 s, CANON §220), anschließend wechselt der Data Layer von `DL_Story_R##_Silence` auf `DL_Story_R##_Healed` (CANON §43). Die Welle verdeckt den Layer-Wechsel; das Streaming der „Healed“-Zellen wird 30 s vorher vorgeladen.

### 8.5 Licht und Lumen

Lumen ist auf PS5/XSX/PC die globale Beleuchtung; auf Switch 2 ersetzt SSGI + Light Probes Lumen (CANON §221). Für Technical Art heißt das:

- Jede Region hat ein **Lichtprofil** (`DA_LightProfile_R##`) mit Sonnenfarbe, Himmelslicht, Nebel und Belichtung je Tageszeit; gesteuert über `MPC_TimeOfDay` (K15).
- Emissive Klangmale tragen zur Beleuchtung bei (Lumen Emissive) ab LOD0–1; auf Switch 2 wird für die drei nächsten Echos ein kleines Punktlicht (Radius 2 m, ohne Schatten) gesetzt.
- Innenräume: Lumen + lokale Lichter, keine Lightmaps; Höhlen nutzen Klangmale und Kristalle als Hauptlicht (Art-Regel K56 §4).

---

## 9. Welt-Pipeline: PCG, World Partition, HLOD

### 9.1 Ablauf je Region

```
Höhenfeld (World Machine/Gaea, 1 m) ─► Landscape-Import (L_Aethris_World, Region als Landscape-Proxy)
 ─► Blockout (DL_Editor_Blockout, BSP/Grey-Box Kits) ─► LD-Metriken prüfen (CANON §43/§47)
 ─► PCG je Layer (PCG_R##_Canopy … Hazards) ─► Landmarken + Siedlungen als Level Instances
 ─► Set-Dressing ─► Licht ─► HLOD-Build ─► Performance-Pass (K65) ─► Abnahme
```

### 9.2 PCG

| Layer | Inhalt | Eingaben | Regeln |
|---|---|---|---|
| Canopy | große Bäume | Biom-Maske, Höhe, Hang < 35° | Abstand ≥ 6 m, keine Bäume auf Pfaden (Spline-Ausschluss) |
| Understory | Büsche, junge Bäume | Canopy-Dichte (invers) | Sichtlinien zu Landmarken frei halten (Sichtachsen-Spline) |
| Ground | Gras, Moos, Blumen | Material-Layer des Landscapes | Gras-Budget §9.4, Glockenblüten nur R01 |
| Rocks | Felsen, Geröll | Hang, Krümmung | Kletterfelsen mit Klettermaterial-Tag |
| Water | Ufer, Schilf, Seerosen | Wasser-Spline | R03: Seerosen > 2 m begehbar |
| Props | Zäune, Wegsteine, Schilder | Straßen-/Pfad-Splines | Kultur-Kit je Region |
| Hazards | Dornen, Lava-Risse, Eisplatten | Gefahrenmasken (K09 §2) | Mit Gameplay-Volumen gekoppelt |

PCG wird **im Editor gebacken** (CANON §46 Tech-Art), nicht zur Laufzeit erzeugt. Grund: Determinismus, Performance auf Switch 2, und dass Level Design nach dem Backen gezielt nachbessern kann. Laufzeit-PCG bleibt auf zwei Fälle beschränkt: Lava-Layer A/B in Ignareth (vorbereitet, umgeschaltet) und Wetter-Streudetails (Pfützen-Decals).

### 9.3 World Partition, Level Instances, HLOD

| Element | Festlegung |
|---|---|
| Grids | MainGrid 128 m (Ladebereich 768 m, Switch 2 512 m), FarGrid 512 m / 3 km, Underground 64 m / 256 m, Sky 256 m / 2 km (CANON §43) |
| Siedlungen | Je Siedlung eine **Packed Level Instance** für statische Teile + eine Level Instance für interaktive Actors; Bearbeitung im Kontext (Level-Instance-Editing) |
| Interiors | Level Instances, gestreamt über das Underground-/MainGrid je nach Lage; keine separaten Levels mit Ladebildschirm |
| HLOD | 3 Ebenen: HLOD0 Instanzierung (Nanite-Instanzen zusammengefasst, < 768 m), HLOD1 Merged Mesh (768 m – 3 km), HLOD2 Simplified/Approx. Mesh (> 3 km, Landmarken immer enthalten) |
| Landmarken | Mindestens 2 km sichtbar (CANON §47): eigener HLOD-Satz mit Silhouetten-Priorität, nie aus HLOD2 entfernt |
| Data Layers | `DL_Base`, Story-Layer je Region (Silence/Healed), Gates, Nachhall, Events, Blockout (CANON §43) |
| One File Per Actor | Pflicht; Sperren pro Actor statt pro Level (Perforce) |

### 9.4 Budgets je Region (PS5 / Switch 2)

| Budget | PS5 | Switch 2 | Prüfung |
|---|---|---|---|
| Nanite-Instanzen Foliage | ≤ 1,6 Mio. | ≤ 400 k | PCG-Statistik je Zelle |
| Gras-Instanzen (sichtbar) | ≤ 250 k | ≤ 60 k | Laufzeit-Zähler |
| Geladene Zellen (MainGrid) | ≤ 140 | ≤ 70 | Streaming-Bericht |
| Draw Calls (Nicht-Nanite) | ≤ 2.500 | ≤ 1.200 | RenderDoc/Insights |
| Texturspeicher Welt | ≤ 2,2 GB | ≤ 900 MB | Texture-Streaming-Pool |
| Echo-Actors | 40 | 16 | K52 |
| NPC-Actors (voll) | 60 | 24 | K53 |

Details zu Frame-Budgets und Plattformprofilen in K65.

---

## 10. Validierung und Werkzeuge

### 10.1 Editor-Validatoren

| Validator | Prüft | Schwere | Ort |
|---|---|---|---|
| `UAethrisAssetNamingValidator` | Präfix je Klasse (CANON §23), Texturen-Suffix (_D/_N/_ORM/_E/_M), Pfad unter `/Game/Aethris` | Fehler | `Source/AethrisEditor/…/Validation` |
| `UAethrisEchoAssetValidator` | Skelett = `SKEL_Arch_<Archetyp>` laut `Species.csv`, Klangmal-Maske vorhanden, LOD-Anzahl 4, Physics Asset, `pet_socket` | Fehler | AethrisEditor (P2) |
| `UAethrisTextureValidator` | Größe ≤ Budget, Kompression je Suffix (BC5 für _N, BC7/BC1 für _D, Linear für _ORM/_M), sRGB-Flag | Fehler | AethrisEditor (P2) |
| `UAethrisMaterialValidator` | MI hat Master aus der freigegebenen Liste, keine neuen Masters, ≤ 2 MPCs | Fehler | AethrisEditor (P2) |
| `UAethrisAnimValidator` | Clip auf richtigem Skelett, Kompression (ACL), Notifies aus der erlaubten Liste, Root Motion nur in erlaubten Kategorien | Fehler | AethrisEditor (P2) |
| `UAethrisBlueprintValidator` | Keine Gameplay-Werte in Defaults (TA-01), keine harten Asset-Referenzen auf Echos (Soft, DD-02) | Fehler | AethrisEditor (P2) |
| World-Validatoren | Regionsfläche, POI-Abstände, Steine, Kampfflächen (CANON §43) | Fehler | `tools/` + Commandlet |

Der Namensvalidator ist bereits im Repository (Grundgerüst, P1). Seine Kernlogik:

```cpp
// Auszug aus AethrisAssetNamingValidator.cpp (vereinfacht)
FString UAethrisAssetNamingValidator::ExpectedPrefix(const UClass* C)
{
    if (C->IsChildOf<UStaticMesh>())               return TEXT("SM_");
    if (C->IsChildOf<USkeletalMesh>())             return TEXT("SK_");
    if (C->IsChildOf<UAnimSequence>())             return TEXT("AS_");
    if (C->IsChildOf<UAnimMontage>())              return TEXT("AM_");
    if (C->IsChildOf<UMaterialInstanceConstant>()) return TEXT("MI_");
    if (C->IsChildOf<UMaterial>())                 return TEXT("M_");
    if (C->IsChildOf<UTexture2D>())                return TEXT("T_");
    return FString();   // unbekannte Klasse: keine Präfixregel
}
// Texturen: Name muss auf _D, _N, _ORM, _E oder _M enden.
```

### 10.2 Pseudocode: Pre-Submit

```
on_submit(changelist):
    files = changelist.files
    if any(f under "Data/" for f in files):
        run("python3 tools/data_lint.py")                   → Abbruch bei Fehler
        run_generators_if_inputs_changed(files)             → generierte CSVs müssen im Changelist sein
    if any(f.endswith(".uasset") for f in files):
        run_editor_commandlet("DataValidation", assets=files)  → alle UEditorValidatorBase
    if any(f under "Source/" for f in files):
        run("python3 tools/check_layers.py")                 → Schichtregeln CANON §26
        compile_and_unit_test(changed_modules)
    if count(files of type .uasset) > 200 and "[ART-BULK]" not in changelist.description:
        reject("Massenänderung ohne [ART-BULK]")
```

### 10.3 Nächtliche Berichte

| Bericht | Inhalt | Empfänger |
|---|---|---|
| Platzhalter-Kurve | Arten mit Proxy-Mesh je Region, Clips fehlend je Archetyp | Produktion, Art Director |
| Budget-Bericht | Tris/Texturen/Instanzen je Region vs. `AssetBudgets.csv` und §9.4 | Technical Art |
| Shader-Bericht | Permutationen je Master, PSO-Cache-Abdeckung | Technical Art, Rendering |
| Cook-Größe | Paketgröße je Plattform, Delta zum Vortag | Build, Plattform |
| Animation-Abdeckung | Clips vorhanden vs. Soll (`aethris_anim.py`) | Animation Director |

---

## 11. Produktionsumfang und Schätzung

### 11.1 Mengen

| Bereich | Menge | Quelle |
|---|---|---|
| Echo-Arten (Meshes) | 256 (+ Schillernd-Varianten als Materialinstanz) | K20–K27 |
| Archetyp-Skelette und -Rigs | 18 | CANON §70 |
| Kreatur-Clips | 1.035 | §6 |
| Menschliche Clips (ohne Zwischensequenzen) | ≈ 1.000 (Summe `HumanAnimSets.csv` ohne Cinematic) | §7 |
| Zwischensequenzen | ≈ 70 Szenen, ≈ 95 min | K44–K46 |
| NPC-Grundkörper / Köpfe | 8 / 60 | K53 |
| Benannte NPCs | 194 | K53 `Npcs.csv` |
| Regionen | 10 | K09/K10 |
| Architektur-Kits | 7 Kulturen | K56 §7 |
| Master-Materialien | 9 | §8.1 |

### 11.2 Aufwand Kreaturen

Mit den Ø-Werten aus §5.1 (Stufe 1 = 18, Stufe 2/3 = 24,5, Legendär/Mythisch = 53 Personentage):

| Gruppe | Anzahl (ca.) | Personentage je Art | Summe |
|---|---|---|---|
| Stufe 1 (ohne Legendär/Mythisch) | 107 | 18 | 1.926 |
| Stufe 2/3 | 133 | 24,5 | 3.259 |
| Legendär und Mythisch | 16 | 53 | 848 |
| Archetyp-Rigs + geteilte Clips | 18 | 60 | 1.080 |
| **Summe** | | | **≈ 7.110 PT** |

Mit 220 produktiven Tagen je Person und Jahr sind das ≈ 32 Personenjahre. Bei einer Kreaturen-Produktion von P2 bis Beta (ca. 3,5 Jahre) braucht es ≈ 10 Personen intern oder eine Mischung aus 6 intern und externen Partnern (§12). Die Detailplanung erfolgt in K67.

### 11.3 Durchsatzziel

| Phase | Ziel | Messung |
|---|---|---|
| Vertical Slice (K67) | 16 Arten final (R01, K01 §16.2), 18 Archetyp-Sätze in Rohfassung | Platzhalter-Kurve |
| Alpha | 160 Arten final, alle Archetypen final | Platzhalter-Kurve |
| Beta | 256 Arten final, 0 Platzhalter | Platzhalter-Kurve = 0 |

---

## 12. Externe Partner und Abnahme

Externe Partner (Outsourcing) übernehmen Umgebungsassets, einen Teil der Kreatur-Modelle (nicht Konzept, nicht Signaturen) und die Mocap-Aufnahme. Rechte, Clean-Room und Qualität sind vertraglich und technisch abgesichert.

| Bereich | Intern | Extern | Begründung |
|---|---|---|---|
| Kreatur-Konzept | ✔ | – | Clean-Room (DR-22), Identität |
| Kreatur-Modell/Textur | Hero, Legendär, Mythisch | Stufe 1–3 nach Konzeptfreigabe | Volumen |
| Rigs/Archetypen | ✔ | – | Kernsystem |
| Geteilte Clips | ✔ | – | Qualität der Basis |
| Signaturen | ✔ | teilweise mit Supervision | Charakter |
| Umgebungs-Kits | Kernkits je Kultur | Varianten, Props | Volumen |
| Mocap | Regie intern | Studio, Bereinigung | Infrastruktur |
| Zwischensequenzen | Layout, Kamera, Finale | Bereinigung, Kreaturen-Animation nach Vorgabe | Volumen |

**Übergabepaket an Partner:** Brief (K16-Datenblatt, K56-Gestaltungsbrief), Archetyp-Skelett, Export-Skript, Budget-Tabelle, Prüfskript (Offline-Version der Validatoren als Python, läuft ohne Editor), Beispiel-Asset.

**Abnahme in drei Stufen:** (1) automatische Prüfung (Validatoren, Budgets) – nur grüne Lieferungen werden angesehen, (2) Art-Review gegen K56, (3) In-Engine-Review (30 m, Nacht, Nebel, Farbenblind). Zwei Korrekturrunden sind im Vertrag enthalten.

---

## 13. Risiken

| Risiko | Wahrscheinlichkeit | Wirkung | Gegenmaßnahme |
|---|---|---|---|
| Archetyp-Rig passt nicht für eine Art (Proportionen zu extrem) | mittel | Eigene Clips nötig | Zusatzknochen-Slots, Größenbereiche je Archetyp früh testen, Ausnahmeliste ≤ 5 Arten |
| Shader-Kompilierzeit/PSO-Ruckler | hoch | Ruckler beim ersten Sehen | Permutationsbudget ≤ 250, PSO-Precaching, nächtliche PSO-Sammelläufe |
| HLOD-Builds dauern zu lange | mittel | Blockiert Welt-Iteration | Verteilte HLOD-Builds (Horde), inkrementell je Region |
| Mocap-Termine verschieben sich | mittel | Zwischensequenzen spät | Previs mit Proxy, Aufnahmeblöcke je Akt, Puffer 8 Wochen |
| Animation-to-Texture-Übergang sichtbar | niedrig | Ploppen bei 150 m | Phasenübergabe, Hysterese 30 m, Dither |
| Perforce-Umzug (P2) verliert Historie | niedrig | Nachvollziehbarkeit | Migration nur Code/Daten mit Historie; Art beginnt frisch in Perforce |
| Externe Lieferungen verletzen Clean-Room | niedrig | Rechtliches Risiko | Clean-Room-Erklärung, Ähnlichkeitstest, Quellenarchiv |

---

## 14. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| VFX | Klangmal-Partikel, Evolution-Licht, Heilungswelle, Stille-Partikel; Anbindung an `MF_Klangmal`/`MPC_Silence` | K58 |
| Netzwerk | Animation ist rein kosmetisch und nicht repliziert außer Montage-Start und Phase (Koop, Kampf-Tick) | K59 |
| Plattformen | Switch-2-Profile: LOD-Verschiebung, SSGI statt Lumen, Gras ≤ 60 k, Pose Search 0,45 ms | K65 |
| QA | Testfälle für Validatoren, Platzhalter-Kurve als Release-Kriterium | K66 |
| Produktion | Personalplanung Kreaturen (≈ 32 Personenjahre), Outsourcing-Verträge | K67 |
| Audio | `AN_Footstep` mit Oberflächen-Tag, Quartz-Takt für Rufe | K55 |
| Design | Neue Arten nur mit gültigem Archetyp, Signaturkonzept in `Species.csv` | K16 |

---

## 15. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-221 | Geteilte Clips je Archetyp + Signaturen nur für Crescendo-Arten (1.035 Kreatur-Clips) | Umfang machbar, einheitliche Qualität, Platzhalter ab Tag 1 | Einzelanimation je Art (> 14.000 Clips) |
| ADR-222 | `ABP_Echo_Base` mit Linked Anim Layers je Archetyp, Emotionen additiv | Eine Logik, Wartbarkeit, Thread-sicher | 18 eigenständige Animation Blueprints |
| ADR-223 | Animation-to-Texture für MassNear (150–500 m), Impostor für XL/XXL in MassFar | Hunderte Echos sichtbar bei kleinem Budget | Skeletal Meshes bis 500 m |
| ADR-224 | Motion Matching nur für die Spielerfigur; NPCs und Echos klassisch | Spielgefühl beim Spieler, Kosten bei NPCs | Motion Matching überall |
| ADR-225 | Zwischensequenzen in Echtzeit mit Laufzeit-Bindung von Spielerfigur und Begleit-Echo | Personalisierte Spielerfigur, Begleiter reagiert | vorgerenderte Videos |
| ADR-226 | Neun Master-Materialien, Permutationsbudget ≤ 250 je Plattform | PSO-Cache, Kompilierzeit, Konsistenz | freie Materialien je Asset |
| ADR-227 | PCG im Editor gebacken; Laufzeit-PCG nur für Lava-Layer und Wetter-Streudetails | Determinismus, Switch-2-Leistung, Nachbearbeitung | Laufzeit-PCG |
| ADR-228 | Erste CSV-Spalte heißt `Name` (CR-006), Importer akzeptiert `Id` als Alias | Bestand > 100 Dateien, Tools lesen `Name` | Massenumbenennung zu `Id` |

---

## 16. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §222 | Pipeline-Stufen, Austauschformate (FBX, USD; Alembic nur Ausnahmeliste), Inhaltsordner `/Game/Aethris/…`, Quellordner `Art/Source/`, Benennungsmuster für Echos/Clips/Materialien, `[ART-BULK]`, Grundsätze TA-01–TA-07 | LOCKED |
| §223 | Kreatur-Rigs (18 `SKEL_Arch_*`, ≤ 12 Zusatzknochen, kein Ragdoll), 12 Clip-Kategorien (`AnimCategories.csv`), 1.035 Clips, `ABP_Echo_Base` mit Linked Layers, Emotionen additiv, Ruf/Klangmal synchron über Quartz, LOD-Kette bis Animation-to-Texture/Impostor, Schwarm als Niagara | LOCKED |
| §224 | Menschliche Sätze (`HumanAnimSets.csv`), Motion Matching nur Spieler, `SKEL_Human` für alle Menschen, NPC-Distanzstufen, Lippensynchronisierung audio-gesteuert, Zwischensequenzen in Echtzeit mit Performance Capture | LOCKED |
| §225 | Neun Master-Materialien, Material Functions (`MF_Klangmal` u. a.), MPCs (Silence, Weather, TimeOfDay, Resonance, Player), Stille-Darstellung auf drei Ebenen, Heilungswelle verdeckt Data-Layer-Wechsel, PCG gebacken, HLOD-Ebenen, Regionsbudgets | LOCKED |
| §226 | Validatoren (Namen, Echo, Textur, Material, Animation, Blueprint, Welt), Pre-Submit-Ablauf, nächtliche Berichte, Platzhalter-Kurve, Abnahme externer Lieferungen in drei Stufen | LOCKED |
| §31 | CR-006: erste CSV-Spalte `Name` (Primärschlüssel); `Id` als Alias | LOCKED (ändert §31) |
| §10 | ADR-221 – ADR-228 | LOCKED |

---

## 17. Kapitel-Checkliste

- [x] Grundsätze TA-01–TA-07, Pipeline-Überblick mit Stufen und Verantwortlichen
- [x] Ordnerstruktur, Benennungsmuster, Versionierung (Git P1 → Perforce P2)
- [x] Datenpipeline, Importer-Kette, Platzhalter-Regel, CR-006
- [x] Kreaturen-Pipeline, Aufwand je Art, Archetyp-Skelette, Retargeting, Mesh-LODs bis Mass
- [x] Kreatur-Animation: 12 Kategorien, 1.035 Clips (berechnet), ABP-Aufbau, Emotionen, Ruf-Sync, Schwärme
- [x] Menschliche Animation, Motion Matching, NPC-Stufen, Zwischensequenzen
- [x] Master-Materialien, Material Functions, MPCs, Stille, Licht
- [x] Welt-Pipeline: PCG-Layer, World Partition, HLOD, Budgets
- [x] Validatoren (Namensvalidator im Repository), Pre-Submit, Berichte
- [x] Produktionsumfang und Schätzung (≈ 32 Personenjahre Kreaturen), Outsourcing, Risiken
- [x] Anforderungen, ADR-221 – ADR-228, CANON §222–§226, CR-006

➡️ **Nächstes Kapitel: K58 – VFX.**
