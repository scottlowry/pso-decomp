#!/usr/bin/env python3
"""Bisect which statement-split component (row/off/lo) lands era frame+arm from CHAMPION base."""
import re, subprocess, sys, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
REL = "src/pso/misc/TLobby_804050DC.cpp"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"
orig = open(os.path.join(REPO, REL)).read()

OLD = """                b1 = (w >> 16) & 0xFF;
                row = (u8 *)((BufPool_80406BD8 *)&network_buffer_pool_state)->rows + 60 * tbl;
                addr = *(u32 *)row;
                addr = (w & 0xFFFF) + addr;
                addr = *(u16 *)(row + 6 * (s16)b1 + 14) + addr;
"""
ROW1 = """                row = (u8 *)((BufPool_80406BD8 *)&network_buffer_pool_state)->rows;
                row = (u8 *)((s8 *)row + 60 * tbl);
"""
OFF1 = """                off = 6 * b1;
                off = off + 14;
"""
LO1 = """                lo = w & 0xFFFF;
"""
MBR1 = """                mbr = *(u16 *)((s8 *)row + off);
"""
def build(name, src):
    open(os.path.join(REPO, REL), "w").write(src)
    try:
        r = subprocess.run(["ninja", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                           cwd=REPO, capture_output=True, text=True)
        if r.returncode != 0:
            print(name, "BUILD_FAIL", r.stdout[-200:]); return
        g = subprocess.run([GNM, "-S", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                           cwd=REPO, capture_output=True, text=True)
        m = re.search(r"([0-9a-f]{8}) ([0-9a-f]{8}) T TLobby__sub_80406BD8", g.stdout)
        o = subprocess.run([sys.executable,
            "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py",
            "psov3/pso/misc/TLobby_804050DC", "sub_80406BD8"], cwd=REPO, capture_output=True, text=True)
        mm = re.search(r"match=([\d.]+)", o.stdout)
        nb = sum(1 for ln in o.stdout.splitlines() if re.search(r"slot\s*\d+ O:\s*[a-z]+\s+r?\d*,? ?[^0-9]*0x[0-9a-f]+\s+N:", ln) and " 0x" in ln)
        print(f"{name} size={int(m.group(2),16) if m else -1} score={mm.group(1) if mm else 'ERR'}")
        if mm: open(f"/tmp/champ_{name}.cpp","w").write(src)
    finally:
        open(os.path.join(REPO, REL), "w").write(orig)

DECL = "    union { u16 s; u8 c[2]; } su;\n"
def with_decls(src, temps):
    return src.replace(DECL, "".join(f"    {t};\n" for t in temps) + DECL, 1)

def mut(row=None, off=None, lo=None, mbr=None, prop=False):
    src = orig
    assert src.count(OLD) == 2, src.count(OLD)
    temps = []
    new = OLD
    if row: new = new.replace(OLD.split("\n")[1]+"\n", ROW1)
    if off: temps.append("s32 off"); new = new.replace(
        "                addr = *(u16 *)(row + 6 * (s16)b1 + 14) + addr;\n",
        MBR1 + "                addr = off + addr;\n").replace("6 * (s16)b1 + 14", "") if False else new
    out = new
    return src, out

# simpler explicit variants:
def V(name, repl_fn, temps=()):
    src = orig
    assert src.count(OLD) == 2
    src = repl_fn(src)
    if temps: src = with_decls(src, temps)
    build(name, src)

def only_row(s): return s.replace(OLD, OLD.replace(OLD.splitlines()[1]+"\n", ROW1))
def only_lo(s):
    return s.replace(OLD, OLD.replace("addr = *(u32 *)row;\n                addr = (w & 0xFFFF) + addr;", "addr = *(u32 *)row;\n                lo = w & 0xFFFF;\n                addr = lo + addr;"))
def only_off(s):
    a = "                addr = *(u32 *)row;\n                addr = (w & 0xFFFF) + addr;\n                addr = *(u16 *)(row + 6 * (s16)b1 + 14) + addr;\n"
    b = "                off = 6 * b1;\n                off = off + 14;\n                addr = *(u32 *)row;\n                addr = (w & 0xFFFF) + addr;\n                addr = *(u16 *)((s8 *)row + off) + addr;\n"
    assert s.count(a)==2
    return s.replace(a,b)
def row_off(s):
    a = OLD
    b = ("""                b1 = (w >> 16) & 0xFF;
""" + ROW1 + OFF1.replace("6 * b1", "6 * b1") +
        """                addr = *(u32 *)row;
                addr = (w & 0xFFFF) + addr;
                addr = *(u16 *)((s8 *)row + off) + addr;
""")
    return s.replace(a,b)

V("C1_only_row", only_row)
V("C2_only_lo", only_lo, temps=("u32 lo",))
V("C3_only_off", only_off, temps=("s32 off",))
V("C4_row_off", row_off, temps=("s32 off",))
