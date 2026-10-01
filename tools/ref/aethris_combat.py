#!/usr/bin/env python3
"""Referenz-Kampfmodell (K31 Zeitleiste, K32 Schaden) – ganzzahlig, deterministisch, bitgleich zu GF_Combat.

Enthält:
  delay(cost, ges)                 Zeitleisten-Verzögerung (K31 §3)
  Timeline                         Ereignis-Warteschlange mit Ticks, Gleichstand, Haste/Delay-Deckel, Vorgriff
  damage(...)                      Schadensformel (K32 §2)
  simulate_duel(...)               Monte-Carlo-Duelle für Balancing-Berichte (K31 §9, K32 §9, K63)
Aufruf: aethris_combat.py report   -> Kennzahlen-Tabellen (Kampfdauern je Level/Format)
"""
from __future__ import annotations
import csv, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aethris_random import AethrisRandom
import aethris_stats as st

ROOT = pathlib.Path(__file__).resolve().parents[2]

# ── K31: Zeitleiste ─────────────────────────────────────────────────────────────
DELAY_NUM, DELAY_OFFSET, MIN_DELAY = 300, 200, 10
EXTERNAL_DELAY_CAP = 100        # max. fremde Verzögerung zwischen zwei eigenen Zügen (Anti-Frost-Lock)
VORGRIFF_PER_PRIORITY = 25      # Ticks Vorgriff je Prioritätsstufe
ROUND_TICKS = 100               # globale Runde (Terrain/Wetter-Dauer)
SWITCH_COST = 60
CHARGE_RECOVERY_COST = 50


def delay(cost: int, ges: int) -> int:
    """Verzögerung in Ticks = ⌊Zeitkosten × 300 / (GES_eff + 200)⌋, mindestens 10."""
    return max(MIN_DELAY, cost * DELAY_NUM // (max(1, ges) + DELAY_OFFSET))


def start_tick(ges: int, rng: AethrisRandom, ambush: bool = False) -> int:
    """Erster Zug: Verzögerung einer Standardaktion × 850–1000 ‰ (gedeckelter Zufall, DR-07); Hinterhalt −200 ‰."""
    j = rng.range_inclusive(850, 1000) - (200 if ambush else 0)
    return max(1, delay(100, ges) * j // 1000)


class Combatant:
    def __init__(self, cid, side, ges):
        self.cid, self.side, self.ges = cid, side, ges
        self.next = 0
        self.ext_delay = 0          # seit dem letzten eigenen Zug erlittene Fremdverzögerung
        self.speed_stage = 0
        self.alive = True

    def ges_eff(self):
        return st.apply_stage(self.ges, self.speed_stage, False) if hasattr(st, "apply_stage") else self.ges


class Timeline:
    """Ereignisliste nach Tick; Gleichstand: höhere GES, dann Seitenwechsel, dann Zufall (PCG)."""

    def __init__(self, rng: AethrisRandom):
        self.rng, self.now, self.cs, self.last_side = rng, 0, [], None

    def add(self, c: Combatant, ambush=False):
        c.next = self.now + start_tick(c.ges, self.rng, ambush)
        self.cs.append(c)

    def pop(self) -> Combatant:
        alive = [c for c in self.cs if c.alive]
        t = min(c.next for c in alive)
        tied = [c for c in alive if c.next == t]
        tied.sort(key=lambda c: (-c.ges, c.side == self.last_side))   # stabil, wie TArray::Sort mit gleicher Ordnung
        eq = [x for x in tied if x.ges == tied[0].ges and (x.side == self.last_side) == (tied[0].side == self.last_side)]
        c = eq[self.rng.next_bounded(len(eq))] if len(eq) > 1 else tied[0]
        self.now, self.last_side = t, c.side
        c.ext_delay = 0
        return c

    def commit(self, c: Combatant, cost: int, slowed=False, cursed=False):
        eff = cost * 13 // 10 if slowed else cost
        eff += 20 if cursed else 0
        c.next = self.now + delay(eff, c.ges)

    def push_back(self, c: Combatant, ticks: int):
        """Fremdverzögerung (Frost/Klang): gedeckelt auf EXTERNAL_DELAY_CAP zwischen zwei eigenen Zügen."""
        room = max(0, EXTERNAL_DELAY_CAP - c.ext_delay)
        d = min(ticks, room)
        c.next += d
        c.ext_delay += d
        return d

    def pull_forward(self, c: Combatant, ticks: int):
        c.next = max(self.now + 1, c.next - ticks)

    def preview(self, n=8):
        """Die nächsten n Züge (DR-06) – Projektion ohne Zustandsänderung (Wiederholung über Standardkosten 100)."""
        sim = [(c.next, -c.ges, c.cid, c.ges) for c in self.cs if c.alive]
        out = []
        while len(out) < n:
            sim.sort()
            t, g, cid, ges = sim[0]
            out.append((t, cid))
            sim[0] = (t + delay(100, ges), g, cid, ges)
        return out


# ── K32: Schaden ────────────────────────────────────────────────────────────────
DMG_DIV = 180
CRIT_PERMILLE = [42, 125, 250, 500]   # Volltreffer-Chance je Stufe 0..3
CRIT_MULT = 1500
EIGENKLANG = 1250


def damage(power, atk, dfn, level, mods=()):
    """Basis = ⌊Stärke × A × (L+10) / (V × 180)⌋ + 2; danach Promille-Faktoren in fester Reihenfolge (CANON §77)."""
    base = power * atk * (level + 10) // (max(1, dfn) * DMG_DIV) + 2
    for m in mods:
        base = base * m // 1000
    return max(1, base)


# ── Simulation ─────────────────────────────────────────────────────────────────
def load_species():
    return [r for r in csv.DictReader(open(ROOT / "Data/Echos/Species.csv", encoding="utf-8"))]


def load_chart():
    rows = [r for r in csv.DictReader(l for l in open(ROOT / "Data/Combat/TypeChart.csv", encoding="utf-8") if not l.startswith("#"))]
    return {r["Name"]: {k: int(v) for k, v in r.items() if k != "Name"} for r in rows}


def build(sp, level, apt=7):
    b = {k: int(sp[k]) for k in ("HP", "Attack", "Defense", "SpAttack", "SpDefense", "Speed")}
    return {"hp": st.hp(b["HP"], level, apt), "atk": st.core(b["Attack"], level, apt), "def": st.core(b["Defense"], level, apt),
            "sat": st.core(b["SpAttack"], level, apt), "sdf": st.core(b["SpDefense"], level, apt),
            "ges": st.core(b["Speed"], level, apt),
            "types": [sp["PrimaryType"].split(".")[1]] + ([sp["SecondaryType"].split(".")[1]] if sp["SecondaryType"] else [])}


def simulate_duel(a_sp, b_sp, level, chart, rng, power=70, cost=100):
    """1v1 mit je einer Standardfähigkeit (Stärke 70, Kosten 100) in der jeweils besseren Kategorie und Eigenklang."""
    A, B = build(a_sp, level), build(b_sp, level)
    tl = Timeline(rng)
    ca, cb = Combatant("A", 0, A["ges"]), Combatant("B", 1, B["ges"])
    tl.add(ca), tl.add(cb)
    hp = {"A": A["hp"], "B": B["hp"]}
    stats = {"A": A, "B": B}
    turns = 0
    while hp["A"] > 0 and hp["B"] > 0 and turns < 200:
        c = tl.pop()
        me, foe = stats[c.cid], stats["B" if c.cid == "A" else "A"]
        phys = me["atk"] >= me["sat"]
        atk, dfn = (me["atk"], foe["def"]) if phys else (me["sat"], foe["sdf"])
        t = me["types"][0]
        tf = 1000
        for ft in foe["types"]:
            tf = tf * chart[t][ft] // 1000
        crit = CRIT_MULT if rng.chance_permille(CRIT_PERMILLE[0]) else 1000
        d = damage(power, atk, dfn, level, (EIGENKLANG, tf, crit))
        if rng.chance_permille(950):
            hp["B" if c.cid == "A" else "A"] -= d
        tl.commit(c, cost)
        turns += 1
    return turns, tl.now, ("A" if hp["B"] <= 0 else "B")


def report_levels(n=400):
    sp = [s for s in load_species() if s["LineKind"] not in ("Legendary", "Mythical")]
    chart = load_chart()
    rng = AethrisRandom(0xA37B, 0x51)
    out = ["| Level | Ø Züge gesamt (1v1) | Median | P90 | Ø Ticks | Ø Dauer bei 7 s/Zug |", "|---|---|---|---|---|---|"]
    for level in (5, 10, 20, 35, 50, 70, 100):
        res = []
        for i in range(n):
            a = sp[rng.next_bounded(len(sp))]
            b = sp[rng.next_bounded(len(sp))]
            res.append(simulate_duel(a, b, level, chart, rng))
        tt = sorted(r[0] for r in res)
        avg = sum(tt) / len(tt)
        out.append(f"| {level} | {avg:.1f} | {tt[len(tt) // 2]} | {tt[int(len(tt) * 0.9)]} | {sum(r[1] for r in res) // len(res)} | {avg * 7:.0f} s |".replace(".", ","))
    return "\n".join(out)


def report_speed():
    out = ["| GES_eff | Verzögerung bei Kosten 50 / 100 / 150 / 200 | Züge je 1.000 Ticks (Kosten 100) |", "|---|---|---|"]
    for g in (30, 60, 100, 150, 200, 300, 394):
        out.append(f"| {g} | {delay(50, g)} / {delay(100, g)} / {delay(150, g)} / {delay(200, g)} | {1000 / delay(100, g):.1f} |".replace(".", ","))
    return "\n".join(out)


def report_matrix():
    gs = (30, 45, 60, 80, 100, 125, 150, 200, 250, 300, 394)
    out = ["| Zeitkosten \\ GES_eff | " + " | ".join(map(str, gs)) + " |", "|---|" + "---|" * len(gs)]
    for cost in range(50, 210, 10):
        out.append(f"| {cost} | " + " | ".join(str(delay(cost, g)) for g in gs) + " |")
    return "\n".join(out)


# ── K32: vollständige Schadenskette ─────────────────────────────────────────────
STAGE_CORE = [500, 571, 667, 800, 1000, 1250, 1500, 1750, 2000]


def stage(v, st_):
    return v * STAGE_CORE[max(-4, min(4, st_)) + 4] // 1000


def load_weather():
    rows = [r for r in csv.DictReader(l for l in open(ROOT / "Data/World/WeatherTypeResonance.csv", encoding="utf-8") if not l.startswith("#"))]
    out = {}
    for r in rows:
        m = {}
        for k in ("Boost1", "Boost2", "Boost3", "Malus1", "Malus2"):
            if r[k]:
                m[r[k].split(".")[1]] = int(r[k + "Permille"])
        out[r["Name"]] = m
    return out


WEATHER_ID = {"Clear": "W01", "Rain": "W02", "Thunderstorm": "W03", "Fog": "W04", "Snow": "W05", "Heatwave": "W06",
              "Sandstorm": "W07", "Aurora": "W08", "Ashfall": "W09", "ResonanceStorm": "W10"}


def damage_chain(power, category, ab_type, user, target, level, chart, weather=None, crit=False, a_stage=0, d_stage=0,
                 burned=False, formation=1000, other=(), eigenklang=EIGENKLANG):
    """Gibt (Endschaden, Schritte) zurück. Reihenfolge CANON §77: Basis × Eigenklang × Typ × Wetter × Krit × Formation × Sonstige."""
    if category == "Physical":
        a, d = user["atk"], target["def"]
    else:
        a, d = user["sat"], target["sdf"]
    if crit:                       # Volltreffer ignoriert ungünstige Stufen
        a_stage, d_stage = max(0, a_stage), min(0, d_stage)
    a, d = stage(a, a_stage), stage(d, d_stage)
    if burned and category == "Physical":
        a = a * 750 // 1000
    base = power * a * (level + 10) // (max(1, d) * DMG_DIV) + 2
    steps = [("Basis", base)]
    v = base
    if ab_type in user["types"]:
        v = v * eigenklang // 1000
    steps.append(("Eigenklang", v))
    tf = 1000
    for t in target["types"]:
        tf = tf * chart[ab_type][t] // 1000
    v = v * tf // 1000
    steps.append((f"Typ {tf}‰", v))
    wf = 1000
    if weather:
        wf = load_weather()[WEATHER_ID[weather]].get(ab_type, 1000)
    v = v * wf // 1000
    steps.append((f"Wetter {wf}‰", v))
    v = v * (CRIT_MULT if crit else 1000) // 1000
    steps.append(("Krit" if crit else "kein Krit", v))
    v = v * formation // 1000
    steps.append((f"Formation {formation}‰", v))
    for o in other:
        v = v * o // 1000
    steps.append(("Sonstige", v))
    return max(1, v), steps


def example_table():
    sp = {r["DisplayName"]: r for r in load_species()}
    ab = {r["DisplayName"]: r for r in csv.DictReader(open(ROOT / "Data/Abilities/Abilities.csv", encoding="utf-8"))}
    chart = load_chart()
    cases = [("Fernwyn", "Saugwurzel", "Brokkar", 20, None, False, 1000, ()),
             ("Torgrath", "Felsrammen", "Zephyrion", 36, None, False, 1000, ()),
             ("Sengrath", "Esseneruption", "Kjalmur", 50, "Heatwave", False, 1000, ()),
             ("Klirrathan", "Prismenfächer", "Uvasil", 60, None, True, 1000, ()),
             ("Nimbaroth", "Himmelszorn", "Ignavor", 70, "Thunderstorm", False, 1000, ()),
             ("Snevrik", "Frostbiss", "Solaryx", 45, "Snow", False, 750, ()),
             ("Tilgrath", "Hohlklang", "Thaelarch", 55, "Fog", False, 1000, ()),
             ("Pyroluth", "Feueratem", "Nubiluna", 40, "Rain", False, 1000, (800,))]
    out = ["| Angreifer → Ziel (Lv.) | Fähigkeit (Stärke, Kat.) | Basis | ×Eigenklang | ×Typ | ×Wetter | ×Krit | ×Formation | ×Sonstige | Schaden | % Ziel-HP |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for (u, a, t, lv, w, cr, form, oth) in cases:
        U, T, A = build(sp[u], lv), build(sp[t], lv), ab[a]
        dmg, steps = damage_chain(int(A["Power"]), A["Category"], A["Type"], U, T, lv, chart, w, cr, formation=form, other=oth)
        sv = [str(x[1]) for x in steps]
        out.append(f"| {u} → {t} ({lv}) | {a} ({A['Power']}, {A['Category'][:4]}.) | " + " | ".join(sv[:1]) + " | " +
                   " | ".join(f"{steps[i][0].split()[-1] if '‰' in steps[i][0] else ''} → {sv[i]}".strip() for i in range(1, 7)) +
                   f" | **{dmg}** | {dmg * 100 // T['hp']} % |")
    return "\n".join(out)


def sample_log():
    """Durchgerechnetes Duo-Beispiel (K31 §13.2): Wisplet & Brokkar gegen Uvlet & Kharsgrat-Spinne (Ligrel)."""
    rng = AethrisRandom(0xC31, 0x7)
    tl = Timeline(rng)
    team = [("Wisplet", 0, 74), ("Brokkar", 0, 41), ("Uvlet", 1, 58), ("Ligrel", 1, 52)]
    cs = {n: Combatant(n, side, g) for n, side, g in team}
    for c in cs.values():
        tl.add(c)
    plan = {"Wisplet": [("Böenhieb", 60, None), ("Klingenwind", 60, None), ("Böenchor", 50, ("haste_allies", 50)), ("Böenhieb", 60, None)],
            "Brokkar": [("Steinhaut", 60, None), ("Felsrammen", 80, ("erschuettert", "Uvlet")), ("Kieselwurf", 60, None)],
            "Uvlet": [("Raureifhauch", 60, ("delay", "Wisplet", 20)), ("Frostbiss", 80, None), ("Raureifhauch", 60, ("delay", "Brokkar", 20))],
            "Ligrel": [("Massezug", 90, ("pull", "Brokkar")), ("Gewichtslast", 60, None), ("Schwerefaust", 60, None)]}
    idx = {n: 0 for n in cs}
    out = ["| # | Tick | Echo | Aktion (Kosten) | Wirkung auf die Zeitleiste | Nächster Zug |", "|---|---|---|---|---|---|"]
    for i in range(14):
        c = tl.pop()
        name, cost, eff = plan[c.cid][idx[c.cid] % len(plan[c.cid])]
        idx[c.cid] += 1
        note = "–"
        if eff:
            if eff[0] == "delay":
                d = tl.push_back(cs[eff[1]], eff[2])
                note = f"{eff[1]} +{d} Ticks → {cs[eff[1]].next}"
            elif eff[0] == "erschuettert":
                d = tl.push_back(cs[eff[1]], 50)
                note = f"{eff[1]} erschüttert: +{d} → {cs[eff[1]].next}"
            elif eff[0] == "haste_allies":
                for o in cs.values():
                    if o.side == c.side and o is not c:
                        tl.pull_forward(o, eff[1])
                        note = f"{o.cid} −{eff[1]} Ticks → {o.next}"
            elif eff[0] == "pull":
                note = f"{eff[1]} in die Vorderreihe (K33)"
        tl.commit(c, cost)
        out.append(f"| {i + 1} | {tl.now} | {c.cid} | {name} ({cost}) | {note} | {c.next} |")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "report":
        print(report_levels())
        print()
        print(report_speed())
    else:
        assert delay(100, 100) == 100 and delay(100, 394) == 50 and delay(200, 1) == 298
        assert damage(80, 87, 87, 50) == 28
        print("ok")
