#!/usr/bin/env python3
"""Prüft die Schichtenregel aus K01 §13.2 / K05 §4 für alle Projektmodule.

Schichten (unten -> oben): Core < Game < Domain < Feature < Presentation; Editor darf alles.
Regeln:
  R1  Core hängt von keinem Projektmodul ab.
  R2  Game hängt nur von Core ab.
  R3  Domain hängt nur von Core ab (Domain-Module kennen sich nicht gegenseitig).
  R4  Feature hängt nur von Core + Domain ab – NIE von anderen Features (nur Event-Bus/Interfaces).
  R5  Presentation hängt von Core, Domain, Feature ab (nur lesend über ViewModels/Events).
  R6  Keine Laufzeitmodule hängen von Editor-Modulen ab.
Zusätzlich werden #include-Pfade in Feature-Plugins auf fremde Feature-Header geprüft.
Exitcode 1 bei Verstößen (CI-Gate, K05 §7).
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEP_RE = re.compile(r'DependencyModuleNames\.AddRange\(\s*new\s+string\[\]\s*\{(.*?)\}', re.S)

def module_layers():
    layers = {"AethrisCore": "Core", "AethrisGame": "Game", "AethrisEditor": "Editor"}
    for up in ROOT.glob("Plugins/GameFeatures/*/*.uplugin"):
        layers[up.stem] = json.loads(up.read_text())["AethrisLayer"]
    return layers

def build_files():
    yield from ROOT.glob("Source/*/*.Build.cs")
    yield from ROOT.glob("Plugins/GameFeatures/*/Source/*/*.Build.cs")

ALLOWED = {
    "Core": set(),
    "Game": {"Core"},
    "Domain": {"Core"},
    "Feature": {"Core", "Domain"},
    "Presentation": {"Core", "Domain", "Feature"},
    "Editor": {"Core", "Game", "Domain", "Feature", "Presentation"},
}

def main() -> int:
    layers = module_layers()
    errors = []
    for bf in build_files():
        mod = bf.name.removesuffix(".Build.cs")
        layer = layers.get(mod)
        deps = set()
        for block in DEP_RE.findall(bf.read_text()):
            deps |= set(re.findall(r'"([^"]+)"', block))
        for d in sorted(deps):
            if d not in layers or d == mod:
                continue  # Engine-Modul
            if layers[d] not in ALLOWED[layer]:
                errors.append(f"{mod} ({layer}) -> {d} ({layers[d]}) verletzt Schichtenregel")
    features = {m for m, l in layers.items() if l == "Feature"}
    for f in features:
        for src in (ROOT / "Plugins/GameFeatures" / f).rglob("*.[hc]*"):
            for inc in re.findall(r'#include\s+"([^"]+)"', src.read_text(errors="ignore")):
                for other in features - {f}:
                    if inc.startswith(other + "/") or f"/{other}/" in inc:
                        errors.append(f"{src.relative_to(ROOT)} inkludiert Feature-Header von {other}")
    for e in errors:
        print("FEHLER:", e)
    print(f"{len(layers)} Module geprüft, {len(errors)} Verstöße.")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
