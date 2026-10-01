"""K46: Epilog-Matrix (2 Enden × 8 Vignetten-Kombinationen → 4 Schlussbilder)."""
import itertools

TABLEAU = {3: "Voller Chor", 2: "Zwei Stimmen", 1: "Eine Stimme", 0: "Der eigene Chor"}
ENDINGS = [("NewSong", "Neues Lied"), ("SoftSilence", "Sanfte Stille")]
VIG = {
    "FS": ("Freie Stimmen verbündet", "Freie Stimmen im Untergrund"),
    "KAEL": ("Kael kehrt heim", "Kael an Venns Seite"),
    "SERETH": ("Sereth versöhnt", "Sereth gebrochen"),
}


def outcome(fs, kael, sereth):
    """Bedingungen laut K46 §8: FS_STANCE ≥ 0, KAEL_TRUST ≥ 1, SERETH_RESPECT ≥ 1."""
    return (fs >= 0, kael >= 1, sereth >= 1)


def epilog_matrix():
    rows = ["| # | Ende | Freie Stimmen | Kael | Sereth | Schlussbild | Dauer (s) |", "|---|---|---|---|---|---|---|"]
    n = 0
    for key, name in ENDINGS:
        for combo in itertools.product((True, False), repeat=3):
            n += 1
            parts = [VIG[k][0 if ok else 1] for k, ok in zip(("FS", "KAEL", "SERETH"), combo)]
            score = sum(combo)
            dur = 95 + 3 * 40 + 30 + 10 * score   # Endsequenz + 3 Vignetten + Schlussbild
            rows.append(f"| {n} | {name} | {parts[0]} | {parts[1]} | {parts[2]} | {TABLEAU[score]} | {dur} |")
    return "\n".join(rows)


def flag_paths():
    """Wie viele Flag-Kombinationen (−2…2)³ führen zu welchem Schlussbild?"""
    cnt = {k: 0 for k in TABLEAU}
    for fs, ka, se in itertools.product(range(-2, 3), repeat=3):
        cnt[sum(outcome(fs, ka, se))] += 1
    total = sum(cnt.values())
    rows = ["| Schlussbild | Positive Vignetten | Flag-Kombinationen | Anteil |", "|---|---|---|---|"]
    for k in (3, 2, 1, 0):
        rows.append(f"| {TABLEAU[k]} | {k} | {cnt[k]} | {100 * cnt[k] / total:.1f} %".replace(".", ",") + " |")
    rows.append(f"| **Summe** | | **{total}** | 100 % |")
    return "\n".join(rows)


if __name__ == "__main__":
    print(epilog_matrix()); print(); print(flag_paths())
