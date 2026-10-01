#!/usr/bin/env python3
"""Performance-Referenzmodell (K65): Frame- und Speicherbudgets je Plattform, Split-Screen (Q6), Koop-Host-Grenze.

Prüfregeln:
  PF-01 Summe je Thread und Szenario ≤ 85 % der Bildzeit (Zielbildrate je Plattform)
  PF-02 Speicher ≤ 90 % des verfügbaren Spielspeichers
  PF-03 Budgets stimmen mit den Kanon-Werten der Fachkapitel überein
  PF-04 Split-Screen-Entscheidung (Profil) = Ergebnis der Machbarkeitsrechnung
  PF-05 Koop-Host-Grenze (Profil) = Ergebnis der Rechnung (Speicher, Game Thread)
  PF-06 jedes Profil hat Zielbildrate, Auflösung, Upscaler

Aufruf: aethris_perf.py validate | frames | memory | split
"""
import csv, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PLATFORMS = ["PS5", "XSX", "XSS", "Switch2", "PCMin", "PCRec"]
NAMES = {"PS5": "PS5", "XSX": "Xbox Series X", "XSS": "Xbox Series S", "Switch2": "Switch 2", "PCMin": "PC Min", "PCRec": "PC Empf."}
HEADROOM = 0.85
MEM_HEADROOM = 0.90


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


FB = rows("Data/Perf/FrameBudgets.csv")
MB = rows("Data/Perf/MemoryBudgets.csv")
PP = {r["Name"]: r for r in rows("Data/Perf/PlatformProfiles.csv")}


def de(x, nd=1):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def frame_ms(p):
    return 1000 / int(PP[p]["TargetFps"])


def thread_sum(p, thread, scenario):
    return sum(float(r[p]) for r in FB if r["Thread"] == thread and r["Scenario"] in ("ALL", scenario))


def frames_table():
    lines = ["| Thread / Szenario | " + " | ".join(NAMES[p] for p in PLATFORMS) + " |", "|---|" + "---|" * len(PLATFORMS)]
    lines.append("| Zielbildrate (Bildzeit) | " + " | ".join(f"{PP[p]['TargetFps']} fps ({de(frame_ms(p))} ms)" for p in PLATFORMS) + " |")
    for thread in ("Game", "Render", "Audio"):
        lines.append(f"| {thread} Thread | " + " | ".join(f"{de(thread_sum(p, thread, 'EXPLORE'))} ms ({100 * thread_sum(p, thread, 'EXPLORE') / frame_ms(p):.0f} %)" for p in PLATFORMS) + " |")
    for sc, label in (("EXPLORE", "GPU Erkundung"), ("COMBAT", "GPU Kampf (Worst Case)")):
        lines.append(f"| {label} | " + " | ".join(f"{de(thread_sum(p, 'GPU', sc))} ms ({100 * thread_sum(p, 'GPU', sc) / frame_ms(p):.0f} %)" for p in PLATFORMS) + " |")
    return "\n".join(lines)


def detail_table(thread):
    sel = [r for r in FB if r["Thread"] == thread]
    lines = ["| Posten | Szenario | " + " | ".join(NAMES[p] for p in PLATFORMS) + " | Quelle |", "|---|---|" + "---|" * len(PLATFORMS) + "---|"]
    for r in sel:
        lines.append(f"| {r['Component']} | {r['Scenario']} | " + " | ".join(de(float(r[p]), 1) for p in PLATFORMS) + f" | {r['Source']} |")
    return "\n".join(lines)


def mem_sum(p):
    return sum(int(r[p]) for r in MB)


def memory_table():
    lines = ["| Posten | " + " | ".join(NAMES[p] for p in PLATFORMS) + " |", "|---|" + "---|" * len(PLATFORMS)]
    for r in MB:
        lines.append(f"| {r['Component']} | " + " | ".join(de(int(r[p]), 0) for p in PLATFORMS) + " |")
    lines.append("| **Σ** | " + " | ".join(f"**{de(mem_sum(p), 0)}**" for p in PLATFORMS) + " |")
    lines.append("| verfügbar (Annahme) | " + " | ".join(de(int(PP[p]["AvailableMB"]), 0) for p in PLATFORMS) + " |")
    lines.append("| Auslastung | " + " | ".join(f"{100 * mem_sum(p) / int(PP[p]['AvailableMB']):.0f} %" for p in PLATFORMS) + " |")
    return "\n".join(lines)


# ---------------- Split-Screen (Q6) ----------------
SPLIT_GPU = 1.6        # zweite Ansicht: Geometrie/Post doppelt, GI/Schatten-Caches teilweise geteilt
SPLIT_RT = 1.5
SPLIT_GT_STREAM = 1.0  # zweite Streaming-Quelle: +100 % Streaming
SPLIT_WORLD_MEM = 0.35 # zweite Quelle: +35 % geladene Welt
SPLIT_FPS = 30
SPLIT_RT_MEM = 0.5    # zweite Ansicht: Render-Ziele zur Hälfte zusätzlich (halbe Auflösung je Ansicht)


def split_eval(p):
    frame = 1000 / SPLIT_FPS * HEADROOM
    gpu = thread_sum(p, "GPU", "EXPLORE") * SPLIT_GPU
    rt = thread_sum(p, "Render", "EXPLORE") * SPLIT_RT
    gt = thread_sum(p, "Game", "EXPLORE") + float(next(r for r in FB if r["Name"] == "GT_STREAMING")[p]) * SPLIT_GT_STREAM
    mem = (mem_sum(p) + int(next(r for r in MB if r["Name"] == "MEM_WORLD")[p]) * SPLIT_WORLD_MEM
           + int(next(r for r in MB if r["Name"] == "MEM_RT")[p]) * SPLIT_RT_MEM)
    ok = gpu <= frame and rt <= frame and gt <= frame and mem <= int(PP[p]["AvailableMB"]) * MEM_HEADROOM
    return gpu, rt, gt, mem, ok


def split_table():
    lines = ["| Plattform | GPU (×1,6) | Render (×1,5) | Game (+Streaming) | Speicher (+35 % Welt, +50 % Render-Ziele) | Budget 30 fps (85 %) | machbar |", "|---|---|---|---|---|---|---|"]
    for p in PLATFORMS:
        gpu, rt, gt, mem, ok = split_eval(p)
        lines.append(f"| {NAMES[p]} | {de(gpu)} ms | {de(rt)} ms | {de(gt)} ms | {de(mem, 0)} / {de(int(PP[p]['AvailableMB']) * MEM_HEADROOM, 0)} MB | {de(1000 / SPLIT_FPS * HEADROOM)} ms | {'✅' if ok else '❌'} |")
    return "\n".join(lines)


# ---------------- Koop-Host ----------------
HOST_STREAM_PER_GUEST = 0.35   # +35 % Streaming-Last und Weltspeicher je weiterer Streaming-Quelle
HOST_NET_PER_GUEST = 0.5       # Iris-Kosten wachsen mit Gästen (Basis = 4 Spieler)


def host_eval(p, players):
    extra = players - 1
    gt = thread_sum(p, "Game", "EXPLORE") + float(next(r for r in FB if r["Name"] == "GT_STREAMING")[p]) * HOST_STREAM_PER_GUEST * extra
    mem = mem_sum(p) + int(next(r for r in MB if r["Name"] == "MEM_WORLD")[p]) * HOST_STREAM_PER_GUEST * extra
    ok = gt <= frame_ms(p) * HEADROOM and mem <= int(PP[p]["AvailableMB"]) * MEM_HEADROOM
    return gt, mem, ok


def host_max(p):
    best = 1
    for n in range(2, 5):
        if host_eval(p, n)[2]:
            best = n
    return best


def host_table():
    lines = ["| Plattform | 2 Spieler (Game / Speicher) | 3 Spieler | 4 Spieler | max. Host |", "|---|---|---|---|---|"]
    for p in PLATFORMS:
        cells = []
        for n in (2, 3, 4):
            gt, mem, ok = host_eval(p, n)
            cells.append(f"{de(gt)} ms / {de(mem, 0)} MB {'✅' if ok else '❌'}")
        lines.append(f"| {NAMES[p]} | " + " | ".join(cells) + f" | **{host_max(p)}** |")
    return "\n".join(lines)


CANON = {("GT_ECOLOGY", "PS5"): 1.6, ("GT_ECOLOGY", "Switch2"): 2.2, ("GT_NPC", "PS5"): 1.2, ("GT_NPC", "Switch2"): 1.8,
         ("GT_UI", "PS5"): 0.8, ("GT_UI", "Switch2"): 1.2, ("RT_UI", "PS5"): 0.6, ("RT_UI", "Switch2"): 1.0,
         ("GPU_VFX_C", "PS5"): 4.0, ("GPU_VFX_C", "Switch2"): 5.5, ("AU_RENDER", "PS5"): 1.5, ("AU_RENDER", "Switch2"): 2.5}


def validate():
    err = []
    for p in PLATFORMS:
        f = frame_ms(p) * HEADROOM
        for thread in ("Game", "Render", "Audio", "GPU"):
            for sc in ("EXPLORE", "COMBAT"):
                v = thread_sum(p, thread, sc)
                if v > f:
                    err.append(f"PF-01 {p} {thread} {sc}: {v:.1f} > {f:.1f} ms")
        if mem_sum(p) > int(PP[p]["AvailableMB"]) * MEM_HEADROOM:
            err.append(f"PF-02 {p}: {mem_sum(p)} MB")
        pr = PP[p]
        if not (pr["TargetFps"] and pr["InternalRes"] and pr["Upscaler"]):
            err.append(f"PF-06 {p}")
        if split_eval(p)[4] != pr["SplitScreen"].startswith("ja"):
            err.append(f"PF-04 {p}: Split-Screen-Profil passt nicht zur Rechnung")
        if host_max(p) != int(pr["CoopHostMax"]):
            err.append(f"PF-05 {p}: Host-Grenze {pr['CoopHostMax']} ≠ Rechnung {host_max(p)}")
    by = {r["Name"]: r for r in FB}
    for (n, p), v in CANON.items():
        if abs(float(by[n][p]) - v) > 1e-9:
            err.append(f"PF-03 {n}/{p}: {by[n][p]} ≠ Kanon {v}")
    return err


def report():
    e = validate()
    return (f"Prüfregeln PF-01–PF-06: **{len(e)} Verstöße**. {len(FB)} Frame-Posten, {len(MB)} Speicherposten, {len(PP)} Profile; "
            f"Split-Screen machbar auf {', '.join(NAMES[p] for p in PLATFORMS if split_eval(p)[4])}; "
            f"Koop-Host maximal: " + ", ".join(f"{NAMES[p]} {host_max(p)}" for p in PLATFORMS) + ".")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "frames":
        print(frames_table())
    elif cmd == "memory":
        print(memory_table())
    elif cmd == "split":
        print(split_table()); print(host_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
