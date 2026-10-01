#!/usr/bin/env python3
"""Netzwerk-Referenzmodell (K59): Bandbreite je Modus und Rolle, Kampfbefehl-Packing, Serverkapazität,
CCU-Modell je Region, Prüfregeln NET-01–NET-06.

  NET-01 jeder Command (Client → Server) hat eine Serverprüfung
  NET-02 State-Nachrichten laufen nur über zuverlässige Kanäle
  NET-03 Koop mit 4 Spielern: Gast-Download ≤ 256 kbit/s, Host-Upload ≤ 1.024 kbit/s
  NET-04 Regionsanteile = 1.000 ‰, Ziel-RTT ≤ 60 ms je Region
  NET-05 in Kampf-/Raid-/Ranked-Modi sendet der Client keine State-Nachrichten (DR-21)
  NET-06 Kampfbefehl passt in die angegebene Nutzlast (Bit-Layout)

Aufruf: aethris_net.py validate | bandwidth | capacity
"""
import csv, math, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


MSG = {r["Name"]: r for r in rows("Data/Online/NetMessages.csv")}
REG = rows("Data/Online/ServerRegions.csv")
MODES = rows("Data/Online/ModeTopology.csv")

NET_HZ = 30                 # Iris-Sendetakt Koop (Pakete/s je Verbindung)
PKT_OVERHEAD = 28 + 12      # UDP/IPv4 + Paket-/Bunch-Header (Bytes)
VISIBLE_ECHOS = 18          # Ø relevante Echo-Actors je Gast (max. 40)
RELEVANT_NPCS = 20          # Ø relevante NPC-Actors je Gast (max. 60)
BUDGET_GUEST_DOWN = 256     # kbit/s
BUDGET_HOST_UP = 1024       # kbit/s
COMBAT_BITS = {"Tick": 32, "Slot": 3, "Action": 3, "Ability": 4, "Target": 4, "Reserve": 3}


def rate_bytes_per_s(name, count=1):
    m = MSG[name]
    hz = float(m["RateHz"]) or float(m["PerMin"]) / 60
    return hz * int(m["Bytes"]) * count


def coop(players=4, echos=VISIBLE_ECHOS, npcs=RELEVANT_NPCS):
    others = players - 1
    down = {
        "Andere Spieler": rate_bytes_per_s("NM_PLAYER_REPL", others),
        "Begleit-Echos": rate_bytes_per_s("NM_COMPANION_REPL", players),
        "Echo-Actors": rate_bytes_per_s("NM_ECHO_ACTOR_REPL", echos),
        "NPCs": rate_bytes_per_s("NM_NPC_REPL", npcs),
        "Weltereignisse": rate_bytes_per_s("NM_WORLD_EVENT"),
        "Kampf (Start, Ergebnisse)": rate_bytes_per_s("NM_COMBAT_START") + rate_bytes_per_s("NM_COMBAT_RESULT"),
        "Paket-Header": NET_HZ * PKT_OVERHEAD,
    }
    up = {
        "Bewegung": rate_bytes_per_s("NM_PLAYER_MOVE"),
        "Interaktion, Kampfbefehle, Hash, Bindung": sum(rate_bytes_per_s(n) for n in
                                                         ("NM_INTERACT", "NM_COMBAT_COMMAND", "NM_COMBAT_HASH", "NM_BOND_TIMING")),
        "Herzschlag": rate_bytes_per_s("NM_HEARTBEAT"),
        "Paket-Header": NET_HZ * PKT_OVERHEAD,
    }
    kb = lambda b: b * 8 / 1000
    d = {k: kb(v) for k, v in down.items()}
    u = {k: kb(v) for k, v in up.items()}
    return d, u, sum(d.values()), sum(u.values()), sum(d.values()) * others


def de(x, nd=1):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def bandwidth_table():
    d, u, dsum, usum, host = coop(4)
    dm, um, dmsum, umsum, hostm = coop(4, 40, 60)
    lines = ["| Strom (Koop, 4 Spieler) | Gast ↓ Ø | Gast ↓ Max (40 Echos, 60 NPCs) | Gast ↑ |", "|---|---|---|---|"]
    for k, v in d.items():
        lines.append(f"| {k} | {de(v, 2)} | {de(dm[k], 2)} | – |")
    for k, v in u.items():
        lines.append(f"| {k} (Gast → Host) | – | – | {de(v, 2)} |")
    lines.append(f"| **Σ je Gast (kbit/s)** | **{de(dsum)}** | **{de(dmsum)}** (Budget {BUDGET_GUEST_DOWN}) | **{de(usum)}** |")
    lines.append(f"| **Host-Upload (3 Gäste, kbit/s)** | **{de(host)}** | **{de(hostm)}** (Budget {de(BUDGET_HOST_UP, 0)}) | |")
    return "\n".join(lines)


def pvp_bandwidth():
    per_s = sum(rate_bytes_per_s(n) for n in ("NM_COMBAT_RESULT", "NM_COMBAT_TIMER", "NM_HEARTBEAT"))
    pkts = 2  # Ø Pakete/s (Timer 1 Hz + Herzschlag 1 Hz, Ergebnisse gebündelt)
    return (per_s + pkts * PKT_OVERHEAD) * 8 / 1000


def pack(tick, slot, action, ability, target, reserve):
    """Referenz zu FAethrisCombatCommand::Pack (7 Byte, Little Endian)."""
    assert slot < 8 and action < 8 and ability < 16 and target < 16 and reserve < 8
    bits = slot | action << 3 | ability << 6 | target << 10 | reserve << 14
    return (tick | bits << 32).to_bytes(7, "little")


def pack_examples():
    ex = [("Fähigkeit 2 auf Gegnerplatz 9", 1200, 0, 0, 2, 9, 0), ("Crescendo (Index 4) auf Gegnerplatz 8", 3450, 1, 0, 4, 8, 0),
          ("Wechsel auf Reserveplatz 3", 5100, 0, 1, 0, 0, 3), ("Aufgeben", 7000, 0, 6, 0, 0, 0)]
    lines = ["| Befehl | Tick | Slot | Aktion | Fähigkeit | Ziel | Reserve | 7 Byte (hex) |", "|---|---|---|---|---|---|---|---|"]
    for name, *v in ex:
        lines.append(f"| {name} | {v[0]} | {v[1]} | {v[2]} | {v[3]} | {v[4]} | {v[5]} | `{pack(*v).hex(' ')}` |")
    return "\n".join(lines)


def combat_bits():
    return sum(COMBAT_BITS.values())


# Kapazitätsmodell (Annahmen K59 §7; Überprüfung in der Closed Beta P5)
PEAK_CCU = 150_000           # Spitze im Launch-Monat (≈ 2,5 Mio. Spielende × 6 % gleichzeitig)
SHARE = {"Raid": 0.04, "PvP": 0.07, "Koop": 0.18}
PLAYERS_PER_MATCH = {"Raid": 3.2, "PvP": 2.0}
MATCHES_PER_CORE = {"Raid": 25, "PvP": 60}
EUR_PER_CORE_H = 0.045
HEADROOM = 1.3


def capacity_rows():
    out = []
    for r in REG:
        ccu = PEAK_CCU * int(r["Share"]) / 1000
        cores = 0
        for m in ("Raid", "PvP"):
            matches = ccu * SHARE[m] / PLAYERS_PER_MATCH[m]
            cores += matches / MATCHES_PER_CORE[m]
        cores = math.ceil(cores * HEADROOM)
        out.append((r, ccu, cores))
    return out


def capacity_table():
    lines = ["| Region | Standort | Anteil | Spitzen-CCU | davon Koop (Listen-Server, ohne Serverkosten) | Dedicated-Kerne (Spitze, +30 %) |",
             "|---|---|---|---|---|---|"]
    tot_c = tot_k = 0
    for r, ccu, cores in capacity_rows():
        tot_c += ccu
        tot_k += cores
        lines.append(f"| {r['DisplayName']} | {r['Location']} | {int(r['Share']) / 10:.0f} % | {de(ccu, 0)} | {de(ccu * SHARE['Koop'], 0)} | {cores} |")
    avg_cores = tot_k * 0.45          # Tagesmittel ≈ 45 % der Spitze (Autoscaling)
    cost = avg_cores * 24 * 30 * EUR_PER_CORE_H
    lines.append(f"| **Σ** | | 100 % | **{de(tot_c, 0)}** | **{de(tot_c * SHARE['Koop'], 0)}** | **{tot_k}** |")
    lines.append("")
    lines.append(f"Monatliche Kosten Dedicated Server bei Autoscaling (Ø 45 % der Spitzenkerne, {de(EUR_PER_CORE_H, 3)} € je Kernstunde): **≈ {de(cost, 0)} €** zuzüglich Backend-Dienste (§8).")
    return "\n".join(lines)


def messages_table():
    lines = ["| Nachricht | Modus | Richtung | Art | Kanal | Rate | Bytes | Serverprüfung |", "|---|---|---|---|---|---|---|---|"]
    for m in MSG.values():
        rate = f"{m['RateHz']} Hz" if float(m["RateHz"]) else f"Ereignis (~{m['PerMin']}/min)"
        lines.append(f"| `{m['Name']}` | {m['Mode']} | {m['Direction']} | {m['Kind']} | {m['Channel']} | {rate.replace('.', ',')} | {m['Bytes']} | {m['Validation']} |")
    return "\n".join(lines)


def validate():
    err = []
    for m in MSG.values():
        if m["Kind"] == "Command" and m["Validation"] in ("", "–"):
            err.append(f"NET-01 {m['Name']}: Command ohne Serverprüfung")
        if m["Kind"] == "State" and "Unreliable" in m["Channel"]:
            err.append(f"NET-02 {m['Name']}: State über unzuverlässigen Kanal")
        if m["Direction"] == "C→S" and m["Kind"] == "State" and m["Mode"] in ("ALL_COMBAT", "MODE_RAID", "MODE_PVP_RANKED", "MODE_PVP_CASUAL"):
            err.append(f"NET-05 {m['Name']}: Client sendet Zustand im Kampfmodus")
    _, _, dsum, _, host = coop(4, 40, 60)
    if dsum > BUDGET_GUEST_DOWN:
        err.append(f"NET-03 Gast-Download {dsum:.1f} > {BUDGET_GUEST_DOWN} kbit/s")
    if host > BUDGET_HOST_UP:
        err.append(f"NET-03 Host-Upload {host:.1f} > {BUDGET_HOST_UP} kbit/s")
    if sum(int(r["Share"]) for r in REG) != 1000:
        err.append("NET-04 Regionsanteile ≠ 1.000 ‰")
    for r in REG:
        if int(r["RttMs"]) > 60:
            err.append(f"NET-04 {r['Name']}: RTT-Ziel {r['RttMs']} ms > 60")
    if math.ceil(combat_bits() / 8) > int(MSG["NM_COMBAT_COMMAND"]["Bytes"]):
        err.append("NET-06 Kampfbefehl passt nicht in die Nutzlast")
    return err


def report():
    e = validate()
    _, _, dsum, usum, host = coop(4)
    return (f"Prüfregeln NET-01–NET-06 über {len(MSG)} Nachrichten, {len(MODES)} Modi, {len(REG)} Regionen: **{len(e)} Verstöße**. "
            f"Koop (4 Spieler): Gast ↓ {de(dsum)} kbit/s, Gast ↑ {de(usum)} kbit/s, Host ↑ {de(host)} kbit/s; "
            f"PvP je Spieler ≈ {de(pvp_bandwidth(), 2)} kbit/s; Kampfbefehl {combat_bits()} Bit → {math.ceil(combat_bits() / 8)} Byte.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "bandwidth":
        print(bandwidth_table())
    elif cmd == "capacity":
        print(capacity_table())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
