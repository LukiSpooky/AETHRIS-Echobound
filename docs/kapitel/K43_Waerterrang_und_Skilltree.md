# K43 · Wärterrang und Skilltree

| Feld | Wert |
|---|---|
| Dokument | Kapitel 43 von 68 · Systeme, Teil VIII |
| Version | 1.0 |
| Owner | Lead Systems Designer (Progression) |
| Mitwirkende | Balancing Analyst, UX Lead (Skilltree-UI), Lead Combat Designer (Kampf-Ast), Online-Designer (Ranked-Regeln) |
| Baut auf | ADR-008 (Wärterrang 1–40), CANON §6.2 (Äste Bindung/Überleben/Forschung/Kampf), §15 (Chorgröße, Freischaltungen – PROVISIONAL), §18 (Wärter-EP-Anteile), K02 §13.2 (`FWardenRankRow`), K36–K42 (Systeme, die Skills verstärken) |
| Status | ✅ Freigegeben – **löst Q14** (Wärterrang-EP-Kurve) |
| Im Repository | `Data/Progression/WardenRank.csv` (40 Ränge), `Data/Progression/Skills.csv` (48 Fähigkeiten), `tools/ref/aethris_progression.py` |
| Neue Kanon-Einträge | CANON §164 (Wärterrang & EP-Kurve), §165 (Freischaltungen & Chorgröße), §166 (Skilltree), §167 (Skillpunkte & Neustimmung) |

---

## Inhalt

1. [Zwei Fortschritte: Echos und Wärter](#1-zwei-fortschritte-echos-und-wärter)
2. [Wärter-EP und Quellen](#2-wärter-ep-und-quellen)
3. [Die Rangkurve (Q14)](#3-die-rangkurve-q14)
4. [Freischaltungen und Chorgröße](#4-freischaltungen-und-chorgröße)
5. [Der Skilltree](#5-der-skilltree)
6. [Skillpunkte und Neustimmung](#6-skillpunkte-und-neustimmung)
7. [Builds und Spielstile](#7-builds-und-spielstile)
8. [Ranked und Koop](#8-ranked-und-koop)
9. [UI](#9-ui)
10. [Code](#10-code)
11. [Tests und Telemetrie](#11-tests-und-telemetrie)
12. [Decision Records](#12-decision-records)
13. [Kanon-Änderungen](#13-kanon-änderungen)
14. [Kapitel-Checkliste](#14-kapitel-checkliste)

---

## 1. Zwei Fortschritte: Echos und Wärter

| Spur | Wer | Maximum | Wirkung |
|---|---|---|---|
| Echo-Level (P1) | jedes Echo | 100 | Kampfwerte (K18) |
| **Wärterrang (P6)** | der Spieler | 40 | Freischaltungen (Formate, Chorgröße, Zucht, Raid, Ranked), Skillpunkte |
| **Skilltree (P7)** | der Spieler | 48 Fähigkeiten | Komfort, Wissen, Werkzeuge – **keine rohe Kampfkraft** |

Der Wärterrang wächst aus **allem**, was der Spieler tut (Quests, Entdeckungen, Kodex, Arenen), nicht nur aus Kämpfen. Damit lohnen alle drei Primär-Loops gleichermaßen (K02 §5).

---

## 2. Wärter-EP und Quellen

| Quelle | Wärter-EP | Zielanteil (CANON §18) |
|---|---|---|
| Hauptquest-Schritt | 300–1.500 | Haupt 25 % |
| Nebenquest | 400–2.000 | Neben 25 % |
| Kodex-Stufe 1/2/3/4 | 10 / 30 / 60 / 120 | Kodex 20 % |
| Klangfragment | 80 | Kodex |
| Entdeckung (POI, Aussicht, Resonanzstein) | 20–150 | Entdeckung 15 % |
| Arena (Vorprüfung/Akkord) | 300 / 2.000 | Arenen 10 % |
| Aufträge, Crafting, Fotos, Zucht | 10–200 | Sonstiges 5 % |

Kämpfe selbst geben **keine** Wärter-EP (nur Echo-EP); Arenen und Story-Kämpfe zählen über ihre Quest- und Akkord-Belohnung. So wird niemand zum Grinden von Wildkämpfen für den Wärterrang gedrängt.

---

## 3. Die Rangkurve (Q14)

```
EP(Rang) = max( 300 × (Rang − 1),  rund100( 154 × (Rang − 1)^1,94 ) )
```

Die Kurve trifft die Stützstellen aus K02 §13.2 (Rang 5 ≈ 2.600, 10 ≈ 11.000, 14 ≈ 21.500, 22 ≈ 52.000, 28 ≈ 86.000, 40 ≈ 190.000) mit ±10 % und ist glatt (keine Sprünge).

| Rank | RequiredWardenXP | SkillPointsGranted | ChorCapacity | Unlocks |
|---|---|---|---|---|
| 1 | 0 | 0 | 2 | Feature.Chor2 |
| 2 | 300 | 1 | 3 | Feature.Chor3 |
| 3 | 600 | 1 | 3 |  |
| 4 | 1300 | 1 | 3 |  |
| 5 | 2300 | 1 | 4 | Feature.Combat.Duo|Feature.Chor4 |
| 6 | 3500 | 1 | 4 |  |
| 7 | 5000 | 1 | 4 |  |
| 8 | 6700 | 1 | 4 |  |
| 9 | 8700 | 1 | 4 |  |
| 10 | 10900 | 2 | 5 | Feature.Combat.Trio|Feature.Chor5 |
| 11 | 13400 | 1 | 5 |  |
| 12 | 16100 | 1 | 5 |  |
| 13 | 19100 | 1 | 5 |  |
| 14 | 22300 | 1 | 6 | Feature.Breeding|Feature.Chor6 |
| 15 | 25800 | 1 | 6 |  |
| 16 | 29500 | 1 | 6 |  |
| 17 | 33400 | 1 | 6 |  |
| 18 | 37500 | 1 | 6 | Feature.Contracts.Tier3 |
| 19 | 42000 | 1 | 6 |  |
| 20 | 46600 | 2 | 6 |  |
| 21 | 51500 | 1 | 6 |  |
| 22 | 56600 | 1 | 6 | Feature.Raid |
| 23 | 61900 | 1 | 6 |  |
| 24 | 67500 | 1 | 6 |  |
| 25 | 73300 | 1 | 6 | Feature.Tutors.Rank4 |
| 26 | 79300 | 1 | 6 |  |
| 27 | 85600 | 1 | 6 |  |
| 28 | 92100 | 1 | 6 | Feature.Ranked |
| 29 | 98900 | 1 | 6 |  |
| 30 | 105800 | 2 | 6 |  |
| 31 | 113000 | 1 | 6 |  |
| 32 | 120400 | 1 | 6 | Feature.DeepResonance.Master |
| 33 | 128100 | 1 | 6 |  |
| 34 | 136000 | 1 | 6 |  |
| 35 | 144100 | 1 | 6 |  |
| 36 | 152400 | 1 | 6 | Feature.Hain.Stage5 |
| 37 | 161000 | 1 | 6 |  |
| 38 | 169800 | 1 | 6 |  |
| 39 | 178800 | 1 | 6 |  |
| 40 | 188000 | 2 | 6 | Feature.Title.Grandwarden |

### 3.1 Rang über die Spielzeit

Mit den Wärter-EP-Raten typischer Spielweise (`aethris_progression.timeline()`):

| Abschnitt | Spielzeit | Wärter-EP/h | EP am Ende | Rang am Ende | Ø Minuten je Rang |
|---|---|---|---|---|---|
| Prolog | 3 h | 800 | 2.400 | 5 | 45 |
| Akt I | 15 h | 2.000 | 32.400 | 16 | 81 |
| Akt II | 20 h | 2.000 | 72.400 | 24 | 150 |
| Akt III | 12 h | 2.500 | 102.400 | 29 | 144 |
| Endgame 1–20 h | 20 h | 2.800 | 158.400 | 36 | 171 |
| Endgame 20–40 h | 20 h | 3.000 | 218.400 | 40 | 300 |
| Endgame 40–60 h | 20 h | 3.000 | 278.400 | 40 | – |

**Ergebnis:** Story-Finale bei **Rang ~29** (CANON §15: ~28 ✓), Zucht (Rang 14) am Ende von Akt I ✓, Raid (22) in Akt II, Ranked (28) in Akt III. Rang 40 nach ~90 Spielstunden.

**CR-003:** K02 nannte als Ziel „Wärterrang-Aufstieg 45–90 min (Story-Phase)“. Mit 40 Rängen über ~90 Stunden gilt das für Prolog und Akt I (45–81 min); in Akt II/III liegen Aufstiege bei ~145–150 min. Begründung: Ränge sind Meilensteine mit Freischaltungen; zwischen ihnen tragen Echo-Level, Bindungsstufen, Kodex und Akkorde den gefühlten Fortschritt (K02 §6 „Belohnungsrhythmus“ bleibt erfüllt). Das Ziel wird präzisiert zu „45–90 min in Prolog/Akt I, ≤ 150 min in Akt II/III“.

---

## 4. Freischaltungen und Chorgröße

| Rang | Freischaltung | Kapitel |
|---|---|---|
| 1 | Chor 2 | – |
| 2 | Chor 3 | – |
| 5 | Chor 4, **Duo-Format** | K33 |
| 10 | Chor 5, **Trio-Format** | K33 |
| 14 | Chor 6 (Maximum, ADR-009), **Zucht** | K38 |
| 18 | Aufträge Stufe 3 (seltene Aufträge) | K13 |
| 22 | **Raids** | K35 |
| 25 | Tutoren mit Ruf 4 (zweite Tutorstufe) | K29 |
| 28 | **Ranked** | K61 |
| 32 | Tiefenresonanzen Meisterstufe | K62 |
| 36 | Hain-Ausbau Stufe 5 | K37 |
| 40 | Titel „Großwärter/in“ (Kosmetik) | – |

Damit sind die PROVISIONAL-Werte aus CANON §15 bestätigt (Chorgröße 2/3/4/5/6 bei Rang 1/2/5/10/14; Duo 5, Trio 10, Zucht 14, Raid 22, Ranked 28).

---

## 5. Der Skilltree

Vier Äste mit je zwölf Fähigkeiten in vier Stufen (Tier 0/5/10/15 = benötigte Punkte im Ast). Kosten 1–3 Punkte; Summe aller Kosten **88**.

```
        BINDUNG                 ÜBERLEBEN               FORSCHUNG               KAMPF
 T0  Leiser Schritt (1)     Ausdauer I (1)          Resonanzsinn I (1)      Taktiker (1)
     Köderkunde (1)         Sammler (1)             Beobachter (2)          Erste Hilfe (1)
     Ruhige Hand (2)        Feldkoch (2)            Spurenleser (1)         Lehrmeister (2)
 T5  Einfühlung (1)         Wetterkunde I (1)       Typenkunde (2)          Wechselmeister (2)
     Fallenbau (2)          Kletterprofi (2)        Resonanzsinn II (2)     Harmonieführung (2)
     Siegelpflege (2)       Reitkunst (2)           Fotograf (1)            Konterkenntnis (1)
 T10 Herdenruf (2)          Ausdauer II (2)         Fragmentlauscher (2)    Kombokunde (2)
     Stimmlage (2)          Gleitkunst (2)          Evolutionsahnung (2)    Feldstratege (2)
     Seelenband (2)         Wetterkunde II (2)      Glyphenleser (2)        Schliffmeister (2)
 T15 Hainpflege (2)         Handwerk (2)            Resonanzsinn III (2)    Ruhiger Puls (2)
     Erbkunde (3)           Wegfinder (2)           Kodexgelehrte (2)       Vorausschau (2)
     Morphkunde (3)         Nachtauge (2)           Archivkunde (3)         Chorleiter (3)
```

| Branch | DisplayName | Tier | Cost | Requires | Effect | Ranked |
|---|---|---|---|---|---|---|
| Bindung | Leiser Schritt | 0 | 1 |  | Entdeckungsradius wilder Echos −10 % | – |
| Bindung | Köderkunde | 0 | 1 |  | Lieblingsköder einer Art schon ab Kodex-Stufe 1 sichtbar | – |
| Bindung | Ruhige Hand | 0 | 2 |  | Bindungs-Gut-Fenster ×1 | 05 |
| Bindung | Einfühlung | 5 | 1 |  | Bindungswert und Stimmung als Zahl sichtbar | ja |
| Bindung | Fallenbau | 5 | 2 | SK_BND_01 | Fallen wirken 20 statt 10 Spielminuten; 2 Fallen je Bindung erlaubt (nur eine wirkt auf R) | – |
| Bindung | Siegelpflege | 5 | 2 |  | Jedes 5. Siegel wird beim Anschlag nicht verbraucht (Zähler sichtbar) | – |
| Bindung | Herdenruf | 10 | 2 | SK_BND_05 | Ruhenetz: Bindung eines Herdenechos auch vor dem letzten möglich (1× je Kampf) | – |
| Bindung | Stimmlage | 10 | 2 | SK_BND_03 | Perfekt-Fenster +15 ms | – |
| Bindung | Seelenband | 10 | 2 | SK_BND_04 | Bindungszuwachs aller Echos +10 % | – |
| Bindung | Hainpflege | 15 | 2 |  | Hain-Ertrag +50 %; Stimmung im Hain +10 | – |
| Bindung | Erbkunde | 15 | 3 | SK_BND_09 | Allele im Kodex sichtbar (ab Kodex 4); Zuchtvorschau zeigt Loci | ja |
| Bindung | Morphkunde | 15 | 3 | SK_BND_11 | Morph-Chance ×2 (K38) | – |
| Überleben | Ausdauer I | 0 | 1 |  | Wärter-Ausdauer +10 | – |
| Überleben | Sammler | 0 | 1 |  | +1 Ertrag je Sammelknoten (Stufe I–III) | – |
| Überleben | Feldkoch | 0 | 2 |  | Gerichte wirken 2 Spieltage | – |
| Überleben | Wetterkunde I | 5 | 1 |  | Vorhersage: nächster Block aller besuchten Regionen (CANON §63 Stufe 2) | – |
| Überleben | Kletterprofi | 5 | 2 | SK_SUR_01 | Klettern verbraucht 25 % weniger Ausdauer | – |
| Überleben | Reitkunst | 5 | 2 |  | Reit-Ausdauer +20 % | – |
| Überleben | Ausdauer II | 10 | 2 | SK_SUR_05 | Wärter-Ausdauer +10 | – |
| Überleben | Gleitkunst | 10 | 2 |  | Gleiter-Sinkrate −0 | 15 m/s (wirkt wie halbe Stufe) |
| Überleben | Wetterkunde II | 10 | 2 | SK_SUR_04 | Vorhersage: 2 Blöcke + seltene Bedingungen (CANON §63 Stufe 3) | ja |
| Überleben | Handwerk | 15 | 2 | SK_SUR_02 | Rezepte −10 % Zutaten (abgerundet; mindestens 1) | – |
| Überleben | Wegfinder | 15 | 2 |  | Schnellreise auch von jedem Klangbrunnen aus | – |
| Überleben | Nachtauge | 15 | 2 |  | Nachtsicht ohne Laterne (Radius 15 m) | – |
| Forschung | Resonanzsinn I | 0 | 1 |  | Resonanzsinn-Reichweite +30 m | – |
| Forschung | Beobachter | 0 | 2 |  | Beobachtung dauert 2 statt 3 s (K39) | – |
| Forschung | Spurenleser | 0 | 1 |  | Spuren bleiben 20 statt 10 Spielminuten sichtbar | – |
| Forschung | Typenkunde | 5 | 2 |  | Effektivitätsvorschau schon ab Kodex-Stufe 1 | ja |
| Forschung | Resonanzsinn II | 5 | 2 | SK_RES_01 | Reichweite +30 m | – |
| Forschung | Fotograf | 5 | 1 |  | Fotobewertung Komposition +5 | – |
| Forschung | Fragmentlauscher | 10 | 2 | SK_RES_05 | Klangfragmente ab 60 m spürbar | – |
| Forschung | Evolutionsahnung | 10 | 2 |  | Evolutionsahnungen schon ab Kodex-Stufe 2 | ja |
| Forschung | Glyphenleser | 10 | 2 |  | Glyphe-Pfad-Tore ohne Feldfähigkeit lösbar | – |
| Forschung | Resonanzsinn III | 15 | 2 | SK_RES_05 | Reichweite +30 m (gesamt 150 m) | – |
| Forschung | Kodexgelehrte | 15 | 2 | SK_RES_02 | Kodex-Wärter-EP +25 % | – |
| Forschung | Archivkunde | 15 | 3 | SK_RES_07 | Klangfragmente oberhalb der Wahrheitsebene zeigen ein unverzerrtes Wort (Hinweis-Modus) | – |
| Kampf | Taktiker | 0 | 1 |  | Zeitleiste zeigt 12 statt 8 Züge | ja |
| Kampf | Erste Hilfe | 0 | 1 |  | Items im Kampf Zeitkosten 40 statt 60 | – |
| Kampf | Lehrmeister | 0 | 2 |  | Reserve-Echos erhalten 75 % statt 50 % EP | – |
| Kampf | Wechselmeister | 5 | 2 |  | Wechsel kostet 50 statt 60 Zeit | – |
| Kampf | Harmonieführung | 5 | 2 |  | Start-Harmonie +10 (zählt zur Synergie-Grenze 30) | – |
| Kampf | Konterkenntnis | 5 | 1 | SK_CMB_01 | Passive der Gegner ab Kodex 2 sichtbar | ja |
| Kampf | Kombokunde | 10 | 2 | SK_CMB_05 | Kombo-Fenster +10 Ticks | – |
| Kampf | Feldstratege | 10 | 2 |  | Eigene Terrains dauern 1 Runde länger | – |
| Kampf | Schliffmeister | 10 | 2 | SK_CMB_03 | Schliff-Training +2 Punkte | – |
| Kampf | Ruhiger Puls | 15 | 2 | SK_CMB_07 | Crescendo-Kosten −5 | – |
| Kampf | Vorausschau | 15 | 2 | SK_CMB_06 | Absicht der KI-Gegner vor ihrem Zug sichtbar (nicht PvP) | – |
| Kampf | Chorleiter | 15 | 3 | SK_CMB_05 | 3 Chor-Akkorde gleichzeitig (Grenze 30 bleibt) | – |

**Designregeln des Skilltrees:**
1. **Keine rohe Kampfkraft:** Kein Skill erhöht Echo-Werte oder Schaden. Kampf-Skills verbessern Information (Taktiker, Konterkenntnis, Vorausschau), Tempo von Wärter-Aktionen (Erste Hilfe, Wechselmeister) und Teamrhythmus (Harmonie, Kombos) – in kleinen, gedeckelten Schritten.
2. **Wissen bleibt Spielerwissen:** Forschungs-Skills beschleunigen Wissen, ersetzen es nicht (DR-01): Köderkunde zeigt den Lieblingsköder früher – aber der Spieler muss das Echo erst sichten.
3. **Jede Fähigkeit spürbar:** Kein „+2 %“; jede Fähigkeit verändert eine Entscheidung oder eine Routine.
4. **Querverweise:** Effekte nutzen ausschließlich vorhandene Systeme (K28–K42) – keine Sonderregeln.

---

## 6. Skillpunkte und Neustimmung

| Quelle | Punkte |
|---|---|
| Rangaufstieg 2–40 | 39 |
| Bonus bei Rang 10/20/30/40 | 4 |
| Kodex-Gesamtfortschritt 25/50/75/100 % | 4 |
| Akkorde: je 2 Akkorde | 5 |
| **Summe** | **52** von 88 (59 %) |

| Regel | Wert |
|---|---|
| Neustimmung (Respec) | Akademie-Labor oder Wildwacht-Lager; erste Neustimmung kostenlos, danach 500 ◎ × Rang/10 (aufgerundet) |
| Teil-Neustimmung | einzelne Fähigkeit zurücknehmen: 1/5 der Kosten, wenn keine abhängige Fähigkeit gelernt ist |
| Spezialisierung | Mit 52 Punkten kann ein Ast vollständig (22–25 Punkte) und ein zweiter weitgehend gelernt werden – oder alle Äste breit |

---

## 7. Builds und Spielstile

| Build | Schwerpunkt | Kernfähigkeiten |
|---|---|---|
| **Sammlerin** | Bindung + Forschung | Leiser Schritt, Ruhige Hand, Stimmlage, Beobachter, Köderkunde, Morphkunde |
| **Wanderer** | Überleben + Forschung | Ausdauer I/II, Kletterprofi, Gleitkunst, Wegfinder, Resonanzsinn I–III |
| **Strategin** | Kampf + Forschung | Taktiker, Konterkenntnis, Vorausschau, Typenkunde, Kombokunde, Chorleiter |
| **Züchter** | Bindung + Überleben | Seelenband, Hainpflege, Erbkunde, Morphkunde, Handwerk |
| **Fotografin** | Forschung | Fotograf, Beobachter, Spurenleser, Nachtauge (Überleben) |

Die Builds sind Vorschläge im Skilltree-Menü („Pfad hervorheben“), keine Klassen.

---

## 8. Ranked und Koop

| Regel | Wert |
|---|---|
| Ranked (DR-21) | Nur Skills mit „Ranked = ja“ wirken (Information/Komfort: Taktiker, Einfühlung, Typenkunde, Konterkenntnis, Erbkunde, Wetterkunde II, Evolutionsahnung); alle übrigen sind deaktiviert – faire Bedingungen für alle |
| Koop | Jeder Spieler nutzt eigene Skills; Kampf-Skills wirken auf die eigenen Echos (Harmonieführung zählt einmal je Seite, höchster Wert) |
| Raid | wie Koop; Chorleiter-Akkorde je Spieler |

---

## 9. UI

```
┌─ WÄRTER · Rang 17 · 33.400 / 37.500 EP ────────────────────────────────────────────────┐
│ Skillpunkte: 3     [Bindung 9]  [Überleben 6]  [Forschung 4]  [Kampf 3]                     │
│                                                                                              │
│   ◉ Leiser Schritt   ◉ Köderkunde   ◉ Ruhige Hand                                            │
│   ◉ Einfühlung       ◉ Fallenbau    ○ Siegelpflege (2)                                       │
│   ◎ Herdenruf (2)    ◎ Stimmlage (2) ◎ Seelenband (2)        ◉ gelernt  ○ verfügbar  ◎ ab Tier│
│                                                                                              │
│ Stimmlage: Perfekt-Fenster +15 ms – „Dein Anschlag trifft den Ton genauer.“                  │
│ [Lernen]  [Pfad: Sammlerin hervorheben]  [Neustimmung]                                       │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 10. Code

```cpp
// GF_Progression – Wärterrang
int64 Aethris::Progression::RequiredXP(int32 Rank)
{
    if (Rank <= 1) return 0;
    const int64 Linear = 300LL * (Rank - 1);
    const int64 Curve = FMath::RoundToInt64(154.0 * FMath::Pow(double(Rank - 1), 1.94) / 100.0) * 100;   // nur beim Import
    return FMath::Max(Linear, Curve);
}

void UWardenProgressionService::AddXP(int64 Amount, FGameplayTag Source)
{
    State.WardenXP += Amount;
    Telemetry->Record(TAG_Telemetry_WardenXP, Source, Amount);
    while (State.Rank < 40 && State.WardenXP >= RankTable[State.Rank].RequiredWardenXP)   // RankTable[i] = Rang i+1
    {
        const FWardenRankRow& Row = RankTable[State.Rank];
        ++State.Rank;
        State.SkillPoints += Row.SkillPointsGranted;
        for (const FGameplayTag& U : Row.Unlocks) Unlocks->Grant(U);
        Bus->Broadcast(TAG_Warden_RankUp, FRankUpMessage{ State.Rank });
    }
}
```

Die Kurve wird **nur beim Datenimport** berechnet (Fließkomma ist außerhalb der Determinismus-Zone unkritisch); zur Laufzeit gilt ausschließlich die ganzzahlige Tabelle `WardenRank.csv`.

---

## 11. Tests und Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Progression.Curve` | Tabelle monoton, Stützstellen ±10 % |
| `…Progression.Unlocks` | Freischaltungen genau einmal |
| `…Skills.Tree` | Tier-Bedingungen, Voraussetzungen, Kosten, Neustimmung |
| `…Skills.Ranked` | Ranked deaktiviert alle Skills ohne „ja“ |
| `Aethris.Func.Progression.StoryRank` | Bot-Durchlauf: Rang am Finale 27–31 |

**Telemetrie:** Rang am Ende jedes Akts, Skill-Wahlen (Popularität), Neustimmungen, Anteil EP je Quelle (Soll-Anteile CANON §18).

---

## 12. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-158 | Kämpfe geben keine Wärter-EP | Kein Grind-Druck, alle Loops gleichwertig | Wärter-EP je Kampf |
| ADR-159 | Skilltree ohne rohe Kampfkraft | Balance, Ranked-Fairness, DR-21 | Werte-Boni |
| ADR-160 | 52 von 88 Skillkosten erreichbar | Spezialisierung mit Identität | Alles freischaltbar |

---

## 13. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §164 | EP(Rang) = max(300 × (R−1), rund100(154 × (R−1)^1,94)); Tabelle `WardenRank.csv`; Wärter-EP-Quellen K43 §2 (keine EP aus Kämpfen); Finale ~Rang 29, Rang 40 nach ~90 h | LOCKED – **Q14 gelöst** |
| §165 | Chor 2/3/4/5/6 bei Rang 1/2/5/10/14; Duo 5, Trio 10, Zucht 14, Aufträge III 18, Raid 22, Tutoren II 25, Ranked 28, Tiefenresonanz-Meister 32, Hain V 36, Titel 40 (CANON §15 bestätigt) | LOCKED |
| §166 | Skilltree 4 × 12 (`Skills.csv`), Tiers 0/5/10/15, Kosten 1–3 (Σ 88), keine rohe Kampfkraft; Ranked nur Informations-/Komfort-Skills | LOCKED |
| §167 | Skillpunkte 52 (39 Ränge + 4 Rangboni + 4 Kodex + 5 Akkorde); Neustimmung erste kostenlos, dann 500 ◎ × ⌈Rang/10⌉ | LOCKED |
| §11 | CR-003: Rangaufstieg 45–90 min (Prolog/Akt I), ≤ 150 min (Akt II/III) | – |
| §10 | ADR-158 – ADR-160 | LOCKED |

---

## 14. Kapitel-Checkliste

- [x] Wärter-EP-Quellen und -Anteile
- [x] Rangkurve 1–40 als Daten (Q14), Simulation über die Spielzeit
- [x] Freischaltungen und Chorgröße final (CANON §15 bestätigt)
- [x] Skilltree 4 × 12 als Daten mit Designregeln
- [x] Skillpunkte, Neustimmung, Builds
- [x] Ranked/Koop-Regeln, UI, Code, Tests
- [x] CR-003, ADR-158 – ADR-160, CANON §164–§167

➡️ **Nächstes Kapitel: K44 – Story, Akt I (Prolog bis „Der Riegel“).**
