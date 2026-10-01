# K34 · Kampfsystem IV – Kampf-KI

| Feld | Wert |
|---|---|
| Dokument | Kapitel 34 von 68 · Combat Guide, Teil VII |
| Version | 1.0 |
| Owner | Lead AI Programmer |
| Mitwirkende | Lead Combat Designer, Creature Design Lead (Temperamente/Merkmale), Narrative (Rivale, Arenameister), Balancing Analyst, Online-Programmierer (Server-KI im Koop) |
| Baut auf | K16 (Verhaltensmerkmale, `BehaviorTraits.csv`), K18 (Temperamente), K31–K33 (Zeitleiste, Schaden, Formation, Harmonie, Kombos), CANON §16 (Schwierigkeitsgrade), §51 (Arena-Feldregeln), DR-07, DR-09, DR-14 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/Combat/AIProfiles.csv` (11 Profile), `tools/ref/aethris_ai.py` (Referenz-Utility-KI + Simulation mit echten Lernsets) |
| Neue Kanon-Einträge | CANON §124 (KI-Architektur & Betrachtungen), §125 (Profile & Persönlichkeit), §126 (Schwierigkeit & Fairness), §127 (Arenameister- und Boss-Taktiken) |

---

## Inhalt

1. [Ziele der Kampf-KI](#1-ziele-der-kampf-ki)
2. [Architektur: Utility statt Baum](#2-architektur-utility-statt-baum)
3. [Betrachtungen (Considerations)](#3-betrachtungen-considerations)
4. [Profile](#4-profile)
5. [Wildechos: Instinkt, Temperament, Merkmale](#5-wildechos-instinkt-temperament-merkmale)
6. [Wärter: Kampfset-Bau, Wechsel, Crescendo](#6-wärter-kampfset-bau-wechsel-crescendo)
7. [Arenameister und Rivale](#7-arenameister-und-rivale)
8. [Schwierigkeitsgrade](#8-schwierigkeitsgrade)
9. [Fairness und Wissensstand](#9-fairness-und-wissensstand)
10. [Simulation](#10-simulation)
11. [Code](#11-code)
12. [Tests, Debugging, Telemetrie](#12-tests-debugging-telemetrie)
13. [Decision Records](#13-decision-records)
14. [Kanon-Änderungen](#14-kanon-änderungen)
15. [Kapitel-Checkliste](#15-kapitel-checkliste)

---

## 1. Ziele der Kampf-KI

| Ziel | Messgröße |
|---|---|
| **Glaubwürdig** – ein scheues Echo verhält sich scheu, ein Arenameister wie ein Meister | Playtest-Frage „Wirkte der Gegner wie ein Lebewesen/eine Person?“ ≥ 4/5 |
| **Lesbar** – Spieler verstehen im Nachhinein, warum der Gegner so handelte | Kampfprotokoll mit „Absicht“-Kurztext (Erklärmodus) |
| **Fair** – keine verdeckten Vorteile, kein Lesen der Spielereingabe, kein Würfel-Betrug | Fairness-Regeln §9, automatisierte Prüfung |
| **Skalierbar** – drei Schwierigkeitsgrade ohne neue Inhalte | Siegquoten-Bänder §8 |
| **Deterministisch** – reproduzierbar für Replays, Koop und Tests | KI nutzt nur Kampf-RNG (`Fork(5)`) |
| **Schnell** – Entscheidung < 2 ms auf Switch 2 (Trio, 4 Fähigkeiten × 3 Ziele × Wechsel) | Profiling-Budget K65 |

---

## 2. Architektur: Utility statt Baum

Die Kampf-KI ist eine **Utility-KI**: Für jede legale Aktion (Fähigkeit × Ziel, Stellungswechsel, Reserve-Wechsel, Crescendo, Item, Flucht) wird ein **Nutzwert** berechnet; gewählt wird die beste Aktion – je nach Profil mit Rauschen. Die Bewertung ist **je Zeiteinheit** normiert, weil Zeit die Ressource der Zeitleiste ist.

```
                ┌──────────────────────┐
 Kampfzustand ─►│  Aktionsgenerator     │  alle legalen Aktionen (Formation, Status, Verstummt …)
                └─────────┬────────────┘
                          ▼
                ┌──────────────────────┐   Gewichte aus AIProfiles.csv
                │  Betrachtungen (12)   │◄──────────────────────────────
                │  Schaden, Kill, Status, Stufen, Heilung, Tempo, Kombo, …
                └─────────┬────────────┘
                          ▼
                ┌──────────────────────┐
                │  Nutzwert / Verzögerung│  ← Zeitleiste (K31): Wert pro 100 Ticks
                └─────────┬────────────┘
                          ▼
                ┌──────────────────────┐   Rauschen (Profil) · Lookahead (Ankündigungen)
                │  Auswahl              │──► Absicht (Kurztext fürs Protokoll)
                └──────────────────────┘
```

**Warum Utility?** Ein Verhaltensbaum müsste jede Kombination aus 330 Fähigkeiten, 15 Typen, Formation und Status ausformulieren. Utility-Bewertung skaliert mit den Daten (DR-25): Eine neue Fähigkeit wird über ihre Effekte automatisch richtig eingeschätzt. **StateTrees** (K53) steuern dagegen das Verhalten *außerhalb* des Kampfes (Annähern, Flucht in der Welt, Herden) – die Schnittstelle ist das Ereignis „Kampf beginnt/endet“.

---

## 3. Betrachtungen (Considerations)

| # | Betrachtung | Formel (vereinfacht) | Profil-Gewicht |
|---|---|---|---|
| 1 | Schaden | erwarteter Schaden / aktuelle Ziel-HP × 100 (gedeckelt 100) | Damage |
| 2 | Kill | +Bonus, wenn erwarteter Schaden ≥ Ziel-HP | Kill |
| 3 | Status | Statuswert × Chance, wenn Ziel keinen Haupt-Status hat (Gift: freie Stapel) | Status |
| 4 | Stärkung (Setup) | +12 je eigener positiver Stufe × HP-Anteil (keine Stärkung bei niedrigen HP) | Setup |
| 5 | Schwächung | +8 je gegnerischer negativer Stufe | Debuff |
| 6 | Heilung/Schild | fehlender HP-Anteil × 60 bzw. Schildwert | Heal |
| 7 | Tempo | Delay × 0,25, Haste × 0,15; ×2 gegen Ankündigungen (Lookahead) | Tempo |
| 8 | Kombo | +Kombo-Bonus, wenn ein gültiger Anklang am Ziel liegt (K33) | Combo |
| 9 | Wechsel | Matchup-Differenz Reserve vs. aktiv (Typ, HP, Status) − Wechselkosten | Switch |
| 10 | Crescendo | Budget × Situation (Gegner-HP-Summe, eigene Not) ab Harmonie ≥ Kosten | Crescendo |
| 11 | Formation | Kontakt-Erreichbarkeit, Hinterreihen-Schutz, Spott | (in 1/5) |
| 12 | Risiko | Eigener erwarteter Schaden bis zum nächsten Zug (Lookahead) – senkt Wert riskanter Aufladungen | Lookahead |

**Normierung:** `Nutzwert = Σ Gewicht × Betrachtung / Verzögerung(Zeitkosten, GES) × 100`. Eine Fähigkeit mit doppeltem Effekt, aber doppelter Zeit, ist damit gleich gut – die KI „versteht“ die Zeitleiste.

**Beispiel** (aus `aethris_ai.explain()`, Profil Taktiker):

Torgrath (Lv. 40, HP 191) gegen Zephyrion (HP 152); Profil Taktiker

| Fähigkeit | erw. Schaden | % Ziel-HP | Zeitkosten | Verzögerung | Nutzwert/100 Ticks |
|---|---|---|---|---|---|
| Felsrammen | 41 | 27 % | 80 | 89 | 35,8 |
| Schwerefaust | 28 | 18 % | 60 | 67 | 27,5 |
| Umkehrfeld | 0 | 0 % | 50 | 55 | 0,0 |
| Kieselwurf | 28 | 18 % | 60 | 67 | 27,5 |

Torgrath wählt *Felsrammen*: nicht der höchste Rohschaden je Treffer, sondern der beste Wert pro Zeit und mit Erschüttert-Chance.

---

## 4. Profile

| DisplayName | Damage | Kill | Status | Setup | Debuff | Heal | Tempo | Combo | Switch | Crescendo | NoisePermille | Lookahead | KitQuality | Knowledge | UsedBy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wild-Instinkt | 1000 | 500 | 500 | 300 | 300 | 600 | 300 | 0 | 0 | 800 | 300 | 0 | Learnset | Sichtbar | Wildechos (Standard) |
| Scheu | 600 | 300 | 800 | 200 | 600 | 1200 | 800 | 0 | 0 | 600 | 250 | 0 | Learnset | Sichtbar | Wildechos mit Merkmal Shy (Flucht bei HP < 50 %) |
| Angriffslustig | 1300 | 900 | 300 | 500 | 200 | 300 | 200 | 0 | 0 | 1000 | 200 | 0 | Learnset | Sichtbar | Wildechos mit Aggressive/Territorial (keine Flucht) |
| Verspielt | 700 | 400 | 1000 | 600 | 800 | 500 | 1000 | 0 | 0 | 700 | 350 | 0 | Learnset | Sichtbar | Wildechos mit Playful/Curious |
| Alpha | 1100 | 800 | 900 | 800 | 800 | 900 | 900 | 500 | 0 | 1000 | 50 | 1 | Best | Sichtbar | Alpha-Echos (K52) |
| Anfänger | 1000 | 300 | 200 | 0 | 0 | 200 | 0 | 0 | 200 | 500 | 150 | 0 | Learnset | Sichtbar | Wärter Stufe 1–2 (Akt I früh) |
| Geübt | 1000 | 600 | 1000 | 800 | 800 | 1000 | 1000 | 600 | 700 | 900 | 50 | 1 | Best | Sichtbar | Wärter Akt I–II |
| Veteran | 1000 | 800 | 1200 | 1000 | 1000 | 1200 | 1200 | 1000 | 1000 | 1000 | 0 | 1 | Best | Kodex2 | Wärter Akt III und Endgame |
| Arenameister | 1000 | 800 | 1200 | 1000 | 1000 | 1200 | 1200 | 1200 | 1000 | 1200 | 0 | 1 | Signature | Kodex2 | Arenameister (mit Signatur-Taktik) |
| Rivale (adaptiv) | 1000 | 700 | 1000 | 900 | 900 | 1000 | 1000 | 900 | 900 | 1000 | 30 | 1 | Best | Kodex2 | Kael Duran (passt Profil an Spielerverlauf an) |
| Boss | 1000 | 600 | 1200 | 1000 | 1000 | 1000 | 1200 | 1200 | 0 | 1300 | 0 | 1 | Script | Voll | Bosse/Raids (Phasenskripte K35) |

**Rauschen** ist bewusst Teil des Profils: Wildechos (30 %) sollen *lebendig*, nicht optimal wirken; Veteranen und Arenameister handeln rauschfrei. Rauschen wählt immer eine **legale, sinnvolle** Aktion (keine Heilung bei vollen HP, kein Status auf immune Ziele) – „Zufall“ heißt nicht „dumm“.

---

## 5. Wildechos: Instinkt, Temperament, Merkmale

Wildechos nutzen `AI_WILD` als Basis; Verhaltensmerkmale (K16, `BehaviorTraits.csv`) und Temperamente (K18) **modulieren** die Gewichte. Damit passt das Kampfverhalten zum beobachtbaren Weltverhalten (DR-02, DR-04): Was man in der Welt sieht, erlebt man im Kampf.

| Merkmal / Temperament | Profil-Anpassung | Kampfverhalten |
|---|---|---|
| Shy (Scheu) | → `AI_WILD_SHY` | Flucht-Marker bei HP < 50 % (sichtbar, unterbrechbar durch Bind/Starre) |
| Aggressive, Territorial | → `AI_WILD_AGGR` | keine Flucht, Damage/Kill hoch, nutzt Crescendo früh |
| Playful, Curious | → `AI_WILD_PLAY` | Status/Tempo-lastig, „neckt“ (Delay, Stufen) |
| Pack, Herd, FamilyGroup | Combo +500 | Herden kombinieren untereinander (K33) |
| Guardian | Heal +300, Switch nicht möglich (keine Reserve) | schützt Jungtiere/Herde: Spott, Schilde |
| Ambusher | erster Zug: Hinterhalt-Bonus (DR-14, angekündigt) | stark im ersten Zug, dann normal |
| Sleepy | Startposition +200 ‰ | handelt spät, oft nur noch Flucht |
| Temperament „Hitzig“ | Damage +200, Noise +50 | – |
| Temperament „Bedacht“ | Lookahead 1, Noise −100 | reagiert auf Ankündigungen |

**Bindungsdialog:** Während einer Bindung (K36) wechselt das Wildecho in einen eigenen Modus (Beruhigen/Locken); die Kampf-KI pausiert. Erfolgloses Beruhigen kann Shy-Echos zur Flucht treiben – das ist K36s Spannungsbogen.

---

## 6. Wärter: Kampfset-Bau, Wechsel, Crescendo

### 6.1 Kampfset-Bau (`KitQuality`)

| Stufe | Regel | Einsatz |
|---|---|---|
| `Learnset` | die 4 zuletzt gelernten Fähigkeiten | Wildechos, Anfänger |
| `Best` | stärkste Primärtyp-Schadensfähigkeit (Kategorie nach ANG/SAN) · stärkste Fremd-/Sekundärtyp-Schadensfähigkeit · beste Status/Hilfe · nächststärkste Schadensfähigkeit; Passive mit bestem Matchup; Klangschriften/Tutoren laut NPC-Daten | Wärter ab Akt I Mitte |
| `Signature` | wie `Best`, aber feste Signatur-Sets aus NPC-Daten (K53) | Arenameister, Rivale, Fraktionsführer |
| `Script` | Phasenskripte | Bosse (K35) |

Der `Best`-Algorithmus ist identisch in Python (`aethris_ai.kit`) und C++ (`UCombatKitBuilder`) und wird für **alle generierten NPC-Teams** genutzt; Design-Hand nur für Signatur-Wärter.

### 6.2 Wechsel

```
MatchupScore(E, Gegner) = Σ_Gegner [ bester eigener Typfaktor gegen G − bester Typfaktor von G gegen E ]
                          + HP-Anteil × 50 − Status-Malus
Wechsel, wenn  MatchupScore(Reserve) − MatchupScore(aktiv) > 120 × (1000 / Switch-Gewicht)
           und  aktives Echo nicht unmittelbar vor einem Kill steht
```

Wechsel-Hysterese: Nach einem Wechsel kein erneuter Wechsel desselben Platzes für 2 eigene Züge (verhindert Ping-Pong).

### 6.3 Crescendo

Crescendo wird gewählt, wenn Harmonie ≥ Kosten **und** (a) die erwartete Wirkung ≥ 35 % der gegnerischen HP-Summe beträgt, **oder** (b) die eigene Seite in Not ist (≤ 2 Echos, Ø HP < 40 %), **oder** (c) der Gegner eine eigene Ankündigung platziert hat (Konter-Crescendo, Lookahead 1). Die KI hält Harmonie nie > 2 eigene Runden auf 100 („verschenkte Harmonie“).

### 6.4 Formation (Duo/Trio)

Startformation: höchste VER/SVE-Summe und Tank-Rolle vorn, Caster/Support hinten (mind. 1 vorn). Stellungswechsel, wenn ein Hinterreihen-Echo Kontakt-Fähigkeiten als beste Option hätte oder ein Vorderreihen-Echo < 25 % HP hat und ein Tank verfügbar ist.

---

## 7. Arenameister und Rivale

Arenameister nutzen `AI_ARENA` und eine **Signatur-Taktik**, die ihre Arena-Feldregel (CANON §51) lehrt. Die Taktik ist kein Skript, sondern ein Gewichts-Overlay plus Startaktion.

| Arena | Meister | Feldregel | Signatur-Taktik |
|---|---|---|---|
| ARN_01 Eichenhall | Maelis Wendt | Überwuchs | Heilt über Terrain, hält Gegner mit Dornenranke fest; erstes Crescendo „Urwaldchor“ |
| ARN_02 Kharsholm | Torvik Hrall | Wandernde Plattformen (Reihentausch alle 4 Runden) | Plant den Tausch ein: stellt Tanks so, dass sie nach dem Tausch vorn stehen; Erdsog-Kombo |
| ARN_03 Morvenfurt | Evhe Corrach | Moornebel (AUS +1, Hinterreihe nur per Fläche; nachts) | Hält Caster hinten, nutzt Flächen-Gift (Miasma) und Giftblüte-Kombo |
| ARN_04 Qasr Sahrun | Shirah Harrâd | Sonnenspiegel (Licht trifft 2. Ziel mit 60 %) | Licht-Fähigkeiten auf das Ziel mit den meisten Nachbarn; Blendschein vor Strahlenkranz |
| ARN_05 Schlackenwehr | Kaldrex Vorn | Schmiedeglut (Glutboden, 3 % Max-HP je Runde Vorderreihe) | Ambross als Anker vorn, Weißglut-Kombo, zwingt Gegner zum Rückzug in die Hinterreihe |
| ARN_06 Saltrand-Hafen | Beke Tamsen | Gezeitenbecken (Ebbe/Flut alle 3 Runden) | Push/Pull im Gezeitenrhythmus, Dampfstoß- und Sturmflut-Kombos zur Flut-Phase |
| ARN_07 Hvitmark | Sigrun Fjall | Spiegeleis (Wechsel −50 % Zeit, Rückstoß ×2) | Häufige Wechsel, Rückstoß-Ketten; Verzögerung bis an den Deckel, Snevrik-Vorgriffe |
| ARN_08 Dorunsruh | Aevrin Thal | Glyphenfeld (Typtabelle alle 5 Runden 1 Runde umgekehrt) | Plant Schläge in die Umkehr-Runde; Wandlungsglyphe auf den Gegner davor |
| ARN_09 Prismara | Ilyx Brannoc | Lichtbrechung (25 % Brechung auf anderes Ziel) | Reflexion und Aufladung; Gebrochen gegen Schilde; Flächen statt Einzelziele |
| ARN_10 Aerion | Oruma Siyel | Sternenfall (alle 4 Runden Treffer + 15 Harmonie) | Harmonie-Wettlauf, zwei Crescendos, Formation verteilt gegen Sternenfall |

Feldregeln laut CANON §51 (`Data/World/Arenas.csv`); „Züge“ der Arena-Regeln gelten als Runden (CANON §109).

**Rivale Kael Duran (`AI_RIVAL`, adaptiv):** Kael passt sein Profil zwischen den Begegnungen an den Spieler an (Telemetrie des Spielstands, keine Online-Daten): Hat der Spieler gegen Kael zuletzt mit Status gewonnen, nimmt Kael ein Licht-Echo mit Reinigen; hat der Spieler mit Tempo gewonnen, setzt Kael auf Frost. Adaptivität ist auf **eine** Anpassung je Begegnung begrenzt und wird im Dialog angedeutet („Diesmal bin ich vorbereitet“). Nach seiner Umkehr (Akt III) kämpft Kael als Koop-Partner mit demselben Profil.

---

## 8. Schwierigkeitsgrade

Die drei Grade (CANON §16) skalieren mehrere Hebel gleichzeitig – nicht nur Werte:

| Hebel | Entspannt | Wärter (Standard) | Meister |
|---|---|---|---|
| Profil Wärter | Anfänger (Rauschen 150 ‰) | Geübt | Veteran |
| Profil Arenameister | Geübt + Signatur | Arenameister | Arenameister + Lookahead 2 |
| Kampfset | Learnset | Best | Best + Klangschriften |
| Anlagen NPC | 5 | 9 | 13 |
| Schliff NPC | 0 | 40 % des Levels | 80 % |
| Wechsel | aus | an | an, aggressiver (Switch 1300) |
| Kombos der KI | aus | an | an |
| Informationsstand | Sichtbar | Sichtbar | Kodex2 |
| Spielerhilfen | Effektivität immer sichtbar, Erklärmodus, EP ×1,25 | Effektivität ab Kodex 2 | keine Zusatzhilfen; Rückklang-Strafe Sol |

**Zielbänder** (Siegquote erfahrener Testspieler beim ersten Versuch): Arena Entspannt ≥ 90 %, Wärter 65–80 %, Meister 35–55 %. K63 kalibriert die Bänder mit Playtest-Daten.

---

## 9. Fairness und Wissensstand

| Regel | Inhalt |
|---|---|
| F-1 Kein Eingabelesen | Die KI entscheidet, bevor der Spieler seine Wahl für denselben Tick trifft (simultane Planung, K31 §9); sie kennt die Spielerwahl nie im Voraus |
| F-2 Kein Würfelbetrug | Die KI nutzt dieselben Formeln und denselben RNG-Strom; sie „weiß“ nicht, ob ein Wurf gelingt |
| F-3 Wissensstand | `Sichtbar`: alles, was der Spieler auf dem Bildschirm sieht (Typen, HP-Balken, Status, Zeitleiste). `Kodex2`: zusätzlich Fähigkeits- und Passivlisten der Arten (wie ein Spieler mit Kodex-Stufe 2). `Voll`: nur Bosse (Skript) |
| F-4 Keine Werte-Boni für die KI | außer über die Hebel der Tabelle §8 (Anlagen, Schliff, Kampfset), die für Spieler gleichermaßen erreichbar sind |
| F-5 Erklärbarkeit | Jede KI-Aktion schreibt eine Absicht ins Kampfprotokoll („Uvlet will deinen Angriff verzögern“) |

---

## 10. Simulation

`aethris_ai.matrix()` lässt die Profile in 1v1-Duellen gegeneinander antreten (Lv. 30, 150 zufällige Artenpaare, je **gespiegelt**, um Artvorteile auszugleichen; Kampfsets nach §6.1 `Best` aus den echten Lernsets):

| Profil ↓ gegen → | Zufall | Gierig | Taktiker | Meister |
|---|---|---|---|---|
| **Zufall** | 47 % | 38 % | 36 % | 37 % |
| **Gierig** | 64 % | 49 % | 49 % | 47 % |
| **Taktiker** | 62 % | 52 % | 48 % | 49 % |
| **Meister** | 59 % | 50 % | 50 % | 48 % |

**Interpretation:**
- Gegenüber zufälliger Aktionswahl gewinnt jede bewertende KI etwa 60–65 % – **gute Entscheidungen zählen**, aber sie entscheiden ein 1v1 nicht allein (Typen und Arten wiegen mehr).
- Zwischen Gierig, Taktiker und Meister liegen im reinen 1v1 nur wenige Prozentpunkte. Der Unterschied der höheren Profile entsteht in **Duo/Trio** (Kombos, Formation, Wechsel, Crescendo-Timing) – genau dort, wo die Schwierigkeitsgrade ihre Hebel ansetzen (§8).
- Folgerung für das Design: Schwierigkeit wird **mehrdimensional** skaliert, nicht nur über das KI-Profil. Das bestätigt ADR-123.

---

## 11. Code

```cpp
// GF_Combat – Utility-KI
USTRUCT() struct FAIProfileRow : public FTableRowBase
{
    GENERATED_BODY()
    UPROPERTY() int32 Damage = 1000, Kill = 0, Status = 0, Setup = 0, Debuff = 0, Heal = 0, Tempo = 0;
    UPROPERTY() int32 Combo = 0, Switch = 0, Crescendo = 0, NoisePermille = 0, Lookahead = 0;
};

struct FScoredAction { FCombatChoice Choice; int64 ScoreMilli = 0; FText Intent; };

FCombatChoice UCombatBrain::Decide(const FCombatView& View, const FAIProfileRow& P, FAethrisRandom& Rng) const
{
    TArray<FScoredAction> Options;
    Generator.Enumerate(View, Options);                               // legale Aktionen (Formation, Verstummt …)
    for (FScoredAction& O : Options)
    {
        int64 V = 0;
        for (const IConsideration* C : Considerations) V += int64(C->Weight(P)) * C->Evaluate(View, O.Choice) / 1000;
        if (P.Lookahead > 0) V -= Risk.Evaluate(View, O.Choice);      // Ankündigungen, Kill-Gefahr
        O.ScoreMilli = V * 100000 / Aethris::Timeline::Delay(O.Choice.TimeCost(), View.Self().SpeedEff);
    }
    if (Rng.ChancePermille(P.NoisePermille)) return Options[Rng.NextBounded(Options.Num())].Choice;   // legal & sinnvoll
    Options.StableSort([](const FScoredAction& A, const FScoredAction& B) { return A.ScoreMilli > B.ScoreMilli; });
    return Options[0].Choice;                                          // Gleichstand: Datenreihenfolge (deterministisch)
}
```

- **Ausführungsort:** Solo lokal; Koop und PvP-Bots auf dem Host/Server (DR-21).
- **Budget:** ~40 Aktionen × 12 Betrachtungen; < 2 ms auf Switch 2 (Messung K65).
- **Debug-Ansicht:** `aethris.ai.debug 1` blendet je Aktion die Betrachtungswerte ein (Gameplay Debugger-Kategorie „Combat AI“).

---

## 12. Tests, Debugging, Telemetrie

| Test | Inhalt |
|---|---|
| `Aethris.Unit.AI.Legal` | Nie illegale Aktionen (Kontakt aus Hinterreihe, Status bei Verstummt) |
| `…AI.Sensible` | Keine Heilung bei vollen HP, kein Status auf immune Ziele, kein Setup bei < 25 % HP |
| `…AI.PythonParity` | 5.000 Entscheidungen gegen `aethris_ai.py` |
| `…AI.Fairness` | KI-Entscheidung unabhängig von noch nicht bestätigter Spielerwahl (F-1) |
| `Aethris.Func.AI.Matrix` | Nightly: Siegquoten-Matrix; Alarm, wenn Taktiker < Gierig − 5 pp |

**Telemetrie:** Absichten je KI-Aktion, Anteil Rausch-Aktionen, Wechsel je Kampf, Crescendo-Zeitpunkt (Harmonie-Wartezeit), Kombos der KI. Ziel: Spieler sollen in ≥ 70 % der Arena-Niederlagen im Protokoll eine erkennbare Ursache finden (Umfrage K66).

---

## 13. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-122 | Utility-KI mit Nutzwert je Zeiteinheit | skaliert mit Daten, versteht Zeitleiste | Verhaltensbäume je Gegner (unwartbar), Monte-Carlo-Suche (Budget Switch 2) |
| ADR-123 | Schwierigkeit über mehrere Hebel (Profil, Kampfset, Anlagen, Schliff, Wechsel, Info) | Simulation zeigt: Profil allein bewegt 1v1 nur wenige pp | Nur Werte-Skalierung (unfair, „Schwamm-Gegner“) |
| ADR-124 | Wild-KI aus Merkmalen/Temperament moduliert | Welt- und Kampfverhalten konsistent (DR-02/DR-04) | Einheitliche Wild-KI |
| ADR-125 | Fairness-Regeln F-1 bis F-5 | Vertrauen, Ranked-Integrität, Erklärbarkeit | „Cheating AI“ auf hohen Graden |
| ADR-126 | Adaptiver Rivale (1 Anpassung je Begegnung) | Erzählerische Rivalität ohne Frust | Voll adaptive Gummiband-KI |

---

## 14. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §124 | Utility-KI: Aktionsgenerator → 12 Betrachtungen → Nutzwert / Verzögerung × 100 → Auswahl mit Profil-Rauschen; StateTree außerhalb des Kampfes; Entscheidung < 2 ms; Kampf-RNG | LOCKED |
| §125 | 11 Profile (`AIProfiles.csv`); Wild-Profile moduliert durch Merkmale/Temperament (Shy flieht < 50 % HP, Aggressive/Territorial nie); Kampfset-Bau Learnset/Best/Signature/Script; Wechsel-Hysterese 2 Züge; Crescendo-Regeln (a)–(c) | LOCKED |
| §126 | Schwierigkeitsgrade skalieren Profil, Kampfset, Anlagen (5/9/13), Schliff (0/40/80 % des Levels), Wechsel, KI-Kombos, Wissensstand; Zielbänder Arena 90/65–80/35–55 %; Fairness F-1…F-5 | LOCKED (Bänder → K63) |
| §127 | Signatur-Taktiken der 10 Arenameister (Gewichts-Overlay + Startaktion); adaptiver Rivale (1 Anpassung je Begegnung) | LOCKED |
| §10 | ADR-122 – ADR-126 | LOCKED |

---

## 15. Kapitel-Checkliste

- [x] KI-Ziele, Architektur (Utility), 12 Betrachtungen
- [x] 11 KI-Profile als Daten
- [x] Wild-KI aus Merkmalen und Temperamenten
- [x] Wärter: Kampfset-Bau, Wechsel, Crescendo, Formation
- [x] Arenameister-Signaturtaktiken, adaptiver Rivale
- [x] Schwierigkeitsgrade mehrdimensional, Fairness-Regeln
- [x] Referenz-KI in Python mit echten Lernsets, Siegquoten-Matrix
- [x] Code, Tests, Debugging, Telemetrie
- [x] ADR-122 – ADR-126, CANON §124–§127

➡️ **Nächstes Kapitel: K35 – Kampfsystem V: Bosse, Raids und Tiefenresonanz-Kämpfe.**
