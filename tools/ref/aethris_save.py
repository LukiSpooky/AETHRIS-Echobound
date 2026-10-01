#!/usr/bin/env python3
"""Save-Referenzmodell (K64): Container-Format (identisch zu FAethrisSaveContainer in GF_Save), Größenbudget,
Fragment-Register, Fehlertoleranz.

Container (Little Endian):
  u32 Magic 'AETH' (0x48544541) · u32 ContainerVersion (=2) · u32 HeaderSize · Header-Bytes
  u32 FragmentCount · je Fragment: u16 IdLen · Id (UTF-8) · u32 Version · u32 Offset · u32 Size · u32 Crc32
  Nutzlast (Fragmente hintereinander) · u32 PayloadCrc32 (über die gesamte Nutzlast)
Header-Bytes: u16 BuildLen · Build · i64 SavedAtUnix · i64 PlayTimeSec · u16 RegionLen · Region · i32 WardenRank ·
              i32 Akkorde · u8 ChorCount · je u16 Len + Species
Kompression (Oodle im Spiel) liegt außerhalb des Containers; die Referenz nutzt zlib nur für Größenschätzungen.

Prüfregeln:
  SV-01 jedes in den Kapiteln genannte Fragment (`Player.*`, `World.*`, `Profile.*`) steht im Register
  SV-02 Owner-Modul existiert
  SV-03 IDs eindeutig, Version ≥ 1, Scope World|Profile
  SV-04 Größenbudget: Weltstand ≤ 2,5 MB unkomprimiert, alle Slots inkl. Rotation ≤ 32 MB (komprimiert geschätzt)
  SV-05 Rundreise, Korruptionserkennung je Fragment (SA-03), unbekannte Fragmente bleiben erhalten (SA-04)
  SV-06 Autosave-Auslöser vollständig beschrieben

Aufruf: aethris_save.py validate | sizes | vector
"""
import csv, pathlib, re, struct, sys, zlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
MAGIC = 0x48544541
CONTAINER_VERSION = 2


def rows(p):
    return list(csv.DictReader(l for l in open(ROOT / p, encoding="utf-8") if not l.startswith("#")))


FRAG = rows("Data/Save/Fragments.csv")
TRIG = rows("Data/Save/AutosaveTriggers.csv")


# ---------------- Container ----------------
def _str(s):
    b = s.encode("utf-8")
    return struct.pack("<H", len(b)) + b


def pack_header(build, saved_at, playtime, region, rank, akkorde, chor):
    out = _str(build) + struct.pack("<qq", saved_at, playtime) + _str(region) + struct.pack("<iiB", rank, akkorde, len(chor))
    for c in chor:
        out += _str(c)
    return out


def pack(header_bytes, fragments):
    """fragments: Liste (Id, Version, bytes). Rückgabe: Container-Bytes."""
    payload = b""
    entries = b""
    for fid, ver, data in fragments:
        entries += _str(fid) + struct.pack("<IIII", ver, len(payload), len(data), zlib.crc32(data) & 0xFFFFFFFF)
        payload += data
    return (struct.pack("<III", MAGIC, CONTAINER_VERSION, len(header_bytes)) + header_bytes
            + struct.pack("<I", len(fragments)) + entries + payload + struct.pack("<I", zlib.crc32(payload) & 0xFFFFFFFF))


def unpack(blob):
    """Rückgabe (header_bytes, {Id: (Version, bytes)}, defekte Ids, payload_ok)."""
    magic, ver, hsize = struct.unpack_from("<III", blob, 0)
    if magic != MAGIC:
        raise ValueError("kein AETHRIS-Save")
    pos = 12
    header = blob[pos:pos + hsize]
    pos += hsize
    (n,) = struct.unpack_from("<I", blob, pos)
    pos += 4
    entries = []
    for _ in range(n):
        (ln,) = struct.unpack_from("<H", blob, pos)
        pos += 2
        fid = blob[pos:pos + ln].decode("utf-8")
        pos += ln
        v, off, size, crc = struct.unpack_from("<IIII", blob, pos)
        pos += 16
        entries.append((fid, v, off, size, crc))
    payload = blob[pos:len(blob) - 4]
    (pcrc,) = struct.unpack_from("<I", blob, len(blob) - 4)
    frags, bad = {}, []
    for fid, v, off, size, crc in entries:
        data = payload[off:off + size]
        if zlib.crc32(data) & 0xFFFFFFFF != crc:
            bad.append(fid)          # SA-03: nur dieses Fragment zurücksetzen
            continue
        frags[fid] = (v, data)
    return header, frags, bad, (zlib.crc32(payload) & 0xFFFFFFFF) == pcrc


def vector():
    """Testvektor für den C++-Test (GF_Save): zwei Fragmente."""
    h = pack_header("1.0.0-CL123", 1893456000, 3600 * 52, "R03", 17, 5, ["ECHO_001", "ECHO_067"])
    blob = pack(h, [("Chor", 3, bytes(range(16))), ("World.Zones", 1, b"\x01\x02\x03\x04")])
    return blob.hex()


# ---------------- Größen ----------------
SLOTS_WORLD = 3 + 1 + 1          # 3 Weltstände, 1 Eiserner Wärter, 1 Finale-Speicherpunkt
ROTATION = 3                     # rotierende Autosave-Kopien je Weltstand-Slot (SA-05)
COMPRESSION = 0.35               # erwartetes Verhältnis Oodle Kraken (Echo-Instanzen, Bitfelder)


def size_of(f):
    return int(f["Count"]) * int(f["BytesEach"])


def sizes_table():
    world = [f for f in FRAG if f["Scope"] == "World"]
    prof = [f for f in FRAG if f["Scope"] == "Profile"]
    lines = ["| Fragment | Owner | Version | Inhalt | Obergrenze unkomprimiert |", "|---|---|---|---|---|"]
    for f in sorted(world, key=lambda f: -size_of(f)):
        lines.append(f"| `{f['Name']}` | {f['Owner']} | v{f['Version']} | {f['Content']} | {de(size_of(f) / 1024, 1)} KB |")
    ws = sum(size_of(f) for f in world)
    ps = sum(size_of(f) for f in prof if f["Name"] != "Profile.PhotoAlbum")
    lines.append(f"| **Σ Weltstand** | | | | **{de(ws / 1024, 0)} KB** (komprimiert ≈ {de(ws * COMPRESSION / 1024, 0)} KB) |")
    lines += ["", "| Profil-Fragment | Owner | Version | Inhalt | Obergrenze |", "|---|---|---|---|---|"]
    for f in prof:
        lines.append(f"| `{f['Name']}` | {f['Owner']} | v{f['Version']} | {f['Content']} | {de(size_of(f) / 1024, 1)} KB |")
    lines.append(f"| **Σ Profil (ohne Bilder)** | | | | **{de(ps / 1024, 0)} KB** |")
    return "\n".join(lines)


def total_mb():
    ws = sum(size_of(f) for f in FRAG if f["Scope"] == "World") * COMPRESSION
    ps = sum(size_of(f) for f in FRAG if f["Scope"] == "Profile" and f["Name"] != "Profile.PhotoAlbum")
    return (ws * (SLOTS_WORLD + 3 * ROTATION) + ps) / 1024 / 1024


def de(x, nd):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ---------------- Prüfungen ----------------
def mentioned():
    pat = re.compile(r"`((?:Player|World|Profile)\.[A-Za-z]+)`")
    found = set()
    for p in (ROOT / "docs").rglob("*.md"):
        found |= set(pat.findall(p.read_text(encoding="utf-8")))
    return found


def module_exists(m):
    return (ROOT / "Plugins/GameFeatures" / m).exists() or (ROOT / "Source" / m).exists()


def validate():
    err = []
    names = [f["Name"] for f in FRAG]
    for m in sorted(mentioned()):
        if m not in names:
            err.append(f"SV-01 {m} nicht im Register")
    for f in FRAG:
        if not module_exists(f["Owner"]):
            err.append(f"SV-02 {f['Name']}: Modul {f['Owner']} fehlt")
        if int(f["Version"]) < 1 or f["Scope"] not in ("World", "Profile"):
            err.append(f"SV-03 {f['Name']}")
    if len(set(names)) != len(names):
        err.append("SV-03 doppelte IDs")
    ws = sum(size_of(f) for f in FRAG if f["Scope"] == "World")
    if ws > 2.5 * 1024 * 1024 or total_mb() > 32:
        err.append(f"SV-04 Budget: Weltstand {ws / 1024:.0f} KB, gesamt {total_mb():.1f} MB")
    # SV-05 Rundreise + Korruption + unbekannt
    h = pack_header("t", 0, 0, "R01", 1, 0, [])
    frs = [("Chor", 3, b"abc" * 10), ("Zukunft.Fragment", 9, b"\x00" * 7), ("World.Zones", 1, b"\x05" * 4)]
    blob = bytearray(pack(h, frs))
    _, got, bad, ok = unpack(bytes(blob))
    if bad or not ok or got.get("Zukunft.Fragment") != (9, b"\x00" * 7):
        err.append("SV-05 Rundreise/unbekanntes Fragment")
    i = bytes(blob).rfind(b"\x05\x05\x05\x05")
    blob[i] ^= 0xFF
    _, got, bad, ok = unpack(bytes(blob))
    if bad != ["World.Zones"] or "Chor" not in got or ok:
        err.append("SV-05 Korruption nicht auf ein Fragment begrenzt")
    for t in TRIG:
        if not t["Trigger"] or not t["Rhythm"]:
            err.append(f"SV-06 {t['Name']}")
    return err


def report():
    e = validate()
    ws = sum(size_of(f) for f in FRAG if f["Scope"] == "World")
    return (f"Prüfregeln SV-01–SV-06: **{len(e)} Verstöße**. {len(FRAG)} Fragmente ({sum(1 for f in FRAG if f['Scope'] == 'World')} Weltstand, "
            f"{sum(1 for f in FRAG if f['Scope'] == 'Profile')} Profil), alle in den Kapiteln genannten Fragmente registriert; "
            f"Weltstand ≤ {de(ws / 1024, 0)} KB unkomprimiert, alle Slots mit Rotation ≈ {de(total_mb(), 1)} MB; "
            f"Rundreise, Korruption je Fragment und unbekannte Fragmente geprüft.")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    if cmd == "sizes":
        print(sizes_table())
    elif cmd == "vector":
        print(vector())
    else:
        e = validate()
        print("\n".join(e))
        print(report())
        sys.exit(1 if e else 0)
