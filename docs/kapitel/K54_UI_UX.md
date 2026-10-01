# K54 · UI/UX

| Feld | Wert |
|---|---|
| Dokument | Kapitel 54 von 68 · Präsentation I |
| Version | 1.0 |
| Owner | Lead UI/UX Designer |
| Mitwirkende | UX Researcher, UI Artist, UI Programmer (CommonUI/MVVM), Accessibility Lead, Localization Lead, Audio (UI-Klang) |
| Baut auf | K02 §5 (Steuerung, Kamera), §11.3 (Zugänglichkeit), K03 §9 (Menüarchitektur), K17 (Typ-Symbole), K31–K36 (Kampf, Bindung), K39 (Kodex, Fotografie), K43 (Wärter), K46 (Entscheidungs-UX), K47 (Fraktionsseite), K48 (Tagebuch, Hinweisstufen), CANON §9 (CommonUI + UMG + MVVM), §24 (Sprachen), DR-06, DR-24, DR-27 |
| Status | ✅ Freigegeben |
| Im Repository | `Data/UI/InputActions.csv` (45 Aktionen), `Screens.csv` (28 Bildschirme), `HudElements.csv`, `AccessibilityOptions.csv` (23 Optionen), Prüfer `tools/gen_ui.py` (UI-01–UI-06); `tools/data_lint.py` um Spaltenprüfung DL-COL erweitert |
| Neue Kanon-Einträge | CANON §206 (UX-Prinzipien), §207 (Eingabe), §208 (Bildschirme, HUD), §209 (Kampf- und Bindungs-UI), §210 (Barrierefreiheit, Lokalisierung), §211 (UI-Technik) |

---

## Inhalt

1. [UX-Prinzipien](#1-ux-prinzipien)
2. [Plattformen und Darstellung](#2-plattformen-und-darstellung)
3. [Eingabe](#3-eingabe)
4. [Bildschirmarchitektur](#4-bildschirmarchitektur)
5. [HUD](#5-hud)
6. [Kampf-UI](#6-kampf-ui)
7. [Bindungs-UI](#7-bindungs-ui)
8. [Menüs im Einzelnen](#8-menüs-im-einzelnen)
9. [Benachrichtigungen und Belohnungen](#9-benachrichtigungen-und-belohnungen)
10. [Barrierefreiheit](#10-barrierefreiheit)
11. [Lokalisierung und Text](#11-lokalisierung-und-text)
12. [Visuelle Sprache](#12-visuelle-sprache)
13. [Technik](#13-technik)
14. [UX-Forschung und Kennzahlen](#14-ux-forschung-und-kennzahlen)
15. [Anforderungen an andere Abteilungen](#15-anforderungen-an-andere-abteilungen)
16. [Decision Records](#16-decision-records)
17. [Kanon-Änderungen](#17-kanon-änderungen)
18. [Kapitel-Checkliste](#18-kapitel-checkliste)

---

## 1. UX-Prinzipien

| Prinzip | Regel | Prüfbar durch |
|---|---|---|
| **UX-01 Welt vor Interface** | Der HUD ist im Standard minimal; Informationen erscheinen, wenn sie gebraucht werden (Kontext-Sichtbarkeit) | HUD-Tabelle §5 |
| **UX-02 Hören heißt sehen** | Jedes Klangsignal hat ein gleichwertiges visuelles Muster (Form + Farbe + Rhythmus) – Pflicht, nicht Option (DR-24) | Audit je Mechanik |
| **UX-03 Vorher wissen** | Zeitkosten, Reihenfolge und Wirkung sind vor der Bestätigung sichtbar (DR-06, F-4 „keine verdeckten Werte“) | Kampf-UI §6 |
| **UX-04 Nie bestrafen fürs Lesen** | Menüs pausieren offline die Spieluhr; im Koop nie (Hinweis im HUD) | Screens.csv „Pauses“ |
| **UX-05 Drei Klicks** | Jede häufige Aufgabe (Echo wechseln, Item nutzen, Quest verfolgen, Kodex öffnen) in ≤ 3 Eingaben | Aufgabenmatrix §14 |
| **UX-06 Unumkehrbares halten** | Freilassen, Neustimmung, Finale-Entscheidung: Halten 3 s statt Klick | UI-05 |
| **UX-07 Symbol + Wort** | Typen, Status, Fraktionen immer mit Symbol und Name, nie nur Farbe (K17) | Farbenblind-Test |
| **UX-08 Ruhige Belohnung** | Belohnungen gesammelt, kurz, nie mehr als zwei gleichzeitig (DR-27) | §9 |
| **UX-09 Einheitliche Navigation** | Gleiche Taste = gleiche Bedeutung in allen Menüs (Bestätigen, Zurück, Reiter, Details, Sortieren) | UI-02 |
| **UX-10 Text, der passt** | Layouts mit +40 % Textreserve (Deutsch/Polnisch), CJK-Schriften getestet | §11 |
| **UX-11 Diegese, wo es trägt** | Kompass mit Sonne/Mond, Resonanzsinn in der Welt, Klangbriefe als Benachrichtigung | §5 |
| **UX-12 Zugänglich ab Start** | Barrierefreiheitsfragen beim ersten Start (Untertitel, Textgröße, Farbenblind, Timing) | §10 |

---

## 2. Plattformen und Darstellung

| Plattform | Auflösung UI | Sicherheitsbereich | Mindest-Schriftgröße | Besonderheit |
|---|---|---|---|---|
| PS5 | 4K-Layout, skaliert | 90 % (TV) | 28 px bei 1080p-Referenz | DualSense-Glyphen, Haptik für Bindungsfenster |
| Xbox Series | 4K-Layout | 90 % | 28 px | Xbox-Glyphen |
| PC | 1080p–4K, 16:9/21:9 | 100 % (wählbar) | 22 px | Maus/Tastatur-Layouts (Tab-Leiste statt Radial), freie Belegung |
| Switch 2 (TV) | 1080p | 90 % | 28 px | Joy-Con-Glyphen |
| Switch 2 (Handheld) | 1080p auf 7,9″ | 95 % | **22 px** + Textgröße L als Standard | Touch für Menüs und Karte (optional) |

**Skalierung:** UI wird für 1080p entworfen und mit DPI-Kurven auf 4K skaliert; 21:9 erweitert Kampfansicht und Karte, Menüs bleiben 16:9-zentriert.

---

## 3. Eingabe

Alle Aktionen sind Enhanced-Input-Aktionen mit Tags `Input.*` (K04). Belegungen sind vollständig umbelegbar; Glyphen wechseln automatisch mit dem zuletzt benutzten Gerät.

### 3.1 Welt

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Bewegen | LS | WASD | – | – |
| Kamera | RS | Maus | – | Invertieren je Achse |
| Interagieren / Springen | A | E / Leertaste | – | Kontextabhängig: Interagieren hat Vorrang in Reichweite |
| Ducken / Schleichen | B | Strg | – | Umschalten oder Halten (Option) |
| Echo-Befehl | X | F | – | Gehe dorthin / Sammle / Feldfähigkeit |
| Reittier rufen | Y | R | – | – |
| Werkzeuge (Radial) | LB | 1–8 / Mausrad | – | – |
| Chor (Radial) | RB | Tab | – | – |
| Resonanzsinn | LT | Q (halten) | 0,3 s | Option: Umschalten statt Halten (Barrierefreiheit) |
| Resonator / Kodex-Linse | RT | Rechte Maustaste | – | – |
| Schnellzugriff Items | D-Pad | Z / X / C / V | – | – |
| Pausemenü (Radial-Hub) | Menu | Esc | – | – |
| Karte | View | M | – | – |
| Tagebuch | View (halten) | J | 0,5 s | – |

### 3.2 Kampf

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Menü-Navigation | LS / D-Pad | Pfeile / Maus | – | – |
| Bestätigen | A | Linke Maustaste / Enter | – | – |
| Zurück | B | Rechte Maustaste / Rücktaste | – | – |
| Formation | X | F | – | – |
| Detailansicht Ziel | Y | R | – | – |
| Zeitleiste vorschauen | LB | Umschalt | – | Zeigt Auswirkung der gewählten Aktion auf ≥ 8 Züge (DR-06) |
| Echo wechseln | RB | Tab | – | – |
| Analyse (Kodex-Overlay) | LT | Q | – | – |
| Crescendo | RT | Leertaste | – | Nur bei Harmonie 100 |
| Animationstempo | View | T | – | 1× / 1,5× / 2× / Überspringen (K02 §4) |

### 3.3 Bindung

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Anschlag | A | Leertaste / Linke Maustaste | – | Timing-Fenster K36; Option Auto-Einklang |
| Abbrechen | B | Esc | – | – |
| Lockmittel wechseln | Y | R | – | – |
| Fokus | LT | Q (halten) | – | Verlangsamt Frequenzwelle, kostet Ausdauer |
| Siegel wählen | RT | 1–8 | – | – |

### 3.4 Menü, Foto, Gleiten, Reiten

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Navigieren | LS / D-Pad | Pfeile / Maus | – | – |
| Bestätigen | A | Enter / Linke Maustaste | – | – |
| Zurück | B | Esc / Rechte Maustaste | – | – |
| Reiter links | LB | Q | – | – |
| Reiter rechts | RB | E | – | – |
| Details | Y | R | – | – |
| Sortieren / Filtern | X | F | – | – |
| Halten zum Bestätigen | A (halten) | Enter (halten) | 3,0 s | Unumkehrbare Entscheidungen (Finale K46, Freilassen, Neustimmung) |

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Auslösen | RT | Linke Maustaste | – | – |
| Zoom | LT / RS | Mausrad | – | – |
| Fotomodus verlassen | B | Esc | – | – |

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Gleiter öffnen | A (in der Luft) | Leertaste (in der Luft) | – | – |
| Sturzflug | B | Strg | – | – |

| Aktion | Gamepad | Tastatur/Maus | Halten | Hinweis |
|---|---|---|---|---|
| Absteigen | B | Strg | – | – |
| Sprinten | LS (drücken) | Umschalt | – | Kostet Reit-Ausdauer |
| Reitfähigkeit | X | F | – | Graben / Klettern / Steigen je Reitart |

**Kontextregeln:** „Interagieren“ hat Vorrang vor „Springen“, wenn ein Interaktionsziel in Reichweite ist (Hinweis-Glyphe sichtbar). Der Kontext wechselt sichtbar (HUD-Rahmenfarbe dezent) – nie ohne Signal.

---

## 4. Bildschirmarchitektur

### 4.1 Ebenen (CommonUI)

```
 Modal       ┌───────────────────────────────┐  Entscheidung (Finale), Bestätigen, Fehler
 Menu        │ Vollbild-Menüs (Chor, Kodex …) │  pausiert offline die Spieluhr
 GameMenu    │ Radial-Hub, Dialog, Overlays   │  Welt sichtbar, abgedunkelt
 Game        │ HUD, Kampf, Bindung, Foto      │  Welt läuft
             └───────────────────────────────┘
```

### 4.2 Bildschirme

| Name | DisplayName | Layer | Source | Pauses | Opens | Notes |
|---|---|---|---|---|---|---|
| SCR_HUD | HUD | Game | K54 | nein | – | Minimal; Elemente in HudElements.csv |
| SCR_COMBAT | Kampf | Game | K31–K33 | nein | SCR_ECHO_DETAIL|SCR_KODEX_OVERLAY | Zeitleiste ≥ 8 Züge (DR-06) |
| SCR_BOND | Resonanzbindung | Game | K36 | nein | – | Frequenzwelle, Fenster, Resonanz |
| SCR_PAUSE_HUB | Radial-Hub | GameMenu | K03 §9 | ja | SCR_CHORUS|SCR_KODEX|SCR_INVENTORY|SCR_MAP|SCR_CRAFTING|SCR_JOURNAL|SCR_WARDEN | Gamepad Radial / Maus Tab-Leiste |
| SCR_WARDEN | Wärter (Zentrum) | Menu | K43 | ja | SCR_SKILLTREE|SCR_FACTIONS | Rang, Sol, Akkorde, Ausrüstung |
| SCR_SKILLTREE | Skilltree | Menu | K43 | ja | – | 4 Äste |
| SCR_FACTIONS | Fraktionen | Menu | K47 | ja | – | Ruf, Ränge, Rüstmeister |
| SCR_CHORUS | Chor | Menu | K18/K37 | ja | SCR_ECHO_DETAIL|SCR_SANCTUARY | 6 Plätze + Reserve |
| SCR_ECHO_DETAIL | Echo-Detail | Menu | K18/K29/K37/K38 | ja | – | Werte, Fähigkeiten, Bindungsstufe, Genetik |
| SCR_SANCTUARY | Resonanzhain | Menu | K37 | ja | SCR_BREEDING | 10 Gärten |
| SCR_BREEDING | Zucht | Menu | K38 | ja | – | Erbklang, Keime |
| SCR_KODEX | Kodex | Menu | K39 | ja | SCR_PHOTO_ALBUM | 256 Arten × 4 Stufen, Fragmente, Lore |
| SCR_KODEX_OVERLAY | Kodex-Overlay (Analyse) | GameMenu | K39 | nein | – | Im Kampf und in der Welt |
| SCR_PHOTO | Fotomodus | Game | K39 | nein | – | Kodex-Linse First-Person |
| SCR_PHOTO_ALBUM | Fotoalbum | Menu | K39 | ja | – | Sterne, Verhaltensfotos |
| SCR_INVENTORY | Inventar | Menu | K40/K41 | ja | – | Taschen je Kategorie |
| SCR_CRAFTING | Crafting | Menu | K41 | ja | – | Rezepte, fehlende Zutaten markieren |
| SCR_SHOP | Händler | Menu | K42 | ja | – | Kauf/Verkauf, Rabatt (K47) |
| SCR_MAP | Karte | Menu | K08/K48 | ja | – | Hinweisstufen, Wetter-Vorhersage, Resonanzsteine |
| SCR_JOURNAL | Tagebuch | Menu | K48 | ja | – | Quests / Aufgaben / Erledigt |
| SCR_DIALOGUE | Dialog | GameMenu | K44/K48 | nein | – | Drei Haltungen; Schiefertafel (Orden) |
| SCR_DECISION | Entscheidung (Finale) | Modal | K46 | ja | – | Halten 3 s, keine Zeitgrenze, zufällige Reihenfolge |
| SCR_REWARD | Belohnung / Rangaufstieg | Modal | K43/K47 | nein | – | Kurz (2 s), Warteschlange |
| SCR_SETTINGS | Einstellungen | Menu | K54 | ja | – | Inkl. Barrierefreiheit |
| SCR_SAVE | Speichern/Laden | Menu | K64 | ja | – | Finale-Speicherpunkt eigener Slot |
| SCR_ONLINE | Online | Menu | K59–K61 | nein | – | Koop, Tausch, Ranked |
| SCR_CHARACTER | Charakter-Editor | Menu | K01/K54 | ja | – | Körper, Gesicht, Stimme, Pronomen |
| SCR_TITLE | Titel | Menu | K03 | – | SCR_CHARACTER|SCR_SAVE|SCR_SETTINGS |  |

### 4.3 Radial-Hub (Pausenmenü)

```
                           ┌────────────┐
                 ┌─────────│    CHOR    │─────────┐
                 │         └────────────┘         │
          ┌────────────┐                    ┌────────────┐
          │   KODEX    │     ┌────────┐     │  INVENTAR  │
          └────────────┘     │ WÄRTER │     └────────────┘
          ┌────────────┐     │ Rang 17│     ┌────────────┐
          │   KARTE    │     │ 4.210 ◎│     │  CRAFTING  │
          └────────────┘     └────────┘     └────────────┘
                 │         ┌────────────┐         │
                 └─────────│  TAGEBUCH  │─────────┘
                           └────────────┘
     ─────────────────────────────────────────────────────────
     Fotoalbum · Fraktionen · Online · Einstellungen · Speichern
```

Gamepad: rechter Stick wählt, A öffnet, die Auswahl merkt sich die letzte Position. Maus/Tastatur: Tab-Leiste oben, Zahlentasten 1–7 springen direkt.

---

## 5. HUD

| DisplayName | Default | Hideable | Diegetic | Position | Notes |
|---|---|---|---|---|---|
| Kompass mit Sonne/Mond | Always | ja | Teilweise | Oben Mitte | Questrichtung nach Hinweisstufe (K48 §9), Phase (CANON §65) |
| Resonanzsinn-Pulse | Context | nein | Ja | Weltraum | Visuelle Wellen + Audio (DR-24); Hochkontrast-Option |
| Chor-Leiste (HP/Status) | Context | ja | Nein | Unten links | Nur bei Schaden/Status oder auf Tastendruck |
| Ausdauer (Wärter/Reiten) | Context | ja | Teilweise | Am Charakter | Ring, nur bei Verbrauch |
| Questziel (verfolgt) | Context | ja | Nein | Rechts | Einblendung bei Schrittwechsel, sonst ausgeblendet |
| Interaktions-Hinweis | Context | ja | Nein | Am Objekt | Glyphe + Verb |
| Benachrichtigungen | Context | ja | Nein | Rechts oben | Warteschlange (§9) |
| Uhr | Off | ja | Nein | Oben rechts | Optional (CANON §65) |
| Wetter-Vorhersage | Off | ja | Nein | Oben rechts | Optional; Karte zeigt immer |
| Untertitel | Context | ja | Nein | Unten Mitte | Sprecher, Richtung, Klangbeschreibung |
| Minikarte | Off | ja | Nein | Unten rechts | Barrierefreiheit (Orientierung) |
| Schadenszahlen | Context | ja | Nein | Kampf | Nur im Kampf |
| Klangradar | Off | ja | Nein | Unten Mitte | Barrierefreiheit Hören: Richtung wichtiger Geräusche |

```
┌──────────────────────────── ☼ ── N ── ◆ Eiðvik ── O ── ☾ ────────────────────────────┐
│                                                                                       │
│                                                                                       │
│                         (Welt; Resonanzsinn als Wellen im Raum)                       │
│                                                                                       │
│                                                  ┌─────────────────────────────────┐ │
│                                                  │ ✉ Klangbrief von Ysolde          │ │
│                                                  └─────────────────────────────────┘ │
│  ◐ Fernwyn  ███████░░  Gift                                                          │
│  ◑ Brokkar  █████████                         [A] Sprechen: Fischerin Tjarke          │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

Im Standard sind nur Kompass und Interaktions-Hinweis sichtbar; Chor-Leiste und Ausdauer erscheinen bei Bedarf. „HUD-frei“ (alles aus außer Resonanzsinn) ist eine Einstellung, keine Kamera-Funktion.

---

## 6. Kampf-UI

```
┌───────────────────────────── ZEITLEISTE (nächste 10 Züge) ─────────────────────────────┐
│  ▶ Fernwyn │ Brokk* │ Fernwyn │ Gegner A │ Brokkar │ Gegner B │ Fernwyn │ … │ ⟳ Runde 4   │
│    jetzt      +30     +80        +95        +110      +140       +170                   │
└────────────────────────────────────────────────────────────────────────────────────────┘
                     * Vorschau: „Rankenschlag“ (Zeit 110) verschiebt Gegner A um +40
   Harmonie  ▓▓▓▓▓▓▓▓▓▓░░░░░  68/100          Wetter: Regen (Flut ×1,2 · Glut ×0,8)

   ┌─ Fernwyn (Blüte/Sturm) Lv. 24 ──────────────┐   ┌─ Gegner A: Rillward Lv. 22 ─────┐
   │ HP ███████████░░  71 %   Status: –          │   │ HP ██████░░░  58 %  ⚠ Gift (2)  │
   │ 1 Rankenschlag   Blüte  Phys  Zeit 110       │   │ Schwach: Glut, Gift · Stark: Flut│
   │ 2 Böenhieb       Sturm  Phys  Zeit 90  ×1,5  │   └──────────────────────────────────┘
   │ 3 Sporenwolke    Blüte  Stat  Zeit 120       │
   │ 4 Windwechsel    Sturm  Stat  Zeit 70        │   Kombo bereit: „Sturmsaat“ (60 Ticks)
   │ ★ Crescendo: Urwaldchor (Harmonie 100)      │
   └──────────────────────────────────────────────┘
```

| Element | Regel | Quelle |
|---|---|---|
| Zeitleiste | ≥ 8 Züge sichtbar (10 auf großen Bildschirmen); Vorschau der gewählten Aktion verschiebt Einträge live | DR-06, K31 |
| Zeitkosten | Vor Bestätigung sichtbar, inkl. Gehorsam-Aufschlag (+40 %) | K31, CANON §18 |
| Effektivität | ×-Wert und Wort („sehr effektiv“), nie nur Farbe | K17 |
| Wetter | Modifikatoren als Klartext | K14 §6 |
| Harmonie | Zahl + Balken; Crescendo-Taste leuchtet bei 100 | K33 |
| Kombos | Hinweis, wenn eine Kombo im 60-Tick-Fenster möglich ist | K33 |
| Status | Symbol + Name + Restdauer | K32 |
| Gegnerinfo | Nur Wissen, das der Kodex hat (Stufe 2: Schwächen, Stufe 3: Fähigkeiten) – F-3 Wissensstand | K34, K39 |
| Tempo | 1× / 1,5× / 2× / Überspringen | K02 §4 |
| Erklärmodus | Optional: jede Zeitkosten-Zahl mit Formel-Tooltip | §10 |

---

## 7. Bindungs-UI

```
                 Resonanz  ███████████████░░░░░  412 / 1000    Schwelle ▲ 400 (Selten)
   ┌──────────────────────────────────────────────────────────────────────────┐
   │      ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿[ GUT  ▕▔▔PERFEKT▔▔▏  GUT ]∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿     │
   │                       ◄────── 280 ms ──────►                               │
   └──────────────────────────────────────────────────────────────────────────┘
          Versuche ◆◆◇        Siegel: Gestimmt (Fenster ×1,1)     [A] Anschlag
```

| Regel | Inhalt |
|---|---|
| Kein Prozentwert | Die UI zeigt Resonanz gegen Schwelle und das Fenster – nie eine Erfolgschance (K36, DR-03) |
| Welle | Frequenzwelle als Form + Farbe + Rhythmus; Ton parallel (DR-24); Fokus verlangsamt die Welle sichtbar |
| Haptik | DualSense/Joy-Con: Pulse im Takt der Welle; Gut-Fenster spürbar |
| Großzügiges Timing | Option ×1,25–×2 vergrößert das Fenster sichtbar (K54 §10) |
| Auto-Einklang | Option: Anschlag automatisch im Gut-Fenster |

---

## 8. Menüs im Einzelnen

| Menü | Inhalt | Kernaufgaben (≤ 3 Eingaben) | Quelle |
|---|---|---|---|
| **Chor** | 6 Plätze, Reserve, Hain-Zugang | Echo tauschen, Reihenfolge ändern, Detail öffnen | K18, K37 |
| **Echo-Detail** | Werte (HP, ANG, VER, SAN, SVE, GES, PRÄ, AUS), Schliff, Fähigkeiten (4 + Passiv + Crescendo + Feld), Bindungsstufe, Genetik, Herkunft (DR-16) | Fähigkeit tauschen, Passiv wechseln (Wandelklang), Stimmung sehen | K18, K29, K37, K38 |
| **Kodex** | 256 Arten × 4 Stufen, Spuren, Lore, Klangfragmente (verzerrt bis zur Wahrheitsebene) | Art suchen, Aufgabe verfolgen, Klang anhören | K39 |
| **Karte** | Regionen, Zonen, Resonanzsteine, Questbereiche (Hinweisstufe), Wettervorhersage, Spieluhr | Ziel setzen, Schnellreise, Vorhersage lesen | K08, K14, K48 |
| **Tagebuch** | Hauptquest, Nebenquests, Fraktionen, Aufgaben, Erledigt | Verfolgen, Zurückstellen, Hinweis anfordern | K48 |
| **Inventar** | Taschen je Kategorie, Siegel, Lockmittel, Materialien, Schlüssel | Item nutzen, sortieren, zum Schnellzugriff legen | K40, K41 |
| **Crafting** | Rezepte nach Werkbank, fehlende Zutaten markieren | Herstellen, Marker setzen | K41 |
| **Händler** | Kauf/Verkauf, Tagespreis, Rabatt (K47) | Kaufen, verkaufen, vergleichen | K42 |
| **Wärter** | Rang, Sol, Akkorde, Ausrüstung, Skilltree, Fraktionen | Skill wählen, Ausrüstung wechseln | K40, K43, K47 |
| **Hain/Zucht** | 10 Gärten, Stimmung, Keime | Echo platzieren, Paar wählen, Keim ausbrüten | K37, K38 |
| **Fotoalbum** | Fotos mit Sternen, Verhaltensfotos, Spuren | Foto bewerten, teilen (Plattform) | K39 |
| **Dialog** | Drei Haltungen als gleich große Optionen; Orden: Schiefertafel | Antworten, Verlauf ansehen | K44, K48 |
| **Entscheidung** | Finale: zwei Optionen, Halten 3 s, keine Zeitgrenze | – | K46 |
| **Charakter-Editor** | Körper (8 Grundformen, frei skalierbar), Gesicht (Vorlagen + Regler), Haut, Haare, Stimme (2 Sprecher, Tonlage), Pronomen (er/sie/neutral, CANON §24) | – | K01 |

**Vergleich statt Rechnen:** Überall, wo Werte gewählt werden (Fähigkeit, Ausrüstung, Echo), zeigt die UI die Differenz zum aktuellen Zustand (▲ +12 GES).

---

## 9. Benachrichtigungen und Belohnungen

| Typ | Darstellung | Dauer | Regel |
|---|---|---|---|
| Klangbrief (Nachricht) | Brief-Symbol, Absender | 4 s, bleibt im Tagebuch | Diegetisch (UX-11) |
| Kodex-Fortschritt | Art-Symbol + Stufe | 2,5 s | gesammelt nach Kampf/Beobachtung |
| Ruf | Wappen + Zahl | 2 s | gesammelt (K47 §11) |
| Rangaufstieg / Akkord | Modal (SCR_REWARD) | 2 s + Liste | nie während Kampf |
| Item erhalten | Symbol + Anzahl | 2 s | gestapelt je Item |
| Quest-Schritt | Tagebuch-Zeile | 3 s | nur verfolgte Quest im HUD |

**Warteschlange:** höchstens zwei Einblendungen gleichzeitig; Rest wartet, bis Ruhe ist (kein Kampf, kein Dialog). Gleichartige Meldungen werden zusammengefasst („+3 Kodex-Beobachtungen“). DR-27 gilt auch für die Darstellung: Kein Belohnungstyp dominiert die Einblendungen einer halben Stunde.

---

## 10. Barrierefreiheit

| Area | DisplayName | Values | Default | Notes |
|---|---|---|---|---|
| Motorik | Vollständiges Remapping | alle Aktionen | an | InputActions.csv „Remappable“ |
| Motorik | Ein-Hand-Profil | links/rechts | aus | Kombiniert Bewegen und Aktionen auf einer Gamepad-Hälfte |
| Motorik | Halten → Umschalten | an/aus je Aktion | aus | Resonanzsinn, Ducken, Fokus |
| Motorik | Großzügiges Timing | 1,0×/1,25×/1,5×/2,0× | 1,0× | Bindungsfenster (K36) und Kombo-Fenster (K33) |
| Motorik | Auto-Einklang | an/aus | aus | Anschlag erfolgt im Gut-Fenster automatisch; Perfekt-Bonus entfällt |
| Motorik | Halten statt Hämmern | an/aus | an | Keine Tastenhämmer-Mechaniken im Spiel; Option betrifft Minispiele |
| Sehen | Farbenblind-Modus | Aus/Protan/Deutan/Tritan | Aus | Paletten verschoben; Typen immer Symbol + Name (K17) |
| Sehen | Textgröße | S/M/L/XL | M | Min. 28 px bei 1080p (TV), 22 px Handheld |
| Sehen | Hochkontrast-UI | an/aus | aus | Hintergründe abdunkeln, Konturen |
| Sehen | Hochkontrast-Resonanzsinn | an/aus | aus | Wellen kräftiger, Formen statt Farben |
| Sehen | Bewegungsreduktion | an/aus | aus | Kamerawackeln, Bildschirmblitze, Bewegungsunschärfe aus |
| Hören | Untertitel | aus/Dialog/Dialog+Klänge | Dialog | Sprecherfarbe + Name, Richtungspfeil |
| Hören | Visuelle Klangsignale | an (fest) | an | Jede Frequenz-Mechanik mit Wellenmuster (DR-24) – nicht abschaltbar |
| Hören | Klangradar | an/aus | aus | HUD_SOUND_RADAR |
| Hören | Mono-Audio | an/aus | aus |  |
| Kognition | Questziel-Erinnerung | an/aus | an | Nach 10 min ohne Fortschritt dezenter Hinweis |
| Kognition | Kampf-Empfehlungen | an/aus | aus | Schlägt eine sinnvolle Aktion vor (nie automatisch) |
| Kognition | Zeitleisten-Erklärmodus | an/aus | aus | Erklärt Zeitkosten jeder Aktion |
| Kognition | Hinweisstufe | Lauschend/Geführt/Markiert | Geführt | K48 §9.1 |
| Tempo | Kampfanimation | 1×/1,5×/2×/Überspringen | 1× | K02 §4 |
| Tempo | Dialog-Autoplay | an/aus | aus |  |
| Allgemein | Schwierigkeit | Erzählung/Standard/Meister | Standard | K02 §11 (Ranked unabhängig) |
| Allgemein | Menü-Vorlesen | an/aus | aus | Plattform-TTS für Menüs und Untertitel |

### 10.1 Ersteinrichtung

Beim ersten Start (vor dem Titelbild) fragt das Spiel vier Dinge mit Live-Vorschau: Untertitel, Textgröße, Farbenblind-Modus, Timing. Alles ist später änderbar. Plattform-Einstellungen (Systemschriftgröße, TTS) werden übernommen.

### 10.2 Ein Spiel über Hören, gehörlos spielbar

| Klangmechanik | Visuelles Gegenstück |
|---|---|
| Resonanzsinn | Wellen im Raum (Form je Typ, Rhythmus je Entfernung) |
| Frequenzwelle (Bindung) | Welle mit Fenster; Haptik |
| Echo-Rufe (Kodex, Verhalten) | Untertitel „[ruft dreimal kurz]“ + Richtungspfeil |
| Grundfrequenzen (Story) | Leuchtende Notenlinien (K44 Vision Ilens) |
| Stille-Motiv | Entsättigung + Partikel-Stillstand |
| Klangbriefe | Text |
| Glockenrätsel, Orgeln, Harfen (Quests) | Ton als Farbe + Höhe auf einer Notenleiste |
| Wetter-Ankündigung | Symbol + Kompass-Hinweis |

QA prüft jede Klangmechanik im **Stummschalt-Durchlauf** (K66): Das Spiel muss ohne Ton vollständig lösbar sein.

---

## 11. Lokalisierung und Text

| Regel | Inhalt |
|---|---|
| Sprachen | Text 12, Vertonung 5 (CANON §24) |
| Textreserve | Layouts +40 % gegenüber Englisch; Buttons +60 % |
| Textboxen | ≤ 3 Zeilen / 160 Zeichen (CANON §24) |
| Schriften | Latein, Kyrillisch (Reserve), CJK (JA, KO, ZH-Hans, ZH-Hant) mit eigenen Größen (+2 px) |
| Zahlen | Lokalisierte Trennzeichen (1.000 / 1,000), Dezimalkomma im Deutschen |
| Geschlecht | Ansprache er/sie/neutral über String-Varianten (Gender-Tokens) |
| Namen | Echos, Orte, Typen als Eigennamen; Klangfamilien regional (CANON §22) |
| Pseudo-Lokalisierung | CI-Build mit verlängerten, akzentuierten Strings findet Überläufe automatisch |

---

## 12. Visuelle Sprache

| Element | Regel |
|---|---|
| Farben | Token-System (UI-Grund, Akzent, Warnung, Erfolg, Typ-Farben je 15 Typen); Farbenblind-Paletten als alternative Token-Sätze |
| Typ-Symbole | 15 Symbole (K17), immer mit Namen; Formen unterscheidbar in Graustufe |
| Typografie | Eine Serifen-Schrift für Titel (Ton: alt, gesungen), eine Grotesk für Text; Zahlen tabellarisch |
| Ikonografie | 64-px-Raster, 2 px Strich, runde Enden; Fraktionswappen (K47) |
| Bewegung | Übergänge 120–200 ms, Ease-out; Bewegungsreduktion schaltet auf Überblenden |
| Klang (UI) | Jede Bestätigung hat einen Ton aus der Skala des Weltlieds; „Zurück“ ist ein absteigendes Intervall (K55) |

Die Art Bible (K56) legt Farbwerte und Schriften fest; K54 legt Regeln und Tokens fest.

---

## 13. Technik

### 13.1 Architektur

```
 Domain/Feature-Dienste (K06 Services) ──Events──► ViewModels (MVVM, GF_UI) ──Bindings──► UMG-Widgets (CommonUI)
                                       ◄──Befehle (Commands)──────────────────────────────
```

| Baustein | Regel |
|---|---|
| CommonUI | Ebenen §4.1, Eingabe-Routing, Glyphen, Fokus-Verwaltung für Gamepad |
| MVVM | Ein ViewModel je Bildschirm + geteilte ViewModels (Chor, Wärter, Uhr, Wetter); Widgets enthalten keine Spiellogik |
| GF_UI (Presentation) | liest nur über Events/ViewModels; ruft Feature-Dienste über Interfaces (Schichtregel R5, `tools/check_layers.py`) |
| Daten | Bildschirme, HUD, Eingabe, Barrierefreiheit als Daten (`Data/UI/*.csv`) → `UAethrisUISettings` / Primary Assets |
| Text | String Tables je Domäne (`<Domäne>.<Id>.Name`, K04 §11) |

### 13.2 Budgets

| Messgröße | PS5 | Switch 2 | PC (Min-Spec) |
|---|---|---|---|
| UI-Gamethread je Frame | ≤ 0,8 ms | ≤ 1,2 ms | ≤ 1,0 ms |
| UI-Rendering | ≤ 0,6 ms | ≤ 1,0 ms | ≤ 0,8 ms |
| UI-Speicher (Texturen, Fonts) | ≤ 180 MB | ≤ 120 MB | ≤ 200 MB |
| Menü öffnen (Eingabe → erstes Bild) | ≤ 100 ms | ≤ 150 ms | ≤ 100 ms |

### 13.3 Prüfung

`python3 tools/gen_ui.py`:

| Regel | Prüfung |
|---|---|
| UI-01 | Jede Aktion hat Gamepad- und Tastatur/Maus-Belegung |
| UI-02 | Keine Doppelbelegung im selben Kontext (Ausnahmen nur als „Kontext“ markiert) |
| UI-03 | Alle Bildschirm-Verweise existieren |
| UI-04 | Alle Barrierefreiheitsoptionen aus K02 §11.3 vorhanden |
| UI-05 | Unumkehrbares nur mit Halten ≥ 3 s |
| UI-06 | Alle HUD-Elemente abschaltbar außer Resonanzsinn (DR-24) |

**Ergebnis:** 0 Verstöße. Zusätzlich prüft `data_lint.py` ab jetzt **alle** Datentabellen auf gleiche Spaltenzahl (DL-COL) – dabei wurden zehn ältere Tabellen mit ungeschützten Kommas in Werten gefunden und korrigiert (u. a. Solo-Varianten der Raids in `Bosses.csv`, zwei Skill-Effekte in `Skills.csv`); die betroffenen Kapitel wurden neu erzeugt.

---

## 14. UX-Forschung und Kennzahlen

| Kennzahl | Ziel | Messung |
|---|---|---|
| Zeit bis „Echo im Kampf wechseln“ | ≤ 2 s (Median, Spielstunde 2) | Telemetrie `ui.task` |
| Fehlbedienungen „Zurück statt Bestätigen“ | < 2 % je Menüsitzung | Telemetrie |
| Kodex-Nutzung | ≥ 60 % öffnen den Kodex in den ersten 3 h | Telemetrie |
| Zeitleisten-Verständnis | ≥ 80 % beantworten „Wer ist als Nächstes dran?“ korrekt (Playtest P2) | Fragebogen |
| Barrierefreiheit | Stummschalt-Durchlauf ohne Blocker; Spielende mit Farbenblindheit/Hörbeeinträchtigung in jedem Großtest (n ≥ 6) | P3/P4 (K02 §12) |
| Lesbarkeit Handheld | 95 % lesen Questtexte ohne Zoom (Switch 2) | Playtest |

**Aufgabenmatrix (UX-05):** Für 20 häufige Aufgaben ist die Eingabezahl dokumentiert und wird bei jeder Menüänderung neu gemessen (automatisierter UI-Test).

---

## 15. Anforderungen an andere Abteilungen

| Abteilung | Anforderung | Kapitel |
|---|---|---|
| Art | Farbtokens, Typ-Symbole, Wappen, Schriften, Icons (64-px-Raster) | K56 |
| Audio | UI-Klänge aus der Weltlied-Skala, Haptik-Muster (Bindung) | K55 |
| Programmierung | CommonUI-Ebenen, ViewModels, Datentabellen-Import, Glyphenwechsel | K05/K06 |
| Lokalisierung | Pseudo-Loc-Build, CJK-Fonts, Gender-Tokens | K66 |
| QA | Stummschalt-Durchlauf, Farbenblind-Durchlauf, Aufgabenmatrix, Textüberläufe | K66 |
| Plattformen | Zertifizierungsanforderungen (Sicherheitsbereiche, Glyphen, Systemmenüs) | K65 |

---

## 16. Decision Records

| ADR | Entscheidung | Begründung | Verworfen |
|---|---|---|---|
| ADR-206 | Minimaler Kontext-HUD als Standard, alles abschaltbar außer Resonanzsinn | Welt vor Interface; Resonanzsinn ist DR-24-Pflichtsignal | Voller HUD |
| ADR-207 | Radial-Hub (Gamepad) und Tab-Leiste (Maus/Tastatur) als zwei gleichwertige Layouts | Jede Eingabeart bekommt ihr natürliches Menü | ein Layout für alle |
| ADR-208 | Bindungs-UI ohne Erfolgsprozent | Bindung ist deterministisch (K36), Prozente würden Zufall suggerieren | Prozentanzeige |
| ADR-209 | Menüs pausieren offline die Spieluhr, im Koop nie | Kein Druck beim Lesen; Koop bleibt synchron | immer Echtzeit |
| ADR-210 | UI-Konfiguration (Eingabe, Bildschirme, HUD, Barrierefreiheit) als Daten mit Prüfer | Konsistenz, Lokalisierung, automatische Tests | im Widget-Code |

---

## 17. Kanon-Änderungen

| Bereich | Eintrag | Status |
|---|---|---|
| §206 | UX-Prinzipien UX-01–UX-12 | LOCKED |
| §207 | Eingabe: `InputActions.csv` (45 Aktionen, 7 Kontexte), vollständiges Remapping, Kontextregel Interagieren > Springen | LOCKED |
| §208 | Bildschirme `Screens.csv` (CommonUI-Ebenen Game/GameMenu/Menu/Modal), Radial-Hub/Tab-Leiste, HUD `HudElements.csv` (Kontext-Sichtbarkeit) | LOCKED |
| §209 | Kampf-UI (Zeitleiste ≥ 8, Vorschau, Effektivität mit Wort, Gegnerinfo nach Kodex-Stufe), Bindungs-UI (ohne Prozent, Welle + Haptik) | LOCKED |
| §210 | Barrierefreiheit `AccessibilityOptions.csv` (23 Optionen, Ersteinrichtung, Stummschalt-Durchlauf), Lokalisierung (+40 % Reserve, CJK, Gender-Tokens, Pseudo-Loc) | LOCKED |
| §211 | UI-Technik (CommonUI + MVVM, Budgets), Prüfer UI-01–UI-06, DL-COL | LOCKED |
| §10 | ADR-206 – ADR-210 | LOCKED |

---

## 18. Kapitel-Checkliste

- [x] UX-Prinzipien, Plattformen, Sicherheitsbereiche, Schriftgrößen
- [x] Eingabe für alle Kontexte (Gamepad + Maus/Tastatur), Kontextregeln
- [x] Bildschirmarchitektur (Ebenen, 28 Bildschirme, Radial-Hub)
- [x] HUD mit Kontext-Sichtbarkeit
- [x] Kampf- und Bindungs-UI mit Mockups
- [x] Menüs mit Kernaufgaben, Charakter-Editor
- [x] Benachrichtigungen und Belohnungsregeln
- [x] Barrierefreiheit vollständig, gehörlos spielbar
- [x] Lokalisierung, visuelle Sprache, Technik, Budgets
- [x] Prüfer (0 Verstöße), DL-COL ergänzt und Altdaten korrigiert
- [x] Anforderungen, ADR-206 – ADR-210, CANON §206–§211

➡️ **Nächstes Kapitel: K55 – Audio Bible.**
