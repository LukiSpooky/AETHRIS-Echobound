# K18 · Statuswerte, Persönlichkeit, Temperament, Wachstumsraten

| Feld | Wert |
|---|---|
| Dokument | Kapitel 18 von 68 · Monster Bible, Teil II |
| Version | 1.0 |
| Owner | RPG Systems Designer |
| Mitwirkende | Combat Designer, Economy Designer (EP-Ökonomie), AI Engineer (Temperament-KI), Animation Lead (Persönlichkeits-Idles), Lead Gameplay Programmer |
| Baut auf | CANON §5 (8 Statuswerte, Persönlichkeit, Temperament, Wachstumsrate), §18 (Schliff, Chor-Lernen), §29 (FEchoStats, GAS-Regeln), §71 (Basiswert-Spannen), DR-07 |
| Status | ✅ Freigegeben |
| Im Repository | `tools/ref/aethris_stats.py` (Referenz), `Source/AethrisCore/Public/Echo/EchoStatCalculator.h` (constexpr, mit static_asserts), `Data/Echos/GrowthRates.csv`, `Personalities.csv`, `Temperaments.csv`, `Data/Combat/StatStages.csv` |
| Neue Kanon-Einträge | CANON §79 (Statusformeln & Stufen), §80 (Anlagen & Schliff), §81 (Persönlichkeiten), §82 (Temperamente), §83 (Wachstumsraten & EP) |

---

## Inhalt

1. [Die acht Statuswerte](#1-die-acht-statuswerte)
2. [Formeln](#2-formeln)
3. [Kampfstufen, Präzision & Ausweichen](#3-kampfstufen-präzision--ausweichen)
4. [Persönlichkeit](#4-persönlichkeit)
5. [Temperament](#5-temperament)
6. [Wachstumsraten & Erfahrung](#6-wachstumsraten--erfahrung)
7. [Anlagen (Genetik der Werte)](#7-anlagen-genetik-der-werte)
8. [Schliff (Training)](#8-schliff-training)
9. [Darstellung im UI](#9-darstellung-im-ui)
10. [Code & Tests](#10-code--tests)
11. [Decision Records](#11-decision-records)
12. [Kanon-Updates](#12-kanon-updates)
13. [Kapitel-Checkliste](#13-kapitel-checkliste)

---

## 1. Die acht Statuswerte

| Wert | Kürzel | Wirkung im Kampf | Wirkung außerhalb |
|---|---|---|---|
| **HP** | HP | Lebenspunkte; 0 = erschöpft | – |
| **Angriff** | ANG | Physische Fähigkeiten (Nah-/Kontaktangriffe) | Feldfähigkeiten „Kraft“ (Felsen bewegen) |
| **Verteidigung** | VER | Mindert physischen Schaden | – |
| **Spezialangriff** | SAN | Klang-/Energie-Fähigkeiten (Fernwirkung) | Feldfähigkeiten „Wirkung“ (Pflanzen wachsen lassen) |
| **Spezialverteidigung** | SVE | Mindert Spezialschaden; Statusresistenz (+) | – |
| **Geschwindigkeit** | GES | **Zeitleiste**: Zeitkosten jeder Aktion (K31) | Reittiere: Tempo-Bonus ±10 % |
| **Präzision** | PRÄ | Trefferchance (§3.3), Kritischer-Treffer-Chance (K32) | Fotografie: Ruhig halten |
| **Ausweichen** | AUS | Gegnerische Trefferchance | Bindung: schwieriger zu treffende Anschläge (Unruhe, K36) |

**Kernsumme** = HP + ANG + VER + SAN + SVE + GES (Basiswerte). PRÄ/AUS sind Sekundärwerte (Basis 80–120, ADR-078).

---

## 2. Formeln

### 2.1 Variablen

| Symbol | Bedeutung | Bereich |
|---|---|---|
| B | Basiswert der Art | 25–160 (Kern), 80–120 (PRÄ/AUS) |
| L | Level | 1–100 |
| A | **Anlage** (genetisch, §7) | 0–15 je Wert |
| S | **Schliff** (Training, §8) | 0–80 je Wert, Summe ≤ 240 |
| P | Persönlichkeitsfaktor | 1100 für den Persönlichkeits-Wert, sonst 1000 (‰) |

### 2.2 Formeln (LOCKED, ganzzahlig, `⌊ ⌋` = abrunden)

```
 HP        = ⌊ B · (L + 10) · (1000 + 10·A) / 40000 ⌋ + L + 12 + S

 Kernwert  = ⌊ ⌊ B · (L + 10) · (1000 + 10·A) / 55000 ⌋ · P / 1000 ⌋ + ⌊ S / 2 ⌋

 PRÄ / AUS = B + ⌊ A / 3 ⌋ (+ 5, falls Persönlichkeits-Wert)          ← levelunabhängig
```

**Designbegründung:**
- **Linear in (L + 10)**: Werte wachsen gleichmäßig; Level-1-Echos sind nicht völlig wehrlos (Offset +10).
- **Anlage als Prozent (bis +15 %)** statt flacher Punkte: Wirkt auf allen Levels proportional gleich – ein Echo mit guten Anlagen ist früh wie spät „spürbar“ besser, aber nie dominant.
- **Schliff flach**: Training lohnt sich besonders in frühen Levels und für spezialisierte Builds.
- **PRÄ/AUS levelunabhängig**: Trefferquoten bleiben über das ganze Spiel lesbar (DR-07: gedeckelte Varianz).

### 2.3 Beispielwerte

Fernlit (Basis 48/42/50/55/58/47, Anlage 7, ohne Schliff):

| Level | HP | ANG | VER | SAN | SVE | GES |
|---|---|---|---|---|---|---|
| 5 (Erstresonanz) | 36 | 12 | 14 | 16 | 16 | 13 |
| 16 (Evolution) | 61 | 21 | 25 | 27 | 29 | 23 |
| 50 | 139 | 49 | 58 | 64 | 67 | 54 |

**Grenzwerte:** Kernwert-Maximum (B 140, L 100, A 15, S 80, Persönlichkeit) = **394**; HP-Maximum (B 160, L 100, A 15, S 80) = **698**.

### 2.4 Paritätsprüfung

`Source/AethrisCore/Public/Echo/EchoStatCalculator.h` enthält die Formeln als `constexpr` mit `static_assert`s gegen Werte aus `tools/ref/aethris_stats.py` – eine Formeländerung, die nicht in beiden Implementierungen erfolgt, **kompiliert nicht**.

---

## 3. Kampfstufen, Präzision & Ausweichen

### 3.1 Stufen (Buffs/Debuffs)

Daten: `Data/Combat/StatStages.csv`. Stufen −4 … +4 (CANON §29 GAS-02).

| Stufe | −4 | −3 | −2 | −1 | 0 | +1 | +2 | +3 | +4 |
|---|---|---|---|---|---|---|---|---|---|
| Kernwerte (ANG, VER, SAN, SVE, GES) | ×0,50 | ×0,571 | ×0,667 | ×0,80 | ×1 | ×1,25 | ×1,50 | ×1,75 | ×2,00 |
| PRÄ / AUS | ×0,70 | ×0,775 | ×0,85 | ×0,925 | ×1 | ×1,075 | ×1,15 | ×1,225 | ×1,30 |

Regeln: Stufen sind pro Kampf und Echo; Wechsel in die Reserve setzt Stufen zurück (Ausnahme: Passive, K28). HP hat keine Stufen. Stufen werden auf der Echo-Karte des Kampf-UI als Pfeile angezeigt (DR-06).

### 3.2 Geschwindigkeit & Zeitleiste

GES bestimmt die Zeitkosten jeder Aktion (Formel K31; Vorgabe aus K05 §10: `Delay = Kosten × 200 / (GES + 100)`). Eine GES-Stufe +1 verkürzt Zeitkosten spürbar, aber nicht linear (abnehmender Ertrag durch +100 im Nenner) – verhindert „Doppelzug-Spiralen“.

### 3.3 Trefferchance (Vorgabe für K32)

```
 Treffer (‰) = clamp( Fähigkeitsgenauigkeit (‰) × PRÄ_eff / AUS_eff , 500 , 1000 )
 PRÄ_eff = PRÄ × Stufenfaktor(PRÄ-Stufe) · AUS_eff analog
```

| Beispiel | Ergebnis |
|---|---|
| Genauigkeit 95 %, PRÄ 100 vs. AUS 100 | 95,0 % |
| Genauigkeit 95 %, PRÄ 100 vs. AUS 120 | 79,1 % |
| Genauigkeit 80 %, PRÄ 90 vs. AUS 120 (+4 Stufen) | 50,0 % (Untergrenze) |

**DR-07-Konformität:** Untergrenze 50 % (kein Fähigkeitsspam durch Ausweichen), Obergrenze 100 %. Fehlschläge erzeugen Harmonie (DR-10, K33). Fähigkeiten mit „sicherem Treffer“ ignorieren die Formel.

---

## 4. Persönlichkeit

Daten: `Data/Echos/Personalities.csv`. **16 Persönlichkeiten**; jedes Echo hat genau eine (zufällig beim Wildvorkommen, erblich in der Zucht, K38).

| Tag | Name | Wert-Bonus | Lieblingsinteraktion | Begleiter-Idle | Kampf-KI-Neigung (wild/NPC) |
|---|---|---|---|---|---|
| `Personality.Brave` | Mutig | ANG +10 % | Training | läuft voraus, schaut zurück | direkte Angriffe |
| `Personality.Wild` | Wild | ANG +10 % | Spielen | jagt Blätter | schwächstes Ziel |
| `Personality.Steadfast` | Standhaft | VER +10 % | Training | bleibt dicht beim Wärter | schützt Verbündete |
| `Personality.Serene` | Gelassen | VER +10 % | Streicheln | setzt sich, beobachtet | wartet auf Konter |
| `Personality.Clever` | Klug | SAN +10 % | Loben | untersucht Gegenstände | nutzt Typvorteile |
| `Personality.Dreamy` | Träumerisch | SAN +10 % | Streicheln | schaut in den Himmel | spart Harmonie |
| `Personality.Gentle` | Sanft | SVE +10 % | Füttern | schmiegt sich an | heilt früh |
| `Personality.Patient` | Geduldig | SVE +10 % | Füttern | liegt im Schatten | spielt auf Zeit |
| `Personality.Nimble` | Flink | GES +10 % | Spielen | rennt im Kreis | handelt häufig |
| `Personality.Restless` | Rastlos | GES +10 % | Training | springt auf Erhöhungen | wechselt Position |
| `Personality.Tough` | Zäh | HP +10 % | Füttern | wälzt sich im Gras | bleibt vorne |
| `Personality.Kind` | Gutmütig | HP +10 % | Streicheln | folgt im Schritt | stärkt Verbündete |
| `Personality.Keen` | Scharfsichtig | PRÄ +5 | Loben | späht Ressourcen aus | zielt auf Ausweichende |
| `Personality.Diligent` | Gewissenhaft | PRÄ +5 | Training | sortiert Steinchen | sichere Fähigkeiten |
| `Personality.Playful` | Verspielt | AUS +5 | Spielen | versteckt sich | weicht aus, neckt |
| `Personality.Sly` | Listig | AUS +5 | Loben | schleicht, beobachtet | nutzt Status |

**Keine Abzüge (ADR-084):** Persönlichkeiten geben nur Boni. Das vermeidet „falsche Persönlichkeit = wertloses Echo“-Frust (DR-05, Persona Lina) und macht jede Persönlichkeit zu einem *Ausdrucksmittel* (Idle, Lieblingsinteraktion) statt einer Optimierungsfalle. Kompetitive Tiefe entsteht über die Wahl des Bonus-Werts.

**Ändern:** Item **Wesensklang** (seltenes Crafting-Ergebnis, K41) ändert die Persönlichkeit auf eine gewählte mit gleichem Bonus-Wert-*Paar* oder beliebig? → **beliebig**, aber teuer (Endgame-Material). Zucht bleibt der Hauptweg (DR-18).

---

## 5. Temperament

Daten: `Data/Echos/Temperaments.csv`. **5 Temperamente**; bestimmen das **Verhalten** eines Echos – besonders im Wildzustand und bei der Bindung (K36) – und eine kleine Kampfnuance.

| Tag | Name | Bindungsfenster | Max. Anschläge | Bei Fehlversuch | Wahrnehmungsradius | Harmonie-Gewinn | Flucht ab HP | Beschreibung |
|---|---|---|---|---|---|---|---|---|
| `Temperament.Calm` | Ruhig | ×1,2 | 4 | bleibt | ×0,9 | ×1,0 | 15 % | geduldig |
| `Temperament.Fiery` | Feurig | ×0,9 | 2 | **greift an** | ×1,0 | ×1,1 (beim Angreifen) | nie | hitzig |
| `Temperament.Wary` | Wachsam | ×1,0 | 2 | **flieht** | ×1,3 | ×1,0 | 35 % | misstrauisch |
| `Temperament.Curious` | Neugierig | ×1,1 | 3 | **nähert sich** | ×0,8 | ×1,0 | 10 % | lockbar |
| `Temperament.Stoic` | Stoisch | ×1,0 | 3 | bleibt | ×1,0 | ×0,95 | nie | Furcht halbiert |

**Verteilung beim Wildvorkommen:** artabhängig (Temperament-Gewichte im Bindungs-Fragment, K36); Standard 30/15/20/20/15 % (Ruhig/Feurig/Wachsam/Neugierig/Stoisch). Das Temperament ist bei **Kodex-Stufe 2** im Resonanzsinn sichtbar (Farbton der Frequenzwelle) → Wissen hilft beim Binden (DR-01).

**Im Chor:** Temperament beeinflusst Begleiter-Reaktionen (Feurig knurrt bei Gefahr, Wachsam warnt früher) und den Harmonie-Gewinn wie in der Tabelle.

---

## 6. Wachstumsraten & Erfahrung

### 6.1 Kurven (LOCKED)

Daten: `Data/Echos/GrowthRates.csv` (Gesamt-EP bis Level L).

| Kurve | Name | Formel (Gesamt-EP bis L) | L 30 | L 50 | L 70 | L 100 | Charakter |
|---|---|---|---|---|---|---|---|
| `Swift` | Schnell | 0,6 · L³ | 16.200 | 75.000 | 205.800 | 600.000 | kleine, häufige Arten |
| `Steady` | Stetig | 0,8 · L³ | 21.600 | 100.000 | 274.400 | 800.000 | Standard, Starter |
| `Late` | Spätblüher | L³ · (0,45 + 0,65·L/100) | 17.415 | 96.875 | 310.415 | 1.100.000 | früh schnell, spät teuer (Endstufen, Drachen) |
| `Wave` | Wellenförmig | L³ · (0,8 + 0,08·sin(L/6)) | 19.528 | 108.872 | 252.910 | 734.524 | schwankende Phasen (Arkan, Klang, Geist) |

Alle Kurven sind streng monoton (geprüft). Legendäre/Mythische nutzen `Late`.

### 6.2 EP-Gewinn (Struktur LOCKED, Tuning → K63)

```
 EP = ⌊ Ertrag(Art) × Ld × (2·Ld + 10) / ( (Ld + Lp + 10) × 6 ) ⌋ × Quelle × Bonus
   Ertrag(Art): Stufe 1 ≈ 60 · Stufe 2 ≈ 140 · Stufe 3 / Einzelart ≈ 210 · Legendär 320   (Spalte in Species.csv ab K20)
   Ld = Level des besiegten/gebundenen Echos, Lp = Level des empfangenden Echos
   Quelle: Kampf 1,0 · Bindung 1,2 (Bindung lohnt mehr als Erschöpfen – S2) · Trainerkampf 1,3
   Bonus: Chor-Lernen (Reserve 0,5, CANON §18), Schwierigkeit Entspannt ×1,25, Glücksbringer-Items (≤ ×1,2)
```

Die Formel belohnt das Besiegen höherleveliger Gegner überproportional und dämpft Überleveln (Ld ≪ Lp → kleiner Bruch). K63 kalibriert Ertrag und Spawnlevel, sodass die Story-Kurve (CANON §15: Finale Lv. 68–70 nach ~40 h) eingehalten wird.

### 6.3 Level-Up

Beim Level-Up: Werte neu berechnen (außerhalb des Kampfes; im Kampf erst nach Kampfende, GAS-03), Lernset prüfen (Repertoire, CANON §18), Evolution prüfen (K19), Event `Event.Echo.LevelUp`.

---

## 7. Anlagen (Genetik der Werte)

| Eigenschaft | Festlegung |
|---|---|
| Bereich | 0–15 je Wert (8 Werte inkl. PRÄ/AUS), gespeichert in `FEchoGenome::Aptitudes` |
| Wildvorkommen | Gleichverteilt 0–15 je Wert; **Seltenheitsbonus**: Rare/VeryRare garantieren 2 bzw. 3 Werte mit 15 („Resonanzbegabung“) |
| Sichtbarkeit | Kodex-Forschungs-Skill (K43): Stufen „unbekannt“ → „Bewertung in 4 Klassen“ (schwach 0–4, solide 5–9, stark 10–13, vollendet 14–15) → exakter Wert (Skill „Resonanzlesen II“) |
| Wirkung | +1 % je Punkt auf HP/Kernwerte, +1 je 3 Punkte auf PRÄ/AUS |
| Vererbung | K38 (Allel-Modell) |
| Ändern | **Klangstimmung** (Endgame-Item aus Tiefenresonanzen, K62) setzt einen Wert auf 15 – begrenzt verfügbar (DR-18: Zucht bleibt Hauptweg) |

---

## 8. Schliff (Training)

| Eigenschaft | Festlegung (finalisiert CANON §18 PROVISIONAL) |
|---|---|
| Bereich | 0–80 je Wert (nur 6 Kernwerte), **Summe ≤ 240** |
| Wirkung | HP: +S · Kernwerte: +⌊S/2⌋ (max. +40) |
| Gewinn durch Kampf | Jede besiegte/gebundene Art gibt 1–3 Schliff in ihrem „Lehrwert“ (Spalte `PolishYield` in Species.csv ab K20, Format `Stat:Punkte`) an alle beteiligten Echos |
| Gewinn durch Training | Lager-Moment und Trainingsplätze: gezielte Übungen (Minispiele, K37) → 4–8 Punkte in gewähltem Wert pro Einheit; Abklingzeit 1 Spieltag je Echo |
| Steuerung | Spieler kann einzelne Werte „sperren“ (kein weiterer Schliff) – präzises Bauen ohne Grind-Frust |
| Zurücksetzen | **Klangbad** (Thermen Seraphe, Schlackenwehr; später überall per Item „Klangsalz“): setzt Schliff eines Wertes oder aller Werte zurück (Sol-Kosten, K42) |
| Ranked | Schliff zählt voll (Vorbereitung ist Teil der Kompetenz); Level-Normalisierung K61 betrifft nur L |

---

## 9. Darstellung im UI

```
 ┌──────────────── ECHO-KARTE: Fernlit · Lv. 16 · Blüte ────────────────┐
 │ Persönlichkeit: Sanft (SVE +10 %) ♥ Füttern   Temperament: Ruhig       │
 │                                                                      │
 │ HP  ███████████░░░░░  61 / 61                                         │
 │ ANG ███████░░░░░░░░░  21          Anlage ●●○○ (solide)  Schliff  0/80  │
 │ VER ████████░░░░░░░░  25          Anlage ●●●○ (stark)   Schliff  4/80  │
 │ SAN █████████░░░░░░░  27          Anlage ●●○○           Schliff  0/80  │
 │ SVE ██████████░░░░░░  29 ▲        Anlage ●●●● (vollendet) Schliff 12/80│
 │ GES ███████░░░░░░░░░  23          Anlage ●○○○ (schwach) Schliff  0/80  │
 │ PRÄ 100   AUS 105                                     Σ Schliff 16/240 │
 │ EP ████████████░░░░  3.512 / 3.930 bis Lv. 17 (Stetig)                │
 └──────────────────────────────────────────────────────────────────────┘
   ▲ = Persönlichkeits-Wert · Anlage-Anzeige abhängig vom Forschungs-Skill
```

Detail-UI in K54.

---

## 10. Code & Tests

### 10.1 Rechenkern

`Source/AethrisCore/Public/Echo/EchoStatCalculator.h` (im Repository) – `constexpr`-Funktionen `ComputeHP`, `ComputeCore`, `ComputeSecondary`, `ApplyStage`, `HitChancePermille` mit Kompilierzeit-Prüfungen.

### 10.2 Werte einer Instanz berechnen

```cpp
// GF_Monsters/Private/Stats/EchoStatsService.cpp (Auszug)
FEchoStats UEchoStatsService::ComputeStats(const FEchoInstance& Echo) const
{
	using namespace Aethris::Stats;
	const UEchoSpeciesDefinition& Sp = *Species(Echo.Species);
	const FEchoStats& B = Sp.BaseStats;
	const FEchoStats& A = Echo.Genome.Aptitudes;
	const FEchoStats& S = Echo.Polish;
	const FGameplayTag Boost = Personalities->BoostedStat(Echo.Personality);   // Stat.Attack …

	FEchoStats Out;
	Out.HP        = ComputeHP(B.HP, Echo.Level, A.HP, S.HP);
	Out.Attack    = ComputeCore(B.Attack,    Echo.Level, A.Attack,    S.Attack,    Boost == AethrisTags::Stat_Attack);
	Out.Defense   = ComputeCore(B.Defense,   Echo.Level, A.Defense,   S.Defense,   Boost == AethrisTags::Stat_Defense);
	Out.SpAttack  = ComputeCore(B.SpAttack,  Echo.Level, A.SpAttack,  S.SpAttack,  Boost == AethrisTags::Stat_SpAttack);
	Out.SpDefense = ComputeCore(B.SpDefense, Echo.Level, A.SpDefense, S.SpDefense, Boost == AethrisTags::Stat_SpDefense);
	Out.Speed     = ComputeCore(B.Speed,     Echo.Level, A.Speed,     S.Speed,     Boost == AethrisTags::Stat_Speed);
	Out.Precision = ComputeSecondary(B.Precision, A.Precision, Boost == AethrisTags::Stat_Precision);
	Out.Evasion   = ComputeSecondary(B.Evasion,   A.Evasion,   Boost == AethrisTags::Stat_Evasion);
	// HP-Persönlichkeit (Zäh/Gutmütig): +10 % nach Formel, gerundet ab (Ganzzahl)
	if (Boost == AethrisTags::Stat_HP) { Out.HP = Out.HP * 1100 / 1000; }
	return Out;
}
```

### 10.3 Schliff-Regel

```cpp
/** Fügt Schliff hinzu unter Beachtung der Grenzen (80/Wert, 240 gesamt) und Sperren (K18 §8). */
int32 UEchoStatsService::AddPolish(FEchoInstance& Echo, FGameplayTag Stat, int32 Points) const
{
	using namespace Aethris::Stats;
	if (Echo.PolishLocks.HasTag(Stat)) { return 0; }
	int32& Cur = StatRef(Echo.Polish, Stat);
	const int32 Total = Echo.Polish.HP + Echo.Polish.Attack + Echo.Polish.Defense
	                  + Echo.Polish.SpAttack + Echo.Polish.SpDefense + Echo.Polish.Speed;
	const int32 Granted = FMath::Clamp(Points, 0, FMath::Min(MaxPolishPerStat - Cur, MaxPolishTotal - Total));
	Cur += Granted;
	return Granted;
}
```

*Ergänzung Datenmodell:* `FEchoInstance` erhält `FGameplayTagContainer PolishLocks` (Save-Fragment „Chor“ v2, Migration: leer).

### 10.4 Tests

| Test | Inhalt |
|---|---|
| `Aethris.Unit.Core.Stats.PythonParity` | 10.000 Zufallskombinationen (B, L, A, S, P) – C++ = Python-Referenz |
| `Aethris.Unit.Core.Stats.Bounds` | Keine Überläufe (int64-Zwischenwerte), Max-Werte §2.3 |
| `Aethris.Unit.Monsters.Polish.Caps` | 80/240-Grenzen, Sperren |
| `Aethris.Unit.Monsters.Growth.Monotonic` | Alle Kurven streng monoton, L1 = 0 EP |

---

## 11. Decision Records

### ADR-084 – Persönlichkeiten nur mit Boni, ohne Abzüge
| Option | Vorteile | Nachteile |
|---|---|---|
| (a) +10 %/−10 % Paare (25 Kombinationen) | Optimierungstiefe | „Falsche“ Persönlichkeit entwertet Echos; Genre-Nähe |
| (b) 16 Persönlichkeiten, nur Bonus + Verhalten | Jedes Echo brauchbar, Persönlichkeit als Charakterausdruck, eigene Identität | Etwas weniger Min-Max-Spielraum |
- **Entscheidung:** (b).

### ADR-085 – Anlage multiplikativ (bis +15 %), Schliff additiv
- **Entscheidung:** Anlagen wirken proportional (genetische „Qualität“), Schliff flach (Trainingsspezialisierung). Vorteil: zwei unterscheidbare Optimierungsachsen; Anlage bleibt auf allen Levels relevant. Nachteil: zwei Konzepte erklären → UI trennt klar („Anlage“ = Punkte/Sterne, „Schliff“ = Balken).

### ADR-086 – Trefferchance gedeckelt auf 50–100 %
- **Entscheidung:** DR-07-konform; Ausweich-Stacking kann Kämpfe nicht unendlich verlängern (DR-11).

### ADR-087 – Bindung gibt mehr EP als Erschöpfen (×1,2)
- **Entscheidung:** Belohnt das Kernverb der Säule S2. Nachteil: Spieler könnten aus EP-Gründen binden und freilassen → erwünscht (Kodex-Fortschritt, Freilassen stärkt Wildwacht-Ruf, K47).

---

## 12. Kanon-Updates

| Bereich | Eintrag | Status |
|---|---|---|
| §79 | Formeln HP / Kernwert / PRÄ-AUS (§2.2), ganzzahlig, `EchoStatCalculator.h` = Referenz `tools/ref/aethris_stats.py` (static_asserts) | LOCKED |
| §79 | Stufen −4…+4: Kern ×0,5…×2,0, PRÄ/AUS ×0,70…×1,30 (`StatStages.csv`); Reservewechsel setzt Stufen zurück | LOCKED |
| §79 | Trefferchance = clamp(Genauigkeit × PRÄ_eff / AUS_eff, 50 %, 100 %) | LOCKED |
| §80 | Anlagen 0–15 je Wert (8 Werte), +1 %/Punkt bzw. +1 je 3 bei PRÄ/AUS; Rare/VeryRare garantieren 2/3 Werte mit 15; Anzeige in 4 Klassen bzw. exakt per Skill; Item **Klangstimmung** (Endgame) setzt einen Wert auf 15 | LOCKED |
| §80 | Schliff 0–80 je Kernwert, Summe 240 (finalisiert), HP +S, Kern +⌊S/2⌋; Quellen Kampf (`PolishYield`) und Training (4–8, 1 Spieltag Abklingzeit); Sperren (`PolishLocks`); Reset per **Klangbad**/Klangsalz | LOCKED |
| §81 | 16 Persönlichkeiten (`Personalities.csv`): +10 % auf HP/ANG/VER/SAN/SVE/GES bzw. +5 PRÄ/AUS, keine Abzüge, Lieblingsinteraktion, Idle, KI-Neigung; Änderung per **Wesensklang** (Endgame) | LOCKED |
| §82 | 5 Temperamente (`Temperaments.csv`): Ruhig, Feurig, Wachsam, Neugierig, Stoisch mit Bindungsfenster, Anschlägen, Reaktion, Wahrnehmung, Harmonie, Fluchtschwelle; Standardverteilung 30/15/20/20/15 %; sichtbar ab Kodex-Stufe 2 | LOCKED |
| §83 | Wachstumskurven Swift 0,6·L³ · Steady 0,8·L³ · Late L³·(0,45+0,65·L/100) · Wave L³·(0,8+0,08·sin(L/6)) (`GrowthRates.csv`); Legendäre/Mythische = Late | LOCKED |
| §83 | EP-Formel (Struktur) mit Ertrag je Stufe, Quelle Kampf 1,0/Bindung 1,2/Trainer 1,3; Tuning K63; Species.csv erhält ab K20 Spalten `ExpYield`, `PolishYield` | LOCKED (Struktur) |
| §29 | `FEchoInstance` + `PolishLocks` (Chor-Fragment v2) | LOCKED |
| §10 | ADR-084 – ADR-087 | LOCKED |

---

## 13. Kapitel-Checkliste

- [x] Acht Statuswerte mit Kampf- und Oberweltwirkung
- [x] Ganzzahlige Formeln (HP, Kern, PRÄ/AUS) mit Beispielen und Grenzwerten
- [x] C++-Rechenkern mit Kompilierzeit-Parität zur Python-Referenz (im Repo)
- [x] Kampfstufen, Geschwindigkeitsbezug, Trefferformel (DR-07)
- [x] 16 Persönlichkeiten (ohne Abzüge) als Daten
- [x] 5 Temperamente mit Bindungs- und KI-Wirkung als Daten
- [x] 4 Wachstumskurven (Daten, Monotonie geprüft) und EP-Formel
- [x] Anlagen und Schliff vollständig (Schliff-PROVISIONAL aus K03 finalisiert)
- [x] UI-Skizze, Code, Tests
- [x] ADR-084 – ADR-087, CANON aktualisiert

➡️ **Nächstes Kapitel: K19 – Evolutionssystem.**
