#!/usr/bin/env python3
"""K30 – 30 Crescendos (ABL_U001–U030) und 30 Feldfähigkeiten (ABL_F001–F030), je Typ 2.

Crescendo-Zeile: (Name, Kat., Stärke, Gen., Ziel, Effekte, Tags) – Budget 200–320 (AB-08), Harmoniekosten aus Budget.
Feld-Zeile: (Name, Feld-Tag, Bedingung(Merkmal/Größe), Beschreibung)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "abilities"))
from abl_write import write_kind
from abl import budget, parse

P, S, St = "Physical", "Special", "Status"
U = {
"Ember": [("Sonnensturz", S, 150, 900, "Enemies", "Terrain(Glutboden,3)", ""),
          ("Phönixlied", St, 0, 0, "Allies", "Revive(50);Heal(Allies,30);Stage(Allies,Attack,+1);Cleanse(Allies);Haste(Allies,40)", "")],
"Tide": [("Weltflut", S, 140, 950, "Enemies", "Push(Target);Weather(Rain,3)", ""),
         ("Gezeitenschoß", St, 0, 0, "Allies", "Regen(Allies,10,3);Cleanse(Allies);Shield(Allies,20);Heal(Allies,40);Harmony(10)", "")],
"Stone": [("Bergsturz", P, 160, 900, "Row", "Status(Erschuettert,500)", "Ground"),
          ("Ewiger Fels", St, 0, 0, "Allies", "Shield(Allies,35);Stage(Allies,Defense,+2);Stage(Allies,SpDefense,+1);Taunt(1);Heal(Allies,15);Harmony(10)", "")],
"Storm": [("Himmelszorn", S, 75, 900, "Enemies", "Multi(2,2);WeatherBoost(Thunderstorm)", ""),
          ("Orkanschwinge", St, 0, 0, "Allies", "Haste(Allies,100);Stage(Allies,Speed,+2);Weather(Thunderstorm,4);Stage(Allies,Evasion,+1);Harmony(20)", "")],
"Bloom": [("Urwaldchor", St, 0, 0, "Allies", "Heal(Allies,50);Regen(Allies,8,3);Terrain(Ueberwuchs,5);Cleanse(Allies)", "Sound"),
          ("Dornenmeer", P, 130, 950, "Enemies", "Bind(2)", "")],
"Frost": [("Ewiger Winter", S, 120, 900, "Enemies", "Delay(Enemies,60)", ""),
          ("Eiszeit", St, 0, 900, "Enemies", "Status(Starre,700);Weather(Snow,5);Stage(Enemies,Speed,-2);Stage(Enemies,Precision,-1);Terrain(Eisflaeche,4)", "")],
"Void": [("Weltlöscher", S, 180, 850, "Single", "Dispel(Target);IgnoreShield();HarmonyDrain(20)", ""),
         ("Große Leere", St, 0, 950, "Enemies", "Dispel(Enemies);HarmonyDrain(40);Status(Entzug,1000);Terrain(Stillefeld,4);Stage(Enemies,SpAttack,-1)", "")],
"Light": [("Zenitfeuer", S, 150, 1000, "Enemies", "Reveal();SureHit()", ""),
          ("Morgenweihe", St, 0, 0, "Allies", "Cleanse(Allies);Heal(Allies,40);Shield(Allies,20);Stage(Allies,Precision,+1);Harmony(20)", "")],
"Venom": [("Pestwolke", S, 90, 950, "Enemies", "Status(Vergiftet,1000,3)", ""),
          ("Säureflut", S, 130, 900, "Row", "Stage(Target,Defense,-2);Stage(Target,SpDefense,-2)", "")],
"Metal": [("Schmiedehammer", P, 180, 900, "Single", "Status(Gebrochen,1000)", "Contact"),
          ("Eherne Phalanx", St, 0, 0, "Allies", "Shield(Allies,30);Stage(Allies,Defense,+2);Counter(Physical,1000);Stage(Allies,SpDefense,+1);Harmony(20)", "")],
"Spirit": [("Geisterheer", S, 100, 1000, "Enemies", "IgnoreFormation();Status(Furcht,500)", ""),
           ("Seelenrückkehr", St, 0, 0, "Allies", "Revive(60);Decoy();Stage(Allies,Evasion,+1);Heal(Allies,30);Harmony(20)", "")],
"Crystal": [("Prismenkatarakt", S, 120, 900, "Enemies", "Charge();Status(Gebrochen,500)", ""),
            ("Spiegelpalast", St, 0, 0, "Allies", "Reflect(Special);Reflect(Physical);Shield(Allies,25);Charged();Stage(Allies,SpDefense,+2);Harmony(10)", "")],
"Sound": [("Sinfonie der Welt", S, 110, 1000, "Enemies", "Delay(Enemies,50);Harmony(20)", "Sound"),
          ("Großer Takt", St, 0, 0, "Allies", "Haste(Allies,80);Harmony(40);Stage(Allies,Attack,+1);Stage(Allies,SpAttack,+1);Cleanse(Allies);Stage(Allies,Speed,+1)", "Sound")],
"Gravity": [("Ereignishorizont", S, 140, 900, "Enemies", "Pull(Target);Bind(2)", ""),
            ("Schwerkraftsturz", P, 190, 850, "Single", "SwapRows();Stage(Target,Speed,-2)", "")],
"Arcane": [("Formel des Ursprungs", S, 140, 950, "Enemies", "TypeChange(Target,Arcane,2)", ""),
           ("Umkehr der Welt", St, 0, 0, "Field", "InvertChart(2);StealBuffs();Copy();Terrain(Glyphenfeld,4);Stage(Allies,SpAttack,+2)", "")],
}

# Feldfähigkeiten: (Name, Tag, Bedingung, Beschreibung)
F = {
"Ember": [("Fackelschein", "Field.Sense", "Trait:Glowing|Trait:Thermal", "Erhellt dunkle Höhlen (Radius 12 m) und verscheucht lichtscheue Wildechos."),
          ("Glutschmelze", "Field.Traversal", "Size:M+", "Schmilzt Eisbarrieren und brennt Dornengestrüpp nieder (Pfad-Tor Typ „Eis/Dorn“, K40).")],
"Tide": [("Quellsucher", "Field.Gather", "Trait:Swimmer|Trait:Filterer", "Findet Süßwasserquellen und Muschelbänke; +1 Wasser-/Perlen-Ressource je Fundstelle."),
         ("Wasserlauf", "Field.Traversal", "Size:M+", "Trägt den Wärter über flaches Wasser (≤ 1,2 m) ohne Schwimmreittier; Gezeitenpfade bei Ebbe.")],
"Stone": [("Felsbrecher", "Field.Traversal", "Size:M+", "Zerschlägt rissige Felsblöcke (Pfad-Tor „Geröll“)."),
          ("Erzspur", "Field.Gather", "Trait:Lithophage|Trait:Burrower", "Markiert Erzadern im Resonanzsinn (Radius 40 m); +1 Erz je Abbau.")],
"Storm": [("Aufwind", "Field.Traversal", "Trait:Flier|Trait:Drifter", "Erzeugt eine Thermiksäule für den Gleiter (+18 m Höhe, 1× je 60 s)."),
          ("Wetterwitterung", "Field.Sense", "Trait:Migratory|Trait:Flier", "Zeigt das Wetter der nächsten 2 Wetterblöcke an (Vorhersage K14 §11).")],
"Bloom": [("Rankenbrücke", "Field.Traversal", "Size:S+", "Lässt Ranken über Spalten bis 6 m wachsen (Pfad-Tor „Spalt“, 3 min)."),
          ("Kräuterkunde", "Field.Gather", "Trait:Pollinator|Trait:Grazer", "Findet Heilkräuter; +1 Kräuter je Sammelpunkt, seltene Kräuter sichtbar.")],
"Frost": [("Eisbrücke", "Field.Traversal", "Size:S+", "Friert Wasserflächen zu begehbarem Eis (Radius 8 m, 90 s)."),
          ("Frischhalter", "Field.Gather", "Trait:Hunter|Trait:Collector", "Kühlt Proviant: Lager-Gerichte halten einen Spieltag länger (K41).")],
"Void": [("Stillesinn", "Field.Sense", "Any", "Zeigt Stillezonen und Stillsteine im Umkreis von 150 m an (Hauptquest-Relevanz, K44)."),
         ("Schattenschritt", "Field.Social", "Trait:Camouflaged|Trait:Ambusher", "Wärter wird 20 s lang von Wildechos und Wachen schwer bemerkt (Schleichen, K53).")],
"Light": [("Leuchtfeuer", "Field.Sense", "Trait:Glowing", "Erhellt Umgebung (Radius 20 m) und markiert versteckte Kisten/Fragmente."),
          ("Lichtsignal", "Field.Social", "Any", "Sendet ein Signal an Koop-Partner und NPC-Wachen (Ping, Hilferuf, Händlerruf).")],
"Venom": [("Giftschneise", "Field.Traversal", "Size:S+", "Zersetzt Moorgestrüpp und Pilzwände (Pfad-Tor „Gestrüpp“)."),
          ("Ködermischer", "Field.Gather", "Trait:Ambusher|Trait:Hunter", "Verbessert eigene Lockmittel: +20 % Wirkung auf Bindungs-Köder (K36).")],
"Metal": [("Erzwitterung", "Field.Gather", "Trait:Collector|Trait:ToolUser", "Findet Metallteile und Relikte im Boden (Grab-Punkte im Resonanzsinn)."),
          ("Mechanik", "Field.Puzzle", "Trait:ToolUser", "Bedient dorunische Mechanismen und Kontor-Winden (Rätsel-Tor „Mechanik“).")],
"Spirit": [("Geistersicht", "Field.Sense", "Any", "Macht Geisterspuren, Klangfragmente und verborgene Echos sichtbar (Radius 30 m)."),
           ("Seelenpfad", "Field.Puzzle", "Trait:Drifter|Trait:Singer", "Folgt Ahnenpfaden in Ruinen; öffnet Geister-Tore (Rätsel-Tor „Ahnen“).")],
"Crystal": [("Kristallklang", "Field.Gather", "Trait:Lithophage|Trait:Collector|Trait:Glowing", "Findet Kristallknoten; +1 Kristall je Abbau."),
            ("Lichtlenker", "Field.Puzzle", "Any", "Lenkt Lichtstrahlen über Kristallspiegel (Rätsel-Tor „Prisma“).")],
"Sound": [("Echolot", "Field.Sense", "Trait:Echolocator|Trait:Singer", "Kartiert Höhlen und Innenräume im Umkreis von 60 m auf der Karte."),
          ("Lockruf", "Field.Social", "Any", "Lockt Wildechos der eigenen Linie und verwandter Arten an (+1 Spawn-Chance, K52).")],
"Gravity": [("Schwebelast", "Field.Puzzle", "Size:M+", "Hebt und verschiebt schwere Objekte bis 2 t (Rätsel-Tor „Last“)."),
            ("Leichtschritt", "Field.Traversal", "Any", "Halbiert die Schwerkraft des Wärters für 15 s (Sprunghöhe ×1,6, Fallschaden aus).")],
"Arcane": [("Glyphenlesen", "Field.Puzzle", "Any", "Liest dorunische Inschriften (Lore, Kodex-Hinweise, Rätsel-Tor „Glyphe“)."),
           ("Siegelöffner", "Field.Puzzle", "Trait:ToolUser|Trait:Collector|Trait:Guardian", "Öffnet magisch versiegelte Truhen und Türen (Rätsel-Tor „Siegel“).")],
}

if __name__ == "__main__":
    rows = []
    for t, lst in U.items():
        for (name, cat, pw, acc, tgt, eff, tags) in lst:
            v, _ = budget(pw, acc, tgt, cat, parse(eff))
            hc = max(60, min(100, (60 + (v - 200) // 3 + 5) // 10 * 10))
            rows.append(dict(Type=t, DisplayName=name, Category=cat, Power=pw, Accuracy=acc, Target=tgt, Effects=eff,
                             Tags="|".join(x for x in (tags, f"HarmonyCost={hc}") if x)))
    write_kind("Crescendo", rows)
    rows = []
    for t, lst in F.items():
        for (name, tag, cond, text) in lst:
            rows.append(dict(Type=t, DisplayName=name, Effects="", Trigger=cond, Tags=tag, Description=text))
    write_kind("Field", rows)
