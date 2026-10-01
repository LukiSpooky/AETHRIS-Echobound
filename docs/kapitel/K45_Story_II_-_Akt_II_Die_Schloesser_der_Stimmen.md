# K45 · Story II – Akt II: „Die Schlösser der Stimmen“

| Feld | Wert |
|---|---|
| Dokument | Kapitel 45 von 68 · Narrative Bible, Teil II |
| Version | 1.0 |
| Owner | Narrative Director |
| Mitwirkende | Lead Writer, Quest Designer, Cinematics Director, Level Design (Sahrun-Weite, Ignareth, Hvitfell, Ael'Dorun), Audio (Leitmotive), Combat Designer (Story-Bosse), Sensitivity Review (R04/R07) |
| Baut auf | K07 §7 (Die Wahrheit), §13 (W4–W7), K44 (Erzählprinzipien §168, Flags §171), CANON §15 (Akt-II-Struktur, Traversal), §34 (Ursprungsstimmen), §36 (Fraktionssitze), §51 (Arenen), §131 (Story-Bosse), K40 (Grab-/Flugreiten) |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Quests/MainQuests.csv` (+11 Quests MQ_A2_01–11), `Data/Quests/StoryFlags.csv` (+3 Flags) |
| Neue Kanon-Einträge | CANON §172 (Akt-II-Struktur), §173 (Akt II Quests), §174 (Kronensplitter), §175 (Flags Akt II) |

---

## Inhalt

1. [Akt II in einem Satz](#1-akt-ii-in-einem-satz)
2. [Struktur, Freiheit, Intensität](#2-struktur-freiheit-intensität)
3. [Figuren in Akt II](#3-figuren-in-akt-ii)
4. [Die Kronensplitter](#4-die-kronensplitter)
5. [Der Auftakt](#5-der-auftakt)
6. [Die drei freien Regionen](#6-die-drei-freien-regionen)
7. [Die Wende in Dorunsruh](#7-die-wende-in-dorunsruh)
8. [Ael'Dorun und der Thronsaal](#8-aeldorun-und-der-thronsaal)
9. [Dynamische Erzählung](#9-dynamische-erzählung)
10. [Entscheidungen und Flags](#10-entscheidungen-und-flags)
11. [Zwischensequenzen und Leitmotive](#11-zwischensequenzen-und-leitmotive)
12. [Quest-Daten](#12-quest-daten)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Akt II in einem Satz

> *Der Wärter erfährt, dass die Arenen Schlösser über schlafenden Stimmen sind und dass er selbst einen Schlüssel in sich trägt – und muss zusehen, wie der Mann, der ihm am freundlichsten geholfen hat, genau diese Schlüssel benutzt, um eine Krone zusammenzusetzen.*

**Thema des Akts:** *Vertrauen.* Ysolde hat geschwiegen, um zu schützen. Venn hat geholfen, um zu benutzen. Sereth hat gekämpft, ohne zu wissen, für wen. Kael folgt, weil er gesehen werden will. Akt II fragt, ob man jemandem vertrauen kann, der nicht alles sagt – und gibt keine einfache Antwort.

**Ton:** weiter, rauer, älter. Die Landschaften sind größer (Wüste, Vulkan, Eis, Ruinen), die Städte selbstbewusster, die Konflikte politischer. Humor bleibt (Marieke, Hralda, die Echos), aber er wird leiser, je näher Dorunsruh rückt.

---

## 2. Struktur, Freiheit, Intensität

| Abschnitt | Regionen | Akkorde (gesamt) | Wahrheit | Spielzeit |
|---|---|---|---|---|
| Auftakt | R01 Eichenhall | 4 | W4 | 1 h |
| Freie Regionen | R04 Sahrun-Weite, R05 Ignareth, R07 Hvitfell (frei, 2 von 3 vor der Wende) | 5–6 | W5 (nach dem 2. Akt-II-Akkord) | 9 h |
| Wende | R08 Dorunsruh (öffnet bei 6 Akkorden) | 6 | W6 | 2,5 h |
| Ausklang der Freiheit | dritte freie Region + Arena Dorunsruh (beliebige Reihenfolge) | 7–8 | – | 5 h |
| Finale des Akts | R08 Thronsaal (8 Akkorde) | 8 | W7 | 2,5 h |
| **Summe** | | **+4** | **W4–W7** | **~20 h** |

Wild-Level-Korridor Akt II: 25–55 (CANON §15). Die drei freien Regionen fixieren ihre Stufe beim ersten Betreten nach Akkordanzahl (T4 bei 4 Akkorden, T5 bei 5, T6 bei 6, T7 bei 7). Ael'Dorun hat nur T6–T7 (CANON §40). Wärterrang am Ende von Akt II: ~24 (K43 §3.1) – Raids (Rang 22) öffnen in der zweiten Hälfte des Akts.

```
Intensität (1–10) über Akt II
10 ┤
 9 ┤                                         ███ Verrat                         ███ Thronsaal
 8 ┤                       ███ Eiðvik
 7 ┤        ███ Sonnenhof
 6 ┤                  ██ Krater                              ██ Glyphen
 5 ┤                               ██ Ysolde
 4 ┤ ██ Schlösser                          ██ Messung
 3 ┤                                                   ██ Freunde
 2 ┤                                                                                  ██ Neun
 1 ┼────────────────────────────────────────────────────────────────────────────────────────
     A2-01   A2-02  A2-03  A2-04  A2-05  A2-06  A2-07  A2-08  A2-09   (3. Region)  A2-10  A2-11
```

**Atemzug-Regel (DR-29):** Nach dem Verrat (9) folgt *Unter Freunden* (3); nach dem Thronsaal (9) folgt *Neun von Zehn* (2). Zwischen den freien Regionen liegt jeweils eine Reise mit Lager-Moment. Eiðvik (8) wird von *Was Ysolde verschwieg* (5) gefolgt, wenn Hvitfell die zweite Region ist; sonst folgt auf Eiðvik die Reise nach Dorunsruh mit Lager (≥ 20 min).

---

## 3. Figuren in Akt II

| Figur | Rolle in Akt II | Bogen in diesem Akt |
|---|---|---|
| **Ysolde Varn** | Mentorin | Gesteht in MQ_A2_05, dass sie vom Nachklang wusste; sucht danach Nähe, ohne sich zu entschuldigen, was sie nicht bereut |
| **Kael Duran** | Venns Protegé | Misst die Akkorde, glaubt an die Akademie; nach dem Verrat bleibt er bei Venn – „jemand muss ihn aufhalten, falls er zu weit geht“; nimmt im Thronsaal den Splitter |
| **Aldric Venn** | Antagonist | Freundlich, bis er es nicht mehr sein muss; trägt sein Argument fair vor (Venns Regel) |
| **Sereth Vaun** | Ordensoberhaupt | Erfährt in MQ_A2_07, dass Venn den Orden benutzt hat; Krise des Glaubens, nicht des Ziels; wird Verbündete auf Zeit |
| **Hralda Brakk** | Wildwacht | Öffnet das Archiv; bietet Unterschlupf, wenn die Freien Stimmen es nicht tun |
| **Tavesh Amaru** | Freie Stimmen | In Ignareth an der Befreiung der Arbeits-Echos beteiligt; bietet Unterschlupf bei `FLAG_FS_STANCE` ≥ 0 |
| **Marieke Holm** | Goldklang | Fordert in Ignareth ihren Gefallen ein (bei `FLAG_KONTOR_DEBT` = 1), sonst bittet sie darum |
| **Shirah Harrad** | Arenameisterin Qasr Sahrun | Licht; liest Wahrheit in Spiegeln; vertraut dem Spieler eine Sonnenhof-Legende an |
| **Kaldrex Vorn** | Arenameister Schlackenwehr | Glut/Metall; Schmied, ehemaliger Kontor-Vorarbeiter mit schlechtem Gewissen |
| **Sigrun Fjall** | Arenameisterin Hvitmark | Frost; Enkelin einer Klangpest-Überlebenden; kennt Sereth aus Kindertagen |
| **Aevrin Thal** | Arenameister Dorunsruh | Arkan; Glyphenforscher; verweigert Venn nach dem Verrat den Zutritt zur Arena |
| **Ulrek** | Ordenskommandant | Kehrt in Hvitfell zurück (Schweigfels); hat seine Niederlage nicht vergessen, aber auch nicht übelgenommen |
| **Ilen / Maedryn** | historisch | Visionen im Thronsaal (W7) |

---

## 4. Die Kronensplitter

Die Resonanzkrone zersprang bei der Großen Stille in **zehn Splitter** (CANON §36). Jeder Splitter fiel an den Ort, an dem eine Stimme einschlief, und ist auf diese Stimme gestimmt. Die Splitter sind ohne Akkord nicht zu orten – ihr Klang verschwindet im Schlaf der Stimme. Ein Akkord öffnet nicht nur das Schloss, er lässt die Stimme im Schlaf „umdrehen“: Für einige Wochen ist der Splitter hörbar.

```
 Spieler gewinnt Akkord ──► Stimme dreht sich im Schlaf ──► Splitter klingt (≈ 3 Wochen)
                                                              │
             Venns Messung (Akademie-Resonometer) ◄───────────┘ ortet ihn
                                                              │
             Orden (glaubt: „Stillstein-Rohstoff“) birgt ihn ─┘ und liefert an Dorunsruh
```

| Splitter | Stimme | Ort | Wer ihn birgt | Wann |
|---|---|---|---|---|
| 1 | Sylv'anor (R01) | unter Arena Eichenhall | Orden (Akt I, unbemerkt) | nach Akkord 1 |
| 2 | Orh'gruun (R02) | unter Kharsholm | Orden | nach Akkord R02 |
| 3 | Nhael'vesh (R03) | unter Morvenfurt | Orden (im Chaos nach MQ_A1_08) | nach dem Turm |
| 4 | Thal'assyr (R06) | Tiefseegrotte | Kontor-Taucher im Auftrag der Akademie | nach Akkord R06 |
| 5–7 | Ash'kareth, Pyr'thagon, Isv'aldr | R04/R05/R07 | Orden / Kontor-Kisten (MQ_A2_03) | nach den Akkorden in Akt II |
| 8 | Ka'thurel (R08) | Thronsaal-Gewölbe | **Kael** für Venn (MQ_A2_10) | Ende Akt II |
| 9 | Aeth'rion (R10) | Sternenarena Aerion | seit Jahren in Venns Besitz (Akademie-Expedition 983) | vor Spielbeginn |
| 10 | Prism'aion (R09) | Resonanzkammer Prismara | offen – Ziel von Akt III | Akt III |

**Zählregel:** Am Ende von Akt II hat Venn **neun** Splitter. Der zehnte liegt in Prismara und ist nur mit dem neunten Akkord erreichbar – der Spieler muss ihn holen, um die Krone zu verhindern, und bringt ihn damit ebenfalls in Reichweite (Akt III, K46).

**L-01:** Bis MQ_A2_07 heißen die Splitter in allen Texten „Stillstein-Rohstoff“ oder „Kristallkern“; danach „Kronensplitter“. Klangfragmente über die Krone (LORE_FRG mit TruthLevel 6–7) bleiben bis dahin verzerrt (K39 §6).

---

## 5. Der Auftakt

### MQ_A2_01 · Die Schlösser der Stimmen (Eichenhall, Intensität 4)

Hralda Brakk ruft den Spieler ins **Wildwacht-Archiv** unter Eichenhall. Ysolde ist da, wortkarg. Auf dem Tisch: eine Kiste mit Notizbüchern einer Frau, die vor 124 Jahren die Arenen gründete – **Wendelin Aar**.

> **Hralda:** „Die Akademie hat das Archiv vor zwei Monaten angefragt. Ganz höflich. Ich habe Nein gesagt. Ganz unhöflich.“
> **Ysolde:** „Lies Seite vierzig.“

Wendelins Handschrift, mit dorunischen Glyphen am Rand: *„Ich baue keine Bühnen. Ich baue Türen, die nur von außen aufgehen. Wer zehn Schlüssel hält, kann zehn Schläfer wecken – oder zehn Schläfer zwingen. Möge niemand je alle zehn halten, der Gründe hat.“*

**W4 enthüllt:** Die Arenen stehen über den Schlafstätten der Stimmen; Akkorde sind Schlüssel. Das erste **Wendelin-Tagebuch** (von 20, K39) wird zur Sammelquest; Seiten liegen in jeder Arena.

> *(einfühlsam)* „Sie hatte Angst vor dem, was sie gebaut hat.“ · *(neugierig)* „Wer hat die anderen Seiten?“ · *(entschlossen)* „Dann sammeln wir die Schlüssel, bevor es jemand anderes tut.“

Hralda überreicht den **Grabsattel-Bauplan** (Grabreiten für die Sahrun-Weite, CANON §15). Ysolde sagt, sie werde „im Süden“ sein; sie sagt nicht, warum sie den Spieler nicht ansieht.

Bei `FLAG_KONTOR_DEBT` = 1 wartet vor dem Archiv ein Kontor-Bote: Marieke erwartet den Spieler in Schlackenwehr. „Kein Eilauftrag. Aber auch kein Vergessen.“

---

## 6. Die drei freien Regionen

### MQ_A2_02 · Die Wahrheit unter dem Sonnenhof (Sahrun-Weite, Intensität 7)

**Orte:** Qasr Sahrun, Wanderdorf Ashurim (mobil), Glasebene-Turm, Plateau-Lager. **Neues System:** Grabreiten (Sandtunnel, Höhlen der Glasebene).

Das **Wanderdorf Ashurim** zieht jede Woche weiter; der Spieler muss es über Spuren und Dünen-Echos finden (Kodex-Aufgabe). Die Ältesten erzählen, dass die Glasebene „vor tausend Jahren eine Stadt war, die die Sonne zu laut besang“ (Lore für die Hochkultur, K07 §8). Am Glasebene-Turm hat sich ein **Dunmarsch** mit Glas überzogen – der **Glaskoloss der Weite** (BOSS_A2_01, Lv. 42): Spiegelung, Großwelle, frühes Anschwellen (K35 §7).

Nach dem Sieg zerfällt das Glas; der Dunmarsch kehrt zu seiner Herde zurück. **Shirah Harrad** lädt zum Arenakampf (Sonnenspiegel-Regel). Mit dem Akkord dreht sich **Ash'kareth** im Schlaf, und für einen Atemzug sieht der Spieler alle Lichter der Stadt **doppelt** – eine Wahrheitsstimme zeigt, was verborgen ist: Ein Ordensmann in der Menge trägt eine Akademie-Spange unter dem Schweigegewand. Der Spieler kann es noch nicht deuten (W6-Vorahnung, ohne Enthüllung).

> **Shirah:** „Ash'kareth lässt nichts verbergen. Darum schläft sie. Eine Welt, in der nichts verborgen bleibt, hält niemand lange aus.“

**Sensitivity:** Die Sonnenhöfe sind ein Glaube unter vielen (CANON §36); Ashurim ist kein Abbild einer realen Kultur (CANON §22). Das Wanderdorf ist wohlhabend, gebildet und politisch eigenständig.

### MQ_A2_03 · Das Kraterherz (Ignareth, Intensität 6)

**Orte:** Schlackenwehr, Vorthax, Kaldra, Obsidianwacht. **Thema:** Arbeit und Ausbeutung.

In Schlackenwehr arbeiten Echos in den Schmieden – die meisten freiwillig, gebunden, gut versorgt. Am Kraterrand aber betreibt ein Kontor-Konsortium ein **Lager** mit verstummten Echos aus den Stillezonen, die „ohnehin nichts mehr spüren“. **Tavesh Amaru** und die Freien Stimmen planen eine Befreiung.

**Mariekes Gefallen.** Ist `FLAG_KONTOR_DEBT` = 1, verlangt Marieke, dass der Spieler drei **versiegelte Kisten** nach Obsidianwacht bringt; sonst bittet sie darum, gegen Bezahlung. Wer eine Kiste öffnet (Resonanzsinn hört einen „Kristallkern“), findet Stillsteine – und darunter einen dumpf klingenden Splitter.

| Wahl | Ergebnis | Flag |
|---|---|---|
| Kisten liefern, ohne zu öffnen | Marieke zahlt, Schuld getilgt; Splitter geht an „Abnehmer in Dorunsruh“ | `KONTOR_CRATES` = 0 |
| Öffnen, trotzdem liefern | Splitter geht weiter; der Spieler weiß von den Stillsteinen; Marieke: „Ich frage nicht, was drin ist. Das ist mein Geschäftsmodell.“ | `KONTOR_CRATES` = 1 |
| Öffnen, zurückbringen | Marieke ist verärgert, dann nachdenklich; der Splitter geht trotzdem verloren (Ordensleute holen ihn nachts) | `KONTOR_CRATES` = 2 |

Keine Wahl verhindert, dass Venn den Splitter bekommt (ADR-165). Die Wahl verändert, was der Spieler weiß und wie Marieke und das Kontor ihn in Akt III sehen (K47 Ruf).

Die **Befreiung** des Lagers ist Pflicht und gewaltfrei: Der Spieler heilt mit dem Resonator die verstummten Echos (Mini-Stillezone, drei Kreise), Tavesh lenkt die Wachen ab. **Kaldrex Vorn**, der Arenameister, war früher Vorarbeiter im Kontor; er schaut weg, als die Echos durch sein Tor ziehen.

> **Kaldrex:** „Ich schmiede seit dreißig Jahren. Man lernt, wann ein Eisen bricht. Dieses hier ist gebrochen.“
> *(einfühlsam)* „Danke, dass Ihr weggesehen habt.“ · *(neugierig)* „Wer betreibt das Lager wirklich?“ · *(entschlossen)* „Nächstes Mal seht Ihr hin.“ → `FS_STANCE` +1 / 0 / 0

Im Akkord-Moment brummt unter Schlackenwehr **Pyr'thagon** im Schlaf; die Esse der Arena flackert blau.

### MQ_A2_04 · Eiðvik (Hvitfell, Intensität 8)

**Orte:** Hvitmark, Fjallstad, **Eiðvik-Neu** und die **Ruinen von Eiðvik**, Kloster Schweigfels, Gletscherwacht. Ysolde hatte am Ende von Akt I gesagt: *„Geh nach Eiðvik. Hör hin.“*

In den Ruinen hört der Spieler mit dem Resonanzsinn die **Klangpest von 948** – eine Nachhall-Sequenz (spielbar, ohne Kampf): Ein Resonanzsturm treibt die Echos des Dorfes in Raserei; Menschen fliehen in den Schnee; ein Mädchen hält ein Echo fest, das sie nicht mehr erkennt. Das Mädchen ist **Sereth**.

Im **Kloster Schweigfels** empfängt Sereth den Spieler, ohne Wachen. Sie erzählt ihre Geschichte ruhig, ohne Bitterkeit:

> **Sereth:** „Es war nicht böse. Das ist das Schreckliche. Es war nur zu laut. Ein Lied, das niemand mehr dirigiert hat. Ich habe mir geschworen, dass kein Kind mehr hören muss, was ich gehört habe. Die Stillsteine sind keine Waffe. Sie sind ein Wiegenlied.“
> *(einfühlsam)* „Es tut mir leid, was Euch geschehen ist.“ · *(neugierig)* „Wer hat Euch die Steine beigebracht?“ · *(entschlossen)* „Ein Wiegenlied, das Echos die Stimme nimmt.“ → `SERETH_RESPECT` +1 / +1 / 0

Die neugierige Frage führt zur wichtigsten Zeile des Akts, die erst später Gewicht bekommt:

> **Sereth:** „Beigebracht? Niemand. Ein Gelehrter hat mir vor Jahren eine Formel geschickt. Ohne Namen. Er schrieb, dass er mein Leid verstehe.“

**Venns Schatten.** Auf dem Gletscher über der Gletscherwacht stellt sich ein **Tysvorn** (BOSS_A2_02, Lv. 50) in den Weg – ein Leere-Oberton, der seit der Großen Stille im Eis schläft und nun von einer fernen Stimme geführt wird. Taktraub, Stillezähler, Stillepuls (K35 §7). In Phase 3 erscheint in der Aurora eine **Silhouette** mit dem Umriss eines Gelehrtenmantels; eine Stimme sagt: *„Noch nicht.“* Dann verschwindet sie. Ist der Verrat schon geschehen (Hvitfell als dritte Region), erkennt der Spieler Venns Stimme, und Ulrek, der zu Hilfe kam, flucht leise (§9).

Arena **Hvitmark**: **Sigrun Fjall** (Eis-Regel). Mit dem Akkord singt **Isv'aldr** im Schlaf eine einzelne, lange Note; im Polarlicht erscheinen für eine Nacht die Namen der Toten von Eiðvik.

---

## 7. Die Wende in Dorunsruh

### MQ_A2_05 · Was Ysolde verschwieg (dynamisch, Intensität 5)

Nach dem **zweiten Akkord in Akt II** wartet Ysolde in der Siedlung dieser Region (Ashurim, Kaldra oder Fjallstad) an einem Lagerfeuer. Sie hat gelesen, was der Spieler in Morvenmoor gesehen hat, und sie hat die Notizbücher Wendelins Seite für Seite verglichen.

> **Ysolde:** „Als du sieben warst, hast du im Lindwald gesessen und gesagt, die Bäume summen in Moll. Ich habe gelacht. Dann habe ich zugehört. Und dann wusste ich, wessen Kind du in deinem Klang trägst.“
> **Ysolde:** „Ilens Blutlinie ist nicht gestorben. Ihr Ton auch nicht. Du hörst die Grundfrequenzen, weil ein Teil des Riegels in dir klingt. Ihr **Nachklang**.“

**W5 enthüllt.** Ysolde wusste es seit Lindwiesen. Sie hat geschwiegen, weil jeder, der von einem lebenden Nachklang weiß, ihn benutzen will.

| Haltung | Antwort | Ysoldes Reaktion | Flag |
|---|---|---|---|
| Einfühlsam | „Du hast mich beschützt.“ | „Ich habe mich auch selbst beschützt. Vor dem Moment hier.“ | `YSOLDE_BOND` +1 |
| Neugierig | „Was kann der Nachklang?“ | Erklärt Resonanzsinn II: Grundfrequenzen auch durch Stillezonen hören | `YSOLDE_BOND` 0 |
| Entschlossen | „Du hättest es mir sagen müssen.“ | „Ja.“ (Pause.) „Ja. Das hätte ich.“ | `YSOLDE_BOND` −1 |

Spielmechanisch: **Resonanzsinn II** (Reichweite +15 m, Stillezonen-Durchsicht – K40). Die Szene endet in jedem Fall damit, dass Ysolde bleibt, bis das Feuer ausgeht.

### MQ_A2_06 · Die Messung (Dorunsruh, Intensität 4)

Mit **sechs Akkorden** kommt ein Brief von Kael: Die Akademie in **Dorunsruh** bitte um eine Messung – die sechs Akkorde zusammen könnten zeigen, wie man die Stillezonen „für immer“ heilt. Gleichzeitig liefert die Akademie den **Flugsattel** (nimbarische Technik aus Akademie-Beständen): Flugreiten (CANON §15, K40).

Dorunsruh ist eine Stadt der Gelehrten auf Säulen über den Ruinen; der Spieler erlebt eine freundliche, neugierige Akademie mit Studierenden, Echo-Bibliotheken und Glyphenwänden. **Venn** führt persönlich durch die Halle der Grundfrequenzen.

> **Venn:** „Weißt du, was mich an dir fasziniert? Du hörst, was wir messen müssen. Und trotzdem stehst du hier und lässt dich messen. Das ist Größe. Oder Vertrauen. Ich hoffe, beides.“

Kael bedient das **Resonometer**; die Akkorde klingen nacheinander, und auf einer Glaskarte von Aethris leuchten sechs Punkte auf. Kael ist stolz. Venn bedankt sich, mit echter Wärme.

### MQ_A2_07 · Der Verrat (Dorunsruh, Intensität 9)

In der Nacht weckt der Resonanzsinn den Spieler: Unter der Akademie klingt etwas, das *zu viele* Stimmen auf einmal hat. Das **Gewölbe** liegt unter der Halle der Grundfrequenzen. Dort, in Glasschreinen: **sechs Kronensplitter**, jeder mit einem Etikett im Ordensformat – *„Stillstein-Rohstoff, Lieferung Hvitfell/Schweigfels“*. Daneben die Glaskarte der Messung: Die sechs Punkte sind die Fundorte.

**W6 enthüllt.** Venn steuert den Orden; die Formel der Stillsteine kam von ihm; er sammelt die Kronensplitter; die Akkorde des Spielers waren sein Wegweiser.

Venn erscheint, ohne Wachen, mit Kael an seiner Seite.

> **Venn:** „Ich hätte es dir gesagt. Am Ende. Ich wollte, dass du siehst, was ich sehe, bevor du entscheidest, ob du es hasst.“
> **Venn:** „Eiðvik. Die Siegelkriege. Ein Kind, das in einem Keller wartet, während Echos die Stadt über ihm zerreißen, weil jemand ihnen befohlen hat, es zu tun – oder weil niemand es ihnen verboten hat. Ich war dieses Kind. Freiheit ohne Ordnung ist nur eine andere Form von Leid.“
> **Venn:** „Die Krone zwingt nicht. Sie *stimmt*. Ein Weltlied, das nie mehr zu laut wird. Ich biete dir einen Platz daneben.“

| Haltung | Antwort | Venns Reaktion |
|---|---|---|
| Einfühlsam | „Du hast so viel verloren. Das gibt dir nicht das Recht.“ | „Doch. Genau das gibt es mir. Wer sonst sollte es haben?“ |
| Neugierig | „Was passiert mit den Stimmen, wenn du sie stimmst?“ | „Sie schlafen nicht mehr. Sie singen. Nur eben… zusammen.“ (Er weicht aus.) |
| Entschlossen | „Ich werde dich aufhalten.“ | „Ich weiß. Darum mag ich dich.“ |

**Kael** steht zwischen ihnen. Er wusste nichts vom Orden – aber er wusste von den Splittern, und er hat geglaubt, sie seien zur Heilung.

> **Kael:** „Er hat mich *gesehen*. Nicht das, was ich nicht kann. Das, was ich kann.“
> *(einfühlsam)* „Ich sehe dich auch.“ (`KAEL_TRUST` +1) · *(neugierig)* „Und was siehst du jetzt?“ (0) · *(entschlossen)* „Komm mit mir.“ (`KAEL_TRUST` +1 bei ≥ 0, sonst −1)

Kael bleibt bei Venn – immer (K07 §12). Seine letzte Zeile hängt vom Vertrauen ab: bei `KAEL_TRUST` ≥ 1 *„Jemand muss ihn aufhalten, falls er zu weit geht. Lass mich das sein.“*; sonst *„Du hättest es nie verstanden.“*

**Flucht.** Venn lässt den Spieler nicht festnehmen – er braucht die restlichen Akkorde. Aber die Ordensleute im Gewölbe wissen das nicht. Eine Fluchtsequenz durch die Glyphengänge (DR-14: ein angekündigter Hinterhalt), Kämpfe gegen Ordenswachen (Ordenstrupp, Stufe Zone +2), dann über die Säulen mit dem neuen **Flugsattel**. Am Rand der Stadt wartet **Sereth**. Sie hat das Etikett im Gewölbe gelesen – ein Orden, der aus Barmherzigkeit Stille bringen wollte, hat einem Mann Kronensplitter geliefert.

> **Sereth:** „Ich habe zwanzig Jahre lang geglaubt, ich bringe Ruhe. Ich habe einem Mann Werkzeug gebracht, der *Gehorsam* meint, wenn er Ruhe sagt.“ (Pause.) „Ich glaube immer noch an die Stille. Aber nicht an seine.“

`SERETH_RESPECT` steigt um +1 für alle Spieler, die Sereth in Hvitfell nicht verhöhnt haben (≥ 0); sonst bleibt es. Sereth bricht mit Venn; ein Teil des Ordens folgt ihr, ein Teil bleibt Venn treu.

### MQ_A2_08 · Unter Freunden (dynamisch, Intensität 3)

Der **Atemzug** nach dem Verrat. Der Unterschlupf hängt von `FLAG_FS_STANCE` ab (ADR-166):

| Bedingung | Unterschlupf | Gastgeber | Besonderheit |
|---|---|---|---|
| `FS_STANCE` ≥ 0 | Verborgenes Lager der Freien Stimmen bei Säulenrast | Tavesh Amaru | Befreite Echos aus Ignareth sind da und erkennen den Spieler |
| `FS_STANCE` < 0 | Wildwacht-Außenposten Archontenwacht | Hralda Brakk | Hralda kocht; die Wildwacht stellt Späher |

In beiden Fällen: **Lager-Moment** mit dem ganzen Chor (Starter-Szene, K44 §2), ein Gespräch mit Ysolde (Ton nach `YSOLDE_BOND`), eine Nachricht von Marieke (Ton nach `KONTOR_CRATES`), und Sereth bittet um ein Gespräch unter vier Augen. Sie erzählt, was sie über Venns Pläne weiß: Er braucht **alle zehn Splitter** und einen Ort, an dem die Krone schon einmal klang – **Nimbara**. Er braucht außerdem einen Ton, der den Riegel lösen kann. Sereth sieht den Spieler lange an, sagt aber nicht, welchen.

Freischaltung: **Hain-Erweiterung** (Lagerplatz-Echos aus dem Unterschlupf ziehen in den Resonanzhain, K37), Ordensgegner in Ael'Dorun sind ab jetzt gemischt (Venn-treu: feindlich; Sereth-treu: neutral, handelbar).

---

## 8. Ael'Dorun und der Thronsaal

### MQ_A2_09 · Glyphen von Dorunsruh (Intensität 6)

Die Arena von Dorunsruh steht unter Akademie-Aufsicht. **Aevrin Thal**, Glyphenforscher und Arenameister, verweigert Venn nach dem Verrat den Zutritt und lässt den Spieler über die Ruinen von **Thae'Luun** und **Säulenrast** zur Arena kommen. Arena-Regel *Glyphen* (K11). Aevrin kennt den Thronsaal aus Grabungsakten, die Venn hat schwärzen lassen.

> **Aevrin:** „Die Akademie hat mir beigebracht, dass Wissen frei sein muss. Ich habe nur nie gefragt, frei für wen.“

Mit dem Akkord öffnet sich der Weg zum **Thronsaal-Gewölbe** – sobald der Spieler insgesamt **acht Akkorde** hält. Die dritte freie Region kann davor oder danach gespielt werden (§9).

### MQ_A2_10 · Der Thronsaal (Ael'Dorun, Intensität 9)

Unter Dorunsruh, tiefer als die Akademie je gegraben hat: das **Thronsaal-Gewölbe** des Archon Maedryn. Glyphen an den Wänden erzählen die Geschichte der Krone – mit dem Akkord von Dorunsruh werden sie lesbar (Kodex: 6 Lore-Einträge, TruthLevel 7).

Vor dem Thron steht der **Kronensplitter-Wächter** (BOSS_A2_03, Thaelarch, Lv. 55): Klangpanzer (Arkan → Metall → Geist), Schwachstelle am Helm, Begleiter-Glyphen (K35 §7). Bei < 15 % kniet Thaelarch nieder, und der Thronsaal beginnt zu singen – **Ka'thurel**, die Stimme der Erinnerung, zeigt, was dieser Raum gesehen hat.

**Vision (W7).** Der Thronsaal, gut tausend Jahre jünger. **Archon Maedryn** setzt die Krone auf; zehn Stimmen werden zu *einer* Stimme gezwungen, und in ganz Ael'Dorun hören Echos auf, eigene Töne zu singen. Echos tragen Lasten, kämpfen in Reihen, schweigen auf Befehl. Dann: **Ilen** im Gewand des Erstchors, mit Aeth'rion an ihrer Seite. Sie spricht nicht mit Maedryn. Sie spricht mit den Stimmen.

> **Ilen:** „Ich kann euch nicht befreien, ohne euch zu brechen. Aber ich kann euch schlafen lassen, bis jemand kommt, der euch fragt, statt zu befehlen. Wollt ihr das?“
> *(Zehn Töne antworten. Dann öffnet sie die Pause.)*

**W7 enthüllt:** Die Große Stille war keine Katastrophe, sondern **Ilens bewusste Tat** gegen Maedryns Krone – mit dem Einverständnis der Stimmen. Der Riegel, der jetzt bröckelt, ist ihr Versprechen.

Als die Vision endet, steht **Kael** im Thronsaal. Er hat den Kampf aus dem Schatten verfolgt. Er nimmt den **achten Splitter** vom Thron.

| `KAEL_TRUST` | Kaels Verhalten |
|---|---|
| ≥ 1 | Er zögert. „Du hast es auch gesehen, oder? Was sie getan hat?“ Er nimmt den Splitter, lässt aber seinen Resonometer-Notizblock liegen (Akt III: Hinweis auf Venns Ritualplan) |
| 0 | Er nimmt den Splitter wortlos, sieht den Spieler einen Moment zu lang an |
| ≤ −1 | „Sie hat die Welt zum Schweigen gebracht, und ihr nennt das Freiheit.“ Er geht ohne Zögern |

Der Spieler kann Kael nicht aufhalten: Ein Glyphenschild, den Venn ihm gegeben hat, hält den Spieler eine Szene lang fest (kein Kampf; ADR-167). Belohnung: **Stimmsiegel Ka'thurel** (Bindung der Ursprungsstimme nach Regionalquest, CANON §34), Klangfragment *Ilens Frage*.

### MQ_A2_11 · Neun von Zehn (Intensität 2)

Abend auf den Säulen von Dorunsruh. Ein **Rat** auf einer Ruinenterrasse: Ysolde, Hralda, Sereth, Aevrin – dazu Tavesh (bei `FLAG_SHELTER` = FS) oder ein Wildwacht-Späher, und Marieke per Klangbrief (immer; ihr Ton hängt von `KONTOR_CRATES` ab).

Was bekannt ist: Venn hat **neun Splitter**. Der zehnte liegt in der Resonanzkammer von **Prismara** und lässt sich nur mit einem neunten Akkord orten. Venn braucht ihn – und er braucht den Ton, der Ilens Riegel lösen kann (Sereth sieht den Spieler an; Ysolde auch).

> **Ysolde:** „Wenn wir nach Prismara gehen, bringen wir ihm den letzten Schlüssel vielleicht selbst.“
> **Sereth:** „Wenn wir nicht gehen, nimmt er ihn sich.“
> *(einfühlsam)* „Wir gehen zusammen.“ · *(neugierig)* „Was passiert mit mir, wenn der Riegel bricht?“ · *(entschlossen)* „Wir gehen. Morgen.“

Niemand beantwortet die neugierige Frage. Ysolde dreht sich weg (W9 bleibt verborgen; L-01). Die Kamera fährt über die Säulen nach Westen, wo der Krater von Prismtiefen schimmert. **Akt III** beginnt.

---

## 9. Dynamische Erzählung

Die drei freien Regionen und der Zeitpunkt der Wende erzeugen sechs Reihenfolgen. Damit jede eine runde Erzählung ergibt:

| Ereignis | Auslöser | Ort |
|---|---|---|
| MQ_A2_05 Ysoldes Geständnis | zweiter Akkord in Akt II | Siedlung der zweiten Akt-II-Region |
| MQ_A2_06 Die Messung | sechster Akkord gesamt | Brief erscheint im Lager; Ziel Dorunsruh |
| MQ_A2_07–08 | nach der Messung | Dorunsruh |
| Dritte freie Region | nach der Wende spielbar oder vor MQ_A2_06 (wer Dorunsruh ignoriert) | beliebig |
| MQ_A2_10 Thronsaal | acht Akkorde gesamt + MQ_A2_09 | Ael'Dorun |

**Varianten der dritten Region nach der Wende (`FLAG_W6_DONE`):**

| Region | Vor der Wende | Nach der Wende |
|---|---|---|
| Sahrun-Weite | Ordensmann mit Akademie-Spange (Vorahnung) | Der Ordensmann ist geflohen; Shirah hat ihn gestellt und übergibt einen Lieferschein an Dorunsruh |
| Ignareth | Kisten gehen an „Abnehmer in Dorunsruh“ | Marieke weiß, wer der Abnehmer ist; ihr Gefallen wird zur Bitte um Wiedergutmachung (`KONTOR_CRATES` bleibt wählbar) |
| Hvitfell | Venns Schatten ist eine fremde Silhouette | Der Spieler erkennt Venns Stimme; **Ulrek** kommt mit Sereth-treuen Ordensleuten zu Hilfe und kämpft in Phase 3 als NPC-Begleiter |

**Skalierung:** Story-Bosse übernehmen die Zonenstufe (BOSS_A2_01 und BOSS_A2_02 skalieren zwischen Lv. 42 und 50 mit der fixierten Region; Thaelarch ist fest Lv. 55). Die Zielwerte in `Bosses.csv` sind die Stufe bei kanonischer Reihenfolge (R04 → R05 → R07).

**Ignorieren erlaubt:** Ein Spieler kann nach sechs Akkorden die Messung vertagen und zuerst die dritte Region spielen. Dann erhält er den Flugsattel trotzdem – über Hralda (Wildwacht-Bestände, „die Akademie war schneller, aber wir sind nicht langsam“). Das Gespräch in MQ_A2_06 verweist dann auf sieben Punkte statt sechs.

---

## 10. Entscheidungen und Flags

| DisplayName | Range | SetIn | Affects |
|---|---|---|---|
| Haltung zu den Freien Stimmen | -2..2 | MQ_A1_04|MQ_A2_* | Epilog Freie Stimmen verbündet/verfeindet; Tavesh im Finale |
| Vertrauen Kael | -2..2 | MQ_P02|MQ_A1_07|MQ_A2_*|MQ_A3_* | Kaels Umkehr (immer), Epilog Kael gerettet/an Venns Seite verloren (nie tot) |
| Respekt Sereth | -2..2 | MQ_A1_06|MQ_A2_*|MQ_A3_* | Sereths Angebot im Finale (immer möglich), Epilog Sereth versöhnt/gebrochen |
| Schuld beim Kontor | 0..1 | MQ_A1_05 | Marieke Holms Gefallen in Akt II |
| Starterlinie | Bloom|Stone|Storm | MQ_P01 | Kaels Starter (Vorteil), Dialogvarianten |
| Region der W2-Enthüllung | R02|R03|R06 | MQ_A1_06 | Ortsbezug späterer Dialoge |
| Umgang mit den Kontor-Kisten | 0..2 | MQ_A2_03 | 0 geliefert, 1 geöffnet und geliefert, 2 zurückgegeben; Mariekes Haltung in Akt III, Kontor-Ruf (K47) |
| Nähe zu Ysolde | -2..2 | MQ_A2_05|MQ_A2_08|MQ_A3_* | Dialoge in Akt III, Ysoldes Szene vor dem Finale (nur Ton, nie Inhalt) |
| Unterschlupf nach dem Verrat | FS|WW | MQ_A2_08 | FS bei FLAG_FS_STANCE ≥ 0, sonst WW (Wildwacht); Ortsbezug Akt III |
| Verrat erlebt (System) | 0..1 | MQ_A2_07 | Varianten der dritten freien Region (K45 §9); nicht vom Spieler wählbar |

| Entscheidung | Quest | Wirkung in Akt II | Wirkung später |
|---|---|---|---|
| Mariekes Kisten | MQ_A2_03 | Wissen um Stillsteine; Mariekes Ton | Kontor-Ruf (K47), Mariekes Hilfe in Nimbara (K46) |
| Kaldrex danken | MQ_A2_03 | FS_STANCE +1 | Unterschlupf, Epilog Freie Stimmen |
| Haltung zu Sereths Geschichte | MQ_A2_04 | SERETH_RESPECT | Sereths Angebot (immer möglich), Epilog |
| Haltung zu Ysolde | MQ_A2_05 | YSOLDE_BOND | Ysoldes Szene vor dem Finale |
| Antwort an Kael | MQ_A2_07 | KAEL_TRUST | Notizblock im Thronsaal, Kaels Umkehr-Szene |

**Regel (fortgeschrieben aus K44):** Keine Entscheidung in Akt II sperrt Inhalte oder verhindert Venns Fortschritt. Flags bestimmen *wer* hilft und *wie* Figuren sprechen – nie *ob* der Spieler weiterkommt.

---

## 11. Zwischensequenzen und Leitmotive

| Szene | Länge | Leitmotiv (K55) |
|---|---|---|
| Archiv: Wendelins Seite vierzig | 0:50 | Wendelin-Motiv (Spieluhr, erstmals) |
| Glaskoloss zerfällt | 0:25 | Sahrun-Thema (Oud-ähnliche Saiten, Wüstenwind) |
| Lagerbefreiung | 0:40 | Freie-Stimmen-Thema (Trommeln, Rufe) |
| Klangpest-Nachhall in Eiðvik | 1:30 | Stille-Motiv gegen Sturm-Thema, Kinderstimme |
| Sereths Geschichte | 1:20 | Orden-Thema (Glocken), Solo-Cello |
| Ysoldes Geständnis | 1:40 | Ilen-Motiv in Ysoldes Summen (die Melodie, die sie seit Akt I summt, ist Ilens) |
| Die Messung | 0:45 | Akademie-Thema (Streicher-Kanon), sechs Akkord-Glocken |
| Das Gewölbe | 2:10 | Akademie-Thema kippt in Moll; Krone-Motiv (erstmals: zehn Töne, gezwungen unisono) |
| Sereth am Stadtrand | 0:50 | Orden-Thema, gebrochen |
| Vision Maedryn/Ilen | 2:30 | Krone-Motiv → Ilen-Motiv (erstmals vollständig) → Pause (3 s Stille) |
| Kael nimmt den Splitter | 0:40 | Kael-Thema in Akademie-Instrumentierung |
| Neun von Zehn | 1:00 | Wärter-Thema, leise, mit Ysoldes Summen |

Das **Krone-Motiv** ist ein zehnstimmiger Unisono-Akkord – musikalisch das Gegenteil des Weltlied-Themas, das zehn verschiedene Linien verwebt. K55 legt fest, dass jede Krone-Variation dieselben zehn Töne nutzt.

---

## 12. Quest-Daten

| Name | Order | Region | Title | Prerequisite | Truth | Intensity | DurationMin | Boss | Akkord | Rewards |
|---|---|---|---|---|---|---|---|---|---|---|
| MQ_A2_01 | 1 | R01 | Die Schlösser der Stimmen | MQ_A1_09 | W4 | 4 | 60 |  |  | Wendelin-Tagebuch 1, Grabsattel-Bauplan |
| MQ_A2_02 | 2 | R04 | Die Wahrheit unter dem Sonnenhof | MQ_A2_01 | – | 7 | 180 | BOSS_A2_01 | ARN_04 | Akkord Sonnenhof, Grabreiten |
| MQ_A2_03 | 2 | R05 | Das Kraterherz | MQ_A2_01 | – | 6 | 170 |  | ARN_05 | Akkord Schmiede, Kontor-Gefallen |
| MQ_A2_04 | 2 | R07 | Eiðvik | MQ_A2_01 | – | 8 | 200 | BOSS_A2_02 | ARN_07 | Akkord Polarlicht, Schweigfels-Zugang |
| MQ_A2_05 | 3 | dynamisch | Was Ysolde verschwieg | 2 Akt-II-Akkorde | W5 | 5 | 50 |  |  | Ilens Nachklang (Resonanzsinn II) |
| MQ_A2_06 | 4 | R08 | Die Messung | 6 Akkorde | – | 4 | 60 |  |  | Flugsattel, Akademie-Zugang |
| MQ_A2_07 | 5 | R08 | Der Verrat | MQ_A2_06 | W6 | 9 | 90 |  |  | – |
| MQ_A2_08 | 6 | dynamisch | Unter Freunden | MQ_A2_07 | – | 3 | 60 |  |  | Lager der Verbündeten, Hain-Erweiterung |
| MQ_A2_09 | 7 | R08 | Glyphen von Dorunsruh | MQ_A2_08 | – | 6 | 150 |  | ARN_08 | Akkord Glyphe |
| MQ_A2_10 | 8 | R08 | Der Thronsaal | 8 Akkorde | W7 | 9 | 120 | BOSS_A2_03 |  | Stimmsiegel Ka'thurel, Klangfragment Ilen |
| MQ_A2_11 | 9 | R08 | Neun von Zehn | MQ_A2_10 | – | 2 | 45 |  |  | Prismtiefen-Zugang, Akt III |

### 12.1 Quest-Zusammenfassungen

| Name | Title | Summary |
|---|---|---|
| MQ_A2_01 | Die Schlösser der Stimmen | Eichenhall-Archiv: Hralda und Ysolde zeigen Wendelin Aars Notizen – Arenen über den Schlafstätten, Akkorde als Schlüssel; Öffnung von R04/R05/R07 |
| MQ_A2_02 | Die Wahrheit unter dem Sonnenhof | Wanderdorf Ashurim, Glasebene, Glaskoloss der Weite; Shirah Harrad; Ash'kareth regt sich und zeigt eine Wahrheit, die der Spieler noch nicht versteht |
| MQ_A2_03 | Das Kraterherz | Schlackenwehr; Mariekes Gefallen (versiegelte Kisten); Freie Stimmen befreien Arbeits-Echos; Kaldrex Vorn; Pyr'thagon im Schlaf |
| MQ_A2_04 | Eiðvik | Ruinen von Eiðvik (Klangpest 948), Kloster Schweigfels, Sereths Geschichte; Venns Schatten im Eis; Sigrun Fjall |
| MQ_A2_05 | Was Ysolde verschwieg | In der zweiten Akt-II-Region erzählt Ysolde am Lagerfeuer die Wahrheit: der Spieler trägt Ilens Nachklang, sie wusste es seit Lindwiesen |
| MQ_A2_06 | Die Messung | Kael lädt nach Dorunsruh ein; Venn bittet, die sechs Akkorde zu messen; Flugreiten wird freigeschaltet |
| MQ_A2_07 | Der Verrat | Die Messung war eine Karte: sechs Kronensplitter liegen in Venns Gewölbe; der Orden hat sie in seinem Auftrag geborgen; Sereth erfährt es zeitgleich; Flucht aus Dorunsruh |
| MQ_A2_08 | Unter Freunden | Atemzug: Unterschlupf bei Freien Stimmen oder Wildwacht (FLAG_FS_STANCE); Sereth bittet um ein Gespräch; Plan für Ael'Dorun |
| MQ_A2_09 | Glyphen von Dorunsruh | Arena unter Akademie-Aufsicht; Aevrin Thal verweigert Venn den Zutritt; Thae'Luun und Säulenrast; Weg zum Thronsaal |
| MQ_A2_10 | Der Thronsaal | Thronsaal-Gewölbe; Kronensplitter-Wächter; Vision Maedryns und Ilens: die Große Stille war Ilens bewusste Tat; Kael nimmt den Splitter für Venn |
| MQ_A2_11 | Neun von Zehn | Abend auf den Säulen; Venn besitzt neun Splitter, der zehnte ruht in Prismara; Ysolde, Hralda, Tavesh/Marieke, Sereth – ein Rat; Aufbruch nach Prismtiefen |

### 12.2 Dialogvarianten nach Haltung (Akt II)

| Zeile | Situation | Einfühlsam | Neugierig | Entschlossen | Flag-Effekt |
|---|---|---|---|---|---|
| DLG_A2_01_02 | Wendelins Seite vierzig | „Sie hatte Angst vor dem, was sie gebaut hat.“ | „Wer hat die anderen Seiten?“ | „Wir sammeln die Schlüssel zuerst.“ | – |
| DLG_A2_02_03 | Ashurims Älteste fragt, warum der Spieler sucht | „Damit die Echos wieder singen.“ | „Weil ich wissen will, was darunter liegt.“ | „Weil es sonst jemand anderes tut.“ | – |
| DLG_A2_02_05 | Shirah über Ash'kareths Wahrheit | „Manche Wahrheiten tun weh.“ | „Was hat sie mir gezeigt?“ | „Dann soll sie mir alles zeigen.“ | – |
| DLG_A2_03_02 | Marieke übergibt die Kisten | „Ich vertraue dir.“ | „Was ist drin?“ | „Ich trage, aber ich schaue nach.“ | KONTOR_CRATES (Wahl folgt) |
| DLG_A2_03_06 | Kaldrex sieht weg | „Danke, dass Ihr weggesehen habt.“ | „Wer betreibt das Lager?“ | „Nächstes Mal seht Ihr hin.“ | FS_STANCE +1 / 0 / 0 |
| DLG_A2_04_03 | Sereth erzählt von Eiðvik | „Es tut mir leid.“ | „Wer hat Euch die Steine beigebracht?“ | „Ein Wiegenlied, das Stimmen nimmt.“ | SERETH_RESPECT +1 / +1 / 0 |
| DLG_A2_05_01 | Ysoldes Geständnis | „Du hast mich beschützt.“ | „Was kann der Nachklang?“ | „Du hättest es sagen müssen.“ | YSOLDE_BOND +1 / 0 / −1 |
| DLG_A2_06_02 | Venn lobt das Vertrauen | „Ich glaube an Hilfe.“ | „Was genau messt ihr?“ | „Machen wir es kurz.“ | – |
| DLG_A2_07_04 | Venns Angebot | „Das gibt dir nicht das Recht.“ | „Was geschieht mit den Stimmen?“ | „Ich halte dich auf.“ | – |
| DLG_A2_07_06 | Kael wählt Venn | „Ich sehe dich auch.“ | „Was siehst du jetzt?“ | „Komm mit mir.“ | KAEL_TRUST +1 / 0 / ±1 |
| DLG_A2_08_03 | Sereth bittet um ein Gespräch | Zuhören, bis sie fertig ist | „Welchen Ton braucht er?“ | „Kämpfst du jetzt mit uns?“ | SERETH_RESPECT +1 / 0 / 0 |
| DLG_A2_10_04 | Kael im Thronsaal | „Du hast es auch gesehen.“ | „Was wirst du ihm sagen?“ | „Leg ihn hin, Kael.“ | – (Verhalten nach KAEL_TRUST) |
| DLG_A2_11_02 | Rat auf der Terrasse | „Wir gehen zusammen.“ | „Was passiert mit mir?“ | „Wir gehen. Morgen.“ | YSOLDE_BOND +1 / 0 / 0 |

Regeln wie K44 §10.2 (gleiche Länge, keine Ankündigung, eigene Reaktion je Haltung, Echos nonverbal).

### 12.3 Begegnungs- und Belohnungstakt

| Abschnitt | Kämpfe (Pflicht) | Kämpfe (optional) | Bindungsgelegenheiten | Neue Systeme | Ziel-Spielzeit |
|---|---|---|---|---|---|
| MQ_A2_01 | 0 | 2 | 2 | Wendelin-Tagebuch, Grabsattel | 1 h |
| Freie Regionen (3) | je 6 (+ Boss in R04/R07) | je 14 | je 9 | Grabreiten, Lagerbefreiung, Klangpest-Nachhall | je 3 h |
| MQ_A2_05 | 0 | 0 | 0 | Resonanzsinn II | 0,8 h |
| MQ_A2_06–08 | 5 (Flucht) | 3 | 2 | Flugreiten, gemischte Ordensgegner | 3,5 h |
| MQ_A2_09–11 | 4 + Boss | 8 | 6 | Stimmsiegel Ka'thurel, Raid-Zugang (Rang 22) | 5 h |
| **Summe Akt II** | **~29** | **~55** | **~37** | | **~20 h** |

Wärter-EP Akt II: ~40.000 bei 2.000 EP/h (K43 §3.1) → Rang 16 → ~24.

### 12.4 Wahrheitsebenen und Lore-Freigaben

| Ebene | Quest | Freigegebene Lore (Auszug) | Verzerrt bis dahin |
|---|---|---|---|
| W4 | MQ_A2_01 | Wendelin-Tagebuch 1–20, Arenen-Glyphen, Kodex-Einträge der Ursprungsstimmen (Seite 2) | Klangfragmente über „Türen“ und „Schläfer“ |
| W5 | MQ_A2_05 | Ilens Blutlinie, Nachklang-Einträge, Ysoldes Briefe (rückwirkend lesbar) | Fragmente mit Ilens Stimme |
| W6 | MQ_A2_07 | Kronensplitter (Kodex), Venns Akte, Lieferscheine, Ordensformel | „Kristallkern“, „Stillstein-Rohstoff“ |
| W7 | MQ_A2_10 | Maedryns Herrschaft, Ilens Frage, Erstchor-Gelöbnis | Alle Fragmente zur Großen Stille |

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | Wanderdorf Ashurim als mobile Siedlung (3 Lagerplätze, wöchentlicher Wechsel); Lager am Kraterrand mit drei Heilkreisen; Ruinen von Eiðvik mit Nachhall-Pfad; Akademie-Gewölbe und Fluchtroute über die Säulen; Thronsaal-Gewölbe | K57 |
| Combat | Ordenstrupp-Encounter (Zone +2), NPC-Begleiter Ulrek in Phase 3 von BOSS_A2_02 (Variante nach der Wende) | K34/K35 |
| Audio | Krone-Motiv, Wendelin-Motiv, Ilen-Motiv vollständig, Klangpest-Nachhall-Mix | K55 |
| Cinematics | 12 Sequenzen (§11), Vision im Thronsaal mit Echtzeit-Übergang in die Gegenwart | K56/K58 |
| UI | Glaskarte der Messung (6/7 Punkte), Splitterzähler erscheint erst nach W6 im Kodex | K54 |
| Sensitivity | Review Sahrun-Weite und Hvitfell (Ashurim, Sonnenhöfe, Eiðvik-Trauer) | K66 |
| Daten | `MainQuests.csv` (MQ_A2_01–11), `StoryFlags.csv` (+3), Lore TruthLevel 4–7 | K48 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-164 | Die Wende (W6) hängt an der Akkordanzahl (6), nicht an einer Region | Freie Reihenfolge bleibt erhalten; jeder Spieler erlebt den Verrat nach gleich viel Vertrauensaufbau | Verrat fest in Hvitfell |
| ADR-165 | Spielerentscheidungen verhindern Venns Splitterfortschritt nie | Tragik der Wende: der Spieler hat geholfen, ohne es zu wissen; Entscheidungen färben Wissen und Beziehungen | Splitter durch Wahl rettbar (würde Akt III verzweigen) |
| ADR-166 | Unterschlupf nach dem Verrat abhängig von `FS_STANCE` | Frühere Haltung wird sichtbar, ohne Inhalte zu sperren | Fester Unterschlupf |
| ADR-167 | Kael nimmt den achten Splitter in einer nicht spielbaren Szene | Kael bleibt Figur, kein Boss; DR-09; „Kael stirbt nie“ (CANON §37) | Bosskampf gegen Kael |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §172 | Akt-II-Struktur: Auftakt (W4) → R04/R05/R07 frei → W5 nach 2. Akt-II-Akkord → Messung/Verrat bei 6 Akkorden (W6) → Arena Dorunsruh + 3. Region → Thronsaal bei 8 Akkorden (W7); ~20 h; Rang ~24 | LOCKED |
| §173 | Akt-II-Quests MQ_A2_01–11 (`MainQuests.csv`) | LOCKED |
| §174 | Kronensplitter: einer je Stimme, durch Akkorde hörbar; Venn hält am Ende von Akt II neun (Aerion seit 983, acht über Orden/Kontor/Kael); der zehnte in Prismara | LOCKED |
| §175 | Flags Akt II: KONTOR_CRATES (0–2), YSOLDE_BOND (−2…2), SHELTER (FS/WW) | LOCKED |
| §10 | ADR-164 – ADR-167 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Logline, Thema und Ton von Akt II
- [x] Struktur mit freier Regionsreihenfolge, Intensitätskurve (DR-29), Spielzeit, Rang
- [x] Figuren und ihre Bögen in Akt II
- [x] Kronensplitter-Logik (wer, wo, wann; Zählregel neun von zehn)
- [x] 11 Hauptquests mit Szenen, Dialogen und Entscheidungen
- [x] W4, W5, W6, W7 an festen Auslösern
- [x] Dynamische Erzählung (6 Reihenfolgen, Varianten nach der Wende)
- [x] Flags, Zwischensequenzen, Leitmotive, Lore-Freigaben
- [x] Quest-Daten, Anforderungen, ADR-164 – ADR-167, CANON §172–§175

➡️ **Nächstes Kapitel: K46 – Story III: Akt III „Das neue Lied“ und Enden.**
