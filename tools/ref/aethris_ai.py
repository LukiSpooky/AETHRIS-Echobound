#!/usr/bin/env python3
"""Referenz-Kampf-KI (K34): Utility-Bewertung von Aktionen, Profile, Simulation mit echten Lernsets.

Aufruf:
  aethris_ai.py matrix [N]   -> Siegquoten-Matrix der KI-Profile (1v1, gespiegelte Paarungen)
  aethris_ai.py explain      -> Bewertungsprotokoll eines Beispielzuges
Vereinfachungen gegenüber GF_Combat: 1v1, keine Reserve, Effekte Status/Stufen/Delay/Haste/Heal/Shield/Drain/Recoil/Multi/Charge.
"""
from __future__ import annotations
import csv, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "abilities"))
import aethris_combat as ac
from aethris_random import AethrisRandom
from abl import parse

ROOT = pathlib.Path(__file__).resolve().parents[2]
STATUS_DOT = {"Brand": 60, "Vergiftet": 30}


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


class Data:
    def __init__(self):
        self.sp = [s for s in rows("Data/Echos/Species.csv") if s["LineKind"] not in ("Legendary", "Mythical")]
        self.ab = {a["Name"]: a for a in rows("Data/Abilities/Abilities.csv") if a["Kind"] == "Active"}
        self.ls = {}
        for r in rows("Data/Echos/Learnsets.csv"):
            if r["Method"] == "Level" and r["Ability"] in self.ab:
                self.ls.setdefault(r["Species"], []).append((int(r["Level"]), r["Ability"]))
        self.chart = ac.load_chart()


def kit(D, sp, level):
    """NPC-Kampfset-Bau (K34 §6): stärkste Primärtyp-Schadensfähigkeit, stärkste Sekundärtyp-/Abdeckungs-Schadensfähigkeit,
    beste Status-/Hilfsfähigkeit, dann die nächststärkste Schadensfähigkeit. Kategorie nach ANG/SAN-Profil bevorzugt."""
    known = [D.ab[a] for lv, a in sorted(D.ls.get(sp["Name"], [])) if lv <= level]
    types = [sp["PrimaryType"].split(".")[1]] + ([sp["SecondaryType"].split(".")[1]] if sp["SecondaryType"] else [])
    phys = int(sp["Attack"]) >= int(sp["SpAttack"])
    pref = "Physical" if phys else "Special"

    def dmg_key(a):
        return (int(a["Power"] or 0) * int(a["Accuracy"] or 1000) // 1000 * (1250 if a["Type"] in types else 1000) // 1000
                * (1000 if a["Category"] == pref else 700) // 1000) * 100 // int(a["TimeCost"])

    dmg = [a for a in known if a["Power"] not in ("", "0")]
    out = []
    prim = sorted([a for a in dmg if a["Type"] == types[0]], key=dmg_key, reverse=True)
    if prim:
        out.append(prim[0])
    other = sorted([a for a in dmg if a["Type"] != types[0] and a not in out], key=dmg_key, reverse=True)
    if other:
        out.append(other[0])
    status = [a for a in known if a["Power"] in ("", "0") and a["Target"] not in ("Field",)]
    if status:
        out.append(status[-1])
    rest = sorted([a for a in dmg if a not in out], key=dmg_key, reverse=True)
    out += rest[:4 - len(out)]
    if len(out) < 4:
        out += [a for a in known if a not in out][:4 - len(out)]
    return out


class Fighter:
    def __init__(self, D, sp, level, side):
        self.sp, self.level, self.side = sp, level, side
        self.st = ac.build(sp, level)
        self.hp = self.max_hp = self.st["hp"]
        self.kit = kit(D, sp, level)
        self.stages = {"Attack": 0, "Defense": 0, "SpAttack": 0, "SpDefense": 0, "Speed": 0}
        self.status, self.status_turns, self.poison, self.shield = None, 0, 0, 0
        self.skip = False
        self.cb = ac.Combatant(sp["DisplayName"] + str(side), side, self.st["ges"])


def expected_damage(D, a, user, foe):
    p = int(a["Power"] or 0)
    if not p:
        return 0
    phys = a["Category"] == "Physical"
    atk = user.st["atk" if phys else "sat"]
    dfn = foe.st["def" if phys else "sdf"]
    atk = ac.stage(atk, user.stages["Attack" if phys else "SpAttack"])
    dfn = ac.stage(dfn, foe.stages["Defense" if phys else "SpDefense"])
    if user.status == "Brand" and phys:
        atk = atk * 750 // 1000
    tf = 1000
    for t in foe.st["types"]:
        tf = tf * D.chart[a["Type"]][t] // 1000
    e = ac.EIGENKLANG if a["Type"] in user.st["types"] else 1000
    hits = 1
    for n, args in parse(a["Effects"]):
        if n == "Multi":
            hits = (int(args[0]) + int(args[1])) / 2
    d = ac.damage(p, atk, dfn, user.level, (e, tf))
    acc = int(a["Accuracy"] or 1000) / 1000
    return d * hits * acc


def score(D, a, user, foe, profile):
    """Nutzwert einer Aktion je Zeiteinheit (Ticks). Profile gewichten die Betrachtungen (K34 §3)."""
    w = PROFILES[profile]
    dmg = expected_damage(D, a, user, foe)
    frac = min(1.0, dmg / max(1, foe.hp))
    v = w["damage"] * frac * 100
    if dmg >= foe.hp:
        v += w["kill"]
    for n, args in parse(a["Effects"]):
        if n == "Status" and foe.status is None and args[0] != "Vergiftet":
            v += w["status"] * int(args[1] if len(args) > 1 else 1000) / 1000 * 25
        if n == "Status" and args[0] == "Vergiftet" and foe.poison < 5:
            v += w["status"] * int(args[1] if len(args) > 1 else 1000) / 1000 * 10 * int(args[2] if len(args) > 2 else 1)
        if n == "Stage" and args[0] == "Self" and int(args[2]) > 0 and user.stages.get(args[1], 0) < 2:
            v += w["setup"] * 12 * int(args[2]) * (user.hp / user.max_hp)
        if n == "Stage" and args[0] in ("Target", "Enemies") and int(args[2]) < 0:
            v += w["debuff"] * 8 * -int(args[2])
        if n in ("Heal", "Regen") and args[0] in ("Self", "Ally", "Allies"):
            missing = 1 - user.hp / user.max_hp
            v += w["heal"] * missing * 60
        if n == "Shield" and args[0] in ("Self", "AllyRow", "Allies"):
            v += w["heal"] * 0.4 * int(args[1]) * (1 - user.hp / user.max_hp + 0.3)
        if n == "Delay" and args[0] in ("Target", "Enemies"):
            v += w["tempo"] * int(args[1]) * 0.25
        if n == "Haste" and args[0] in ("Self", "Ally", "Allies"):
            v += w["tempo"] * int(args[1]) * 0.15
    cost = int(a["TimeCost"])
    return v / ac.delay(cost, user.st["ges"]) * 100


PROFILES = {
    "Zufall":   dict(damage=0, kill=0, status=0, setup=0, debuff=0, heal=0, tempo=0, noise=1000),
    "Gierig":   dict(damage=1.0, kill=30, status=0.2, setup=0.0, debuff=0.0, heal=0.2, tempo=0.0, noise=150),
    "Taktiker": dict(damage=1.0, kill=60, status=1.0, setup=0.8, debuff=0.8, heal=1.0, tempo=1.0, noise=50),
    "Meister":  dict(damage=1.0, kill=80, status=1.2, setup=1.0, debuff=1.0, heal=1.2, tempo=1.2, noise=0),
}


def choose(D, user, foe, profile, rng):
    if not user.kit:
        return None
    if rng.chance_permille(PROFILES[profile]["noise"]):
        return user.kit[rng.next_bounded(len(user.kit))]
    best = max(user.kit, key=lambda a: (score(D, a, user, foe, profile), a["Name"]))
    return best


def apply(D, a, user, foe, tl, rng):
    if a is None:
        return
    acc = int(a["Accuracy"] or 0)
    if acc and not rng.chance_permille(acc):
        return
    effs = parse(a["Effects"])
    hits = 1
    for n, args in effs:
        if n == "Multi":
            hits = int(args[0]) + rng.next_bounded(int(args[1]) - int(args[0]) + 1)
    dealt = 0
    for _ in range(hits):
        d = int(expected_damage(D, dict(a, Accuracy="1000", Effects=""), user, foe)) if a["Power"] not in ("", "0") else 0
        if d and rng.chance_permille(42):
            d = d * 1500 // 1000
        absorbed = min(foe.shield, d)
        foe.shield -= absorbed
        foe.hp -= d - absorbed
        dealt += d
    for n, args in effs:
        if n == "Status" and rng.chance_permille(int(args[1]) if len(args) > 1 else 1000):
            s = args[0]
            if s == "Vergiftet":
                foe.poison = min(5, foe.poison + (int(args[2]) if len(args) > 2 else 1))
            elif foe.status is None and s not in IMMUNE.get(foe.st["types"][0], ()):
                foe.status, foe.status_turns = s, 3
                if s == "Starre":
                    foe.skip = True
        elif n == "Stage":
            tgt = user if args[0] in ("Self", "Ally", "Allies", "AllyRow") else foe
            if args[1] in tgt.stages and (len(args) < 4 or rng.chance_permille(int(args[3]))):
                tgt.stages[args[1]] = max(-4, min(4, tgt.stages[args[1]] + int(args[2])))
        elif n == "Delay" and args[0] in ("Target", "Enemies"):
            tl.push_back(foe.cb, int(args[1]))
        elif n == "Haste" and args[0] == "Self":
            pass   # wirkt nach Commit (siehe run_duel)
        elif n in ("Heal",) and args[0] in ("Self", "Ally", "Allies"):
            user.hp = min(user.max_hp, user.hp + user.max_hp * int(args[1]) // 100)
        elif n == "Regen" and args[0] in ("Self", "Ally", "Allies"):
            user.hp = min(user.max_hp, user.hp + user.max_hp * int(args[1]) * int(args[2]) // 200)
        elif n == "Shield" and args[0] in ("Self", "AllyRow", "Allies"):
            user.shield = min(user.max_hp // 2, user.shield + user.max_hp * int(args[1]) // 100)
        elif n == "Drain":
            user.hp = min(user.max_hp, user.hp + dealt * int(args[0]) // 1000)
        elif n == "Recoil":
            user.hp -= dealt * int(args[0]) // 1000


IMMUNE = {"Ember": ("Brand",), "Frost": ("Starre",), "Venom": ("Vergiftet",), "Storm": ("Verlangsamt",)}


def run_duel(D, sa, sb, level, pa, pb, rng):
    A, B = Fighter(D, sa, level, 0), Fighter(D, sb, level, 1)
    tl = ac.Timeline(rng)
    tl.add(A.cb), tl.add(B.cb)
    by = {A.cb.cid: (A, B, pa), B.cb.cid: (B, A, pb)}
    turns = 0
    while A.hp > 0 and B.hp > 0 and turns < 120:
        c = tl.pop()
        me, foe, prof = by[c.cid]
        if me.status in STATUS_DOT:
            me.hp -= me.max_hp * STATUS_DOT[me.status] // 1000
        me.hp -= me.max_hp * 30 * me.poison // 1000
        if me.status:
            me.status_turns -= 1
            if me.status_turns <= 0:
                me.status = None
        if me.hp <= 0:
            break
        if me.skip:
            me.skip = False
            tl.commit(c, 100)
            turns += 1
            continue
        a = choose(D, me, foe, prof, rng)
        apply(D, a, me, foe, tl, rng)
        cost = int(a["TimeCost"]) if a else 100
        tl.commit(c, cost, slowed=me.status == "Verlangsamt")
        for n, args in (parse(a["Effects"]) if a else []):
            if n == "Haste" and args[0] == "Self":
                tl.pull_forward(c, int(args[1]))
        turns += 1
    return 0 if B.hp <= 0 and A.hp > 0 else (1 if A.hp <= 0 and B.hp > 0 else -1), turns


def matrix(n=200, level=30):
    D = Data()
    rng = AethrisRandom(0x34A1, 0x2)
    profs = list(PROFILES)
    out = ["| Profil ↓ gegen → | " + " | ".join(profs) + " |", "|---|" + "---|" * len(profs)]
    for p in profs:
        cells = []
        for q in profs:
            win = tot = 0
            for i in range(n):
                sa = D.sp[rng.next_bounded(len(D.sp))]
                sb = D.sp[rng.next_bounded(len(D.sp))]
                for (x, y, flip) in ((sa, sb, False), (sb, sa, True)):     # gespiegelt gegen Artenvorteil
                    r, _ = run_duel(D, x, y, level, p, q, rng)
                    if r >= 0:
                        tot += 1
                        win += 1 if r == 0 else 0
            cells.append(f"{win * 100 // max(1, tot)} %")
        out.append(f"| **{p}** | " + " | ".join(cells) + " |")
    return "\n".join(out)


def explain():
    D = Data()
    sp = {s["DisplayName"]: s for s in D.sp}
    A, B = Fighter(D, sp["Torgrath"], 40, 0), Fighter(D, sp["Zephyrion"], 40, 1)
    out = [f"Torgrath (Lv. 40, HP {A.hp}) gegen Zephyrion (HP {B.hp}); Profil Taktiker", "",
           "| Fähigkeit | erw. Schaden | % Ziel-HP | Zeitkosten | Verzögerung | Nutzwert/100 Ticks |", "|---|---|---|---|---|---|"]
    for a in A.kit:
        d = expected_damage(D, a, A, B)
        out.append(f"| {a['DisplayName']} | {d:.0f} | {d * 100 / B.hp:.0f} % | {a['TimeCost']} | {ac.delay(int(a['TimeCost']), A.st['ges'])} | "
                   f"{score(D, a, A, B, 'Taktiker'):.1f} |".replace(".", ","))
    return "\n".join(out)


def kit_learnset(D, sp, level):
    known = [a for lv, a in sorted(D.ls.get(sp["Name"], [])) if lv <= level]
    return [D.ab[a] for a in known[-4:]]


def kit_table():
    D = Data()
    sp = {s["DisplayName"]: s for s in D.sp}
    cases = [("Fernwyn", 20), ("Torgrath", 40), ("Zephyrion", 40), ("Cragar", 25), ("Undrath", 38), ("Irraune", 40),
             ("Maraune", 45), ("Solaryx", 45), ("Pyroluth", 48), ("Ambross", 50), ("Kjalgrund", 55), ("Uvasil", 55),
             ("Skriveth", 58), ("Ligravor", 60), ("Klirrathan", 62), ("Nimbaroth", 66)]
    out = ["| Art (Lv.) | Learnset (letzte 4) | Best (K34 §6.1) |", "|---|---|---|"]
    for n, lv in cases:
        if n not in sp:
            continue
        a = ", ".join(x["DisplayName"] for x in kit_learnset(D, sp[n], lv))
        b = ", ".join(x["DisplayName"] for x in kit(D, sp[n], lv))
        out.append(f"| {n} ({lv}) | {a} | {b} |")
    return "\n".join(out)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "matrix"
    if cmd == "matrix":
        print(matrix(int(sys.argv[2]) if len(sys.argv) > 2 else 150))
    else:
        print(explain())
