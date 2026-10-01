#!/usr/bin/env python3
"""Referenz für FAethrisFixed (Q16.16). Erzeugt die Exp2-Tabelle und prüft Log2/Exp2/Pow."""
import math
ONE = 1 << 16

def table():
    return [round(2 ** (2 ** -(k + 1)) * ONE) for k in range(16)]

TABLE = table()

def log2(raw):
    v, ip = raw, 0
    while v >= 2 * ONE: v >>= 1; ip += 1
    while v < ONE: v <<= 1; ip -= 1
    frac = 0
    for bit in range(15, -1, -1):
        v = (v * v) >> 16
        if v >= 2 * ONE:
            v >>= 1; frac |= 1 << bit
    return ip * ONE + frac

def exp2(raw):
    ip, frac = raw >> 16, raw & (ONE - 1)
    res = ONE
    for k in range(16):
        if frac & (1 << (15 - k)):
            res = (res * TABLE[k]) >> 16
    return res << ip if ip >= 0 else res >> -ip

def mul(a, b): return (a * b) >> 16

def pow_(b, e): return exp2(mul(e, log2(b)))

if __name__ == "__main__":
    print("Tabelle:", TABLE)
    for base, ex in [(2.0, 0.85), (0.5, 0.85), (1.6, 0.85), (3.0, 0.5)]:
        got = pow_(round(base * ONE), round(ex * ONE)) / ONE
        print(f"{base}^{ex}: fixed={got:.5f} float={base**ex:.5f} err={abs(got-base**ex):.5f}")
