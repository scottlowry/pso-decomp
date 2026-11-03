#!/usr/bin/env python3
"""Second bisect: C1 row-split x pragma windows; plus V5/V6 frame check."""
import re, subprocess, sys, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
REL = "src/pso/misc/TLobby_804050DC.cpp"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"
orig = open(os.path.join(REPO, REL)).read()  # champion = C1 state

FN = "u16 TLobby__sub_80406BD8(void *arg0, s16 arg1) {"
def propwin(src, pragmas):
    i = src.index(FN)
    endr = src.index("\n}\n", i) + 3
    body = "\n".join(f"#pragma {p}" for p in pragmas)
    return src[:i] + "#pragma push\n" + body + "\n" + src[i:endr] + "#pragma pop\n" + src[endr:]

LO_INLINE = "                addr = *(u32 *)row;\n                addr = (w & 0xFFFF) + addr;\n"
LO_SPLIT  = "                addr = *(u32 *)row;\n                lo = w & 0xFFFF;\n                addr = lo + addr;\n"
MBR_INL   = "                addr = *(u16 *)(row + 6 * (s16)b1 + 14) + addr;\n"
DECL = "    union { u16 s; u8 c[2]; } su;\n"

def real_diffs():
    o = subprocess.run([sys.executable,
        "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py",
        "psov3/pso/misc/TLobby_804050DC", "sub_80406BD8"], cwd=REPO, capture_output=True, text=True).stdout
    mm = re.search(r"match=([\d.]+)", o)
    fr = any("stwu" in ln for ln in o.splitlines() if "O:" in ln and re.search(r"slot\s+4 ", ln))
    return (mm.group(1) if mm else "ERR"), fr

def build(name, src):
    open(os.path.join(REPO, REL), "w").write(src)
    try:
        r = subprocess.run(["ninja", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                           cwd=REPO, capture_output=True, text=True)
        if r.returncode != 0:
            print(name, "BUILD_FAIL", r.stdout[-150:]); return
        g = subprocess.run([GNM, "-S", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                           cwd=REPO, capture_output=True, text=True)
        m = re.search(r"([0-9a-f]{8}) ([0-9a-f]{8}) T TLobby__sub_80406BD8", g.stdout)
        sc, fr = real_diffs()
        print(f"{name} size={int(m.group(2),16) if m else -1} score={sc} frame_off={fr}")
        open(f"/tmp/champ_{name}.cpp","w").write(src)
    finally:
        open(os.path.join(REPO, REL), "w").write(orig)

def split_lo(s):
    assert s.count(LO_INLINE)==2
    return s.replace(LO_INLINE, LO_SPLIT).replace(DECL, "    u32 lo;\n"+DECL, 1)

build("E1_C1_propoff", propwin(orig, ["opt_propagation off"]))
build("E2_C1_lo_propoff", propwin(split_lo(orig), ["opt_propagation off"]))
build("E3_C1_cseoff", propwin(orig, ["opt_common_subs off"]))
build("E4_C1_lo_only", split_lo(orig))
build("E5_C1_bothoff", propwin(orig, ["opt_propagation off", "opt_common_subs off"]))
