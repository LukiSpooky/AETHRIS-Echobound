# K65 · Performance und Plattformen

| Feld | Wert |
|---|---|
| Dokument | Kapitel 65 von 68 · Technik IV |
| Version | 1.0 |
| Owner | Technical Director, Lead Engine Programmer |
| Mitwirkende | Rendering Programmer, Plattform-Programmierung (Sony, Microsoft, Nintendo, PC), Technical Art Director, Performance-QA, Build Engineer |
| Baut auf | K01 §11 (Plattformen, FPS-Ziel, CANON §2/§9), K05 (Engine, CI), K08 §10 (World Partition, CANON §43), K15 (Licht, ADR-070), K52/K53 (Ökologie-/NPC-Budgets), K54 (UI-Budgets), K55 (Audio-Budgets), K56/K57 (Asset-Budgets, Technical Art), K58 (VFX-Budgets), K59 (Koop-Host, Netz), K64 (Save-Budgets) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Perf/PlatformProfiles.csv`, `FrameBudgets.csv`, `MemoryBudgets.csv`; Referenzmodell `tools/ref/aethris_perf.py` (PF-01–PF-06, Split-Screen- und Koop-Host-Rechnung) |
| Neue Kanon-Einträge | CANON §256 (Plattformprofile), §257 (Frame- und Speicherbudgets), §258 (Q6 Split-Screen, Koop-Host, Streaming), §259 (Messung, Gates, Optimierungskatalog); CR-009 (Switch-2-Bildrate und GI-Begriff) |

---

## Inhalt

1. [Ziele](#1-ziele)
2. [Plattformprofile](#2-plattformprofile)
3. [Frame-Budgets](#3-frame-budgets)
4. [Speicher-Budgets](#4-speicher-budgets)
5. [Streaming und Ladezeiten](#5-streaming-und-ladezeiten)
6. [Split-Screen – Entscheidung Q6 – und Koop-Host](#6-split-screen--entscheidung-q6--und-koop-host)
7. [Switch 2](#7-switch-2)
8. [PC](#8-pc)
9. [Messung und Performance-Gates](#9-messung-und-performance-gates)
10. [Optimierungskatalog](#10-optimierungskatalog)
11. [Prüfregeln](#11-prüfregeln)
12. [Anforderungen an andere Abteilungen](#12-anforderungen-an-andere-abteilungen)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Ziele

| Ziel | Bedeutung | Messbar an |
|---|---|---|
| **PZ-1 Stabil vor hoch** | Gleichmäßige Bildzeiten sind wichtiger als Spitzenwerte; Frame-Pacing ohne Mikroruckler | 99. Perzentil der Bildzeit ≤ 1,25 × Ziel |
| **PZ-2 60 fps auf PS5, Xbox, PC** | CANON §2: 60 fps auf allen Plattformen | Erkundung und Kampf im Budget (PF-01) |
| **PZ-3 Switch 2 stabil** | Gesperrte 30 fps mit DLSS, Handheld und TV | PF-01 mit 33,3 ms |
| **PZ-4 Keine Shader-Ruckler** | PSO-Vorkompilierung, keine Kompilierung im Spiel | 0 PSO-Treffer ohne Cache in Testläufen |
| **PZ-5 Kurze Ladezeiten** | Start, Laden, Schnellreise schnell; kein Ladebildschirm in der offenen Welt | §5 |
| **PZ-6 Messbar** | Jeder Bereich hat ein Budget mit Owner; Überschreitungen fallen im CI auf | Performance-Gates (§9) |

---

## 2. Plattformprofile

| DisplayName | TargetFps | InternalRes | OutputRes | Upscaler | AvailableMB | MainGridRange | EchoActors | NpcActors | SplitScreen | CoopHostMax | Rendering |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PlayStation 5 | 60 | 1440p (dyn. 1152p–1620p) | 4K | TSR | 12500 | 768 | 40 | 60 | ja (30 fps, Qualitätsprofil Split) | 4 | Lumen SW, Nanite, VSM |
| Xbox Series X | 60 | 1440p (dyn. 1152p–1620p) | 4K | TSR | 13500 | 768 | 40 | 60 | ja (30 fps, Qualitätsprofil Split) | 4 | Lumen SW, Nanite, VSM |
| Xbox Series S | 60 | 900p (dyn. 720p–1080p) | 1440p | TSR | 8000 | 640 | 32 | 48 | ja (30 fps, Profil Split-S) | 4 | Lumen SW (reduziert), Nanite, VSM |
| Nintendo Switch 2 | 30 | Docked 1080p / Handheld 720p (dyn.) | Docked 1440p–4K / Handheld 1080p | DLSS | 9000 | 512 | 16 | 24 | nein (lokales Funk-Koop mit zwei Konsolen) | 2 | TOD-Irradiance + SSGI, Nanite reduziert, VSM aus (Cascades) |
| PC Mindestanforderung | 60 | 1080p Niedrig (Renderskalierung 50–67 %) | 1080p | TSR/FSR/DLSS/XeSS | 12000 | 640 | 32 | 48 | ja (30 fps) | 4 | Lumen SW niedrig, Nanite, VSM |
| PC Empfohlen | 60 | 1440p Hoch | 1440p–4K | TSR/FSR/DLSS/XeSS | 20000 | 768 | 40 | 60 | ja (60 fps) | 4 | Lumen SW/HW (optional), Nanite, VSM |

Die Xbox Series S ist die engste der aktuellen Konsolen: gleiche CPU-Klasse wie die Series X, aber deutlich weniger GPU-Leistung und Speicher. AETHRIS behandelt sie nicht als Sonderfall, sondern als eigenes Profil mit niedrigerer interner Auflösung und kleinerem Textur-Pool; alle Spielfunktionen einschließlich Split-Screen bleiben erhalten.

**Hinweise:** Die verfügbaren Speichermengen sind Planungsannahmen; maßgeblich sind die Werte der Entwicklungskits. Die Profile sind **eine** Codebasis mit Skalierbarkeitsgruppen (`DefaultScalability.ini` je Plattform) – keine getrennten Inhalte. Die Actor-Grenzen für Echos und NPCs stammen aus K52/K53 und K57 §9.4.

---

## 3. Frame-Budgets

### 3.1 Überblick

Jeder Thread hat je Plattform ein Budget. Die Summe darf **85 % der Bildzeit** nicht überschreiten (PF-01) – die übrigen 15 % sind Reserve für Spitzen, Betriebssystem und Messungenauigkeit. Szenario *Erkundung* ist die offene Welt mit voller Vegetation; *Kampf (Worst Case)* ist ein Trio-Kampf mit Crescendo im Gewitter (K58 §8.2) mit dem **Kampfring-Profil** (Foliage-Dichte 50 %, reduziertes Final Gather außerhalb des Rings).

| Thread / Szenario | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. |
|---|---|---|---|---|---|---|
| Zielbildrate (Bildzeit) | 60 fps (16,7 ms) | 60 fps (16,7 ms) | 60 fps (16,7 ms) | 30 fps (33,3 ms) | 60 fps (16,7 ms) | 60 fps (16,7 ms) |
| Game Thread | 12,0 ms (72 %) | 12,0 ms (72 %) | 12,8 ms (77 %) | 20,2 ms (61 %) | 13,0 ms (78 %) | 10,4 ms (62 %) |
| Render Thread | 7,9 ms (47 %) | 7,9 ms (47 %) | 8,0 ms (48 %) | 15,5 ms (46 %) | 8,6 ms (52 %) | 7,0 ms (42 %) |
| Audio Thread | 1,5 ms (9 %) | 1,5 ms (9 %) | 1,5 ms (9 %) | 2,5 ms (7 %) | 2,0 ms (12 %) | 1,5 ms (9 %) |
| GPU Erkundung | 13,8 ms (83 %) | 13,8 ms (83 %) | 13,8 ms (83 %) | 22,5 ms (68 %) | 13,8 ms (83 %) | 12,9 ms (77 %) |
| GPU Kampf (Worst Case) | 14,0 ms (84 %) | 14,0 ms (84 %) | 14,0 ms (84 %) | 22,2 ms (67 %) | 14,0 ms (84 %) | 13,3 ms (80 %) |

### 3.2 Game Thread

| Posten | Szenario | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. | Quelle |
|---|---|---|---|---|---|---|---|---|
| Spielfigur, Traversal, Interaktion, Kamera | ALL | 1,5 | 1,5 | 1,6 | 2,6 | 1,6 | 1,2 | K40 |
| Animation (Game-Thread-Anteil inkl. Motion Matching ≤ 0,25/0,45) | ALL | 1,2 | 1,2 | 1,3 | 2,2 | 1,3 | 1,0 | K57 |
| Ökologie (Mass-Prozessoren, Actor-Wechsel) | ALL | 1,6 | 1,6 | 1,7 | 2,2 | 1,7 | 1,4 | K52 (CANON §216) |
| NPC-Tagesabläufe, Crowd, Barks | ALL | 1,2 | 1,2 | 1,3 | 1,8 | 1,3 | 1,0 | K53 |
| Kampf, Zeitleiste, Kampf-KI | ALL | 0,8 | 0,8 | 0,9 | 1,4 | 0,9 | 0,7 | K31, K34 |
| Quests, Bedingungs-Index, Ereignisbus | ALL | 0,3 | 0,3 | 0,3 | 0,5 | 0,3 | 0,3 | K48 |
| UI (CommonUI, MVVM) | ALL | 0,8 | 0,8 | 0,8 | 1,2 | 0,9 | 0,7 | K54 (CANON §208) |
| Chaos-Physik, Kollision, Wasser | ALL | 1,0 | 1,0 | 1,1 | 1,8 | 1,1 | 0,9 | K65 |
| World Partition, Level Instances, Data Layers | ALL | 1,0 | 1,0 | 1,1 | 2,0 | 1,1 | 0,9 | K08 |
| Iris-Replikation (Koop-Host 4 Spieler) | ALL | 0,5 | 0,5 | 0,5 | 0,8 | 0,5 | 0,4 | K59 |
| Save (amortisiert, Spitze zeitlich verteilt) | ALL | 0,1 | 0,1 | 0,1 | 0,2 | 0,1 | 0,1 | K64 |
| Engine-Grundlast, Tick, GC (inkrementell) | ALL | 2,0 | 2,0 | 2,1 | 3,5 | 2,2 | 1,8 | K05 |

### 3.3 Render Thread und Audio

| Posten | Szenario | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. | Quelle |
|---|---|---|---|---|---|---|---|---|
| Szene (Sichtbarkeit, Draw-Aufbau, Nanite-Culling-Aufträge) | ALL | 4,5 | 4,5 | 4,6 | 9,0 | 4,9 | 4,0 | K57 |
| UI-Rendering | ALL | 0,6 | 0,6 | 0,6 | 1,0 | 0,6 | 0,5 | K54 (CANON §208) |
| Niagara-Verwaltung | ALL | 0,8 | 0,8 | 0,8 | 1,5 | 0,9 | 0,7 | K58 |
| Post, Upscaler-Setup, Sonstiges | ALL | 2,0 | 2,0 | 2,0 | 4,0 | 2,2 | 1,8 | K65 |

| Posten | Szenario | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. | Quelle |
|---|---|---|---|---|---|---|---|---|
| Audio-Render (MetaSounds, Mix) | ALL | 1,5 | 1,5 | 1,5 | 2,5 | 2,0 | 1,5 | K55 |

### 3.4 GPU

| Posten | Szenario | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. | Quelle |
|---|---|---|---|---|---|---|---|---|
| Nanite + Virtual Shadow Maps | EXPLORE | 3,6 | 3,6 | 3,6 | 7,5 | 3,6 | 3,4 | K57 |
| Globale Beleuchtung (Lumen; Switch 2: TOD-Irradiance + SSGI) | EXPLORE | 3,8 | 3,8 | 3,8 | 3,0 | 3,8 | 3,6 | K15, ADR-070 |
| Foliage (WPO, Gras) | EXPLORE | 1,2 | 1,2 | 1,2 | 2,5 | 1,2 | 1,1 | K09 |
| Himmel, Wolken, Nebel, Wasser | EXPLORE | 1,6 | 1,6 | 1,6 | 3,0 | 1,6 | 1,5 | K15 |
| VFX (Erkundung typisch) | EXPLORE | 1,2 | 1,2 | 1,2 | 2,0 | 1,2 | 1,1 | K58 |
| Post-Process + Upscaler (TSR; Switch 2: DLSS) | ALL | 1,8 | 1,8 | 1,8 | 3,5 | 1,8 | 1,7 | K65 |
| UI-Komposition | ALL | 0,6 | 0,6 | 0,6 | 1,0 | 0,6 | 0,5 | K54 |
| Nanite + VSM (Kampfring-Profil) | COMBAT | 2,8 | 2,8 | 2,8 | 6,0 | 2,8 | 2,6 | K65 |
| GI (Kampfring-Profil, reduziertes Final Gather) | COMBAT | 3,0 | 3,0 | 3,0 | 2,5 | 3,0 | 2,8 | K65 |
| Foliage (Kampfring: Dichte 50 %) | COMBAT | 0,6 | 0,6 | 0,6 | 1,2 | 0,6 | 0,6 | K65 |
| Himmel, Nebel, Wetter | COMBAT | 1,2 | 1,2 | 1,2 | 2,5 | 1,2 | 1,1 | K65 |
| VFX Worst Case (Trio, Crescendo) | COMBAT | 4,0 | 4,0 | 4,0 | 5,5 | 4,0 | 4,0 | K58 (CANON §230) |

**Lesart:** Die GPU ist auf PS5/Xbox der engste Bereich (83–84 % in beiden Szenarien). Die Dynamik der Auflösung (TSR mit Zielbildzeit) gleicht Spitzen aus; das Kampfring-Profil gibt im Kampf genau das Budget frei, das die VFX benötigen. Auf Switch 2 ist die GPU bei 30 fps gut ausgelastet (≈ 68 %) und der Game Thread der engste Bereich (61 % von 33,3 ms) – bei 60 fps (16,7 ms) läge allein der Game Thread mit 20,2 ms weit darüber.

### 3.5 Spitzen (Hitches)

Durchschnittswerte reichen nicht; einzelne lange Bilder zerstören das Spielgefühl stärker als ein etwas niedrigerer Mittelwert. Deshalb gelten Regeln für Spitzen:

| Quelle | Regel |
|---|---|
| Garbage Collection | inkrementell, ≤ 1 ms je Bild; vollständige Durchläufe nur bei Ladebildschirmen |
| Streaming | Actor-Spawns zeitlich verteilt (≤ 2 ms je Bild), Level-Instance-Aktivierung über mehrere Bilder |
| Shader | PSO-Precaching; fehlende PSOs werden asynchron kompiliert und das Objekt bis dahin mit Ersatzmaterial gezeigt |
| Echo-Spawns | Actor-Pools (8 je Archetyp), Wechsel Mass → Actor höchstens 2 je Bild |
| Save | Fragmente zeitlich verteilt; Autosave nie im Kampf (K64) |
| Kampfstart | Vorwärmen der Kampf-Vorlagen (VFX, Audio, Animation) während des Übergangs |

Ziel: Kein einzelnes Bild über 2 × Zielbildzeit in automatisierten Flügen und Kampf-Benches.

---

## 4. Speicher-Budgets

| Posten | PS5 | Xbox Series X | Xbox Series S | Switch 2 | PC Min | PC Empf. |
|---|---|---|---|---|---|---|
| Textur-Streaming-Pool | 2.400 | 2.600 | 1.200 | 1.700 | 1.500 | 3.500 |
| Nanite/Meshes/HLOD | 1.400 | 1.500 | 800 | 1.100 | 1.000 | 2.000 |
| Geladene Zellen, Actors, Level Instances | 1.400 | 1.500 | 1.000 | 1.300 | 1.300 | 1.800 |
| Animation (Clips, Pose-Search-Datenbank, AnimToTexture) | 500 | 500 | 350 | 400 | 450 | 600 |
| Audio (Banken, Streaming-Puffer) | 450 | 450 | 300 | 220 | 500 | 500 |
| Niagara (Partikel, Puffer) | 250 | 250 | 150 | 150 | 200 | 350 |
| Mass-Fragmente, Population | 200 | 200 | 150 | 150 | 200 | 250 |
| UI (Atlanten, Schriften inkl. CJK) | 220 | 220 | 200 | 200 | 220 | 250 |
| Gameplay, Definitionen, Daten | 600 | 600 | 550 | 550 | 650 | 700 |
| Render-Ziele, GBuffer, Lumen-/VSM-Caches | 1.400 | 1.500 | 750 | 900 | 1.000 | 2.000 |
| Engine, Code, Allokator-Reserve | 800 | 800 | 650 | 700 | 900 | 900 |
| **Σ** | **9.620** | **10.120** | **6.100** | **7.370** | **7.920** | **12.850** |
| verfügbar (Annahme) | 12.500 | 13.500 | 8.000 | 9.000 | 12.000 | 20.000 |
| Auslastung | 77 % | 75 % | 76 % | 82 % | 66 % | 64 % |

Die Einzelplatz-Auslastung liegt bewusst bei 64–82 %: Die Reserve trägt Koop-Host (bis zu vier Streaming-Quellen) und Split-Screen (§6). Der Textur-Streaming-Pool ist der flexible Posten: Er wird bei Engpässen per Mip-Bias reduziert, bevor andere Systeme betroffen sind.

| Regel | Festlegung |
|---|---|
| Speicherbericht | Nächtlich je Plattform (Memreport, LLM-Tags je Posten) gegen `MemoryBudgets.csv` |
| Fragmentierung | Feste Pools für Echos (Actor-Pool 8 je Archetyp, K52), NPCs und Partikel; Garbage Collection inkrementell |
| Out-of-Memory | Nie Absturz durch Inhalte: Streaming-Pool reduziert, HLOD früher, Mass statt Actors – Telemetrie-Ereignis `Perf.MemoryPressure` |

---

## 5. Streaming und Ladezeiten

| Kennzahl | PS5 / Xbox Series X | Xbox Series S | Switch 2 | PC (SSD) |
|---|---|---|---|---|
| Spielstart bis Titel | ≤ 12 s | ≤ 15 s | ≤ 20 s | ≤ 15 s |
| Spielstand laden | ≤ 8 s | ≤ 10 s | ≤ 18 s | ≤ 10 s |
| Schnellreise | ≤ 4 s | ≤ 5 s | ≤ 10 s | ≤ 5 s |
| Hain betreten | ≤ 4 s (vorgeladen, CANON GameFlow) | ≤ 4 s | ≤ 8 s | ≤ 4 s |
| Gleiten mit Höchsttempo | kein Nachladen sichtbar | kein Nachladen sichtbar | ggf. HLOD länger sichtbar | kein Nachladen sichtbar |

**Grundlagen:** World Partition mit MainGrid 128 m (Ladebereich 768 m, Switch 2 512 m, CANON §43), HLOD in drei Ebenen (K57 §9), One File Per Actor, Data Layers für Story-Zustände. Die Switch 2 liest von Spielkarte oder internem Speicher langsamer als die SSDs der anderen Konsolen; deshalb kleinerer Ladebereich, aggressivere HLOD-Nutzung und das Vorladen von Zielzellen bei Schnellreise (Ladebildschirm mit Weltlied-Motiv statt schwarzem Bild).

**Gleiten und Flugreiten** sind der Streaming-Härtetest: Bei 18 m/s in Windströmen (CANON Traversal) erreicht die Spielfigur alle 7 s eine neue Zelle. Die Streaming-Quelle des Spielers wird deshalb in Bewegungsrichtung um bis zu 200 m vorgeschoben (geschwindigkeitsabhängig).

### 5.1 Installationsgröße

| Bereich | PS5 / Xbox Series X | Xbox Series S | Switch 2 | PC |
|---|---|---|---|---|
| Welt (Nanite-Geometrie, Landschaft, HLOD) | 38 GB | 30 GB | 18 GB | 40 GB |
| Texturen | 30 GB | 18 GB | 12 GB | 34 GB (inkl. 4K-Paket optional) |
| Echos und Charaktere | 12 GB | 9 GB | 6 GB | 12 GB |
| Animation (inkl. Zwischensequenzen) | 8 GB | 8 GB | 5 GB | 8 GB |
| Audio (Musik, Rufe, Sprachausgabe 2 Sprachen standard) | 9 GB | 9 GB | 5 GB | 9 GB |
| Weitere Sprachpakete (je Sprache) | ≈ 2 GB, optional | ≈ 2 GB | ≈ 1,2 GB | ≈ 2 GB |
| Sonstiges (Daten, Shader-Caches, UI) | 3 GB | 3 GB | 2 GB | 5 GB |
| **Σ (ohne Zusatzsprachen)** | **≈ 100 GB** | **≈ 77 GB** | **≈ 48 GB** | **≈ 108 GB** |

Ziele: Konsolen ≤ 100 GB, Switch 2 auf einer 64-GB-Spielkarte. Sprachausgabe wird nach Systemsprache installiert, weitere Sprachen laden auf Wunsch nach. Patches folgen dem Container-Layout (IoStore-Chunks je Region), damit ein Daten-Patch nicht die ganze Welt neu herunterlädt.

---

## 6. Split-Screen – Entscheidung Q6 – und Koop-Host

### 6.1 Rechnung

Lokales Split-Screen bedeutet zwei Ansichten mit zwei Streaming-Quellen. Das Modell (`aethris_perf.py split`) rechnet mit 30 fps (Split-Screen-Ziel), GPU-Faktor 1,6 (Geometrie und Post doppelt, GI- und Schatten-Caches teilweise geteilt), Render-Thread-Faktor 1,5, doppelter Streaming-Last und +35 % Weltspeicher plus +50 % Render-Ziele:

| Plattform | GPU (×1,6) | Render (×1,5) | Game (+Streaming) | Speicher (+35 % Welt, +50 % Render-Ziele) | Budget 30 fps (85 %) | machbar |
|---|---|---|---|---|---|---|
| PS5 | 22,1 ms | 11,8 ms | 13,0 ms | 10.810 / 11.250 MB | 28,3 ms | ✅ |
| Xbox Series X | 22,1 ms | 11,8 ms | 13,0 ms | 11.395 / 12.150 MB | 28,3 ms | ✅ |
| Xbox Series S | 22,1 ms | 12,0 ms | 13,9 ms | 6.825 / 7.200 MB | 28,3 ms | ✅ |
| Switch 2 | 36,0 ms | 23,2 ms | 22,2 ms | 8.275 / 8.100 MB | 28,3 ms | ❌ |
| PC Min | 22,1 ms | 12,9 ms | 14,1 ms | 8.875 / 10.800 MB | 28,3 ms | ✅ |
| PC Empf. | 20,6 ms | 10,5 ms | 11,3 ms | 14.480 / 18.000 MB | 28,3 ms | ✅ |

### 6.2 Entscheidung Q6

**Split-Screen-Koop für 2 Spieler** gibt es auf **PS5, Xbox Series X, Xbox Series S und PC** mit **30 fps** und eigenem Qualitätsprofil (Renderskalierung je Ansicht 70 %, Foliage-Dichte 70 %, Lumen-Qualität mittel). Auf der **Switch 2** reicht die GPU nicht (36 ms > 28,3 ms) und der Speicher wird knapp; dort gibt es stattdessen **lokales Funk-Koop mit zwei Konsolen** (Listen-Server im lokalen Netz, K59) – dasselbe Spielerlebnis auf zwei Bildschirmen.

| Regel | Festlegung |
|---|---|
| Spielerzahl | 2 lokal; zusätzlich Online-Gäste möglich (max. 4 gesamt, Host = Split-Screen-Konsole) |
| Profil | Gast im Split-Screen spielt mit eigenem Profil (Plattform-Konto) oder als Gast-Profil (Fortschritt über Gast-Protokoll, K59 §6.4) |
| Ansicht | Vertikal geteilt (Standard) oder horizontal; UI je Hälfte skaliert (K54 Textgrößen bleiben lesbar) |
| Kämpfe | gemeinsamer Kampfbildschirm (Vollbild), beide steuern ihre Echos |
| Priorität | *Should* (K03); Umsetzung ab Alpha, Abnahme in Beta |

### 6.3 Koop-Host-Grenze

Jeder Gast im Koop ist für den Host eine weitere Streaming-Quelle (+35 % Streaming-Last und Weltspeicher je Gast, K59 §4.2):

| Plattform | 2 Spieler (Game / Speicher) | 3 Spieler | 4 Spieler | max. Host |
|---|---|---|---|---|
| PS5 | 12,3 ms / 10.110 MB ✅ | 12,7 ms / 10.600 MB ✅ | 13,1 ms / 11.090 MB ✅ | **4** |
| Xbox Series X | 12,3 ms / 10.645 MB ✅ | 12,7 ms / 11.170 MB ✅ | 13,1 ms / 11.695 MB ✅ | **4** |
| Xbox Series S | 13,2 ms / 6.450 MB ✅ | 13,6 ms / 6.800 MB ✅ | 14,0 ms / 7.150 MB ✅ | **4** |
| Switch 2 | 20,9 ms / 7.825 MB ✅ | 21,6 ms / 8.280 MB ❌ | 22,3 ms / 8.735 MB ❌ | **2** |
| PC Min | 13,4 ms / 8.375 MB ✅ | 13,8 ms / 8.830 MB ✅ | 14,2 ms / 9.285 MB ✅ | **4** |
| PC Empf. | 10,7 ms / 13.480 MB ✅ | 11,0 ms / 14.110 MB ✅ | 11,3 ms / 14.740 MB ✅ | **4** |

Damit bestätigt K65 die vorläufige Grenze aus K59: **Switch-2-Hosts nehmen höchstens 1 Gast** (2 Spieler); ein Switch-2-Spieler kann aber in jede 4er-Gruppe eines anderen Hosts eintreten.

---

## 7. Switch 2

| Thema | Festlegung |
|---|---|
| Bildrate | **30 fps gesperrt** (TV und Handheld), Frame-Pacing über Plattform-API; Menüs und Kampfbildschirm 30 fps (gleichmäßiger Eindruck) |
| Auflösung | TV: intern 1080p dynamisch, DLSS auf 1440p–4K; Handheld: intern 720p dynamisch, DLSS auf 1080p |
| Beleuchtung | TOD-Irradiance-Blending (ADR-070: vorberechnete Sonden je Tageszeit, überblendet) + SSGI für lokale Details; keine Lumen |
| Schatten | Cascaded Shadow Maps statt VSM; Kontaktschatten |
| Geometrie | Nanite mit reduziertem Detail für statische Geometrie (Annahme; Fallback: HLOD-Meshes); Foliage ≤ 400 k Instanzen, Gras ≤ 60 k (CANON §46) |
| Echos/NPCs | 16 Echo-Actors, 24 NPC-Actors (voll), MassNear 120, MassFar 400 (K52) |
| VFX | Profil K58 §8.4 (≈ 30 % der Partikel, keine Partikel-Lichter außer Crescendo) |
| Audio | 96 Stimmen, 220 MB (K55) |
| Akku/Wärme | Handheld: Bildrate fix 30; Leistungsmodus nach Plattformvorgaben; keine unnötigen Hintergrundberechnungen bei Pause (Weltzeit steht, Mass-Prozessoren aus) |
| Speicher | 9.000 MB verfügbar (Annahme), Einzelplatz 82 % |

### 7.1 TV- und Handheld-Modus

| Aspekt | TV (Docked) | Handheld |
|---|---|---|
| Interne Auflösung | 1080p dynamisch (≥ 810p) | 720p dynamisch (≥ 540p) |
| Ausgabe | DLSS auf 1440p, auf 4K-Fernsehern bis 4K | DLSS auf 1080p (Bildschirm) |
| Sichtweite Foliage | 100 % des Switch-2-Profils | 80 % |
| Schatten | Kaskaden 3, Auflösung mittel | Kaskaden 2 |
| UI | TV-Layout (K54) | Handheld-Layout mit größerer Schrift (K54 Textgrößen +1 Stufe Standard) |
| Audio | −16 LUFS | −14 LUFS (K55, Handheld-Lautheit) |

Der Wechsel zwischen TV und Handheld erfolgt nahtlos ohne Ladepause: Die Skalierbarkeitsgruppe wird zur Laufzeit gewechselt, Auflösungsziele passen sich innerhalb von zwei Sekunden an.

**CR-009:** CANON §2 nennt „60 fps auf allen Plattformen; Switch 2 Fallback 30 (Gate: VS-Review)“. Die Budgetrechnung zeigt, dass 60 fps auf Switch 2 nur mit erheblichen Inhaltskürzungen (Ökologie, NPC-Dichte, Sichtweite) erreichbar wären – genau das, was AETHRIS ausmacht. K65 legt deshalb **30 fps als Planungsziel** für Switch 2 fest; das VS-Review (K67) prüft die Annahmen mit echter Hardware. Zugleich präzisiert CR-009 den Begriff aus §221 („SSGI + Lightprobes“): Gemeint ist das TOD-Irradiance-Blending aus ADR-070 (Lichtsonden je Tageszeit) plus SSGI.

---

## 8. PC

| | Mindestanforderung (1080p, Niedrig, 60 fps mit Upscaler) | Empfohlen (1440p, Hoch, 60 fps) |
|---|---|---|
| Betriebssystem | Windows 10/11 64 Bit | Windows 11 64 Bit |
| CPU | 6 Kerne / 12 Threads, Zen 2 oder vergleichbar | 8 Kerne / 16 Threads, Zen 3 oder vergleichbar |
| Arbeitsspeicher | 16 GB | 32 GB |
| Grafik | 6 GB VRAM, DirectX 12, Shader Model 6.6 (Klasse PS5-nah bei reduzierter Auflösung) | 12 GB VRAM |
| Speicher | SSD erforderlich, ≈ 120 GB | NVMe-SSD |
| Upscaler | TSR, FSR, DLSS, XeSS (Wahl im Menü) | wie Min. |

| Thema | Festlegung |
|---|---|
| Einstellungen | Voreinstellungen Niedrig/Mittel/Hoch/Episch + Einzelwerte; Vorschau im Menü; Bildratenbegrenzer; HDR |
| PSO | Vorkompilierung beim ersten Start (Fortschrittsanzeige, im Hintergrund fortgesetzt), PSO-Cache je Treiber |
| Hardware-Raytracing | Optional für Lumen (Episch); nicht erforderlich |
| Handheld-PCs | Ziel: ein Profil nahe Switch 2 (30 fps, 720p intern) für Geräte der Steam-Deck-Klasse |
| Barrierefreiheit | Alle Optionen aus K54 auch auf PC; freie Tastenbelegung |

---

## 9. Messung und Performance-Gates

### 9.1 Werkzeuge

| Werkzeug | Zweck |
|---|---|
| Unreal Insights (Trace) | Thread-Zeiten je Posten, Hitches, Streaming |
| `stat`-Gruppen + LLM | Budgets je Posten (`FrameBudgets.csv`/`MemoryBudgets.csv` als Tags) |
| Automatisierte Flüge | Je Region 3 Kamerarouten (Boden, Gleiten, Flug) + 2 Siedlungsrouten; Zeitmessung je 100 m |
| Kampf-Bench | 6 Kampfszenen (Duell, Trio, Raid, Crescendo, Gewitter, Stillezone) mit festen Seeds |
| Telemetrie | Bildzeit-Histogramme je Plattform und Region (anonymisiert, K59 §10) |

### 9.2 Kampf-Bench

| Szene | Inhalt | Seed | Erwartung (PS5 / Switch 2) |
|---|---|---|---|
| CB-01 Duell | Wildkampf R01, Klar, Tag | 0xA371 | GPU ≤ 12 / 20 ms |
| CB-02 Trio | Arena 6, Kristallfeld | 0xA372 | GPU ≤ 13 / 21 ms |
| CB-03 Raid | RAID_04 Sturmkrone, 4 Spieler (Bots) | 0xA373 | Game ≤ 13 / 22 ms |
| CB-04 Crescendo | Trio, Crescendo Klang, Gewitter | 0xA374 | GPU ≤ 14 / 22,5 ms (Worst Case) |
| CB-05 Gewitter | Duo, Blitzschlag-Runde, Regen | 0xA375 | GPU ≤ 13,5 / 22 ms |
| CB-06 Stillezone | Duell in Stillezone (Entsättigung, wenig Partikel) | 0xA376 | GPU ≤ 11 / 19 ms |

Jede Szene läuft nächtlich auf allen Plattformen; die Ergebnisse fließen in denselben Bericht wie die Flüge.

### 9.3 Gates

| Meilenstein (K67) | Anforderung |
|---|---|
| Vertical Slice | R01 auf PS5 im Budget (Erkundung + Kampf); Switch-2-Messung für CR-009 |
| Alpha | Alle Regionen auf PS5/Xbox Series X ≤ 100 % Budget; Switch 2 ≤ 115 % |
| Beta | Alle Plattformen ≤ 100 %; 99. Perzentil ≤ 1,25 × Ziel; 0 PSO-Ruckler in Flügen |
| Release-Kandidat | Wie Beta, plus Speicher ≤ 90 % in Koop-Host-Szenarien |

Überschreitungen im nächtlichen Lauf erzeugen automatisch Tickets beim Owner des Postens; drei Nächte in Folge über Budget blockieren Merges in den betroffenen Bereich (K05 CI).

---

## 10. Optimierungskatalog

| Bereich | Maßnahme | Kapitel |
|---|---|---|
| Echos | Significance-LOD, URO, AnimToTexture ab 150 m, Impostor > 500 m, Actor-Pools | K52, K57 |
| NPCs | Distanzstufen, Mass-Crowd > 150 m, Tagesplan deterministisch (nur Abweichungen simuliert) | K53 |
| Welt | Nanite, HLOD 3 Ebenen, Packed Level Instances, PCG gebacken, Foliage-Budgets | K57 |
| Licht | Lumen-Profile je Region, Kampfring-Profil, Switch 2 TOD-Irradiance | K15, K65 |
| VFX | Budgets je Kategorie, Effektdichte, GPU-Simulation, Pooling | K58 |
| Audio | Stimmenbudget, Banken je Region | K55 |
| UI | MVVM ohne Tick, Invalidierungs-Boxen, Atlanten | K54 |
| Gameplay | Kein Tick per Default (CANON §28), Ereignisbus, Bedingungs-Index für Quests | K06, K48 |
| Speicher | Mip-Bias bei Druck, LLM-Tags, Pools | K65 |
| Shader | ≤ 250 Permutationen je Plattform, PSO-Precaching | K57 |

---

## 11. Prüfregeln

`tools/ref/aethris_perf.py validate`:

| Regel | Inhalt |
|---|---|
| PF-01 | Summe je Thread und Szenario ≤ 85 % der Bildzeit |
| PF-02 | Speicher ≤ 90 % des verfügbaren Spielspeichers |
| PF-03 | Budgets stimmen mit den Kanon-Werten der Fachkapitel überein (Ökologie, NPC, UI, VFX, Audio) |
| PF-04 | Split-Screen-Profil = Machbarkeitsrechnung |
| PF-05 | Koop-Host-Grenze = Rechnung |
| PF-06 | Profile vollständig |

**Ergebnis:** Prüfregeln PF-01–PF-06: **0 Verstöße**. 29 Frame-Posten, 11 Speicherposten, 6 Profile; Split-Screen machbar auf PS5, Xbox Series X, Xbox Series S, PC Min, PC Empf.; Koop-Host maximal: PS5 4, Xbox Series X 4, Xbox Series S 4, Switch 2 2, PC Min 4, PC Empf. 4.

---

## 12. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Alle Systeme | Eigene Posten in `FrameBudgets.csv` einhalten; LLM-/Insights-Tags | alle |
| Level Design | Flugrouten je Region pflegen; Sichtachsen ohne Überladung | K08–K10 |
| Technical Art | Kampfring-Profil, Switch-2-Profile, Permutationsbudget | K57 |
| Netzwerk | Koop-Host-Grenze Switch 2 = 2 durchsetzen; lokales Funk-Koop | K59 |
| UI | Split-Screen-Layouts, Einstellungsmenü PC | K54 |
| QA | Performance-Gates, Kampf-Bench, Plattform-Matrix | K66 |
| Produktion | Switch-2-Messung im VS-Review (CR-009) | K67 |

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-273 | Budgets als Daten mit 15 % Reserve und Prüfregel | Messbar, Owner je Posten, CI-fähig | Budgets nur in Dokumenten |
| ADR-274 | Kampfring-Profil (Foliage 50 %, reduziertes Final Gather außerhalb) | VFX-Spitzen ohne Auflösungseinbruch | globale Qualitätsreduktion im Kampf |
| ADR-275 | Q6: Split-Screen 2 Spieler mit 30 fps auf PS5, Xbox Series X\|S, PC; Switch 2 lokales Funk-Koop | Rechnung (GPU, Speicher) | Split-Screen überall; gar kein lokales Koop |
| ADR-276 | Switch 2: 30 fps gesperrt als Planungsziel (CR-009), DLSS, TOD-Irradiance + SSGI | Inhalte (Ökologie, Dichte) bleiben erhalten | 60 fps mit Inhaltskürzung |
| ADR-277 | Switch-2-Koop-Host max. 2 Spieler (bestätigt) | Speicher bei weiteren Streaming-Quellen | 4 Spieler mit reduzierter Welt |
| ADR-278 | Performance-Gates je Meilenstein mit automatischen Tickets und Merge-Sperre nach 3 Nächten | Früh erkennen, Verantwortung klar | manuelle Performance-Pässe am Ende |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §256 | Plattformprofile (`PlatformProfiles.csv`): PS5/XSX 60 fps 1440p dyn. TSR, XSS 60 fps 900p dyn., Switch 2 30 fps DLSS (TV 1080p→1440p–4K, Handheld 720p→1080p), PC Min/Empf. 60 fps; Mindest-/Empfohlene PC-Hardware | LOCKED |
| §257 | Frame-Budgets (`FrameBudgets.csv`, ≤ 85 % Bildzeit je Thread/Szenario; Kampfring-Profil) und Speicher-Budgets (`MemoryBudgets.csv`, ≤ 90 % verfügbar; Einzelplatz 64–82 %) | LOCKED |
| §258 | Q6: Split-Screen 2 Spieler (30 fps) auf PS5, Xbox Series X\|S, PC; Switch 2 lokales Funk-Koop; Koop-Host max. 4 (Switch 2: 2); Ladezeiten-Ziele; Streaming-Vorschub bis 200 m in Bewegungsrichtung | LOCKED (schließt Q6) |
| §259 | Messwerkzeuge, automatisierte Flüge und Kampf-Bench, Performance-Gates VS/Alpha/Beta/RC, Optimierungskatalog | LOCKED |
| §2 | CR-009: FPS-Ziel Switch 2 = 30 fps (Planung; VS-Review bestätigt); GI-Begriff „SSGI + Lightprobes“ (§221) = TOD-Irradiance-Blending (ADR-070) + SSGI | LOCKED (ändert §2, präzisiert §221) |
| Q-Liste | Q6 geschlossen (→ §258) | – |
| §10 | ADR-273 – ADR-278 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] Ziele PZ-1–PZ-6
- [x] Plattformprofile für 6 Zielsysteme
- [x] Frame-Budgets je Thread/Szenario/Plattform (berechnet, ≤ 85 %)
- [x] Speicher-Budgets (berechnet, ≤ 90 %)
- [x] Streaming und Ladezeiten
- [x] Q6 entschieden (Rechnung), Koop-Host-Grenze bestätigt
- [x] Switch 2 und PC im Detail, CR-009
- [x] Messung, Gates, Optimierungskatalog
- [x] Prüfregeln PF-01–PF-06 (0 Verstöße), Anforderungen
- [x] ADR-273 – ADR-278, CANON §256–§259

➡️ **Nächstes Kapitel: K66 – QA und Tests.**
