# K46 · Story III – Akt III, Finale und Enden: „Das neue Lied“

| Feld | Wert |
|---|---|
| Dokument | Kapitel 46 von 68 · Narrative Bible, Teil III |
| Version | 1.0 |
| Owner | Narrative Director |
| Mitwirkende | Lead Writer, Quest Designer, Cinematics Director, Level Design (Prismtiefen, Nimbara), Audio (Finale-Partitur), Combat Designer (Krone, Velnox), World Tech (Data Layers Nachhall), UX (Entscheidungsmoment) |
| Baut auf | K07 §13 (W8, W9, Enden), K35 §7 (BOSS_A3_01–03), K44 §168–§171, K45 §172–§175, CANON §34 (Stimmen, Velnox), §38 (Enden), §43 (Data Layers), §63 (Resonanzsturm), DR-09, DR-19 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Quests/MainQuests.csv` (+9 Quests MQ_A3_01–09; gesamt 32 Hauptquests), `Data/Quests/StoryFlags.csv` (+2 Flags), `tools/authoring/story_k46.py` (Epilog-Matrix) |
| Neue Kanon-Einträge | CANON §176 (Akt III), §177 (Finale), §178 (Enden und Weltzustand), §179 (Epilog-System), §180 (Hauptstory gesamt) |

---

## Inhalt

1. [Akt III in einem Satz](#1-akt-iii-in-einem-satz)
2. [Struktur und Intensität](#2-struktur-und-intensität)
3. [Figuren in Akt III](#3-figuren-in-akt-iii)
4. [Prismtiefen](#4-prismtiefen)
5. [Nimbara](#5-nimbara)
6. [Das Finale: Die Große Pause](#6-das-finale-die-große-pause)
7. [Die zwei Enden](#7-die-zwei-enden)
8. [Epilog-System](#8-epilog-system)
9. [Nachhall: Übergang ins Post-Game](#9-nachhall-übergang-ins-post-game)
10. [Zwischensequenzen und Partitur](#10-zwischensequenzen-und-partitur)
11. [Quest-Daten](#11-quest-daten)
12. [Hauptstory gesamt](#12-hauptstory-gesamt)
13. [Anforderungen an andere Abteilungen](#13-anforderungen-an-andere-abteilungen)
14. [Decision Records](#14-decision-records)
15. [Kanon-Änderungen](#15-kanon-änderungen)
16. [Kapitel-Checkliste](#16-kapitel-checkliste)

---

## 1. Akt III in einem Satz

> *Der Wärter bringt den letzten Schlüssel genau dorthin, wo sein Gegner ihn haben will, weil die Pause ohnehin erwacht – und entscheidet im Angesicht der Stille, ob er das, was ihn hören lässt, zurückgibt.*

**Thema des Akts:** *Verzicht.* Ilen gab ihren Körper, Ysolde ihr Schweigen, Sereth ihren Glauben an einen Mann, Kael seinen Platz neben ihm. Am Ende gibt der Spieler – vielleicht – seine Gabe. Akt III zeigt, dass jede dieser Gaben etwas kostet und etwas ermöglicht.

**Ton:** feierlich, hell und ernst. Prismtiefen ist schön und gefährlich (Glas, Licht, Missklang), Nimbara ist erhaben und leer (Himmel, Wind, verlassene Werften). Der Humor kehrt im Lager (MQ_A3_04) und im Epilog zurück – als Erleichterung, nicht als Witz.

---

## 2. Struktur und Intensität

| Abschnitt | Region | Akkorde (gesamt) | Wahrheit | Spielzeit |
|---|---|---|---|---|
| Prismtiefen | R09 (fest 50–62) | 9 | W8 | 4,8 h |
| Atemzug | R09 Kristallsee | 9 | – | 0,7 h |
| Nimbara | R10 (fest 58–70) | 10 | – | 3,5 h |
| Finale | R10 Kronenwerft, Himmel über Nimbara | 10 | W9 | 2,3 h |
| Epilog | R01 Lindwiesen | 10 | – | 0,7 h |
| **Summe** | | **+2** | **W8, W9** | **~12 h** |

Akt III ist **linear** (CANON §15): Prismtiefen vor Nimbara, beide mit fester Stufe (ADR-044). Der Spieler kann jederzeit in alle früheren Regionen zurück; die Story wartet. Wärterrang am Ende: **~29** (K43 §3.1; CANON §15 Ziel ~28 ✓). Echo-Level am Finale: **68–70** (CANON §15).

```
Intensität (1–10) über Akt III
10 ┤                                                              ███ Große Pause
 9 ┤                                                    ███ Krone
 8 ┤          ███ Missklang
 7 ┤                                          ██ Sternenarena
 6 ┤                 ██ Prismara   ██ Aufstieg
 5 ┤ ██ Hinab
 4 ┤
 3 ┤
 2 ┤                         ██ Letzte Nacht                              ██ Nachhall
 1 ┼────────────────────────────────────────────────────────────────────────────────
     A3-01  A3-02   A3-03   A3-04   A3-05   A3-06   A3-07    A3-08     A3-09
```

**DR-29-Ausnahme (ADR-168):** Zwischen *Die Krone* (9) und *Die Große Pause* (10) liegt **keine** Ruhephase ≥ 20 min. Das Finale ist ein durchgehender Bogen. Ausgleich: Vor MQ_A3_07 steht ein expliziter **Point of no Return** mit Lager-Angebot, und zwischen den beiden Kämpfen liegt eine 3-minütige nicht-interaktive Sequenz (Kael, Venn, der Riegel bricht), in der volle Heilung erfolgt.

---

## 3. Figuren in Akt III

| Figur | Rolle in Akt III | Abschluss |
|---|---|---|
| **Ysolde Varn** | Begleitet den Spieler bis Nimbara (erstmals dauerhaft an seiner Seite) | Übergibt einen versiegelten Brief; im Epilog gelesen |
| **Kael Duran** | Venns Rechte Hand bis zur Kronenwerft | **Umkehr** bei < 15 % von BOSS_A3_02 (immer); Epilog nach `KAEL_TRUST` |
| **Aldric Venn** | Antagonist; setzt die Krone auf | Überlebt; die Krone zerbricht; Epilog nach Ende |
| **Sereth Vaun** | Verbündete auf Zeit; trägt das Angebot der „Sanften Stille“ | Steht in Phase 4 neben dem Spieler; Epilog nach `SERETH_RESPECT` |
| **Hralda Brakk** | Führt die Wildwacht-Späher in Nimbara | Bundesrat-Szene im Epilog |
| **Tavesh Amaru** | Freie Stimmen sichern die Windanker (bei `FLAG_SHELTER` = FS) | Epilog nach `FS_STANCE` |
| **Marieke Holm** | Liefert Ausrüstung per Luftschiff-Fracht (bei `KONTOR_CRATES` ≥ 1) oder Geld (0) | Epilog: Kontor-Vignette (Ton nach Flag) |
| **Ilyx Brannoc** | Arenameister Prismara (Nachfahre der Lauscherin Brannoc) | Hilft im Missklang mit Kristall-Echos |
| **Oruma Siyel** | Arenameisterin Aerion, Sternwarte | Liest Velnox' Erwachen am Himmel |
| **Ilen** | spricht im Finale durch den Spieler | Verabschiedet sich |
| **Velnox** | Die Große Pause | Kehrt als Pause ins Lied zurück oder umhüllt es sanft |

---

## 4. Prismtiefen

### MQ_A3_01 · Hinab nach Prismara (Intensität 5)

Die **Liftstation Kraterrand** senkt den Spieler in den Krater. Unter dem Glasdach liegt **Prismara**: eine Stadt aus gefärbtem Glas, in der das Licht hörbar ist (jede Farbe ein Ton; Audio-Gimmick K55). **Ilyx Brannoc**, Arenameister und Nachfahre der Lauscherin, führt durch Glanzschacht und Quarzgrund.

> **Ilyx:** „Meine Ahnin hat ein Echo gezähmt, indem sie drei Tage neben ihm saß. Ich sitze seit drei Wochen neben dem Missklang. Er wird nicht zahmer. Er wird lauter.“

Seit Akt II herrscht in Prismara eine **Energiekrise** (`DL_Story_EnergyCrisis`, CANON §54): Die Kristalle, die die Stadt beleuchten, flackern im Takt eines fremden Pulses. Ilyx hört schwach Grundfrequenzen – als einziger Mensch außer dem Spieler – und erkennt in ihm sofort einen Verwandten im Gehör. Die **Missklang-Adern** – kristallisierte Reste der Krone von −20 v.St. – pulsieren seit Wochen. Ilyx weiß nicht warum; der Spieler schon: Neun Splitter, an einem Ort versammelt, singen (K45 §4).

### MQ_A3_02 · Der versteinerte Missklang (Intensität 8)

Über die **Missklang-Wacht** in die tiefsten Adern. Hier ist der Missklang nicht Erinnerung, sondern Körper: **Missgrath**, die **Missklang-Hydra** (BOSS_A3_01, Lv. 62), spaltet sich in zwei Hälften, die binnen zwei Runden fallen müssen (K35 §7).

**W8 enthüllt** – je nach Vorgeschichte aus zwei Quellen (ADR-169):

| Bedingung | Quelle | Inhalt |
|---|---|---|
| `KAEL_TRUST` ≥ 1 | **Kaels Notizblock** aus dem Thronsaal (K45 MQ_A2_10) – der Spieler kann ihn erst jetzt mit dem Missklang als Schlüssel lesen | Venns Ritualplan in Kaels Handschrift, mit Randnotizen: *„Riegel muss brechen?? Er hat nicht gesagt, dass —“* |
| sonst | **Sereths Kundschafter** (Sereth-treue Ordensleute in Venns Gefolge) | Mündlicher Bericht; derselbe Inhalt, ohne Kaels Zweifel |

**W8:** Venn will die Krone in **Nimbara** aktivieren, an der Kronenwerft, wo sie schon einmal klang. Damit zehn Stimmen in einen Ton gezwungen werden können, muss Ilens **Riegel** brechen – sonst bleibt ein Teil jeder Stimme in der Pause gebunden. Bricht der Riegel, ist **Velnox** frei. Venn glaubt, die vollständige Krone könne auch die Pause stimmen.

> **Ysolde:** „Er glaubt, er kann die Stille dirigieren.“
> **Sereth:** „Niemand dirigiert die Stille. Man kann sie nur einladen oder bitten zu gehen.“

### MQ_A3_03 · Das neunte Schloss (Intensität 6)

Arena **Prismara** (fest Stufe 9, Brechungs-Regel). Mit dem neunten Akkord öffnet sich die **Resonanzkammer**; **Prism'aion** erwacht halb, und der **zehnte Splitter** hebt sich aus dem Kristall – aber nur in die Hand des Spielers. Er löst sich für niemanden sonst: Er ist auf die Stimme gestimmt, und die Stimme vertraut nur dem Nachklang.

Die Gruppe diskutiert, ob man den Splitter zerstören kann. Ilyx versucht es mit allem, was Prismara hat: Der Splitter singt nur lauter. **Kronensplitter brechen erst, wenn die Krone singt** (ADR-170).

> *(einfühlsam)* „Dann trage ich ihn, und niemand anderes muss es.“ · *(neugierig)* „Was, wenn ich ihn in der Kammer lasse?“ · *(entschlossen)* „Dann bringen wir ihn zu Venn – und brechen die Krone mit ihm.“

Die neugierige Antwort zeigt eine kurze Sequenz: Der Spieler legt den Splitter zurück, und die Missklang-Adern beginnen sofort zu wachsen. Ysolde: „Der Riegel bricht ohnehin. Mit oder ohne Krone. Die Frage ist, wer dann dort steht.“

### MQ_A3_04 · Die letzte Nacht am Boden (Intensität 2)

Lager am **Kristallsee**. Der wichtigste Atemzug der Hauptstory: Alle Verbündeten sind da (Zusammensetzung nach Flags), der ganze Chor des Spielers liegt um das Feuer. Jede Figur bietet ein Gespräch an; keines ist Pflicht.

| Gespräch | Inhalt | Flag-Wirkung |
|---|---|---|
| Ysolde | Erzählt von ihrer letzten Arena-Verteidigung 996 – sie hörte auf, weil sie den Nachklang im Spieler zum ersten Mal deutlich hörte und Angst hatte, jemand anderes könnte es auch | `YSOLDE_BOND` +1 bei Zuhören bis zum Ende |
| Sereth | Fragt, ob der Spieler sich vorstellen kann, dass Stille eine Gnade ist | `SERETH_RESPECT` +1 bei einfühlsamer oder neugieriger Antwort |
| Hralda | Erzählt, wie sie Ysolde kennenlernte (Hralda verlor einen Ringkampf um einen Sattel) | – |
| Tavesh (FS) / Späher (WW) | Die befreiten Echos aus Ignareth singen | `FS_STANCE` +1 bei einfühlsamer Antwort |
| Ilyx | Eine Lauscher-Übung: drei Minuten nur zuhören | Kodex-Eintrag *Die Geduld der Brannoc* |
| Starter-Echo | Eigene Szene (K44 §2): Es legt sich auf den versiegelten Brief | – |

Vor dem Schlafen übergibt Ysolde den **Brief**: *„Öffne ihn erst, wenn du entschieden hast. Nicht vorher. Versprich es.“* (Der Brief liegt im Inventar, nicht öffnbar; Text in §8.4.)

---

## 5. Nimbara

### MQ_A3_05 · Aufstieg nach Nimbara (Intensität 6)

Mit dem Flugsattel durch die **Windbänder** zu den Himmelsinseln, die Orh'gruuns Schwerkraft vor über tausend Jahren hob. **Lumeya** und **Wolkenrast** sind fast leer – die Nimbari haben sich vor dem Sturm in die Windanker zurückgezogen. Die **Kronenwerft-Wacht** ist von Venn-treuen Ordensleuten besetzt. Bei `FLAG_SHELTER` = FS sichern die Freien Stimmen die Windanker, sonst die Wildwacht-Späher; beide melden: „Er wartet auf dich.“

Gameplay: Flug-Traversal mit Windböen (K40), drei Ordensposten (gewaltfrei umgehbar oder kämpfbar, DR-14), Aktivierung der Nimbara-Resonanzsteine.

### MQ_A3_06 · Die Sternenarena (Intensität 7)

**Oruma Siyel**, Arenameisterin von Aerion, hat die Sterne seit Wochen beobachtet: Über Nimbara fehlen Sterne – nicht verdeckt, sondern *still*. Sie lässt den Spieler antreten (fest Stufe 10, Sternfall-Regel), weil „ein zehnter Akkord in deiner Hand besser ist als in seiner“.

Aerion ist seit der Großen Stille isoliert; in der Halle der Baumeister steht die **Wand der Zehn** – zehn Reliefs des Erstchors, nur ein Gesicht ist erhalten: **Ilens**. Der Spieler erkennt die Frau aus den Visionen; Ysolde berührt das Relief und sagt nichts. (Die Nebenquest „Wendelins letzter Stein“ (SQ_198, K51) – erloschener Resonanzstein, K12 – wird hier angeboten.)

Mit dem **zehnten Akkord** erwachen **alle zehn Stimmen** gleichzeitig: Über ganz Aethris steigen Licht- und Klangsäulen auf (globale Sequenz, alle Regionen sichtbar). **Aeth'rion**, die Leitstimme, erhebt sich über der Arena – und hält inne. Von der Kronenwerft antworten **neun Splitter** dem zehnten im Gepäck des Spielers. Ein **Resonanzsturm** bricht über ganz Aethris los (CANON §63, Finale-Auslöser) und hält bis zum Ende von MQ_A3_08 an.

**Point of no Return:** Vor dem Weg zur Kronenwerft fragt das Spiel einmal, ob der Spieler bereit ist (Lager und Händler verfügbar; Hinweis, dass ein **Finale-Speicherpunkt** angelegt wird – §9.2).

### MQ_A3_07 · Die Krone (Intensität 9)

Die **Kronenwerft**: eine Plattform aus dorunischem Stein über den Wolken, in deren Mitte der Ring steht, in dem Maedryn die Krone aktivierte. **Venn** wartet mit **Kronvaal**, dem Thronhüter-Echo, und neun Splittern in einem Reif aus Glas. Kael steht hinter ihm.

> **Venn:** „Du hast ihn mitgebracht. Ich wusste es. Nicht weil du schwach bist – weil du hörst, dass die Pause kommt. Mit oder ohne mich. Ich biete dir nur an, dass jemand sie dirigiert.“
> *(einfühlsam)* „Du willst, dass niemand mehr leidet. Ich auch.“ · *(neugierig)* „Was, wenn die Pause sich nicht dirigieren lässt?“ · *(entschlossen)* „Nimm die Krone ab.“
> **Venn** (auf die neugierige Frage): „Dann war ich der Letzte, der es versucht hat. Auch das ist eine Antwort.“

Venn setzt die Krone auf. Der **zehnte Splitter** wird aus dem Gepäck des Spielers gerissen und fügt sich ein. Die zehn Stimmen schreien einmal auf – und verstummen im erzwungenen Unisono (Krone-Motiv, K45 §11). Der Chor des Spielers erstarrt für einen Herzschlag, dann löst ihn der **Nachklang**: Was in Ilens Blutlinie klingt, kann die Krone nicht stimmen.

**Kampf:** BOSS_A3_02 **Aldric Venn mit der Resonanzkrone** (Kronvaal, Lv. 68, K35 §7): Klangpanzer + Taktraub, Stillezähler mit Venns Monolog (Venns Regel), Resonanzflut als Crescendo-Duell. Bei **< 15 %** greift **Kael** ein (immer, ADR-171):

> **Kael:** „Du hast gesagt, es geht um Ordnung. Hör sie dir an! Das ist keine Ordnung, das ist ein Käfig, der singt!“

Kael richtet seinen Resonometer gegen die Krone – die Messung, mit der Venn die Splitter fand, in umgekehrter Richtung. Die Krone springt. Venn sinkt auf die Knie; Kronvaal löst sich (kein Tod, ADR-007). Die Stimmen sind frei – aber der **Riegel** ist mit der Krone gebrochen.

**Zwischensequenz (3 min, volle Heilung):** Kael kniet neben Venn. Ysolde zieht den Spieler weg. Über Nimbara öffnet sich der Himmel nach innen: kein Loch, sondern eine **Pause** – das Licht hört auf zu klingen. **Velnox** ist frei.

> **Venn** (leise, zu Kael): „Ich wollte nur, dass es aufhört.“
> **Kael:** „Ich weiß. Es hört auf. Nur nicht so.“

---

## 6. Das Finale: Die Große Pause

### MQ_A3_08 · Die Große Pause (Intensität 10)

**BOSS_A3_03 Velnox** (Lv. 70, K35 §7). Der Kampf findet auf den zerbrechenden Inseln Nimbaras statt; Gleit-Übergänge zwischen den Phasen (Traversal als Teil des Finales).

| Phase | HP | Was geschieht | Erzählung |
|---|---|---|---|
| 1 | 100–75 % | Stillepuls, Schwerebrunnen: die Welt verstummt; das HUD verliert Ton-Indikatoren | Velnox ist nicht böse – eine Pause, die zu lange gehalten wurde |
| 2 | < 75 % | Die **zehn Stimmen** antworten: je Runde eine Resonanzflut einer anderen Klangfarbe für den Spieler | Die Stimmen kämpfen *mit* dem Spieler, weil er sie gefragt hat (Akkorde) |
| 3 | < 50 % | Stillezähler 3; bei 0 „Große Pause“ (Harmonie 0, Stillefeld) | Ilens Stimme wird hörbar, erst verzerrt (L-01), dann klar |
| 4 | < 25 % | **Kein HP-Kampf mehr.** Die Entscheidung | W9 |

**Phase 4 – Die Entscheidung.** Der Kampf hält an. Die Welt ist grau, nur der Spieler und sein Chor tragen Farbe. **Ilen** spricht – nicht als Vision, sondern *durch* den Spieler: Die Stimme des Spielercharakters wird von Ilens Stimme überlagert (beide Sprecherstimmen, K55).

> **Ilen (durch den Spieler):** „Ich habe sie schlafen lassen, bis jemand kommt, der fragt. Du hast gefragt. Zehnmal. Jetzt ist der Riegel fort, und was von ihm übrig ist, klingt in dir.“
> **Ilen:** „Gib mir zurück, was ich dir geliehen habe, und ich gebe es den Stimmen. Dann ist die Pause wieder ein Atemzug zwischen zwei Tönen. Nicht das Ende des Lieds. Aber du wirst nicht mehr hören, was du gehört hast.“

**W9 enthüllt:** Das Lied kann nur frei neu erklingen, wenn der Nachklang zurückgegeben wird – und der Spieler verliert dabei die Gabe, Grundfrequenzen zu hören.

**Sereth** tritt neben den Spieler (immer, unabhängig von `SERETH_RESPECT`; ADR-172). Sie trägt keinen Stillstein mehr.

> **Sereth:** „Es gibt einen zweiten Weg. Lass Velnox das Lied umhüllen. Nicht verschlingen – umhüllen. Die Stimmen schlafen wieder, für immer, und kein Lied wird je wieder zu laut. Kein Eiðvik mehr. Und du behältst, was du bist.“

**Ysolde** sagt nichts. Sie sieht den Spieler an; ihr Brief ist in seiner Tasche.

**UX der Entscheidung (ADR-173):**

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│         ◯ Den Nachklang zurückgeben                                │
│           „Lass sie frei singen.“                                  │
│                                                                    │
│         ◯ Sereths Angebot annehmen                                 │
│           „Lass sie ruhen.“                                        │
│                                                                    │
│   [Halten zum Bestätigen – 3 s]     Keine Zeitbegrenzung           │
└────────────────────────────────────────────────────────────────────┘
```

- Keine Zeitbegrenzung; der Kampf pausiert, Musik hält einen einzigen Ton.
- Bestätigen per **Halten** (3 s), Abbruch durch Loslassen; kein versehentliches Wählen.
- Keine Moral-Anzeige, keine Belohnungsvorschau. Beide Optionen sind gleich groß, gleich gesetzt, abwechselnd oben (zufällig pro Spielstand, Seed-Fork 4 nicht berührt – eigene UI-Zufallsquelle).
- Vor der Bestätigung kann der Spieler mit jedem Chor-Echo „sprechen“ (nonverbale Reaktion) – Abschied oder Ermutigung, je nach Bindungsstufe (K37).

---

## 7. Die zwei Enden

### 7.1 „Neues Lied“ (kanonisch)

Der Spieler legt die Hand auf die Brust; ein Ton löst sich – Ilens Ton und sein eigener, ineinander. Er steigt zu den zehn Stimmen auf, und die Stimmen singen **zehn verschiedene Linien** (Weltlied-Thema, erstmals vollständig und frei). Velnox schrumpft nicht und stirbt nicht: Er wird zur **Pause zwischen den Tönen** – man hört ihn nur, weil die Töne um ihn herum klingen.

Die Stillezonen heilen überall gleichzeitig (Data Layer `DL_Story_R##_Healed` für alle Regionen). Der Spieler hört zum letzten Mal die Grundfrequenzen – und dann nur noch Klang. Sein **Resonanzsinn** wird zum **Resonator-Sinn** (technisch über den Resonator; spielmechanisch identisch, CANON §38).

> **Ilen:** „Danke, dass du gefragt hast.“
> *(Stille. Dann: Vogelgesang, Wind, Echos. Ganz normale Geräusche.)*

### 7.2 „Sanfte Stille“

Der Spieler nickt Sereth zu. Sereth legt die Hand auf Velnox' Rand und summt – das Wiegenlied aus Eiðvik, das ihre Mutter sang. Velnox breitet sich aus, nicht als Riss, sondern als **Decke**. Die zehn Stimmen sinken zurück in den Schlaf, diesmal ohne Riegel und ohne Schloss: Sie werden nicht mehr erwachen. Die Echos der Welt bleiben, freundlich und ruhig; neue Evolutionen der Stimmen gibt es nicht (K07 §13.1).

Die Stillezonen verlieren ihre Feindseligkeit: Grau wird zu Silber, verstummte Echos erwachen still (Data Layer `DL_Story_R##_Healed` mit Material-Variante „Silber“, ADR-174). Der Spieler **behält** den Resonanzsinn – er hört jetzt das langsame, gleichmäßige Atmen schlafender Stimmen.

> **Sereth:** „Es ist nicht das Lied, das du wolltest. Aber kein Kind wird mehr schreien.“
> **Ilen** (ganz leise, ein letztes Mal): „…dann schlaft.“

### 7.3 Was beide Enden gemeinsam haben

| Aspekt | Neues Lied | Sanfte Stille |
|---|---|---|
| Velnox | Pause im Lied; im Nachhall bindbar | Decke über dem Lied; im Nachhall bindbar (mechanisch identisch) |
| Ursprungsstimmen | wach und frei; bindbar nach Regionalquest + Stimmsiegel | schlafend; bindbar als „schlafende Stimmen“ (identische Werte) |
| Stillezonen | geheilt (Grün) | befriedet (Silber) |
| Resonanzsinn | → Resonator-Sinn (gleiche Werte) | bleibt |
| Endgame-Inhalte | vollständig | vollständig (DR-19) |
| Ranked, Raids, Tiefenresonanzen | identisch | identisch |
| Achievement | „Das neue Lied“ | „Die sanfte Stille“ |

Die Unterschiede sind **ausschließlich erzählerisch und kosmetisch** (CANON §38). Spieler in Koop/Handel sehen das Ende des anderen nur in dessen Welt (K60).

---

## 8. Epilog-System

### 8.1 Aufbau

Jeder Epilog besteht aus vier Teilen (ADR-175):

```
 [Endsequenz je Ende, 95 s] → [Vignette Freie Stimmen, 40 s] → [Vignette Kael, 40 s]
                            → [Vignette Sereth, 40 s] → [Schlussbild, 30–60 s] → [Ysoldes Brief]
```

| Vignette | Positiv (Bedingung) | Negativ |
|---|---|---|
| **Freie Stimmen** | verbündet (`FS_STANCE` ≥ 0): Tavesh spricht im Bundesrat als Gast; die befreiten Arbeits-Echos ziehen frei durch Ignareth | im Untergrund (< 0): Tavesh schreibt Flugblätter gegen Bund *und* Akademie; seine Echos sind frei, er bleibt misstrauisch |
| **Kael** | kehrt heim (`KAEL_TRUST` ≥ 1): Kael in Lindwiesen, ein Rückspiel in der Arena der Wurzeln, Venn-Brief ungelesen auf dem Tisch | an Venns Seite (≤ 0): Kael begleitet Venn nach Schweigfels; er pflegt ihn, liest ihm vor; ein Brief an den Spieler – „nicht verloren, nur woanders“ |
| **Sereth** | versöhnt (`SERETH_RESPECT` ≥ 1): Sereth öffnet Schweigfels als Hospiz für Klangpest-Opfer und für Echos, die zu laut wurden | gebrochen (≤ 0): Sereth legt das Ordensgewand ab und wandert allein durch Hvitfell; der Orden zerfällt in Splittergruppen |

Die Vignetten haben je **zwei Fassungen pro Ende** (Neues Lied: Klang, Farbe; Sanfte Stille: Silber, Atem) – 3 Vignetten × 2 Ausgänge × 2 Enden = **12 Vignetten-Sequenzen**.

### 8.2 Die vier Schlussbilder

Die Anzahl positiver Vignetten bestimmt das **Schlussbild** – das sind die **4 Epilog-Varianten** je Ende aus CANON §38:

| Positive Vignetten | Schlussbild | Beschreibung |
|---|---|---|
| 3 | **Voller Chor** | Lindwiesen-Fest: alle Figuren (auch Venn am Rand, mit Kael) um den Klangbrunnen; der Chor des Spielers spielt |
| 2 | **Zwei Stimmen** | Abend auf dem Hügel über Lindwiesen mit Ysolde und zwei Figuren; ein leerer Platz |
| 1 | **Eine Stimme** | Ysolde und eine Figur am Feuer; der Rest als Briefe auf dem Tisch |
| 0 | **Der eigene Chor** | Der Spieler allein mit seinen Echos auf dem Lindwald-Hügel; Ysolde kommt zuletzt mit zwei Tassen |

Jedes Schlussbild existiert in beiden Enden → **2 × 4 = 8 Epilog-Varianten**. Keine ist „schlecht“; die Abwesenden sind lebendig und haben eigene Wege gewählt.

### 8.3 Vollständige Matrix

| # | Ende | Freie Stimmen | Kael | Sereth | Schlussbild | Dauer (s) |
|---|---|---|---|---|---|---|
| 1 | Neues Lied | Freie Stimmen verbündet | Kael kehrt heim | Sereth versöhnt | Voller Chor | 275 |
| 2 | Neues Lied | Freie Stimmen verbündet | Kael kehrt heim | Sereth gebrochen | Zwei Stimmen | 265 |
| 3 | Neues Lied | Freie Stimmen verbündet | Kael an Venns Seite | Sereth versöhnt | Zwei Stimmen | 265 |
| 4 | Neues Lied | Freie Stimmen verbündet | Kael an Venns Seite | Sereth gebrochen | Eine Stimme | 255 |
| 5 | Neues Lied | Freie Stimmen im Untergrund | Kael kehrt heim | Sereth versöhnt | Zwei Stimmen | 265 |
| 6 | Neues Lied | Freie Stimmen im Untergrund | Kael kehrt heim | Sereth gebrochen | Eine Stimme | 255 |
| 7 | Neues Lied | Freie Stimmen im Untergrund | Kael an Venns Seite | Sereth versöhnt | Eine Stimme | 255 |
| 8 | Neues Lied | Freie Stimmen im Untergrund | Kael an Venns Seite | Sereth gebrochen | Der eigene Chor | 245 |
| 9 | Sanfte Stille | Freie Stimmen verbündet | Kael kehrt heim | Sereth versöhnt | Voller Chor | 275 |
| 10 | Sanfte Stille | Freie Stimmen verbündet | Kael kehrt heim | Sereth gebrochen | Zwei Stimmen | 265 |
| 11 | Sanfte Stille | Freie Stimmen verbündet | Kael an Venns Seite | Sereth versöhnt | Zwei Stimmen | 265 |
| 12 | Sanfte Stille | Freie Stimmen verbündet | Kael an Venns Seite | Sereth gebrochen | Eine Stimme | 255 |
| 13 | Sanfte Stille | Freie Stimmen im Untergrund | Kael kehrt heim | Sereth versöhnt | Zwei Stimmen | 265 |
| 14 | Sanfte Stille | Freie Stimmen im Untergrund | Kael kehrt heim | Sereth gebrochen | Eine Stimme | 255 |
| 15 | Sanfte Stille | Freie Stimmen im Untergrund | Kael an Venns Seite | Sereth versöhnt | Eine Stimme | 255 |
| 16 | Sanfte Stille | Freie Stimmen im Untergrund | Kael an Venns Seite | Sereth gebrochen | Der eigene Chor | 245 |

Verteilung bei Gleichverteilung der Flag-Werte (−2…+2, nur zur Kontrolle der Erreichbarkeit; reale Werte siehe Telemetrie K68):

| Schlussbild | Positive Vignetten | Flag-Kombinationen | Anteil |
|---|---|---|---|
| Voller Chor | 3 | 12 | 9,6 % |
| Zwei Stimmen | 2 | 44 | 35,2 % |
| Eine Stimme | 1 | 51 | 40,8 % |
| Der eigene Chor | 0 | 18 | 14,4 % |
| **Summe** | | **125** | 100 % |

Alle vier Schlussbilder sind mit jeder Starterlinie und jeder Regionsreihenfolge erreichbar; „Voller Chor“ erfordert mindestens zwei zugewandte Entscheidungen gegenüber Kael und eine gegenüber Sereth.

### 8.4 Ysoldes Brief

Nach dem Schlussbild öffnet der Spieler den Brief (automatisch, Stimme Ysolde). Der Kern ist in beiden Enden gleich; ein Absatz unterscheidet sich, und die Anrede hängt von `YSOLDE_BOND` ab (nur Ton, ADR-163 fortgeschrieben).

> *„Ich habe diesen Brief vor Prismara geschrieben, also weiß ich nicht, was du gewählt hast. Ich weiß nur, dass du gewählt hast, nachdem du gefragt hast. Das ist mehr, als Maedryn getan hat, und mehr, als Venn getan hat. Es ist genau das, was Ilen getan hat.*
>
> *(Neues Lied:) Wenn du nicht mehr hörst, was du gehört hast: Ich habe es auch nie gehört. Ich habe dir zugehört. Das reicht. Es hat immer gereicht.*
>
> *(Sanfte Stille:) Wenn die Stimmen schlafen: Dann hüte ihren Schlaf. Du bist der Einzige, der ihn hören kann. Das ist keine kleine Aufgabe.*
>
> *Komm nach Hause. Der Brunnen in Lindwiesen summt in Moll. Ich habe nie aufgehört zu lachen, als du das gesagt hast.“*

---

## 9. Nachhall: Übergang ins Post-Game

### 9.1 MQ_A3_09 · Nachhall (Intensität 2)

Nach dem Epilog erwacht der Spieler in **Lindwiesen** – im eigenen Bett, wie im Prolog. Draußen: die Welt im Zustand des gewählten Endes. Freischaltungen:

| Freischaltung | Bedingung | Kapitel |
|---|---|---|
| Post-Game-Zustand „Nachhall“ (`DL_Nachhall`, Wild-Spawns 72–90) | Ende gesehen | K62 |
| **Velnox** bindbar (Questreihe „Die Pause hören“) | Ende gesehen | K36/K62 |
| Ursprungsstimmen-Bindung (alle, nach Regionalquest + Stimmsiegel) | Ende gesehen + Stimmsiegel | CANON §34 |
| Tiefenresonanzen DR_01–10 | Rang ≥ 30 | K35/K62 |
| Mythische Questreihen (Chronaire, Mirrowisp, Ouroveth, Aurelune) | je eigene Bedingung | K39/K62 |
| Sturmstimmgabel (Resonanzsturm auslösen) | Ende gesehen | CANON §63 |
| Akademie unter kommissarischer Leitung (Aevrin Thal) | Ende gesehen | K39 §7, K47 |

### 9.2 Finale-Speicherpunkt (ADR-176)

Vor MQ_A3_07 legt das Spiel einen gesonderten, nicht überschreibbaren **Finale-Speicherpunkt** an (K64). Wer das andere Ende sehen will, lädt ihn; die dabei gewonnenen Echos, Items und Ränge **bleiben nicht** erhalten (getrennter Spielstand), aber das Achievement und ein Kodex-Eintrag „Das andere Lied“ werden kontoweit vermerkt. Der Nachhall-Spielstand folgt immer dem zuletzt **im Hauptspielstand** gewählten Ende.

### 9.3 Weltzustand im Nachhall

| System | Neues Lied | Sanfte Stille | Technik |
|---|---|---|---|
| Stillezonen | Grün, belebt, eigene Nachhall-Spawns | Silber, ruhig, eigene Nachhall-Spawns | Data Layer `DL_Story_R##_Healed` + Material-Parameter `Healed.Variant` |
| Himmel | Aurora in zehn Farben (nachts) | silberner Schleier (nachts) | Sky-Preset je Ende |
| Musik | Weltlied-Thema als Grundlage aller Regionsthemen | Wiegenlied-Variation als Grundlage | Musik-State `Ending` (K55) |
| Barks | ~600 Ende-spezifische Barks | ~600 Ende-spezifische Barks | Bark-Tag `Story.Ending.*` |
| Venn | lebt in Schweigfels (bei Kael-Vignette negativ mit Kael), hält Vorlesungen an Wänden | lebt in Schweigfels, sitzt am Fenster: „Ruhe. Nicht Ordnung. Aber Ruhe.“ | NPC-Zustand |

---

## 10. Zwischensequenzen und Partitur

| Szene | Länge | Leitmotiv (K55) |
|---|---|---|
| Abstieg mit der Liftstation | 0:40 | Prismara-Thema (Glasharfe, Farbtöne) |
| Missgrath spaltet sich | 0:30 | Krone-Motiv, verzerrt |
| Der zehnte Splitter hebt sich | 0:35 | Ilen-Motiv + Prism'aion-Glockenspiel |
| Kristallsee-Lager | frei | Wärter-Thema, Gitarren-/Lautenfassung |
| Windbänder | 0:45 | Nimbara-Thema (Wind, Chöre ohne Worte) |
| Zehn Stimmen erwachen | 1:20 | Weltlied-Thema, zehn Linien setzen nacheinander ein |
| Venn setzt die Krone auf | 0:50 | Krone-Motiv, voll; zehn Töne unisono |
| Kael greift ein | 0:30 | Kael-Thema in eigener Instrumentierung (zurückgewonnen) |
| Der Riegel bricht | 3:00 | Pause: 4 s völlige Stille, dann ein einzelner tiefer Ton |
| Phase 4 | frei | ein gehaltener Ton (Dauer offen), darunter Ilens Atem |
| Neues Lied | 1:35 | Weltlied-Thema vollständig, frei, 10 Linien |
| Sanfte Stille | 1:35 | Wiegenlied aus Eiðvik (Sereth summt), Streicher-Decke |
| Vignetten | je 0:40 | Figurenthemen |
| Schlussbild | 0:30–1:00 | Lindwiesen-Thema (Tag) |
| Ysoldes Brief | 1:10 | Ysoldes Summen = Ilen-Motiv, aufgelöst in Dur |

**Partitur-Regel:** Die gesamte Hauptstory baut auf vier Motiven auf – Weltlied (10 Linien), Stille (Pausen), Ilen (Ysoldes Summen), Krone (Unisono). Das Finale löst sie auf: Neues Lied = Weltlied gewinnt; Sanfte Stille = Stille wird zum Wiegenlied. Das Krone-Motiv erklingt nach MQ_A3_07 nie wieder.

---

## 11. Quest-Daten

| Name | Order | Region | Title | Prerequisite | Truth | Intensity | DurationMin | Boss | Akkord | Rewards |
|---|---|---|---|---|---|---|---|---|---|---|
| MQ_A3_01 | 1 | R09 | Hinab nach Prismara | MQ_A2_11 | – | 5 | 45 |  |  | Liftstation-Zugang, Prismara-Resonanzstein |
| MQ_A3_02 | 2 | R09 | Der versteinerte Missklang | MQ_A3_01 | W8 | 8 | 140 | BOSS_A3_01 |  | Klangfragment Maedryn, Kaels Notizblock (Deutung) |
| MQ_A3_03 | 3 | R09 | Das neunte Schloss | MQ_A3_02 | – | 6 | 100 |  | ARN_09 | Akkord Brechung, zehnter Splitter (getragen) |
| MQ_A3_04 | 4 | R09 | Die letzte Nacht am Boden | MQ_A3_03 | – | 2 | 40 |  |  | Ysoldes Brief (versiegelt), Lager-Moment |
| MQ_A3_05 | 5 | R10 | Aufstieg nach Nimbara | MQ_A3_04 | – | 6 | 110 |  |  | Nimbara-Resonanzsteine, Windanker |
| MQ_A3_06 | 6 | R10 | Die Sternenarena | MQ_A3_05 | – | 7 | 100 |  | ARN_10 | Akkord Sternfall, alle zehn Stimmen wach |
| MQ_A3_07 | 7 | R10 | Die Krone | MQ_A3_06 | – | 9 | 80 | BOSS_A3_02 |  | – |
| MQ_A3_08 | 8 | R10 | Die Große Pause | MQ_A3_07 | W9 | 10 | 60 | BOSS_A3_03 |  | Ende, Nachhall |
| MQ_A3_09 | 9 | R01 | Nachhall | MQ_A3_08 | – | 2 | 40 |  |  | Post-Game Nachhall, Velnox bindbar, Epilog |

### 11.1 Quest-Zusammenfassungen

| Name | Title | Summary |
|---|---|---|
| MQ_A3_01 | Hinab nach Prismara | Liftstation Kraterrand, Glanzschacht; Prismara als Glasstadt im Krater; Ilyx Brannoc erzählt von den kristallisierten Missklang-Adern |
| MQ_A3_02 | Der versteinerte Missklang | Missklang-Wacht, tiefste Adern; Missklang-Hydra; Kaels Notizblock bzw. Sereths Kundschafter: Venn will die Krone in Nimbara aktivieren, wofür der Riegel brechen muss |
| MQ_A3_03 | Das neunte Schloss | Arena Prismara (fest Stufe 9); Prism'aion erwacht halb; der zehnte Splitter löst sich nur in der Hand des Nachklang-Trägers |
| MQ_A3_04 | Die letzte Nacht am Boden | Lager am Kristallsee mit allen Verbündeten; jede Figur ein Gespräch; Ysolde übergibt einen Brief: erst öffnen, wenn entschieden ist |
| MQ_A3_05 | Aufstieg nach Nimbara | Flug durch die Windbänder; Lumeya und Wolkenrast; die Kronenwerft-Wacht ist von Venn-treuen Ordensleuten besetzt |
| MQ_A3_06 | Die Sternenarena | Arena Aerion (fest Stufe 10); Oruma Siyel; mit dem zehnten Akkord erwachen alle Stimmen – und die neun Splitter in Venns Krone antworten dem zehnten |
| MQ_A3_07 | Die Krone | Kronenwerft; Venn setzt die Krone auf, der zehnte Splitter wird aus dem Spieler gezogen; Kampf gegen Venn und Kronvaal; Kael greift ein; die Krone zerbricht, der Riegel auch – Velnox ist frei |
| MQ_A3_08 | Die Große Pause | Velnox über Nimbara; die zehn Stimmen helfen; Phase 4: Ilen spricht durch den Spieler (W9); Entscheidung Neues Lied oder Sanfte Stille |
| MQ_A3_09 | Nachhall | Epilog je Ende mit drei Vignetten (Freie Stimmen, Kael, Sereth) und einem von vier Schlussbildern; Ysoldes Brief; Rückkehr nach Lindwiesen |

### 11.2 Dialogvarianten nach Haltung (Akt III)

| Zeile | Situation | Einfühlsam | Neugierig | Entschlossen | Flag-Effekt |
|---|---|---|---|---|---|
| DLG_A3_01_02 | Ilyx über den Missklang | „Er hat Schmerzen.“ | „Warum wird er lauter?“ | „Zeig mir die tiefste Ader.“ | – |
| DLG_A3_02_04 | Kaels Notizblock / Kundschafter-Bericht | „Er hatte Zweifel.“ | „Was braucht Venn noch?“ | „Dann nach Nimbara.“ | KAEL_TRUST +1 / 0 / 0 (nur Notizblock) |
| DLG_A3_03_03 | Der zehnte Splitter | „Ich trage ihn.“ | „Was, wenn ich ihn hierlasse?“ | „Wir brechen die Krone mit ihm.“ | – |
| DLG_A3_04_01 | Ysolde am Kristallsee | Zuhören bis zum Ende | „Warum hast du aufgehört?“ | „Morgen ist es vorbei.“ | YSOLDE_BOND +1 / 0 / 0 |
| DLG_A3_04_02 | Sereth fragt nach Stille als Gnade | „Für manche ist sie das.“ | „Für wen nicht?“ | „Nicht, wenn man sie erzwingt.“ | SERETH_RESPECT +1 / +1 / 0 |
| DLG_A3_04_04 | Befreite Echos singen | Mitsummen | Den Ton mit dem Resonator festhalten | Applaudieren und aufstehen | FS_STANCE +1 / 0 / 0 |
| DLG_A3_06_03 | Oruma über fehlende Sterne | „Sie haben Angst.“ | „Was zählt Ihr?“ | „Dann beeilen wir uns.“ | – |
| DLG_A3_07_01 | Venns letztes Angebot | „Du willst, dass niemand leidet.“ | „Was, wenn die Pause sich nicht dirigieren lässt?“ | „Nimm die Krone ab.“ | – |
| DLG_A3_07_05 | Kael nach dem Kampf | Kael aufhelfen | „Was wirst du jetzt tun?“ | „Bleib bei ihm, wenn du musst.“ | – (Vignette nach KAEL_TRUST) |
| DLG_A3_08_04 | Vor der Entscheidung, Chor-Abschied | je Echo nonverbal | je Echo nonverbal | je Echo nonverbal | – |

### 11.3 Begegnungs- und Belohnungstakt

| Abschnitt | Kämpfe (Pflicht) | Kämpfe (optional) | Bindungsgelegenheiten | Neues | Ziel-Spielzeit |
|---|---|---|---|---|---|
| Prismtiefen (MQ_A3_01–03) | 7 + Boss | 16 | 10 | Missklang-Adern, Resonanzkammer | 4,8 h |
| Lager (MQ_A3_04) | 0 | 0 | 0 | sechs Gespräche | 0,7 h |
| Nimbara (MQ_A3_05–06) | 6 | 12 | 8 | Windbänder, alle Stimmen wach | 3,5 h |
| Finale (MQ_A3_07–08) | 2 Bosse | 0 | 0 | Entscheidung | 2,3 h |
| Epilog (MQ_A3_09) | 0 | 0 | 0 | Nachhall | 0,7 h |
| **Summe Akt III** | **~15** | **~28** | **~18** | | **~12 h** |

---

## 12. Hauptstory gesamt

| Teil | Quests | Spielzeit | Akkorde | Wahrheiten | Story-Bosse | Rang am Ende |
|---|---|---|---|---|---|---|
| Prolog | 3 | ~3 h | 0 | W1 | 1 | 5 |
| Akt I | 9 | ~15 h | 4 | W2, W3 | 2 | 16 |
| Akt II | 11 | ~20 h | 4 | W4–W7 | 3 | 24 |
| Akt III | 9 | ~12 h | 2 | W8, W9 | 3 (inkl. Velnox) | 29 |
| **Summe** | **32** | **~50 h** | **10** | **W1–W9** | **9 + Ulrek-Variante = 10 Story-Bosse (CANON §131)** | **~29** |

Die **32 Hauptquests** entsprechen der Planung aus K07 §14 („~32“). Die Summe der `DurationMin` aller Hauptquests beträgt **~51 h** – das ist die *typische* Spielweise inklusive optionaler Kämpfe, Bindungen und Erkundung (K43 §3.1). Ohne optionale Inhalte (Story-Fokus) sinkt die Zeit um ~20 % auf **~41 h** und liegt damit im Designziel 35–45 h (K01 §7.4). QA misst beide Werte (K66). Alle neun Wahrheitsebenen sind an genau einer Quest verankert:

| Wahrheit | Quest | Kapitel |
|---|---|---|
| W1 | MQ_P01 | K44 |
| W2 | MQ_A1_06 | K44 |
| W3 | MQ_A1_08 | K44 |
| W4 | MQ_A2_01 | K45 |
| W5 | MQ_A2_05 | K45 |
| W6 | MQ_A2_07 | K45 |
| W7 | MQ_A2_10 | K45 |
| W8 | MQ_A3_02 | K46 |
| W9 | MQ_A3_08 | K46 |

---

## 13. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Level Design | Prismara (Glasstadt, Lichttöne), Missklang-Adern mit wachsenden Kristallen (Zustand an Story gebunden), Kronenwerft-Plattform, zerbrechende Inseln für Velnox-Phasenwechsel | K57 |
| World Tech | `DL_Story_R##_Healed` mit Material-Variante (Grün/Silber), Sky-Presets je Ende, globale Sequenz „Zehn Stimmen erwachen“ (alle Regionen gestreamt als Fernsicht-Impostor) | K57/K65 |
| Combat | Velnox Phase 4 ohne HP-Ende (Kampfzustand „Narrativ“), Kael-Eingriff bei < 15 % als Skript-Event | K35 |
| Audio | Vier Motive (Weltlied, Stille, Ilen, Krone), Doppelstimme Spieler/Ilen, gehaltener Ton in Phase 4, ~1.200 Ende-spezifische Barks | K55 |
| UX | Entscheidungsdialog mit Halten-Bestätigung, zufälliger Reihenfolge, ohne Zeitlimit; Finale-Speicherpunkt-Hinweis | K54 |
| Save | Finale-Speicherpunkt (gesonderter Slot), kontoweite Achievements „anderes Ende“ | K64 |
| QA | Testmatrix: 2 Enden × 8 Vignetten-Kombinationen × 3 Starter × 6 Akt-II-Reihenfolgen (Smoke) | K66 |
| Daten | `MainQuests.csv` (32 Quests), `StoryFlags.csv` (12 Flags), Epilog-Matrix (`story_k46.py`) | K48 |

---

## 14. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-168 | Keine Ruhephase zwischen Krone und Velnox (DR-29-Ausnahme) | Finale als ein Bogen; Ausgleich durch Point of no Return, 3-min-Sequenz, volle Heilung | Lager zwischen den Kämpfen |
| ADR-169 | W8 aus zwei Quellen (Kaels Notizblock oder Sereths Kundschafter) | Frühere Entscheidung wird belohnt, ohne Information zu sperren | W8 nur über Kael |
| ADR-170 | Kronensplitter sind nur durch die singende Krone zerbrechbar | Erklärt, warum der Spieler den Splitter nach Nimbara bringt | Splitter zerstörbar (Story würde kollabieren) |
| ADR-171 | Kaels Eingriff erfolgt immer; Flags bestimmen nur den Epilog | Kael-Umkehr ist kanonisch (CANON §37) | Eingriff nur bei hohem Vertrauen |
| ADR-172 | Sereths Angebot ist immer verfügbar | Beide Enden sind für jeden Spieler wählbar (CANON §38) | Angebot an SERETH_RESPECT gebunden |
| ADR-173 | Entscheidung ohne Zeitlimit, mit 3-s-Halten, zufälliger Reihenfolge | Würde und Ernst des Moments, keine Fehlbedienung, keine implizite Empfehlung | Timer, feste Reihenfolge |
| ADR-174 | Stillezonen im Ende „Sanfte Stille“: Silber statt Grün, sonst gleiche Spawns | DR-19: identisches Endgame bei sichtbarem Unterschied | eigene Spawn-Tabellen je Ende |
| ADR-175 | Epilog = Endsequenz + 3 binäre Vignetten + 4 Schlussbilder je Ende | Erfüllt „2 Enden × 4 Epilog-Varianten“ und bildet alle drei Flag-Achsen ab | 8 vollständig getrennte Epilog-Filme |
| ADR-176 | Finale-Speicherpunkt als gesonderter Slot; Nachhall folgt dem Hauptspielstand | Beide Enden erlebbar, ohne Endgame-Fortschritt zu duplizieren | Ende im Nachhall umschaltbar |

---

## 15. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §176 | Akt III: MQ_A3_01–06 (Prismtiefen W8, zehnter Splitter nur in der Hand des Nachklang-Trägers, Lager, Nimbara, zehn Stimmen erwachen, Resonanzsturm) | LOCKED |
| §177 | Finale: MQ_A3_07 Venn mit Krone (Kael greift immer ein, Krone und Riegel brechen) → MQ_A3_08 Velnox, Phase 4 Entscheidung (W9), Sereths Angebot immer verfügbar, UX ohne Zeitlimit | LOCKED |
| §178 | Enden und Weltzustand: Neues Lied (Grün, Resonator-Sinn) / Sanfte Stille (Silber, Resonanzsinn bleibt, schlafende Stimmen); Endgame identisch; Finale-Speicherpunkt | LOCKED |
| §179 | Epilog-System: 3 Vignetten (FS ≥ 0, KAEL ≥ 1, SERETH ≥ 1) → 4 Schlussbilder je Ende (Voller Chor, Zwei Stimmen, Eine Stimme, Der eigene Chor); Ysoldes Brief | LOCKED |
| §180 | Hauptstory gesamt: 32 Quests, ~50 h, 10 Akkorde, W1–W9 je an einer Quest, Rang ~29 am Ende | LOCKED |
| §15 | Story-Finale Echo-Level 68–70, Rang ~28–29 aus Story-Sicht bestätigt; Freigabe in K63 | PROVISIONAL → K63 |
| §11 | CR-004: Story-Platzierung aus K09 an K44/K45 angepasst (W2 zweite Region, Sereth-Auftritte, Venn-Grabung) | – |
| §10 | ADR-168 – ADR-176 | LOCKED |

---

## 16. Kapitel-Checkliste

- [x] Logline, Thema, Ton von Akt III
- [x] Struktur, Intensitätskurve, DR-29-Ausnahme begründet
- [x] Figuren und ihre Abschlüsse
- [x] 9 Hauptquests mit Szenen, Dialogen und Entscheidungen
- [x] W8 (zwei Quellen) und W9 (Finale) verankert
- [x] Finale mit Phasen und Entscheidungs-UX
- [x] Beide Enden ausgeschrieben, Gemeinsamkeiten und Weltzustand
- [x] Epilog-System: Vignetten, Schlussbilder, vollständige Matrix, Ysoldes Brief
- [x] Nachhall-Übergang, Finale-Speicherpunkt
- [x] Partitur-Regel, Zwischensequenzen
- [x] Quest-Daten, Hauptstory-Übersicht, Anforderungen, ADR-168 – ADR-176, CANON §176–§180

➡️ **Nächstes Kapitel: K47 – Fraktionen und Ruf.**
