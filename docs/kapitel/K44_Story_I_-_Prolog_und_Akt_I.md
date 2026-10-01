# K44 · Story I – Prolog und Akt I: „Die Stille kommt“

| Feld | Wert |
|---|---|
| Dokument | Kapitel 44 von 68 · Narrative Bible, Teil I |
| Version | 1.0 |
| Owner | Narrative Director |
| Mitwirkende | Lead Writer, Quest Designer, Cinematics Director, Level Design (Verdanthain, Kharsgrat, Morvenmoor, Saltrand), Audio (Leitmotive), Combat Designer (Story-Bosse) |
| Baut auf | K07 (Kosmologie, Figuren, Wahrheiten W1–W9, Enden), K02 §8 (Prolog-Ablauf 0:00–3:00), CANON §15 (Progression, freie Regionsreihenfolge), §34 (Ursprungsstimmen), §38 (Story-Rückgrat), §51 (Arenen), §131 (Story-Bosse), §148 (Klangfragmente), DR-09, DR-14, DR-29 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Quests/MainQuests.csv` (Prolog + Akt I: 12 Quests), `Data/Quests/StoryFlags.csv` (6 Flags) |
| Neue Kanon-Einträge | CANON §168 (Erzählprinzipien), §169 (Prolog), §170 (Akt I), §171 (Story-Flags) |

---

## Inhalt

1. [Die Geschichte in einem Satz](#1-die-geschichte-in-einem-satz)
2. [Erzählprinzipien](#2-erzählprinzipien)
3. [Akt-Struktur und Intensität](#3-akt-struktur-und-intensität)
4. [Figuren in Akt I](#4-figuren-in-akt-i)
5. [Prolog](#5-prolog)
6. [Akt I](#6-akt-i)
7. [Freie Reihenfolge: dynamische Erzählung](#7-freie-reihenfolge-dynamische-erzählung)
8. [Entscheidungen und Flags](#8-entscheidungen-und-flags)
9. [Zwischensequenzen und Leitmotive](#9-zwischensequenzen-und-leitmotive)
10. [Quest-Daten](#10-quest-daten)
11. [Anforderungen an andere Abteilungen](#11-anforderungen-an-andere-abteilungen)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Die Geschichte in einem Satz

> *Ein junger Wärter, der als Einziger die Grundfrequenzen der Welt hören kann, folgt der sich ausbreitenden Stille bis zu ihrem Ursprung – und muss am Ende entscheiden, ob er die Gabe, die ihn ausmacht, zurückgibt, damit das Lied frei sein kann.*

**Themen:** Hören und Verstehen · Freiheit und Ordnung · Erbe und Verzicht · Stille als Ruhe oder als Verlust.

**Ton:** warm, staunend, mit wachsendem Ernst; Humor in den Figuren (Ysoldes Trockenheit, Mariekes Geschäftssinn, Kaels Ehrgeiz), nie zynisch. Niemand stirbt durch die Hand des Spielers (ADR-007); Verluste sind Verstummen, Vergessen, Verzicht.

---

## 2. Erzählprinzipien

| Prinzip | Regel |
|---|---|
| **L-01 Wahrheitsebenen** | Keine Lore vor ihrer Ebene; Fragmente oberhalb des Wissensstands sind verzerrt (K39 §6) |
| **Venns Regel** | Jede Szene mit Aldric Venn trägt sein Argument fair vor: „Freiheit ohne Ordnung ist nur eine andere Form von Leid.“ (K07 §13.2) |
| **DR-09** | Story ist auf „Wärter“ ohne Kombos/Formation gewinnbar; Niederlagen gegen Rivalen führen weiter |
| **Freie Reihenfolge** | Kharsgrat, Morvenmoor, Saltrand sind frei wählbar; die Erzählung passt sich an (§7) |
| **DR-14** | Begegnungen sind sichtbar; höchstens ein angekündigter Hinterhalt pro Quest |
| **DR-29 Atemzug** | Nach Intensität ≥ 7 folgen ≥ 20 Minuten Ruhe (Erkundung, Lager, Stadt) |
| **Stimme des Spielers** | Der Wärter antwortet in kurzen Auswahlantworten mit drei Haltungen – **einfühlsam**, **neugierig**, **entschlossen**; zwei Sprecherstimmen wählbar; keine Haltung wird bestraft |
| **Echos als Figuren** | Starter und Begleiter reagieren in Szenen (Animation, Laut); der Starter hat in jedem Akt mindestens eine eigene Szene |

---

## 3. Akt-Struktur und Intensität

| Teil | Regionen | Akkorde | Spielzeit | Wahrheiten | Höhepunkt |
|---|---|---|---|---|---|
| Prolog | R01 Lindwiesen, Lindwald | – | ~3 h | W1 | Erstresonanz, Gleitpanorama |
| **Akt I** | R01 Eichenhall, dann R02/R03/R06 frei | 4 | ~15 h | W2 (Mitte), W3 (Ende) | Der versunkene Turm |
| Akt II | R04/R05/R07 frei, R08 nach 2 weiteren | 4 | ~20 h | W4–W7 | Venns Verrat (W6), Ael'Dorun (W7) |
| Akt III | R09, R10 | 2 | ~12 h | W8, W9 | Velnox, Entscheidung |

```
Intensität (1–10) über Prolog und Akt I
10 ┤
 9 ┤                                                                   ███ Turm
 8 ┤                                                ███ Stillsteine
 7 ┤ ███ Stillezone   ███ Lindwald
 6 ┤      ██ Wächter                  ██ R02 ██ R03 ██ R06
 5 ┤                       ██ Arena 1
 4 ┤                                                         ██ Venn
 3 ┤            ██ Wald
 2 ┤                                                                        ██ Nachklang
 1 ┼──────────────────────────────────────────────────────────────────────────────────
     P01  P02   P03    A1-01  A1-02  A1-03/04/05 (frei)  A1-06  A1-07   A1-08  A1-09
```

Zwischen jeder Spitze ≥ 7 liegt eine Ruhephase ≥ 20 min (Lager-Moment, Stadt, Erkundung) – DR-29 ist eingehalten (siehe Spalte `Intensity` in `MainQuests.csv`).

---

## 4. Figuren in Akt I

| Figur | Rolle in Akt I | Erste Szene | Was der Spieler über sie lernt |
|---|---|---|---|
| **Ysolde Varn** | Mentorin, Wildwacht | MQ_P01 Waldrand | Sie hört mehr, als sie sagt; sie war Arenameisterin von Eichenhall (989–996) und hörte auf, „als die Stille kam“ |
| **Kael Duran** | Rivale, Jugendfreund | MQ_P01 | Brillant, ungeduldig; glaubt an Messbarkeit statt Gehör; wird Akademie-Anwärter (MQ_A1_07) |
| **Hralda Brakk** | Hauptwächterin der Wildwacht | MQ_A1_01 | Kharsk, wortkarg, loyal zu Ysolde; vergibt die Lizenz und den ersten Sattel |
| **Maelis Wendt** | Arenameisterin Eichenhall | MQ_A1_01 | Ysoldes Nachfolgerin; Blüte; hält die Arena für ein Gartenfest – und für eine Wache |
| **Torvik Hrall** | Arenameister Kharsholm | MQ_A1_03 | Ehrt die Ahnen; liest Wetter aus Steinen |
| **Evhe Corrach** | Arenameisterin Morvenfurt | MQ_A1_04 | Kämpft nur nachts; Moorweise |
| **Tavesh Amaru** | Anführer der Freien Stimmen | MQ_A1_04 | Ehemaliger Arbeiter in einem Echo-Lager; misstraut Akademie und Kontor |
| **Marieke Holm** | Handelsherrin, Goldklang-Kontor | MQ_A1_05 | Pragmatisch, witzig; leiht dem Spieler, was er braucht – gegen einen Gefallen |
| **Beke Tamsen** | Arenameisterin Saltrand-Hafen | MQ_A1_05 | Lotsin, Gezeitenkundige |
| **Ulrek** | Ordenskommandant | MQ_A1_06 | Glaubt an Stille als Gnade; überzeugter, nicht grausamer Gegner |
| **Sereth Vaun** | Ordensoberhaupt | MQ_A1_06 | Sanft, unbeirrbar; Überlebende der Klangpest; Erfinderin der Stillsteine |
| **Aldric Venn** | Rektor der Akademie | MQ_A1_07 | Charismatisch, freundlich, beunruhigend klug; bietet Hilfe an |
| **Ilen** | historisch | MQ_A1_08 (Vision) | Eine Stimme, die nach dem Spieler zu greifen scheint |

---

## 5. Prolog

### MQ_P01 · Ein Ton im Dunkel (0:00–0:52, Intensität 7)

**Kalte Eröffnung.** Schwarzbild. Ein einziger, tiefer Ton, der sich zu einem Akkord öffnet: das Weltlied. Eine Vision – über Wolkeninseln (Nimbara, der Spieler weiß es noch nicht) schwebt ein riesiges, sternförmiges Echo; es singt, dann bricht sein Ton ab. Stille. Der Spieler erwacht in seinem Elternhaus in **Lindwiesen**.

**Charakter-Editor** im Spiegel des Hauses (eingebettet, ohne Menüwechsel).

**Morgen im Dorf.** Ein kleines wildes Echo (ein Verdanthain-Häufiges) stiehlt Brot vom Fensterbrett der Bäckerin; Verfolgung durch Lindwiesen (Bewegen, Sprinten, Springen). Das Echo verschwindet im Lindwald.

**Ysolde am Waldrand.**

> **Ysolde:** „Du rennst einem Brotdieb hinterher, als ginge es um den Weltakkord.“
> *(einfühlsam)* „Es sah hungrig aus.“ · *(neugierig)* „Was war das für eins?“ · *(entschlossen)* „Ich hätte es gekriegt.“
> **Ysolde:** „Mach die Augen zu. Was hörst du?“

Der Resonanzsinn wird eingeführt: Die Welt entsättigt, Frequenzen erscheinen als Wellenlinien. Der Spieler findet drei Frequenzen (Tutorial). Ysolde sagt nichts – aber ihre Hand am Resonator zittert kurz (erster Hinweis auf W5).

**Kael kommt dazu** – mit einem Notizbuch voller Messwerte. „Drei Frequenzen? Ich messe zwei. Die dritte ist Wunschdenken.“ Gemeinsamer Waldgang (Klettern, Ausdauer).

**Die Stillezone bricht aus.** Auf einer Lichtung verlieren die Farben ihren Ton; das Rauschen des Waldes erlischt; Echos fliehen. Drei Klangspuren führen in drei Richtungen – Blüte, Stein, Sturm (**Spurwahl** = Starterwahl, ADR-011). Ysolde: „Folge einer. Nur einer. Ich hole Kael.“

**Verfolgung** durch die zerfallende Zone (Annähern, Schleichen). Am Ende: das Starter-Echo (Fernlit, Brokk oder Wisplet), verletzt, zitternd, in einem hohlen Baumstumpf.

**Die Erstresonanz.** Beruhigen (Summen = Taste halten), dann der Anschlag im Takt seines Klangmals. Die Szene kann nicht scheitern (K36 §10: Fenster ×1,5, unbegrenzte Versuche, Annäherung +150). Musik: das Leitmotiv des Spielers erklingt zum ersten Mal vollständig (K55).

> *Bindungstext im Kodex (automatisch):* „Wir haben uns gefunden.“

**Flag:** `FLAG_STARTER_LINE` = gewählte Linie; Kael erhält den Starter mit Typvorteil (Starter-Zyklus Blüte > Stein > Sturm > Blüte, CANON §14).

### MQ_P02 · Der verstummte Wächter (0:52–1:32, Intensität 6)

Die Stillezone erreicht das Versteck. Aus dem Grau tritt ein **verstummtes Lorncant** (BOSS_P01, K35 §6.1): ein Geist-Klang-Echo, dessen Lied erloschen ist. Erster Kampf; nur Angriff und Zeitleiste-Lesen. Der Stillezähler (K35) sinkt bei jedem Zug Lorncants; bei 50 % HP kündigt es eine Nachklang-Heilung an – das Spiel lehrt: *Greif an, bevor der Marker erreicht ist.*

Nach dem Sieg kehrt Farbe in Lorncant zurück; es singt einen einzelnen Ton und flieht in den Wald – **geheilt, nicht besiegt**. Ysolde erscheint mit Kael, versiegelt die Zone provisorisch mit einem alten Wildwacht-Ritual (Resonator gegen den Boden, ein tiefer Ton).

> **Ysolde:** „Du hast es gehört. Die Grundfrequenz. Nicht die Oberfläche – den Ton darunter.“
> **Kael:** „Das ist nicht messbar.“
> **Ysolde:** „Nicht alles, was zählt, ist messbar, Kael.“ *(Sie gibt dem Spieler ihren alten Resonator.)* „Er hat lange auf jemanden gewartet.“

**Lindwiesen:** Begleitersystem (Streicheln, Füttern), Heilen am Klangbrunnen. Kael zeigt sein Echo – mit Typvorteil.

**Erster Rivalenkampf (1v1).** Kael gewinnt typischerweise (Typvorteil), außer der Spieler nutzt die Verzögerung seiner zweiten Fähigkeit. Niederlage erlaubt (DR-09). Kael nach dem Kampf, egal wie er ausgeht: „Nächstes Mal habe ich Daten über dich.“
**Flag:** `FLAG_KAEL_TRUST` ±1 nach Antwort („Gut gekämpft“ +1 / „Daten helfen dir nicht“ −1 / neutral 0).

### MQ_P03 · Was der Wald erzählt (1:32–3:00, Intensität 3)

**Erste Freiheit.** Ysoldes Auftrag: drei Echos im Lindwald beobachten, eines binden (Kodex, Bindung frei, ~0,8 km² freie Zone). Eine Herde mit Alpha, ein Wetterumschwung zu Regen – neue Echos erscheinen (Wetter-Spawns, K14).

**Lager-Moment** am Rastplatz: Heiltrank herstellen, kochen, Chor-Interaktion; im nächsten Kampf Wechsel und Reserve.

**Die Ruine im Wald.** Ein dorunisches Gewölbe mit einem Klangrätsel – das Feldfähigkeits-Tutorial (K30): Das Echo des Spielers öffnet den Mechanismus. Im Inneren: der **Gleiter** (nimbarische Bauart, ein Rätsel für später) und das erste **Klangfragment** (LORE_FRG der Ebene 0: „Das erste Lied – Wurzelhalle“, ein Kinderchor, der ein Lied über zehn Stimmen singt).

**Gleitpanorama** vom Ruinenturm: Verdanthain, Eichenhall am Horizont, die Gipfel des Kharsgrat, die Küste. Der erste **Resonanzstein** wird aktiviert (Schnellreise).

**Reise nach Eichenhall** (frei, ~1,5 km): erster Trainerkampf mit Harmonie und Kombo-Einführung. Ankunft in der Stadt, Questbrett, Arena-Plakat. **Ende des Onboardings** (~3:00).

---

## 6. Akt I

### MQ_A1_01 · Die Arena der Wurzeln (Intensität 5)

Ysolde schickt den Spieler zu **Hralda Brakk**, Hauptwächterin der Wildwacht in Eichenhall. Hralda prüft ihn wortkarg („Zeig mir, wie du gehst, wenn ein Echo schläft.“) – eine Schleich-Aufgabe in den Stadtgärten. Belohnung: **Wildwacht-Lizenz** und der **Bodensattel** (Bodenreiten nach Akkord 1, CANON §15).

**Arena von Eichenhall (ARN_01, Stufe 1, Duell):** Vorprüfung durch zwei Arena-Wärter, dann **Maelis Wendt** (Blüte, Feldregel Überwuchs). Nach dem Sieg: **Akkord der Wurzeln** und eine Klangschrift.

> **Maelis:** „Ysolde hat diese Arena geführt, als ich noch Unkraut gejätet habe. Sie hat aufgehört, als die Stille kam. Hat sie dir gesagt, warum?“
> *(neugierig)* „Nein. Warum?“ → **Maelis:** „Frag sie. Ich habe es nie verstanden.“

Unter der Arena, in der **Wurzelhalle**, summt etwas – der Spieler hört es im Resonanzsinn als tiefen, schlafenden Ton (Sylv'anor; W4-Vorahnung, ohne Namen).

### MQ_A1_02 · Stille über Lindwald (Intensität 7)

Die provisorische Versiegelung bricht. Ysolde ruft den Spieler zurück. Im Herzen des Lindwalds liegt ein **Stillkern**: Vernaune, eine Blüte/Licht-Erscheinung, erstarrt und grau, umgeben von zwei **Stillstein-Splittern** (BOSS_A1_01). Der Spieler kennt die Steine noch nicht – sie werden als „fremde graue Kristalle“ beschrieben (L-01).

Nach dem Sieg erwacht Vernaune und hebt den Wald mit einem einzigen Ton. Ysolde erhält Botschaften der Wildwacht: **Stillezonen am Kharsgrat, im Morvenmoor und vor der Küste von Saltrand**.

> **Ysolde:** „Drei Feuer, und wir haben einen Eimer. Such dir aus, wo du hingehst. Ich gehe dorthin, wo du nicht bist.“

**Der Weg teilt sich** – Kharsgrat, Morvenmoor, Saltrand sind frei wählbar (CANON §15). Ysolde wird für den Rest des Akts in der jeweils *anderen* Region gemeldet (Briefe, Sichtungen – sie ist präsent, ohne mitzulaufen).

### MQ_A1_03 · Fels und Ahnen (Kharsgrat, Intensität 6)

**Kharsholm**, die Stadt an der Wand. **Torvik Hrall** liest das Wetter aus den Ahnenfelsen und erklärt dem Spieler, dass die Kharsk ihre Toten in Steinen erinnern (Memoro-Echos). Am Grat ist eine Stillezone entstanden, die die Ahnenfelsen „schweigen“ lässt – für die Kharsk eine Katastrophe des Gedächtnisses.

- **Kletterreiten:** Die Wildwacht-Station am Grat übergibt den Klettersattel (Cragar/Hallbrand-Vorläufer).
- **Zone am Grat:** Der Spieler löst die Zone mit dem Wissen aus Lindwald (Stillkern finden, Echo heilen).
- **Arena ARN_02** (Stufe skaliert 2–4): Torvik Hrall, Wandernde Plattformen.

**Dorfthema:** Die Kharsk fürchten, ihre Ahnen zu vergessen. Am Ende singt Torvik einen Ahnenruf; die Felsen antworten. **Akkord des Fels.**

### MQ_A1_04 · Nebel über dem Moor (Morvenmoor, Intensität 6)

**Morvenfurt**, die Stadt auf Pfählen, Oberstadt der Händler, Unterstadt der Vergessenen. In der Unterstadt begegnet der Spieler **Tavesh Amaru** und den **Freien Stimmen**, die verstummte Echos verstecken, weil die Kontor-Fischer sie für Schädlinge halten.

> **Tavesh:** „Akademie misst sie. Kontor verkauft sie. Orden lässt sie schweigen. Und du? Bindest du sie, oder hörst du ihnen zu?“
> *(einfühlsam)* „Beides. Das eine geht nicht ohne das andere.“ (`FLAG_FS_STANCE` +1)
> *(entschlossen)* „Ich löse die Zonen. Was danach kommt, ist eure Sache.“ (0)
> *(neugierig)* „Woher habt ihr sie?“ → Tavesh weicht aus (−0, später relevant)

- **Arena ARN_03** (nachts): Evhe Corrach, Moornebel.
- **Zone im Ried:** Eine Mirepip-Herde ist verstummt; Lösung durch Heilen des Alpha.
- **Schwimmreiten:** Falls noch nicht in Saltrand erhalten, übergibt die Moorgemeinde den Schwimmsattel (Undfin).
- Der **versunkene Turm** ist sichtbar, aber verschlossen: „Erst, wenn alle Akkorde des Westens klingen“ – Vorbereitung für MQ_A1_08.

**Akkord des Nebels.**

### MQ_A1_05 · Gezeiten und Handel (Saltrand, Intensität 6)

**Saltrand-Hafen**, Sitz des Goldklang-Kontors. **Marieke Holm** begrüßt den Spieler mit einer Rechnung („Du hast meinen Hafen gerettet, bevor ich dich darum bitten konnte – das ist schlechtes Geschäft. Für mich.“). Die Fischgründe vor der Küste sind verstummt; die Fischerei steht still.

- Optional: Kontor-Kredit (Schwimmsattel sofort gegen einen Gefallen) → `FLAG_KONTOR_DEBT` = 1; in Akt II fordert Marieke den Gefallen ein (eine Lieferung, die moralisch grau ist).
- **Arena ARN_06:** Beke Tamsen, Gezeitenbecken.
- **Zone im Riffgrund:** Tauchen mit Schwimmreittier; ein verstummter Aquafin-Schwarm.

**Akkord der Gezeiten.**

### MQ_A1_06 · Die Stillsteine (dynamisch, Intensität 8)

Diese Quest beginnt in der **zweiten** besuchten Region (Kharsgrat, Morvenmoor oder Saltrand) und wird an deren Zone angehängt (§7). Der Spieler findet die Zone nicht nur verstummt, sondern **verstärkt**: Graue Steine in einem Kreis, von Ordensleuten in Schweigegewändern gepflegt.

**Ordenskommandant Ulrek** (BOSS_A1_02, Kraggoth) stellt sich: kein Fanatiker, sondern einer, der die Klangpest überlebt hat.

> **Ulrek:** „Du nennst es Heilung. Ich habe gesehen, was ein Lied anrichtet, wenn es zu laut wird. Eiðvik hat geschrien, drei Tage lang. Dann war es still. Wir bringen nur die Stille, bevor das Schreien beginnt.“

Nach dem Kampf erscheint **Sereth Vaun** – ruhig, ohne Wachen, mit einem Stillstein in der Hand.

> **Sereth:** „Ulrek hat seine Wahl getroffen. Ich treffe meine: Ich gehe. Aber hör mir zu, Wärter. Du hörst den Ton darunter. Das tun nicht viele. Frag dich, ob er dir gehört – oder ob du ihm gehörst.“
> *(einfühlsam)* „Ihr nehmt den Echos ihre Stimme.“ · *(neugierig)* „Was meint Ihr damit?“ · *(entschlossen)* „Haltet euch aus meinen Zonen raus.“
> → `FLAG_SERETH_RESPECT` (+1 / +1 / −1)

**W2 enthüllt:** Der Orden verstärkt die Zonen mit Stillsteinen. Die Splitter (Echo-Material `ITM_EMAT_STILLSHARD`) bringt der Spieler zu Ysolde.

### MQ_A1_07 · Ein Riss im Lied (nach 3 Akkorden, Intensität 4)

In Eichenhall eröffnet die **Akademie der Resonanz** eine Außenstelle. **Rektor Aldric Venn** hält eine Rede auf dem Marktplatz: Die Akademie werde die Stillezonen *messen, ordnen, verstehen*.

> **Venn:** „Wir fürchten die Stille, weil wir das Lied nicht verstehen. Ich biete euch kein Wunder an. Ich biete euch Ordnung. Ordnung ist nicht das Gegenteil von Freiheit – sie ist ihre Bedingung.“

Venn spricht den Spieler persönlich an, freundlich, interessiert an den Stillstein-Splittern. Er bittet, ein Klangfragment analysieren zu dürfen, und gibt es verbessert zurück (eine Wort-Lücke weniger – er kann mehr hören, als er zugibt). **Kael** wird vor den Augen des Spielers als **Akademie-Anwärter** aufgenommen; Venn legt ihm die Hand auf die Schulter.

> **Kael:** „Er glaubt, man kann es lernen. Das Hören. Du nicht?“
> *(einfühlsam)* „Ich hoffe es für dich.“ (+1) · *(neugierig)* „Was misst er eigentlich?“ (0) · *(entschlossen)* „Ich traue ihm nicht.“ (−1, Kael verteidigt Venn)

### MQ_A1_08 · Der versunkene Turm (nach 4 Akkorden, Morvenmoor, Intensität 9)

Mit vier Akkorden öffnet sich der **versunkene Turm** unter Morvenfurt: Die Akkorde klingen zusammen und das Wasser weicht. Ysolde und – je nach Flag – Tavesh begleiten den Spieler bis zum Eingang.

Unten: der **Stillkern im Morvenmoor** (BOSS_A1_03, Umbracoil). Phasen-Heilung, Begleiter, Stillezähler (K35 §6.1). Nach dem Sieg erwacht nicht nur Umbracoil: Am Grund des Turms schlägt etwas – die schlafende Ursprungsstimme **Nhael'vesh** regt sich im Schlaf; ihr Nebel durchdringt den Spieler.

**Vision (Ilen).** Ein Raum aus Licht und Notenlinien. Eine Frau im Gewand des Erstchors, das Gesicht abgewandt. Vor ihr ein Riss – dahinter eine lautlose, unendliche Tiefe. Sie hält ihn mit beiden Händen zu; ihr Ton ist dünn geworden.

> **Ilen (verzerrt, L-01):** „…hält nicht mehr… die Stimmen sind unruhig… wenn sie erwachen, ohne dass jemand…“ *(Der Ton bricht.)*

**W3 enthüllt:** Die eigentliche Ursache der Stillezonen ist ein **Riegel**, der schwächer wird; der Orden beschleunigt es nur. Ysolde hört die Beschreibung des Spielers und wird blass.

> **Ysolde:** „…Ilen.“
> *(neugierig)* „Du kennst den Namen?“ → **Ysolde:** „Jedes Kind kennt die Lieder vom Erstchor. Komm. Du brauchst Schlaf.“ *(Sie lügt nicht – aber sie sagt nicht alles. W5 bleibt verborgen.)*

### MQ_A1_09 · Nachklang (Intensität 2)

Rückkehr nach **Lindwiesen**. Ein ruhiger Abend: Lager-Moment mit dem ganzen Chor, Gespräche mit der Familie, ein Brief von Kael (Ton je nach `FLAG_KAEL_TRUST`). Ysolde steht lange am Klangbrunnen.

> **Ysolde:** „Die Weite, Ignareth, Hvitfell. Die Stillezonen sind älter dort. Hralda kennt Leute im Norden. Und… wenn du in Hvitfell bist, geh nach Eiðvik. Hör hin.“

Freischaltungen: **Zucht** (Rang 14, K38), Hain-Ausbau; Akt II öffnet R04/R05/R07.

---

## 7. Freie Reihenfolge: dynamische Erzählung

Kharsgrat (3a), Morvenmoor (3b) und Saltrand (3c) sind frei wählbar. Damit die Erzählung trotzdem eine Mitte und ein Ende hat:

| Position | Was passiert | Technik |
|---|---|---|
| Erste besuchte Region | Regionsquest ohne Orden; Ysolde in einer anderen Region gemeldet | Standardvariante |
| **Zweite** besuchte Region | Regionsquest + **MQ_A1_06 Die Stillsteine** wird an deren Zone angehängt (Ulrek, Sereth, W2) | Variante „W2“; `FLAG_W2_REGION` |
| Dritte besuchte Region | Regionsquest; Ordenswachen an der Zone (W2 bekannt), Dialoge beziehen sich auf Ulrek | Variante „nach W2“ |
| Nach drei Akkorden | MQ_A1_07 (Venn) in Eichenhall | Bedingung Akkordzahl |
| Nach vier Akkorden | MQ_A1_08 im Morvenmoor (Turm) – auch wenn Morvenmoor zuerst besucht wurde | Turm bleibt bis dahin verschlossen |

**Skalierung:** Arenen und Zonen fixieren ihre Stufe beim ersten Betreten (CANON §51); Story-Bosse skalieren mit (BOSS_A1_02 nutzt die Zonenstufe der zweiten Region).

---

## 8. Entscheidungen und Flags

| DisplayName | Range | SetIn | Affects |
|---|---|---|---|
| Haltung zu den Freien Stimmen | -2..2 | MQ_A1_04|MQ_A2_* | Epilog Freie Stimmen verbündet/verfeindet; Tavesh im Finale |
| Vertrauen Kael | -2..2 | MQ_P02|MQ_A1_07|MQ_A2_*|MQ_A3_* | Kaels Umkehr (immer), Epilog Kael gerettet/an Venns Seite verloren (nie tot) |
| Respekt Sereth | -2..2 | MQ_A1_06|MQ_A2_*|MQ_A3_* | Sereths Angebot im Finale (immer möglich), Epilog Sereth versöhnt/gebrochen |
| Schuld beim Kontor | 0..1 | MQ_A1_05 | Marieke Holms Gefallen in Akt II |
| Starterlinie | Bloom|Stone|Storm | MQ_P01 | Kaels Starter (Vorteil), Dialogvarianten |
| Region der W2-Enthüllung | R02|R03|R06 | MQ_A1_06 | Ortsbezug späterer Dialoge |

**Regel:** Keine Entscheidung in Akt I sperrt Inhalte. Flags verändern Dialoge, die Bereitschaft von Figuren und den Epilog (K46). Die drei Haltungen (einfühlsam/neugierig/entschlossen) sind gleichwertig; `FLAG_KAEL_TRUST` und `FLAG_SERETH_RESPECT` sind zusätzlich über Nebenquests veränderbar (K49–K51).

---

## 9. Zwischensequenzen und Leitmotive

| Szene | Länge | Leitmotiv (K55) |
|---|---|---|
| Kalte Eröffnung (Nimbara-Vision) | 0:45 | Weltlied-Thema (voll) → Abbruch |
| Stillezone bricht aus | 0:30 | Stille-Motiv (Pausen, gedämpfte Streicher) |
| Erstresonanz | 0:40 | Wärter-Thema (erste volle Fassung) |
| Gleitpanorama | 0:35 | Verdanthain-Thema + Wärter-Thema |
| Maelis nach dem Sieg | 0:25 | Arena-Fanfare (Blüte-Variation) |
| Vernaune erwacht | 0:20 | Verdanthain-Thema, Chor |
| Ulrek / Sereth | 1:10 | Orden-Thema (Glocken, Schweigen) |
| Venns Rede | 1:00 | Akademie-Thema (Ordnung, Streicher-Kanon) |
| Vision Ilens | 1:30 | Ilen-Motiv (erstmals, fragmentiert) |
| Nachklang-Abend | 0:50 | Lindwiesen-Thema (Nachtversion) |

Alle Zwischensequenzen sind überspringbar, In-Engine (Sequencer), mit Echtzeit-Begleiter des Spielers im Bild.

---

## 10. Quest-Daten

| Name | Act | Order | Region | Title | Prerequisite | Truth | Intensity | DurationMin | Boss | Akkord | Rewards |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MQ_P01 | Prolog | 1 | R01 | Ein Ton im Dunkel | Spielstart | W1 | 7 | 52 |  |  | Starter-Echo, Resonanzsinn |
| MQ_P02 | Prolog | 2 | R01 | Der verstummte Wächter | MQ_P01 | – | 6 | 40 | BOSS_P01 |  | Resonator, 300 Wärter-EP |
| MQ_P03 | Prolog | 3 | R01 | Was der Wald erzählt | MQ_P02 | – | 3 | 88 |  |  | Gleiter, erster Resonanzstein, 500 Wärter-EP |
| MQ_A1_01 | Akt I | 1 | R01 | Die Arena der Wurzeln | MQ_P03 | – | 5 | 120 |  | ARN_01 | Akkord der Wurzeln, Wildwacht-Lizenz, Bodensattel |
| MQ_A1_02 | Akt I | 2 | R01 | Stille über Lindwald | MQ_A1_01 | – | 7 | 75 | BOSS_A1_01 |  | 1.500 Wärter-EP, Klangfragment-Hinweis |
| MQ_A1_03 | Akt I | 3a | R02 | Fels und Ahnen | MQ_A1_02 | – | 6 | 180 |  | ARN_02 | Akkord des Fels, Klettersattel |
| MQ_A1_04 | Akt I | 3b | R03 | Nebel über dem Moor | MQ_A1_02 | – | 6 | 180 |  | ARN_03 | Akkord des Nebels, Schwimmsattel (falls noch nicht) |
| MQ_A1_05 | Akt I | 3c | R06 | Gezeiten und Handel | MQ_A1_02 | – | 6 | 180 |  | ARN_06 | Akkord der Gezeiten, Schwimmsattel (falls noch nicht) |
| MQ_A1_06 | Akt I | 4 | dyn | Die Stillsteine | Zweite Regionsquest (3a/3b/3c) abgeschlossen | W2 | 8 | 70 | BOSS_A1_02 |  | 2.000 Wärter-EP, Stillstein-Splitter ×3 |
| MQ_A1_07 | Akt I | 5 | R01 | Ein Riss im Lied | 3 Akkorde | – | 4 | 60 |  |  | Akademie-Zugang (Außenstelle), 1.000 Wärter-EP |
| MQ_A1_08 | Akt I | 6 | R03 | Der versunkene Turm | 4 Akkorde + MQ_A1_06 | W3 | 9 | 90 | BOSS_A1_03 |  | 3.000 Wärter-EP, Vision Ilens |
| MQ_A1_09 | Akt I | 7 | R01 | Nachklang | MQ_A1_08 | – | 2 | 45 |  |  | Zucht-Freischaltung (Rang 14), Hain-Ausbau, Akt II |

---

### 10.1 Quest-Zusammenfassungen

| Name | Title | Summary |
|---|---|---|
| MQ_P01 | Ein Ton im Dunkel | Erwachen in Lindwiesen, Ysolde und Kael, Stillezone bricht im Lindwald aus, Spurwahl und Erstresonanz |
| MQ_P02 | Der verstummte Wächter | Kampf gegen den verstummten Lorncant, Ysolde versiegelt die Zone, Rivalenkampf gegen Kael |
| MQ_P03 | Was der Wald erzählt | Freie Zone Lindwald, Beobachtungen, Ruine mit Klangrätsel, Gleitpanorama, Reise nach Eichenhall |
| MQ_A1_01 | Die Arena der Wurzeln | Eichenhall: Wildwacht-Lizenz bei Hralda Brakk, Vorprüfung, Maelis Wendt |
| MQ_A1_02 | Stille über Lindwald | Die Zone kehrt zurück; Stillkern um Vernaune; Stillezonen in drei Regionen gemeldet – der Weg teilt sich |
| MQ_A1_03 | Fels und Ahnen | Kharsholm, Torvik Hrall, Ahnenfelsen, Stillezone am Grat, Kletterreiten |
| MQ_A1_04 | Nebel über dem Moor | Morvenfurt, Freie Stimmen in der Unterstadt, Evhe Corrach (nachts), Moorgemeinde |
| MQ_A1_05 | Gezeiten und Handel | Saltrand-Hafen, Marieke Holm und das Kontor, Beke Tamsen, verstummte Fischgründe |
| MQ_A1_06 | Die Stillsteine | Ordenskommandant Ulrek verstärkt eine Zone mit Stillsteinen; erste Begegnung mit Sereth Vaun |
| MQ_A1_07 | Ein Riss im Lied | Rektor Aldric Venn in Eichenhall; Kael wird Akademie-Anwärter; Klangfragment-Analyse |
| MQ_A1_08 | Der versunkene Turm | Stillkern im Morvenmoor unter dem versunkenen Turm; Vision: Ilens Riegel um Velnox schwächelt |
| MQ_A1_09 | Nachklang | Rückkehr nach Lindwiesen; Ysolde schweigt zu einer Frage; Weg in die Weite, nach Ignareth und Hvitfell |

### 10.2 Dialogvarianten nach Haltung

Jede Hauptquest bietet mindestens eine Haltungs-Antwort (ADR-162). Die drei Antworten sind gleich lang, gleich wertvoll und führen zum selben Questziel; sie färben nur die Reaktion der Figur und setzen die in der letzten Spalte genannten Flags. Die Tabelle ist die Vorlage für das Dialog-Team (K48 Quest-Bibel); Zeilen-IDs folgen `DLG_<Quest>_<Nr>`.

| Zeile | Situation | Einfühlsam | Neugierig | Entschlossen | Flag-Effekt |
|---|---|---|---|---|---|
| DLG_P01_01 | Kael fragt, ob man Angst vor der Stille habe | „Ich habe Angst um die Echos da drin.“ | „Ich will wissen, was sie ist.“ | „Angst hilft niemandem. Gehen wir.“ | – |
| DLG_P02_02 | Der verstummte Wächter liegt geheilt am Boden | Echo streicheln, warten bis es aufsteht | Klang des Wächters mit dem Resonator abhören | Den Weg sichern, Kael zum Wächter schicken | – |
| DLG_P03_03 | Ysolde übergibt den Resonator | „Ich passe auf ihn auf.“ | „Wer hat ihn gebaut?“ | „Ich werde ihn brauchen.“ | – |
| DLG_A1_01_01 | Kael verliert den Arena-Kampf gegen den Spieler | Trösten, ihm ein Rückspiel anbieten | Nach seiner Taktik fragen | „Du warst zu schnell zu sicher.“ | KAEL_TRUST +1 / 0 / −1 |
| DLG_A1_02_02 | Stillezone am Lindwald-Rand, ein Echo sitzt stumm | Neben das Echo setzen | Die Ränder der Zone vermessen | Die Zone direkt betreten | – |
| DLG_A1_03_01 | Die Ahnenhüterin fragt nach dem Respekt vor Gräbern | „Die Toten haben hier Vorrang.“ | „Was erzählen die Steine?“ | „Wir müssen trotzdem hinein.“ | – |
| DLG_A1_04_03 | Tavesh bittet, Freie Stimmen nicht zu verraten | „Euer Geheimnis ist bei mir sicher.“ | „Warum versteckt ihr euch?“ | „Wenn ihr Schaden anrichtet, sage ich es.“ | FS_STANCE +1 / 0 / −1 |
| DLG_A1_05_02 | Kontor bietet einen Vorschuss an | Ablehnen, der Fischerin am Kai helfen | Bedingungen erfragen und verhandeln | Annehmen, sofort weiter | KONTOR_DEBT 0 / 0 / 1 |
| DLG_A1_06_04 | Sereth hält das Schwert gesenkt und spricht | „Du klingst müde.“ | „Wem gehorchst du wirklich?“ | „Geh mir aus dem Weg.“ | SERETH_RESPECT +1 / +1 / −1 |
| DLG_A1_06_05 | Ulrek liegt besiegt, der Orden zieht ab | Ulrek aufhelfen | Seinen Befehl lesen | Den Stillstein zerbrechen | SERETH_RESPECT 0 / +1 / 0 |
| DLG_A1_07_02 | Venn bietet Kael den Anwärterstatus an | „Du hast es dir verdient.“ | „Was ändert sich für ihn?“ | „Er wird uns noch retten.“ | KAEL_TRUST +1 / 0 / +1 |
| DLG_A1_08_03 | Vision Ilens im versunkenen Turm | Ilens Hand nehmen | Fragen, warum sie schwieg | Den Turm verlassen, bevor er fällt | – |
| DLG_A1_09_01 | Ysoldes Brief am Lagerfeuer | Antwort schreiben | Den Brief zweimal lesen, Notiz im Kodex | Brief einstecken, aufbrechen | – |

**Regeln für Dialog-Autor:innen**
1. Keine Antwort darf „falsch“ wirken; Wortanzahl der drei Antworten ±20 %.
2. Flag-Änderungen werden nie angekündigt (keine „Kael wird sich daran erinnern“-Einblendung).
3. Jede Figur reagiert auf jede Haltung mit eigener Zeile; Sammelreaktionen sind verboten.
4. Echos reagieren nonverbal (Animation `React_Soft`, `React_Curious`, `React_Brace`, K57).
5. Barks nach Entscheidungen werden bis zum Ende des Akts einmalig wiederholt (Rückbezug), danach nicht mehr.

### 10.3 Begegnungs- und Belohnungstakt

| Abschnitt | Kämpfe (Pflicht) | Kämpfe (optional) | Bindungsgelegenheiten | Neue Systeme | Ziel-Spielzeit |
|---|---|---|---|---|---|
| Prolog | 3 | 2 | 1 (Erstresonanz) | Zeitleiste, Resonanzsinn, Gleiter | 3 h |
| MQ_A1_01–02 | 4 | 6 | 4 | Formation, Kodex-Aufgaben, Klangfragmente | 2 h |
| Regionsquests (3) | je 5 | je 12 | je 8 | Region-Traversal (Kletterhaken, Sumpfboot, Gezeitenkarte) | je 3 h |
| MQ_A1_06 | 4 + Boss | 3 | 2 | Stillesteine (Puzzle), Ordensgegner | 1,5 h |
| MQ_A1_07–09 | 3 + Boss | 4 | 3 | Resonanzhain-Freischaltung, Akkord-Fusion | 2,5 h |
| **Summe Akt I inkl. Prolog** | ~32 | ~51 | ~34 | | **~18 h** |

Die Summe deckt sich mit der Rangkurve aus K43 §6 (Prolog + Akt I ≈ 18 h, Wärterrang ~16 am Ende von Akt I, Zucht-Freischaltung bei Rang 14 in MQ_A1_09).

## 11. Anforderungen an andere Abteilungen

| Abteilung | Anforderung |
|---|---|
| Level Design | Lindwald (freie Zone 0,8 km², Ruine mit Klangrätsel, Ruinenturm mit Panorama); Stillezonen-Varianten für Grat, Ried, Riffgrund (je mit Stillstein-Kreis-Variante für W2); versunkener Turm (wasserfreie Variante nach Akkord 4) |
| Cinematics | 10 Sequenzen (§9), Begleiter-Echtzeit-Einbindung |
| Audio | Leitmotive Weltlied, Wärter, Stille, Orden, Akademie, Ilen; Stillezonen-Mix (Hochpass, Pausen) |
| Combat | BOSS_P01, BOSS_A1_01–03 (K35) |
| Narrative | ~1.200 Dialogzeilen Akt I (Haupt), Barks für Ordenswachen, Briefe Ysolde/Kael |
| UX | Haltungswahl (3 Symbole), Questlog mit „Der Weg teilt sich“-Ansicht |

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-161 | W2 in der zweiten besuchten Region (dynamische Anhängung) | Freie Reihenfolge + verlässliche Erzählmitte | Feste Region für W2 (bricht Freiheit) |
| ADR-162 | Spieler antwortet mit drei gleichwertigen Haltungen | Rollenspiel ohne Moral-Meter, keine Bestrafung | Gut/Böse-Leiste |
| ADR-163 | Ysolde ist in Akt I „präsent ohne mitzulaufen“ (Briefe, Sichtungen) | Mentorin bleibt wichtig, Spieler bleibt Hauptfigur | Begleiterin auf Dauer |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §168 | Erzählprinzipien: L-01, Venns Regel, DR-09, freie Reihenfolge, DR-14, DR-29, drei Haltungen (einfühlsam/neugierig/entschlossen), Echos als Figuren | LOCKED |
| §169 | Prolog MQ_P01–P03 (Ein Ton im Dunkel, Der verstummte Wächter, Was der Wald erzählt); W1; Resonator von Ysolde; Gleiter aus der Ruine; erstes Klangfragment | LOCKED |
| §170 | Akt I MQ_A1_01–09: Arena der Wurzeln, Stille über Lindwald, drei freie Regionsquests, Die Stillsteine (2. Region, Ulrek, Sereth, W2), Ein Riss im Lied (Venn, Kael Anwärter), Der versunkene Turm (W3, Vision Ilens), Nachklang | LOCKED |
| §171 | Story-Flags (`StoryFlags.csv`): FS_STANCE, KAEL_TRUST, SERETH_RESPECT (−2…2), KONTOR_DEBT, STARTER_LINE, W2_REGION | LOCKED |
| §131 | BOSS_A1_02 heißt „Ordenskommandant Ulrek“ und erscheint in der zweiten besuchten Region | aktualisiert |
| §10 | ADR-161 – ADR-163 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Logline, Themen, Ton, Erzählprinzipien
- [x] Akt-Struktur mit Intensitätskurve (DR-29)
- [x] Figuren in Akt I
- [x] Prolog (3 Hauptquests) mit Szenen und Dialogen
- [x] Akt I (9 Hauptquests) mit Szenen, Dialogen, Entscheidungen
- [x] Dynamische Erzählung bei freier Regionsreihenfolge
- [x] Story-Flags, Zwischensequenzen, Leitmotive
- [x] Quest-Daten, Anforderungen, ADR-161 – ADR-163, CANON §168–§171

➡️ **Nächstes Kapitel: K45 – Story II: Akt II „Die Schlösser der Stimmen“.**
