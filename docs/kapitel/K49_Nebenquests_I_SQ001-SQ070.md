# K49 · Nebenquests I (SQ_001–SQ_070): Verdanthain, Kharsgrat, Morvenmoor, Saltrand I

| Feld | Wert |
|---|---|
| Dokument | Kapitel 49 von 68 · Quest-Bibel, Nebenquests Teil I |
| Version | 1.0 |
| Owner | Lead Quest Designer |
| Mitwirkende | Writer (Verdanthain, Kharsgrat, Morvenmoor, Saltrand), Level Design, Narrative Director (L-01-Review), Systems Designer (Belohnungen) |
| Baut auf | K48 (Quest-Bibel QR-01–QR-12, Gerüst `SideQuests.csv`, EP-/Sol-Formeln), K47 (Fraktionen, Ketten, Ruf), K09–K13 (Regionen, Städte, Dörfer, Außenposten), K20–K22 (Arten R01–R03, R06), K44 (Akt I) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Quests/SideQuestDetails.csv`, `SideQuestSteps.csv` (SQ_001–070, 288 Schritte), `FactionChains.csv` (18 Ketten), `Data/Items/Decor.csv`, `KeyItems.csv`, Quelle `tools/authoring/sq_k49.py`, Prüfregeln `sq_common.py` (QS-01–QS-15) |
| Neue Kanon-Einträge | CANON §189 (Nebenquests SQ_001–070), §190 (Hain-Dekor und Schlüsselgegenstände) |

---

## Inhalt

1. [Überblick](#1-überblick)
2. [Wie diese Quests zu lesen sind](#2-wie-diese-quests-zu-lesen-sind)
3. [Verdanthain (R01) – SQ_001–SQ_024](#3-verdanthain-r01--sq_001sq_024)
4. [Kharsgrat (R02) – SQ_025–SQ_046](#4-kharsgrat-r02--sq_025sq_046)
5. [Morvenmoor (R03) – SQ_047–SQ_067](#5-morvenmoor-r03--sq_047sq_067)
6. [Saltrand I (R06) – SQ_068–SQ_070](#6-saltrand-i-r06--sq_068sq_070)
7. [Fraktionsketten in diesem Kapitel](#7-fraktionsketten-in-diesem-kapitel)
8. [Auftraggeber](#8-auftraggeber)
9. [Prüfung gegen die Quest-Bibel](#9-prüfung-gegen-die-quest-bibel)
10. [Anforderungen an andere Abteilungen](#10-anforderungen-an-andere-abteilungen)
11. [Decision Records](#11-decision-records)
12. [Kanon-Änderungen](#12-kanon-änderungen)
13. [Kapitel-Checkliste](#13-kapitel-checkliste)

---

## 1. Überblick

Die ersten 70 Nebenquests gehören zu den Regionen, die der Spieler in Prolog und Akt I betritt. Sie erzählen von einem Land, das sich gerade von der ersten Stille erholt: Wege, die neu gefunden werden müssen; Handel, der wieder anläuft; Echos, deren Gewohnheiten durcheinandergeraten sind. Spätere Quests in denselben Regionen (Akt II, Akt III, Nachhall) greifen die Wahrheiten der Hauptstory auf – Kronensplitter-Lieferungen im Moor, die Siegelkriegs-Chronik der Klans, Pells Abschlussarbeit über den geheilten Lindwald.

| Kennzahl | Wert |
|---|---|
| Quests | 70 |
| Schritte | 288 (Ø 4,1) |
| Ø Dauer | 34 min |
| Σ Spielzeit | 39,2 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 41 (59 %) |
| Σ Sol | 48.050 ◎ |
| Σ Wärter-EP | 115.800 |
| Kategorien | Fraktion 41, Rätsel & Ruinen 6, Forschung 6, Echo-Geschichte 5, Menschen 5, Wärterprüfung 4, Weltereignis 3 |
| Häufigste Zieltypen | Sprechen 59, Beobachten 56, Untersuchen 41, Entscheidung 41, Gehen 20, Begleiten 13, Bedingung 12, Kampf 11 |

**Ton nach Region:**

| Region | Grundton | Wiederkehrende Motive |
|---|---|---|
| Verdanthain | Warm, häuslich, neugierig | Honig, Brannoc die Lauscherin, Kinder und Echos, die Außenstelle der Akademie |
| Kharsgrat | Rau, stolz, solidarisch | Klanschwüre, Bergrettung, Erz und Ehre, die Gratkin-Wanderung |
| Morvenmoor | Geheimnisvoll, nächtlich, gemeinschaftlich | Unterstadt, Lieder als Währung, Nebel, die Kapellen des Ordens nach W6 |
| Saltrand | Offen, geschäftig, salzig | Werft, Fischerei, Kontorhandel (Fortsetzung in K50) |

---

## 2. Wie diese Quests zu lesen sind

Jede Quest erscheint als **Questkarte**: Kopfzeile (Kategorie, Fraktion, Kette, Verfügbarkeit, Auftraggeber, Intensität, Dauer), Kurzinhalt, gegebenenfalls **Lösungen** (bei Dilemmata immer mit dritter Lösung, QR-04), Schritte in Tagebuch-Formulierung (K48 §3), Voraussetzung in Bedingungssprache (K48 §6), Belohnung und **Folge** (QR-05). Sol und Wärter-EP sind **nicht handgesetzt**, sondern aus K48 §8 berechnet:

| Wert | Formel (K48 §8) |
|---|---|
| Sol | `round50((150 + 12 × Dauer) × Aktfaktor)`, Aktfaktor 1,0 / 1,8 / 2,6 / 3,2 (Akt I / II / III / Nachhall), ≤ 3.000 |
| Wärter-EP | `round50((300 + 40 × Dauer) × 1,0 / 1,3 / 1,6 / 1,8)`, Kettenabschluss × 1,5, 400–2.000 |
| Ruf | Fraktionsquest +150, Kettenabschluss +400 (K47) |

**Voraussetzungen** entstehen ebenfalls automatisch: Verfügbarkeitsakt (`Act>=…`), Rufstart der Fraktion (`Quest.MQ_…`, K47 §2), Einstiegsrang der Kette (`Rank.F##>=n`) und die vorherige Kettenquest. Handgesetzte Zusätze stehen in den Daten (`ExtraPre`).

**Dialog-IDs** folgen `DLG_SQ_###_##`; Untersuchungshinweise `CLUE_SQ###_n` werden von Level Design platziert (K57); Rätsel `PZ_SQ###_*` sind Instanzen der Rätselbausteine aus K48 §5.

---

## 3. Verdanthain (R01) – SQ_001–SQ_024

Verdanthain ist der Ort, an dem der Spieler das Zuhören lernt. Die Nebenquests verstärken das: Viele lösen sich nicht mit Kampf, sondern mit Geduld – ein Rillo, das rückwärts schwimmt, ein Torgrath, der auf einem Nest schläft, eine Nacht in Stille an Brannocs Platz. Drei Fraktionen sind präsent: die Wildwacht (Heimat), die Akademie (neue Außenstelle ab MQ_A1_07) und das Kontor (Ossians Honigweg); die Freien Stimmen ziehen als Kurierin Ennis durch.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_001 | Messlatten im Farn | Fraktion | F01 · FQ_F01_01 | Akt I | 2 | 25 | – |
| SQ_002 | Das Rillo, das rückwärts schwimmt | Echo-Geschichte | – | Akt I | 2 | 20 | Time=Dusk |
| SQ_003 | Kaels altes Notizbuch | Fraktion | F01 · FQ_F01_01 | Akt I | 3 | 30 | – |
| SQ_004 | Der Schläfer im Uralthain | Echo-Geschichte | – | Akt I | 3 | 25 | – |
| SQ_005 | Das Echo der Außenstelle | Fraktion | F01 · FQ_F01_01 | Akt I | 4 | 35 | Time=Night |
| SQ_006 | Das Gewitter der Wisplets | Weltereignis | – | Akt II | 4 | 25 | Weather=Thunderstorm |
| SQ_007 | Honig für Kharsholm | Fraktion | F02 · FQ_F02_01 | Akt I | 2 | 25 | – |
| SQ_008 | Die Glyphe unter dem Moos | Rätsel & Ruinen | – | Akt I | 3 | 30 | Time=Night |
| SQ_009 | Leere Fässer | Fraktion | F02 · FQ_F02_01 | Akt I | 3 | 30 | Time=Night |
| SQ_010 | Wendelins erste Seite | Rätsel & Ruinen | – | Akt I | 2 | 25 | Time=Dawn |
| SQ_011 | Der Mann mit dem Wagen | Fraktion | F02 · FQ_F02_01 | Akt I | 4 | 35 | – |
| SQ_012 | Briefe an Ilen | Menschen | – | Akt III | 3 | 30 | – |
| SQ_013 | Wo Brannoc saß | Fraktion | F03 · FQ_F03_01 | Akt I | 2 | 25 | Time=Night |
| SQ_014 | Odos Rezept | Menschen | – | Akt I | 1 | 20 | – |
| SQ_015 | Das alte Echo | Fraktion | F03 · FQ_F03_01 | Akt I | 3 | 30 | Weather=Rain |
| SQ_016 | Farnzählung | Forschung | – | Akt I | 2 | 25 | Time=Dawn & Weather=Rain |
| SQ_017 | Das Lied im Stein | Fraktion | F03 · FQ_F03_01 | Akt I | 3 | 30 | – |
| SQ_018 | Nachklang im Lindwald | Forschung | – | Nachhall | 3 | 35 | – |
| SQ_019 | Die Lauscherin | Fraktion | F03 · FQ_F03_01 | Akt I | 5 | 45 | Time=Night & Moon=New |
| SQ_020 | Die Probe der Wurzeln | Wärterprüfung | – | Akt I | 5 | 30 | – |
| SQ_021 | Die Wanderung beginnt | Fraktion | F03 · FQ_F03_02 | Akt I | 3 | 30 | Time=Day |
| SQ_022 | Eine Kiste Äpfel | Fraktion | F04 · FQ_F04_01 | Akt I | 3 | 25 | – |
| SQ_023 | Der Steinbruch von Moosgrund | Fraktion | F04 · FQ_F04_01 | Akt I | 4 | 35 | – |
| SQ_024 | Die Nachtfähre | Fraktion | F04 · FQ_F04_01 | Akt I | 4 | 30 | Time=Night |

#### SQ_001 · Messlatten im Farn

*Fraktion · Akademie der Resonanz · Kette **Die Außenstelle** (1/4) · Akt I · Auftrag: Archivarin Pell (Eichenhall) · Intensität 2 · ~25 min*

Die neue Akademie-Außenstelle braucht Messreihen vom Rand der geheilten Lindwald-Zone. Pell gibt dem Wärter drei Resonanzlatten mit – und die Bitte, nicht nur zu messen, sondern aufzuschreiben, wie sich die Echos dort verhalten. Ihre These: Geheilte Zonen klingen eine Weile nach.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Archivarin Pell in der Außenstelle aufsuchen |
| 2 | Gehen | Drei Messlatten am Rand der geheilten Zone setzen |
| 3 | Beobachten | Zwei Verhaltensmerkmale der Mossling-Herde am Zonenrand festhalten |
| 4 | Liefern | Die Klangharz-Probe von der Latte zu Pell bringen |

**Voraussetzung:** `Quest.MQ_A1_07`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Ruf F01 +150 · Kodex-Beobachtung Mossling; ITM_LURE_BELLCHIME
**Folge:** Pells Messkarte hängt in der Außenstelle; Barks über „nachklingende Zonen“

#### SQ_002 · Das Rillo, das rückwärts schwimmt

*Echo-Geschichte · Akt I · Auftrag: Lina (Kind, Lindwiesen) (Lindwiesen) · Intensität 2 · ~20 min*

Lina schwört, dass ein Rillo im Mühlbach gegen die Strömung zurück zum Wald schwimmt, jeden Abend. Die Erwachsenen lachen. Der Wärter folgt dem Rillo und findet ein Nest unter einer eingestürzten Brücke, das seit der Stillezone abgeschnitten war.

**Lösungen:** Selbst räumen (schnell) oder Lina anleiten (+Bark-Kette, Lina wird später Wildwacht-Helferin im Nachhall).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Lina zuhören |
| 2 | Beobachten | Das Rillo in der Dämmerung beobachten |
| 3 | Untersuchen | Spuren am Bach bis zur alten Brücke verfolgen |
| 4 | Entscheidung | Den Durchgang freiräumen oder Lina zeigen, wie man es selbst tut |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 400 ◎ · 1.100 Wärter-EP · ITM_FOOD_LINDHONEY ×3; Kodex-Beobachtung Rillo
**Folge:** Rillo-Familie lebt am Mühlbach (sichtbar); Lina grüßt den Wärter mit Namen

#### SQ_003 · Kaels altes Notizbuch

*Fraktion · Akademie der Resonanz · Kette **Die Außenstelle** (2/4) · Akt I · Auftrag: Archivarin Pell (Eichenhall) · Intensität 3 · ~30 min*

Pell hat in den Kisten der Außenstelle ein Notizbuch von Kael gefunden – aus der Zeit vor seiner Aufnahme. Seine Thesen über „messbares Hören“ sind klug und falsch zugleich. Pell bittet den Wärter, drei Versuche nachzustellen, um zu sehen, wo Kael recht hatte.

**Lösungen:** Einfühlsam (Kael hatte Angst, nicht zu hören), neugierig (die Messungen sind brauchbar), entschlossen (die Methode ist gefährlich) – alle gleich belohnt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Pell zeigt das Notizbuch |
| 2 | Untersuchen | Drei Versuchsorte im Eichenhall-Forst wiederfinden |
| 3 | Foto | Ein Chimbal beim Antwortgesang fotografieren (≥ 3 Sterne) |
| 4 | Entscheidung | Pell sagen, was an Kaels Thesen stimmt |

**Voraussetzung:** `Quest.MQ_A1_07 & Quest.SQ_001`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F01 +150 · ITM_KS_017; Kodex-Fragment „Messbares Hören“
**Folge:** Notizbuch wird in K45 (MQ_A2_06) von Kael erwähnt; Dialogvariante je Antwort

#### SQ_004 · Der Schläfer im Uralthain

*Echo-Geschichte · Akt I · Auftrag: Holzfäller Torben (Uralthain-Lager) · Intensität 3 · ~25 min*

Ein Torgrath liegt seit Tagen quer über dem Holzweg im Uralthain und rührt sich nicht. Torben will ihn nicht wecken – „man weckt keinen Berg“. Der Wärter findet heraus, warum das Echo dort ruht: Unter ihm brütet eine Brokk-Familie in einer Mulde.

**Lösungen:** Weg verlegen (Torben brummt, hilft aber) · warten (3 Spieltage, kein Echtzeit-Timer) · Torgrath mit Ruhekorb umsiedeln (nur mit ITM_TRAP_REST aus SQ_001-Kette, Kodex-Bonus).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Torben am Lager |
| 2 | Beobachten | Den ruhenden Torgrath beobachten |
| 3 | Untersuchen | Die Mulde unter dem Torgrath untersuchen |
| 4 | Entscheidung | Den Holzweg verlegen oder auf das Schlüpfen warten |

**Voraussetzung:** `–`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_TRAP_REST; Rezept RCP_037
**Folge:** Neuer Holzweg (Data Layer) oder Brokk-Jungtiere am alten Weg nach 3 Spieltagen

#### SQ_005 · Das Echo der Außenstelle

*Fraktion · Akademie der Resonanz · Kette **Die Außenstelle** (3/4) · Akt I · Auftrag: Archivarin Pell (Eichenhall) · Intensität 4 · ~35 min*

In der Außenstelle verschwinden nachts Messinstrumente. Pell verdächtigt die Freien Stimmen. Der Wärter findet stattdessen ein junges Lumow, das die glänzenden Teile sammelt – und eine Frage: Darf die Akademie ein Echo einfangen, das sie stört?

**Lösungen:** Lumow binden (Wärter) · freilassen im Forst mit Ersatz-Glanzsteinen (Wildwacht-Bark) · Pell richtet ein „Lumow-Fach“ ein (dritte Lösung, Pell-Bark im Nachhall).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Spuren in der Außenstelle bei Nacht |
| 2 | Beobachten | Das Lumow beim Sammeln beobachten |
| 3 | Gehen | Dem Lumow zu seinem Hort folgen |
| 4 | Entscheidung | Pell vorschlagen, was mit dem Lumow geschieht |

**Voraussetzung:** `Quest.MQ_A1_07 & Quest.SQ_003` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F01 +150 · ITM_LURE_LANTERN; Kodex-Beobachtung Lumow (Sammler)
**Folge:** Lumow wohnt im Dachgebälk der Außenstelle oder im Forst; Pell entschuldigt sich bei Tavesh' Leuten (Bark)

#### SQ_006 · Das Gewitter der Wisplets

*Weltereignis · Akt II · Auftrag: Wirt Odo (Eichenhall) · Intensität 4 · ~25 min*

Seit der Resonanzsturm über Aethris lag, ziehen Wisplets bei jedem Gewitter in Schwärmen über Eichenhall und schlagen Funken an den Dachrinnen. Odo fürchtet um sein Strohdach. Der Wärter findet heraus, dass die Wisplets einem Ton folgen, der vom alten Wetterturm kommt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Auf ein Gewitter über Eichenhall warten (Zeit vorspulen erlaubt) |
| 2 | Beobachten | Den Schwarm beobachten |
| 3 | Untersuchen | Den Ton zum Wetterturm zurückverfolgen |
| 4 | Rätsel | Die Windglocken des Turms neu stimmen |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · ITM_LURE_WINDCHIME; Hain-Dekor ITM_DECO_WEATHERBELL
**Folge:** Wisplets tanzen bei Gewitter um den Turm statt um die Dächer; Odo stiftet ein Freibier-Bark

#### SQ_007 · Honig für Kharsholm

*Fraktion · Goldklang-Kontor · Kette **Lindenhonig** (1/4) · Akt I · Auftrag: Kontorschreiber Ossian (Eichenhall) · Intensität 2 · ~25 min*

Ossian will einen kleinen Handelsweg eröffnen: Lindenhonig aus Lindwiesen gegen Bergkäse aus Kharsholm. Dafür braucht er einen Wärter, der die Imker überzeugt – die trauen dem Kontor nicht, seit es vor Jahren ihre Preise drückte.

**Lösungen:** Hoher Preis (Hilde zufrieden, Ossian murrt) · niedriger Preis (Ossian zufrieden) · Gewinnbeteiligung (beide zufrieden, nur mit neugieriger Frage nach den Bienen-Echos freigeschaltet).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ossian im Kontor |
| 2 | Sprechen | Imkerin Hilde zuhören |
| 3 | Beobachten | Die Myrthorn bei der Bestäubung beobachten (Hildes Bedingung) |
| 4 | Entscheidung | Einen Preis aushandeln |

**Voraussetzung:** `Quest.MQ_A1_05`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Ruf F02 +150 · ITM_FOOD_LINDHONEY ×5; Rezept RCP_041
**Folge:** Honigfässer am Kontor; Hilde verkauft ab jetzt an Wendels Wärterbedarf

#### SQ_008 · Die Glyphe unter dem Moos

*Rätsel & Ruinen · Akt I · Auftrag: Schnitzer Anselm (Eichenhall) · Intensität 3 · ~30 min*

Anselm hat beim Holzholen im Moosgrund eine Steinplatte mit dorunischen Zeichen gefunden. Er will sie als Tischplatte. Der Wärter erkennt, dass die Glyphen einen Ton beschreiben – und dass drei weitere Platten im Hügel liegen müssen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Anselms Fund ansehen |
| 2 | Untersuchen | Drei weitere Platten im Moosgrund finden |
| 3 | Rätsel | Die Platten in Klangreihenfolge legen |
| 4 | Beobachten | Das Glyphaune beobachten, das auf den Ton antwortet |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_EVO_GLYPHSHARD; Klangfragment (TruthLevel 0)
**Folge:** Glyphenkreis im Moosgrund (POI, Rückkehrort); Glyphaune nachts dort häufiger

#### SQ_009 · Leere Fässer

*Fraktion · Goldklang-Kontor · Kette **Lindenhonig** (2/4) · Akt I · Auftrag: Kontorschreiber Ossian (Eichenhall) · Intensität 3 · ~30 min*

Die erste Honiglieferung kommt in Kharsholm leer an. Ossian vermutet Diebe. Der Wärter verfolgt den Weg zurück und findet bei der Linnfurt einen Riss im Fass – und eine Spur, die nicht von Menschen stammt, sondern von einer Sporix-Kolonie, die süchtig nach Honig geworden ist.

**Lösungen:** Kolonie vertreiben (schnell, Wildwacht-Bark tadelt) · Fässer mit Harz versiegeln (Ossian zahlt) · Köderhonig an einem anderen Ort anbieten (dritte Lösung, Kodex-Bonus).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum Linnfurt-Posten |
| 2 | Untersuchen | Spuren der Fässer in der Farnschlucht |
| 3 | Beobachten | Die Sporix-Kolonie nachts beobachten |
| 4 | Entscheidung | Lösung für Weg und Kolonie wählen |

**Voraussetzung:** `Quest.MQ_A1_05 & Quest.SQ_007` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F02 +150 · ITM_TRAP_SCENT; ITM_MAT_FERNFIBER ×5
**Folge:** Neue Wegführung mit Duftfallen-Schutz; Sporix-Kolonie bleibt und bestäubt die Farnschlucht

#### SQ_010 · Wendelins erste Seite

*Rätsel & Ruinen · Akt I · Auftrag: Greta (Wildwacht-Kammer) (Eichenhall) · Intensität 2 · ~25 min*

Greta hat beim Ausräumen der Wildwacht-Kammer eine Seite in Wendelins Handschrift gefunden – eine Wegbeschreibung zu einem Ort „wo die erste Arena hätte stehen sollen“. Der Ort ist ein Felsring im Lindwald, in dem Echos still werden, um zu lauschen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Greta zeigt die Seite |
| 2 | Gehen | Der Wegbeschreibung in den Lindwald folgen |
| 3 | Untersuchen | Den Felsring untersuchen |
| 4 | Beobachten | Das Cantaroth beobachten, das im Ring singt |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Dawn`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Wendelin-Tagebuch (Sammelseite); ITM_LURE_TUNINGFORK
**Folge:** Felsring wird zum Rastplatz (Lager-Moment möglich)

#### SQ_011 · Der Mann mit dem Wagen

*Fraktion · Goldklang-Kontor · Kette **Lindenhonig** (3/4) · Akt I · Auftrag: Kontorschreiber Ossian (Eichenhall) · Intensität 4 · ~35 min*

Ein fremder Händler bietet den Imkern das Doppelte für ihren Honig – unter der Bedingung, nicht mehr an Ossian zu liefern. Der Wärter folgt seinem Wagen und findet heraus, dass er für ein Konsortium arbeitet, das den Weg nach Kharsholm übernehmen will.

**Lösungen:** Ossian berichten (Kontor setzt sich durch) · Hilde warnen (Imker gründen eine Genossenschaft) · mit dem Händler reden (er gibt zu, unter Druck zu stehen; wird zum fairen Zweitkäufer).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Hilde erzählt vom Angebot |
| 2 | Begleiten | Dem Wagen unauffällig folgen (Abstand halten) |
| 3 | Untersuchen | Die Ladepapiere am Farnwacht-Posten lesen |
| 4 | Entscheidung | Ossian, Hilde oder den Händler selbst ansprechen |

**Voraussetzung:** `Quest.MQ_A1_05 & Quest.SQ_009`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F02 +150 · Kontor-Lieferschein (Lore); ITM_CON_SENSE ×2
**Folge:** Konsortium-Händler verschwindet oder bleibt als fairer Konkurrent (Preise in Lindwiesen −5 %)

#### SQ_012 · Briefe an Ilen

*Menschen · Akt III · Auftrag: Maren (Lindwiesen) (Lindwiesen) · Intensität 3 · ~30 min*

Die alte Maren schreibt seit sechzig Jahren Briefe an „Ilen“ und legt sie in den Klangbrunnen von Lindwiesen. Nach Akt III fragt sie den Wärter, ob Ilen sie je gelesen hat. Der Wärter findet die Briefe – und in ihnen Erinnerungen an seine eigene Familie.

**Lösungen:** Die Wahrheit (Nachklang) erzählen · schonend erzählen · Maren selbst schließen lassen – alle drei würdevoll, kein Flag.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Maren besuchen |
| 2 | Untersuchen | Den Klangbrunnen und die alte Kapelle durchsuchen |
| 3 | Entscheidung | Maren antworten, was mit Ilen geschah |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Familienchronik (Lore, TruthLevel 5); Hain-Dekor ITM_DECO_LETTERBOX
**Folge:** Maren legt ihren letzten Brief „für den, der zuhört“ in den Brunnen; Epilog-Bark

#### SQ_013 · Wo Brannoc saß

*Fraktion · Wildwacht · Kette **Die Spur der Lauscherin** (1/4) · Akt I · Auftrag: Zeugmeisterin Fenja (Eichenhall) · Intensität 2 · ~25 min*

Die Wildwacht ehrt Brannoc die Lauscherin, die 287 ein Echo durch Geduld statt Gewalt zähmte. Fenja glaubt, der Ort liege im Uralthain, nicht dort, wo das Denkmal steht. Der Wärter soll drei Tage-Nächte-Zeichen deuten, die in Brannocs Lied vorkommen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Fenja und Brannocs Lied |
| 2 | Untersuchen | Die Zeichen aus dem Lied im Uralthain finden |
| 3 | Beobachten | Das Lorncant am Fundort beobachten |

**Voraussetzung:** `Quest.MQ_P03` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Ruf F03 +150 · ITM_LURE_WHISTLE; Kodex-Fragment „Brannoc I“
**Folge:** Steinmal „Brannocs Platz“ im Uralthain (Rastort); Denkmal in Eichenhall erhält Tafel

#### SQ_014 · Odos Rezept

*Menschen · Akt I · Auftrag: Wirt Odo (Eichenhall) · Intensität 1 · ~20 min*

Odo kocht seit dreißig Jahren den gleichen Wurzeleintopf und hat das Rezept vergessen – seine Mutter hatte es nur gesungen. Ein altes Chimkin, das im Hof des Wurzelkrugs lebt, summt die Melodie noch. Der Wärter hört hin.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Odos Kummer |
| 2 | Beobachten | Dem Chimkin im Hof zuhören |
| 3 | Sammeln | Die besungenen Zutaten sammeln |
| 4 | Liefern | Odo beim Kochen helfen |

**Voraussetzung:** `–`
**Belohnung:** 400 ◎ · 1.100 Wärter-EP · Rezept RCP_046; ITM_FOODC_STEW ×2
**Folge:** „Odos Wurzeleintopf“ als Gasthaus-Gericht; Chimkin wird Hausechos-Bark

#### SQ_015 · Das alte Echo

*Fraktion · Wildwacht · Kette **Die Spur der Lauscherin** (2/4) · Akt I · Auftrag: Zeugmeisterin Fenja (Eichenhall) · Intensität 3 · ~30 min*

Ein uralter Myrthorn soll sich an Brannoc erinnern – Myrthorn werden alt, und dieser hat einen Klangmal-Riss, der zu Brannocs Lied passt. Der Wärter muss sein Vertrauen gewinnen, ohne ihn zu binden.

**Lösungen:** Geduld (Zeit vorspulen nicht erlaubt im Kreis; 2 Spielstunden) · Lied (Resonanzsinn-Minispiel) · Lockmittel (schnell, aber Fenja ist enttäuscht – Bark).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Den alten Myrthorn im Uralthain finden |
| 2 | Beobachten | Drei Verhaltensmerkmale des Alten beobachten |
| 3 | Entscheidung | Annäherung wählen (Lockmittel, Lied, Geduld) |
| 4 | Untersuchen | Dem Myrthorn zu Brannocs zweitem Ort folgen |

**Voraussetzung:** `Quest.MQ_P03 & Quest.SQ_013` · **Variante/Bedingung:** `Weather=Rain`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F03 +150 · Kodex-Fragment „Brannoc II“; ITM_FOOD_MOSSCAKE ×3
**Folge:** Der alte Myrthorn begleitet den Wärter im Uralthain als Gast (keine Bindung)

#### SQ_016 · Farnzählung

*Forschung · Akt I · Auftrag: Apotheker Lorin (Eichenhall) · Intensität 2 · ~25 min*

Lorin braucht Fernlit-Sporen für Heilsalben, aber Fernlits sind sehr selten geworden. Bevor jemand sammelt, will er wissen, wie viele es gibt. Der Wärter zählt in der Morgendämmerung im Regen – nur dann zeigen sich Fernlits.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Lorins Sorge |
| 2 | Bedingung | Regnerische Morgendämmerung abwarten |
| 3 | Foto | Drei Fernlits fotografieren (Zählung) |
| 4 | Entscheidung | Lorin eine Sammelmenge empfehlen |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Dawn & Weather=Rain`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_CON_HEAL_2 ×3; Kodex-Beobachtung Fernlit
**Folge:** Lorin sammelt nur noch, was der Wärter empfiehlt; Fernlit-Bestand im Nachhall höher oder gleich

#### SQ_017 · Das Lied im Stein

*Fraktion · Wildwacht · Kette **Die Spur der Lauscherin** (3/4) · Akt I · Auftrag: Zeugmeisterin Fenja (Eichenhall) · Intensität 3 · ~30 min*

Am dritten Ort Brannocs, in der Farnschlucht, ist ein Lied in den Fels geritzt – aber zerstört, Teile fehlen. Ein Skirrow imitiert Bruchstücke davon. Der Wärter setzt das Lied aus Fels und Vogelruf zusammen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Felswand in der Farnschlucht |
| 2 | Untersuchen | Lesbare Liedteile finden |
| 3 | Beobachten | Die Imitationen des Skirrow aufzeichnen |
| 4 | Rätsel | Das Lied zusammensetzen |

**Voraussetzung:** `Quest.MQ_P03 & Quest.SQ_015`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F03 +150 · ITM_KS_009; Kodex-Fragment „Brannoc III“
**Folge:** Das Lied ist am Lagerfeuer spielbar (Lager-Moment-Option)

#### SQ_018 · Nachklang im Lindwald

*Forschung · Nachhall · Auftrag: Archivarin Pell (Eichenhall) · Intensität 3 · ~35 min*

Im Nachhall bittet Pell um einen letzten Vergleich: Wie klingt der Lindwald heute, verglichen mit ihrer Messung vom Anfang? Je nach Ende hört der Wärter grünes Wachstum oder silbrige Ruhe – und Pell schreibt ihre Abschlussarbeit darüber.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zu den alten Messlatten |
| 2 | Untersuchen | Die Latten ablesen |
| 3 | Beobachten | Das Vernaune am Zonenrand beobachten |
| 4 | Sprechen | Pell die Ergebnisse bringen |

**Voraussetzung:** `Act>=Nachhall & Ending=NewSong | Ending=SoftSilence`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_MEASURESTAFF; Kodex-Eintrag „Pells Abschlussarbeit“
**Folge:** Pells Arbeit liegt in der Akademie-Bibliothek; Text je Ende verschieden

#### SQ_019 · Die Lauscherin

*Fraktion · Wildwacht · Kette **Die Spur der Lauscherin** (4/4) · Akt I · Auftrag: Zeugmeisterin Fenja (Eichenhall) · Intensität 5 · ~45 min*

Mit allen drei Orten und dem Lied hört der Wärter, was Brannoc 287 hörte: Ein Echo kommt, wenn man lange genug still ist. In einer Nacht am Uralthain wird die Probe wiederholt – ohne Siegel, ohne Köder, nur mit Zuhören. Am Ende steht kein gebundenes Echo, sondern ein Gelöbnis der Wildwacht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Fenja und Hralda erwarten den Wärter |
| 2 | Gehen | Zu Brannocs Platz |
| 3 | Lager | Die Nacht in Stille verbringen (kein Kampf, kein Ruf) |
| 4 | Beobachten | Das Phantalume, das sich nähert, beobachten |
| 5 | Entscheidung | Das Gelöbnis der Lauscher sprechen |

**Voraussetzung:** `Quest.MQ_P03 & Quest.SQ_017` · **Variante/Bedingung:** `Time=Night & Moon=New`
**Belohnung:** 700 ◎ · 2.000 Wärter-EP · Ruf F03 +400 · Titel „Lauscher“; Hain-Dekor ITM_DECO_LISTENERSTONE; ITM_LURE_TUNINGFORK
**Folge:** Wildwacht-Barks nennen den Wärter „Lauscher“; Phantalume erscheint im Uralthain häufiger

#### SQ_020 · Die Probe der Wurzeln

*Wärterprüfung · Akt I · Auftrag: Maelis Wendt (Eichenhall) · Intensität 5 · ~30 min*

Maelis lädt zu einer Schauprobe: drei Kämpfe in Folge, jeder mit einer eigenen Regel des Gartens – nur Blüte-Echos, Überwuchs ab Runde 1, und ein Kampf, in dem nur Formation entscheidet. Wer alle drei besteht, darf im Garten der Arena trainieren.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Maelis' Einladung |
| 2 | Kampf | Erste Probe: nur Blüte-Echos |
| 3 | Kampf | Zweite Probe: Überwuchs ab Runde 1 |
| 4 | Kampf | Dritte Probe: Formationsduell |
| 5 | Beobachten | Unter der Arena lauschen (Sylv'anor im Schlaf) |

**Voraussetzung:** `Akkorde>=4`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_HELD_TONE_BLOOM; Trainingsplatz Arena-Garten
**Folge:** Arena-Garten als Trainingsort; Maelis-Barks

#### SQ_021 · Die Wanderung beginnt

*Fraktion · Wildwacht · Kette **Grenzgänger** (1/4) · Akt I · Auftrag: Zeugmeisterin Fenja (Eichenhall) · Intensität 3 · ~30 min*

Jedes Jahr ziehen Gratkins aus dem Kharsgrat über die Pässe in die Lindwiesen-Auen. Seit der Stille sind die Wege durcheinander. Fenja bittet den Wärter, die Vorhut der Wanderung zu finden und ihren Weg zu kennzeichnen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Fenja und die Wanderkarte |
| 2 | Beobachten | Die Vorhut der Gratkins beobachten |
| 3 | Untersuchen | Alte Wegmarken in der Farnschlucht finden |
| 4 | Gehen | Den Weg am Linnfurt-Posten melden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=2` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F03 +150 · ITM_LURE_WHISTLE; Kodex-Beobachtung Gratkin (Wanderung)
**Folge:** Wegmarken mit Wildwacht-Bändern; Gratkin-Zug sichtbar in R01_Z02

#### SQ_022 · Eine Kiste Äpfel

*Fraktion · Freie Stimmen · Kette **Die Kurierin** (1/4) · Akt I · Auftrag: Ennis Rook (Kurierin) (Moosgrund) · Intensität 3 · ~25 min*

Ennis Rook bittet den Wärter, eine Kiste Äpfel durch die Kontrolle am Linnfurt-Posten zu bringen. Unter den Äpfeln schläft ein junges Brokkar, freigekauft aus einem Steinbruch. Ennis sagt es dem Wärter erst, nachdem er die Kiste trägt.

**Lösungen:** Mitspielen · Ennis überreden, die Kiste offen vorzuzeigen (die Wildwacht lässt es durch – Hralda-Bark) · Wildwacht vorab informieren (Ennis enttäuscht, Ruf trotzdem).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ennis am Rand von Moosgrund |
| 2 | Entscheidung | Die Wahrheit über die Kiste aufnehmen |
| 3 | Begleiten | Mit Ennis durch die Kontrolle |
| 4 | Beobachten | Das Brokkar beim ersten freien Schritt beobachten |

**Voraussetzung:** `Quest.MQ_A1_04`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Ruf F04 +150 · ITM_FOOD_BERRYMIX ×3; Kodex-Beobachtung Brokkar
**Folge:** Ennis vertraut dem Wärter (Bark), Brokkar lebt in der Farnschlucht

#### SQ_023 · Der Steinbruch von Moosgrund

*Fraktion · Freie Stimmen · Kette **Die Kurierin** (2/4) · Akt I · Auftrag: Ennis Rook (Kurierin) (Moosgrund) · Intensität 4 · ~35 min*

Woher kam das Brokkar? Ennis führt den Wärter zum Steinbruch hinter Moosgrund, wo Brokks in Schichten arbeiten – gut gefüttert, aber angekettet. Der Besitzer ist kein Unmensch, nur arm. Die Freien Stimmen wollen die Echos befreien; der Wärter sucht einen Weg, der auch den Besitzer Arnulf nicht ruiniert.

**Lösungen:** Befreien (Freie Stimmen jubeln, Arnulf verarmt – Bark) · Arnulf mit Kontor-Kredit Maschinen ermöglichen (Ossian-Bark) · Brokks frei lassen und Arnulf zeigen, wie man mit Erzkrümeln freiwillige Hilfe gewinnt (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum Steinbruch |
| 2 | Beobachten | Die Arbeits-Brokks beobachten |
| 3 | Sprechen | Steinbrecher Arnulf zuhören |
| 4 | Entscheidung | Lösung für Brokks und Arnulf |

**Voraussetzung:** `Quest.MQ_A1_04 & Quest.SQ_022`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F04 +150 · ITM_TRAP_HOARD; ITM_MAT_COPPERORE ×5
**Folge:** Arnulfs Steinbruch arbeitet mit freiwilligen Brokks (Lohn: Erzkrümel) oder steht still

#### SQ_024 · Die Nachtfähre

*Fraktion · Freie Stimmen · Kette **Die Kurierin** (3/4) · Akt I · Auftrag: Ennis Rook (Kurierin) (Moosgrund) · Intensität 4 · ~30 min*

Ennis muss sieben befreite Echos über den Linnfluss bringen, nachts, ohne Laterne. Ein Rillward-Paar kennt die Furt. Der Wärter muss die Echos ruhig halten – ein einziger Ruf, und die Kontrolle am Posten wird aufmerksam.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Nacht abwarten |
| 2 | Beobachten | Dem Rillward-Paar zur Furt folgen |
| 3 | Begleiten | Ennis und die Echos über die Furt begleiten |
| 4 | Entscheidung | Am anderen Ufer: Ennis' Frage beantworten, wohin die Echos sollen |

**Voraussetzung:** `Quest.MQ_A1_04 & Quest.SQ_023` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F04 +150 · ITM_CON_REPEL ×2; Hain-Dekor ITM_DECO_FERRYLANTERN
**Folge:** Rillwards nisten an der Furt; Ennis' Zelle hat einen sicheren Weg


---

## 4. Kharsgrat (R02) – SQ_025–SQ_046

Im Kharsgrat wiegt das Wort mehr als die Münze. Klanschwüre, Klanchronik, Ahnenfeuer – und eine Bergwelt, in der die Wildwacht vor allem rettet. Die Gratkin-Wanderung zieht sich als Kette über zwei Regionen; das Kontor ringt mit Klanehre; die Akademie misst Basalt, der zurückklingt.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_025 | Basalt, der zurückklingt | Fraktion | F01 · FQ_F01_01 | Akt I | 5 | 50 | – |
| SQ_026 | Das Tetri ohne Gewicht | Echo-Geschichte | – | Akt I | 3 | 25 | Time=Night |
| SQ_027 | Kharsk-Formen | Fraktion | F01 · FQ_F01_02 | Akt I | 3 | 35 | Time=Dusk |
| SQ_028 | Schneenacht am Grollhorn | Weltereignis | – | Akt I | 4 | 30 | Weather=Snow |
| SQ_029 | Käse und Klanschwur | Fraktion | F02 · FQ_F02_01 | Akt I | 5 | 50 | – |
| SQ_030 | Die Tür ohne Griff | Rätsel & Ruinen | – | Akt II | 4 | 35 | – |
| SQ_031 | Das Gewicht der Bücher | Fraktion | F02 · FQ_F02_02 | Akt I | 3 | 30 | Time=Night |
| SQ_032 | Die Linn-Quelle | Rätsel & Ruinen | – | Akt I | 3 | 30 | Weather=Rain |
| SQ_033 | Verschüttet | Fraktion | F02 · FQ_F02_02 | Akt I | 4 | 40 | – |
| SQ_034 | Ein Hammer für Hralda | Menschen | – | Akt I | 2 | 25 | – |
| SQ_035 | Die zweite Waage | Fraktion | F02 · FQ_F02_02 | Akt I | 4 | 35 | Time=Night |
| SQ_036 | Die Schuld der Lastzüge | Menschen | – | Akt III | 3 | 30 | – |
| SQ_037 | Pass der Gratkins | Fraktion | F03 · FQ_F03_02 | Akt I | 3 | 30 | Time=Day |
| SQ_038 | Kristalle, die nachts wachsen | Forschung | – | Akt I | 3 | 30 | Time=Night |
| SQ_039 | Lawinenhunde | Fraktion | F03 · FQ_F03_02 | Akt I | 4 | 35 | Weather=Snow |
| SQ_040 | Die Stimme unter Kharsholm | Forschung | – | Akt I | 3 | 30 | – |
| SQ_041 | Die Grenze hält | Fraktion | F03 · FQ_F03_02 | Akt I | 6 | 50 | Weather=Thunderstorm |
| SQ_042 | Die Probe der Ahnen | Wärterprüfung | – | Nachhall | 5 | 40 | – |
| SQ_043 | Das Horn im Nebel | Fraktion | F03 · FQ_F03_03 | Akt I | 4 | 35 | Weather=Fog |
| SQ_044 | Die Lawine von Brakkfels | Fraktion | F03 · FQ_F03_03 | Akt I | 5 | 40 | Weather=Snow |
| SQ_045 | Nacht der Ahnenfeuer | Fraktion | F03 · FQ_F03_03 | Akt I | 4 | 35 | Time=Day |
| SQ_046 | Über die Kettenbrücken | Fraktion | F04 · FQ_F04_01 | Akt I | 6 | 50 | Time=Night |

#### SQ_025 · Basalt, der zurückklingt

*Fraktion · Akademie der Resonanz · Kette **Die Außenstelle** (4/4) · Akt I · Auftrag: Messmeister Hakon (Akademie) (Kharsholm) · Intensität 5 · ~50 min*

Die Messreihen der Außenstelle enden in Kharsholm: Der Grollbasalt der Kettenbrücken klingt nach, wenn ein Echo darüber geht – stärker, seit Orh'gruun im Schlaf liegt. Hakon will den Basalt anbohren. Die Klans verbieten es. Der Wärter sucht eine Messung, die nichts zerstört.

**Lösungen:** Bohrung (Hakon gewinnt, Klans grollen) · Verbot (Gerd gewinnt) · Abhören ohne Bohrung (dritte Lösung, beide akzeptieren).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Hakon an den Kettenbrücken |
| 2 | Sprechen | Gerd in der Halle der Klans |
| 3 | Beobachten | Kraggoths auf den Brücken beobachten |
| 4 | Rätsel | Die Brücke mit Resonanzlatten „abhören“ |
| 5 | Entscheidung | Ergebnis an Hakon und Gerd übergeben |

**Voraussetzung:** `Quest.MQ_A1_07 & Quest.SQ_005`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F01 +400 · Resonator-Upgrade-Bauteil ITM_MAT_SOUNDRESIN ×3; Kodex-Fragment „Grollbasalt“
**Folge:** Akademie und Klans teilen sich die Messung; Brücken-Barks

#### SQ_026 · Das Tetri ohne Gewicht

*Echo-Geschichte · Akt I · Auftrag: Sigga (Brakkfels) (Brakkfels) · Intensität 3 · ~25 min*

Siggas junges Tetri schwebt plötzlich und kommt nicht mehr herunter. Die Dörfler sagen, es sei verflucht. Der Wärter erkennt eine Schwerkraft-Anomalie an den Ahnenfelsen, die das Tetri im Schlaf aufgeladen hat.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Sigga und ihr schwebendes Tetri |
| 2 | Beobachten | Das Tetri beobachten |
| 3 | Untersuchen | Die Anomalie an den schwebenden Ahnenfelsen finden |
| 4 | Begleiten | Sigga und das Tetri zur Gegenanomalie begleiten |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_EVO_GRAVITY; Kodex-Beobachtung Tetri
**Folge:** Sigga erklärt den Dörflern die Anomalie (Bark); Tetri landet

#### SQ_027 · Kharsk-Formen

*Fraktion · Akademie der Resonanz · Kette **Vaels Lücken** (1/4) · Akt I · Auftrag: Messmeister Hakon (Akademie) (Kharsholm) · Intensität 3 · ~35 min*

Vael beschrieb 812 die Lithi als reine Steinart. Hakon hat Lithshells mit Wasserklang gefunden – eine Regionalform, die Vael übersah. Der Wärter soll drei Belege fotografieren und eine Herde in der Dämmerung beobachten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Hakons Zweifel an Vael |
| 2 | Foto | Drei Lithshells im Grollschlund fotografieren |
| 3 | Beobachten | Eine Lithi-Herde in der Dämmerung beobachten |
| 4 | Liefern | Eine Schalenprobe abliefern (Fundstück, kein Verletzen) |

**Voraussetzung:** `Quest.MQ_A1_07 & Rank.F01>=2` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F01 +150 · ITM_KS_022; Kodex-Fragment „Vaels Lücken I“
**Folge:** Kodex-Eintrag Lithshell erhält „Regionalform (Kharsgrat)“

#### SQ_028 · Schneenacht am Grollhorn

*Weltereignis · Akt I · Auftrag: Bergführerin Branda (Grollhorn-Biwak) · Intensität 4 · ~30 min*

Bei Schneefall ziehen Rimpaws auf das Grollhorn, um auf dem Gipfel im Schnee zu singen – eine Wanderung, die kein Mensch je ganz gesehen hat. Branda will sie sehen, bevor ihre Knie nicht mehr mitmachen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Schneefall am Grollhorn abwarten |
| 2 | Begleiten | Branda zum Gipfel begleiten |
| 3 | Beobachten | Den Rimpaw-Gesang beobachten |
| 4 | Foto | Ein Foto für Branda (≥ 4 Sterne) |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_CON_WARM ×3; Hain-Dekor ITM_DECO_SUMMITFLAG
**Folge:** Brandas Foto hängt im Biwak; Rimpaw-Gesang als Wetterzeichen in Barks

#### SQ_029 · Käse und Klanschwur

*Fraktion · Goldklang-Kontor · Kette **Lindenhonig** (4/4) · Akt I · Auftrag: Tova (Erzkontor) (Kharsholm) · Intensität 5 · ~50 min*

Das Ende des Honigwegs: Tova soll den Bergkäse liefern, aber der Klan der Hralls verweigert das Geschäft mit dem Kontor – ein alter Klanschwur. Der Wärter findet heraus, dass der Schwur nicht gegen das Kontor gerichtet ist, sondern gegen einen Mann, der vor Jahren Hralls betrogen hat: den Konsortiums-Händler aus SQ_011.

**Lösungen:** Ossians Vertrag vorlegen (Kontor-Weg) · den betrügerischen Händler zum Klan bringen (nur wenn in SQ_011 mit ihm gesprochen) · dem Klan einen eigenen Schwur anbieten (dritte Lösung, Klan-Bark).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tova erklärt das Problem |
| 2 | Gehen | Nach Hrallsted |
| 3 | Untersuchen | Die Klanchronik am Ahnenfelsen lesen |
| 4 | Entscheidung | Den Klan um ein neues Wort bitten |
| 5 | Liefern | Den ersten Käse nach Eichenhall bringen |

**Voraussetzung:** `Quest.MQ_A1_05 & Quest.SQ_011`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F02 +400 · ITM_FOOD_ALPINECHEESE ×5; Rezept RCP_043
**Folge:** Handelsweg Eichenhall–Kharsholm offen (Händler-Sortimente +2 Waren)

#### SQ_030 · Die Tür ohne Griff

*Rätsel & Ruinen · Akt II · Auftrag: Ahnenstein-Tutorin Yrsa (Kharsholm) · Intensität 4 · ~35 min*

Nach W4 kennt der Wärter Wendelins Wort von den „Türen, die nur von außen aufgehen“. Yrsa zeigt ihm eine Tür im Erzgrat, die die Klans seit Jahrhunderten bewachen. Mit dem Akkord von Kharsholm öffnet sie sich – dahinter liegt kein Schatz, sondern ein Raum zum Zuhören.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Yrsa am Ahnenstein |
| 2 | Gehen | Zur Tür im Erzgrat |
| 3 | Rätsel | Den Akkord an der Tür anschlagen |
| 4 | Untersuchen | Den Raum dahinter untersuchen |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Wendelin-Tagebuch (Sammelseite); ITM_LURE_TUNINGFORK
**Folge:** Hörraum im Erzgrat (Rückkehrort, Resonanzsinn +10 m dort)

#### SQ_031 · Das Gewicht der Bücher

*Fraktion · Goldklang-Kontor · Kette **Erz und Ehre** (1/4) · Akt I · Auftrag: Tova (Erzkontor) (Kharsholm) · Intensität 3 · ~30 min*

Im Erzkontor stimmen die Erzmengen nicht. Tova fürchtet, ein Vorarbeiter zweige ab. Der Wärter findet heraus, dass die Waage falsch wiegt – ein Ponderath hat sich darunter eingenistet und macht alles schwerer.

**Lösungen:** Umsiedeln · binden · die Waage verlegen und das Ponderath als Kontor-Maskottchen behalten (Tova lacht).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tova und die Bücher |
| 2 | Untersuchen | Waage, Lager und Bücher prüfen |
| 3 | Beobachten | Das Ponderath unter der Waage beobachten |
| 4 | Entscheidung | Was wird aus dem Ponderath? |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=2` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F02 +150 · ITM_HELD_ROOTCHARM; Kodex-Beobachtung Ponderath
**Folge:** Vorarbeiter entlastet (Bark); Ponderath als „Kontorgewicht“ oder im Grollschlund

#### SQ_032 · Die Linn-Quelle

*Rätsel & Ruinen · Akt I · Auftrag: Bergführerin Branda (Grollhorn-Biwak) · Intensität 3 · ~30 min*

Die Linn entspringt im Kharsgrat und fließt bis Lindwiesen. Seit Wochen ist ihr Wasser trüb. Branda vermutet einen Erdrutsch. Der Wärter findet eine Höhle, in der Rivetkins Metall aus dem Fels lösen – und eine alte Glyphe, die vor genau diesem Ort warnt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Linn-Quelle |
| 2 | Untersuchen | Den Ursprung der Trübung finden |
| 3 | Beobachten | Die Rivetkins in der Höhle beobachten |
| 4 | Rätsel | Die Warnglyphe deuten |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Weather=Rain`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_MAT_KHARSIRON ×3; Klangfragment (TruthLevel 0)
**Folge:** Linn klärt sich nach 2 Spieltagen; Mühlbach in Lindwiesen sichtbar klarer

#### SQ_033 · Verschüttet

*Fraktion · Goldklang-Kontor · Kette **Erz und Ehre** (2/4) · Akt I · Auftrag: Tova (Erzkontor) (Kharsholm) · Intensität 4 · ~40 min*

Ein Stollen der Erzgrat-Minen ist eingestürzt; drei Bergleute und ihre Ferrows sitzen fest. Der Klan will graben, das Kontor will die Kosten nicht tragen. Der Wärter rettet zuerst – und verhandelt danach.

**Lösungen:** Kontor zahlt (Tova setzt es durch) · Klan zahlt (Ehre) · beide teilen und die Ferrows erhalten Ruhetage (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Erzgrat-Hütte |
| 2 | Untersuchen | Den Stollen mit Resonanzsinn abhören |
| 3 | Traversal | Über den Lüftungsschacht hinab |
| 4 | Begleiten | Ulf Brakk und die Eingeschlossenen hinausführen |
| 5 | Entscheidung | Wer zahlt die Stützbalken? |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=2 & Quest.SQ_031`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F02 +150 · ITM_GEAR_TOOL_2; ITM_CON_STAMINA ×3
**Folge:** Stollen mit neuen Balken (Data Layer); Bergleute-Barks

#### SQ_034 · Ein Hammer für Hralda

*Menschen · Akt I · Auftrag: Grollschmied Hraldur (Kharsholm) · Intensität 2 · ~25 min*

Der Grollschmied hat für Hralda Brakk – seine Cousine – einen Hammer geschmiedet, den sie nie abgeholt hat. „Sie trägt keine Waffen mehr, seit Eichenhall.“ Er bittet den Wärter, ihr den Hammer zu bringen und zu fragen, warum.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Der Grollschmied |
| 2 | Liefern | Den Hammer zu Hralda bringen |
| 3 | Entscheidung | Hralda fragen – oder nicht |

**Voraussetzung:** `–`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Kodex-Fragment „Hraldas Hammer“; Hain-Dekor ITM_DECO_ANVIL
**Folge:** Hralda hängt den Hammer in die Wildwacht-Kammer; Gespräch im Lager von K45 MQ_A2_08 erhält eine Zeile

#### SQ_035 · Die zweite Waage

*Fraktion · Goldklang-Kontor · Kette **Erz und Ehre** (3/4) · Akt I · Auftrag: Tova (Erzkontor) (Kharsholm) · Intensität 4 · ~35 min*

Tova hat einen Vertrag mit Saltrand in Aussicht: Kharsk-Eisen für Schiffsbeschläge. Doch der Klanrat verlangt, dass das Eisen gesungen, nicht nur gewogen wird – ein altes Ritual, bei dem ein Echo das Metall prüft. Ein Forgoth soll singen, aber er singt nicht für Fremde.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Der Klanrat stellt die Bedingung |
| 2 | Beobachten | Den Forgoth bei der Arbeit beobachten |
| 3 | Entscheidung | Den Forgoth um den Gesang bitten |
| 4 | Kampf | Probe gegen den Klanprüfer (Metall-Regel) |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=2 & Quest.SQ_033` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F02 +150 · ITM_HELD_TONE_METAL; Rezept RCP_051
**Folge:** Vertrag geschlossen; Kharsk-Eisen in Saltrand-Händlern (K50)

#### SQ_036 · Die Schuld der Lastzüge

*Menschen · Akt III · Auftrag: Gerd (Halle der Klans) (Kharsholm) · Intensität 3 · ~30 min*

Nach Akt III will Gerd die Klanchronik um die Wahrheit über die Siegelkriege ergänzen – auch um die Rolle der Kharsk-Klans, die Echos als Lastträger in den Krieg schickten. Der Wärter sammelt Erinnerungen der Ältesten und eines alten Cragar, der dabei war.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Gerds Vorhaben |
| 2 | Sprechen | Die Älteste Ingrid |
| 3 | Beobachten | Den alten Cragar mit den Kriegsnarben beobachten |
| 4 | Entscheidung | Was in die Chronik kommt |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Lore „Klanchronik, Siegelkriege“; ITM_LURE_BELLCHIME
**Folge:** Neue Tafel in der Halle der Klans; Barks über „die schweren Jahre“

#### SQ_037 · Pass der Gratkins

*Fraktion · Wildwacht · Kette **Grenzgänger** (2/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Passwacht Nord) · Intensität 3 · ~30 min*

Die Gratkin-Wanderung erreicht den Nordpass – und stockt. Ein Kraggoth hat sich auf die enge Stelle gelegt und lässt niemanden vorbei. Jorn will den Pass sprengen. Der Wärter findet heraus, was der Kraggoth bewacht.

**Lösungen:** Kampf (Kraggoth erschöpft, weicht) · Sprengung verhindern und Ausweichpfad bauen · Kraggoth' Gelege mit Brokkar-Hilfe umbetten (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Jorn und der blockierte Pass |
| 2 | Beobachten | Den Kraggoth beobachten |
| 3 | Untersuchen | Die Felsspalte hinter ihm untersuchen |
| 4 | Entscheidung | Einen Weg für Gratkins und Kraggoth finden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=2 & Quest.SQ_021` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F03 +150 · ITM_TRAP_NET; Kodex-Beobachtung Kraggoth (Wächter)
**Folge:** Gratkins passieren; Kraggoth bleibt als Passwächter (Bark)

#### SQ_038 · Kristalle, die nachts wachsen

*Forschung · Akt I · Auftrag: Akademie-Lehrling Mikkel (Erzgrat-Hütte) · Intensität 3 · ~30 min*

Mikkel behauptet, dass Quarlings nachts Kristalle wachsen lassen, indem sie singen. Niemand glaubt einem Lehrling. Der Wärter beobachtet drei Nächte lang – und findet etwas Seltsameres: Die Kristalle wachsen nur, wenn ein Resonix in der Nähe antwortet.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Mikkels Theorie |
| 2 | Beobachten | Quarlings nachts beobachten |
| 3 | Beobachten | Das antwortende Resonix finden |
| 4 | Foto | Einen Quarcoil im Kristallgesang fotografieren |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_KS_028; ITM_MAT_QUARTZSHARD ×5
**Folge:** Mikkels Aufsatz in der Akademie (Bark „der Lehrling hatte recht“)

#### SQ_039 · Lawinenhunde

*Fraktion · Wildwacht · Kette **Grenzgänger** (3/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Passwacht Nord) · Intensität 4 · ~35 min*

Die Wildwacht will Rimlets zu Lawinensuchern ausbilden – sie spüren Wärme unter Schnee. Jorn bittet den Wärter, drei Rimlets zu gewinnen, die das freiwillig tun. Am Ende steht eine echte Suche.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Rimlets beim Spiel im Schnee beobachten |
| 2 | Binden | Ein Rimlet binden (oder einen Rimlet-Begleiter aus dem Chor einsetzen) |
| 3 | Bedingung | Auf Schnee warten |
| 4 | Untersuchen | Mit den Rimlets drei Verschüttete (Übungspuppen) finden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=2 & Quest.SQ_037` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F03 +150 · ITM_SEAL_TUNED ×2; Wildwacht-Abzeichen (Kosmetik)
**Folge:** Rimlet-Staffel an der Passwacht (sichtbar); Bark „unsere Schneenasen“

#### SQ_040 · Die Stimme unter Kharsholm

*Forschung · Akt I · Auftrag: Ahnenstein-Tutorin Yrsa (Kharsholm) · Intensität 3 · ~30 min*

Yrsa hört seit dem Akkord ein Brummen unter der Stadt. Sie fragt, ob Orh'gruun träumt. Der Wärter lauscht an drei Ahnenfelsen und zeichnet den Rhythmus auf – er stimmt mit den Gezeiten der schwebenden Felsen überein.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Yrsas Frage |
| 2 | Untersuchen | An drei Ahnenfelsen lauschen |
| 3 | Beobachten | Ein Anchrex bei den schwebenden Felsen beobachten |
| 4 | Sprechen | Yrsa vom Rhythmus erzählen |

**Voraussetzung:** `Quest.MQ_A1_03`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Kodex-Eintrag Orh'gruun (Seite 1); ITM_LURE_BELLCHIME
**Folge:** Yrsa singt den Rhythmus in der Halle (Bark, Musik-Variante)

#### SQ_041 · Die Grenze hält

*Fraktion · Wildwacht · Kette **Grenzgänger** (4/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Passwacht Nord) · Intensität 6 · ~50 min*

Die Wanderung ist fast am Ziel, als ein Unwetter die Gratkins am Grollhorn überrascht. Gleichzeitig wartet am Pass ein Händler mit Netzen, der weiß, dass verängstigte Gratkins leicht zu fangen sind. Der Wärter muss die Herde durch den Sturm führen und den Fänger aufhalten – ohne Gewalt gegen Menschen.

**Lösungen:** Rask übergeben (Gesetz) · laufen lassen (Gnade) · Rask als Netzflicker für die Wildwacht anwerben (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Das Unwetter bricht los |
| 2 | Begleiten | Mit Jorn die Herde zum Pass treiben |
| 3 | Kampf | Die Echos des Fängers erschöpfen |
| 4 | Entscheidung | Was mit Rask geschieht |
| 5 | Beobachten | Die Gratrex-Leitkuh in den Auen beobachten |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=2 & Quest.SQ_039` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F03 +400 · ITM_GEAR_CLOAK_2; Hain-Dekor ITM_DECO_GRATKINBANNER
**Folge:** Gratkin-Wanderung jährlich (Weltereignis WE_GRATKIN_MIGRATION); Rask arbeitet für die Wildwacht oder ist verbannt

#### SQ_042 · Die Probe der Ahnen

*Wärterprüfung · Nachhall · Auftrag: Torvik Hrall (Kharsholm) · Intensität 5 · ~40 min*

Im Nachhall lädt Torvik zur Ahnenprobe: drei Kämpfe auf den Kettenbrücken bei Wind, jede Brücke mit verschobenen Plattformen. Nur wer seinen Chor kennt, besteht – Torvik will sehen, ob der Wärter ohne seine alte Gabe (oder mit ihr) noch zuhört.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Torviks Einladung |
| 2 | Kampf | Erste Brücke |
| 3 | Kampf | Zweite Brücke |
| 4 | Kampf | Dritte Brücke gegen Torvik |
| 5 | Entscheidung | Torvik antworten, was sich verändert hat |

**Voraussetzung:** `Act>=Nachhall`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_GRAVITY; Titel „Brückengänger“
**Folge:** Torvik-Barks im Nachhall je Ende

#### SQ_043 · Das Horn im Nebel

*Fraktion · Wildwacht · Kette **Pässe im Schnee** (1/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Passwacht Nord) · Intensität 4 · ~35 min*

Ein Wanderer ist im Nebel am Grollschlund verschwunden. Die Wildwacht hat ein altes Rettungshorn, aber niemand weiß mehr, wie man es bläst – es muss auf einen Ton gestimmt sein, den Gratwyns hören. Der Wärter stimmt das Horn und sucht.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Nebel am Grollschlund |
| 2 | Rätsel | Das Horn auf den Gratwyn-Ton stimmen |
| 3 | Beobachten | Den Gratwyns zum Verirrten folgen |
| 4 | Begleiten | Den Wanderer zurückbringen |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=3` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F03 +150 · ITM_LURE_WHISTLE; ITM_CON_HEAL_ALL
**Folge:** Rettungshorn hängt wieder an der Passwacht (spielbar bei Nebel)

#### SQ_044 · Die Lawine von Brakkfels

*Fraktion · Wildwacht · Kette **Pässe im Schnee** (2/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Passwacht Nord) · Intensität 5 · ~40 min*

In Akt II fällt eine Lawine auf die Straße nach Brakkfels; ein Fuhrwerk und zwei Cragars liegen darunter. Die Rimlet-Staffel aus SQ_039 kommt zum ersten echten Einsatz – oder der Wärter sucht mit dem Resonanzsinn allein.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Lawine |
| 2 | Untersuchen | Verschüttete mit Rimlets oder Resonanzsinn finden |
| 3 | Traversal | Einen Gang zum Fuhrwerk graben (Grabreiten, falls vorhanden; sonst Werkzeug) |
| 4 | Begleiten | Die Kutscherin nach Brakkfels bringen |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=3 & Quest.SQ_043 & Act>=Akt II` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F03 +150 · ITM_GEAR_BOOTS_2; ITM_CON_WARM ×3
**Folge:** Neue Lawinengalerie an der Straße (Data Layer)

#### SQ_045 · Nacht der Ahnenfeuer

*Fraktion · Wildwacht · Kette **Pässe im Schnee** (3/4) · Akt I · Auftrag: Gerd (Halle der Klans) (Kharsholm) · Intensität 4 · ~35 min*

Einmal im Jahr entzünden die Klans Feuer auf allen Ahnenfelsen. Dieses Jahr fehlt der Klan von Hrallsted, weil sein Feuerträger krank ist. Gerd bittet den Wärter, das Feuer mit einem Emblit über den Erzgrat zu tragen – Emblits tragen Glut nur bei Mittagssonne.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Gerd bittet um Hilfe |
| 2 | Beobachten | Ein Emblit zur Mittagszeit finden |
| 3 | Begleiten | Mit dem Emblit das Feuer nach Hrallsted tragen |
| 4 | Entscheidung | Das Feuer mit dem Klanspruch entzünden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=3 & Quest.SQ_044` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F03 +150 · ITM_EVO_EMBER; Hain-Dekor ITM_DECO_ANCESTORFIRE
**Folge:** Ahnenfeuer-Nacht als jährliches Weltereignis; Hrallsted-Klan dankt (Bark)

#### SQ_046 · Über die Kettenbrücken

*Fraktion · Freie Stimmen · Kette **Die Kurierin** (4/4) · Akt I · Auftrag: Ennis Rook (Kurierin) (Kharsholm) · Intensität 6 · ~50 min*

Ennis' letzte Fahrt in dieser Kette: zwölf befreite Echos, darunter das Brokkar aus Moosgrund, sollen über die Kettenbrücken in ein verborgenes Tal. Die Kontor-Wache am Erzkontor zählt jeden Wagen. Der Wärter muss wählen, wem er vertraut: Tova, den Klans oder der Nacht.

**Lösungen:** Tova bitten (sie schaut weg – Kontor-Bark) · Klanrat bitten (Gerd gewährt Durchgang) · nachts ohne Hilfe (Hinterhalt schwerer).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ennis' Plan |
| 2 | Entscheidung | Weg wählen: Kontor, Klan oder Nacht |
| 3 | Begleiten | Über die Kettenbrücken |
| 4 | Flucht | Angekündigter Hinterhalt eines Fängers – durch den Grollschlund ausweichen |
| 5 | Beobachten | Das Brokkar im neuen Tal beobachten |

**Voraussetzung:** `Quest.MQ_A1_04 & Quest.SQ_024` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F04 +400 · ITM_HELD_SWIFTFEATHER; Zellen-Schnellreisepunkt Grollschlund (K47 F04 Rang 3)
**Folge:** Verborgenes Tal der Freien Stimmen (Rückkehrort mit freien Echos)


---

## 5. Morvenmoor (R03) – SQ_047–SQ_067

Das Moor ist nachts am lebendigsten. Hier sitzt die Unterstadt der Freien Stimmen, hier bezahlt man mit Liedern, hier liegen die verlassenen Kapellen des Ordens, die sich in Akt III wieder öffnen. Viele Quests sind an Nebel, Regen oder Nacht gebunden; das Moor steigt bei Regen, und mit ihm ändern sich die Wege.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_047 | Moorformen | Fraktion | F01 · FQ_F01_02 | Akt I | 3 | 35 | Weather=Fog |
| SQ_048 | Der Humbog-Chor | Echo-Geschichte | – | Akt I | 2 | 25 | Time=Night |
| SQ_049 | Irrlichtjagd | Fraktion | F01 · FQ_F01_02 | Akt I | 4 | 35 | Time=Night |
| SQ_050 | Wenn das Moor steigt | Weltereignis | – | Akt I | 4 | 30 | Weather=Rain |
| SQ_051 | Eine Nacht im Moor | Fraktion | F03 · FQ_F03_03 | Akt I | 6 | 55 | Time=Night & Weather=Fog |
| SQ_052 | Der Stein mit zwei Seiten | Rätsel & Ruinen | – | Akt II | 4 | 35 | – |
| SQ_053 | Graue Ränder | Fraktion | F03 · FQ_F03_04 | Akt I | 4 | 40 | Weather=Rain |
| SQ_054 | Das Turmgeheimnis der Fährmeisterin | Rätsel & Ruinen | – | Akt I | 3 | 30 | – |
| SQ_055 | Schulden in der Unterstadt | Fraktion | F04 · FQ_F04_02 | Akt I | 3 | 30 | Time=Night |
| SQ_056 | Fennhavens Brücke | Menschen | – | Akt I | 2 | 25 | – |
| SQ_057 | Die Liederschuld | Fraktion | F04 · FQ_F04_02 | Akt I | 4 | 35 | Time=Night |
| SQ_058 | Die Ouroveth-Legende | Forschung | – | Akt III | 3 | 30 | – |
| SQ_059 | Ein Verrat, der keiner war | Fraktion | F04 · FQ_F04_02 | Akt I | 5 | 45 | Time=Night |
| SQ_060 | Torf und Glut | Forschung | – | Akt I | 3 | 30 | – |
| SQ_061 | Lieder für Tavesh | Fraktion | F04 · FQ_F04_02 | Akt I | 6 | 50 | Time=Night |
| SQ_062 | Die Probe im Nebel | Wärterprüfung | – | Akt I | 5 | 30 | Weather=Fog |
| SQ_063 | Das erste Netz | Fraktion | F04 · FQ_F04_03 | Akt I | 4 | 35 | – |
| SQ_064 | Der Moorkönig | Wärterprüfung | – | Nachhall | 6 | 40 | Time=Night |
| SQ_065 | Perlen aus Saltrand | Fraktion | F04 · FQ_F04_03 | Akt I | 4 | 40 | – |
| SQ_066 | Die Kapelle öffnet sich | Fraktion | F05 · FQ_F05_01 | Akt III | 3 | 30 | – |
| SQ_067 | Was Stille heilt | Fraktion | F05 · FQ_F05_01 | Akt III | 4 | 40 | Time=Dusk |

#### SQ_047 · Moorformen

*Fraktion · Akademie der Resonanz · Kette **Vaels Lücken** (2/4) · Akt I · Auftrag: Gelehrte Oona (Akademie) (Morvenfurt) · Intensität 3 · ~35 min*

Oona setzt Vaels Lücken im Moor fort: Mirels in Duvreth tragen ein Klangmal, das Vael nur aus Saltrand kannte. Sie braucht Fotos bei Nebel – nur dann leuchten die Male – und Beobachtungen, ob sich die Mirels mit Brinlets paaren.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Oona in der Laternengasse |
| 2 | Bedingung | Nebel in Duvreth |
| 3 | Foto | Zwei Mirels mit leuchtendem Klangmal fotografieren |
| 4 | Beobachten | Brinlets im Ried beobachten (Paarungsverhalten) |

**Voraussetzung:** `Quest.MQ_A1_07 & Rank.F01>=2 & Quest.SQ_027` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F01 +150 · ITM_KS_031; Kodex-Fragment „Vaels Lücken II“
**Folge:** Kodex Mirel: „Regionalform Morvenmoor“

#### SQ_048 · Der Humbog-Chor

*Echo-Geschichte · Akt I · Auftrag: Nialla (Laternensteg) (Morvenfurt) · Intensität 2 · ~25 min*

Der Nachtmarkt von Morvenfurt beginnt traditionell mit dem ersten Humbog-Ruf. Seit Wochen ruft keiner. Die Händler warten, die Laternen bleiben dunkel. Nialla bittet den Wärter, die Humbogs zu finden – sie sind in eine neue Senke gezogen, weil der alte Teich verlandet.

**Lösungen:** Teich ausbaggern (Kontor zahlt) · Markt an die Senke verlegen (neuer Markt-Ort) · Humbog-Rufe mit einem Ruf-Horn ersetzen (Nialla lehnt traurig ab – dritte Lösung nur als Gesprächsoption).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Nialla am dunklen Laternensteg |
| 2 | Untersuchen | Den alten Teich untersuchen |
| 3 | Beobachten | Die Humbogs in der Senke beobachten |
| 4 | Entscheidung | Markt verlegen oder Teich ausbaggern? |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · ITM_LURE_LANTERN; Hain-Dekor ITM_DECO_MARKETLANTERN
**Folge:** Nachtmarkt öffnet wieder; Händlerangebot nachts +2 Waren

#### SQ_049 · Irrlichtjagd

*Fraktion · Akademie der Resonanz · Kette **Vaels Lücken** (3/4) · Akt I · Auftrag: Gelehrte Oona (Akademie) (Morvenfurt) · Intensität 4 · ~35 min*

Seit Generationen jagen Moorleute bei Nacht dem „Irrel-Weißling“ hinterher – einer Form, die Vael nie bestätigte. Oona will die Jagd beenden, mit einer Antwort. Der Wärter findet heraus, dass das „Weißling“ ein Irrel ist, das sich in einem Kalkbecken weiß gefärbt hat – oder doch nicht?

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | In den Nebelwald Corrach |
| 2 | Beobachten | Irrels bei Nacht beobachten |
| 3 | Untersuchen | Das Kalkbecken untersuchen |
| 4 | Entscheidung | Oona das Ergebnis vortragen |

**Voraussetzung:** `Quest.MQ_A1_07 & Rank.F01>=2 & Quest.SQ_047` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F01 +150 · ITM_EVO_MISTVEIL; Kodex-Fragment „Vaels Lücken III“
**Folge:** Kodex-Anmerkung „Weißling = Kalkfärbung“ (oder offene Frage, je Antwort)

#### SQ_050 · Wenn das Moor steigt

*Weltereignis · Akt I · Auftrag: Bootsbauer Finn (Morvenfurt) · Intensität 4 · ~30 min*

Bei Regen steigt das Morvenmoor um fast einen halben Meter. Dann treiben Undlinge aus ihren Senken in die Kanäle der Stadt und verirren sich. Finn baut Boote; er braucht jemanden, der die Undlinge zurückführt, bevor die Fischer sie für Schädlinge halten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Regen über Morvenfurt |
| 2 | Beobachten | Verirrte Undlinge in den Kanälen finden |
| 3 | Traversal | Mit einem Schwimm-Echo durch die Kanäle |
| 4 | Begleiten | Die Undlinge mit Finns Boot zur Senke leiten |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Weather=Rain`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_GEAR_MASK_2; ITM_FOOD_SMOKEDFISH ×3
**Folge:** Kanal-Sperrgitter mit Durchlass (Data Layer); Fischer-Barks über „Finns Undlinge“

#### SQ_051 · Eine Nacht im Moor

*Fraktion · Wildwacht · Kette **Pässe im Schnee** (4/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Riedwacht) · Intensität 6 · ~55 min*

Jorn hat einen Auftrag angenommen, den er bereut: Ein Kind aus Fennhaven ist ins Moor gelaufen, einem Irraune nach. Die Bergretter sind fremd im Moor. Der Wärter führt die Suche durch eine Nebelnacht – und findet das Kind bei einem Echo, das es beschützt hat.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Jorn an der Riedwacht |
| 2 | Bedingung | Nacht über dem Ried |
| 3 | Untersuchen | Spuren im Nebel verfolgen |
| 4 | Beobachten | Das Irraune beobachten, das das Kind wärmt |
| 5 | Begleiten | Tamsin nach Fennhaven bringen |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=3 & Quest.SQ_045` · **Variante/Bedingung:** `Time=Night & Weather=Fog`
**Belohnung:** 800 ◎ · 2.000 Wärter-EP · Ruf F03 +400 · ITM_GEAR_LANTERN_2; Titel „Moorläufer“
**Folge:** Tamsin und das Irraune besuchen sich (Bark); Riedwacht erhält Nebelglocken

#### SQ_052 · Der Stein mit zwei Seiten

*Rätsel & Ruinen · Akt II · Auftrag: Moorweise Corrach (Morvenfurt) · Intensität 4 · ~35 min*

Nach W6 bringt Corrach dem Wärter einen Stillstein, den ihr Sohn im Moor gefunden hat. Auf der Rückseite: eine Akademie-Prägung. Corrach will wissen, wie lange das schon so geht. Die Spur führt zu einer verlassenen Ordenskapelle bei Duvreth.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Corrach zeigt den Stein |
| 2 | Gehen | Zur Kapelle bei Duvreth |
| 3 | Untersuchen | Lieferlisten in der Kapelle finden |
| 4 | Entscheidung | Corrach die Wahrheit erzählen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A2_07`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Lore „Lieferlisten 991–1003“ (TruthLevel 6); ITM_EMAT_STILLSHARD
**Folge:** Corrach warnt die Moorleute vor Ordenssteinen (Barks)

#### SQ_053 · Graue Ränder

*Fraktion · Wildwacht · Kette **Die stillen Ränder** (1/4) · Akt I · Auftrag: Passwart Jorn (Wildwacht) (Riedwacht) · Intensität 4 · ~40 min*

Rang 4 der Wildwacht: Jorn wird an die Riedwacht versetzt, um die Nachwirkungen der geheilten Zone zu beobachten. Am Rand wachsen Pflanzen grau nach, und Blossis meiden die Stelle. Der Wärter findet einen vergessenen Stillstein-Splitter im Schlamm.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Versunkenen Senke |
| 2 | Beobachten | Das Ausweichverhalten der Blossis beobachten |
| 3 | Heilen | Zwei graue Nachwirkungs-Kreise heilen |
| 4 | Untersuchen | Den Splitter im Schlamm finden |

**Voraussetzung:** `Quest.MQ_P03 & Rank.F03>=4` · **Variante/Bedingung:** `Weather=Rain`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F03 +150 · ITM_EMAT_STILLSHARD; ITM_GEAR_RESONATOR_2
**Folge:** Graue Ränder verschwinden; Blossis kehren zurück

#### SQ_054 · Das Turmgeheimnis der Fährmeisterin

*Rätsel & Ruinen · Akt I · Auftrag: Fährmeisterin Ailsa Duvreth (Morvenfurt) · Intensität 3 · ~30 min*

Bei Ebbe im Morve-Delta hört man eine Glocke unter Wasser – Ailsas Großvater, auch er Fährmeister, nannte sie „die Glocke des versunkenen Turms“. Seit MQ_A1_08 läutet sie öfter. Der Wärter taucht und findet eine Glocke mit dorunischen Zeichen, aber nicht vom Turm.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ailsa an der Fähre |
| 2 | Traversal | Zum Delta schwimmen |
| 3 | Untersuchen | Die Glocke und ihre Inschrift untersuchen |
| 4 | Rätsel | Den Glockenton mit dem Resonator spiegeln |

**Voraussetzung:** `Quest.MQ_A1_08`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_LURE_BELLCHIME; Klangfragment (TruthLevel 3)
**Folge:** Die Glocke läutet bei Ebbe hörbar über die Stadt (Ambient)

#### SQ_055 · Schulden in der Unterstadt

*Fraktion · Freie Stimmen · Kette **Unterstadt** (1/4) · Akt I · Auftrag: Der Schatten (Morvenfurt) · Intensität 3 · ~30 min*

Der Schatten – Rüstmeister der Freien Stimmen – hat ein Problem: Ein Mitglied schuldet einem Hehler Geld und hat dafür sein Echo verpfändet. Die Freien Stimmen kaufen keine Echos frei, aus Prinzip. Der Wärter soll eine andere Lösung finden.

**Lösungen:** Schuld bezahlen (Prinzip gebrochen, Schatten seufzt) · Hehler beim Stadtrat melden (Echo kommt frei, Roan verliert Ansehen) · Roans Schuld durch Arbeit für Finn tilgen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Der Schatten im Hinterzimmer |
| 2 | Sprechen | Roan erzählen lassen |
| 3 | Untersuchen | Den Hehler und sein Lager finden |
| 4 | Entscheidung | Lösung wählen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=2` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · Ruf F04 +150 · ITM_CON_SENSE ×2; Zugang Schwarzmarkt (Vorbereitung)
**Folge:** Roan hat sein Echo zurück; Hehler-Barks

#### SQ_056 · Fennhavens Brücke

*Menschen · Akt I · Auftrag: Brückenwart Elwyn (Fennhaven) · Intensität 2 · ~25 min*

Die Stelzenbrücke von Fennhaven fault. Neue Pfähle aus Moorweide würden halten, aber Weiduna wohnen in den Weiden und verlassen sie nicht, solange dort gesungen wird – und die Dorfkinder singen immer dort.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Elwyns Brücke |
| 2 | Beobachten | Die Weiduna in den Weiden beobachten |
| 3 | Sammeln | Weidenholz aus verlassenen Weiden sammeln |
| 4 | Entscheidung | Die Kinder an einen neuen Singplatz führen |

**Voraussetzung:** `–`
**Belohnung:** 450 ◎ · 1.300 Wärter-EP · Rezept RCP_052; ITM_MAT_MOORWILLOW ×4
**Folge:** Neue Brücke (Data Layer); Kinderchor an neuem Ort (Ambient)

#### SQ_057 · Die Liederschuld

*Fraktion · Freie Stimmen · Kette **Unterstadt** (2/4) · Akt I · Auftrag: Der Schatten (Morvenfurt) · Intensität 4 · ~35 min*

In der Unterstadt bezahlt man mit Liedern: Wer einen Gefallen erhält, singt dafür. Ein Lied wurde gestohlen – ein Händler aus der Oberstadt verkauft es als eigenes. Die Unterstadt will es zurück, ohne aufzufallen.

**Lösungen:** Beweis öffentlich machen · Händler unter vier Augen stellen · dem Händler anbieten, das Lied gemeinsam zu singen (dritte Lösung, er wird Gast der Unterstadt).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Das gestohlene Lied |
| 2 | Untersuchen | Den Händler in der Oberstadt beobachten |
| 3 | Beobachten | Den Humbog hören, der das Lied „bezeugt“ |
| 4 | Entscheidung | Das Lied zurückholen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=2 & Quest.SQ_055` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F04 +150 · ITM_KS_035; Hain-Dekor ITM_DECO_SONGSHEET
**Folge:** Lied wird in der Unterstadt gesungen (Musik-Variante)

#### SQ_058 · Die Ouroveth-Legende

*Forschung · Akt III · Auftrag: Moorweise Corrach (Morvenfurt) · Intensität 3 · ~30 min*

In Akt III erzählt Corrach von Ouroveth, dem Mythischen, das „im Kreis der Generationen“ lebt. Wer züchtet, sagt sie, hört es irgendwann. Der Wärter sammelt drei Moorlieder über Ouroveth – der erste Schritt zu einer Spur, die erst die Zucht-Meisterschaft vollendet (K62).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Corrachs Erzählung |
| 2 | Untersuchen | Drei Moorlieder bei Ältesten in Duvreth hören |
| 3 | Beobachten | Ein Blossmire beim Laichen beobachten |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Ouroveth (Gerücht); ITM_BREED_KEIMWAERME
**Folge:** Spur „Ouroveth“ im Kodex aktiv (K62)

#### SQ_059 · Ein Verrat, der keiner war

*Fraktion · Freie Stimmen · Kette **Unterstadt** (3/4) · Akt I · Auftrag: Der Schatten (Morvenfurt) · Intensität 5 · ~45 min*

Eine Razzia der Stadtwache trifft ein Versteck der Unterstadt. Alle glauben, Roan habe sie verraten. Der Wärter findet heraus, dass ein Irrlit die Wachen zum Versteck geführt hat – angelockt von den Laternen, die die Freien Stimmen selbst aufgehängt hatten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Unterstadt ist in Aufruhr |
| 2 | Untersuchen | Das geräumte Versteck untersuchen |
| 3 | Beobachten | Irrlits und Laternen beobachten |
| 4 | Entscheidung | Vor der Versammlung sprechen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=2 & Quest.SQ_057` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 700 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_GEAR_LANTERN_2; ITM_TRAP_SHADE
**Folge:** Roan bleibt in der Unterstadt; Laternen werden abgedunkelt (Ambient)

#### SQ_060 · Torf und Glut

*Forschung · Akt I · Auftrag: Torfstecher Bran (Duvreth) · Intensität 3 · ~30 min*

Bran sticht Torf in Duvreth. Ein Torfgor hat sich dort eingegraben, und wo es schläft, glüht der Torf – Cindrel-Eier, eingeschleppt von Händlern aus Verdanthain. Ein Moorbrand droht.

**Lösungen:** Eier nach Verdanthain zurückbringen (Wildwacht-Bark) · Feld fluten (Torfgor zieht um) · Torfgor als Glutwächter belassen und Gräben ziehen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Bran und der glühende Torf |
| 2 | Beobachten | Das Torfgor beobachten |
| 3 | Untersuchen | Glutnester finden |
| 4 | Entscheidung | Eier umsiedeln oder Feld fluten? |

**Voraussetzung:** `–`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_MAT_PEATCOAL ×5; ITM_EVO_EMBER
**Folge:** Kein Moorbrand; Cindrels leben im Uralthain (R01) oder im Moor

#### SQ_061 · Lieder für Tavesh

*Fraktion · Freie Stimmen · Kette **Unterstadt** (4/4) · Akt I · Auftrag: Tavesh Amaru (Morvenfurt) · Intensität 6 · ~50 min*

Tavesh will die Unterstadt aus dem Verborgenen holen – ein Fest am Laternensteg, offen für alle, mit Liedern, die die Unterstadt sonst nur unter sich singt. Die Stadtwache ist nervös, der Rat skeptisch. Der Wärter organisiert, vermittelt und hält am Ende eine Rede (drei Haltungen).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tavesh' Idee |
| 2 | Sprechen | Ratsherrin Maire überzeugen |
| 3 | Liefern | Laternen für den Steg bringen |
| 4 | Entscheidung | Die Rede am Laternensteg |
| 5 | Lager | Das Fest feiern |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=2 & Quest.SQ_059` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F04 +400 · Titel „Chorfreund“; Hain-Dekor ITM_DECO_UNDERSTREETFLAG
**Folge:** Unterstadt-Fest als Weltereignis im Nachhall (jeden 20. Spieltag)

#### SQ_062 · Die Probe im Nebel

*Wärterprüfung · Akt I · Auftrag: Evhe Corrach (Morvenfurt) · Intensität 5 · ~30 min*

Evhe, Corrachs Tochter und Arenameisterin, bietet eine Nebelprobe an: Zwei Kämpfe bei so dichtem Nebel, dass die Zeitleiste nur drei Züge zeigt – eine Lektion darin, Gegner zu hören statt zu sehen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Evhes Angebot |
| 2 | Bedingung | Dichter Nebel |
| 3 | Kampf | Erster Kampf im Nebel |
| 4 | Kampf | Zweiter Kampf gegen Evhe |
| 5 | Beobachten | Unter der Arena lauschen (Nhael'vesh) |

**Voraussetzung:** `Akkorde>=4` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 500 ◎ · 1.500 Wärter-EP · ITM_HELD_FOGSCARF; ITM_KS_041
**Folge:** Evhe-Barks; Nebeltraining in der Arena verfügbar

#### SQ_063 · Das erste Netz

*Fraktion · Freie Stimmen · Kette **Netze im Nebel** (1/4) · Akt I · Auftrag: Der Schatten (Morvenfurt) · Intensität 4 · ~35 min*

Fischer finden in ihren Reusen immer öfter fremde Netze – feinmaschig, mit Klangperlen beschwert, gemacht für Echos, nicht für Fische. Die Freien Stimmen wollen wissen, wer sie knüpft. Der Wärter folgt den Perlen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Netze in den Kanälen finden |
| 2 | Beobachten | Ein gefangenes Undfin beobachten und befreien |
| 3 | Untersuchen | Den Perlenhändler aufspüren |
| 4 | Sprechen | Dem Schatten berichten |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=3`
**Belohnung:** 550 ◎ · 1.700 Wärter-EP · Ruf F04 +150 · ITM_MAT_FOGPEARL ×3; ITM_TRAP_POOL
**Folge:** Netzfunde werden seltener; Spur führt nach Saltrand (SQ_065, K50)

#### SQ_064 · Der Moorkönig

*Wärterprüfung · Nachhall · Auftrag: Evhe Corrach (Morvenfurt) · Intensität 6 · ~40 min*

Im Nachhall fordert ein alter Moorkönig – Evhes Lehrer, der sich zurückgezogen hatte – jeden heraus, der Nhael'vesh geweckt hat oder schlafen ließ. Sein Kampf läuft bei Nacht in der Versunkenen Senke; Gift und Geist, Nebel und Wasser.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Evhe kündigt ihren Lehrer an |
| 2 | Bedingung | Nacht in der Senke |
| 3 | Kampf | Kampf gegen Orrin |
| 4 | Entscheidung | Orrins Frage beantworten |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_VENOM; Titel „Moorkönigs Gast“
**Folge:** Orrin bleibt als Trainer in der Senke (wöchentlicher Rückkampf)

#### SQ_065 · Perlen aus Saltrand

*Fraktion · Freie Stimmen · Kette **Netze im Nebel** (2/4) · Akt I · Auftrag: Der Schatten (Morvenfurt) · Intensität 4 · ~40 min*

Die Klangperlen der Netze stammen aus Saltrand – aus einer Werkstatt, die auch für das Kontor arbeitet. Bevor der Wärter nach Saltrand reist, sucht er in Morvenfurt den Mittelsmann und findet eine Liste mit Abnehmern.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Den Mittelsmann beim Perlenkauf beobachten |
| 2 | Entscheidung | Den Mittelsmann zur Rede stellen oder beschatten |
| 3 | Gehen | Nach Saltrand-Hafen reisen |

**Voraussetzung:** `Quest.MQ_A1_04 & Rank.F04>=3 & Quest.SQ_063`
**Belohnung:** 650 ◎ · 1.900 Wärter-EP · Ruf F04 +150 · Abnehmerliste (Lore); ITM_CON_REPEL ×2
**Folge:** Kette setzt sich in Saltrand fort (SQ_088, K50)

#### SQ_066 · Die Kapelle öffnet sich

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (1/6) · Akt III · Auftrag: Schwester Ivra (Morvenfurt) · Intensität 3 · ~30 min*

In Akt III öffnen die Sereth-treuen Ordensleute ihre Kapelle in Morvenfurt. Schwester Ivra, mit Schiefertafel, lädt den Wärter ein, eine Stunde mit ihnen zu schweigen. Danach schreibt sie: „Wir wussten nicht, wem wir dienten. Hilf uns, es wiedergutzumachen.“

**Lösungen:** Steine zerstören (Ivra nickt) · der Akademie zur Untersuchung geben · im Moor versenken, wo sie niemandem schaden (Ivra schreibt: „Stille, die niemanden zwingt.“).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ivras Tafel |
| 2 | Lager | Eine Stunde Stille in der Kapelle |
| 3 | Untersuchen | Drei alte Stillsteine im Moor finden, die der Orden gesetzt hat |
| 4 | Entscheidung | Ivra sagen, was mit den Steinen geschehen soll |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · ITM_EMAT_STILLSHARD ×2; Kodex-Fragment „Ordensgelübde“
**Folge:** Kapelle bleibt offen; Ordensleute grüßen schweigend (Gesten-Barks)

#### SQ_067 · Was Stille heilt

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (2/6) · Akt III · Auftrag: Schwester Ivra (Morvenfurt) · Intensität 4 · ~40 min*

Ivra bringt den Wärter zu einem Undrath, das seit der Klangpest-ähnlichen Raserei eines Sturms nicht mehr schläft. Der Orden glaubt, nur Stille kann es heilen. Der Wärter versucht beides: ein Lied und eine Stille – und beobachtet, was hilft.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum ruhelosen Undrath |
| 2 | Beobachten | Drei Verhaltensmerkmale des Undrath beobachten |
| 3 | Entscheidung | Lied oder Stille anbieten |
| 4 | Beobachten | Die Wirkung beobachten |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07 & Quest.SQ_066` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · ITM_CON_CLEANSE ×3; Rezept RCP_058
**Folge:** Das Undrath schläft; Ivras Notiz „Beides heilt – aber nicht dasselbe.“ im Kodex


---

## 6. Saltrand I (R06) – SQ_068–SQ_070

Die ersten drei Saltrand-Quests schließen Ketten ab, die in anderen Regionen begannen (Vaels Lücken, Erz und Ehre), und führen eine Echo-Geschichte ein. Die übrigen 20 Saltrand-Quests folgen in K50.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_068 | Die Küste hat eigene Regeln | Fraktion | F01 · FQ_F01_02 | Akt I | 5 | 50 | Time=Day |
| SQ_069 | Die Möwe von Möwenhuk | Echo-Geschichte | – | Akt I | 2 | 20 | Time=Dawn |
| SQ_070 | Eisen für die Werft | Fraktion | F02 · FQ_F02_02 | Akt I | 5 | 50 | – |

#### SQ_068 · Die Küste hat eigene Regeln

*Fraktion · Akademie der Resonanz · Kette **Vaels Lücken** (4/4) · Akt I · Auftrag: Gelehrte Oona (Akademie) (Saltrand-Hafen) · Intensität 5 · ~50 min*

Oonas Arbeit über Vaels Lücken endet in Saltrand: Marwyns an der Dünenküste haben zwei Klangmal-Muster, je nach Gezeit. Vael hielt sie für zwei Arten. Der Wärter beweist, dass es eine ist – oder dass Vael doch recht hatte. Oona will die Wahrheit, keine Bestätigung.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Oona an der Kaimauer |
| 2 | Beobachten | Marwyns bei Flut beobachten |
| 3 | Beobachten | Marwyns bei Ebbe beobachten |
| 4 | Foto | Ein Maraune beim Musterwechsel fotografieren |
| 5 | Entscheidung | Ergebnis vortragen |

**Voraussetzung:** `Quest.MQ_A1_07 & Rank.F01>=2 & Quest.SQ_049` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F01 +400 · ITM_KS_029; Kodex-Fragment „Vaels Lücken IV“; Akademie-Abzeichen (Kosmetik)
**Folge:** Oonas Arbeit „Vaels Lücken“ in der Akademie-Bibliothek; Kodex-Korrekturen in drei Arten

#### SQ_069 · Die Möwe von Möwenhuk

*Echo-Geschichte · Akt I · Auftrag: Fischerin Tjarke (Möwenhuk) · Intensität 2 · ~20 min*

Ein Aerlet folgt Tjarkes Boot jeden Morgen und stiehlt einen Fisch. Tjarke ist das recht – bis das Aerlet ausbleibt. Sie bittet den Wärter, nachzusehen. Das Aerlet hat sich im Kliffsund in einem alten Netz verfangen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tjarke am Hafen |
| 2 | Untersuchen | Im Kliffsund nach dem Aerlet suchen |
| 3 | Beobachten | Das verfangene Aerlet beruhigen und beobachten |
| 4 | Liefern | Mit dem Aerlet einen Fisch zu Tjarke bringen |

**Voraussetzung:** `–` · **Variante/Bedingung:** `Time=Dawn`
**Belohnung:** 400 ◎ · 1.100 Wärter-EP · ITM_FOOD_KELPSNACK ×3; Kodex-Beobachtung Aerlet
**Folge:** Aerlet begleitet Tjarkes Boot wieder (morgens sichtbar)

#### SQ_070 · Eisen für die Werft

*Fraktion · Goldklang-Kontor · Kette **Erz und Ehre** (4/4) · Akt I · Auftrag: Werftmeister Klaas (Saltrand-Hafen) · Intensität 5 · ~50 min*

Das Kharsk-Eisen aus SQ_035 kommt in Saltrand an – und Werftmeister Klaas weigert sich, es zu verbauen: Es „singt“ unter dem Hammer. Tova und Klaas streiten per Klangbrief. Der Wärter muss zeigen, dass singendes Eisen kein Mangel ist, sondern ein Qualitätsmerkmal.

**Lösungen:** Klaas überzeugen (Messung) · Tova anweisen, „stilles“ Eisen zu liefern (teurer) · Brassel als Prüfer in die Werft holen (dritte Lösung, Werftmeister-Bark).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Klaas und das singende Eisen |
| 2 | Beobachten | Ein Brassel in der Werft beim Nieten beobachten |
| 3 | Rätsel | Mit dem Resonator den Klang des Eisens vergleichen |
| 4 | Entscheidung | Klaas und Tova (per Klangbrief) zusammenbringen |
| 5 | Sprechen | Marieke den Abschluss melden |

**Voraussetzung:** `Quest.MQ_A1_05 & Rank.F02>=2 & Quest.SQ_035`
**Belohnung:** 750 ◎ · 2.000 Wärter-EP · Ruf F02 +400 · ITM_GEAR_BAG_2; Rezept RCP_060
**Folge:** Werft verbaut Kharsk-Eisen; neue Schiffe im Hafen (Data Layer, Akt II)


---

## 7. Fraktionsketten in diesem Kapitel

| Kette | Fraktion | Einstieg | Titel | Quests (dieses Kapitel fett) |
|---|---|---|---|---|
| FQ_F01_01 | F01 | Rang 1 | Die Außenstelle | **SQ_001**, **SQ_003**, **SQ_005**, **SQ_025** |
| FQ_F02_01 | F02 | Rang 1 | Lindenhonig | **SQ_007**, **SQ_009**, **SQ_011**, **SQ_029** |
| FQ_F03_01 | F03 | Rang 1 | Die Spur der Lauscherin | **SQ_013**, **SQ_015**, **SQ_017**, **SQ_019** |
| FQ_F03_02 | F03 | Rang 2 | Grenzgänger | **SQ_021**, **SQ_037**, **SQ_039**, **SQ_041** |
| FQ_F04_01 | F04 | Rang 1 | Die Kurierin | **SQ_022**, **SQ_023**, **SQ_024**, **SQ_046** |
| FQ_F01_02 | F01 | Rang 2 | Vaels Lücken | **SQ_027**, **SQ_047**, **SQ_049**, **SQ_068** |
| FQ_F02_02 | F02 | Rang 2 | Erz und Ehre | **SQ_031**, **SQ_033**, **SQ_035**, **SQ_070** |
| FQ_F03_03 | F03 | Rang 3 | Pässe im Schnee | **SQ_043**, **SQ_044**, **SQ_045**, **SQ_051** |
| FQ_F03_04 | F03 | Rang 4 | Die stillen Ränder | **SQ_053**, SQ_084, SQ_086, SQ_107 |
| FQ_F04_02 | F04 | Rang 2 | Unterstadt | **SQ_055**, **SQ_057**, **SQ_059**, **SQ_061** |
| FQ_F04_03 | F04 | Rang 3 | Netze im Nebel | **SQ_063**, **SQ_065**, SQ_088, SQ_089 |
| FQ_F05_01 | F05 | Rang 1 | Das Schweigen lernen | **SQ_066**, **SQ_067**, SQ_144, SQ_146, SQ_148, SQ_150 |

**Rückkehr-Design:** Ketten mit Einstiegsrang 3 oder 4 (z. B. *Pässe im Schnee*, *Die stillen Ränder*, *Netze im Nebel*) liegen in Akt-I-Regionen, sind aber erst mit dem Ruf erreichbar, den Spielende typischerweise in Akt II haben (K47 §8). So lohnt die Rückkehr in Kharsgrat und Morvenmoor; die Wege sind dann durch Grab- und Flugreiten schneller (CANON §15).

---

## 8. Auftraggeber

Je NPC höchstens drei Geschichten; eine Fraktionskette zählt als eine Geschichte (K48 §3, QS-14).

| NPC-ID | Name | Quests |
|---|---|---|
| NPC_AILSA | Fährmeisterin Ailsa Duvreth | SQ_054 |
| NPC_BRANDA | Bergführerin Branda | SQ_028, SQ_032 |
| NPC_BRUECKENWART_ELWYN | Brückenwart Elwyn | SQ_056 |
| NPC_ENNIS | Ennis Rook (Kurierin) | SQ_022, SQ_023, SQ_024, SQ_046 |
| NPC_EVHE | Evhe Corrach | SQ_062, SQ_064 |
| NPC_FENJA | Zeugmeisterin Fenja | SQ_013, SQ_015, SQ_017, SQ_019, SQ_021 |
| NPC_FISCHERIN_TJARKE | Fischerin Tjarke | SQ_069 |
| NPC_GELEHRTE_OONA | Gelehrte Oona (Akademie) | SQ_047, SQ_049, SQ_068 |
| NPC_LEHRLING_MIKKEL | Akademie-Lehrling Mikkel | SQ_038 |
| NPC_LINA | Lina (Kind, Lindwiesen) | SQ_002 |
| NPC_MAELIS | Maelis Wendt | SQ_020 |
| NPC_MAREN | Maren (Lindwiesen) | SQ_012 |
| NPC_MESSER_HAKON | Messmeister Hakon (Akademie) | SQ_025, SQ_027 |
| NPC_OSSIAN | Kontorschreiber Ossian | SQ_007, SQ_009, SQ_011 |
| NPC_PASSWART_JORN | Passwart Jorn (Wildwacht) | SQ_037, SQ_039, SQ_041, SQ_043, SQ_044, SQ_051, SQ_053 |
| NPC_PELL | Archivarin Pell | SQ_001, SQ_003, SQ_005, SQ_018 |
| NPC_R01_ANSELM | Schnitzer Anselm | SQ_008 |
| NPC_R01_GRETA | Greta (Wildwacht-Kammer) | SQ_010 |
| NPC_R01_LORIN | Apotheker Lorin | SQ_016 |
| NPC_R01_ODO | Wirt Odo | SQ_006, SQ_014 |
| NPC_R02_GERD | Gerd (Halle der Klans) | SQ_036, SQ_045 |
| NPC_R02_HRALDA_SMITH | Grollschmied Hraldur | SQ_034 |
| NPC_R02_TOVA | Tova (Erzkontor) | SQ_029, SQ_031, SQ_033, SQ_035 |
| NPC_R02_YRSA | Ahnenstein-Tutorin Yrsa | SQ_030, SQ_040 |
| NPC_R03_CORRACH | Moorweise Corrach | SQ_052, SQ_058 |
| NPC_R03_FINN | Bootsbauer Finn | SQ_050 |
| NPC_R03_NIALLA | Nialla (Laternensteg) | SQ_048 |
| NPC_R03_SHADE | Der Schatten | SQ_055, SQ_057, SQ_059, SQ_063, SQ_065 |
| NPC_R06_KLAAS | Werftmeister Klaas | SQ_070 |
| NPC_SCHWESTER_IVRA | Schwester Ivra | SQ_066, SQ_067 |
| NPC_SIGGA | Sigga (Brakkfels) | SQ_026 |
| NPC_TAVESH | Tavesh Amaru | SQ_061 |
| NPC_TORBEN | Holzfäller Torben | SQ_004 |
| NPC_TORFSTECHER_BRAN | Torfstecher Bran | SQ_060 |
| NPC_TORVIK | Torvik Hrall | SQ_042 |

Neue benannte NPCs dieses Kapitels (u. a. Archivarin Pell, Kontorschreiber Ossian, Zeugmeisterin Fenja, Kurierin Ennis Rook, Messmeister Hakon, Passwart Jorn, Gelehrte Oona, Schwester Ivra) werden in `Data/World/Npcs.csv` (K53) mit Tagesablauf-Muster (CANON §53) geführt. Pell, Ossian, Fenja und Ivra sind zugleich die **Rüstmeister** ihrer Fraktionen (K47 §2).

---

## 9. Prüfung gegen die Quest-Bibel

`python3 tools/authoring/sq_k49.py` prüft alle 70 Quests gegen die Regeln aus K48:

| Regel | Prüfung | Ergebnis |
|---|---|---|
| QS-01 | Jede Gerüst-Quest ist beschrieben | ✓ |
| QS-02 | 3–6 Schritte | ✓ |
| QS-03 | Mindestens ein Verstehen-Schritt (Beobachten, Untersuchen, Foto, Rätsel, Entscheidung, Heilen) – QR-02 | ✓ |
| QS-04 | Kein Sammel-Schritt am Ende – QR-03 | ✓ |
| QS-05/06 | Zieltypen und Orte existieren; Orte in der eigenen Region (außer Ketten, Liefern, Gespräch) | ✓ |
| QS-07 | Arten, Items, Arenen existieren | ✓ |
| QS-08 | Intensität ≤ 6 (Kettenabschluss ≤ 7) | ✓ |
| QS-09 | Dauer 15–45 min (Ketten ≤ 60) | ✓ |
| QS-10 | Nicht-monetäre Belohnung, Items existieren – QR-10 | ✓ |
| QS-11 | `TruthLevel` ≤ Wahrheit des Verfügbarkeitsakts – QR-12 / L-01 | ✓ |
| QS-12 | Wärterprüfung mit Kampf; Weltereignis mit Bedingung | ✓ |
| QS-13 | Referenzierte Hauptquests und Flags existieren | ✓ |
| QS-14 | Auftraggeber-Regel | ✓ |
| QS-15 | ≥ 25 % je Region mit Tageszeit/Wetter/Mond – QR-09 | ✓ (R01 50 %, R02 64 %, R03 62 %) |

### 9.1 Regionale Kennzahlen

**Verdanthain**

| Kennzahl | Wert |
|---|---|
| Quests | 24 |
| Schritte | 96 (Ø 4,0) |
| Ø Dauer | 29 min |
| Σ Spielzeit | 11,6 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 12 (50 %) |
| Σ Sol | 14.250 ◎ |
| Σ Wärter-EP | 36.100 |
| Kategorien | Fraktion 14, Echo-Geschichte 2, Rätsel & Ruinen 2, Menschen 2, Forschung 2, Weltereignis 1, Wärterprüfung 1 |
| Häufigste Zieltypen | Beobachten 20, Sprechen 19, Untersuchen 15, Entscheidung 14, Gehen 10, Bedingung 3, Rätsel 3, Begleiten 3 |

**Kharsgrat**

| Kennzahl | Wert |
|---|---|
| Quests | 22 |
| Schritte | 93 (Ø 4,2) |
| Ø Dauer | 36 min |
| Σ Spielzeit | 13,2 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 14 (64 %) |
| Σ Sol | 15.350 ◎ |
| Σ Wärter-EP | 37.900 |
| Kategorien | Fraktion 13, Rätsel & Ruinen 2, Menschen 2, Forschung 2, Echo-Geschichte 1, Weltereignis 1, Wärterprüfung 1 |
| Häufigste Zieltypen | Sprechen 18, Beobachten 17, Entscheidung 12, Untersuchen 10, Begleiten 8, Gehen 5, Kampf 5, Rätsel 4 |

**Morvenmoor**

| Kennzahl | Wert |
|---|---|
| Quests | 21 |
| Schritte | 85 (Ø 4,0) |
| Ø Dauer | 35 min |
| Σ Spielzeit | 12,4 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 13 (62 %) |
| Σ Sol | 16.550 ◎ |
| Σ Wärter-EP | 36.700 |
| Kategorien | Fraktion 12, Rätsel & Ruinen 2, Forschung 2, Wärterprüfung 2, Echo-Geschichte 1, Weltereignis 1, Menschen 1 |
| Häufigste Zieltypen | Sprechen 18, Beobachten 15, Untersuchen 15, Entscheidung 13, Bedingung 5, Gehen 5, Kampf 3, Traversal 2 |

### 9.2 Sichtbare Folgen (QR-05)

Jede Quest verändert die Welt. Die Folgen gehören zu drei Klassen, die Level Design und Tech unterschiedlich umsetzen:

| Klasse | Umsetzung | Beispiele |
|---|---|---|
| Data Layer | Questzustand schaltet `DL_Quest_SQ###` | Neuer Holzweg (SQ_004), Lawinengalerie (SQ_044), Brücke Fennhaven (SQ_056), Schiffe (SQ_070) |
| Population | Spawn-Tabelle der Zone erhält Eintrag (K52) | Rillo-Familie (SQ_002), Rillwards an der Furt (SQ_024), Gratkin-Wanderung (SQ_041) |
| NPC/Bark | NPC-Zustand, Barks `Quest.SQ###.After` | Lina, Odo, Hralda, Evhe, Orrin |
| Weltereignis | Wiederkehrend im Kalender (K15) | Ahnenfeuer-Nacht (SQ_045), Unterstadt-Fest (SQ_061), Gratkin-Wanderung |

---

## 10. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | 288 Schritte platzieren; ~120 `CLUE_*`, 9 Rätsel `PZ_SQ*`, Data Layer `DL_Quest_SQ004/024/041/044/056/070` | K57 |
| Writing | ~70 × 120 Dialogzeilen, 3–6 Barks je Quest danach | K55 |
| Audio | Brannocs Lied (SQ_017/019), Humbog-Ruf (SQ_048), Liederbogen der Unterstadt (SQ_057), Rettungshorn (SQ_043) | K55 |
| Art | 12 Hain-Dekor-Objekte (`Decor.csv`), 1 Schlüsselgegenstand | K56 |
| Combat | 11 Wärterprüfungs-/Questkämpfe mit Regeln (Nebel-Zeitleiste 3 Züge, Formationsduell, Brückenwind) | K34/K35 |
| QA | Quest-Bot über alle 70 Quests, Varianten (Tageszeit/Wetter) per Debug-Wetter | K66 |

---

## 11. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-187 | Kettengeber dürfen eine ganze Fraktionskette vergeben; Auftraggeber-Grenze zählt Geschichten statt Quests | Ketten sind eine Geschichte mit einer Figur; Wechsel des Gebers würde sie zerreißen | starre Grenze 3 Quests/NPC |
| ADR-188 | Sol, EP, Ruf und Voraussetzungen der Nebenquests werden aus Formeln und Gerüst berechnet, nicht handgesetzt | Konsistenz über 210 Quests; Balancing ändert eine Formel statt 210 Zeilen | Handwerte je Quest |
| ADR-189 | Nebenquests dürfen in andere Regionen liefern oder dort sprechen lassen, aber ihre Handlung findet in ihrer Region statt | Regionen bleiben in sich lesbar; Verbindungen zwischen Regionen entstehen über Ketten | regionsfreie Nebenquests |

---

## 12. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §189 | Nebenquests SQ_001–SQ_070 (Titel, Auftraggeber, Schritte, Folgen; `SideQuestDetails.csv`, `SideQuestSteps.csv`), Prüfregeln QS-01–QS-15 | LOCKED |
| §190 | Hain-Dekor `ITM_DECO_*` (`Decor.csv`, kosmetisch, Stimmung +2 nicht stapelnd), Schlüsselgegenstände `ITM_KEY_*` (`KeyItems.csv`) | LOCKED |
| §10 | ADR-187 – ADR-189 | LOCKED |

---

## 13. Kapitel-Checkliste

- [x] 70 Nebenquests ausgeschrieben (Kurzinhalt, Schritte, Lösungen, Voraussetzungen, Belohnungen, Folgen)
- [x] Vier Regionen mit eigenem Ton; Akt-I-Quests und Spätquests (Akt II/III/Nachhall)
- [x] Fraktionsketten (9 Ketten mit Quests in diesem Kapitel), Auftraggeber-Regel
- [x] Alle Prüfregeln QS-01–QS-15 erfüllt (0 Fehler)
- [x] Hain-Dekor und Schlüsselgegenstände als Daten
- [x] Anforderungen, ADR-187 – ADR-189, CANON §189–§190

➡️ **Nächstes Kapitel: K50 – Nebenquests II (SQ_071–SQ_140).**
