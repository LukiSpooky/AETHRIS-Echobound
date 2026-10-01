#!/usr/bin/env python3
"""K29 – 90 passive Fähigkeiten (ABL_P001–ABL_P090), 6 je Typ.

Zeile: (Name, Auslöser, Effekte, Tags, Zusatztext)
16 Passive sind **Feldklänge** der Ursprungsstimmen/Mythischen (Tag `Feldklang`, art-exklusiv, K27-Signaturen).
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "abilities"))
from abl_write import write_kind

FK = "Feldklang|Exclusive"
P = {
"Ember": [
    ("Glutherz", "LowHP", "TypePower(Ember,1500)", "", ""),
    ("Funkenhaut", "ContactTaken", "Status(Brand,300)", "", "Der Status trifft den Angreifer."),
    ("Hitzespeicher", "Weather.Heatwave", "Heal(Self,6)", "", "Wirkt zu Beginn jedes eigenen Zuges."),
    ("Flammentanz", "CritDealt", "Haste(Self,30)", "", ""),
    ("Aschefell", "Always", "Resist(Tide,800);Immune(Ausgetrocknet)", "", ""),
    ("Weltenschmiede", "FieldSong", "Custom(Pyrthagon)", FK, "Pyr'thagon: Jeder eigene Treffer erhöht die eigene VER um 1 Stufe (max. +4); das Feld bleibt dauerhaft Glutboden."),
],
"Tide": [
    ("Gezeitenkörper", "TurnStart", "Heal(Self,5)", "", "Nur in Regen oder auf Flutfeld."),
    ("Strömungssinn", "SwitchIn", "Haste(Self,40)", "", ""),
    ("Glatte Haut", "Always", "Immune(Rueckstoss);Mod(Evasion,1100)", "", ""),
    ("Brandungsschild", "RowFront", "Resist(Ember,750)", "", ""),
    ("Tiefenruhe", "RowBack", "Regen(Self,4,99)", "", "Solange das Echo in der Hinterreihe steht."),
    ("Gezeitenwende", "FieldSong", "Custom(Thalassyr)", FK, "Thal'assyr: Jede zweite Runde tauschen die Reihen beider Seiten; die eigene Seite handelt danach zuerst."),
],
"Stone": [
    ("Felsenhaut", "Always", "Mod(Defense,1150)", "", ""),
    ("Standfest", "Always", "Immune(Rueckstoss);Immune(Erschuettert)", "", "Rückstoß ist für Stein ohnehin wirkungslos; Standfest ergänzt Erschüttert."),
    ("Bergruhe", "LowHP", "Shield(Self,25)", "", ""),
    ("Sandverbunden", "Weather.Sandstorm", "Mod(SpDefense,1300)", "", ""),
    ("Fundament", "RowFront", "Shield(AllyRow,5)", "", "Zu Beginn jeder Runde für die eigene Reihe."),
    ("Bergschwere", "FieldSong", "Custom(Orhgruun)", FK, "Orh'gruun: Gegner können die Reihe nicht wechseln; alle Verbündeten VER +2 Stufen."),
],
"Storm": [
    ("Windläufer", "Always", "TimeCost(-10)", "", "Gilt für alle eigenen aktiven Fähigkeiten."),
    ("Böenreiter", "Weather.Thunderstorm", "Mod(Speed,1300)", "", ""),
    ("Blitzreflex", "HitTaken", "Haste(Self,20)", "", ""),
    ("Sturmauge", "Always", "Immune(Verlangsamt);Mod(Precision,1050)", "", ""),
    ("Kettenfunke", "HitDealt", "Status(Erschuettert,100)", "", "Nur bei Mehrfachtreffern: je Treffer."),
    ("Rückenwindgeist", "SwitchIn", "Haste(Allies,30)", "", ""),
],
"Bloom": [
    ("Photosynth", "Weather.Clear", "Heal(Self,6)", "", "Zu Beginn jedes eigenen Zuges bei klarem Wetter."),
    ("Wurzelkraft", "RowFront", "Immune(Rueckstoss);Mod(Defense,1100)", "", ""),
    ("Pollenwolke", "ContactTaken", "Stage(Attacker,Precision,-1,300)", "", ""),
    ("Grüner Daumen", "Always", "HealPower(1300)", "", ""),
    ("Keimkraft", "AllyFainted", "Heal(Allies,15)", "", ""),
    ("Wurzellied", "FieldSong", "Custom(Sylvanor)", FK, "Sylv'anor: Jede Runde heilen alle Verbündeten 6 % HP; Blüte-Fähigkeiten kosten 20 Zeit weniger."),
],
"Frost": [
    ("Eiskern", "Always", "Resist(Ember,800);Immune(Starre)", "", ""),
    ("Kältehauch", "ContactTaken", "Delay(Attacker,30)", "", ""),
    ("Schneetarnung", "Weather.Snow", "Mod(Evasion,1250)", "", ""),
    ("Präzisionsfrost", "HitDealt", "Stage(Target,Precision,-1,200)", "", ""),
    ("Firnpanzer", "LowHP", "Shield(Self,20);Delay(Enemies,20)", "", ""),
    ("Aurora der Erhaltung", "FieldSong", "Custom(Isvaldr)", FK, "Isv'aldr: Positive Stufen und Schilde der Verbündeten können nicht entfernt, gestohlen oder durchdrungen werden."),
],
"Void": [
    ("Leerer Blick", "SwitchIn", "Dispel(Target)", "", "Trifft den Gegner gegenüber."),
    ("Seelenhunger", "EnemyFainted", "Heal(Self,20);HarmonyDrain(10)", "", ""),
    ("Schweigsam", "Always", "Immune(Verstummt);Resist(Sound,750)", "", ""),
    ("Nichtigkeit", "HitTaken", "HarmonyDrain(3)", "", ""),
    ("Schattenkörper", "RowBack", "Mod(Evasion,1150)", "", ""),
    ("Große Pause", "FieldSong", "Custom(Velnox)", FK, "Velnox: Die Harmonie beider Seiten wird zu Beginn jeder Runde auf 0 gesetzt; Fähigkeiten mit Tag Sound verstummen."),
],
"Light": [
    ("Strahlkraft", "Always", "TypePower(Light,1100);Immune(Geblendet)", "", ""),
    ("Lichtgestalt", "BattleStart", "Reveal()", "", "Enthüllt alle Gegner für 2 Runden."),
    ("Reiner Glanz", "StatusReceived", "Cleanse(Self)", "", "Einmal pro Kampf."),
    ("Morgenwache", "Weather.Clear", "Mod(SpAttack,1200)", "", ""),
    ("Rätselglanz", "FieldSong", "Custom(Ashkareth)", FK, "Ash'kareth: Alle verborgenen Werte, Passiven und Kampfsets werden enthüllt; Täuschung, Tarnung und Trugbilder enden sofort."),
    ("Finsternis", "FieldSong", "Custom(Aurelune)", FK, "Aurelune: Licht und Leere tauschen ihre Typvorteile, solange Aurelune auf dem Feld steht."),
],
"Venom": [
    ("Giftdrüsen", "Always", "StatusChance(1500)", "", "Gilt nur für Vergiftet."),
    ("Zähe Säfte", "Always", "Immune(Vergiftet);Resist(Bloom,800)", "", ""),
    ("Fäulniskreis", "EnemyFainted", "Status(Vergiftet,1000,2)", "", "Trifft den nächsten Gegner."),
    ("Stachelkleid", "ContactTaken", "Status(Vergiftet,500)", "", "Der Status trifft den Angreifer."),
    ("Moorgedächtnis", "FieldSong", "Custom(Nhaelvesh)", FK, "Nhael'vesh: Verklingende Echos beider Seiten hinterlassen Nebel: Vergiftet überträgt sich auf Gegner und heilt Verbündete."),
    ("Ewiger Kreis", "FieldSong", "Custom(Ouroveth)", FK, "Ouroveth: Gift heilt Verbündete statt zu schaden; ein verklingender Verbündeter keimt einmal mit 25 % HP neu."),
],
"Metal": [
    ("Stahlkörper", "Always", "Mod(Defense,1100);Immune(Erschuettert)", "", ""),
    ("Konterinstinkt", "HitTaken", "Counter(Physical,500)", "", "Einmal pro Runde."),
    ("Magnetfeld", "Always", "Resist(Storm,750)", "", ""),
    ("Schmiedeglut", "LowHP", "Stage(Self,Attack,+2)", "", ""),
    ("Rüstmeister", "SwitchIn", "Shield(AllyRow,10)", "", ""),
    ("Rostfrei", "Always", "Resist(Venom,700)", "", ""),
],
"Spirit": [
    ("Durchscheinend", "Always", "Mod(Evasion,1100);Immune(Furcht)", "", ""),
    ("Spukgestalt", "BattleStart", "Decoy()", "", ""),
    ("Seelenwacht", "AllyFainted", "Stage(Allies,SpDefense,+1);Harmony(15)", "", ""),
    ("Grenzgänger", "Always", "TypePower(Spirit,1100)", "", "Geist-Fähigkeiten ignorieren zusätzlich Schilde."),
    ("Ahnenhauch", "LowHP", "Heal(Self,25)", "", ""),
    ("Weltgedächtnis", "FieldSong", "Custom(Kathurel)", FK, "Ka'thurel: Jede eingesetzte Fähigkeit wird gespeichert; jeder Verbündete kann einmal pro Kampf eine gespeicherte Fähigkeit des Gegners einsetzen."),
],
"Crystal": [
    ("Prismenhaut", "HitTaken", "Reflect(Special)", "", "Einmal pro Kampf."),
    ("Resonanzspeicher", "HitTaken", "Charged()", "", "Nach dem ersten erlittenen Treffer."),
    ("Kristallgitter", "Always", "Mod(SpDefense,1150);Immune(Gebrochen)", "", ""),
    ("Lichtbrecher", "Always", "Resist(Light,700)", "", ""),
    ("Brechung", "FieldSong", "Custom(Prismaion)", FK, "Prism'aion: Jeder Klang- oder Kristall-Angriff trifft zusätzlich ein zweites Ziel mit 50 % Stärke."),
    ("Spiegelwelt", "FieldSong", "Custom(Mirrowisp)", FK, "Mirrowisp: Jeder Angriff trifft zusätzlich ein Spiegelbild des Angreifers mit 30 % Stärke."),
],
"Sound": [
    ("Taktgefühl", "Always", "TimeCost(-5);Immune(Verstummt)", "", ""),
    ("Chorstimme", "HitDealt", "Harmony(5)", "", ""),
    ("Echoohr", "HitTaken", "Stage(Self,Evasion,+1,300)", "", ""),
    ("Resonanzkörper", "Always", "TypePower(Sound,1100);Resist(Sound,800)", "", ""),
    ("Einklang", "FieldSong", "Custom(Aethrion)", FK, "Aeth'rion: Der Eigenklang-Bonus aller Verbündeten gilt für jede Fähigkeit, deren Typ einer ihrer Typen ist – auch für Zweittypen der Fähigkeitswahl."),
    ("Taktwechsel", "FieldSong", "Custom(Chronaire)", FK, "Chronaire: Die Zeitleiste läuft rückwärts – das langsamste Echo handelt zuerst."),
],
"Gravity": [
    ("Schwerpunkt", "Always", "Immune(Schwebend);Immune(Rueckstoss)", "", ""),
    ("Massenträgheit", "RowFront", "Mod(Defense,1150);Mod(Speed,900)", "", ""),
    ("Anziehung", "SwitchIn", "Pull(Target)", "", "Zieht den Gegner gegenüber nach vorn."),
    ("Bahnlenker", "HitDealt", "Stage(Target,Evasion,-1,300)", "", ""),
    ("Fallgewicht", "Always", "TypePower(Gravity,1100)", "", "Zusätzlich +10 % gegen Schwebend-Ziele."),
    ("Sternensturz", "FieldSong", "Custom(Zenthrax)", FK, "Zenthrax: Zu Beginn jeder Runde schlägt ein Meteor (Stärke 60, Schwerkraft) auf ein zufälliges gegnerisches Feld; Schwerkraft-Effekte doppelt."),
],
"Arcane": [
    ("Formelgeist", "Always", "TypePower(Arcane,1100);Immune(Verflucht)", "", ""),
    ("Glyphenwacht", "StatusReceived", "Stage(Self,SpDefense,+1)", "", ""),
    ("Umkehrsinn", "BattleStart", "Stage(Self,SpAttack,+1)", "", "Zusätzlich +1 SAN, solange die Typtabelle umgekehrt ist."),
    ("Wandelhaut", "HitTaken", "TypeChange(Self,Arcane,2)", "", "Einmal pro Kampf; nur bei sehr effektivem Treffer."),
    ("Regelbrecher", "Always", "TimeCost(-10)", "", "Gilt nur für Arkan-Status-Fähigkeiten."),
    ("Spiegelgedächtnis", "EnemyFainted", "Copy()", "", "Kopiert die letzte Fähigkeit des verklungenen Gegners ins Kampfset (bis Kampfende)."),
],
}

if __name__ == "__main__":
    rows = []
    for t, lst in P.items():
        for (name, trig, eff, tags, text) in lst:
            rows.append(dict(Type=t, DisplayName=name, Trigger=trig, Effects=eff, Tags=tags, Description=text))
    write_kind("Passive", rows)
