#!/usr/bin/env python3
"""Referenzimplementierung der Statusformeln (K18). Ganzzahlig, identisch zu FEchoStatCalculator (C++).

HP     = ⌊ B·(L+10)·(1000+10·A) / (40·1000) ⌋ + L + 12 + S
Kern   = ⌊ ⌊ B·(L+10)·(1000+10·A) / (55·1000) ⌋ · P / 1000 ⌋ + ⌊S/2⌋        (P = 1100 bei Persönlichkeits-Stat, sonst 1000)
PRÄ/AUS= B + ⌊A/3⌋ (+50 bei Persönlichkeits-Stat → wirkt als Prozentpunkt-Bonus von +5 % auf die Quote)
B Basiswert, L Level 1..100, A Anlage 0..15, S Schliff 0..80 (Summe ≤ 240).
"""
def hp(B, L, A=0, S=0):
    return B * (L + 10) * (1000 + 10 * A) // (40 * 1000) + L + 12 + S

def core(B, L, A=0, S=0, boosted=False):
    v = B * (L + 10) * (1000 + 10 * A) // (55 * 1000)
    return v * (1100 if boosted else 1000) // 1000 + S // 2

def secondary(B, A=0, boosted=False):
    return B + A // 3 + (5 if boosted else 0)

# Wachstumskurven: Gesamt-EP bis Level L (K18 §6)
import math
def exp_total(curve, L):
    if L <= 1: return 0
    if curve == "Swift":  return int(0.6 * L ** 3)
    if curve == "Steady": return int(0.8 * L ** 3)
    if curve == "Late":   return int(L ** 3 * (0.45 + 0.65 * L / 100))
    if curve == "Wave":   return int(L ** 3 * (0.8 + 0.08 * math.sin(L / 6.0)))
    raise ValueError(curve)

STAGES = {-4: 500, -3: 571, -2: 667, -1: 800, 0: 1000, 1: 1250, 2: 1500, 3: 1750, 4: 2000}
ACC_STAGES = {-4: 700, -3: 775, -2: 850, -1: 925, 0: 1000, 1: 1075, 2: 1150, 3: 1225, 4: 1300}

def hit_chance_permille(ability_acc, prec, eva, prec_stage=0, eva_stage=0):
    """Trefferchance (K18 §3.3): Fähigkeitsgenauigkeit × (PRÄ_eff / AUS_eff), gedeckelt 500..1000 (DR-07)."""
    p = prec * ACC_STAGES[prec_stage] // 1000
    e = eva * ACC_STAGES[eva_stage] // 1000
    return max(500, min(1000, ability_acc * p // e))

if __name__ == "__main__":
    for c in ("Swift", "Steady", "Late", "Wave"):
        vals = [exp_total(c, L) for L in range(1, 101)]
        assert all(b > a for a, b in zip(vals[1:], vals[2:])), f"{c} nicht monoton"
        print(f"{c:7} L10 {exp_total(c,10):>8,} L30 {exp_total(c,30):>9,} L50 {exp_total(c,50):>9,} L70 {exp_total(c,70):>10,} L100 {exp_total(c,100):>10,}")
    # Beispiel Fernlit (48/42/50/55/58/47), Anlage 7, kein Schliff
    B = dict(HP=48, ANG=42, VER=50, SAN=55, SVE=58, GES=47)
    for L in (5, 16, 50):
        print(f"Fernlit L{L}: HP {hp(B['HP'],L,7)} " + " ".join(f"{k} {core(v,L,7)}" for k, v in B.items() if k != 'HP'))
    # Grenzwerte: Basis 140, L100, A15, S80, Persönlichkeit
    print("Max Kern (B140,L100,A15,S80,P):", core(140, 100, 15, 80, True), "| Max HP (B160):", hp(160, 100, 15, 80))
    print("Trefferchance Beispiele:", hit_chance_permille(950, 100, 100), hit_chance_permille(950, 100, 120), hit_chance_permille(800, 90, 120, 0, 4))
