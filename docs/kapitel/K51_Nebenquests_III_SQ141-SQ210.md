# K51 · Nebenquests III (SQ_141–SQ_210): Hvitfell II, Ael'Dorun, Prismtiefen, Nimbara

| Feld | Wert |
|---|---|
| Dokument | Kapitel 51 von 68 · Quest-Bibel, Nebenquests Teil III |
| Version | 1.0 |
| Owner | Lead Quest Designer |
| Mitwirkende | Writer (Hvitfell, Ael'Dorun, Prismtiefen, Nimbara), Narrative Director (L-01, Enden), Level Design, Systems Designer |
| Baut auf | K48 (Quest-Bibel), K49–K50 (SQ_001–140, Prüfregeln), K45–K46 (Akt II/III, Enden, Nachhall), K47 (Orden ab W6), K11–K13 (Städte, Dörfer, Haken), K26–K27 (Arten R08–R10), K39 (Mythische Spuren) |
| Status | ✅ Freigegeben |
| Im Repository | `SideQuestDetails.csv`, `SideQuestSteps.csv` (alle 210 Quests, 849 Schritte), `Decor.csv`, `KeyItems.csv`, Quelle `tools/authoring/sq_k51.py` |
| Neue Kanon-Einträge | CANON §193 (Nebenquests SQ_141–210), §194 (Nebenquests gesamt), §195 (Orte der Pause) |

---

## Inhalt

1. [Überblick](#1-überblick)
2. [Späte Regionen, späte Wahrheiten](#2-späte-regionen-späte-wahrheiten)
3. [Hvitfell II (R07) – SQ_141–SQ_151](#3-hvitfell-ii-r07--sq_141sq_151)
4. [Ael'Dorun (R08) – SQ_152–SQ_172](#4-aeldorun-r08--sq_152sq_172)
5. [Prismtiefen (R09) – SQ_173–SQ_190](#5-prismtiefen-r09--sq_173sq_190)
6. [Nimbara (R10) – SQ_191–SQ_210](#6-nimbara-r10--sq_191sq_210)
7. [Die Orte der Pause](#7-die-orte-der-pause)
8. [Alle 210 Nebenquests im Überblick](#8-alle-210-nebenquests-im-überblick)
9. [Abgleich mit den Haken aus K11–K13](#9-abgleich-mit-den-haken-aus-k11k13)
10. [Auftraggeber dieses Kapitels](#10-auftraggeber-dieses-kapitels)
11. [Anforderungen an andere Abteilungen](#11-anforderungen-an-andere-abteilungen)
12. [Decision Records und Change Request](#12-decision-records-und-change-request)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Überblick

Die letzten 70 Nebenquests gehören zu den Regionen der Spätphase: Hvitfell nach dem Verrat, Ael'Dorun mit der Akademie im Umbruch, Prismtiefen in der Energiekrise, Nimbara nach 1.000 Jahren Isolation. Viele Quests öffnen erst in Akt III oder im Nachhall und erzählen, wie die Welt mit den Wahrheiten lebt: ein Thing, das über Stillsteine streitet; Studierende, die ein Ethikgremium fordern; Baumeister, die lernen, „Bodenleute“ statt „Bodenbewohner“ zu sagen; ein Orden, der seine Steine selbst birgt.

| Kennzahl | Wert |
|---|---|
| Quests | 70 |
| Schritte | 274 (Ø 3,9) |
| Ø Dauer | 38 min |
| Σ Spielzeit | 44,1 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 29 (41 %) |
| Σ Sol | 109.550 ◎ |
| Σ Wärter-EP | 139.250 |
| Kategorien | Fraktion 39, Forschung 7, Menschen 6, Rätsel & Ruinen 6, Wärterprüfung 5, Weltereignis 4, Echo-Geschichte 3 |
| Häufigste Zieltypen | Sprechen 62, Beobachten 62, Entscheidung 34, Untersuchen 30, Rätsel 13, Gehen 12, Lager 11, Kampf 11 |

| Region | Grundton | Wiederkehrende Motive |
|---|---|---|
| Hvitfell II | Erinnerung, Versöhnung | Thing, Kloster, Ulreks Buße, Novizen über den Pass |
| Ael'Dorun | Verantwortung, Aufklärung | Venns Akten, Bundesrat, Studentenstreik, Glyphen |
| Prismtiefen | Dunkelheit und Licht | Energiekrise, Brannocs Erbe, Grubenwehr, Spiegel ohne Bild |
| Nimbara | Weite, Begegnung | Wendelins letzter Stein, Luftfracht, Windrennen, Letzte Bitten |

---

## 2. Späte Regionen, späte Wahrheiten

| Mittel | Regel | Beispiele |
|---|---|---|
| **Nach dem Verrat** | Ael'Dorun-Quests mit Venn-Bezug verlangen MQ_A2_07 (ADR-190) | SQ_152, SQ_154, SQ_166 |
| **Zwei Fassungen** | Quests, die vor und nach W6 spielbar sind, erzählen mit demselben Kern, aber anderem Rahmen | SQ_158 „Kaels Forschungsarbeit“ |
| **Akt III** | Quests vor dem Finale (Prismtiefen, Nimbara) greifen W8 auf | SQ_195, SQ_198, SQ_202 |
| **Nachhall je Ende** | Quests, deren Inhalt je Ende verschieden klingt (Neues Lied / Sanfte Stille), aber dieselben Schritte haben | SQ_175, SQ_184, SQ_193 |
| **Mythische Spuren** | Spätquests legen Spuren zu Chronaire, Mirrowisp, Aurelune und Velnox (K62) | SQ_159, SQ_178, SQ_196, SQ_210 |

**Ein Atemzug vor dem Finale:** SQ_202 „Letzte Bitten“ ist absichtlich in Akt III zwischen MQ_A3_05 und MQ_A3_07 spielbar (Gerüst-Ausnahme in `sq_plan.py`, K12 §5). Sie ist die einzige Nebenquest, die Ysolde selbst vergibt, und setzt `FLAG_YSOLDE_BOND` +1 bei einfühlsamer Antwort.

---

## 3. Hvitfell II (R07) – SQ_141–SQ_151

Die Kette *Das Schweigen lernen* (Orden, ab Akt III) endet hier: Novizen über den Pass, Ulreks Buße, eine Stille Stunde als Dank. Daneben stehen das Thing von Hvitmark, der Wiederaufbau von Eiðvik-Neu und das erste Polarlicht-Foto der Akademie.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_141 | Thing-Streit | Menschen | – | Akt III | 4 | 40 | – |
| SQ_142 | Schlitten ohne Rast | Fraktion | F04 | Akt II | 4 | 35 | Weather=Snow |
| SQ_143 | Eiðvik-Neu baut auf | Menschen | – | Akt II | 3 | 35 | – |
| SQ_144 | Die Schwester im Kloster | Fraktion | F05 · FQ_F05_01 | Akt III | 3 | 40 | – |
| SQ_145 | Was das Eis behält | Forschung | – | Nachhall | 3 | 35 | Time=Night |
| SQ_146 | Der Pass der Schweigenden | Fraktion | F05 · FQ_F05_01 | Akt III | 4 | 40 | Weather=Snow |
| SQ_147 | Aurora-Fotografie | Forschung | – | Akt II | 3 | 30 | Weather=Aurora |
| SQ_148 | Ulreks Buße | Fraktion | F05 · FQ_F05_01 | Akt III | 5 | 45 | – |
| SQ_149 | Sigruns Eisprobe | Wärterprüfung | – | Akt II | 5 | 35 | – |
| SQ_150 | Gast der Stille | Fraktion | F05 · FQ_F05_01 | Akt III | 5 | 55 | – |
| SQ_151 | Die Pause im Gletscher | Fraktion | F05 · FQ_F05_02 | Nachhall | 4 | 45 | – |

#### SQ_141 · Thing-Streit

*Menschen · Akt III · Auftrag: Sprecherin Astrid Eiðsen (Hvitmark) · Intensität 4 · ~40 min*

Alle zehn Spieltage tagt das Thing von Hvitmark. Nach dem Verrat fordern Ordensanhänger, dass die Stadt die Stillsteine weiter duldet – „nur noch freiwillig“. Wärter und Wildwacht wollen ein Verbot. Astrid bittet den Wärter, vor dem Thing zu sprechen, nachdem er beide Seiten gehört hat.

**Lösungen:** Verbot (Wärter) · Duldung (Orden) · freiwillige „Stille Häuser“ für Echos, die Ruhe suchen, ohne Steine in der Wildnis (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Astrid lädt zum Thing |
| 2 | Sprechen | Solveig für die Ordensanhänger |
| 3 | Sprechen | Grete für die Wärter |
| 4 | Beobachten | Ein Eidrun an einem freiwilligen Stillstein beobachten |
| 5 | Entscheidung | Rede vor dem Thing |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Titel „Thingredner“; ITM_LURE_BELLCHIME
**Folge:** Thing-Beschluss: Verbot, Duldung mit Auflagen oder „Stille Häuser“ (dritte Lösung); Barks in Hvitmark

#### SQ_142 · Schlitten ohne Rast

*Fraktion · Freie Stimmen · Akt II · Auftrag: Zelle Hvitmark (Freie Stimmen) (Hvitmark) · Intensität 4 · ~35 min*

Ein Eisfisch-Händler lässt Kjalfs Tag und Nacht Schlitten über den Spiegelsee ziehen. Die Zelle der Freien Stimmen will die Kjalfs nachts losschneiden. Der Wärter beobachtet erst – und findet heraus, dass der Händler selbst kurz vor dem Ruin steht.

**Lösungen:** Nachts befreien (Bjarne ruiniert) · Wildwacht melden · Askels Snevel-Tausch (SQ_133) für Bjarnes Fang nutzen, damit er weniger fahren muss (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Zelle im Wollkeller |
| 2 | Beobachten | Die erschöpften Kjalfs beobachten |
| 3 | Sprechen | Bjarne zuhören |
| 4 | Entscheidung | Lösung für Kjalfs und Bjarne |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_FOOD_ICEFISH ×3; ITM_CON_STAMINA ×2
**Folge:** Kjalfs ziehen nur noch tagsüber mit Ruhezeiten (oder sind frei)

#### SQ_143 · Eiðvik-Neu baut auf

*Menschen · Akt II · Auftrag: Halla (Eiðvik-Neu) (Eiðvik-Neu) · Intensität 3 · ~35 min*

Halla hat die Klangpest als Kind überlebt und lebt seitdem in Eiðvik-Neu. Das Dorf will ein Gemeinschaftshaus bauen, aber niemand traut sich, Holz aus dem alten Eiðvik zu holen. Der Wärter begleitet Halla in die Ruinen – sie will selbst gehen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Halla und der Plan |
| 2 | Begleiten | Halla in die Ruinen begleiten |
| 3 | Untersuchen | Tragfähige Balken finden |
| 4 | Beobachten | Das Eidwacht, das über den Ruinen wacht, beobachten |
| 5 | Lager | Richtfest |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_EIDVIKBEAM; ITM_MAT_FROSTPINE ×4
**Folge:** Gemeinschaftshaus in Eiðvik-Neu (Data Layer); Halla erzählt Besuchern von früher

#### SQ_144 · Die Schwester im Kloster

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (3/6) · Akt III · Auftrag: Schwester Ivra (LOC_KLOSTER_SCHWEIGFELS) · Intensität 3 · ~40 min*

Leif aus Fjallstad hat seine Schwester Gunnhild seit Jahren nicht gesprochen – sie trat dem Orden bei und legte das Schweigegelübde ab. Nach dem Verrat fragt Ivra, ob der Wärter Leifs Brief überbringen will. Gunnhild antwortet auf ihrer Schiefertafel.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Leifs Brief |
| 2 | Gehen | Über den Pass nach Schweigfels |
| 3 | Liefern | Gunnhild den Brief geben |
| 4 | Entscheidung | Gunnhilds Tafel nach Fjallstad tragen – oder sie überreden, selbst zu gehen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07 & Quest.SQ_067`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · ITM_CON_WARM ×2; Kodex-Fragment „Gelübde und Familie“
**Folge:** Gunnhild besucht Fjallstad (Nachhall) oder schreibt Briefe (Bark)

#### SQ_145 · Was das Eis behält

*Forschung · Nachhall · Auftrag: Runa die Erinnernde (Hvitmark) · Intensität 3 · ~35 min*

Im Nachhall bemerkt Runa, dass Uvasils – Leere-Frost-Echos – sich an den Stellen sammeln, wo früher Stillsteine lagen. Sie fragt sich, ob das Eis die Stille „behält“. Der Wärter beobachtet drei Plätze und vergleicht sie mit Ordensakten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Uvasils an drei ehemaligen Steinplätzen beobachten |
| 2 | Untersuchen | Ordensakten zu den Steinplätzen lesen |
| 3 | Sprechen | Runa die Deutung bringen |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Kodex-Fragment „Eisgedächtnis“; ITM_EVO_AURORATHREAD
**Folge:** Uvasil-Plätze als Beobachtungspunkte (Kodex)

#### SQ_146 · Der Pass der Schweigenden

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (4/6) · Akt III · Auftrag: Schwester Ivra (LOC_KLOSTER_SCHWEIGFELS) · Intensität 4 · ~40 min*

Venn-treue Ordensleute halten den oberen Pass. Sechs Novizen wollen nach Schweigfels zu Sereth, ohne Kampf. Ivra führt sie, der Wärter sichert den Weg – im Schneesturm, mit Hallkids als Rufkette.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Schneesturm am Pass |
| 2 | Begleiten | Die Novizen über den Pass führen |
| 3 | Beobachten | Ein Hallbrand als Rufkette nutzen |
| 4 | Flucht | Angekündigter Posten der Venn-Treuen – im Sturm umgehen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07 & Quest.SQ_144` · **Variante/Bedingung:** `Weather=Snow`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · ITM_GEAR_CLOAK_4; Kodex-Fragment „Novizen“
**Folge:** Sechs Novizen in Schweigfels (Gesten-Barks)

#### SQ_147 · Aurora-Fotografie

*Forschung · Akt II · Auftrag: Fotografin Signe (Akademie) (Hvitmark) · Intensität 3 · ~30 min*

Signe will das erste Foto eines Lysthane im Polarlicht für die Akademie-Ausstellung. Lysthanes erscheinen nur, wenn die Aurora singt – und fliehen vor Kameras, die klicken. Der Wärter lernt, mit der Kodex-Linse lautlos zu arbeiten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Signes Ausrüstung |
| 2 | Bedingung | Polarlicht |
| 3 | Beobachten | Das Verhalten der Lysthanes vor dem Foto beobachten |
| 4 | Foto | Ein Lysthane im Polarlicht (≥ 4 Sterne) |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Weather=Aurora`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_GEAR_LENS_3; Hain-Dekor ITM_DECO_AURORAPRINT
**Folge:** Foto in der Akademie-Ausstellung (Dorunsruh, Nachhall)

#### SQ_148 · Ulreks Buße

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (5/6) · Akt III · Auftrag: Schwester Ivra (LOC_KLOSTER_SCHWEIGFELS) · Intensität 5 · ~45 min*

Ulrek, einst Gegner des Wärters, will die Stillsteine bergen, die er selbst gesetzt hat. Er kennt jeden Ort. Er bittet nicht um Vergebung, nur um Begleitung – „damit jemand sieht, dass es getan wird“.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ulrek im Hof des Klosters |
| 2 | Begleiten | Mit Ulrek zu seinen Steinen |
| 3 | Heilen | Drei Steinplätze heilen |
| 4 | Entscheidung | Ulrek antworten, als er fragt, ob es genug ist |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07 & Quest.SQ_146`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · ITM_EMAT_STILLSHARD ×2; Kodex-Fragment „Ulrek“
**Folge:** Ulrek arbeitet für die Wildwacht (Nachhall-Bark) oder bleibt im Kloster

#### SQ_149 · Sigruns Eisprobe

*Wärterprüfung · Akt II · Auftrag: Sigrun Fjall (Hvitmark) · Intensität 5 · ~35 min*

Sigrun lädt zur Eisprobe auf dem Spiegelsee: zwei Kämpfe, bei denen jeder dritte Zug auf dem Eis rutscht und die Formation durcheinanderwirft. Danach erzählt sie von ihrer Großmutter, die die Klangpest überlebte.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Sigruns Einladung |
| 2 | Kampf | Erste Probe auf dem Eis |
| 3 | Kampf | Sigrun selbst |
| 4 | Beobachten | Unter dem Spiegelsee lauschen (Isv'aldr) |

**Voraussetzung:** `Act>=Akt II & Akkorde>=6`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_FROST; ITM_KS_062
**Folge:** Sigrun-Barks; Eistraining

#### SQ_150 · Gast der Stille

*Fraktion · Orden der Stille · Kette **Das Schweigen lernen** (6/6) · Akt III · Auftrag: Schwester Ivra (LOC_KLOSTER_SCHWEIGFELS) · Intensität 5 · ~55 min*

Am Ende der Kette lädt Sereth den Wärter ein, eine Stille Stunde mit dem ganzen Kloster zu verbringen – nicht als Bekehrung, sondern als Dank. Danach spricht Sereth zum ersten Mal vor allen Ordensleuten laut: über Venn, über Schuld, über eine Stille, die niemanden zwingt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Sereths Einladung |
| 2 | Lager | Die Stille Stunde |
| 3 | Beobachten | Uvlets, die sich zum Kloster setzen, beobachten |
| 4 | Entscheidung | Sereth nach ihrer Rede antworten |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A2_07 & Quest.SQ_148`
**Belohnung:** 2.100 ◎ · 2.000 Wärter-EP · Ruf F05 +400 · Titel „Gast der Stille“; Hain-Dekor ITM_DECO_VEILEDWELL
**Folge:** Kloster öffnet den Hof für Besucher; Stille Stunde täglich (K47 REP_STILLHOUR)

#### SQ_151 · Die Pause im Gletscher

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (1/6) · Nachhall · Auftrag: Schwester Ivra (LOC_KLOSTER_SCHWEIGFELS) · Intensität 4 · ~45 min*

Nach dem Finale sagt Ivra, dass man die Pause an manchen Orten hören kann – dort, wo Velnox den Riegel berührte. Der erste ist eine Spalte im Gletscher. Wer dort still ist, hört zwischen zwei Tönen etwas, das kein Ton ist.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Gletscherspalte |
| 2 | Lager | Eine Stunde Stille in der Spalte |
| 3 | Beobachten | Ein Tysvorn, das ruhig neben dem Wärter liegt, beobachten |
| 4 | Sprechen | Ivra berichten |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · Kodex-Fragment „Orte der Pause I“; ITM_LURE_TUNINGFORK
**Folge:** Gletscherspalte als Ort der Pause (Rückkehr)


---

## 4. Ael'Dorun (R08) – SQ_152–SQ_172

Dorunsruh ist Akademie und Ruine zugleich. Die Kette *Aevrins Akten* endet vor dem Bundesrat; Studierende streiken für offene Archive; ein Hehler lernt, Fundstücke zurückzugeben. Im Nachhall wird der Thronsaal zum Ort der Pause.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_152 | Das Rektorat | Fraktion | F01 · FQ_F01_04 | Akt II | 5 | 45 | – |
| SQ_153 | Der Tikkel im Uhrwerk | Echo-Geschichte | – | Akt II | 2 | 25 | – |
| SQ_154 | Akten für den Bundesrat | Fraktion | F01 · FQ_F01_04 | Akt II | 6 | 60 | – |
| SQ_155 | Neumond der Skrivs | Weltereignis | – | Akt II | 3 | 30 | Moon=New |
| SQ_156 | Studentenstreik | Fraktion | F01 | Akt III | 4 | 40 | – |
| SQ_157 | Glyphen-Übersetzung | Rätsel & Ruinen | – | Akt II | 4 | 45 | – |
| SQ_158 | Kaels Forschungsarbeit | Fraktion | F01 | Akt II | 4 | 40 | – |
| SQ_159 | Chronaires Uhr | Rätsel & Ruinen | – | Nachhall | 4 | 40 | Time=Day |
| SQ_160 | Die Prüfung der Hörerin | Fraktion | F01 | Akt II | 3 | 30 | – |
| SQ_161 | Der Hehler | Menschen | – | Akt II | 4 | 40 | Time=Night |
| SQ_162 | Venns leeres Zimmer | Fraktion | F01 | Akt III | 3 | 30 | – |
| SQ_163 | Der Bruder, der spricht | Menschen | – | Akt II | 2 | 25 | Time=Dusk |
| SQ_164 | Die große Stille am Archontenviertel | Fraktion | F03 | Akt II | 5 | 45 | – |
| SQ_165 | Der Wächter ohne Splitter | Forschung | – | Nachhall | 3 | 35 | – |
| SQ_166 | Gefangene Gelehrsamkeit | Fraktion | F04 | Akt II | 5 | 45 | – |
| SQ_167 | Die Bibliothek der Resonanz | Forschung | – | Akt II | 3 | 35 | Time=Night |
| SQ_168 | Hymnoras Chor | Fraktion | F04 | Akt III | 4 | 40 | Time=Dusk |
| SQ_169 | Glyphenduell | Wärterprüfung | – | Akt II | 5 | 35 | – |
| SQ_170 | Die Kapelle im Archontenviertel | Fraktion | F05 · FQ_F05_02 | Nachhall | 3 | 35 | – |
| SQ_171 | Schatten zwischen den Säulen | Fraktion | F05 · FQ_F05_02 | Nachhall | 4 | 40 | Weather=Fog |
| SQ_172 | Der Thron ohne Krone | Fraktion | F05 · FQ_F05_02 | Nachhall | 4 | 45 | – |

#### SQ_152 · Das Rektorat

*Fraktion · Akademie der Resonanz · Kette **Aevrins Akten** (3/4) · Akt II · Auftrag: Aevrin Thal (Dorunsruh) · Intensität 5 · ~45 min*

Aevrin öffnet Venns Rektorat. Zwischen Messprotokollen liegen Kinderzeichnungen – ein Keller, Echos über einer brennenden Stadt. Aevrin will Fakten für den Bundesrat; der Wärter findet auch den Menschen hinter den Fakten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Aevrin am versiegelten Rektorat |
| 2 | Untersuchen | Das Rektorat durchsuchen |
| 3 | Rätsel | Venns Glyphenschrank öffnen |
| 4 | Entscheidung | Was in die Akte kommt |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=4 & Quest.SQ_132 & Quest.MQ_A2_07`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Venns Kindheit“ (TruthLevel 6); ITM_CON_SENSE ×2
**Folge:** Akte für den Bundesrat; Venn-Barks in Dorunsruh werden nachdenklicher

#### SQ_153 · Der Tikkel im Uhrwerk

*Echo-Geschichte · Akt II · Auftrag: Uhrmacher Odil (Säulenrast) · Intensität 2 · ~25 min*

Die alte dorunische Säulenuhr von Säulenrast tickt wieder – zum ersten Mal seit Jahrhunderten. Odil findet darin eine Tikkel-Familie, die die Zahnräder als Nest nutzt und bewegt. Er will die Uhr reparieren, ohne die Tikkels zu vertreiben.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Odil an der Säulenuhr |
| 2 | Beobachten | Tikkels im Uhrwerk beobachten |
| 3 | Rätsel | Zahnräder so setzen, dass Nest und Uhr laufen |

**Voraussetzung:** `Act>=Akt II`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · ITM_HELD_TAKTRING; Kodex-Beobachtung Tikkel
**Folge:** Die Säulenuhr schlägt die Stunden (Ambient, Säulenrast)

#### SQ_154 · Akten für den Bundesrat

*Fraktion · Akademie der Resonanz · Kette **Aevrins Akten** (4/4) · Akt II · Auftrag: Aevrin Thal (Dorunsruh) · Intensität 6 · ~60 min*

Aevrin legt die Akte über Venn dem Bundesrat vor – per Klangbrief aus Dorunsruh, mit dem Wärter als Zeugen. Die Räte streiten, ob die Akademie aufgelöst werden soll. Aevrin will nicht Venn retten, sondern die Akademie.

**Lösungen:** Auflösung empfehlen · Aufsicht durch den Bund · Akademie unter Aevrin mit offenen Archiven (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Aevrin vor der Sitzung |
| 2 | Entscheidung | Als Zeuge sprechen |
| 3 | Beobachten | Ein Thaelon im Sitzungssaal beobachten (Zeugenritual der Dorunier) |
| 4 | Entscheidung | Empfehlung an den Bundesrat |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Rank.F01>=4 & Quest.SQ_152 & Quest.MQ_A2_07`
**Belohnung:** 1.550 ◎ · 2.000 Wärter-EP · Ruf F01 +400 · Titel „Zeuge des Bundes“; ITM_GEAR_RESONATOR_4
**Folge:** Bundesrat stellt die Akademie unter Aufsicht (Nachhall: kommissarisch Aevrin, K47)

#### SQ_155 · Neumond der Skrivs

*Weltereignis · Akt II · Auftrag: Glyphenstudent Marek (Thae'Luun) · Intensität 3 · ~30 min*

Bei Neumond schreiben Skrivs leuchtende Glyphen in die Luft über Thae'Luun. Marek glaubt, sie schreiben ab – Glyphen von den Säulen. Der Wärter vergleicht und findet einen Fehler, den die Skrivs korrigieren.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Neumond |
| 2 | Beobachten | Skrivs beim Schreiben beobachten |
| 3 | Foto | Ein Skriveth-Zeichen fotografieren |
| 4 | Untersuchen | Die Glyphe mit der Säule vergleichen |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Moon=New`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · ITM_EVO_GLYPHSHARD; Kodex-Fragment „Skriv-Korrektur“
**Folge:** Neumond der Skrivs als Weltereignis (WE_SKRIV_NEWMOON)

#### SQ_156 · Studentenstreik

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Studentin Helke (Dorunsruh) · Intensität 4 · ~40 min*

In Akt III streiken die Studierenden der Akademie: Sie wollen offene Archive, ein Ethikgremium für Echo-Forschung und kein Wort mehr von „Ordnung“. Die Professorenschaft ist gespalten. Helke bittet den Wärter, mit beiden Seiten zu reden.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Helke auf der Mensatreppe |
| 2 | Sprechen | Professor Albrecht zuhören |
| 3 | Beobachten | Hymlits, die mit den Streikenden singen, beobachten |
| 4 | Entscheidung | Einen Kompromiss vorschlagen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_KS_064; Hain-Dekor ITM_DECO_STRIKEBANNER
**Folge:** Ethikgremium der Akademie (K47 Nachhall-Zustand)

#### SQ_157 · Glyphen-Übersetzung

*Rätsel & Ruinen · Akt II · Auftrag: Professor Thal (Sprechstunde) (Dorunsruh) · Intensität 4 · ~45 min*

Zehn Glyphentafeln, verteilt über Dorunsruh, Thae'Luun und das Archontenviertel, ergeben zusammen einen Text – die letzte Ansprache des Erstchors vor der Großen Stille. Aevrin übersetzt seit Jahren. Der Wärter findet die Tafeln; das Lesen gelingt erst mit dem Akkord von Dorunsruh.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Aevrins Sprechstunde |
| 2 | Rätsel | Zehn Glyphentafeln finden und abhören |
| 3 | Bedingung | Mit dem Akkord von Dorunsruh lesen |
| 4 | Untersuchen | Den Text zusammensetzen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A2_10`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Lore „Ansprache des Erstchors“ (TruthLevel 7); ITM_LURE_GLYPHTOKEN
**Folge:** Text in der Akademie-Bibliothek; Klangfragment wird entzerrt

#### SQ_158 · Kaels Forschungsarbeit

*Fraktion · Akademie der Resonanz · Akt II · Auftrag: Archivarin Pell (Dorunsruh) · Intensität 4 · ~40 min*

Kael hat in Dorunsruh an einer Arbeit geschrieben: „Hören ohne Gabe“. Vor dem Verrat bittet er den Wärter, Versuche zu bezeugen; danach findet Pell die halbfertige Arbeit in seinem verlassenen Labor und bittet den Wärter, sie zu lesen, bevor sie archiviert wird. Beide Fassungen enden mit derselben Frage.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Pell (vor W6: Kael selbst) im Labor |
| 2 | Beobachten | Kaels Hymnora-Versuche beobachten oder nachstellen |
| 3 | Untersuchen | Kaels Notizen lesen |
| 4 | Entscheidung | Kaels Frage beantworten: „Kann man lernen zu hören?“ |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_KS_066; Kodex-Fragment „Hören ohne Gabe“
**Folge:** Kaels Arbeit in der Bibliothek; KAEL_TRUST-Dialoge in Akt III erhalten einen Rückbezug

#### SQ_159 · Chronaires Uhr

*Rätsel & Ruinen · Nachhall · Auftrag: Uhrmacher Odil (Säulenrast) · Intensität 4 · ~40 min*

Im Nachhall läuft die Säulenuhr manchmal rückwärts – genau eine Minute, jeden Mittag. Odil hält es für einen Defekt. Der Wärter erkennt eine Spur: Chronaire, das Mythische der Zeit, prüft die, die es suchen, mit Zeitherausforderungen (K62).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Mittag an der Säulenuhr |
| 2 | Untersuchen | Die rückwärts laufende Minute untersuchen |
| 3 | Rätsel | In der rückwärts laufenden Minute die Glyphe setzen |
| 4 | Beobachten | Ein Flackern von Chronaire bemerken |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Chronaire (Gerücht); ITM_LURE_TUNINGFORK
**Folge:** Spur „Chronaire“ im Kodex aktiv (K62)

#### SQ_160 · Die Prüfung der Hörerin

*Fraktion · Akademie der Resonanz · Akt II · Auftrag: Tamsin (Hörerin) (Dorunsruh) · Intensität 3 · ~30 min*

Eine junge Hörerin, Tamsin aus Fennhaven (SQ_051), studiert jetzt in Dorunsruh – mit Stipendium der Wildwacht. Sie fürchtet ihre Kodex-Prüfung und bittet den Wärter, mit ihr zu üben: draußen, nicht im Hörsaal.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Tamsin vor der Prüfung |
| 2 | Beobachten | Mit Tamsin Thaelits beobachten |
| 3 | Foto | Ein Optil für Tamsins Arbeit fotografieren |
| 4 | Sprechen | Tamsin zur Prüfung bringen |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_07 & Quest.SQ_051`
**Belohnung:** 900 ◎ · 1.950 Wärter-EP · Ruf F01 +150 · ITM_GEAR_LENS_3; Kodex-Beobachtung Thaelit
**Folge:** Tamsin besteht; Bark-Kette über „die Hörerin aus dem Moor“

#### SQ_161 · Der Hehler

*Menschen · Akt II · Auftrag: Hehler Grave (Dorunsruh) · Intensität 4 · ~40 min*

Grave handelt mit Fundstücken aus den Ruinen – meist harmlos, manchmal nicht. Er bietet dem Wärter einen Klangsplitter-Ring an, der einem Sarkon gestohlen wurde, dessen Nest nun leer klingt. Grave sagt, er habe es ehrlich gekauft. Er lügt nicht ganz.

**Lösungen:** Ring kaufen und zurückbringen · Grave melden · Grave den Weg zeigen, den der Ring genommen hat, und ihn zum Rückgabeweg bewegen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Graves Angebot |
| 2 | Beobachten | Das Sarkon am leeren Nest beobachten |
| 3 | Untersuchen | Den Weg des Rings zurückverfolgen |
| 4 | Entscheidung | Was mit Grave und dem Ring geschieht |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · ITM_HELD_LASTBREATH; Kodex-Beobachtung Sarkon
**Folge:** Ring zurück im Nest; Grave handelt vorsichtiger (oder schließt)

#### SQ_162 · Venns leeres Zimmer

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Aevrin Thal (Dorunsruh) · Intensität 3 · ~30 min*

In Akt III bittet Aevrin den Wärter um etwas Seltsames: Venns privates Zimmer aufzuräumen, bevor die Studierenden es zum Gedenkraum für die Opfer der Siegelkriege machen. Es ist ein einfaches Zimmer. An der Wand: ein Brief an seine Eltern, nie abgeschickt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zu Venns Zimmer |
| 2 | Untersuchen | Das Zimmer ordnen |
| 3 | Entscheidung | Was mit dem Brief geschieht |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Kodex-Fragment „Ein Brief an die Eltern“
**Folge:** Gedenkraum der Siegelkriege in Dorunsruh; Venns Brief liegt aus, verbrannt oder ist im Epilog bei ihm

#### SQ_163 · Der Bruder, der spricht

*Menschen · Akt II · Auftrag: Bruder Odvar (Säulenrast) · Intensität 2 · ~25 min*

Bruder Odvar spricht außerhalb des Klosters, weil sein Gelübde nur innerhalb der Mauern gilt. Er sammelt Wörter, die Menschen nie mehr sagen – „weil man sie aufbewahren muss, wenn man schweigt“. Der Wärter hilft, drei solche Wörter zu finden.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Odvars Wortsammlung |
| 2 | Untersuchen | Drei vergessene Wörter in Inschriften und Gesprächen finden |
| 3 | Entscheidung | Ein eigenes Wort für Odvars Sammlung |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 800 ◎ · 1.700 Wärter-EP · Hain-Dekor ITM_DECO_WORDBOX; Kodex-Fragment „Odvars Wörter“
**Folge:** Odvar liest Besuchern die Wörter vor (Bark)

#### SQ_164 · Die große Stille am Archontenviertel

*Fraktion · Wildwacht · Akt II · Auftrag: Wildwächter Boaz (Archontenwacht) · Intensität 5 · ~45 min*

Die Archontenwacht bewacht die größte Stillezone des Kontinents. Nach der Heilung durch den Akkord bleibt ein Kern, den kein Wärter allein schließen kann. Boaz organisiert einen Heilkreis aus Wildwacht, Akademie und – auf Wunsch des Wärters – Ordensleuten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Boaz an der Wacht |
| 2 | Entscheidung | Wer in den Heilkreis kommt |
| 3 | Heilen | Vier Heilkreise im Archontenviertel schließen |
| 4 | Beobachten | Ein Sarkothar, das aus der Zone erwacht, beobachten |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_P03 & Quest.MQ_A2_09`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_RESONATOR_4; Titel „Kernheiler“
**Folge:** Archontenviertel als begehbare Ruine (Data Layer)

#### SQ_165 · Der Wächter ohne Splitter

*Forschung · Nachhall · Auftrag: Dr. Imke Vael (Thae'Luun) · Intensität 3 · ~35 min*

Im Nachhall steht Thaelarch noch immer vor dem leeren Thron. Imke Vael fragt, was ein Wächter tut, wenn es nichts mehr zu bewachen gibt. Der Wärter beobachtet ihn über drei Tage.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Thaelarch an drei Tagen beobachten |
| 2 | Untersuchen | Spuren seiner neuen Wege finden |
| 3 | Sprechen | Imke berichten |

**Voraussetzung:** `Act>=Nachhall`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Kodex-Fragment „Der Wächter ohne Splitter“; ITM_HELD_SHIELDBROOCH
**Folge:** Thaelarch bewacht nun den Gedenkraum oder die Kinder von Thae'Luun (Ambient)

#### SQ_166 · Gefangene Gelehrsamkeit

*Fraktion · Freie Stimmen · Akt II · Auftrag: Zelle Dorunsruh (Freie Stimmen) (Dorunsruh) · Intensität 5 · ~45 min*

Unter Venn liefen in einem Nebenlabor Versuche mit verstummten Echos. Nach dem Verrat ist das Labor versiegelt – mit den Echos darin. Die Freien Stimmen wollen einbrechen; Aevrin würde öffnen, braucht aber Tage für die Genehmigung.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Zelle in der Unterstadt von Dorunsruh |
| 2 | Entscheidung | Einbruch oder Genehmigung |
| 3 | Heilen | Drei verstummte Echos im Labor heilen |
| 4 | Beobachten | Ein Tilgel nach der Heilung beobachten |

**Voraussetzung:** `Act>=Akt II & Quest.MQ_A1_04 & Quest.MQ_A2_07`
**Belohnung:** 1.250 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_CON_CLEANSE ×3; Laborakte (Lore)
**Folge:** Labor wird Ruheort für Echos (Akademie, Nachhall)

#### SQ_167 · Die Bibliothek der Resonanz

*Forschung · Akt II · Auftrag: Dr. Imke Vael (Thae'Luun) · Intensität 3 · ~35 min*

Dr. Imke Vael, Nachfahrin des Taxonomen, baut in Thae'Luun eine „Bibliothek der Resonanz“: Klangproben aller Arten. Sie bittet um Proben aus drei Regionen und um Hilfe beim Katalog. Wer ihr hilft, erhält eine Kopie für den eigenen Kodex.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Imke in der Bibliothek |
| 2 | Beobachten | Klangprobe Skrivar |
| 3 | Beobachten | Klangprobe Menhirok |
| 4 | Rätsel | Proben katalogisieren |

**Voraussetzung:** `Act>=Akt II` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · Kodex-Funktion „Klangarchiv“ (Rufe aller registrierten Arten abspielbar); ITM_KS_067
**Folge:** Bibliothek der Resonanz in Thae'Luun (Lore-Sammelort)

#### SQ_168 · Hymnoras Chor

*Fraktion · Freie Stimmen · Akt III · Auftrag: Zelle Dorunsruh (Freie Stimmen) (Dorunsruh) · Intensität 4 · ~40 min*

In Akt III wollen die Freien Stimmen und die Studierenden einen Chor aus Hymnoras gründen, die freiwillig singen – als Gegenbild zum Krone-Motiv. Hymnoras singen aber nur zusammen, wenn sie einander kennen. Der Wärter bringt drei Gruppen zusammen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Drei Hymnora-Gruppen beobachten |
| 2 | Begleiten | Mit Helke die Gruppen zum Säulenfeld führen |
| 3 | Entscheidung | Das erste Lied wählen |
| 4 | Lager | Dem Chor zuhören |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_04` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · Hain-Dekor ITM_DECO_CHOIRSTONE; ITM_LURE_WINDCHIME
**Folge:** Freier Chor auf dem Säulenfeld (Ambient, Dämmerung)

#### SQ_169 · Glyphenduell

*Wärterprüfung · Akt II · Auftrag: Glyphenfechter Ivo (Dorunsruh) · Intensität 5 · ~35 min*

Im Glyphenhof fordert Ivo, Aevrins Assistent, zum Duell nach alter Regel: Jede Fähigkeit hinterlässt eine Glyphe, die in der nächsten Runde wirkt. Zwei Kämpfe; wer Glyphen liest, gewinnt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ivos Herausforderung |
| 2 | Kampf | Erstes Duell |
| 3 | Kampf | Aevrin selbst |
| 4 | Beobachten | Unter dem Glyphenhof lauschen (Ka'thurel) |

**Voraussetzung:** `Act>=Akt II & Akkorde>=7`
**Belohnung:** 1.050 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_ARCANE; ITM_KS_068
**Folge:** Glyphentraining im Hof

#### SQ_170 · Die Kapelle im Archontenviertel

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (2/6) · Nachhall · Auftrag: Schwester Ivra (Archontenwacht) · Intensität 3 · ~35 min*

Die zweite Station der Pause: Eine Ordenskapelle im Archontenviertel, in der die Stille seit dem Finale anders klingt. Ivra und Bruder Odvar warten dort mit einer Frage, die sie nicht aufschreiben wollen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Kapelle |
| 2 | Lager | Eine Stunde in der Kapelle |
| 3 | Beobachten | Ein Tilgrath, das in der Kapelle schläft, beobachten |
| 4 | Entscheidung | Ivras Frage beantworten |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2 & Quest.SQ_151`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · Kodex-Fragment „Orte der Pause II“
**Folge:** Kapelle als Ort der Pause

#### SQ_171 · Schatten zwischen den Säulen

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (3/6) · Nachhall · Auftrag: Schwester Ivra (Thae'Luun) · Intensität 4 · ~40 min*

Tilgels verschwinden im Nachhall zwischen den Säulen von Thae'Luun – nicht weg, sondern in die Pause zwischen zwei Säulen. Ivra glaubt, sie zeigen, wo man hören kann. Der Wärter folgt ihnen bei Nebel.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Nebel auf dem Säulenfeld |
| 2 | Beobachten | Tilgels zwischen den Säulen beobachten |
| 3 | Untersuchen | Die drei „stillen Lücken“ finden |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2 & Quest.SQ_170` · **Variante/Bedingung:** `Weather=Fog`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · Kodex-Fragment „Orte der Pause III“; ITM_TRAP_SHADE
**Folge:** Säulenfeld-Lücken als Ort der Pause

#### SQ_172 · Der Thron ohne Krone

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (4/6) · Nachhall · Auftrag: Schwester Ivra (Dorunsruh) · Intensität 4 · ~45 min*

Die vierte Station: der Thronsaal. Wo Maedryn die Krone aufsetzte und Ilen die Pause öffnete, ist es jetzt einfach still. Ka'thurel erinnert sich – und zeigt dem Wärter eine Erinnerung, die nicht Maedryn gehört, sondern einem einfachen Echo im Saal.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | In den Thronsaal |
| 2 | Lager | Stille am leeren Thron |
| 3 | Beobachten | Ka'thurels Erinnerung empfangen |
| 4 | Sprechen | Ivra davon erzählen |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2 & Quest.SQ_171`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · Kodex-Fragment „Orte der Pause IV“; Klangfragment „Das Echo im Saal“
**Folge:** Thronsaal als Ort der Pause


---

## 5. Prismtiefen (R09) – SQ_173–SQ_190

Unter der Erde zählt Licht. Die Energiekrise (CANON §54) prägt Akt III; im Nachhall messen Forscherinnen, wie der Missklang verheilt oder erstarrt. Ilyx und der Wärter teilen Brannocs Erbe; Brannoc der Ältere gründet eine Grubenwehr.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_173 | Labore im Krater | Fraktion | F01 | Akt III | 4 | 40 | – |
| SQ_174 | Spatlings im Dunkeln | Echo-Geschichte | – | Akt III | 2 | 25 | Time=Night |
| SQ_175 | Der Kristall, der zählt | Fraktion | F01 | Nachhall | 3 | 35 | – |
| SQ_176 | Kristallpuls-Nacht | Weltereignis | – | Akt III | 3 | 30 | Time=Night |
| SQ_177 | Psionits Traum | Fraktion | F01 | Akt III | 4 | 35 | Time=Night |
| SQ_178 | Spiegel ohne Bild | Rätsel & Ruinen | – | Nachhall | 3 | 35 | Time=Dusk |
| SQ_179 | Das Stimmer-Archiv | Fraktion | F01 | Akt III | 3 | 30 | – |
| SQ_180 | Die Stalakkord-Orgel | Rätsel & Ruinen | – | Akt III | 4 | 40 | – |
| SQ_181 | Kristallmarkt nach der Krise | Fraktion | F02 | Nachhall | 3 | 30 | – |
| SQ_182 | Brannocs Erbe | Menschen | – | Akt III | 4 | 45 | Time=Night |
| SQ_183 | Licht für die Oberwelt | Fraktion | F02 | Akt III | 4 | 40 | – |
| SQ_184 | Missklang verheilt | Forschung | – | Nachhall | 3 | 30 | Time=Night |
| SQ_185 | Glasbläser-Meisterwerk | Fraktion | F02 | Akt III | 4 | 45 | – |
| SQ_186 | Klirrathans Gesang | Forschung | – | Akt III | 3 | 30 | Time=Night |
| SQ_187 | Das Rettungsseil | Fraktion | F03 | Nachhall | 4 | 40 | – |
| SQ_188 | Ilyx' Brechungsprobe | Wärterprüfung | – | Akt III | 6 | 40 | – |
| SQ_189 | Verschüttete Stimmer | Fraktion | F03 | Akt III | 5 | 45 | – |
| SQ_190 | Die Pause im Kristall | Fraktion | F05 · FQ_F05_02 | Nachhall | 4 | 40 | – |

#### SQ_173 · Labore im Krater

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Laborleiterin Sanne (Akademie) (Prismara) · Intensität 4 · ~40 min*

Die Akademie-Labore in Prismara messen die Energiekrise. Sanne braucht Werte aus drei Tiefen, um zu zeigen, dass der Puls von den Missklang-Adern ausgeht – nicht, wie der Rat glaubt, von den Kristallmärkten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Sanne im Labor |
| 2 | Untersuchen | Messwerte in Glanzschacht, Quarzgrund und Kaverne nehmen |
| 3 | Beobachten | Misslits am Rand der Adern beobachten |
| 4 | Sprechen | Seren Quarz (Stimmergilde) die Werte zeigen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_GEAR_LENS_4; Kodex-Fragment „Puls“
**Folge:** Rat von Prismara verlagert Energie auf alte Lichtschächte

#### SQ_174 · Spatlings im Dunkeln

*Echo-Geschichte · Akt III · Auftrag: Schleiferin Nyx (Quarzgrund) · Intensität 2 · ~25 min*

In Quarzgrund, 310 Meter unter dem Kraterrand, ist es dunkel – Nyx schleift bei Spatling-Licht. Seit der Energiekrise leuchten die Spatlings schwächer. Nyx glaubt, sie hungern; der Wärter findet heraus, dass sie sich vor dem Puls verstecken.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Nyx in der Schleiferei |
| 2 | Beobachten | Spatlings im Dunkeln beobachten |
| 3 | Untersuchen | Ihre Verstecke finden |
| 4 | Entscheidung | Nyx einen Schutzraum vorschlagen |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.150 ◎ · 2.000 Wärter-EP · ITM_GEAR_LANTERN_4; Kodex-Beobachtung Spatling
**Folge:** Spatling-Schutzraum in Quarzgrund; Licht kehrt zurück

#### SQ_175 · Der Kristall, der zählt

*Fraktion · Akademie der Resonanz · Nachhall · Auftrag: Laborleiterin Sanne (Akademie) (Prismara) · Intensität 3 · ~35 min*

Im Nachhall misst Sanne, wie schnell die Missklang-Adern verheilen (Neues Lied) oder erstarren (Sanfte Stille). Sie hat einen Kristall gezüchtet, der zählt – jede Stunde ein Ton weniger Missklang.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Sannes Zählkristall |
| 2 | Untersuchen | Den Kristall an drei Adern ablesen |
| 3 | Beobachten | Einen ruhigen Missgrath beobachten |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A1_07`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Kodex-Fragment „Zählkristall“; ITM_MAT_GLYPHCRYSTAL ×2
**Folge:** Sannes Messreihe je Ende verschieden (Kodex)

#### SQ_176 · Kristallpuls-Nacht

*Weltereignis · Akt III · Auftrag: Seren Quarz (Stimmergilde) (Prismara) · Intensität 3 · ~30 min*

Prismaras Fest: In einer Nacht pro Monat lässt die Stimmergilde alle Kristalle der Stadt im selben Takt pulsieren. Wegen der Energiekrise wollen sie es absagen. Seren bittet den Wärter, einen Takt zu finden, der den Puls der Adern ausgleicht statt verstärkt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Nacht in Prismara |
| 2 | Beobachten | Den Stalakkord-Takt hören |
| 3 | Rätsel | Den Gegentakt setzen |
| 4 | Lager | Das Fest erleben |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_PULSECRYSTAL; ITM_LURE_STARCHIME
**Folge:** Kristallpuls-Nacht findet statt (Weltereignis WE_PULSE_NIGHT)

#### SQ_177 · Psionits Traum

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Seren Quarz (Stimmergilde) (Prismara) · Intensität 4 · ~35 min*

Psionits träumen laut: In ihrer Nähe sehen Menschen Bilder. Seren will der Akademie erlauben, die Bilder aufzuzeichnen; der Wärter fragt erst, ob die Psionits das wollen. Eine Beobachtung entscheidet, ob die Studie stattfindet.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Psionits beim Träumen beobachten |
| 2 | Untersuchen | Die Bilder deuten |
| 3 | Entscheidung | Seren raten |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_KS_071; Kodex-Beobachtung Psionit
**Folge:** Studie mit Einwilligungsregel (Ethikgremium SQ_156) oder abgebrochen

#### SQ_178 · Spiegel ohne Bild

*Rätsel & Ruinen · Nachhall · Auftrag: Glasbläserin Quill (Prismara) · Intensität 3 · ~35 min*

Quills Spiegel zeigen manchmal einen Schemen, der nicht im Raum ist. Im Nachhall häufen sich die Berichte. Der Wärter dokumentiert die Schemen – die ersten Spuren von Mirrowisp, die erst mit der Fotografie-Meisterschaft greifbar werden (K39 §6).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Quill und die Spiegel |
| 2 | Foto | Den Schemen in einem Spiegel fotografieren (nur im Album sichtbar) |
| 3 | Untersuchen | Drei weitere Spiegelorte prüfen |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Mirrowisp (Spur); ITM_LURE_MIRROR
**Folge:** Spur „Mirrowisp“ im Kodex (K39, K62)

#### SQ_179 · Das Stimmer-Archiv

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Stimmwerkstatt Brannoc (Prismara) · Intensität 3 · ~30 min*

Die Stimmwerkstatt hütet ein Archiv aller Stimmgabeln, die je in Prismara gefertigt wurden. Die Akademie will es digital – in Kristallabschriften – sichern. Der Werkstattmeister misstraut der Akademie. Der Wärter vermittelt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Der Werkstattmeister |
| 2 | Untersuchen | Das Archiv sichten |
| 3 | Beobachten | Ein Klirrflug beim Nachsingen der Gabeln beobachten |
| 4 | Entscheidung | Bedingungen für die Abschrift |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_LURE_TUNINGFORK; Rezept RCP_072
**Folge:** Archiv-Abschrift in der Akademie (oder nur in Prismara)

#### SQ_180 · Die Stalakkord-Orgel

*Rätsel & Ruinen · Akt III · Auftrag: Steiger Brannoc d. Ä. (Glanzschacht) · Intensität 4 · ~40 min*

Unter Glanzschacht liegt eine Höhle, deren Tropfsteine Stalakkords tragen. Der alte Steiger erzählt, dass man auf ihnen spielen kann – eine Orgel aus Echos. Wer das richtige Lied spielt, öffnet einen Gang zur Tiefen Resonanz.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Brannoc d. Ä. erzählt |
| 2 | Beobachten | Stalakkords bei der Antwort beobachten |
| 3 | Rätsel | Das Lied der Orgel spielen |
| 4 | Gehen | Den neuen Gang betreten |

**Voraussetzung:** `Act>=Akt III`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · ITM_KS_073; Abkürzung Glanzschacht–Tiefe Resonanz
**Folge:** Neuer Gang (Data Layer); Orgel spielbar

#### SQ_181 · Kristallmarkt nach der Krise

*Fraktion · Goldklang-Kontor · Nachhall · Auftrag: Kristallmarkt Seren (Prismara) · Intensität 3 · ~30 min*

Im Nachhall ist die Energiekrise vorbei, aber der Kristallmarkt erholt sich nicht: Händler aus Saltrand kaufen billig, weil Prismara Geld braucht. Seren will einen fairen Preis – mit Hilfe des Kontors, ausgerechnet.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Seren am Markt |
| 2 | Untersuchen | Die Preise vergleichen |
| 3 | Sprechen | Wiebke per Klangbrief einbeziehen |
| 4 | Entscheidung | Einen Preisrahmen vorschlagen |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A1_05`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_MAT_GLYPHCRYSTAL ×3; ITM_GEAR_BAG_4
**Folge:** Fairer Kristallpreis (Händlerpreise R09 stabil)

#### SQ_182 · Brannocs Erbe

*Menschen · Akt III · Auftrag: Ilyx Brannoc (Prismara) · Intensität 4 · ~45 min*

Ilyx ist ein Nachfahre der Lauscherin. Wer die Kette „Die Spur der Lauscherin“ abgeschlossen hat, bringt ihm deren Lied – das Ilyx nie ganz kannte. Ilyx und der Wärter sitzen eine Nacht neben einem Klirrathan, wie Brannoc 287 neben ihrem Echo saß.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ilyx in der Prismenhalle |
| 2 | Entscheidung | Brannocs Lied vorspielen (oder erzählen) |
| 3 | Gehen | In die Kaverne |
| 4 | Lager | Eine Nacht in Stille |
| 5 | Beobachten | Das Klirrathan, das sich nähert, beobachten |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Titel „Erbe der Lauscherin“; ITM_LURE_TUNINGFORK
**Folge:** Ilyx-Dialoge im Nachhall; Klirrathan erscheint häufiger in der Kaverne

#### SQ_183 · Licht für die Oberwelt

*Fraktion · Goldklang-Kontor · Akt III · Auftrag: Kontoragentin Rieke (Prismara) · Intensität 4 · ~40 min*

Die Energiekrise lässt nicht nur Prismara flackern – auch die Lichter in Städten an der Oberwelt, die Prismara-Kristalle nutzen. Das Kontor will Ersatzkristalle aus Ignareth bringen. Der Wärter organisiert Lieferung und Einbau.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Rieke im Kontor |
| 2 | Liefern | Ersatzkristalle aus Ignareth bringen |
| 3 | Beobachten | Facettors beim Ausrichten der Lichtschächte beobachten |
| 4 | Rätsel | Die Lichtschächte neu ausrichten |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_05`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_GEAR_LANTERN_4; ITM_CON_SENSE ×2
**Folge:** Lichter in Prismara und an der Oberwelt stabil (globales Flackern endet, Data Layer)

#### SQ_184 · Missklang verheilt

*Forschung · Nachhall · Auftrag: Laborleiterin Sanne (Akademie) (Prismara) · Intensität 3 · ~30 min*

Misslits waren Missklang-Kinder. Im Nachhall verändern sie sich: Im Neuen Lied werden sie heller, in der Sanften Stille stiller. Sanne bittet um eine letzte Beobachtungsreihe, bevor sie Prismara verlässt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Misslits an drei Tagen beobachten |
| 2 | Foto | Ein Foto für Sannes Abschied |
| 3 | Sprechen | Sanne verabschieden |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Kodex-Fragment „Missklang verheilt“; Hain-Dekor ITM_DECO_MISSLITLAMP
**Folge:** Kodex Misslit: Nachhall-Verhalten je Ende

#### SQ_185 · Glasbläser-Meisterwerk

*Fraktion · Goldklang-Kontor · Akt III · Auftrag: Glasbläserin Quill (Prismara) · Intensität 4 · ~45 min*

Quill will ein Meisterwerk blasen: eine Glasharfe, auf der jedes Echo spielen kann. Dafür braucht sie Zutaten aus vier Regionen und einen Wärter, der Crafting-Stufe V beherrscht – oder bereit ist, es bei ihr zu lernen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Quills Entwurf |
| 2 | Sammeln | Sonnenglas aus Sahrun |
| 3 | Sammeln | Gletscherquarz aus Hvitfell |
| 4 | Rätsel | Die Glasharfe stimmen |
| 5 | Beobachten | Ein Klirrathan auf der Harfe spielen hören |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_05`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · Rezept RCP_075 (Crafting V); Hain-Dekor ITM_DECO_GLASSHARP
**Folge:** Glasharfe im Kristallmarkt (spielbar)

#### SQ_186 · Klirrathans Gesang

*Forschung · Akt III · Auftrag: Meeresforscherin Liv (Kristallsee-Lager) · Intensität 3 · ~30 min*

Liv, die Aquadrals am Riff erforschte (SQ_083), ist nach Prismtiefen gekommen: Klirrathans singen am Kristallsee in Intervallen wie Aquadrals leuchten. Gibt es eine Verbindung zwischen Meer und Kristall?

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Liv am Kristallsee |
| 2 | Beobachten | Klirrathans nachts beobachten |
| 3 | Untersuchen | Intervalle mit Livs Riffdaten vergleichen |
| 4 | Entscheidung | Livs These bewerten |

**Voraussetzung:** `Act>=Akt III & Quest.SQ_083` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · ITM_KS_074; Kodex-Fragment „Mondzähler II“
**Folge:** Kodex verknüpft Aquadral und Klirrathan (Mondzähler)

#### SQ_187 · Das Rettungsseil

*Fraktion · Wildwacht · Nachhall · Auftrag: Steiger Brannoc d. Ä. (Glanzschacht) · Intensität 4 · ~40 min*

Im Nachhall gründet Brannoc d. Ä. eine Grubenwehr mit der Wildwacht. Die Übung: ein simulierter Einsturz in Glanzschacht, mit Mullhorns als Stützen und Ligravors, die Lasten schweben lassen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Brannocs Übungsplan |
| 2 | Beobachten | Mullhorns beim Stützen beobachten |
| 3 | Untersuchen | „Verschüttete“ mit Resonanzsinn finden |
| 4 | Begleiten | Die Übung abschließen |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_P03`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_TOOL_4; Wildwacht-Abzeichen „Grubenwehr“
**Folge:** Grubenwehr Glanzschacht (Barks, schnellere Rettung bei Ereignissen)

#### SQ_188 · Ilyx' Brechungsprobe

*Wärterprüfung · Akt III · Auftrag: Ilyx Brannoc (Prismara) · Intensität 6 · ~40 min*

Ilyx' Prismenhalle hat eine Brechungsregel: Fähigkeiten treffen gebrochen, ein Teil des Schadens geht auf das Nachbarziel. Die Probe besteht aus zwei Kämpfen und einem Rätsel, bei dem der Wärter Licht durch die Halle lenkt.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Kampf | Erste Brechung |
| 2 | Rätsel | Das Licht durch die Halle lenken |
| 3 | Kampf | Ilyx |
| 4 | Beobachten | Prism'aion lauschen |

**Voraussetzung:** `Act>=Akt III & Akkorde>=9`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_CRYSTAL; ITM_KS_075
**Folge:** Brechungstraining

#### SQ_189 · Verschüttete Stimmer

*Fraktion · Wildwacht · Akt III · Auftrag: Steiger Brannoc d. Ä. (Glanzschacht) · Intensität 5 · ~45 min*

Ein Puls der Missklang-Adern hat einen Stollen in Glanzschacht einstürzen lassen; drei Stimmer der Gilde und ihre Facetins sind eingeschlossen. Diesmal ist es keine Übung.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zum eingestürzten Stollen |
| 2 | Untersuchen | Die Eingeschlossenen orten |
| 3 | Traversal | Einen Rettungsgang graben |
| 4 | Begleiten | Die Stimmer herausführen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_P03`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_BOOTS_4; ITM_CON_HEAL_ALL ×2
**Folge:** Stollen gesichert; Stimmer-Barks

#### SQ_190 · Die Pause im Kristall

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (5/6) · Nachhall · Auftrag: Schwester Ivra (Prismara) · Intensität 4 · ~40 min*

Die fünfte Station: In der Resonanzkammer, wo der zehnte Splitter lag, ist eine Lücke im Kristall – genau in der Form des Splitters. Wer hineinhorcht, hört die Pause am deutlichsten.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | In die Resonanzkammer |
| 2 | Lager | Stille an der Lücke |
| 3 | Beobachten | Ein Klirrnox, das die Lücke umkreist, beobachten |
| 4 | Sprechen | Ivra berichten |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2 & Quest.SQ_172`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Ruf F05 +150 · Kodex-Fragment „Orte der Pause V“
**Folge:** Lücke im Kristall als Ort der Pause


---

## 6. Nimbara (R10) – SQ_191–SQ_210

Nimbara war tausend Jahre allein. Die Nebenquests öffnen es behutsam: ein Sternkatalog im Tausch, Wendelins letzter Stein als Brücke nach Eichenhall, ein gemeinsames Mahl gegen Vorurteile, die erste Luftfracht. Die letzte Nebenquest des Spiels, „Hüter der Pause“, führt an die Kronenwerft zurück – und in die Questreihe, die Velnox bindbar macht.

| ID | Titel | Kategorie | Fraktion/Kette | Verfügbar | Int. | Min | Bedingung |
|---|---|---|---|---|---|---|---|
| SQ_191 | Orumas Sternkatalog | Fraktion | F01 | Akt III | 3 | 35 | Time=Night |
| SQ_192 | Lumaskiffs Heimweg | Echo-Geschichte | – | Akt III | 3 | 30 | Weather=Thunderstorm |
| SQ_193 | Notizen von der Kronenwerft | Fraktion | F01 | Nachhall | 4 | 40 | – |
| SQ_194 | Gewitterharfe | Weltereignis | – | Akt III | 3 | 30 | Weather=Thunderstorm |
| SQ_195 | Das Archiv der Baumeister | Fraktion | F01 | Akt III | 3 | 35 | – |
| SQ_196 | Aurelunes Sturmnacht | Weltereignis | – | Nachhall | 5 | 45 | Weather=ResonanceStorm & Time=Night |
| SQ_197 | Wind gegen Fracht | Fraktion | F02 | Akt III | 3 | 30 | – |
| SQ_198 | Wendelins letzter Stein | Rätsel & Ruinen | – | Akt III | 4 | 45 | – |
| SQ_199 | Die erste Luftfracht | Fraktion | F02 | Nachhall | 4 | 45 | Weather=Thunderstorm |
| SQ_200 | Die Wand der Zehn | Rätsel & Ruinen | – | Akt III | 4 | 40 | – |
| SQ_201 | Inselendemiten | Fraktion | F03 | Akt III | 3 | 35 | Time=Day |
| SQ_202 | Letzte Bitten | Menschen | – | Akt III | 2 | 30 | Time=Dusk |
| SQ_203 | Graupel im Garten | Fraktion | F03 | Akt III | 3 | 30 | Weather=Thunderstorm |
| SQ_204 | Astraviels Sternbild | Forschung | – | Nachhall | 3 | 30 | Time=Night |
| SQ_205 | Wächter der Windstufen | Fraktion | F03 | Nachhall | 4 | 40 | – |
| SQ_206 | Windstrom-Rennen | Wärterprüfung | – | Akt III | 5 | 35 | Time=Day |
| SQ_207 | Bodenbewohner | Fraktion | F04 | Akt III | 4 | 40 | – |
| SQ_208 | Orumas Sternfall | Wärterprüfung | – | Nachhall | 6 | 45 | – |
| SQ_209 | Federn, die freiwillig fallen | Fraktion | F04 | Akt III | 3 | 30 | Time=Day |
| SQ_210 | Hüter der Pause | Fraktion | F05 · FQ_F05_02 | Nachhall | 6 | 60 | – |

#### SQ_191 · Orumas Sternkatalog

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Sternwärter Elun (Lumeya) (Sternwarte Oruma) · Intensität 3 · ~35 min*

Elun aus Lumeya führt die Sternwarte Oruma. Die Akademie will ihren Sternkatalog – Aerion hat 1.000 Jahre isoliert beobachtet. Elun ist bereit, wenn die Akademie im Gegenzug den Bodenkatalog teilt. Der Wärter überbringt und prüft.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Elun in der Sternwarte |
| 2 | Beobachten | Ein Astraviel bei Nacht beobachten |
| 3 | Liefern | Katalogabschrift ins Archiv der Baumeister bringen |
| 4 | Entscheidung | Tauschbedingungen festlegen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · ITM_LURE_STARCHIME; Kodex-Fragment „Himmel über Aerion“
**Folge:** Sternkatalog im Kodex (Himmelsereignisse vorhersagbar)

#### SQ_192 · Lumaskiffs Heimweg

*Echo-Geschichte · Akt III · Auftrag: Windseglerin Ria (Wolkenrast) · Intensität 3 · ~30 min*

Ein junges Lumaskiff hat im Gewitter die Windbänder verlassen und landet erschöpft in Wolkenrast. Ria kennt die Bänder; der Wärter kennt Echos. Gemeinsam bringen sie es zurück zu seinem Schwarm.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ria und das Lumaskiff |
| 2 | Beobachten | Das erschöpfte Lumaskiff beobachten |
| 3 | Traversal | In die Windbänder fliegen |
| 4 | Begleiten | Das Lumaskiff zum Schwarm führen |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · ITM_GEAR_GLIDER_4; Kodex-Beobachtung Lumaskiff
**Folge:** Lumaskiff-Schwarm sichtbar über Wolkenrast

#### SQ_193 · Notizen von der Kronenwerft

*Fraktion · Akademie der Resonanz · Nachhall · Auftrag: Aevrin Thal (Kronenwerft-Wacht) · Intensität 4 · ~40 min*

Im Nachhall sammelt Aevrin für die Akademie Venns Arbeitsnotizen von der Kronenwerft. Viele sind verweht. Der Wärter findet sie zwischen den Steinen – und eine, die Venn nach dem Finale geschrieben haben muss.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Kronenwerft |
| 2 | Untersuchen | Verwehte Notizen finden |
| 3 | Beobachten | Kronvaal, das zurückgekehrt ist, beobachten |
| 4 | Sprechen | Aevrin die Notizen per Klangbrief senden |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A1_07`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Venns letzte Notiz“ (TruthLevel 9); ITM_GEAR_RESONATOR_5
**Folge:** Notizen in der Akademie; Venn-Epilog erhält Rückbezug

#### SQ_194 · Gewitterharfe

*Weltereignis · Akt III · Auftrag: Windhändlerin Aelia (Aerion) · Intensität 3 · ~30 min*

Bei Gewitter spielen Harfions auf den Spannseilen der Windanker – eine Harfe aus Sturm. Aelia sagt, früher hätten die Baumeister dazu getanzt, bis die Isolation das Fest vergessen ließ. Der Wärter bringt das Fest zurück.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Gewitter über Nimbara |
| 2 | Beobachten | Harfions an den Seilen beobachten |
| 3 | Rätsel | Die Seile stimmen |
| 4 | Lager | Das Gewitterfest |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_STORMHARP; ITM_LURE_WINDCHIME
**Folge:** Gewitterharfe als Weltereignis (WE_STORM_HARP)

#### SQ_195 · Das Archiv der Baumeister

*Fraktion · Akademie der Resonanz · Akt III · Auftrag: Archivar der Baumeister (Aerion) · Intensität 3 · ~35 min*

Das Archiv der Baumeister ist älter als die Akademie. Die Baumeister misstrauen der Akademie – sie kennen Maedryn. Der Archivar zeigt dem Wärter Pläne der Kronenwerft, damit „jemand vom Boden versteht, warum wir schweigen“.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Der Archivar |
| 2 | Untersuchen | Pläne der Kronenwerft studieren |
| 3 | Beobachten | Ein Levithar, das die Archivbücher schweben lässt, beobachten |
| 4 | Entscheidung | Was die Akademie erfahren darf |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_07 & Quest.MQ_A3_02`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · Ruf F01 +150 · Lore „Kronenwerft-Pläne“ (TruthLevel 8); ITM_KS_077
**Folge:** Archiv teilweise offen für die Akademie (Nachhall)

#### SQ_196 · Aurelunes Sturmnacht

*Weltereignis · Nachhall · Auftrag: Sternwärter Elun (Lumeya) (Lumeya) · Intensität 5 · ~45 min*

Im Nachhall sieht Elun in Resonanzsturm-Nächten ein Licht, das zugleich Leere ist, über Lumeya. Er glaubt an Aurelune. Der Wärter wartet mit ihm – ein Sturm muss kommen, natürlich oder mit der Sturmstimmgabel (CANON §63).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Bedingung | Resonanzsturm bei Nacht |
| 2 | Beobachten | Aurelunes Licht beobachten (Spur) |
| 3 | Foto | Ein Foto der Erscheinung |
| 4 | Sprechen | Elun berichten |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Weather=ResonanceStorm & Time=Night`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · Kodex-Eintrag Aurelune (Spur); ITM_LURE_AURORAGLASS
**Folge:** Spur „Aurelune“ im Kodex (K62)

#### SQ_197 · Wind gegen Fracht

*Fraktion · Goldklang-Kontor · Akt III · Auftrag: Windhändlerin Aelia (Aerion) · Intensität 3 · ~30 min*

Aelia handelt zwischen den Inseln mit Windkarten. Das Kontor will ihre Karten für die Luftfracht kaufen. Aelia will nicht verkaufen, sondern teilen – gegen einen Sitz im Frachtrat.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Aelias Bedingung |
| 2 | Sprechen | Rieke (Kontor) zuhören |
| 3 | Beobachten | Cirrels auf den Windkarten-Routen beobachten |
| 4 | Entscheidung | Vermitteln |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_05`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · ITM_GEAR_GLIDER_4; Windkarte (Lore)
**Folge:** Frachtrat mit Aelia; Luftfracht-Routen (SQ_199)

#### SQ_198 · Wendelins letzter Stein

*Rätsel & Ruinen · Akt III · Auftrag: Archivar der Baumeister (Aerion) · Intensität 4 · ~45 min*

In Aerion steht ein erloschener Resonanzstein, den Wendelin Aar 880 mit den Hütern setzte – die einzige Verbindung zum Boden. Der Archivar zeigt, wo er steht. Ihn zu reaktivieren verbindet Aerion mit Eichenhall (K12 §5) – und ist Wendelins letzte Seite.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Untersuchen | Den erloschenen Stein und Wendelins Zeichen finden |
| 2 | Rätsel | Den Stein mit den Akkorden stimmen |
| 3 | Beobachten | Aeth'rion antwortet dem Stein |
| 4 | Gehen | Erste Reise von Aerion nach Eichenhall |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A3_06`
**Belohnung:** 1.800 ◎ · 2.000 Wärter-EP · Wendelin-Tagebuch (letzte Seite); Schnellreise Aerion ↔ Eichenhall
**Folge:** Resonanzstein aktiv; Wendelin-Sammlung vollständig (K39)

#### SQ_199 · Die erste Luftfracht

*Fraktion · Goldklang-Kontor · Nachhall · Auftrag: Marieke Holm (Windanker) · Intensität 4 · ~45 min*

Im Nachhall eröffnet Marieke die Luftfracht zwischen Boden und Nimbara. Der erste Flug trägt Saatgut, Bücher und einen Brief von Ysolde an die Baumeister. Ein Sturm, eine nervöse Mannschaft und Aelias Windkarten – der Wärter fliegt mit.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Marieke an den Windankern |
| 2 | Traversal | Den Frachtsegler eskortieren |
| 3 | Beobachten | Nimbaroths, die den Segler stützen, beobachten |
| 4 | Liefern | Ysoldes Brief übergeben |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A1_05` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · Ruf F02 +150 · Titel „Frachtpate“; ITM_GEAR_BAG_5
**Folge:** Luftfracht-Route aktiv (Händlersortimente R10 +4)

#### SQ_200 · Die Wand der Zehn

*Rätsel & Ruinen · Akt III · Auftrag: Hüterin Oruma (Aerion) · Intensität 4 · ~40 min*

Auf der Wand der Zehn ist nur Ilens Gesicht erhalten. Oruma will die anderen neun nicht erfinden – aber vielleicht erinnern sich die Stimmen. Mit jedem Akkord-Klang zeigt das Relief einen Schatten eines Gesichts.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Oruma vor der Wand |
| 2 | Rätsel | Neun Akkorde an der Wand anschlagen |
| 3 | Untersuchen | Die Schatten der Gesichter deuten |
| 4 | Entscheidung | Ob die Gesichter nachgemeißelt werden |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A3_06`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Kodex-Eintrag „Der Erstchor“; Hain-Dekor ITM_DECO_WALLOFTEN
**Folge:** Wand der Zehn mit Schattenrelief (Data Layer)

#### SQ_201 · Inselendemiten

*Fraktion · Wildwacht · Akt III · Auftrag: Wildwächter Boaz (Lumeya) · Intensität 3 · ~35 min*

Die Wildwacht hat zum ersten Mal Kontakt nach Nimbara. Boaz will wissen, welche Arten nur hier leben und ob sie Schutz brauchen. Elun aus Lumeya hilft; die Baumeister sind skeptisch, bis sie sehen, dass niemand etwas mitnehmen will.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Boaz in Lumeya |
| 2 | Beobachten | Holmels auf ihren Inseln beobachten |
| 3 | Beobachten | Cirrhavens in den Gärten beobachten |
| 4 | Foto | Ein Nubiluna fotografieren |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_P03` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_LENS_4; Wildwacht-Abzeichen „Himmelswacht“
**Folge:** Schutzgebiete auf zwei Inseln (Kodex-Markierung)

#### SQ_202 · Letzte Bitten

*Menschen · Akt III · Auftrag: Ysolde Varn (Lumeya) · Intensität 2 · ~30 min*

Vor dem Aufbruch zur Kronenwerft bittet Ysolde den Wärter um einen Spaziergang. Unterwegs: drei kleine Bitten von Menschen, die er unterwegs getroffen hat – ein Brief, ein Lied, ein Versprechen. Ein Atemzug vor dem Finale (DR-29).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Ysoldes Bitte |
| 2 | Liefern | Einen Brief nach Wolkenrast bringen |
| 3 | Beobachten | Tintels in der Dämmerung singen hören |
| 4 | Entscheidung | Ysolde ein Versprechen geben |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A3_05` · **Variante/Bedingung:** `Time=Dusk`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Hain-Dekor ITM_DECO_LASTREQUEST; YSOLDE_BOND +1 (einfühlsam)
**Folge:** Ysolde erwähnt das Versprechen im Brief (K46 §8.4)

#### SQ_203 · Graupel im Garten

*Fraktion · Wildwacht · Akt III · Auftrag: Gärtnerin Sola (Aerion) (Aerion) · Intensität 3 · ~30 min*

In den Gärten von Aerion fällt Graupel bei Gewitter – und Graupix fressen die jungen Wolkenfrüchte. Sola will Netze spannen. Die Wildwacht schlägt etwas anderes vor: Graupix lieben Kälte, nicht Früchte.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Solas Gärten |
| 2 | Beobachten | Graupix bei Gewitter beobachten |
| 3 | Untersuchen | Herausfinden, was die Graupix wirklich anlockt |
| 4 | Entscheidung | Sola eine Lösung zeigen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_P03` · **Variante/Bedingung:** `Weather=Thunderstorm`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_FOOD_CLOUDFRUIT ×5; ITM_TRAP_WARM
**Folge:** Kühlbecken für Graupix, Wolkenfrüchte geschützt

#### SQ_204 · Astraviels Sternbild

*Forschung · Nachhall · Auftrag: Sternwärter Elun (Lumeya) (Sternwarte Oruma) · Intensität 3 · ~30 min*

Im Nachhall fliegen Astraviels in Formationen, die Sternbildern gleichen – aber einem, das es nicht gibt. Elun glaubt, sie zeichnen ein neues: die Stimmen, so wie sie jetzt sind.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Astraviel-Formationen an drei Nächten |
| 2 | Untersuchen | Mit dem Sternkatalog vergleichen |
| 3 | Entscheidung | Dem Sternbild einen Namen geben |

**Voraussetzung:** `Act>=Nachhall` · **Variante/Bedingung:** `Time=Night`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Kodex-Fragment „Das neue Sternbild“; Hain-Dekor ITM_DECO_STARCHART
**Folge:** Neues Sternbild am Nachthimmel (Name je Wahl)

#### SQ_205 · Wächter der Windstufen

*Fraktion · Wildwacht · Nachhall · Auftrag: Wildwächter Boaz (Windanker) · Intensität 4 · ~40 min*

Im Nachhall richtet die Wildwacht an den Windstufen eine Wache ein. Nimbors nisten an den Ankerseilen; jede Wartung stört sie. Boaz will einen Wartungsplan, der Brutzeiten respektiert.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Beobachten | Nimbor-Nester an den Ankern beobachten |
| 2 | Untersuchen | Wartungsbücher prüfen |
| 3 | Traversal | Die Seile aus der Luft prüfen |
| 4 | Entscheidung | Wartungsplan vorschlagen |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_P03`
**Belohnung:** 2.000 ◎ · 2.000 Wärter-EP · Ruf F03 +150 · ITM_GEAR_CLOAK_5; Titel „Windwacht“
**Folge:** Wartungskalender (Nimbor-Population stabil)

#### SQ_206 · Windstrom-Rennen

*Wärterprüfung · Akt III · Auftrag: Windseglerin Ria (Wolkenrast) · Intensität 5 · ~35 min*

Ria veranstaltet das Windstrom-Rennen zwischen den Inseln. Teilnehmer fliegen auf Echos durch die Windbänder; wer zuerst die Sternwarte erreicht, gewinnt. Zwischendurch: zwei Wärterkämpfe auf schwebenden Plattformen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Rias Rennen |
| 2 | Traversal | Durch die Windbänder |
| 3 | Kampf | Kampf auf der ersten Plattform |
| 4 | Kampf | Ria an der Sternwarte |
| 5 | Beobachten | Rias Cirrhaven nach dem Rennen beobachten |

**Voraussetzung:** `Act>=Akt III` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 1.500 ◎ · 2.000 Wärter-EP · ITM_HELD_SWIFTFEATHER; Hain-Dekor ITM_DECO_RACEPENNANT
**Folge:** Windstrom-Rennen als Weltereignis (WE_WIND_RACE)

#### SQ_207 · Bodenbewohner

*Fraktion · Freie Stimmen · Akt III · Auftrag: Freie Stimmen (Windanker) (Aerion) · Intensität 4 · ~40 min*

Die Baumeister nennen Menschen vom Boden „Bodenbewohner“ – nicht freundlich. Ein Baumeisterkind hat Angst vor den Freien Stimmen an den Windankern. Die Freien Stimmen wollen kein Misstrauen säen. Der Wärter bringt beide Seiten an einen Tisch – und die Echos an denselben Brunnen.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Die Freien Stimmen an den Ankern |
| 2 | Sprechen | Baumeisterin Iris zuhören |
| 3 | Beobachten | Nubis und Boden-Echos am Brunnen beobachten |
| 4 | Entscheidung | Ein gemeinsames Mahl vorschlagen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_04 & Quest.MQ_A3_05`
**Belohnung:** 1.650 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_FOOD_CLOUDFRUIT ×3; Hain-Dekor ITM_DECO_SKYTABLE
**Folge:** Gemeinsames Mahl in Aerion (Barks ändern sich: „Bodenleute“ statt „Bodenbewohner“)

#### SQ_208 · Orumas Sternfall

*Wärterprüfung · Nachhall · Auftrag: Oruma Siyel (Aerion) · Intensität 6 · ~45 min*

Im Nachhall lädt Oruma zur Sternfallprobe in der Sternenarena: Jeder dritte Zug fällt ein Stern auf ein zufälliges, aber vorher angezeigtes Feld (DR-07). Drei Kämpfe; der letzte gegen Oruma mit Aeth'rion als Zuschauer.

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Kampf | Erster Sternfall |
| 2 | Kampf | Zweiter Sternfall |
| 3 | Kampf | Oruma |
| 4 | Beobachten | Aeth'rion beobachten |

**Voraussetzung:** `Act>=Nachhall`
**Belohnung:** 2.200 ◎ · 2.000 Wärter-EP · ITM_HELD_TONE_SOUND; Titel „Sternfallgast“
**Folge:** Oruma-Barks im Nachhall

#### SQ_209 · Federn, die freiwillig fallen

*Fraktion · Freie Stimmen · Akt III · Auftrag: Federschneider Brisk (Aerion) · Intensität 3 · ~30 min*

Brisk schneidet Federkiele aus Cirrhawk-Federn. Die Freien Stimmen werfen ihm vor, Federn zu rupfen. Brisk schwört, er sammle nur gemauserte. Der Wärter beobachtet die Cirrhawks bei der Mauser – und Brisks Lieferanten.

**Lösungen:** Brisk entlasten · Lieferanten melden · ein Mausersiegel einführen, das alle drei Seiten prüfen (dritte Lösung).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Sprechen | Brisk in der Federschneiderei |
| 2 | Beobachten | Cirrhawks bei der Mauser beobachten |
| 3 | Untersuchen | Brisks Lieferanten folgen |
| 4 | Entscheidung | Ergebnis: Brisk, Lieferant, Freie Stimmen |

**Voraussetzung:** `Act>=Akt III & Quest.MQ_A1_04` · **Variante/Bedingung:** `Time=Day`
**Belohnung:** 1.350 ◎ · 2.000 Wärter-EP · Ruf F04 +150 · ITM_HELD_SWIFTFEATHER; ITM_MAT_FERNFIBER ×3
**Folge:** Federn mit Mausersiegel (Händler-Kennzeichnung)

#### SQ_210 · Hüter der Pause

*Fraktion · Orden der Stille · Kette **Hüter der Pause** (6/6) · Nachhall · Auftrag: Schwester Ivra (Kronenwerft-Wacht) · Intensität 6 · ~60 min*

Die sechste und letzte Station: die Kronenwerft, wo Velnox frei wurde und zurückkehrte. Ivra, Ulrek, Sereth (je nach Epilog), Ysolde und Bruder Odvar stehen im Kreis. Wer alle Orte der Pause gehört hat, wird zum Hüter – und hört zum ersten Mal Velnox selbst, wie er zwischen zwei Tönen atmet. Der Beginn von „Die Pause hören“ (K62).

| # | Ziel | Was ich tun soll |
|---|---|---|
| 1 | Gehen | Zur Kronenwerft |
| 2 | Lager | Im Kreis schweigen |
| 3 | Beobachten | Velnox' Atem zwischen zwei Tönen hören |
| 4 | Entscheidung | Das Gelöbnis der Hüter sprechen (oder nur zuhören) |

**Voraussetzung:** `Act>=Nachhall & Quest.MQ_A2_07 & Rank.F05>=2 & Quest.SQ_190`
**Belohnung:** 2.800 ◎ · 2.000 Wärter-EP · Ruf F05 +400 · Titel „Hüter der Pause“ (K47 F05 Rang 6 verstärkt); Hain-Dekor ITM_DECO_PAUSEBELL
**Folge:** Questreihe „Die Pause hören“ (Velnox-Bindung, K62) beginnt


---

## 7. Die Orte der Pause

Die Ordenskette *Hüter der Pause* (FQ_F05_02, Nachhall) besucht sechs Orte, an denen die Pause hörbar ist – dort, wo Velnox den Riegel berührte oder die Krone sang. Jeder Ort ist danach ein Rückkehrort mit eigenem Ambient (eine Sekunde völlige Stille in festem Takt, K55).

| Station | Quest | Ort | Echo der Pause |
|---|---|---|---|
| I | SQ_151 | Gletscherspalte, Hvitfell | Tysvorn (ruhig) |
| II | SQ_170 | Ordenskapelle, Archontenviertel | Tilgrath |
| III | SQ_171 | Lücken im Säulenfeld, Thae'Luun | Tilgel |
| IV | SQ_172 | Thronsaal des Maedryn | Ka'thurel (Erinnerung) |
| V | SQ_190 | Lücke in der Resonanzkammer, Prismara | Klirrnox |
| VI | SQ_210 | Kronenwerft, Nimbara | Velnox |

Die Kette beginnt mit Rang 2 beim Orden (K47) und endet mit dem Titel „Hüter der Pause“ – derselbe Titel, den Rang 6 verleiht (K47 `RW_F05_6`). Wer beides erreicht, erhält keinen doppelten Titel, sondern eine goldene Variante des Abzeichens (kosmetisch).

---

## 8. Alle 210 Nebenquests im Überblick

| Kennzahl | Wert |
|---|---|
| Quests | 210 |
| Schritte | 849 (Ø 4,0) |
| Ø Dauer | 36 min |
| Σ Spielzeit | 126,3 h |
| Mit Tageszeit/Wetter/Mond/Bedingung | 110 (52 %) |
| Σ Sol | 232.200 ◎ |
| Σ Wärter-EP | 389.200 |
| Kategorien | Fraktion 120, Rätsel & Ruinen 17, Forschung 16, Echo-Geschichte 15, Weltereignis 14, Menschen 14, Wärterprüfung 14 |
| Häufigste Zieltypen | Sprechen 183, Beobachten 174, Untersuchen 113, Entscheidung 111, Gehen 44, Bedingung 37, Kampf 37, Rätsel 30 |

### 8.1 Alle Fraktionsketten

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
| FQ_F03_04 | F03 | Rang 4 | Die stillen Ränder | **SQ_053**, **SQ_084**, **SQ_086**, **SQ_107** |
| FQ_F04_02 | F04 | Rang 2 | Unterstadt | **SQ_055**, **SQ_057**, **SQ_059**, **SQ_061** |
| FQ_F04_03 | F04 | Rang 3 | Netze im Nebel | **SQ_063**, **SQ_065**, **SQ_088**, **SQ_089** |
| FQ_F05_01 | F05 | Rang 1 | Das Schweigen lernen | **SQ_066**, **SQ_067**, **SQ_144**, **SQ_146**, **SQ_148**, **SQ_150** |
| FQ_F02_03 | F02 | Rang 3 | Hafenbücher | **SQ_072**, **SQ_074**, **SQ_076**, **SQ_078** |
| FQ_F02_04 | F02 | Rang 4 | Die gläserne Route | **SQ_080**, **SQ_082**, **SQ_101**, **SQ_103** |
| FQ_F04_04 | F04 | Rang 4 | Salz und Freiheit | **SQ_090**, **SQ_109**, **SQ_110**, **SQ_111** |
| FQ_F01_03 | F01 | Rang 3 | Glas der Hochkultur | **SQ_091**, **SQ_093**, **SQ_095**, **SQ_097** |
| FQ_F01_04 | F01 | Rang 4 | Aevrins Akten | **SQ_099**, **SQ_132**, **SQ_152**, **SQ_154** |
| FQ_F05_02 | F05 | Rang 2 | Hüter der Pause | **SQ_151**, **SQ_170**, **SQ_171**, **SQ_172**, **SQ_190**, **SQ_210** |

### 8.2 Regionen

| Region | Quests | Kapitel | Später verfügbar |
|---|---|---|---|
| Verdanthain | 24 | K49 | 3 |
| Kharsgrat | 22 | K49 | 3 |
| Morvenmoor | 21 | K49 | 5 |
| Saltrand | 23 | K49/K50 | 3 |
| Sahrun-Weite | 22 | K50 | 3 |
| Ignareth | 19 | K50 | 6 |
| Hvitfell | 20 | K50/K51 | 9 |
| Ael'Dorun | 21 | K51 | 8 |
| Prismtiefen | 18 | K51 | 6 |
| Nimbara | 20 | K51 | 7 |
| **Summe** | **210** | | **53** |

### 8.3 Spielzeit

Bei Ø ~36 min ergeben alle 210 Nebenquests ~126 Spielstunden (Ziel Ø 35 min, K48 §2 ✓). Zusammen mit der Hauptstory (~51 h typisch) und Aufträgen, Kodex und Zucht liegt ein vollständiger Durchgang bei 180–220 h (K01 §7.4 „Vollständig“) ✓; das Standard-Completionist-Profil (50 % Nebenquests) erreicht 80–110 h ✓.

**Wärter-EP:** Alle Nebenquests zusammen geben ~389.000 Wärter-EP – mehr als die Rang-40-Schwelle (188.000, K43). Das ist beabsichtigt: Wer alles spielt, erreicht Rang 40 lange vor dem Ende des Inhalts; Wärter-EP über Rang 40 haben keine mechanische Wirkung mehr (nur Statistik, K54). Die Story-Phase bleibt durch die typische Auswahl (~14 Nebenquests bis Akt III) im Zielband (K48 §8.1); Feinabstimmung in K63.

---

## 9. Abgleich mit den Haken aus K11–K13

K11 und K12 nannten je Stadt „Nebenquest-Haken“, K13 (CANON §57) Schlüssel-NPCs und Haken je Dorf. K49–K51 setzen sie wie folgt um. Wo ein Haken als eigene Quest umgesetzt ist, trägt die Quest seinen Titel (in K49/K50 nachgezogen: SQ_033, SQ_036, SQ_049, SQ_054, SQ_085, SQ_098, SQ_100, SQ_119, SQ_120, SQ_135); wo nicht, ist er als Sammelreihe, Weltereignis oder Teil einer anderen Quest realisiert (CR-005).

### 9.1 Städte

| Stadt | Haken (K11/K12) | Umsetzung |
|---|---|---|
| Eichenhall | „Der Lindentisch“ (Bundesgeschichte) | SQ_154 (Bundesrat, Zeugenrolle) und Weltereignis Lindenfest (CANON §52) |
| Eichenhall | „Wurzelpfade“ (Kletter-Sammlung) | Sammelreihe der Kodex-Aufgaben R01 (K39), keine eigene SQ |
| Eichenhall | „Das Echo im Harzfass“ | SQ_005 „Das Echo der Außenstelle“ (Lumow-Sammler) – gleiche Prämisse, verlegt in die Außenstelle |
| Eichenhall | Fotowettbewerb der Akademie-Außenstelle | SQ_003 (Foto-Schritt) und Foto-Aufträge CT_PHOTO |
| Kharsholm | „Die Schuld der Lastzüge“ | SQ_036 |
| Kharsholm | „Drei Klans, ein Gipfel“ (Klan-Wettkampf) | SQ_042 „Die Probe der Ahnen“ (Brückenprobe der Klans) |
| Kharsholm | „Verschüttet“ (Minenrettung) | SQ_033 |
| Morvenfurt | „Zwei Seiten des Kanals“ (Kontor vs. Freie Stimmen) | SQ_055 / SQ_057 (Unterstadt) – Entscheidung ohne Ausschluss (K47 §7) |
| Morvenfurt | „Irrlichtjagd“ | SQ_049 |
| Morvenfurt | „Der Fährmeister und das Turmgeheimnis“ | SQ_054 „Das Turmgeheimnis der Fährmeisterin“ (Ailsa Duvreth, CANON §52) |
| Morvenfurt | „Laternen für die Toten“ | SQ_048 (Laternensteg) und SQ_059 (Laternen, Irrlits) |
| Qasr Sahrun | „Das Gastrecht“ (Kette, 4 Teile) | Kette FQ_F04_04 „Salz und Freiheit“ (Gastrecht der Oase als Motiv in SQ_109–111) |
| Qasr Sahrun | „Glas aus Licht“ (Glasbläser-Wettbewerb) | SQ_101 (Glasbläserei Tavi) und SQ_185 (Meisterwerk) |
| Qasr Sahrun | „Harun und der Neumond“ | SQ_100 |
| Qasr Sahrun | „Die verirrte Karawane“ | SQ_098 |
| Saltrand-Hafen | „Die goldene Glocke schweigt“ | SQ_071 (Leuchtfelsen-Chor) und Weltereignis Glockenflut (CANON §52) |
| Saltrand-Hafen | „Schmugglerkeller“ (Ebbe) | SQ_076 / SQ_089 (Lager im Kliffsund) |
| Saltrand-Hafen | „Bekes Wetten“ | SQ_085 |
| Saltrand-Hafen | „Flaschenpost“ (Sammelreihe, Lore) | Lore-Sammelreihe (K39, `LoreEntries.csv`), keine eigene SQ |
| Schlackenwehr | „Das Gelübde der Zunft“ | SQ_119 |
| Schlackenwehr | „Sechs Glocken“ (Sammelquest) | SQ_116 (Glockenguss) + Schmiedeglocken als Kodex-Aufgabe |
| Schlackenwehr | „Lavawächter in Not“ | SQ_120 |
| Schlackenwehr | „Echos in den Minen“ (Freie Stimmen vs. Kontor) | SQ_131 / SQ_129 (Zelle Schlackenwehr) |
| Hvitmark | „Namen auf dem Stein“ | SQ_135 |
| Hvitmark | „Thing-Streit“ | SQ_141 |
| Hvitmark | „Eiðvik-Neu baut auf“ | SQ_143 |
| Hvitmark | „Aurora-Fotografie“ | SQ_147 |
| Dorunsruh | „Glyphen-Übersetzung“ (10-teilige Rätselkette) | SQ_157 (zehn Tafeln als Zählschritt) |
| Dorunsruh | „Der Hehler“ | SQ_161 |
| Dorunsruh | „Kaels Forschungsarbeit“ | SQ_158 (vor und nach W6 spielbar) |
| Dorunsruh | „Die Bibliothek der Resonanz“ | SQ_167 |
| Dorunsruh | „Studentenstreik“ | SQ_156 |
| Prismara | „Licht für die Oberwelt“ | SQ_183 |
| Prismara | „Verschüttete Stimmer“ | SQ_189 |
| Prismara | „Brannocs Erbe“ | SQ_182 |
| Prismara | „Glasbläser-Meisterwerk“ | SQ_185 |
| Aerion | „Bodenbewohner“ | SQ_207 |
| Aerion | „Inselendemiten“ | SQ_201 |
| Aerion | „Windstrom-Rennen“ | SQ_206 |
| Aerion | „Wendelins letzter Stein“ | SQ_198 |
| Aerion | „Letzte Bitten“ | SQ_202 |

### 9.2 Dörfer (CANON §57)

| Dorf | Schlüssel-NPC / Haken (CANON §57) | Nebenquests |
|---|---|---|
| Lindwiesen | Ysolde, Bäckerin Hedda, Müller Jost | SQ_002, SQ_012, SQ_007 (Imkerin Hilde) |
| Moosgrund | Köhlerin Brida; Pilzringe | SQ_022–024 (Kurierin Ennis), SQ_008 |
| Brakkfels | Ulf Brakk; Lorenlauf/Minenunglück | SQ_026, SQ_033 (Ulf Brakk), SQ_044 |
| Hrallsted | Hirtin Svala; verlorene Herde | SQ_029, SQ_045 |
| Fennhaven | Lorcan; Reusen-Mysterium | SQ_051, SQ_056, SQ_063 (Reusen) |
| Duvreth | Moorweise Ama Duvreth; Rückkehr nach Heilung | SQ_047, SQ_058, SQ_060 |
| Harrâd / Mirsaan / Ashurim | Nadira, Kesh, Imran | SQ_092, SQ_093, SQ_101, SQ_108–112 |
| Vorthax / Kaldra | Thessa (Ausbruchstag), Kurwirtin Malva | SQ_114, SQ_120, SQ_126, SQ_127, SQ_130 |
| Tangwerft / Möwenhuk / Flottholm | Marlene, Okko, Ebba | SQ_069, SQ_074, SQ_075, SQ_081, SQ_090 |
| Fjallstad / Eiðvik-Neu | Leif (Schwester im Kloster), Halla | SQ_140, SQ_144 (Leif), SQ_143 (Halla) |
| Thae'Luun / Säulenrast | Dr. Imke Vael, Bruder Odvar | SQ_153, SQ_155, SQ_163 (Odvar), SQ_165, SQ_167 (Imke Vael) |
| Glanzschacht / Quarzgrund | Steiger Brannoc d. Ä., Schleiferin Nyx | SQ_174 (Nyx), SQ_180, SQ_187, SQ_189 (Brannoc d. Ä.) |
| Lumeya / Wolkenrast | Elun, Windseglerin Ria | SQ_191, SQ_196, SQ_204 (Elun), SQ_192, SQ_206 (Ria) |

**Namensabgleich:** Der Steinbrecher in SQ_023 heißt Arnulf (der Müller von Lindwiesen heißt Jost, CANON §57); der Bergmann in SQ_033 ist Ulf Brakk aus Brakkfels; die Glocke im Delta gehört zur Fähre von Ailsa Duvreth (CANON §52).

---

## 10. Auftraggeber dieses Kapitels

| NPC-ID | Name | Quests |
|---|---|---|
| NPC_AEVRIN | Aevrin Thal | SQ_152, SQ_154, SQ_162, SQ_193 |
| NPC_BRUDER_ODVAR | Bruder Odvar | SQ_163 |
| NPC_DR_IMKE_VAEL | Dr. Imke Vael | SQ_165, SQ_167 |
| NPC_FORSCHERIN_LIV | Meeresforscherin Liv | SQ_186 |
| NPC_FOTOGRAFIN_SIGNE | Fotografin Signe (Akademie) | SQ_147 |
| NPC_FS_ZELLE_AERION | Freie Stimmen (Windanker) | SQ_207 |
| NPC_FS_ZELLE_DORUNSRUH | Zelle Dorunsruh (Freie Stimmen) | SQ_166, SQ_168 |
| NPC_FS_ZELLE_HVITMARK | Zelle Hvitmark (Freie Stimmen) | SQ_142 |
| NPC_GAERTNERIN_SOLA | Gärtnerin Sola (Aerion) | SQ_203 |
| NPC_GLYPHENFECHTER_IVO | Glyphenfechter Ivo | SQ_169 |
| NPC_GLYPHENSTUDENTIN_MAREK | Glyphenstudent Marek | SQ_155 |
| NPC_HALLA | Halla (Eiðvik-Neu) | SQ_143 |
| NPC_ILYX | Ilyx Brannoc | SQ_182, SQ_188 |
| NPC_KIND_TAMSIN | Tamsin (Hörerin) | SQ_160 |
| NPC_KONTORAGENTIN_RIEKE | Kontoragentin Rieke | SQ_183 |
| NPC_LABORLEITERIN_SANNE | Laborleiterin Sanne (Akademie) | SQ_173, SQ_175, SQ_184 |
| NPC_MARIEKE | Marieke Holm | SQ_199 |
| NPC_ORUMA | Oruma Siyel | SQ_208 |
| NPC_PELL | Archivarin Pell | SQ_158 |
| NPC_R07_ASTRID | Sprecherin Astrid Eiðsen | SQ_141 |
| NPC_R07_RUNA | Runa die Erinnernde | SQ_145 |
| NPC_R08_AEVRIN_TUTOR | Professor Thal (Sprechstunde) | SQ_157 |
| NPC_R08_GRAVE | Hehler Grave | SQ_161 |
| NPC_R09_BRANNOC_SR | Stimmwerkstatt Brannoc | SQ_179 |
| NPC_R09_QUILL | Glasbläserin Quill | SQ_178, SQ_185 |
| NPC_R09_SEREN | Kristallmarkt Seren | SQ_181 |
| NPC_R09_SEREN | Seren Quarz (Stimmergilde) | SQ_176, SQ_177 |
| NPC_R10_AELIA | Windhändlerin Aelia | SQ_194, SQ_197 |
| NPC_R10_BRISK | Federschneider Brisk | SQ_209 |
| NPC_R10_ORUMA_TUTOR | Hüterin Oruma | SQ_200 |
| NPC_R10_SIYEL_ARCHIVE | Archivar der Baumeister | SQ_195, SQ_198 |
| NPC_SCHLEIFERIN_NYX | Schleiferin Nyx | SQ_174 |
| NPC_SCHWESTER_IVRA | Schwester Ivra | SQ_144, SQ_146, SQ_148, SQ_150, SQ_151, SQ_170, SQ_171, SQ_172, SQ_190, SQ_210 |
| NPC_SIGRUN | Sigrun Fjall | SQ_149 |
| NPC_STEIGER_BRANNOC | Steiger Brannoc d. Ä. | SQ_180, SQ_187, SQ_189 |
| NPC_STERNWAERTER_ELUN | Sternwärter Elun (Lumeya) | SQ_191, SQ_196, SQ_204 |
| NPC_STUDENTIN_HELKE | Studentin Helke | SQ_156 |
| NPC_UHRMACHER_ODIL | Uhrmacher Odil | SQ_153, SQ_159 |
| NPC_WILDWAECHTER_BOAZ | Wildwächter Boaz | SQ_164, SQ_201, SQ_205 |
| NPC_WINDSEGLERIN_RIA | Windseglerin Ria | SQ_192, SQ_206 |
| NPC_YSOLDE | Ysolde Varn | SQ_202 |

Die Auftraggeber-Regel (≤ 3 Geschichten je NPC, Ketten zählen als eine) wurde über **alle 210** Quests geprüft (QS-14) – 0 Verstöße.

---

## 11. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | Venns Rektorat und Zimmer, Glyphentafeln (10), Stalakkord-Orgel, Lichtschächte Prismara, Wand der Zehn (Schattenrelief), Kronenwerft-Notizen, sechs Orte der Pause | K57 |
| Writing | Thing-Rede (SQ_141), Bundesrat (SQ_154), Kaels Arbeit in zwei Fassungen (SQ_158), Nachhall-Texte je Ende | K55 |
| Audio | Orte der Pause (getaktete Stille), Glasharfe, Sturmharfe, Hymnora-Chor, Stalakkord-Orgel | K55 |
| Combat | Glyphenduell (Glyphen wirken nächste Runde), Brechungsprobe, Sternfall (angezeigt, DR-07), Plattformkämpfe im Windrennen | K35 |
| Tech | Schnellreise Aerion ↔ Eichenhall (SQ_198), Luftfracht-Route (SQ_199), globales Flackern endet (SQ_183) | K40/K65 |
| QA | Quest-Bot über alle 210 Quests; Nachhall-Varianten je Ende | K66 |

---

## 12. Decision Records und Change Request

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-193 | Ordenskette „Hüter der Pause“ als Nachhall-Pilgerweg zu sechs Orten, endet mit dem Einstieg in die Velnox-Questreihe | Der Orden findet einen neuen Sinn; Velnox-Bindung wird erzählerisch vorbereitet | Velnox-Bindung ohne Vorlauf |
| ADR-194 | Eine Nebenquest („Letzte Bitten“) ist bewusst zwischen MQ_A3_05 und MQ_A3_07 platziert | DR-29-Atemzug vor dem Finale; Ysolde erhält eine leise Szene | kein Raum vor dem Finale |
| ADR-195 | Nachhall-Quests nutzen je Ende denselben Ablauf mit anderem Text/Material | DR-19: identisches Endgame, sichtbarer Unterschied | getrennte Questsätze je Ende |

| CR | Betrifft | Änderung | Begründung |
|---|---|---|---|
| CR-005 | K11/K12 Nebenquest-Haken, K13 Dorf-Haken | Haken sind Vorgaben, keine Quest-IDs; Umsetzung laut K51 §9 (eigene Quest mit Hakentitel, Teil einer Quest, Sammelreihe oder Weltereignis). K49/K50-Titel und NPCs angeglichen. | Die Gerüstverteilung (K48) war verbindlich; nicht jeder Haken trägt eine eigene Quest |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §193 | Nebenquests SQ_141–SQ_210 (R07 11, R08 21, R09 18, R10 20); SQ_202 zwischen MQ_A3_05 und MQ_A3_07 | LOCKED |
| §194 | Nebenquests gesamt: 210 Quests, alle Schritte in `SideQuestSteps.csv`, Belohnungen aus Formeln, 18 Ketten, 53 später verfügbar, ~120 h; Haken-Abgleich K51 §9 | LOCKED |
| §195 | Orte der Pause (6 Stationen, FQ_F05_02) als Rückkehrorte; Einstieg in „Die Pause hören“ (K62) | LOCKED |
| §11 | CR-005 | – |
| §10 | ADR-193 – ADR-195 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] 70 Nebenquests ausgeschrieben; alle 210 Nebenquests vollständig
- [x] Späte Wahrheiten (W6–W9) und Enden in Nebenquests abgesichert
- [x] Orte der Pause und Mythische Spuren (Chronaire, Mirrowisp, Aurelune, Velnox)
- [x] Gesamtübersicht (Kennzahlen, Ketten, Regionen, Spielzeit gegen K01)
- [x] Haken aus K11–K13 abgeglichen, Titel/NPCs in K49/K50 nachgezogen (CR-005)
- [x] Alle Prüfregeln über alle 210 Quests erfüllt (0 Fehler)
- [x] Anforderungen, ADR-193 – ADR-195, CANON §193–§195

➡️ **Nächstes Kapitel: K52 – Ökologie und Schwarm-KI.**
