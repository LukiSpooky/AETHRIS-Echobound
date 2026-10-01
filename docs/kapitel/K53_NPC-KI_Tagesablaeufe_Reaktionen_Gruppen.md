# K53 · NPC-KI: Tagesabläufe, Reaktionen, Gruppen

| Feld | Wert |
|---|---|
| Dokument | Kapitel 53 von 68 · Lebendige Welt II |
| Version | 1.0 |
| Owner | Lead AI Engineer |
| Mitwirkende | Narrative Designer (Barks), Level Design (Smart Objects), Technical Animator, Gameplay Programmer (Mass Crowds), Audio |
| Baut auf | K11–K13 (Städte, Dörfer, Bevölkerung, Tagesablauf-Muster, Siedlungszustände), K14/K15 (Wetter, Spieluhr), K44–K51 (Story-Zustände, Quests, Folgen), K47 (Ruf × Haltung), K52 (Wildechos, Sim-LOD), CANON §53, §56 (Dialog-Präsentation), §60, ADR-056 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/World/Npcs.csv` (NPC-Register, 194 NPCs), `SchedulePatterns.csv`, `NpcReactions.csv`, `BarkTriggers.csv`, `tools/gen_npcs.py` (Register + Validator NP-01–NP-05), `GF_AI/Public/Npc/NpcScheduleTypes.h` (+ `.cpp`) |
| Neue Kanon-Einträge | CANON §201 (NPC-Klassen und Register), §202 (Tagesabläufe), §203 (Reaktionen und Gruppen), §204 (Barks), §205 (Technik) |

---

## Inhalt

1. [Leitbild](#1-leitbild)
2. [NPC-Klassen](#2-npc-klassen)
3. [Das NPC-Register](#3-das-npc-register)
4. [Tagesabläufe](#4-tagesabläufe)
5. [Orte und Smart Objects](#5-orte-und-smart-objects)
6. [Reaktionen](#6-reaktionen)
7. [Barks](#7-barks)
8. [Gruppen](#8-gruppen)
9. [Story- und Weltzustände](#9-story--und-weltzustände)
10. [Wärter und Prüfer](#10-wärter-und-prüfer)
11. [Technik](#11-technik)
12. [Validierung und Debug](#12-validierung-und-debug)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Leitbild

> *Wer in Eichenhall um zwölf Uhr den Wurzelkrug betritt, findet Wendel beim Mittagessen – und Wendel weiß, dass der Wärter gestern die Brücke in Fennhaven gebaut hat.*

NPCs in AETHRIS sind Menschen mit Arbeit, Pausen, Gewohnheiten und Meinungen. Sie reagieren auf Wetter, auf Echos, auf das, was der Spieler getan hat, und auf das, was in der Welt geschehen ist. Drei Prinzipien:

| Prinzip | Bedeutung |
|---|---|
| **Plan vor Zufall** | Jeder benannte NPC folgt einem Tagesablauf; Abweichungen haben einen sichtbaren Grund (Wetter, Fest, Quest, Kampf) |
| **Erinnern statt erzählen** | Folgen von Quests und Story erscheinen als Barks, Orte und Gesten – nicht als Textfenster |
| **Wenige Benannte, viele Lebendige** | Lore-Einwohner ≠ dargestellte NPCs (ADR-056): Benannte NPCs tragen Geschichten, Mass-Bevölkerung trägt Atmosphäre |

---

## 2. NPC-Klassen

| Klasse | Beispiele | Anzahl | Simulation | Darstellung |
|---|---|---|---|---|
| **Story** | Ysolde, Kael, Venn, Sereth, Hralda, Tavesh, Marieke | 9 | StateTree, eigene Szenen | voll vertont |
| **Arenameister** | Maelis, Torvik, Evhe, Shirah, Kaldrex, Beke, Sigrun, Aevrin, Ilyx, Oruma | 10 | StateTree, Trainingszeiten | voll vertont |
| **Quest-NPC** | Pell, Fenja, Ennis, Jorn, Wiebke, Ivra … | ~80 | StateTree (benannt) | Kernzeilen vertont |
| **Händler** | Wendel, Odo, Tavi, Seren … | 55 (K42) | StateTree, Öffnungszeiten | Kernzeilen vertont |
| **Dorf-Schlüssel** | Hedda, Jost, Svala, Halla … (CANON §57) | 23 | StateTree | Kernzeilen vertont |
| **Prüfer/Kämpfer** | Klanprüfer, Gezeitenprüfer, Sternprüfer | ~25 | StateTree (Kampfbereitschaft) | Barks |
| **Rollen-NPC** | Wachen, Fährleute, Marktschreier (unbenannt) | je Siedlung | leichter Actor | Barks |
| **Mass-Bevölkerung** | Passanten, Kinder, Arbeiter | Budget je Stadt (CANON §53) | Mass + Zone Graph | Gesten, Ambient-Barks < 25 m |

---

## 3. Das NPC-Register

Alle benannten NPCs stehen in `Data/World/Npcs.csv`. Das Register wird **aus den Daten erzeugt** (`tools/gen_npcs.py`): aus Hauptquest-Schritten, Nebenquest-Auftraggebern und -Schritten, Händlern (K11/K12), Arenen, Fraktionen (K47) und den Dorf-Schlüssel-NPCs (CANON §57). Feste Angaben für Story-Figuren stehen im Generator; alles andere wird abgeleitet:

| Feld | Ableitung |
|---|---|
| Heimatort | häufigster Ort, an dem der NPC in Quests auftritt (Siedlung/Kloster), sonst Zone |
| Fraktion | häufigste Fraktion der Nebenquests, die der NPC vergibt; Zellen der Freien Stimmen → F04 |
| Muster | Fraktion (Akademie → Gelehrt, Wildwacht → Wache, Orden → Kloster, Freie Stimmen → Nachtvolk), Beruf (Fischer, Hirte, Kind), Ort (Morvenfurt/Qasr Sahrun → Nachtvolk, Kharsholm/Schlackenwehr → Schicht, Ashurim → Karawane), Nachtladen → Nachtvolk; sonst Tagwerk |
| Darstellung | Orden im Kloster → Schiefertafel (Schweigegelübde, CANON §55); Prüfer, Zellen → Barks; sonst vertont |
| Aliasse | Händler-IDs aus K11/K12, die dieselbe Person bezeichnen (z. B. `NPC_R08_PELL` → `NPC_PELL`) |

| Art | Anzahl |
|---|---|
| Quest-NPC | 71 |
| Händler | 50 |
| Prüfer/Kämpfer | 25 |
| Dorf-Schlüssel | 23 |
| Arenameister | 10 |
| Story | 9 |
| Gruppe (Zelle) | 6 |
| **Σ** | **194** |

| Muster | NPCs |
|---|---|
| Tagwerk | 71 |
| Wache | 40 |
| Nachtvolk | 29 |
| Gelehrt | 21 |
| Schicht | 15 |
| Fischer | 8 |
| Kloster | 5 |
| Karawane | 2 |
| Hirte | 2 |
| Kind | 1 |

| Region | NPCs |
|---|---|
| R01 | 26 |
| R02 | 21 |
| R03 | 17 |
| R04 | 22 |
| R05 | 18 |
| R06 | 27 |
| R07 | 23 |
| R08 | 16 |
| R09 | 11 |
| R10 | 13 |

### 3.1 Story-Figuren und Arenameister

| ID | Name | Fraktion | Heimat | Muster | Darstellung | Quests |
|---|---|---|---|---|---|---|
| NPC_ELSBETH_MOOR | Rätin Elsbeth Moor | – | Eichenhall | Tagwerk | Voiced | 0 |
| NPC_HRALDA | Hralda Brakk | F03 | Eichenhall | Wache | Voiced | 2 |
| NPC_KAEL | Kael Duran | F01 | Lindwiesen | Gelehrt | Voiced | 2 |
| NPC_MARIEKE | Marieke Holm | F02 | Saltrand-Hafen | Tagwerk | Voiced | 7 |
| NPC_SERETH | Sereth Vaun | F05 | LOC_KLOSTER_SCHWEIGFELS | Kloster | Voiced | 2 |
| NPC_TAVESH | Tavesh Amaru | F04 | Morvenfurt | Nachtvolk | Voiced | 4 |
| NPC_ULREK | Ulrek | F05 | LOC_KLOSTER_SCHWEIGFELS | Kloster | Voiced | 1 |
| NPC_VENN | Aldric Venn | F01 | Dorunsruh | Gelehrt | Voiced | 3 |
| NPC_YSOLDE | Ysolde Varn | F03 | Lindwiesen | Wache | Voiced | 4 |

| ID | Name | Fraktion | Heimat | Muster | Darstellung | Quests |
|---|---|---|---|---|---|---|
| NPC_AEVRIN | Aevrin Thal | F01 | Dorunsruh | Gelehrt | Voiced | 9 |
| NPC_BEKE | Beke Tamsen | – | Saltrand-Hafen | Fischer | Voiced | 1 |
| NPC_EVHE | Evhe Corrach | – | Morvenfurt | Nachtvolk | Voiced | 2 |
| NPC_ILYX | Ilyx Brannoc | – | Prismara | Tagwerk | Voiced | 3 |
| NPC_KALDREX | Kaldrex Vorn | – | Schlackenwehr | Schicht | Voiced | 1 |
| NPC_MAELIS | Maelis Wendt | – | Eichenhall | Tagwerk | Voiced | 1 |
| NPC_ORUMA | Oruma Siyel | – | Aerion | Tagwerk | Voiced | 2 |
| NPC_SHIRAH | Shirah Harrad | – | Qasr Sahrun | Nachtvolk | Voiced | 2 |
| NPC_SIGRUN | Sigrun Fjall | – | Hvitmark | Tagwerk | Voiced | 1 |
| NPC_TORVIK | Torvik Hrall | – | Kharsholm | Schicht | Voiced | 1 |

### 3.2 Dorf-Schlüssel (CANON §57)

| ID | Name | Fraktion | Heimat | Muster | Darstellung | Quests |
|---|---|---|---|---|---|---|
| NPC_AMA_DUVRETH | Moorweise Ama Duvreth | – | Duvreth | Tagwerk | Voiced | 0 |
| NPC_BRIDA | Köhlerin Brida | – | Moosgrund | Tagwerk | Voiced | 0 |
| NPC_BRUDER_ODVAR | Bruder Odvar | F05 | Säulenrast | Kloster | Voiced | 1 |
| NPC_DR_IMKE_VAEL | Dr. Imke Vael | – | Thae'Luun | Gelehrt | Voiced | 2 |
| NPC_EBBA | Ebba | – | Treibdorf Flottholm | Tagwerk | Voiced | 0 |
| NPC_HALLA | Halla | – | Eiðvik-Neu | Tagwerk | Voiced | 1 |
| NPC_HEDDA | Bäckerin Hedda | – | Lindwiesen | Tagwerk | Voiced | 0 |
| NPC_IMRAN | Imran | – | Wanderdorf Ashurim | Karawane | Voiced | 0 |
| NPC_JOST | Müller Jost | – | Lindwiesen | Tagwerk | Voiced | 0 |
| NPC_KESH | Dünenbauer Kesh | – | Mirsaan | Tagwerk | Voiced | 0 |
| NPC_LEIF | Leif | – | Fjallstad | Tagwerk | Voiced | 1 |
| NPC_LORCAN | Lorcan | – | Fennhaven | Tagwerk | Voiced | 0 |
| NPC_MALVA | Kurwirtin Malva | – | Kaldra | Tagwerk | Voiced | 0 |
| NPC_MARLENE | Marlene | – | Tangwerft | Tagwerk | Voiced | 0 |
| NPC_NADIRA | Brunnenwächterin Nadira | – | Harrâd | Wache | Voiced | 0 |
| NPC_OKKO | Okko | – | Möwenhuk | Tagwerk | Voiced | 0 |
| NPC_SCHLEIFERIN_NYX | Schleiferin Nyx | – | Quarzgrund | Tagwerk | Voiced | 1 |
| NPC_STEIGER_BRANNOC | Steiger Brannoc d. Ä. | F03 | Glanzschacht | Wache | Voiced | 3 |
| NPC_STERNWAERTER_ELUN | Sternwärter Elun | F01 | Lumeya | Gelehrt | Voiced | 3 |
| NPC_SVALA | Hirtin Svala | – | Hrallsted | Hirte | Voiced | 0 |
| NPC_THESSA | Thessa | – | Vorthax | Tagwerk | Voiced | 0 |
| NPC_ULF_BRAKK | Ulf Brakk | – | Brakkfels | Tagwerk | Voiced | 1 |
| NPC_WINDSEGLERIN_RIA | Windseglerin Ria | – | Wolkenrast | Fischer | Voiced | 2 |

### 3.3 Quest-NPCs

| ID | Name | Fraktion | Heimat | Muster | Darstellung | Quests |
|---|---|---|---|---|---|---|
| NPC_AELTESTE_INGRID | Aelteste Ingrid | – | Brakkfels | Tagwerk | Voiced | 1 |
| NPC_AILSA | Fährmeisterin Ailsa Duvreth | – | Morvenfurt | Fischer | Voiced | 1 |
| NPC_BAUMEISTERIN_IRIS | Baumeisterin Iris | – | Aerion | Tagwerk | Voiced | 1 |
| NPC_BOTENJUNGE_LUTZ | Botenjunge Lutz | – | Saltrand-Hafen | Tagwerk | Voiced | 1 |
| NPC_BRANDA | Bergführerin Branda | – | Grollhorn-Biwak | Tagwerk | Voiced | 2 |
| NPC_BRUECKENWART_ELWYN | Brückenwart Elwyn | – | Fennhaven | Wache | Voiced | 1 |
| NPC_EISHAENDLER_BJARNE | Eishaendler Bjarne | – | Hvitmark | Tagwerk | Voiced | 1 |
| NPC_ENNIS | Ennis Rook | F04 | Moosgrund | Nachtvolk | Voiced | 8 |
| NPC_FENJA | Zeugmeisterin Fenja | F03 | Eichenhall | Wache | Voiced | 5 |
| NPC_FEUERTRAEGER_KNUT | Feuertraeger Knut | – | Hrallsted | Tagwerk | Voiced | 1 |
| NPC_FISCHERIN_TJARKE | Fischerin Tjarke | – | Möwenhuk | Fischer | Voiced | 1 |
| NPC_FORSCHERIN_LIV | Meeresforscherin Liv | – | Riffposten | Gelehrt | Voiced | 2 |
| NPC_FORSCHER_IDRIS | Forscher Idris | – | Plateau-Lager | Gelehrt | Voiced | 1 |
| NPC_FOTOGRAFIN_SIGNE | Fotografin Signe | – | Hvitmark | Gelehrt | Voiced | 1 |
| NPC_GAERTNERIN_SOLA | Gärtnerin Sola | F03 | Aerion | Wache | Voiced | 1 |
| NPC_GELEHRTE_OONA | Gelehrte Oona | F01 | Morvenfurt | Gelehrt | Voiced | 3 |
| NPC_GIESSER_BRAM | Glockengießer Bram | – | Schlackenwehr | Schicht | Voiced | 1 |
| NPC_GLETSCHERWART_TORA | Gletscherwartin Tora | F03 | Gletscherwacht | Wache | Voiced | 3 |
| NPC_GLYPHENSTUDENTIN_MAREK | Glyphenstudent Marek | – | Thae'Luun | Gelehrt | Voiced | 1 |
| NPC_GRABUNGSHELFER_TAMIR | Grabungshelfer Tamir | – | Wanderdorf Ashurim | Karawane | Voiced | 1 |
| NPC_GUNNHILD | Gunnhild | F05 | LOC_KLOSTER_SCHWEIGFELS | Kloster | SlateWritten | 0 |
| NPC_HAENDLER_BRISK | Haendler Brisk | – | R01_Z03 | Tagwerk | Voiced | 1 |
| NPC_HIRTE_HALVAR | Hirte Halvar | F03 | Fjallstad | Wache | Voiced | 1 |
| NPC_HIRTIN_NAJLA | Hirtin Najla | – | Wanderdorf Ashurim | Hirte | Voiced | 1 |
| NPC_IMKERIN_HILDE | Imkerin Hilde | – | Lindwiesen | Tagwerk | Voiced | 2 |
| NPC_KIND_TAMSIN | Tamsin | F01 | Dorunsruh | Gelehrt | Voiced | 2 |
| NPC_KONTORAGENTIN_RIEKE | Kontoragentin Rieke | F02 | Prismara | Tagwerk | Voiced | 2 |
| NPC_KRATERWART_OSK | Kraterwart Osk | – | Kraterrand-Posten | Wache | Voiced | 1 |
| NPC_KRISTALLKUNDLERIN_MAJA | Kristallkundlerin Maja | – | Kaldra | Tagwerk | Voiced | 1 |
| NPC_KUTSCHERIN_ALMA | Kutscherin Alma | – | Brakkfels | Tagwerk | Voiced | 1 |
| NPC_LABORLEITERIN_SANNE | Laborleiterin Sanne | F01 | Prismara | Gelehrt | Voiced | 3 |
| NPC_LANDBESITZER_GRIM | Landbesitzer Grim | – | R05_Z02 | Tagwerk | Voiced | 1 |
| NPC_LEHRERIN_DALIA | Lehrerin Dalia | – | Mirsaan | Tagwerk | Voiced | 1 |
| NPC_LEHRLING_MIKKEL | Akademie-Lehrling Mikkel | – | Erzgrat-Hütte | Gelehrt | Voiced | 1 |
| NPC_LEUCHTWART_FOKKE | Leuchtwart Fokke | – | Leuchtfelsen-Wacht | Wache | Voiced | 1 |
| NPC_LINA | Lina | – | Lindwiesen | Kind | Voiced | 1 |
| NPC_LUND | Grabungsleiterin Saphira Lund | F01 | Glasebene-Turm | Gelehrt | Voiced | 4 |
| NPC_MAREN | Maren | – | Lindwiesen | Tagwerk | Voiced | 1 |
| NPC_MESSER_HAKON | Messmeister Hakon | F01 | Kharsholm | Gelehrt | Voiced | 2 |
| NPC_NOTAR_BASIM | Notar Basim | – | Mirsaan | Tagwerk | Voiced | 1 |
| NPC_ORDENSANHAENGERIN_SOLVEIG | Ordensanhaengerin Solveig | – | Hvitmark | Tagwerk | Voiced | 1 |
| NPC_ORDENSPOSTEN_BRUDER_EIK | Ordensposten Bruder Eik | – | R07_Z03 | Tagwerk | Voiced | 1 |
| NPC_OSSIAN | Kontorschreiber Ossian | F02 | Eichenhall | Tagwerk | Voiced | 3 |
| NPC_PASSWART_JORN | Passwart Jorn | F03 | Passwacht Nord | Wache | Voiced | 10 |
| NPC_PELL | Archivarin Pell | F01 | Eichenhall | Gelehrt | Voiced | 5 |
| NPC_PERLENSCHLEIFERIN_ANKE | Perlenschleiferin Anke | – | Saltrand-Hafen | Tagwerk | Voiced | 1 |
| NPC_PROFESSOR_ALBRECHT | Professor Albrecht | – | Dorunsruh | Gelehrt | Voiced | 1 |
| NPC_R07_ASTRID | Sprecherin Astrid Eiðsen | – | Hvitmark | Tagwerk | Voiced | 2 |
| NPC_RAGNA | Kapitänin Ragna | F02 | Saltrand-Hafen | Fischer | Voiced | 4 |
| NPC_SALZMEISTERIN_FARAH | Salzmeisterin Farah | – | Harrâd | Tagwerk | Voiced | 2 |
| NPC_SALZSIEDER_OLE | Salzsieder Ole | – | Tangwerft | Tagwerk | Voiced | 1 |
| NPC_SCHMIEDIN_ISOLDE | Schmiedin Isolde | – | Vorthax | Schicht | Voiced | 1 |
| NPC_SCHULDNER_ROAN | Schuldner Roan | – | Morvenfurt | Nachtvolk | Voiced | 1 |
| NPC_SCHWESTER_IVRA | Schwester Ivra | F05 | LOC_KLOSTER_SCHWEIGFELS | Kloster | SlateWritten | 12 |
| NPC_SIEGELSCHNEIDER_EDO | Siegelschneider Edo | – | Möwenhuk | Tagwerk | Voiced | 1 |
| NPC_SIGGA | Sigga | – | Brakkfels | Tagwerk | Voiced | 1 |
| NPC_STADTRAETIN_MAIRE | Stadtraetin Maire | – | Morvenfurt | Nachtvolk | Voiced | 1 |
| NPC_STAMMGAST_ALDO | Stammgast Aldo | – | Schlackenwehr | Schicht | Voiced | 1 |
| NPC_STEINBRECHER_ARNULF | Steinbrecher Arnulf | – | R01_Z04 | Tagwerk | Voiced | 1 |
| NPC_STIMMER_JOREN | Stimmer Joren | – | Glanzschacht | Tagwerk | Voiced | 1 |
| NPC_STUDENTIN_HELKE | Studentin Helke | F01 | Dorunsruh | Gelehrt | Voiced | 2 |
| NPC_TANGSAMMLERIN_GESA | Tangsammlerin Gesa | – | Tangwerft | Fischer | Voiced | 1 |
| NPC_TORBEN | Holzfäller Torben | – | Uralthain-Lager | Tagwerk | Voiced | 1 |
| NPC_TORFSTECHER_BRAN | Torfstecher Bran | – | Duvreth | Tagwerk | Voiced | 1 |
| NPC_UHRMACHER_ODIL | Uhrmacher Odil | – | Säulenrast | Tagwerk | Voiced | 2 |
| NPC_WAERTERIN_GRETE | Waerterin Grete | – | Hvitmark | Tagwerk | Voiced | 1 |
| NPC_WANDERER_PIET | Wanderer Piet | – | Passwacht Nord | Tagwerk | Voiced | 1 |
| NPC_WIEBKE | Prokuristin Wiebke | F02 | Saltrand-Hafen | Tagwerk | Voiced | 5 |
| NPC_WILDWAECHTERIN_EILA | Wildwächterin Eila | F03 | Aschehütte | Wache | Voiced | 2 |
| NPC_WILDWAECHTER_BOAZ | Wildwächter Boaz | F03 | Archontenwacht | Wache | Voiced | 3 |
| NPC_WITWE_ALKE | Alke | – | Möwenhuk | Tagwerk | Voiced | 1 |

### 3.4 Budget benannter NPCs je Stadt

| Stadt | Benannte NPCs (Register, ohne Prüfer) | Budget (CANON §53) | Reserve für Ambient-Benannte |
|---|---|---|---|
| Eichenhall | 12 | 48 | 36 |
| Kharsholm | 7 | 40 | 33 |
| Morvenfurt | 11 | 42 | 31 |
| Qasr Sahrun | 7 | 44 | 37 |
| Schlackenwehr | 9 | – | – |
| Saltrand-Hafen | 12 | 52 | 40 |
| Hvitmark | 12 | – | – |
| Dorunsruh | 10 | – | – |
| Prismara | 7 | – | – |
| Aerion | 8 | – | – |

Die Reserve füllt Level Design mit benannten Ambient-NPCs (Namen, Tagesablauf, 3–6 Barks, keine Quest) – sie tragen die Stadt, ohne das Register zu überfrachten. Prüfer und Kämpfer zählen nicht zum Budget (sie sind nur zu Prüfungszeiten anwesend).

---

## 4. Tagesabläufe

Die Muster aus K11 §3.2 werden erweitert und als Daten geführt (`SchedulePatterns.csv`). Eine Spielstunde dauert 3 Echtzeitminuten (CANON §65).

| Muster | Wofür | Ablauf (Spielstunden) |
|---|---|---|
| **Tagwerk** | Händler, Handwerk (K11 §3.2) | 00–05 Schlafen · 05–08 Aufstehen · 08–12 Arbeit · 12–14 Essen · 14–18 Arbeit · 18–22 Gasthaus · 22–24 Schlafen |
| **Schicht** | Gruppe A/B/C wechselt um 6/14/22 Uhr (Kharsholm, Schlackenwehr) | 00–05 Schlafen · 05–06 Aufstehen · 06–14 Arbeit · 14–15 Essen · 15–19 Freizeit · 19–21 Gasthaus · 21–24 Schlafen |
| **Nachtvolk** | Morvenfurt, Qasr Sahrun, Freie Stimmen | 00–04 Markt · 04–05 Arbeit · 05–07 Zuhause · 07–14 Schlafen · 14–16 Aufstehen · 16–18 Essen · 18–20 Arbeit · 20–24 Markt |
| **Wache** | Wildwacht, Stadtwache, Prüfer | 00–05 Streife · 05–06 Wachwechsel · 06–07 Essen · 07–12 Streife · 12–14 Essen · 14–18 Streife · 18–19 Wachwechsel · 19–24 Schlafen |
| **Gelehrt** | Akademie | 00–01 Lesen · 01–08 Schlafen · 08–12 Vorlesung · 12–14 Essen · 14–18 Labor · 18–22 Bibliothek · 22–24 Lesen |
| **Kloster** | Orden der Stille (Stille Stunden 4–6, 12, 18–20) | 00–04 Schlafen · 04–06 Stille Stunde · 06–11 Arbeit · 11–12 Essen · 12–13 Stille Stunde · 13–18 Arbeit · 18–20 Stille Stunde · 20–21 Essen · 21–24 Schlafen |
| **Fischer** | Küste, Seen, Fähren | 00–03 Schlafen · 03–04 Aufstehen · 04–09 Fischen · 09–12 Markt · 12–13 Essen · 13–16 Schlafen · 16–19 Arbeit · 19–21 Fischen · 21–23 Gasthaus · 23–24 Schlafen |
| **Hirte** | Herden, Weiden | 00–05 Schlafen · 05–06 Aufstehen · 06–12 Hüten · 12–13 Essen · 13–19 Hüten · 19–21 Zuhause · 21–24 Schlafen |
| **Kind** | Kinder | 00–07 Schlafen · 07–08 Aufstehen · 08–12 Unterricht · 12–13 Essen · 13–19 Spielen · 19–21 Zuhause · 21–24 Schlafen |
| **Karawane** | Wanderdorf Ashurim, Karawanen | 00–04 Schlafen · 04–09 Reise · 09–14 Rast · 14–18 Reise · 18–21 Markt · 21–22 Gasthaus · 22–24 Schlafen |

**Schichtgruppen:** Muster „Schicht“ und „Wache“ verwenden Gruppen A/B/C mit 8 h Versatz (`Aethris::Npc::ActivityAt`). Jede Gruppe ist in der Stadt sichtbar unterwegs – um 6, 14 und 22 Uhr wechseln Ströme von Arbeitern über die Kettenbrücken von Kharsholm.

**Abweichungen (benannte NPCs):** Jeder benannte NPC kann Stunden überschreiben (z. B. Maelis trainiert 6–7 Uhr mit Echos; Rätin Elsbeth Moor tagt am ersten Tag jeder Spielwoche, K11 §4). Abweichungen stehen in den NPC-Assets, nicht im Muster.

**Händler:** Öffnungszeiten (`Merchants.csv`) haben Vorrang vor dem Muster; außerhalb der Öffnungszeit ist der Händler auffindbar (Gasthaus, Zuhause) und verkauft nicht. Nachtläden gehören immer zu „Nachtvolk“ oder „Fischer“ (NP-04).

---

## 5. Orte und Smart Objects

Tätigkeiten werden über **Smart Objects** an Orten ausgeführt. Jede Siedlung bietet je Tätigkeit genügend Slots (Level Design, K57):

| Tätigkeit | Smart Objects | Slots je Stadt (Ziel) |
|---|---|---|
| Arbeit | Werkbank, Theke, Amboss, Netzflickplatz, Pult, Feld | Arbeitsplätze = Arbeiter × 1,1 |
| Essen | Tisch (Gasthaus, Mensa, Zuhause), Garküche | Sitzplätze ≥ 40 % der Bevölkerung im Sichtradius |
| Gasthaus/Markt | Theke, Stand, Bühne, Laternensteg | 1 je 6 NPCs |
| Streife | Wegpunktkette (Zone Graph), Wachturm | 2 Routen je Wache |
| Stille Stunde | Gebetsbank (Schweigfels, Kapellen) | Ordensleute × 1 |
| Spielen | Brunnenrand, Wiese, Steg | 1 je Kind + 2 |
| Schutz suchen | Vordach, Torbogen, Markise, Höhleneingang | Bevölkerung im Freien × 0,7 |

Belegte Slots werden reserviert („Claim“); findet ein NPC keinen Slot, nimmt er die nächstbeste Tätigkeit derselben Kategorie (z. B. Stehen statt Sitzen).

---

## 6. Reaktionen

Reaktionen überschreiben den Plan kurzzeitig. Sie sind als Daten geführt; Chance und Dauer sind ganzzahlig, die Auswahl erfolgt deterministisch je NPC (Hash aus NPC-ID, Spieltag, Reiz), damit Koop-Gäste dasselbe sehen.

| Stimulus | Kind | ChancePermille | Reaction | DurationMin | Notes |
|---|---|---|---|---|---|
| Weather=Rain | * | 600 | SeekShelter | 0 | Unterstände (CANON §62: Regen 60 %) |
| Weather=Thunderstorm | * | 850 | SeekShelter | 0 | Gewitter 85 % |
| Weather=Heatwave & Hour 11–16 | * | 1000 | Siesta | 0 | Siesta (CANON §62) |
| Weather=Sandstorm | * | 1000 | GoHome | 0 | Tore zu (CANON §62) |
| Weather=Ashfall | * | 800 | SeekShelter | 0 | Masken auf (Animation) |
| Weather=Snow | Tagwerk|Hirte|Kind | 400 | Play/Shovel | 20 | Kinder spielen |
| Weather=ResonanceStorm | * | 700 | WatchSky | 10 | Zeigen zum Himmel |
| Kampf < 40 m | * | 700 | Watch | 0 | Zuschauen; Kinder werden weggezogen |
| Kampf < 15 m | * | 900 | Flee | 0 | Rückzug hinter Deckung |
| Aggressives Wildecho < 25 m | * | 1000 | Flee | 0 | Wachen greifen ein (Wache-Muster) |
| Spieler läuft durch Gruppe | * | 500 | StepAside | 0 | Ausweichen + Blick |
| Spieler reitet XL-Echo < 10 m | * | 600 | StepBack | 0 | Staunen |
| Begleiter-Echo frei < 6 m | Kind|Tagwerk | 500 | Pet | 1 | Streicheln (wenn Echo Temperament ≠ Scheu) |
| Spieler gibt Item (Interaktion) | * | 1000 | Thank | 0 | Dank-Animation |
| Fest (Siedlungszustand/Kalender) | * | 900 | Celebrate | 60 | Musik |
| Stillezone < 200 m | * | 600 | Worry | 0 | Gedämpfte Barks |
| Story-Flag FLAG_W6_DONE | Gelehrt | 500 | Gossip | 10 | Akademie-Gespräche in Gruppen |
| Hour 19–21 | Nachtvolk|Fischer | 1000 | LightLanterns | 15 | Laternen anzünden (Morvenfurt |

### 6.1 Prioritäten

```
Kampf/Bedrohung (Flucht, Wache greift ein)
  > Story-Szene oder Quest-Schritt mit diesem NPC
    > Wetter (Schutz, Siesta, Tore zu)
      > Fest/Ereignis (Siedlungszustand, Kalender)
        > Spielerinteraktion (Ausweichen, Blick, Streicheln, Dank)
          > Tagesplan
```

### 6.2 Reaktionen auf den Spieler

| Handlung des Spielers | NPC |
|---|---|
| Nähert sich (< 6 m) | Blick, Gruß-Bark beim ersten Mal am Spieltag |
| Läuft durch eine Gruppe | Ausweichen, kurzer Kommentar |
| Reitet ein XL-Echo | Zurücktreten, Staunen; Kinder winken |
| Begleiter-Echo frei | Kinder/Tagwerk streicheln es (nicht bei scheuem Temperament) |
| Steht lange vor einem Händler | Händler spricht an (einmal je Besuch) |
| Kämpft in der Stadt | Nicht möglich außer in Arenen/Prüfungen; Wildechos werden von Wachen vertrieben |
| Diebstahl/Gewalt gegen NPCs | gibt es nicht (keine Systeme dafür, ADR-007-Geist) |

---

## 7. Barks

Barks sind kurze Zeilen im Vorbeigehen. CANON §38 plant ~4.000 Barks; K48/K49–K51 ergänzen 3–6 Barks je Nebenquest (Tag `Quest.<ID>.After`), K46 ~1.200 Ende-Barks.

| Name | Trigger | Priority | CooldownMin | GlobalCooldownS | RangeM | Example |
|---|---|---|---|---|---|---|
| BARK_GREET | Spieler nähert sich (erstes Mal am Spieltag) | 4 | 240 | 6 | 6 | „Morgen |
| BARK_STORY_STATE | Story-Zustand geändert (Wahrheit/Akt/Ende) | 1 | 1440 | 4 | 10 | „Hast du gehört? Die Akademie…“ (nach W6) |
| BARK_QUEST_AFTER | Nebenquest abgeschlossen (Quest.<ID>.After) | 2 | 720 | 5 | 10 | „Seit der Wärter die Brücke gebaut hat…“ |
| BARK_REP_HIGH | Rufrang ≥ 4 der NPC-Fraktion (K47 §9.3) | 3 | 480 | 6 | 8 | „Für dich immer |
| BARK_REP_STANCE | Story-Haltung zur Fraktion (Flag) | 3 | 480 | 6 | 8 | „Du hilfst uns mehr |
| BARK_WEATHER | Wetterwechsel | 3 | 120 | 8 | 12 | „Regen. Gut für die Rillos.“ |
| BARK_ECHO_COMMENT | Begleiter-Echo des Spielers sichtbar | 4 | 180 | 8 | 6 | „Was für ein schönes Chimbal!“ |
| BARK_COMBAT_NEARBY | Kampf in < 40 m | 2 | 30 | 4 | 40 | „Pass auf |
| BARK_STORM | Resonanzsturm beginnt | 1 | 1440 | 3 | 30 | „Die Echos singen alle zugleich… hörst du das?“ |
| BARK_SETTLEMENT_STATE | Siedlungszustand steigt (K13 §5) | 2 | 1440 | 5 | 15 | „Endlich wieder ein Fest!“ |
| BARK_RUMOR | Gerücht über Nebenquest der Region (K48 §9.2) | 3 | 360 | 10 | 8 | „Im Moor soll ein Irrlicht weiß leuchten…“ |
| BARK_SCHEDULE | Tätigkeitswechsel (Mittag |  Feierabend) | 5 | 0 | 12 | 5 |
| BARK_SILENCE_ZONE | Stillezone in < 200 m | 1 | 720 | 6 | 15 | „Da drüben… alles grau.“ |
| BARK_ENDING | Nachhall-Variante je Ende | 2 | 1440 | 5 | 10 | „Seit dem neuen Lied klingen die Glocken anders.“ |

### 7.1 Auswahl

```
Kandidaten ← alle Barks des NPCs, deren Bedingung erfüllt ist (Bedingungssprache K48 §6)
Kandidaten ← Kandidaten ohne aktiven Cooldown (NPC-Cooldown in Spielminuten, globaler Cooldown in Echtzeit-Sekunden)
wähle höchste Priorität; bei Gleichstand: am längsten nicht gespielt; dann deterministisch nach Hash(NPC, Spieltag)
spiele; setze Cooldowns; protokolliere „gehört“ (jede Zeile höchstens 3× je Spielstand, außer Begrüßungen)
```

### 7.2 Bark-Schichten

| Schicht | Tag-Wurzel | Umfang (Ziel) | Kapitel |
|---|---|---|---|
| Allgemein (Wetter, Tageszeit, Echos) | `Bark.General.*` | 900 | K53 |
| Region/Stadt | `Bark.Region.R##.*` | 600 | K09–K13 |
| Story (je Wahrheit, Akt, Ende) | `Story.*` | 1.200 (davon Enden 1.200 aufgeteilt auf beide) | K44–K46 |
| Fraktion (Rang × Haltung) | `Faction.*` | 500 | K47 |
| Nebenquest danach | `Quest.SQ###.After` | 210 × 4 ≈ 840 | K49–K51 |
| **Summe** | | **~4.000** (+ 1.200 Ende-Varianten) | |

Barks sind in 12 Sprachen untertitelt; vertont werden die Schichten „Story“, „Fraktion“ und „Allgemein“ in 5 Sprachen (CANON §24).

---

## 8. Gruppen

| Gruppe | Mitglieder | Verhalten | Beispiel |
|---|---|---|---|
| **Gesprächsgruppe** | 2–4 | Kreis, Gesten, wechselnde Sprecher (Ambient-Dialog 20–40 s) | Studierende nach W6 (RX_STORY_W6) |
| **Familie** | 2–5 | Gemeinsamer Tagesplan, Kinder folgen Eltern | Lindwiesen-Familien |
| **Karawane** | 4–12 + Lastechos | Reist zwischen Lagerplätzen (Ashurim-Route alle ~18 Spielstunden, CANON §57) | Wanderdorf Ashurim |
| **Streife** | 2 | Wegpunktkette, Wachwechsel um 5/18 Uhr | Wildwacht, Stadtwache |
| **Prozession** | 6–20 | Gesten statt Worte, langsamer Gleichschritt | Orden nach W6 (Kapellen, Akt III) |
| **Arbeitskolonne** | 6–15 | Schichtstrom über feste Wege | Kharsholm, Schlackenwehr |
| **Festgesellschaft** | Siedlung | Tanz, Musik, Stände | Lindenfest, Glockenflut, Unterstadt-Fest |

Gruppen nutzen den Zone Graph (Fußwege, Plätze) und halten Abstand mit denselben ganzzahligen Steuerregeln wie Echo-Gruppen (K52 §7.1, Separation 60 cm).

---

## 9. Story- und Weltzustände

NPCs lesen Zustände über die Bedingungssprache (K48 §6); jeder benannte NPC hat Zustandsvarianten:

| Zustand | Wirkung auf NPCs |
|---|---|
| Wahrheit W1–W9 | Barks, Gesprächsthemen; z. B. nach W6 meiden Akademie-NPCs das Rektorat |
| Akt | Präsenz (z. B. Kael bis W6 im Labor, CANON §54; Venn ab Nachhall in Schweigfels) |
| Ende (`FLAG_ENDING`) | Nachhall-Barks, Kleidung (Sanfte Stille: silberne Bänder), Feste |
| Flags (Kael, Sereth, Freie Stimmen, Kontor) | Ton und Anwesenheit (z. B. Tavesh in Aerion nur bei `FLAG_SHELTER` = FS) |
| Siedlungszustand 0/1/2 | Bedroht: weniger NPCs draußen, sorgenvolle Barks; Blühend: Fest, zusätzlicher Händler (CANON §60) |
| Questfolgen | NPC-Position und Tätigkeit (z. B. Lina wird Wildwacht-Helferin, Ulrek arbeitet für die Wildwacht) |
| Rufrang | Begrüßung, Rabattsatz (K47) |

Zustandswechsel geschehen **außerhalb der Sicht** des Spielers (bei Szenenwechsel, Schlafen, Regionswechsel), damit niemand plötzlich die Kleidung wechselt.

---

## 10. Wärter und Prüfer

Wärter-Kämpfe (Trainer) sind eine wichtige Sol-Quelle (K42: 3 Wärterkämpfe/h) und ein Teil des Weltlebens:

| Typ | Ort | Regel |
|---|---|---|
| **Wandernde Wärter** | Wege, Außenposten | Sichtbar, fordern per Blick + Geste heraus (DR-14); einmal je Spieltag, Revanche ab nächstem Tag |
| **Prüfer** | Arenen, Klanbrücken, Werften | Nur zu Prüfungszeiten anwesend (Muster „Wache“), Quests K49–K51 |
| **Rivale Kael** | Story | K44–K46 |
| **Ordens-/Venn-treue Gegner** | Akt II | Nur in Story-Gebieten, keine Wanderwärter |

Wandernde Wärter haben eine Kampf-KI-Profilstufe nach Zone (Anfänger/Geübt/Veteran, K34) und einen Bark beim Sieg und bei der Niederlage – kein Spott, beide Seiten respektvoll.

---

## 11. Technik

### 11.1 Architektur

```
                   ┌───────────────────────────── GF_AI ─────────────────────────────┐
 Spieluhr (K15) ──►│ NpcScheduleSubsystem ──► StateTree je benanntem NPC ──► Smart Objects
 Wetter (K14)  ──► │        │                       ▲                               │
 Quest/Flags   ──► │        ▼                       │ Reaktionen (NpcReactions.csv) │
 (K48)             │ CrowdSubsystem (Mass + Zone Graph) ── < 25 m ──► leichter Actor │
                   │        │                                                       │
                   │        └──► BarkSubsystem (BarkTriggers.csv, Cooldowns)        │
                   └─────────────────────────────────────────────────────────────────┘
```

| Baustein | Aufgabe |
|---|---|
| `FNpcSchedulePattern`, `Aethris::Npc::ActivityAt` | Muster und Stundenauflösung inkl. Schichtgruppe |
| `UNpcScheduleSubsystem` | Stundenwechsel an alle benannten NPCs; Teleport bei fehlender Sicht, sonst Laufweg |
| StateTree „NPC“ | Zustände: Planaktivität, Reaktion, Szene, Dialog, Bark, Kampf (nur Prüfer/Wärter) |
| `UNpcCrowdSubsystem` | Mass-Bevölkerung, Zone-Graph-Ströme, LOD |
| `UBarkSubsystem` | §7, Lokalisierung, Untertitel, Audio-Prioritäten (K55) |

### 11.2 LOD und Budgets

| Stufe | Abstand | Benannte NPCs | Mass-Bevölkerung |
|---|---|---|---|
| Voll | < 25 m | StateTree 10 Hz, volle Animation, Barks | leichter Actor (Barks, Blick) |
| Nah | 25–80 m | StateTree 2 Hz, reduzierte Animation | Mass, Vertex-Animation |
| Fern | 80–250 m | Plan nur bei Stundenwechsel, Position interpoliert | Mass, ISM |
| Aus | > 250 m oder nicht gestreamt | nur Plan (Stunde → Ort) | entfernt |

**CPU-Budget NPC-KI:** PS5 ≤ 1,2 ms, Switch 2 ≤ 1,8 ms je Frame (Städte bei Spitzenlast, K65). Sichtbare Bevölkerung laut CANON §53 (z. B. Saltrand-Hafen 160 / 80).

### 11.3 Speicherung

`World.Npcs`: nur Abweichungen vom Plan (Questfolgen-Zustand, Position bei dauerhafter Verlegung, gehörte Barks als Bitset). Der Tagesplan selbst wird nie gespeichert – er folgt aus Spieluhr und Muster.

---

## 12. Validierung und Debug

`python3 tools/gen_npcs.py validate`:

| Regel | Prüfung | Ergebnis |
|---|---|---|
| NP-01 | Jeder in Quests und Händlerdaten referenzierte NPC ist im Register (inkl. Aliasse) | ✓ |
| NP-02 | Heimatort existiert (Siedlung, Kloster, Story-POI oder Zone) | ✓ |
| NP-03 | Muster existiert in `SchedulePatterns.csv` | ✓ |
| NP-04 | Nachtläden haben Muster Nachtvolk/Fischer | ✓ |
| NP-05 | Benannte NPCs je Stadt ≤ Budget (CANON §53) | ✓ |

**Zusammenführung von Doppel-IDs:** Beim Aufbau des Registers wurden Quest-IDs, die eine bestehende Händlerin oder einen Händler bezeichneten, auf die kanonischen IDs aus K11/K12 umgestellt (z. B. Wirt Odo → `NPC_R01_ODO`, Sterndeuter Harun → `NPC_R04_HARUN`, Seren Quarz → `NPC_R09_SEREN`); Personen mit eigener Story-ID behalten diese, die Händler-ID wird Alias (`NPC_R08_PELL` → `NPC_PELL`, `NPC_R06_MARIEKE_OFFICE` → `NPC_MARIEKE`).

**Debug** (`Cheat.Npc.*`): Overlay Muster/Aktivität/Reaktion je NPC, Zeitraffer, Bark-Protokoll mit Cooldowns, Smart-Object-Belegung, erzwungene Zustände (Akt, Ende, Siedlungszustand).

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | Smart Objects je Siedlung nach §5; Zone Graph (Wege, Plätze, Unterstände); Reserve-NPCs je Stadt | K57 |
| Narrative | Barks nach §7.2 (~4.000), Zustandsvarianten benannter NPCs (§9) | K55 |
| Animation | Tätigkeitsanimationen (Arbeit je Beruf, Essen, Gasthaus, Stille Stunde, Schutz, Fest), Gesten-Set für Schweigegelübde | K57 |
| Audio | Bark-Priorisierung, Ambient-Dialoge, Stadtklang je Tageszeit | K55 |
| Tech | Subsysteme §11.1, Budgets §11.2 | K65 |
| Save | Fragment `World.Npcs` | K64 |
| QA | Tagesplan-Tests (Zeitraffer 24 h je Stadt), Bark-Wiederholungen, Koop-Konsistenz der Reaktionen | K66 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-201 | NPC-Register wird aus Quest-, Händler-, Arena-, Fraktions- und Dorfdaten generiert; Story-Figuren fest | Eine Quelle der Wahrheit; keine verwaisten NPC-IDs | handgepflegte NPC-Liste |
| ADR-202 | Händler-IDs aus K11/K12 bleiben kanonisch; Mehrfachrollen über Aliasse | Bestehende Daten bleiben gültig, Personen bleiben eins | Umbenennung aller Händler |
| ADR-203 | Reaktionsauswahl deterministisch je (NPC, Spieltag, Reiz) | Koop-Gäste sehen dieselbe Welt | Zufall je Client |
| ADR-204 | Zustandswechsel benannter NPCs nur außerhalb der Sicht | Glaubwürdigkeit, kein „Umziehen“ vor den Augen | sofortige Wechsel |
| ADR-205 | Keine Systeme für Gewalt oder Diebstahl gegen NPCs | Ton und Säulen (ADR-007-Geist), Fokus auf Echos | Kriminalitätssystem |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §201 | NPC-Klassen; Register `Npcs.csv` (generiert, Aliasse, Validator NP-01–05) | LOCKED |
| §202 | Tagesabläufe `SchedulePatterns.csv`: Tagwerk, Schicht (A/B/C, 8 h Versatz), Nachtvolk, Wache, Gelehrt, Kloster, Fischer, Hirte, Kind, Karawane; Öffnungszeiten vor Muster | LOCKED |
| §203 | Reaktionen `NpcReactions.csv` mit Prioritätenkette; Gruppen (Gespräch, Familie, Karawane, Streife, Prozession, Kolonne, Fest) | LOCKED |
| §204 | Barks `BarkTriggers.csv`, Auswahlregel, Schichten (~4.000 + 1.200 Ende-Varianten), höchstens 3× je Zeile | LOCKED |
| §205 | Technik: Schedule-/Crowd-/Bark-Subsysteme, LOD (25/80/250 m), Budgets PS5 1,2 ms / Switch 2 1,8 ms, Save `World.Npcs` | LOCKED |
| §10 | ADR-201 – ADR-205 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] NPC-Klassen und Budgets
- [x] NPC-Register aus allen Datenquellen, Aliasse für Mehrfachrollen, Doppel-IDs bereinigt
- [x] Tagesabläufe als Daten, Schichtgruppen, Händlerzeiten
- [x] Smart Objects und Slot-Ziele
- [x] Reaktionen mit Prioritäten, deterministische Auswahl
- [x] Barks: Auslöser, Auswahl, Umfang
- [x] Gruppen, Story-/Weltzustände, Wärter und Prüfer
- [x] Technik, LOD, Budgets, Save; Validator NP-01–NP-05 (0 Verstöße)
- [x] Anforderungen, ADR-201 – ADR-205, CANON §201–§205

➡️ **Nächstes Kapitel: K54 – UI/UX.**
