#!/opt/homebrew/bin/python3.14
"""gen_variants2.py — color-class variants for draw_compass (v09 = twin+swap+declflip2 base)."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
BASE = open(f"{HERE}/probe_dc.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

OLDCOL = "(s32)((color << 16) | (color >> 16))"
SWAPS = [
    ("state.x = (f32)lbl_804C87E4[1].x + tbl[2];", "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;"),
    ("state.y = (f32)lbl_804C87E4[1].y + tbl[3];", "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;"),
    ("state.x = (f32)lbl_804C87E4[0].x + tbl[0];", "state.x = tbl[0] + (f32)lbl_804C87E4[0].x;"),
    ("state.y = (f32)lbl_804C87E4[0].y + tbl[1];", "state.y = tbl[1] + (f32)lbl_804C87E4[0].y;"),
]
FILL_OLD = ("    state.x = TRaderMapCore__data_805DC528;\n"
            "    state.y = TRaderMapCore__data_805DC528;\n"
            "    state.z = TRaderMapCore__data_805DC528;\n"
            "    state.sx = TRaderMapCore__data_805DC534;\n"
            "    state.sy = TRaderMapCore__data_805DC534;")
FILL_D2 = ("    f32 b = TRaderMapCore__data_805DC534;\n"
           "    f32 a = TRaderMapCore__data_805DC528;\n"
           "    state.x = a;\n"
           "    state.y = a;\n"
           "    state.z = a;\n"
           "    state.sx = b;\n"
           "    state.sy = b;")

def swap(t):
    for a, b in SWAPS: t = t.replace(a, b)
    return t
def d2(t):
    return t.replace(FILL_OLD, FILL_D2)

# c1: twin verbatim, new_var hoisted at top (before guard)
TWIN_C1 = ("(s32((((((color >> 0x10U) & new_var) | ((color << 0x10) & 0xFF000000)) & (~0xFF0000))"
           " | ((color << 0x10) & 0xFF0000))))")
def c1(t):
    t = t.replace("    CS state;\n    u32 color;\n", "    u32 new_var;\n    CS state;\n    u32 color;\n")
    t = t.replace("    if (apply_compass_param", "    new_var = ~0xFF000000;\n    if (apply_compass_param")
    return t.replace(OLDCOL, TWIN_C1)

# c2: twin verbatim inline (no var)
TWIN_C2 = ("(s32((((((color >> 0x10U) & ~0xFF000000) | ((color << 0x10) & 0xFF000000)) & (~0xFF0000))"
           " | ((color << 0x10) & 0xFF0000))))")
def c2(t):
    return t.replace(OLDCOL, TWIN_C2)

# c3: minimal rot-arg guess
TWIN_C3 = "(s32)((color >> 16) | ((color << 16) & 0xFFFF))"
def c3(t):
    return t.replace(OLDCOL, TWIN_C3)

VARIANTS = {
    "v12_c1":     lambda t: c1(t),
    "v13_c1s":    lambda t: swap(c1(t)),
    "v14_c1sd2":  lambda t: d2(swap(c1(t))),
    "v15_c2sd2":  lambda t: d2(swap(c2(t))),
    "v16_c3sd2":  lambda t: d2(swap(c3(t))),
    "v17_c1d2":   lambda t: d2(c1(t)),
}

names = sys.argv[1:] or sorted(VARIANTS)
outs = []
for n in names:
    src = VARIANTS[n](BASE)
    open(f"{HERE}/{n}.cpp", "w").write(src)
    o = f"{HERE}/{n}.o"
    r = subprocess.run(["sh", PCC, f"{HERE}/{n}.cpp", o, "build/GPOE8P/src/pso/misc/TRaderMapCore.o"],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(o):
        print(f"{n}: COMPILE FAIL\n{r.stderr[-400:]}"); continue
    outs.append(o)
if outs:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + outs, capture_output=True, text=True)
    seen = set()
    for ln in r.stdout.splitlines():
        if ln not in seen: print(ln); seen.add(ln)
