# K50 · Nebenquests II (SQ_071–SQ_140): Saltrand II, Sahrun-Weite, Ignareth, Hvitfell I

| Feld | Wert |
|---|---|
| Dokument | Kapitel 50 von 68 · Quest-Bibel, Nebenquests Teil II |
| Version | 1.0 |
| Owner | Lead Quest Designer |
| Mitwirkende | Writer (Saltrand, Sahrun-Weite, Ignareth, Hvitfell), Level Design, Narrative Director (L-01), Sensitivity Review (R04, R07), Systems Designer |
| Baut auf | K48 (Quest-Bibel, Gerüst, Formeln), K49 (Prüfregeln QS-01–QS-15, Ketten), K45 (Akt II, W4–W7), K47 (Fraktionen), K23–K25 (Arten R04, R05, R07), K11–K13 (Orte) |
| Status | ✅ Freigegeben |
| Im Repository | `SideQuestDetails.csv`, `SideQuestSteps.csv` (SQ_071–140, 287 Schritte), `Decor.csv` (+12), Quelle `tools/authoring/sq_k50.py` |
| Neue Kanon-Einträge | CANON §191 (Nebenquests SQ_071–140), §192 (Weltereignisse aus Nebenquests) |

---

## Inhalt

1. [Überblick](#1-überblick)
2. [Akt II in den Nebenquests](#2-akt-ii-in-den-nebenquests)
3. [Saltrand II (R06) – SQ_071–SQ_090](#3-saltrand-ii-r06--sq_071sq_090)
4. [Sahrun-Weite (R04) – SQ_091–SQ_112](#4-sahrun-weite-r04--sq_091sq_112)
5. [Ignareth (R05) – SQ_113–SQ_131](#5-ignareth-r05--sq_113sq_131)
6. [Hvitfell I (R07) – SQ_132–SQ_140](#6-hvitfell-i-r07--sq_132sq_140)
7. [Fraktionsketten in diesem Kapitel](#7-fraktionsketten-in-diesem-kapitel)
8. [Auftraggeber](#8-auftraggeber)
9. [Weltereignisse aus Nebenquests](#9-weltereignisse-aus-nebenquests)
10. [Prüfung gegen die Quest-Bibel](#10-prüfung-gegen-die-quest-bibel)
11. [Anforderungen an andere Abteilungen](#11-anforderungen-an-andere-abteilungen)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Überblick

Die zweiten 70 Nebenquests spielen in den Regionen von Akt II und in der zweiten Hälfte von Saltrand. Der Ton wird ernster: Arbeit und Ausbeutung (Salzgärten, Lager, angekettete Volkets), Erinnerung und Trauer (Eiðvik, die Namen im Polarlicht), Macht und Glas (der Glasreif der Hochkultur als Vorbild Maedryns). Zugleich bleiben die kleinen Geschichten – ein Pyrolm in Isoldes Esse, Snevels, die Köder gegen Eisfiguren tauschen, eine alte Köchin, die ihr Rezeptbuch weitergibt.

| Kennzahl | Wert |
|---|---|
| Quests | 70 |
| Schritte | 287 (Ø 4,1) |
| Ø Dauer | 37 min |
| Σ Spielzeit | 43,1 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 40 (57 %) |
| Σ Sol | 74.600 ◎ |
| Σ Wärter-EP | 134.150 |
| Kategorien | Fraktion 40, Echo-Geschichte 7, Weltereignis 7, Rätsel & Ruinen 5, Wärterprüfung 5, Menschen 3, Forschung 3 |
| Häufigste Zieltypen | Sprechen 62, Beobachten 56, Untersuchen 42, Entscheidung 36, Bedingung 16, Kampf 15, Gehen 12, Traversal 11 |

| Region | Grundton | Wiederkehrende Motive |
|---|---|---|
| Saltrand II | Geschäftig, ehrlich, sturmerprobt | Hafenbücher, die gläserne Route, Netze im Nebel, Leuchtfeuer |
| Sahrun-Weite | Weit, gelehrt, gastfreundlich | Glasebene, Hochkultur-Hymne, Karawanen, Salz und Freiheit |
| Ignareth | Heiß, stolz, schuldbewusst | Zunftgelübde, das Lager und danach, Glockenguss, Ausbrüche |
| Hvitfell I | Still, erinnernd, standhaft | Klangpest, Polarlicht, Gletscher, Venns Briefe |

**Sensitivity:** Sahrun- und Hvitfell-Quests wurden gegen CANON §22 geprüft: Ashurim und Harrâd sind wohlhabende, gebildete, selbstbestimmte Gemeinschaften; Bräuche (Karawanenduell, Nacht der Spiegel, Salzfest) sind eigene Erfindungen ohne Abbild realer Kulturen. Eiðvik-Trauer wird nicht zum Spektakel: Gedenkquests haben Intensität ≤ 3 und keine Kämpfe.

---

## 2. Akt II in den Nebenquests

Die Regionen von Akt II sind frei wählbar; der Verrat (W6) geschieht nach dem sechsten Akkord (K45 ADR-164). Nebenquests müssen deshalb vor **und** nach der Wende funktionieren. Drei Mittel:

| Mittel | Regel | Beispiele |
|---|---|---|
| **W6-Voraussetzung** | Quests, die Venns Rolle voraussetzen, verlangen `Quest.MQ_A2_07` (QS-11) | SQ_095, SQ_097, SQ_099, SQ_121, SQ_132 |
| **Neutrale Fassung** | Quests vor W6 erzählen nur, was Spielende sehen können (Lieferungen, Stillsteine, Grabung), ohne zu deuten | SQ_091, SQ_093, SQ_117, SQ_136 |
| **Spätquest** | Quests in Akt III/Nachhall greifen die Folgen auf | SQ_079, SQ_096, SQ_115, SQ_118, SQ_124, SQ_130, SQ_135, SQ_138 |

Kettenquests mit Einstiegsrang 3–4 (*Hafenbücher*, *Die gläserne Route*, *Salz und Freiheit*, *Glas der Hochkultur*) liegen typischerweise in der zweiten Hälfte von Akt II; *Aevrins Akten* beginnt erst nach W6.

---

## 3. Saltrand II (R06) – SQ_071–SQ_090

Saltrand ist das Herz des Kontors. Die Kette *Hafenbücher* zeigt Marieke Holm als jemand, der Wahrheit statt Schuldige will; *Netze im Nebel* endet mit einer Befreiung ohne Feuer; *Die gläserne Route* verbindet Saltrand mit der Weite.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_071 | Der Leuchtfelsen-Chor | Echo-Geschichte | – | Akt I | 2 | 25 | Time=Night |
| SQ_072 | Zahlen, die nicht klingen | Fraktion | F02 · FQ_F02_03 | Akt I | 3 | 35 | – |
| SQ_073 | Sturmflut | Weltereignis | – | Akt II | 5 | 35 | Weather=Thunderstorm |
| SQ_074 | Das zweite Siegel | Fraktion | F02 · FQ_F02_03 | Akt I | 4 | 35 | – |
| SQ_075 | Die Tangernte | Weltereignis | – | Akt I | 2 | 25 | Moon=Full |
| SQ_076 | Der Agent | Fraktion | F02 · FQ_F02_03 | Akt I | 5 | 40 | Time=Night |
| SQ_077 | Das Wrack der Möwe | Rätsel & Ruinen | – | Akt I | 3 | 30 | – |
| SQ_078 | Vor dem Kontorrat | Fraktion | F02 · FQ_F02_03 | Akt I | 6 | 55 | – |
| SQ_079 | Thal'assyrs Grotte | Rätsel & Ruinen | – | Akt III | 4 | 40 | – |
| SQ_080 | Glas für das Feuer | Fraktion | F02 · FQ_F02_04 | Akt I | 4 | 40 | – |
| SQ_081 | Die Witwe vom Kliff | Menschen | – | Akt I | 3 | 30 | Time=Dusk |
| SQ_082 | Sturm vor Sahrun | Fraktion | F02 · FQ_F02_04 | Akt I | 5 | 50 | Weather=Thunderstorm |
| SQ_083 | Die Perlen der Aquadrals | Forschung | – | Akt I | 3 | 30 | Time=Night |
| SQ_084 | Salz auf grauem Sand | Fraktion | F03 · FQ_F03_04 | Akt I | 4 | 40 | – |
| SQ_085 | Die Probe der Gezeiten | Wärterprüfung | – | Nachhall | 6 | 40 | Moon=Full |
| SQ_086 | Der Leuchtturm schweigt | Fraktion | F03 · FQ_F03_04 | Akt I | 5 | 45 | Time=Day |
| SQ_087 | Die Regatta | Wärterprüfung | – | Akt I | 4 | 30 | Time=Day |
| SQ_088 | Die Perlenwerkstatt | Fraktion | F04 · FQ_F04_03 | Akt I | 5 | 45 | Time=Night |
| SQ_089 | Netze verbrennen | Fraktion | F04 · FQ_F04_03 | Akt I | 6 | 55 | Weather=Fog |
| SQ_090 | Weißes Gold | Fraktion | F04 · FQ_F04_04 | Akt I | 4 | 40 | – |

#### SQ_071 · Der Leuchtfelsen-Chor

*Echo-Geschichte · Akt I · Auftrag: Leuchtwart Fokke (Leuchtfelsen-Wacht) · Intensität 2 · ~25 min*

Nachts singen Glimkins auf dem Leuchtfelsen – Fokke sagt, sie hätten Schiffe gerettet, lange bevor es den Turm gab. Seit das neue Leuchtfeuer brennt, sind sie verstummt. Der Wärter findet heraus, dass das Licht ihren Gesang überstrahlt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Fokke am Turm |
| 2 | Beobachten | Glimkins nachts beobachten |
| 3 | Untersuchen | Den Lichtkegel des Feuers vermessen |
| 4 | Entscheidung | Fokke eine Blende vorschlagen |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_LURE_LANTERN; Kodex-Beobachtung Glimkin
**Folge:** Glimkins singen wieder (Ambient nachts); Leuchtfeuer mit Blende

#### SQ_072 · Zahlen, die nicht klingen

*Fraktion · Goldklang-Kontor · Kette **Hafenbücher** (1/4) · Akt I · Auftrag: Prokuristin Wiebke (Saltrand-Hafen) · Intensität 3 · ~35 min*

Wiebke, Mariekes Prokuristin, findet in den Hafenbüchern Lieferungen, die es nie gab: Fässer, die zweimal verbucht wurden. Marieke will keine Schuldigen, sondern die Wahrheit. Der Wärter zählt im Lagerhaus nach – und ein Brisel zählt mit.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Wiebke im Goldklang-Haupthaus |
| 2 | Untersuchen | Im Lagerhaus nachzählen |
| 3 | Beobachten | Den Lager-Brisel beim Stapeln beobachten |
| 4 | Sprechen | Wiebke berichten |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=3`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F02 +150 · ITM_GEAR_BAG_2; Kontor-Lieferscheine (Lore)
**Folge:** Wiebke führt doppelte Buchprüfung ein (Bark)

#### SQ_073 · Sturmflut

*Weltereignis · Akt II · Auftrag: Taucher Hauke (Saltrand-Hafen) · Intensität 5 · ~35 min*

Bei Gewitter in Akt II drückt eine Sturmflut in die Tangwerft-Bucht. Brisions reiten auf den Wellen und schlagen Boote los. Hauke braucht Hilfe, die Boote zu sichern und ein Tidling-Gelege vor dem Abtreiben zu retten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Gewitter über der Bucht |
| 2 | Beobachten | Den Brision-Zug beobachten |
| 3 | Traversal | Zu den losgerissenen Booten schwimmen |
| 4 | Begleiten | Mit Hauke das Tidling-Gelege bergen |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_GEAR_MASK_3; ITM_CON_HEAL_ALL
**Folge:** Sturmflutmauer in Tangwerft (Data Layer); Hauke-Barks

#### SQ_074 · Das zweite Siegel

*Fraktion · Goldklang-Kontor · Kette **Hafenbücher** (2/4) · Akt I · Auftrag: Prokuristin Wiebke (Saltrand-Hafen) · Intensität 4 · ~35 min*

Die doppelten Fässer tragen zwei Siegel – ein echtes Kontorsiegel und ein gefälschtes. Wiebke vermutet einen Siegelschneider in Möwenhuk. Der Wärter findet ihn: einen alten Mann, der für einen Konsortium-Agenten arbeitet, weil er seine Werkstatt nicht verlieren will.

**Lösungen:** Edo melden · Edo laufen lassen · Edo als Siegelprüfer für das Kontor gewinnen (dritte Lösung, Wiebke-Bark).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Nach Möwenhuk |
| 2 | Untersuchen | Siegelspuren in den Werkstätten finden |
| 3 | Sprechen | Edo befragen |
| 4 | Entscheidung | Was mit Edo geschieht |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=3 & Quest.SQ_072`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F02 +150 · ITM_SEAL_TUNED ×2; Rezept RCP_038
**Folge:** Edo arbeitet für Wiebke oder verlässt die Insel

#### SQ_075 · Die Tangernte

*Weltereignis · Akt I · Auftrag: Tangsammlerin Gesa (Tangwerft) · Intensität 2 · ~25 min*

Bei Springflut legt das Meer die äußeren Tangbänke frei – zwei Stunden lang. Gesa sammelt dann für das ganze Jahr. Doch Tangix haben sich in den Bänken eingenistet. Der Wärter sorgt dafür, dass Ernte und Tangix sich vertragen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Springflut bei Vollmond |
| 2 | Beobachten | Tangix in den Bänken beobachten |
| 3 | Sammeln | Mit Gesa Tang ernten (nur abseits der Nester) |
| 4 | Entscheidung | Gesa eine Erntekarte vorschlagen |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Moon=Full`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_MAT_KELP ×5; ITM_FOOD_KELPSNACK ×3
**Folge:** Gesas Erntekarte im Dorf; Tangix-Bänke als Schutzgebiet markiert

#### SQ_076 · Der Agent

*Fraktion · Goldklang-Kontor · Kette **Hafenbücher** (3/4) · Akt I · Auftrag: Prokuristin Wiebke (Saltrand-Hafen) · Intensität 5 · ~40 min*

Der Konsortium-Agent heißt Bartol und sitzt in der Hafenkneipe. Er will das Kontor nicht betrügen, sondern übernehmen – die doppelten Fässer finanzieren Anteile. Wiebke braucht Beweise, die vor dem Kontorrat halten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Bartol beobachten |
| 2 | Begleiten | Dem Boten zu Bartols Lager folgen |
| 3 | Untersuchen | Das Lager im Kliffsund durchsuchen |
| 4 | Sprechen | Wiebke die Beweise zeigen |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=3 & Quest.SQ_074` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F02 +150 · ITM_CON_SENSE ×2; Anteilsschein (Lore)
**Folge:** Bartol meidet den Hafen (oder wird später in SQ_078 gestellt)

#### SQ_077 · Das Wrack der Möwe

*Rätsel & Ruinen · Akt I · Auftrag: Kuriositätenhändlerin Odalis (Saltrand-Hafen) · Intensität 3 · ~30 min*

Odalis kauft Kurioses aus Wracks. Im Riffgrund liegt die „Möwe“, ein Schiff aus den Siegelkriegen, und darin, sagt sie, eine Kiste mit dorunischen Glasplatten. Die Opalisks im Wrack sehen das anders.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Odalis' Seekarte |
| 2 | Traversal | Zum Wrack tauchen |
| 3 | Beobachten | Die Opalisks im Wrack beobachten |
| 4 | Rätsel | Die Glasplatten-Kiste aus dem Laderaum befreien |

**Voraussetzung:** `–`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_EVO_TIDEPEARL; Klangfragment (TruthLevel 0)
**Folge:** Odalis stellt die Glasplatten aus (Laden-Inventar +1)

#### SQ_078 · Vor dem Kontorrat

*Fraktion · Goldklang-Kontor · Kette **Hafenbücher** (4/4) · Akt I · Auftrag: Prokuristin Wiebke (Saltrand-Hafen) · Intensität 6 · ~55 min*

Der Kontorrat tagt. Bartol hat Freunde im Rat; Wiebke hat Beweise; Marieke hat nur eine Bedingung: „Keine Hexenjagd.“ Der Wärter spricht als Zeuge – in drei Haltungen – und am Ende steht eine Entscheidung über Bartols Anteile.

**Lösungen:** Ausschluss (Gesetz) · Rückzahlung und Bewährung (Gnade) · Anteile in einen Fonds für Werft-Echos umwandeln (dritte Lösung, Marieke lacht).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Marieke vor der Sitzung |
| 2 | Entscheidung | Als Zeuge sprechen |
| 3 | Entscheidung | Vorschlag zu Bartols Anteilen |
| 4 | Beobachten | Den Lager-Brisel als „Zeugen“ vorführen |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=3 & Quest.SQ_076`
**Belohnung:** 800 ◎ · 2.000 Wärter-EP · Ruf F02 +400 · Titel „Kontorzeuge“; ITM_GEAR_TOOL_3
**Folge:** Neue Satzungsklausel (Vorstufe „Klangtreue“, K47); Bartol verliert Anteile oder wird Teilhaber mit Auflage

#### SQ_079 · Thal'assyrs Grotte

*Rätsel & Ruinen · Akt III · Auftrag: Fischhändlerin Beke (Saltrand-Hafen) · Intensität 4 · ~40 min*

In Akt III erzählt Beke – nicht die Arenameisterin, sondern ihre Tante am Fischmarkt – dass die Tiefseegrotte vor dem Hafen „atmet“, seit alle Stimmen erwacht sind (oder schlafen). Sie bittet den Wärter, nachzusehen, ob Thal'assyr Hilfe braucht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Beke am Fischmarkt |
| 2 | Traversal | In die Tiefseegrotte tauchen |
| 3 | Untersuchen | Die Strömungen der Grotte untersuchen |
| 4 | Beobachten | Thal'assyr beobachten |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Thal'assyr (Seite 3); ITM_LURE_TUNINGFORK
**Folge:** Grotte als Pilgerort der Fischer; Tidal-Barks

#### SQ_080 · Glas für das Feuer

*Fraktion · Goldklang-Kontor · Kette **Die gläserne Route** (1/4) · Akt I · Auftrag: Kapitänin Ragna (Saltrand-Hafen) · Intensität 4 · ~40 min*

Saltrands Leuchtfeuer brauchen Linsen aus Sahrun-Glas. Die alte Route über Land ist zu langsam. Kapitänin Ragna will eine Seeroute um die Küste wagen – wenn ein Wärter die Riffe kennt und ein Brisel-Schwarm das Schiff lotst.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ragna an Bord der „Salzbraut“ |
| 2 | Beobachten | Brisel-Schwärme über dem Riff beobachten |
| 3 | Untersuchen | Die gefährlichen Riffpassagen kartieren |
| 4 | Entscheidung | Route festlegen |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=4`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F02 +150 · Seekarte (Lore); ITM_LURE_WINDCHIME
**Folge:** Die „Salzbraut“ läuft aus (Hafen-Data-Layer)

#### SQ_081 · Die Witwe vom Kliff

*Menschen · Akt I · Auftrag: Alke (Kliffsund) (Möwenhuk) · Intensität 3 · ~30 min*

Alkes Mann fuhr vor zwölf Jahren hinaus und kam nicht wieder. Seitdem sitzt ein Ariette auf ihrem Dach und singt jeden Abend. Alke will wissen, ob es sein Echo ist. Der Wärter vergleicht den Gesang mit einem Klangbrief, den ihr Mann hinterließ.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Alke zuhören |
| 2 | Beobachten | Das Ariette in der Dämmerung beobachten |
| 3 | Untersuchen | Den alten Klangbrief abspielen |
| 4 | Entscheidung | Alke antworten |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Hain-Dekor ITM_DECO_CLIFFBELL; Kodex-Beobachtung Ariette (Bindungsgedächtnis)
**Folge:** Alke spricht mit dem Ariette (Bark); im Epilog-Nachhall singt es mit anderen

#### SQ_082 · Sturm vor Sahrun

*Fraktion · Goldklang-Kontor · Kette **Die gläserne Route** (2/4) · Akt I · Auftrag: Kapitänin Ragna (Saltrand-Hafen) · Intensität 5 · ~50 min*

Die erste Fahrt der Salzbraut gerät in einen Sturm vor der Südküste. Ragna will umkehren, die Mannschaft weiter. Der Wärter hält das Schiff mit seinen Echos auf Kurs und findet in der Bucht von Sahrun einen sicheren Hafen – und einen Händler, der schon auf sie wartet.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Sturm auf See |
| 2 | Entscheidung | Umkehren oder weiter |
| 3 | Kampf | Einen aufgebrachten Brision-Leitbullen erschöpfen |
| 4 | Gehen | Die Bucht vor der Harrâd-Oase erreichen |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=4 & Quest.SQ_080` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_GEAR_GLIDER_3; Seefahrer-Abzeichen (Kosmetik)
**Folge:** Seeroute Saltrand–Sahrun (Schnellreise per Schiff zwischen Häfen)

#### SQ_083 · Die Perlen der Aquadrals

*Forschung · Akt I · Auftrag: Meeresforscherin Liv (Riffposten) · Intensität 3 · ~30 min*

Aquadrals leuchten nachts in Mustern, die sich alle drei Nächte wiederholen. Liv glaubt, sie zählen etwas. Der Wärter dokumentiert drei Nächte und findet heraus: Sie zählen Mondphasen – und warnen so vor Springfluten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Liv am Riffposten |
| 2 | Foto | Drei Leuchtmuster fotografieren (drei Nächte) |
| 3 | Beobachten | Aquafins beim Nachahmen beobachten |
| 4 | Sprechen | Liv die Deutung vortragen |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_KS_030; Kodex-Fragment „Mondzähler“
**Folge:** Fischer lesen die Aquadral-Muster als Flutwarnung (Bark)

#### SQ_084 · Salz auf grauem Sand

*Fraktion · Wildwacht · Kette **Die stillen Ränder** (2/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Dünenkate) · Intensität 4 · ~40 min*

Die stillen Ränder in Saltrand: An der Dünenküste bleiben nach der Heilung graue Flecken, auf denen kein Tangi wächst. Jorn vermutet Salz. Der Wärter findet Stillstein-Staub, den die Flut verteilt hat.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Dünenküste |
| 2 | Beobachten | Tangis meiden die Flecken – beobachten |
| 3 | Heilen | Drei graue Flecken heilen |
| 4 | Untersuchen | Den Ursprung des Staubs finden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=4 & Quest.SQ_053`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F03 +150 · ITM_EMAT_STILLSHARD; ITM_CON_CLEANSE ×2
**Folge:** Flecken verschwinden; Tangis wachsen nach

#### SQ_085 · Die Probe der Gezeiten

*Wärterprüfung · Nachhall · Auftrag: Beke Tamsen (Saltrand-Hafen) · Intensität 6 · ~40 min*

Im Nachhall bietet Beke Tamsen eine Gezeitenprobe: drei Kämpfe, deren Arena sich mit jeder Runde hebt und senkt. Die Probe findet nur bei Vollmond statt, wenn die Flut am höchsten steht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Vollmond |
| 2 | Kampf | Erste Flut |
| 3 | Kampf | Zweite Flut |
| 4 | Kampf | Höchste Flut gegen Beke |
| 5 | Beobachten | Der Grotte lauschen |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Moon=Full`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_TIDE; Titel „Gezeitenreiter“
**Folge:** Beke-Barks im Nachhall

#### SQ_086 · Der Leuchtturm schweigt

*Fraktion · Wildwacht · Kette **Die stillen Ränder** (3/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Leuchtfelsen-Wacht) · Intensität 5 · ~45 min*

Der Staub kam vom Leuchtfelsen: Ordensleute hatten dort vor Jahren einen Stillstein vergraben, „damit die Glimkins nicht so laut singen“. Der Stein ist zerbrochen, die Splitter wandern mit der Flut. Jorn und der Wärter bergen sie – vor der nächsten Flut.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Die Splitter am Leuchtfelsen finden |
| 2 | Bedingung | Bei Ebbe am Tag arbeiten |
| 3 | Heilen | Den Fundort heilen |
| 4 | Beobachten | Glimars am geheilten Felsen beobachten |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=4 & Quest.SQ_084` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 700 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_EMAT_STILLSHARD ×2; ITM_GEAR_RESONATOR_3
**Folge:** Leuchtfelsen klar; Glimar-Chor stärker (mit SQ_071)

#### SQ_087 · Die Regatta

*Wärterprüfung · Akt I · Auftrag: Werftmeister Klaas (Saltrand-Hafen) · Intensität 4 · ~30 min*

Einmal im Jahr segeln die Werften gegeneinander – mit Echos als Zugkraft. Klaas fehlt ein Steuermann. Der Wärter tritt an: drei Wettkämpfe gegen die Konkurrenzwerften, in denen Sturm- und Flut-Echos den Ausschlag geben.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Klaas sucht einen Steuermann |
| 2 | Kampf | Gegen die Nordwerft |
| 3 | Kampf | Gegen die Südwerft |
| 4 | Beobachten | Das Aerluna der Siegercrew beobachten |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_HELD_SWIFTFEATHER; Hain-Dekor ITM_DECO_REGATTAFLAG
**Folge:** Regatta als jährliches Weltereignis (WE_REGATTA)

#### SQ_088 · Die Perlenwerkstatt

*Fraktion · Freie Stimmen · Kette **Netze im Nebel** (3/4) · Akt I · Auftrag: Der Schatten (Saltrand-Hafen) · Intensität 5 · ~45 min*

Die Klangperlen der Fangnetze stammen aus einer Werkstatt in Saltrand, die auch für das Kontor Perlen schleift. Die Besitzerin weiß nicht, wofür ihre Perlen verwendet werden – oder will es nicht wissen. Der Wärter muss sie zum Hinsehen bringen.

**Lösungen:** Anke an Wiebke melden (Kontor) · Anke öffentlich bloßstellen · Anke zeigen, was ein Netz anrichtet – Undfin in SQ_063 (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Zelle der Freien Stimmen am Hafen |
| 2 | Untersuchen | Die Werkstatt beobachten |
| 3 | Sprechen | Anke zur Rede stellen |
| 4 | Entscheidung | Anke eine Wahl lassen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=3 & Quest.SQ_065` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 700 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_MAT_NACRE ×3; ITM_TRAP_POOL
**Folge:** Anke liefert keine Netzperlen mehr (oder heimlich weiter – Bark)

#### SQ_089 · Netze verbrennen

*Fraktion · Freie Stimmen · Kette **Netze im Nebel** (4/4) · Akt I · Auftrag: Der Schatten (Saltrand-Hafen) · Intensität 6 · ~55 min*

Die Netzknüpfer lagern ihre Ware in einem Kliffversteck. Die Freien Stimmen wollen es anzünden. Der Wärter weiß: Im Versteck sind auch gefangene Echos. Bei Nacht und Nebel führt er den Einsatz – ohne Feuer, mit Befreiung.

**Lösungen:** Verbrennen (Tavesh-Bark) · versenken · zu Fischernetzen umknüpfen (dritte Lösung, Harm hilft).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Nebel im Kliffsund |
| 2 | Gehen | Zum Versteck |
| 3 | Heilen | Drei verstummte Gefangene befreien und heilen |
| 4 | Kampf | Die Echos des Netzknüpfers erschöpfen |
| 5 | Entscheidung | Die Netze: verbrennen, versenken, umknüpfen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=3 & Quest.SQ_088` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 800 ◎ · 2.000 Wärter-EP · Ruf F04 +400 · Titel „Netzlöser“; ITM_GEAR_LANTERN_3
**Folge:** Keine Fangnetze mehr in R03/R06 (Population erholt sich); Netzknüpfer Harm flieht oder wird Fischer

#### SQ_090 · Weißes Gold

*Fraktion · Freie Stimmen · Kette **Salz und Freiheit** (1/4) · Akt I · Auftrag: Ennis Rook (Kurierin) (Tangwerft) · Intensität 4 · ~40 min*

Ennis ist zurück, diesmal mit einer Spur: In den Salzgärten hinter Tangwerft arbeiten Stonshells unter Vertrag – einem Vertrag, den sie nie unterschreiben konnten. Die Salzsieder sagen, es sei „Tradition“. Ennis nennt es Schuldknechtschaft. Der Wärter sieht sich beides an.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ennis in Tangwerft |
| 2 | Beobachten | Stonshells in den Salzgärten beobachten |
| 3 | Sprechen | Salzsieder Ole zuhören |
| 4 | Untersuchen | Die Verträge im Siedehaus lesen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=4`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F04 +150 · ITM_MAT_SALTWORT ×5; Vertragsabschrift (Lore)
**Folge:** Kette führt nach Sahrun (SQ_109)


---

## 4. Sahrun-Weite (R04) – SQ_091–SQ_112

Die Weite ist die Region der Gelehrten und Händler. Hier liegt die Glasebene mit dem Erbe einer Hochkultur, die „die Sonne zu laut besang“ – ein Echo von Maedryns Krone, das der Spieler nach W6 versteht. Die Kette *Salz und Freiheit* beginnt in Saltrand und endet mit einem Fest in der Oase.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_091 | Scherben im Sand | Fraktion | F01 · FQ_F01_03 | Akt II | 3 | 35 | Time=Night |
| SQ_092 | Die Dunhorn-Mutter | Echo-Geschichte | – | Akt II | 3 | 30 | Weather=Sandstorm |
| SQ_093 | Das Lied der Glasstadt | Fraktion | F01 · FQ_F01_03 | Akt II | 4 | 40 | – |
| SQ_094 | Skarits im Wind | Echo-Geschichte | – | Akt II | 2 | 25 | – |
| SQ_095 | Wer die Sonne zu laut sang | Fraktion | F01 · FQ_F01_03 | Akt II | 5 | 45 | – |
| SQ_096 | Die Nacht der Spiegel | Weltereignis | – | Akt III | 4 | 35 | Moon=Full |
| SQ_097 | Der Reif bleibt im Sand | Fraktion | F01 · FQ_F01_03 | Akt II | 6 | 55 | – |
| SQ_098 | Sandsturm-Lotsen | Weltereignis | – | Akt II | 4 | 35 | Weather=Sandstorm |
| SQ_099 | Geschwärzte Zeilen | Fraktion | F01 · FQ_F01_04 | Akt II | 5 | 45 | – |
| SQ_100 | Das vergrabene Observatorium | Rätsel & Ruinen | – | Akt II | 4 | 40 | Time=Night |
| SQ_101 | Glas ab Harrâd | Fraktion | F02 · FQ_F02_04 | Akt II | 4 | 40 | – |
| SQ_102 | Die alte Brunnenköchin | Menschen | – | Nachhall | 2 | 25 | – |
| SQ_103 | Die gläserne Route | Fraktion | F02 · FQ_F02_04 | Akt II | 5 | 55 | Weather=Heatwave |
| SQ_104 | Die Uhr der Stachiks | Forschung | – | Akt II | 3 | 30 | Time=Night |
| SQ_105 | Die Karawanserei-Wette | Fraktion | F02 | Akt II | 3 | 30 | Time=Day |
| SQ_106 | Die Probe des Mittags | Wärterprüfung | – | Akt III | 5 | 35 | Weather=Heatwave |
| SQ_107 | Die stillen Ränder der Weite | Fraktion | F03 · FQ_F03_04 | Akt II | 6 | 55 | Time=Night |
| SQ_108 | Das Duell der Karawanen | Wärterprüfung | – | Akt II | 4 | 30 | – |
| SQ_109 | Salz in der Oase | Fraktion | F04 · FQ_F04_04 | Akt II | 4 | 40 | Weather=Heatwave |
| SQ_110 | Der Vertrag, den niemand unterschrieb | Fraktion | F04 · FQ_F04_04 | Akt II | 5 | 45 | – |
| SQ_111 | Salz und Freiheit | Fraktion | F04 · FQ_F04_04 | Akt II | 6 | 60 | – |
| SQ_112 | Die Zelle in Mirsaan | Fraktion | F04 | Akt II | 4 | 35 | Weather=Sandstorm |

#### SQ_091 · Scherben im Sand

*Fraktion · Akademie der Resonanz · Kette **Glas der Hochkultur** (1/4) · Akt II · Auftrag: Grabungsleiterin Saphira Lund (Glasebene-Turm) · Intensität 3 · ~35 min*

Die Akademie gräbt auf der Glasebene. Saphira Lund leitet die Grabung, freundlich und gründlich. Sie braucht jemanden, der Glasscherben nach Klang sortiert – die Hochkultur schrieb in Tönen, nicht in Zeichen. Vor W6 arbeitet Venns Team mit; danach Shirahs Leute.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Lund am Grabungszelt |
| 2 | Untersuchen | Drei Scherbenfelder abhören |
| 3 | Rätsel | Scherben nach Tonhöhe ordnen |
| 4 | Beobachten | Vitrels, die nachts auf den Scherben leuchten |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=3` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_MAT_SUNGLASS ×3; Kodex-Fragment „Glaslied I“
**Folge:** Grabungsfeld erweitert (Data Layer)

#### SQ_092 · Die Dunhorn-Mutter

*Echo-Geschichte · Akt II · Auftrag: Hirtin Najla (Ashurim) (Wanderdorf Ashurim) · Intensität 3 · ~30 min*

Eine Dunhorn-Mutter hat ihr Kalb in der Tiefen Weite verloren. Sie weigert sich, mit der Herde weiterzuziehen, und das Wanderdorf kann nicht ohne sie aufbrechen. Najla bittet den Wärter, das Kalb zu finden, bevor der Sandsturm kommt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Najla bei der Herde |
| 2 | Beobachten | Die Dunhorn-Mutter beobachten (Rufmuster) |
| 3 | Untersuchen | Spuren des Kalbs in der Tiefen Weite |
| 4 | Begleiten | Mit dem Kalb zur Herde |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Sandstorm`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_FOOD_DATES ×5; Kodex-Beobachtung Dunkalb
**Folge:** Das Wanderdorf zieht weiter (neuer Lagerplatz); Najla-Barks

#### SQ_093 · Das Lied der Glasstadt

*Fraktion · Akademie der Resonanz · Kette **Glas der Hochkultur** (2/4) · Akt II · Auftrag: Grabungsleiterin Saphira Lund (Glasebene-Turm) · Intensität 4 · ~40 min*

Die sortierten Scherben ergeben ein Lied – die Hymne einer Stadt, die „die Sonne zu laut besang“. Lund will es aufführen. Der Wärter sammelt in Mirsaan und Harrâd Liedreste, die als Kinderreime überlebt haben.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Nach Mirsaan |
| 2 | Sprechen | Kinderreime bei Lehrerin Dalia |
| 3 | Untersuchen | Reimreste in der Oase |
| 4 | Rätsel | Hymne aus Scherben und Reimen setzen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=3 & Quest.SQ_091`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_KS_043; Kodex-Fragment „Glaslied II“
**Folge:** Die Kinder von Mirsaan singen die Hymne (Ambient)

#### SQ_094 · Skarits im Wind

*Echo-Geschichte · Akt II · Auftrag: Sterndeuter Harun (Qasr Sahrun) · Intensität 2 · ~25 min*

Harun beobachtet Skarits, die bei Wind seltsame Kreise ziehen. Er glaubt, sie lesen die Schwerkraft der Dünen. Der Wärter vermisst die Kreise und findet einen hohlen Dünenkern, in dem Skarabons nisten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Harun im Sternturm |
| 2 | Beobachten | Skarit-Kreise beobachten |
| 3 | Traversal | In den Dünenkern graben |
| 4 | Foto | Ein Skarabon im Nest fotografieren |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · ITM_EVO_GRAVITY; Kodex-Beobachtung Skarabon
**Folge:** Harun veröffentlicht „Dünenkerne“ (Bark)

#### SQ_095 · Wer die Sonne zu laut sang

*Fraktion · Akademie der Resonanz · Kette **Glas der Hochkultur** (3/4) · Akt II · Auftrag: Grabungsleiterin Saphira Lund (Glasebene-Turm) · Intensität 5 · ~45 min*

Das Lied der Glasstadt erzählt von einem Herrscher, der die Sonne zwang, länger zu scheinen – mit einem Kronenreif aus Glas. Lund erkennt Parallelen zu den Kronensplitter-Gerüchten. Nach W6 versteht der Wärter, was sie gefunden hat: ein Vorbild Maedryns.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Den Herrschersaal unter der Glasebene freilegen |
| 2 | Traversal | Durch den Sand in den Saal |
| 3 | Beobachten | Das Mirazhar im Saal beobachten |
| 4 | Entscheidung | Lund sagen, was der Saal bedeutet |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=3 & Quest.SQ_093 & Quest.MQ_A2_07`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Der Glasreif“ (TruthLevel 6); ITM_LURE_MIRROR
**Folge:** Der Saal wird zum Rückkehrort; Lunds Bericht in K50/K51-Akten

#### SQ_096 · Die Nacht der Spiegel

*Weltereignis · Akt III · Auftrag: Shirah Harrad (Qasr Sahrun) · Intensität 4 · ~35 min*

In Akt III, wenn Ash'kareth wach ist (oder schläft), richtet Qasr Sahrun die Nacht der Spiegel aus: Alle Spiegel der Stadt werden auf den Mond gerichtet. Wer hineinsieht, sieht eine Wahrheit über sich. Shirah bittet den Wärter, die Spiegel zu stellen – und selbst hineinzusehen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Vollmond |
| 2 | Rätsel | Die Spiegel der Stadt ausrichten |
| 3 | Beobachten | Ash'kareths Licht im Hauptspiegel beobachten |
| 4 | Entscheidung | In den Spiegel sehen |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Moon=Full`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · ITM_LURE_MIRROR; Hain-Dekor ITM_DECO_SUNMIRROR
**Folge:** Nacht der Spiegel als Weltereignis (Vollmond, R04)

#### SQ_097 · Der Reif bleibt im Sand

*Fraktion · Akademie der Resonanz · Kette **Glas der Hochkultur** (4/4) · Akt II · Auftrag: Grabungsleiterin Saphira Lund (Glasebene-Turm) · Intensität 6 · ~55 min*

Im Saal liegt ein Reif aus Glas – kein Kronensplitter, aber nach demselben Prinzip gebaut. Venn-treue Grabungswachen halten den Saal noch besetzt und wollen den Reif nach Nimbara schaffen; Aevrins Akademie will ihn studieren, Shirah ihn zerstören. Lund überlässt die Entscheidung dem Wärter.

**Lösungen:** Zerstören (Shirah) · der Akademie unter Aevrin geben · im Saal versiegeln und den Ort schützen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zurück in den Herrschersaal |
| 2 | Kampf | Die Echos der Venn-treuen Grabungswache erschöpfen |
| 3 | Untersuchen | Den Reif mit dem Resonator abhören |
| 4 | Entscheidung | Reif zerstören, studieren oder begraben |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=3 & Quest.SQ_095 & Quest.MQ_A2_07`
**Belohnung:** 1.450 ◎ · 2.000 Wärter-EP · Ruf F01 +400 · Titel „Glaslauscher“; ITM_HELD_MIRRORSCALE
**Folge:** Reif in der Akademie (Ausstellung, Nachhall) · zerstört · wieder versiegelt (dritte Lösung)

#### SQ_098 · Sandsturm-Lotsen

*Weltereignis · Akt II · Auftrag: Amara (Karawanserei) (Qasr Sahrun) · Intensität 4 · ~35 min*

Bei Sandsturm stehen die Karawanen still – außer man folgt den Sirrkorns, die im Sturm Bahnen fliegen. Amara will eine Karawane mit Arzneien nach Harrâd bringen, die nicht warten kann. Der Wärter navigiert per Resonanzsinn.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Sandsturm |
| 2 | Beobachten | Sirrkorn-Bahnen im Sturm beobachten |
| 3 | Begleiten | Die Karawane nach Harrâd führen |
| 4 | Liefern | Arzneien übergeben |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Sandstorm`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_GEAR_CLOAK_3; ITM_FOOD_DATES ×3
**Folge:** Amaras Karawanen nutzen die Sirrkorn-Bahnen (Bark)

#### SQ_099 · Geschwärzte Zeilen

*Fraktion · Akademie der Resonanz · Kette **Aevrins Akten** (1/4) · Akt II · Auftrag: Aevrin Thal (Qasr Sahrun) · Intensität 5 · ~45 min*

Nach dem Verrat öffnet Aevrin Venns Akten. Eine Spur führt zur Grabung am Sonnenhof: geschwärzte Zeilen über „Fundstücke für das Rektorat“. Aevrin schickt den Wärter, die Originalnotizen der Grabungshelfer zu finden, bevor sie verbrannt werden.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Aevrins Klangbrief |
| 2 | Gehen | Zur verlassenen Grabung am Sonnenhof |
| 3 | Untersuchen | Notizen der Grabungshelfer finden |
| 4 | Sprechen | Den Helfer Tamir befragen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=4 & Quest.MQ_A2_07`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Fundliste Sonnenhof“ (TruthLevel 6); ITM_CON_SENSE ×2
**Folge:** Aevrins Akte wächst (K51: SQ_132, SQ_152)

#### SQ_100 · Das vergrabene Observatorium

*Rätsel & Ruinen · Akt II · Auftrag: Sterndeuter Harun (Qasr Sahrun) · Intensität 4 · ~40 min*

Harun hat eine Sternkarte der Hochkultur gefunden. Sie zeigt ein Observatorium unter dem Sonnenhof-Plateau, dessen Linsen „die Sonne stimmten“. Der Wärter gräbt sich hinein und richtet die Linsen neu aus – auf die Sterne statt auf die Sonne.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Haruns Sternkarte |
| 2 | Traversal | Zum vergrabenen Observatorium |
| 3 | Rätsel | Die Linsen ausrichten |
| 4 | Beobachten | Vitraphas im Sternenlicht beobachten |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · ITM_LURE_STARCHIME; Klangfragment (TruthLevel 4)
**Folge:** Observatorium als Aussichtspunkt (Wärter-EP Entdeckung)

#### SQ_101 · Glas ab Harrâd

*Fraktion · Goldklang-Kontor · Kette **Die gläserne Route** (3/4) · Akt II · Auftrag: Kapitänin Ragna (Harrâd) · Intensität 4 · ~40 min*

Die Salzbraut liegt in der Bucht vor Harrâd. Ragna verhandelt mit der Glasbläserei Tavi um Linsenglas, doch Tavi liefert nur, wenn Saltrand im Gegenzug Salz für die Oase schickt – Salz, das die Oase gegen Hitze braucht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ragna in der Bucht |
| 2 | Sprechen | Tavi in der Glasbläserei |
| 3 | Beobachten | Sengels beim Glasschmelzen helfen sehen |
| 4 | Entscheidung | Tauschverhältnis Glas gegen Salz |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05 & Rank.F02>=4 & Quest.SQ_082`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_MAT_SUNGLASS ×3; Rezept RCP_062
**Folge:** Glas-Salz-Handel (Händler-Sortimente in R04/R06 +2)

#### SQ_102 · Die alte Brunnenköchin

*Menschen · Nachhall · Auftrag: Brunnenköchin Saya (Qasr Sahrun) · Intensität 2 · ~25 min*

Saya kocht seit fünfzig Jahren an der Brunnenküche. Im Nachhall will sie ihr Rezeptbuch an jemanden weitergeben, der „zuhört, wenn das Wasser kocht“. Der Wärter kocht mit ihr drei Gerichte – jedes mit einem Echo als Küchenhilfe.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Saya an der Brunnenküche |
| 2 | Sammeln | Oasenminze sammeln |
| 3 | Beobachten | Ein Solkit beim Feuermachen beobachten |
| 4 | Entscheidung | Das Rezeptbuch annehmen |

**Voraussetzung:** `Act>=Nachhall`
**Belohnung:** 1.450 ◎ · 2.000 Wärter-EP · Rezept RCP_064; ITM_FOODC_STEW ×3
**Folge:** Sayas Gerichte im Gasthaus; Bark über „den Wärter, der kochen kann“

#### SQ_103 · Die gläserne Route

*Fraktion · Goldklang-Kontor · Kette **Die gläserne Route** (4/4) · Akt II · Auftrag: Kapitänin Ragna (Harrâd) · Intensität 5 · ~55 min*

Die erste volle Ladung Linsenglas soll über Land nach Saltrand – auf einer neuen Route durch die Weite, die Sengrath-Herden als Wegweiser nutzt. Die Reise dauert drei Spieltage; unterwegs: Hitzewellen, eine Furt, ein Händlerzug, der die Route für sich will.

**Lösungen:** Route teilen · Zoll erheben · gemeinsamen Karawanenverband gründen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Aufbruch in der Hitze |
| 2 | Beobachten | Einer Sengrath-Herde folgen |
| 3 | Begleiten | Den Glaszug durch die Mirsaan-Dünen führen |
| 4 | Entscheidung | Mit dem konkurrierenden Händlerzug verhandeln |
| 5 | Liefern | Linsenglas in Saltrand abliefern |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05 & Rank.F02>=4 & Quest.SQ_101` · **Variante/Bedingung:** `Weather=Heatwave`
**Belohnung:** 1.450 ◎ · 2.000 Wärter-EP · Ruf F02 +400 · Titel „Routenfinder“; ITM_GEAR_BAG_4
**Folge:** Gläserne Route als Handelsweg; Leuchtfeuer Saltrand mit Sahrun-Linsen

#### SQ_104 · Die Uhr der Stachiks

*Forschung · Akt II · Auftrag: Forscher Idris (Plateau-Lager) · Intensität 3 · ~30 min*

Stachiks kommen nachts aus dem Sand – aber nicht zu jeder Nacht. Idris vermutet einen Takt. Der Wärter beobachtet sie über drei Nächte und findet: Sie folgen nicht dem Mond, sondern der Temperatur des Sandes um Mitternacht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Idris' Hypothese |
| 2 | Beobachten | Stachiks drei Nächte beobachten |
| 3 | Untersuchen | Sandtemperaturen messen |
| 4 | Sprechen | Ergebnis vortragen |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_KS_046; Kodex-Fragment „Sanduhr“
**Folge:** Kodex Stachik: Aktivität mit Temperaturregel

#### SQ_105 · Die Karawanserei-Wette

*Fraktion · Goldklang-Kontor · Akt II · Auftrag: Amara (Karawanserei) (Qasr Sahrun) · Intensität 3 · ~30 min*

Amara hat mit einem Kontor-Händler gewettet, dass ein Solvar schneller durch die Weite läuft als jedes Lastechos des Kontors. Der Einsatz: freie Lagerplätze für ein Jahr. Der Wärter soll das Solvar vorbereiten – und auf faires Spiel achten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Wette |
| 2 | Beobachten | Das Solvar im Training beobachten |
| 3 | Untersuchen | Herausfinden, ob der Kontor-Händler betrügt |
| 4 | Entscheidung | Das Rennen eröffnen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F02 +150 · ITM_HELD_SWIFTFEATHER; ITM_FOOD_DATES ×3
**Folge:** Rennen als monatliches Ereignis; Kontor- und Karawanserei-Barks

#### SQ_106 · Die Probe des Mittags

*Wärterprüfung · Akt III · Auftrag: Shirah Harrad (Qasr Sahrun) · Intensität 5 · ~35 min*

In Akt III fordert Shirah den Wärter zur Mittagsprobe: drei Kämpfe bei Hitzewelle, bei denen Sonnenspiegel jede zweite Runde blenden. Wer bestehen will, muss Licht lesen – oder sich davor schützen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Hitzewelle |
| 2 | Kampf | Erste Mittagsprobe |
| 3 | Kampf | Zweite Mittagsprobe |
| 4 | Kampf | Shirah selbst |
| 5 | Beobachten | Unter der Arena lauschen (Ash'kareth) |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Weather=Heatwave`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_LIGHT; ITM_KS_047
**Folge:** Shirah-Barks; Mittagstraining

#### SQ_107 · Die stillen Ränder der Weite

*Fraktion · Wildwacht · Kette **Die stillen Ränder** (4/4) · Akt II · Auftrag: Passwart Jorn (Wildwacht) (Dünenwacht) · Intensität 6 · ~55 min*

Die letzte Station der stillen Ränder: In der Tiefen Weite ist eine alte Stillezone geheilt, aber ein Ring aus grauem Glas bleibt. Darin leben Mahrsils, die nur dort sicher sind, weil kein anderes Echo hineingeht. Heilen heißt: ihr Refugium zerstören.

**Lösungen:** Ganz heilen (Mahrsils ziehen weg) · lassen (Ring bleibt grau) · nur den Rand heilen und einen Schutzring markieren (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum Glasring in der Tiefen Weite |
| 2 | Beobachten | Mahrsils im Ring beobachten |
| 3 | Untersuchen | Den Ring vermessen |
| 4 | Entscheidung | Heilen, lassen oder umsiedeln |
| 5 | Heilen | (je nach Wahl) den Rand oder den ganzen Ring heilen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03 & Rank.F03>=4 & Quest.SQ_086` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.450 ◎ · 2.000 Wärter-EP · Ruf F03 +400 · Titel „Randgänger“; Hain-Dekor ITM_DECO_GLASSRING
**Folge:** Mahrsil-Refugium bleibt (Teilheilung) oder Ring verschwindet; Jorns Abschiedsbrief

#### SQ_108 · Das Duell der Karawanen

*Wärterprüfung · Akt II · Auftrag: Amara (Karawanserei) (Qasr Sahrun) · Intensität 4 · ~30 min*

Zwei Karawanen streiten um denselben Rastplatz an der Harrâd-Oase. Die Tradition der Weite: ein Wärterkampf, ausgetragen von einem Unbeteiligten für jede Seite. Der Wärter kämpft – für wen, entscheidet er selbst.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Amara erklärt den Brauch |
| 2 | Entscheidung | Eine Seite wählen |
| 3 | Kampf | Kampf gegen den Vertreter der anderen Seite |
| 4 | Beobachten | Das Solaryx des Siegers beobachten |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_HELD_TONE_EMBER; ITM_FOOD_DATES ×3
**Folge:** Rastplatz-Ordnung an der Oase (Ambient)

#### SQ_109 · Salz in der Oase

*Fraktion · Freie Stimmen · Kette **Salz und Freiheit** (2/4) · Akt II · Auftrag: Ennis Rook (Kurierin) (Harrâd) · Intensität 4 · ~40 min*

Die Salzsieder aus Tangwerft haben Verwandte in Harrâd – und auch hier arbeiten Stonshell-Verwandte, Mesakils, in den Salzpfannen, unter denselben Verträgen. Ennis will beide Seiten gleichzeitig angehen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ennis in Harrâd |
| 2 | Beobachten | Mesakils in den Salzpfannen beobachten |
| 3 | Untersuchen | Die Verträge der Oase vergleichen |
| 4 | Sprechen | Salzmeisterin Farah zuhören |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04 & Rank.F04>=4 & Quest.SQ_090` · **Variante/Bedingung:** `Weather=Heatwave`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_MAT_SALTCOPPER ×3; Vertragsabschrift II (Lore)
**Folge:** Kette geht weiter (SQ_110)

#### SQ_110 · Der Vertrag, den niemand unterschrieb

*Fraktion · Freie Stimmen · Kette **Salz und Freiheit** (3/4) · Akt II · Auftrag: Ennis Rook (Kurierin) (Harrâd) · Intensität 5 · ~45 min*

Beide Verträge gehen auf einen Mustervertrag zurück, den ein Kontor-Notar vor vierzig Jahren aufsetzte – mit einer Klausel, die Echos „als Inventar des Salzgartens“ führt. Der Notar lebt noch, in Mirsaan. Ennis will ihn bloßstellen; der Wärter will ihn verstehen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Nach Mirsaan |
| 2 | Sprechen | Den alten Notar Basim befragen |
| 3 | Untersuchen | Basims Archiv durchsehen |
| 4 | Entscheidung | Basim um einen Widerruf bitten |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04 & Rank.F04>=4 & Quest.SQ_109`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_CON_SENSE; Widerrufsurkunde (Lore)
**Folge:** Basim widerruft öffentlich oder schweigt (beeinflusst SQ_111)

#### SQ_111 · Salz und Freiheit

*Fraktion · Freie Stimmen · Kette **Salz und Freiheit** (4/4) · Akt II · Auftrag: Ennis Rook (Kurierin) (Harrâd) · Intensität 6 · ~60 min*

Mit oder ohne Widerruf: Die Salzgärten in Harrâd und Tangwerft sollen an einem Tag die Echos freigeben. Ennis organisiert, Wiebke (Kontor) prüft die Verträge, die Salzsieder fürchten den Ruin. Der Wärter steht dazwischen und hält am Ende eine Rede in der Oase.

**Lösungen:** Sofortige Freigabe (Freie Stimmen) · stufenweise mit Kontor-Krediten · Genossenschaft aus Siedern und Echos mit Rückkehrrecht (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Farah zögert |
| 2 | Entscheidung | Rede in der Oase |
| 3 | Heilen | Zwei verstummte Mesakils in den Pfannen heilen |
| 4 | Beobachten | Den ersten freien Mesakor beobachten |
| 5 | Lager | Das Salzfest feiern |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04 & Rank.F04>=4 & Quest.SQ_110`
**Belohnung:** 1.550 ◎ · 2.000 Wärter-EP · Ruf F04 +400 · Titel „Salzbrecher“; Hain-Dekor ITM_DECO_SALTCRYSTAL
**Folge:** Salzgärten arbeiten mit freiwilligen Echos gegen Lohn; Salzfest als Weltereignis (R04/R06)

#### SQ_112 · Die Zelle in Mirsaan

*Fraktion · Freie Stimmen · Akt II · Auftrag: Zelle Mirsaan (Freie Stimmen) (Mirsaan) · Intensität 4 · ~35 min*

Die Freie-Stimmen-Zelle in Mirsaan versteckt ein Dutzend Echos, die aus Arbeitslagern geflohen sind. Ein Sandsturm hat ihr Versteck freigelegt. Der Wärter hilft, ein neues zu finden – mit Grabreiten unter die Dünen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Zelle in Not |
| 2 | Traversal | Einen Gang unter die Dünen graben |
| 3 | Untersuchen | Eine tragfähige Höhle finden |
| 4 | Begleiten | Die Echos ins neue Versteck führen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04` · **Variante/Bedingung:** `Weather=Sandstorm`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_CON_REPEL ×3; Zellen-Schnellreisepunkt Mirsaan
**Folge:** Neues Versteck (verborgener Ort, Rückkehr)


---

## 5. Ignareth (R05) – SQ_113–SQ_131

Ignareth trägt Schuld: Hier stand das Lager (MQ_A2_03). Die Nebenquests erzählen, was danach kommt – leere Hallen, ein offenes Haus der Freien Stimmen in Kaldra, eine Zunft, die ihr Gelübde gegen neue Versuchungen verteidigt. Die Ausbrüche des Ignar (alle drei Spieltage) und der Ascheregen bestimmen den Rhythmus.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_113 | Die Erzwaage | Fraktion | F02 | Akt II | 3 | 30 | – |
| SQ_114 | Das Pyrolm-Nest | Echo-Geschichte | – | Akt II | 2 | 25 | – |
| SQ_115 | Nach dem Lager | Fraktion | F02 | Akt III | 4 | 35 | Time=Night |
| SQ_116 | Glockenguss | Echo-Geschichte | – | Akt II | 3 | 30 | – |
| SQ_117 | Das Konsortium | Fraktion | F02 | Akt II | 5 | 45 | – |
| SQ_118 | Die Aschenacht | Weltereignis | – | Nachhall | 4 | 35 | Weather=Ashfall |
| SQ_119 | Die Zunft und das Kontor | Fraktion | F02 | Akt II | 4 | 35 | – |
| SQ_120 | Ausbruch | Weltereignis | – | Akt II | 5 | 35 | Weather=Heatwave |
| SQ_121 | Die Kisten von gestern | Fraktion | F02 | Akt III | 4 | 40 | – |
| SQ_122 | Das Kraterherz träumt | Rätsel & Ruinen | – | Akt II | 4 | 40 | – |
| SQ_123 | Rauchzeichen | Fraktion | F03 | Akt II | 3 | 30 | Weather=Ashfall |
| SQ_124 | Thermen für alle | Menschen | – | Nachhall | 2 | 25 | – |
| SQ_125 | Die Obsidianklamm-Brücke | Fraktion | F03 | Akt II | 4 | 35 | Time=Day |
| SQ_126 | Drusen, die summen | Forschung | – | Akt II | 3 | 30 | Weather=Thunderstorm |
| SQ_127 | Was die Freien bauen | Fraktion | F04 | Akt III | 4 | 40 | – |
| SQ_128 | Die Esse-Probe | Wärterprüfung | – | Akt II | 5 | 35 | – |
| SQ_129 | Die Glut im Keller | Fraktion | F04 | Akt II | 4 | 35 | Time=Night |
| SQ_130 | Ein Lied für Kaldra | Fraktion | F04 | Nachhall | 3 | 30 | – |
| SQ_131 | Der Volket-Zaun | Fraktion | F04 | Akt II | 4 | 35 | Weather=Thunderstorm |

#### SQ_113 · Die Erzwaage

*Fraktion · Goldklang-Kontor · Akt II · Auftrag: Erzwaage Volk (Schlackenwehr) · Intensität 3 · ~30 min*

Volk betreibt die Erzwaage des Kontors in Schlackenwehr. Seit Wochen fehlen kleine Mengen Slagsteel. Er verdächtigt die Arbeiter. Der Wärter findet Amboltspuren – die jungen Ambolts fressen Metallspäne und wachsen daran.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Volk an der Waage |
| 2 | Untersuchen | Spuren im Lager |
| 3 | Beobachten | Ambolts beim Fressen beobachten |
| 4 | Entscheidung | Volk einen Futterplatz vorschlagen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F02 +150 · ITM_MAT_SLAGSTEEL ×2; Kodex-Beobachtung Ambolt
**Folge:** Futterplatz für Ambolts; Arbeiter entlastet (Bark)

#### SQ_114 · Das Pyrolm-Nest

*Echo-Geschichte · Akt II · Auftrag: Schmiedin Isolde (Vorthax) · Intensität 2 · ~25 min*

Isolde findet jeden Morgen ein Pyrolm in ihrer Esse. Sie mag es, aber es frisst ihre Kohle. Der Wärter findet heraus, dass das Pyrolm sein Nest im Schlackenstrom verloren hat.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Isolde und der Gast |
| 2 | Beobachten | Das Pyrolm beobachten |
| 3 | Untersuchen | Das alte Nest im Schlackenstrom suchen |
| 4 | Entscheidung | Neues Nest bauen oder Pyrolm behalten |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · ITM_FOOD_CHARCOAL ×5; ITM_EVO_EMBER
**Folge:** Pyrolm-Nest in Isoldes Hof oder am Strom

#### SQ_115 · Nach dem Lager

*Fraktion · Goldklang-Kontor · Akt III · Auftrag: Wehrmarkt-Händler Ithren (Schlackenwehr) · Intensität 4 · ~35 min*

In Akt III, nach der Lagerbefreiung, stehen die Kontor-Hallen am Kraterrand leer. Ithren will sie als Markt nutzen; die Zunft will sie abreißen; die befreiten Echos kehren nachts zurück, weil sie dort Wärme finden.

**Lösungen:** Markt (Kontor) · Abriss (Zunft) · Wärmehaus für Echos mit Markt am Tag (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum ehemaligen Lager |
| 2 | Beobachten | Aschunds in den Hallen nachts beobachten |
| 3 | Sprechen | Ithrens Plan |
| 4 | Entscheidung | Was aus den Hallen wird |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_05 & Quest.MQ_A2_03` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_GEAR_TOOL_3; Lore „Lagerakte“
**Folge:** Hallen werden Markt, Wärmehaus für Echos oder abgerissen

#### SQ_116 · Glockenguss

*Echo-Geschichte · Akt II · Auftrag: Glockengießer Bram (Schlackenwehr) · Intensität 3 · ~30 min*

Jeder 12. Spieltag ist Glockenguss in Schlackenwehr. Diesmal springt die Form. Bram braucht ein Bassalt, das den Ton der neuen Glocke „vorsingt“, damit die Form im Klang gegossen werden kann.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Bram und die gesprungene Form |
| 2 | Beobachten | Ein Bassalt in der Obsidianklamm beobachten |
| 3 | Rätsel | Form und Ton abstimmen |
| 4 | Szene | Der Guss |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_LURE_BELLCHIME; Hain-Dekor ITM_DECO_FORGEBELL
**Folge:** Neue Glocke läutet (eine der sechs Schmiedeglocken)

#### SQ_117 · Das Konsortium

*Fraktion · Goldklang-Kontor · Akt II · Auftrag: Marieke Holm (Schlackenwehr) · Intensität 5 · ~45 min*

Marieke will wissen, wer hinter dem Lager-Konsortium steckt. Die Spur führt zu drei Kontor-Teilhabern – einer davon ist Bartol aus Saltrand. Der Wärter sammelt Beweise in Vorthax, Kaldra und an der Obsidianwacht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Marieke im Kontor |
| 2 | Untersuchen | Lieferbücher in Vorthax |
| 3 | Untersuchen | Lagerlisten in Kaldra |
| 4 | Untersuchen | Frachtbriefe an der Obsidianwacht |
| 5 | Entscheidung | Marieke die Namen nennen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05 & Quest.MQ_A2_03`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_GEAR_BAG_3; Konsortiumsakte (Lore)
**Folge:** Konsortium verliert Kontorrechte (Kontor-Barks)

#### SQ_118 · Die Aschenacht

*Weltereignis · Nachhall · Auftrag: Thermenwirtin Seraphe (Schlackenwehr) · Intensität 4 · ~35 min*

Im Nachhall fällt bei Ascheregen ein feines Leuchten über Ignareth: Aschgrims tanzen in den Flocken. Seraphe will das Schauspiel ihren Gästen zeigen, aber die Aschgrims verschwinden, sobald jemand näherkommt. Der Wärter findet einen Weg, zuzusehen, ohne zu stören.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Ascheregen |
| 2 | Beobachten | Aschgrims beim Tanz beobachten |
| 3 | Untersuchen | Einen verdeckten Aussichtsplatz finden |
| 4 | Begleiten | Seraphes Gäste leise hinführen |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Weather=Ashfall`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_ASHLANTERN; ITM_CON_WARM ×3
**Folge:** Aschenacht-Führungen (Weltereignis bei Ascheregen)

#### SQ_119 · Die Zunft und das Kontor

*Fraktion · Goldklang-Kontor · Akt II · Auftrag: Zunftsprecherin Helka (Schlackenwehr) · Intensität 4 · ~35 min*

Die Schmiedezunft hat ein Gelübde gegen Waffen (seit den Siegelkriegen). Ein Kontor-Auftrag verlangt „Werkzeuge“, die verdächtig nach Stillstein-Fassungen aussehen. Helka bittet den Wärter, die Pläne zu prüfen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Helka in der Zunfthalle |
| 2 | Untersuchen | Die Auftragspläne prüfen |
| 3 | Beobachten | Ein Ambross beim Schmieden der Probe beobachten |
| 4 | Entscheidung | Helka raten |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_05`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_HELD_TONE_METAL; Rezept RCP_066
**Folge:** Zunft lehnt ab oder liefert harmlose Werkzeuge (Bark)

#### SQ_120 · Ausbruch

*Weltereignis · Akt II · Auftrag: Kraterwart Osk (Kraterrand-Posten) · Intensität 5 · ~35 min*

Alle drei Spieltage bricht der Ignar aus. Der Kraterrand-Posten kündigt es einen Tag vorher an. Diesmal ist ein Pyroluth-Gelege genau im Weg der Lava. Osk und der Wärter haben bis zum Ausbruch Zeit – Spielzeit, keine Echtzeit.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Osks Warnung |
| 2 | Beobachten | Das Pyroluth-Elternpaar beobachten |
| 3 | Untersuchen | Einen sicheren Nistplatz finden |
| 4 | Begleiten | Das Gelege mit Osk umbetten |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Heatwave`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_GEAR_BOOTS_3; ITM_EVO_EMBERCORE
**Folge:** Pyroluths nisten auf dem neuen Platz (sichtbar nach Ausbruch)

#### SQ_121 · Die Kisten von gestern

*Fraktion · Goldklang-Kontor · Akt III · Auftrag: Marieke Holm (Schlackenwehr) · Intensität 4 · ~40 min*

In Akt III bittet Marieke den Wärter um einen Gefallen, der keiner ist: Sie will die Kisten aus MQ_A2_03 zurückverfolgen und wissen, wo sie gelandet sind. Je nachdem, was der Wärter damals tat, ist das ein Geständnis – oder eine Abrechnung.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Marieke ohne Lächeln |
| 2 | Untersuchen | Frachtspuren an der Obsidianwacht |
| 3 | Entscheidung | Marieke antworten (Ton nach FLAG_KONTOR_CRATES) |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_05 & Quest.MQ_A2_07`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · Lore „Frachtweg nach Dorunsruh“; ITM_GEAR_TOOL_4
**Folge:** Marieke-Vignette im Epilog erhält eine Zeile

#### SQ_122 · Das Kraterherz träumt

*Rätsel & Ruinen · Akt II · Auftrag: Glutnarben-Tutorin Asha (Schlackenwehr) · Intensität 4 · ~40 min*

Asha hat Glutnarben – Zeichen, dass sie als Kind in einen Ausbruch geriet und ein Ignavyr sie trug. Sie glaubt, Pyr'thagon träumt in Bildern, die man im Obsidian sehen kann. Der Wärter sucht drei Obsidianflächen, in denen sich „Träume“ spiegeln.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ashas Geschichte |
| 2 | Untersuchen | Drei Obsidianspiegel in der Klamm |
| 3 | Rätsel | Die Bilder in Reihenfolge bringen |
| 4 | Beobachten | Ein Ignavyr am Kraterrand beobachten |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Pyr'thagon (Seite 2); ITM_MAT_OBSIDIAN ×3
**Folge:** Ashas Traumtafeln in der Zunfthalle

#### SQ_123 · Rauchzeichen

*Fraktion · Wildwacht · Akt II · Auftrag: Wildwächterin Eila (Aschehütte) · Intensität 3 · ~30 min*

Eila leitet die Aschehütte. Seit dem letzten Ausbruch kommen Fumels aus dem Krater ins Tal und lassen Vieh verstummen. Die Bauern wollen sie vertreiben. Eila glaubt, die Fumels fliehen vor etwas.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Eila an der Aschehütte |
| 2 | Beobachten | Fumels im Tal beobachten |
| 3 | Untersuchen | Im Krater den Grund der Flucht finden |
| 4 | Entscheidung | Bauern und Fumels |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03` · **Variante/Bedingung:** `Weather=Ashfall`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F03 +150 · ITM_CON_CLEANSE ×2; ITM_TRAP_SHADE
**Folge:** Fumels kehren zurück, Vieh erholt sich (Bark)

#### SQ_124 · Thermen für alle

*Menschen · Nachhall · Auftrag: Thermenwirtin Seraphe (Schlackenwehr) · Intensität 2 · ~25 min*

Im Nachhall will Seraphe die Thermen für Echos öffnen – ein Becken nur für sie. Die Stammgäste murren. Der Wärter überzeugt die Gäste mit einem Nachmittag, an dem Echos und Menschen nebeneinander baden.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Seraphes Plan |
| 2 | Sprechen | Stammgast Aldo murrt |
| 3 | Beobachten | Aschwels im warmen Becken beobachten |
| 4 | Lager | Einen Nachmittag in den Thermen |

**Voraussetzung:** `Act>=Nachhall`
**Belohnung:** 1.450 ◎ · 2.000 Wärter-EP · ITM_FOODC_STEW ×2; Hain-Dekor ITM_DECO_HOTSPRING
**Folge:** Echo-Becken in den Thermen (Ambient)

#### SQ_125 · Die Obsidianklamm-Brücke

*Fraktion · Wildwacht · Akt II · Auftrag: Wildwächterin Eila (Aschehütte) · Intensität 4 · ~35 min*

Die Hängebrücke über die Obsidianklamm ist gerissen; Obsidrax nisten auf beiden Seiten und lassen niemanden die Ankerpunkte erreichen. Eila braucht die Brücke für Rettungseinsätze.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur gerissenen Brücke |
| 2 | Beobachten | Obsidrax-Nester beobachten |
| 3 | Traversal | Zu den Ankerpunkten klettern |
| 4 | Entscheidung | Brücke versetzen oder Nester umgehen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_BOOTS_3; ITM_MAT_OBSIDIAN ×2
**Folge:** Neue Brücke (Data Layer)

#### SQ_126 · Drusen, die summen

*Forschung · Akt II · Auftrag: Kristallkundlerin Maja (Kaldra) · Intensität 3 · ~30 min*

Drusils lassen Kristalldrusen in Gesteinsblasen wachsen. Maja hat herausgefunden, dass die Drusen summen, wenn ein Gewitter naht. Sie will ein Frühwarnnetz bauen – mit Drusen, nicht mit gefangenen Echos.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Majas Werkstatt |
| 2 | Beobachten | Drusils beim Wachsenlassen beobachten |
| 3 | Bedingung | Ein Gewitter abwarten |
| 4 | Untersuchen | Summende Drusen für das Netz finden |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_KS_052; ITM_MAT_SULFURCRYSTAL ×3
**Folge:** Gewitter-Warnnetz in Kaldra (Glocken vor Gewitter)

#### SQ_127 · Was die Freien bauen

*Fraktion · Freie Stimmen · Akt III · Auftrag: Tavesh Amaru (Schlackenwehr) · Intensität 4 · ~40 min*

In Akt III bitten die Freien Stimmen den Wärter, ihnen beim Bau eines Hauses für befreite Echos in Kaldra zu helfen – ihr erstes offenes Haus. Die Zunft liefert Metall, wenn der Wärter für die Freien bürgt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tavesh in Kaldra |
| 2 | Sprechen | Helka um Metall bitten |
| 3 | Liefern | Metall liefern |
| 4 | Beobachten | Ambraks beim Bau beobachten |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_04 & Quest.MQ_A2_03`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · Hain-Dekor ITM_DECO_FREEHOUSE; ITM_CON_STAMINA ×3
**Folge:** Haus der Freien Stimmen in Kaldra (offen, sichtbar)

#### SQ_128 · Die Esse-Probe

*Wärterprüfung · Akt II · Auftrag: Kaldrex Vorn (Schlackenwehr) · Intensität 5 · ~35 min*

Kaldrex' Schmiedeprobe (CANON §54): drei Kämpfe an der Großen Esse, in denen jede dritte Runde Glutboden entsteht. Danach erzählt Kaldrex, warum er das Lager-Tor nie schloss.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Kaldrex' Herausforderung |
| 2 | Kampf | Erste Esse |
| 3 | Kampf | Zweite Esse |
| 4 | Kampf | Kaldrex an der Großen Esse |
| 5 | Entscheidung | Kaldrex zuhören |

**Voraussetzung:** `Act>=Akt II & Akkorde>=6`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_EMBER; ITM_HELD_EMBERCORE
**Folge:** Kaldrex-Barks; Essentraining

#### SQ_129 · Die Glut im Keller

*Fraktion · Freie Stimmen · Akt II · Auftrag: Zelle Schlackenwehr (Schlackenwehr) · Intensität 4 · ~35 min*

Die Zelle der Freien Stimmen in Schlackenwehr versteckt in einem Keller ein Nucleox – ein sehr seltenes Echo, das jemand als Energiequelle für eine illegale Schmiede missbrauchte. Es glüht zu stark; der Keller wird zur Falle.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Hilferuf der Zelle |
| 2 | Beobachten | Das überhitzte Nucleox beobachten |
| 3 | Heilen | Seine Glut mit zwei Kühlkreisen beruhigen |
| 4 | Begleiten | Das Nucleox in den Krater zurückbringen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_CON_WARM ×3; Kodex-Beobachtung Nucleox
**Folge:** Nucleox im Krater sichtbar (nachts)

#### SQ_130 · Ein Lied für Kaldra

*Fraktion · Freie Stimmen · Nachhall · Auftrag: Tavesh Amaru (Kaldra) · Intensität 3 · ~30 min*

Im Nachhall feiert das Haus in Kaldra seinen ersten Jahrestag. Tavesh will ein Lied, das Echos und Menschen gemeinsam singen. Der Wärter sammelt Rufe von fünf befreiten Echos und setzt sie zusammen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tavesh' Wunsch |
| 2 | Beobachten | Rufe der befreiten Echos aufzeichnen |
| 3 | Rätsel | Das Lied setzen |
| 4 | Lager | Jahrestag feiern |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A1_04`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · Hain-Dekor ITM_DECO_KALDRASONG; ITM_LURE_WHISTLE
**Folge:** Lied als Musikvariante in Kaldra

#### SQ_131 · Der Volket-Zaun

*Fraktion · Freie Stimmen · Akt II · Auftrag: Zelle Schlackenwehr (Schlackenwehr) · Intensität 4 · ~35 min*

Ein Landbesitzer hat Volkets an einen Metallzaun gekettet, um ihn mit Blitz aufzuladen. Die Zelle will die Volkets befreien, ohne dass der Besitzer sie erneut fängt. Der Wärter sucht einen Weg, den Besitzer zu überzeugen – oder zu überlisten.

**Lösungen:** Befreien und gehen · Grim bei der Wildwacht melden · Grim einen Blitzableiter bauen helfen, der die Volkets überflüssig macht (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum Zaun |
| 2 | Beobachten | Die angeketteten Volkets beobachten |
| 3 | Sprechen | Grim zur Rede stellen |
| 4 | Entscheidung | Lösung wählen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_TRAP_CHIME; ITM_HELD_TAKTRING
**Folge:** Volkets frei; Zaun bleibt mit Blitzableiter statt Ketten


---

## 6. Hvitfell I (R07) – SQ_132–SQ_140

Die ersten neun Hvitfell-Quests drehen sich um Erinnerung (Runa, das Namensbuch, der Eisspiegel) und um das Leben am Gletscher. Die Ordensquests in Hvitfell (Kette *Das Schweigen lernen*) und die übrigen elf Hvitfell-Quests folgen in K51.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_132 | Die Briefe aus Hvitmark | Fraktion | F01 · FQ_F01_04 | Akt II | 5 | 45 | – |
| SQ_133 | Snevel im Spiegelsee | Echo-Geschichte | – | Akt II | 2 | 25 | Time=Dusk |
| SQ_134 | Lawinenwinter | Fraktion | F03 | Akt II | 4 | 40 | Weather=Snow |
| SQ_135 | Der Name im Eis | Echo-Geschichte | – | Akt III | 3 | 30 | Weather=Aurora |
| SQ_136 | Spuren am Pass | Fraktion | F03 | Akt II | 3 | 30 | Weather=Snow |
| SQ_137 | Die Polarlichtnacht | Weltereignis | – | Akt II | 3 | 30 | Weather=Aurora |
| SQ_138 | Die Wacht am Isvaldtind | Fraktion | F03 | Nachhall | 5 | 45 | Time=Night |
| SQ_139 | Der Spiegel unter dem See | Rätsel & Ruinen | – | Akt II | 4 | 35 | Weather=Fog |
| SQ_140 | Rentiere aus Klang | Fraktion | F03 | Akt II | 3 | 30 | Time=Day |

#### SQ_132 · Die Briefe aus Hvitmark

*Fraktion · Akademie der Resonanz · Kette **Aevrins Akten** (2/4) · Akt II · Auftrag: Aevrin Thal (Hvitmark) · Intensität 5 · ~45 min*

Aevrins Akten führen nach Hvitmark: Venn schrieb über Jahre Briefe an „eine Überlebende der Klangpest“ – an Sereth. Runa die Erinnernde bewahrt Abschriften, weil sie alle Briefe der Stadt aufbewahrt. Der Wärter liest, was Venn Sereth versprach.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Runa die Erinnernde |
| 2 | Untersuchen | Venns Briefe im Archiv finden |
| 3 | Entscheidung | Die Briefe an Aevrin senden – oder Sereth zuerst zeigen |
| 4 | Sprechen | Aevrins Antwort per Klangbrief |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=4 & Quest.SQ_099 & Quest.MQ_A2_07`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Venns Briefe“ (TruthLevel 6); ITM_CON_SENSE ×2
**Folge:** Sereth-Szene in MQ_A2_08 erhält eine Zeile, falls der Wärter ihr die Briefe zeigt

#### SQ_133 · Snevel im Spiegelsee

*Echo-Geschichte · Akt II · Auftrag: Eisfischer Askel (Hvitmark) · Intensität 2 · ~25 min*

Askel fischt im Spiegelsee durch Eislöcher. Snevels klauen seine Köder – und lassen ihm dafür kleine Eisfiguren da. Askel will wissen, ob das ein Tausch ist. Der Wärter beobachtet und findet: Ja, und die Figuren sind Fische.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Askel am Eisloch |
| 2 | Beobachten | Snevels in der Dämmerung beobachten |
| 3 | Untersuchen | Die Eisfiguren untersuchen |
| 4 | Entscheidung | Askel den Tausch erklären |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · ITM_FOOD_ICEFISH ×5; Kodex-Beobachtung Snevel (Tausch)
**Folge:** Askel tauscht weiter (Bark); Eisfiguren als Hain-Dekor kaufbar

#### SQ_134 · Lawinenwinter

*Fraktion · Wildwacht · Akt II · Auftrag: Gletscherwartin Tora (Gletscherwacht) · Intensität 4 · ~40 min*

Ein schwerer Schneefall droht die Gletscherzunge abbrechen zu lassen. Darunter liegt Eiðvik-Neu. Tora braucht Messungen am Gletscher und eine Warnkette mit Hallkids, deren Rufe weit tragen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Schneefall |
| 2 | Untersuchen | Risse in der Gletscherzunge messen |
| 3 | Beobachten | Hallkids für die Warnkette finden |
| 4 | Sprechen | Sprecherin Astrid warnen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_CLOAK_3; ITM_CON_WARM ×3
**Folge:** Hallkid-Warnkette (Ruf bei Gefahr, Ambient)

#### SQ_135 · Der Name im Eis

*Echo-Geschichte · Akt III · Auftrag: Runa die Erinnernde (Hvitmark) · Intensität 3 · ~30 min*

In Akt III bittet Runa den Wärter, einen Namen zu finden, der im Polarlicht von MQ_A2_04 fehlte. Ein Uvarn soll ihn kennen – wer seinen Ruf hört, erinnert sich an einen vergessenen Namen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Runa und die Namensliste |
| 2 | Bedingung | Polarlicht |
| 3 | Beobachten | Den Ruf eines Uvarn hören |
| 4 | Entscheidung | Runa den Namen bringen |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Weather=Aurora`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_NAMESTONE; Kodex-Beobachtung Uvarn
**Folge:** Name auf dem Klangpest-Mahnmal ergänzt

#### SQ_136 · Spuren am Pass

*Fraktion · Wildwacht · Akt II · Auftrag: Gletscherwartin Tora (Passhütte) · Intensität 3 · ~30 min*

An der Passhütte kommen Kjalmurs aus dem Hochland ins Tal, viel zu früh. Tora vermutet, dass etwas sie vertreibt. Der Wärter folgt den Spuren zurück und findet einen Ordensposten, der Stillsteine im Schnee lagert.

**Lösungen:** Mit Gewalt räumen ist nicht vorgesehen – stattdessen: Eik überzeugen · Sigrun Fjall holen · Eik zeigen, was die Kjalmurs tun (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Kjalmurs an der Passhütte beobachten |
| 2 | Untersuchen | Spuren zum Hochland verfolgen |
| 3 | Sprechen | Bruder Eik (Schiefertafel) |
| 4 | Entscheidung | Den Posten auflösen oder verhandeln |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F03 +150 · ITM_EMAT_STILLSHARD; ITM_GEAR_BOOTS_3
**Folge:** Ordensposten geräumt; Kjalmurs ziehen zurück

#### SQ_137 · Die Polarlichtnacht

*Weltereignis · Akt II · Auftrag: Ylva (Wollstube) (Hvitmark) · Intensität 3 · ~30 min*

Wenn das Polarlicht über Hvitmark steht, ziehen die Familien auf den Spiegelsee und singen für die Toten von Eiðvik. Ylva fehlen Laternen aus Lysmara-Licht. Der Wärter bittet die Lysmaras, ihr Licht zu teilen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Polarlicht |
| 2 | Beobachten | Lysmaras im Polarlicht beobachten |
| 3 | Entscheidung | Die Lysmaras um Licht bitten (Lied, Köder oder Geduld) |
| 4 | Lager | Mit der Stadt auf dem See singen |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Aurora`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_LURE_AURORAGLASS; Hain-Dekor ITM_DECO_AURORALANTERN
**Folge:** Polarlichtnacht als Weltereignis

#### SQ_138 · Die Wacht am Isvaldtind

*Fraktion · Wildwacht · Nachhall · Auftrag: Gletscherwartin Tora (Isvaldtind-Biwak) · Intensität 5 · ~45 min*

Im Nachhall richtet die Wildwacht am Isvaldtind ein Biwak ein, um den Gletscherdom zu bewachen, unter dem Isv'aldr wacht oder schläft. Tora will den Weg sicher machen – mit Seilen, Kjalgrund-Spuren und einer Nacht auf dem Gipfel.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Traversal | Den Aufstieg sichern |
| 2 | Beobachten | Kjalgrunds auf dem Grat beobachten |
| 3 | Lager | Eine Nacht am Gipfel |
| 4 | Beobachten | Isv'aldr im Dom lauschen |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_P03` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · Titel „Gipfelwacht“; ITM_GEAR_CLOAK_4
**Folge:** Biwak als Schnellreisepunkt

#### SQ_139 · Der Spiegel unter dem See

*Rätsel & Ruinen · Akt II · Auftrag: Silberschmied Eirik (Hvitmark) · Intensität 4 · ~35 min*

Eirik behauptet, unter dem Spiegelsee liege ein zweiter See – ein Spiegel aus Eis, der zeigt, was vor der Klangpest war. Bei Nebel ist er durch die Eislöcher zu sehen. Der Wärter taucht mit Atemmaske unter das Eis.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Eiriks Legende |
| 2 | Bedingung | Nebel über dem See |
| 3 | Traversal | Unter das Eis tauchen |
| 4 | Untersuchen | Bilder im Eisspiegel deuten |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_EVO_AURORATHREAD; Klangfragment (TruthLevel 0)
**Folge:** Eiriks Silberarbeiten zeigen das alte Eiðvik (Laden)

#### SQ_140 · Rentiere aus Klang

*Fraktion · Wildwacht · Akt II · Auftrag: Hirte Halvar (Wildwacht-Helfer) (Fjallstad) · Intensität 3 · ~30 min*

Vardholms ziehen jedes Jahr über das Fjallstad-Tal. Dieses Jahr fehlt der Leitbulle, und die Herde irrt. Halvar, der für die Wildwacht die Herden zählt, vermutet Wilderer. Der Wärter findet den Bullen in einer Gletscherspalte – lebendig, aber eingeklemmt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Die irrende Herde beobachten |
| 2 | Untersuchen | Spuren an der Gletscherzunge |
| 3 | Traversal | In die Spalte steigen |
| 4 | Begleiten | Mit Halvar den Bullen zur Herde führen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F03 +150 · ITM_FOOD_ALPINECHEESE ×3; Kodex-Beobachtung Vardholm (Leittier)
**Folge:** Herde zieht geordnet (Ambient)


---

## 7. Fraktionsketten in diesem Kapitel

| Kette | Fraktion | Einstieg | Titel | Quests (dieses Kapitel fett) |
|---|---|---|---|---|
| FQ_F02_03 | F02 | Rang 3 | Hafenbücher | **SQ_072**, **SQ_074**, **SQ_076**, **SQ_078** |
| FQ_F02_04 | F02 | Rang 4 | Die gläserne Route | **SQ_080**, **SQ_082**, **SQ_101**, **SQ_103** |
| FQ_F03_04 | F03 | Rang 4 | Die stillen Ränder | SQ_053, **SQ_084**, **SQ_086**, **SQ_107** |
| FQ_F04_03 | F04 | Rang 3 | Netze im Nebel | SQ_063, SQ_065, **SQ_088**, **SQ_089** |
| FQ_F04_04 | F04 | Rang 4 | Salz und Freiheit | **SQ_090**, **SQ_109**, **SQ_110**, **SQ_111** |
| FQ_F01_03 | F01 | Rang 3 | Glas der Hochkultur | **SQ_091**, **SQ_093**, **SQ_095**, **SQ_097** |
| FQ_F01_04 | F01 | Rang 4 | Aevrins Akten | **SQ_099**, **SQ_132**, SQ_152, SQ_154 |

| Kette | Bogen | Abschluss |
|---|---|---|
| Hafenbücher | Doppelte Fässer → falsches Siegel → Agent Bartol → Kontorrat | Satzungsklausel als Vorstufe der „Klangtreue“ (K47 §2.2) |
| Die gläserne Route | Leuchtfeuer brauchen Glas → Seeroute → Sturm → Tausch Glas gegen Salz → Landroute | Neuer Handelsweg R04–R06 |
| Die stillen Ränder | Graue Ränder im Moor, an der Küste, am Leuchtfelsen, in der Weite | Jorns Abschiedsbrief; Mahrsil-Refugium |
| Netze im Nebel | Netze im Moor → Perlen aus Saltrand → Werkstatt → Kliffversteck | Keine Fangnetze mehr in R03/R06 |
| Salz und Freiheit | Salzgärten Tangwerft → Harrâd → Notar Basim → Salzfest | Genossenschaften mit Rückkehrrecht |
| Glas der Hochkultur | Scherben → Hymne → Herrschersaal → Glasreif | Reif zerstört, ausgestellt oder versiegelt |
| Aevrins Akten | Geschwärzte Zeilen → Venns Briefe (Fortsetzung K51) | – |

---

## 8. Auftraggeber

| NPC-ID | Name | Quests |
|---|---|---|
| NPC_AEVRIN | Aevrin Thal | SQ_099, SQ_132 |
| NPC_BEKE | Beke Tamsen | SQ_085 |
| NPC_ENNIS | Ennis Rook (Kurierin) | SQ_090, SQ_109, SQ_110, SQ_111 |
| NPC_FORSCHERIN_LIV | Meeresforscherin Liv | SQ_083 |
| NPC_FORSCHER_IDRIS | Forscher Idris | SQ_104 |
| NPC_FS_ZELLE_MIRSAAN | Zelle Mirsaan (Freie Stimmen) | SQ_112 |
| NPC_FS_ZELLE_SCHLACKENWEHR | Zelle Schlackenwehr | SQ_129, SQ_131 |
| NPC_GIESSER_BRAM | Glockengießer Bram | SQ_116 |
| NPC_GLETSCHERWART_TORA | Gletscherwartin Tora | SQ_134, SQ_136, SQ_138 |
| NPC_HIRTE_HALVAR | Hirte Halvar (Wildwacht-Helfer) | SQ_140 |
| NPC_HIRTIN_NAJLA | Hirtin Najla (Ashurim) | SQ_092 |
| NPC_KALDREX | Kaldrex Vorn | SQ_128 |
| NPC_KARAWANENFUEHRERIN_AMARA | Amara (Karawanserei) | SQ_098, SQ_105, SQ_108 |
| NPC_KRATERWART_OSK | Kraterwart Osk | SQ_120 |
| NPC_KRISTALLKUNDLERIN_MAJA | Kristallkundlerin Maja | SQ_126 |
| NPC_LEUCHTWART_FOKKE | Leuchtwart Fokke | SQ_071 |
| NPC_LUND | Grabungsleiterin Saphira Lund | SQ_091, SQ_093, SQ_095, SQ_097 |
| NPC_MARIEKE | Marieke Holm | SQ_117, SQ_121 |
| NPC_PASSWART_JORN | Passwart Jorn (Wildwacht) | SQ_084, SQ_086, SQ_107 |
| NPC_R03_SHADE | Der Schatten | SQ_088, SQ_089 |
| NPC_R04_SAYA | Brunnenköchin Saya | SQ_102 |
| NPC_R05_ASHA | Glutnarben-Tutorin Asha | SQ_122 |
| NPC_R05_ITHREN | Wehrmarkt-Händler Ithren | SQ_115 |
| NPC_R05_KALDREX_GUILD | Zunftsprecherin Helka | SQ_119 |
| NPC_R05_SERAPHE | Thermenwirtin Seraphe | SQ_118, SQ_124 |
| NPC_R05_VOLK | Erzwaage Volk | SQ_113 |
| NPC_R06_BEKE_FISH | Fischhändlerin Beke | SQ_079 |
| NPC_R06_HAUKE | Taucher Hauke | SQ_073 |
| NPC_R06_KLAAS | Werftmeister Klaas | SQ_087 |
| NPC_R06_ODALIS | Kuriositätenhändlerin Odalis | SQ_077 |
| NPC_R07_ASKEL | Eisfischer Askel | SQ_133 |
| NPC_R07_EIRIK | Silberschmied Eirik | SQ_139 |
| NPC_R07_RUNA | Runa die Erinnernde | SQ_135 |
| NPC_R07_YLVA | Ylva (Wollstube) | SQ_137 |
| NPC_RAGNA | Kapitänin Ragna | SQ_080, SQ_082, SQ_101, SQ_103 |
| NPC_SCHMIEDIN_ISOLDE | Schmiedin Isolde | SQ_114 |
| NPC_SHIRAH | Shirah Harrad | SQ_096, SQ_106 |
| NPC_STERNDEUTER_HARUN | Sterndeuter Harun | SQ_094, SQ_100 |
| NPC_TANGSAMMLERIN_GESA | Tangsammlerin Gesa | SQ_075 |
| NPC_TAVESH | Tavesh Amaru | SQ_127, SQ_130 |
| NPC_WIEBKE | Prokuristin Wiebke | SQ_072, SQ_074, SQ_076, SQ_078 |
| NPC_WILDWAECHTERIN_EILA | Wildwächterin Eila | SQ_123, SQ_125 |
| NPC_WITWE_ALKE | Alke (Kliffsund) | SQ_081 |

---

## 9. Weltereignisse aus Nebenquests

Mehrere Nebenquests hinterlassen wiederkehrende Ereignisse (QR-05, K48 §1 „Weltereignis“). Sie werden als `WE_*` im Kalender geführt (K15, K62) und sind nach Questabschluss dauerhaft:

| Ereignis | Quelle | Auslöser | Inhalt |
|---|---|---|---|
| WE_GRATKIN_MIGRATION | SQ_041 (K49) | jährlich, Spieltag 40–45 | Gratkin-Zug über die Pässe |
| WE_ANCESTORFIRE | SQ_045 (K49) | jährlich | Ahnenfeuer auf allen Felsen im Kharsgrat |
| WE_UNDERSTREET_FEST | SQ_061 (K49) | jeder 20. Spieltag | Unterstadt-Fest am Laternensteg |
| WE_REGATTA | SQ_087 | jährlich, Tag | Werftregatta in der Tangwerft-Bucht |
| WE_MIRROR_NIGHT | SQ_096 | Vollmond | Nacht der Spiegel in Qasr Sahrun |
| WE_SALT_FEST | SQ_111 | jährlich | Salzfest in Harrâd und Tangwerft |
| WE_ASH_NIGHT | SQ_118 | Ascheregen (Nachhall) | Aschenacht-Führungen in Ignareth |
| WE_AURORA_NIGHT | SQ_137 | Polarlicht | Gesang auf dem Spiegelsee |
| WE_SOLVAR_RACE | SQ_105 | monatlich | Rennen Karawanserei gegen Kontor |

Weltereignisse geben kleine Belohnungen (Kodex, Dekor, Barks) und nie Machtvorteile (DR-20, DR-27).

---

## 10. Prüfung gegen die Quest-Bibel

`python3 tools/authoring/sq_k50.py` prüft QS-01–QS-15 für SQ_071–140 und QR-09 für die vollständige Region Saltrand (SQ_068–090): **0 Fehler**.

**Saltrand (gesamt mit K49)** – Quote Tageszeit/Wetter/Mond ≥ 25 % ✓

**Sahrun-Weite**

| Kennzahl | Wert |
|---|---|
| Quests | 22 |
| Schritte | 92 (Ø 4,2) |
| Ø Dauer | 39 min |
| Σ Spielzeit | 14,4 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 12 (55 %) |
| Σ Sol | 26.250 ◎ |
| Σ Wärter-EP | 43.500 |
| Kategorien | Fraktion 13, Echo-Geschichte 2, Weltereignis 2, Wärterprüfung 2, Rätsel & Ruinen 1, Menschen 1, Forschung 1 |
| Häufigste Zieltypen | Sprechen 19, Beobachten 17, Untersuchen 12, Entscheidung 11, Gehen 5, Kampf 5, Rätsel 4, Begleiten 4 |

**Ignareth**

| Kennzahl | Wert |
|---|---|
| Quests | 19 |
| Schritte | 77 (Ø 4,1) |
| Ø Dauer | 34 min |
| Σ Spielzeit | 10,8 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 8 (42 %) |
| Σ Sol | 22.800 ◎ |
| Σ Wärter-EP | 37.500 |
| Kategorien | Fraktion 11, Echo-Geschichte 2, Weltereignis 2, Rätsel & Ruinen 1, Menschen 1, Forschung 1, Wärterprüfung 1 |
| Häufigste Zieltypen | Sprechen 19, Beobachten 16, Untersuchen 12, Entscheidung 10, Gehen 3, Rätsel 3, Begleiten 3, Kampf 3 |

**L-01 in Akt II:** Quests mit `TruthLevel` > 4 verlangen `Quest.MQ_A2_07` (W6) oder eine andere Hauptquest-Voraussetzung (QS-11, ergänzt in diesem Kapitel). So kann keine Nebenquest in der Weite den Verrat vorwegnehmen, wenn Spielende die Weite als erste Akt-II-Region wählen.

---

## 11. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | 287 Schritte; Herrschersaal unter der Glasebene, vergrabenes Observatorium, Wrack „Möwe“, Kliffversteck, Eisspiegel; Data Layer für Sturmflutmauer, Obsidianklamm-Brücke, Echo-Becken | K57 |
| Writing | Kontorrat-Sitzung (SQ_078) als Mehrfachentscheidung; Rede in der Oase (SQ_111); Venns Briefe (SQ_132) | K55 |
| Audio | Hymne der Glasstadt (SQ_093), Glockenguss (SQ_116), Lied für Kaldra (SQ_130), Hallkid-Warnkette (SQ_134) | K55 |
| Tech | Seeroute Saltrand–Sahrun als Schnellreise per Schiff (SQ_082) | K40/K65 |
| Combat | Gezeitenprobe (Arena hebt/senkt sich), Mittagsprobe (Blendung alle 2 Runden), Esse-Probe (Glutboden jede 3. Runde) | K35 |
| Art | 12 Hain-Dekor-Objekte | K56 |

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-190 | Nebenquests in frei wählbaren Akt-II-Regionen mit W5–W7-Bezug verlangen die passende Hauptquest als Voraussetzung (QS-11) | L-01 bei freier Reihenfolge | Deutungen in allen Fassungen verzerren |
| ADR-191 | Nebenquest-Folgen dürfen wiederkehrende Weltereignisse erzeugen | Welt wirkt lebendig, Rückkehr lohnt sich (DR-13) | einmalige Folgen |
| ADR-192 | Gedenkquests (Eiðvik, Klangpest) haben Intensität ≤ 3 und keine Kämpfe | Würde des Themas, Sensitivity | Kämpfe gegen „Geister“ |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §191 | Nebenquests SQ_071–SQ_140 (R06 20, R04 22, R05 19, R07 9), 287 Schritte; neue NPCs u. a. Prokuristin Wiebke, Kapitänin Ragna, Leuchtwart Fokke, Grabungsleiterin Saphira Lund, Karawanenführerin Amara, Notar Basim, Wildwächterin Eila, Gletscherwartin Tora, Runa die Erinnernde | LOCKED |
| §192 | Weltereignisse aus Nebenquests `WE_*` (9 in K49/K50) | LOCKED |
| §10 | ADR-190 – ADR-192 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] 70 Nebenquests ausgeschrieben (Kurzinhalt, Schritte, Lösungen, Voraussetzungen, Belohnungen, Folgen)
- [x] Akt-II-Logik (vor/nach W6) über Voraussetzungen abgesichert
- [x] Sensitivity-Hinweise R04/R07
- [x] Ketten fortgeführt bzw. abgeschlossen (7 Ketten)
- [x] Weltereignisse aus Nebenquests
- [x] Alle Prüfregeln erfüllt (0 Fehler), Saltrand vollständig geprüft
- [x] Anforderungen, ADR-190 – ADR-192, CANON §191–§192

➡️ **Nächstes Kapitel: K51 – Nebenquests III (SQ_141–SQ_210).**
