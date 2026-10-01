#!/usr/bin/env python3
"""Parser + Auswerter der Evolutions-Bedingungssprache (K19 §4). Referenz für den C++-Parser.

Grammatik (EBNF):
  expr    := term { '|' term }
  term    := factor { '&' factor }
  factor  := '!' factor | '(' expr ')' | atom
  atom    := KEY OP VALUE
  KEY     := Level | BondTier | Item | TimeOfDay | Weather | Zone | Region | Moon | Knows | ChorHas
             | Personality | Temperament | WinsWhileHolding | StepsInRegion | Stat
  OP      := '>=' | '<=' | '=' | '>' | '<'
Beispiele:
  Level>=16
  Level>=30 & Weather=Rain
  BondTier>=4 & TimeOfDay=Night
  Item=ITM_EVO_TIDE | (Level>=40 & Zone=R06_Z05)
  Stat:Attack>Defense & Level>=28
"""
import re

KEYS = {"Level", "BondTier", "Item", "TimeOfDay", "Weather", "Zone", "Region", "Moon", "Knows", "ChorHas",
        "Personality", "Temperament", "WinsWhileHolding", "StepsInRegion", "Stat"}
NUMERIC = {"Level", "BondTier", "WinsWhileHolding", "StepsInRegion"}
TOKEN = re.compile(r"\s*(>=|<=|[()&|!=<>]|Stat:[A-Za-z]+|[A-Za-z_][A-Za-z0-9_.]*|\d+)")

class ParseError(Exception):
    pass

def tokenize(s):
    pos, out = 0, []
    s = s.strip()
    while pos < len(s):
        m = TOKEN.match(s, pos)
        if not m:
            raise ParseError(f"Unerwartetes Zeichen bei {pos}: '{s[pos:]}'")
        out.append(m.group(1)); pos = m.end()
    return out

def parse(s):
    toks = tokenize(s); i = 0
    def peek(): return toks[i] if i < len(toks) else None
    def take(x=None):
        nonlocal i
        t = peek()
        if x is not None and t != x: raise ParseError(f"Erwartet '{x}', gefunden '{t}'")
        i += 1; return t
    def expr():
        node = term()
        while peek() == "|": take("|"); node = ("or", node, term())
        return node
    def term():
        node = factor()
        while peek() == "&": take("&"); node = ("and", node, factor())
        return node
    def factor():
        t = peek()
        if t == "!": take(); return ("not", factor())
        if t == "(":
            take("("); n = expr(); take(")"); return n
        return atom()
    def atom():
        key = take()
        stat = None
        if key and key.startswith("Stat:"):
            stat, key = key[5:], "Stat"
        if key not in KEYS: raise ParseError(f"Unbekannter Schlüssel '{key}'")
        op = take()
        if op not in (">=", "<=", "=", ">", "<"): raise ParseError(f"Operator erwartet, gefunden '{op}'")
        val = take()
        if val is None: raise ParseError("Wert fehlt")
        if key in NUMERIC and not val.isdigit(): raise ParseError(f"{key} braucht Zahl")
        if key not in NUMERIC and key != "Stat" and op != "=": raise ParseError(f"{key} erlaubt nur '='")
        return ("atom", key, op, val, stat)
    node = expr()
    if peek() is not None: raise ParseError(f"Unerwartetes Token '{peek()}'")
    return node

def atoms(node):
    if node[0] == "atom": yield node
    elif node[0] == "not": yield from atoms(node[1])
    else:
        yield from atoms(node[1]); yield from atoms(node[2])

def evaluate(node, ctx):
    """ctx: dict mit Level, BondTier, Items(set), TimeOfDay, Weather, Zone, Region, Moon, Knows(set), ChorTypes(set), ..."""
    k = node[0]
    if k == "or": return evaluate(node[1], ctx) or evaluate(node[2], ctx)
    if k == "and": return evaluate(node[1], ctx) and evaluate(node[2], ctx)
    if k == "not": return not evaluate(node[1], ctx)
    _, key, op, val, stat = node
    cmp = {">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b, "=": lambda a, b: a == b, ">": lambda a, b: a > b, "<": lambda a, b: a < b}[op]
    if key in NUMERIC: return cmp(int(ctx.get(key, 0)), int(val))
    if key == "Item": return val in ctx.get("Items", set())
    if key == "Knows": return val in ctx.get("Knows", set())
    if key == "ChorHas": return val in ctx.get("ChorTypes", set())
    if key == "Stat": return cmp(int(ctx["Stats"][stat]), int(ctx["Stats"][val]))
    return ctx.get(key) == val

if __name__ == "__main__":
    tests = ["Level>=16", "Level>=30 & Weather=Rain", "BondTier>=4 & TimeOfDay=Night",
             "Item=ITM_EVO_TIDE | (Level>=40 & Zone=R06_Z05)", "Stat:Attack>Defense & Level>=28", "!(Moon=NewMoon) & Level>=22"]
    ctx = dict(Level=30, Weather="Rain", BondTier=4, TimeOfDay="Night", Items={"ITM_EVO_TIDE"}, Zone="R06_Z05",
               Moon="FullMoon", Stats={"Attack": 80, "Defense": 70})
    for t in tests:
        print(f"{t:55} → {evaluate(parse(t), ctx)}")
    for bad in ["Level>16 &", "Weather>=Rain", "Foo=1", "Level>=x"]:
        try: parse(bad); print("FEHLT FEHLER:", bad)
        except ParseError as e: print(f"{bad:20} ✗ {e}")
