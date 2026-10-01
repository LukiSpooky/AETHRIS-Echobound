#!/usr/bin/env python3
"""Erzeugt und bewertet die Typtabelle (K17). Quelle der Design-Absicht sind die Dicts unten;
Ausgabe: Data/Combat/TypeChart.csv (Promille, Angreifer-Zeile × Verteidiger-Spalte) + Balance-Bericht.
Stufen: 1600 sehr effektiv · 1000 neutral · 625 resistent · 400 gedämpft (keine Immunität, DR-07/DR-10)."""
import csv, pathlib, itertools, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
T = ["Ember","Tide","Stone","Storm","Bloom","Frost","Void","Light","Venom","Metal","Spirit","Crystal","Sound","Gravity","Arcane"]
DE = dict(zip(T,["Glut","Flut","Stein","Sturm","Blüte","Frost","Leere","Licht","Gift","Metall","Geist","Kristall","Klang","Schwerkraft","Arkan"]))
SE = {  # Angreifer -> sehr effektiv gegen
 "Ember":["Bloom","Frost","Metal"], "Tide":["Ember","Stone","Venom"], "Stone":["Storm","Ember","Frost"],
 "Storm":["Bloom","Tide","Sound"], "Bloom":["Stone","Tide","Void"], "Frost":["Bloom","Storm","Venom"],
 "Void":["Light","Sound","Arcane"], "Light":["Void","Spirit","Venom"], "Venom":["Bloom","Tide","Metal"],
 "Metal":["Stone","Crystal","Frost"], "Spirit":["Spirit","Arcane","Gravity"], "Crystal":["Light","Void","Spirit"],
 "Sound":["Crystal","Stone","Metal"], "Gravity":["Storm","Metal","Crystal"], "Arcane":["Gravity","Crystal","Arcane"]}
RES = {  # Angreifer -> resistiert von (625)
 "Ember":["Tide","Stone","Ember"], "Tide":["Bloom","Tide","Frost"], "Stone":["Bloom","Metal","Gravity","Spirit"],
 "Storm":["Crystal","Storm","Frost"], "Bloom":["Ember","Venom","Storm"], "Frost":["Ember","Metal","Frost","Sound"],
 "Void":["Bloom","Gravity"], "Light":["Crystal","Light","Metal"], "Venom":["Venom","Stone","Crystal","Storm","Spirit"],
 "Metal":["Tide","Metal"], "Spirit":["Light","Stone","Void"], "Crystal":["Crystal","Metal"],
 "Sound":["Sound","Bloom","Arcane","Venom"], "Gravity":["Gravity","Arcane"], "Arcane":["Metal","Stone","Void"]}
DAMP = {"Storm":["Stone"], "Void":["Void"], "Sound":["Void"], "Gravity":["Spirit"]}  # 400

def chart():
    m = {a:{d:1000 for d in T} for a in T}
    for a,ds in SE.items():
        for d in ds: m[a][d]=1600
    for a,ds in RES.items():
        for d in ds:
            assert m[a][d]==1000, (a,d,"Konflikt SE/RES"); m[a][d]=625
    for a,ds in DAMP.items():
        for d in ds:
            assert m[a][d]==1000, (a,d,"Konflikt DAMP"); m[a][d]=400
    return m

def report(m):
    print(f"{'Typ':12} offSE offRes  defWeak defRes | offEV  defEV")
    rows=[]
    for t in T:
        offse=sum(1 for d in T if m[t][d]==1600); offre=sum(1 for d in T if m[t][d]<1000)
        defwk=sum(1 for a in T if m[a][t]==1600); defre=sum(1 for a in T if m[a][t]<1000)
        offev=sum(m[t][d] for d in T)/len(T)/1000; defev=sum(m[a][t] for a in T)/len(T)/1000
        rows.append((t,offse,offre,defwk,defre,offev,defev))
        print(f"{DE[t]:12} {offse:5} {offre:6}  {defwk:7} {defre:6} | {offev:.3f}  {defev:.3f}")
    # Dual-Typ-Abdeckung: Anteil Typkombinationen, die von jedem Angriffstyp neutral+ getroffen werden
    return rows

if __name__=="__main__":
    m=chart(); r=report(m)
    # Starter-Zyklus prüfen (CANON §14)
    assert m["Bloom"]["Stone"]==1600 and m["Stone"]["Storm"]==1600 and m["Storm"]["Bloom"]==1600, "Starter-Zyklus verletzt"
    assert m["Stone"]["Bloom"]<1000 and m["Storm"]["Stone"]<1000 and m["Bloom"]["Storm"]<1000, "Starter-Rückrichtung muss resistiert sein"
    offs=[x[5] for x in r]; defs=[x[6] for x in r]
    print(f"\nOffensiv-EV Spanne {min(offs):.3f}–{max(offs):.3f}; Defensiv-EV Spanne {min(defs):.3f}–{max(defs):.3f}")
    out=ROOT/"Data/Combat/TypeChart.csv"
    with open(out,"w",newline="",encoding="utf-8") as f:
        f.write("# Typtabelle (K17): Zeile = Typ der Fähigkeit (Angreifer), Spalte = Typ des Ziels. Promille. Generiert von tools/build_typechart.py.\n")
        w=csv.writer(f); w.writerow(["Name"]+T)
        for a in T: w.writerow([a]+[m[a][d] for d in T])
