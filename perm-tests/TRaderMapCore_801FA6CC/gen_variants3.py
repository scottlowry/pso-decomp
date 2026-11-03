#!/opt/homebrew/bin/python3.14
"""gen_variants3.py — conversion-block ordering variants on the v14 base."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
BASE = open(f"{HERE}/v14_c1sd2.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

B1X = "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;"
B1Y = "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;"
B2X = "state.x = tbl[0] + (f32)lbl_804C87E4[0].x;"
B2Y = "state.y = tbl[1] + (f32)lbl_804C87E4[0].y;"

def repl(t, pairs):
    for a, b in pairs:
        assert a in t, a
        t = t.replace(a, b)
    return t

# W1: named f32 temps per block, stores after
def w1(t):
    return repl(t, [
        (B1X + "\n    " + B1Y,
         "f32 fx = tbl[2] + (f32)lbl_804C87E4[1].x;\n"
         "    f32 fy = tbl[3] + (f32)lbl_804C87E4[1].y;\n"
         "    state.x = fx;\n    state.y = fy;"),
        (B2X + "\n    " + B2Y,
         "f32 gx = tbl[0] + (f32)lbl_804C87E4[0].x;\n"
         "    f32 gy = tbl[1] + (f32)lbl_804C87E4[0].y;\n"
         "    state.x = gx;\n    state.y = gy;"),
    ])

# W2: s16 -> s32 temps first, then conversion at use
def w2(t):
    return repl(t, [
        (B1X + "\n    " + B1Y,
         "s32 ix = lbl_804C87E4[1].x;\n"
         "    s32 iy = lbl_804C87E4[1].y;\n"
         "    state.x = tbl[2] + (f32)ix;\n"
         "    state.y = tbl[3] + (f32)iy;"),
        (B2X + "\n    " + B2Y,
         "s32 jx = lbl_804C87E4[0].x;\n"
         "    s32 jy = lbl_804C87E4[0].y;\n"
         "    state.x = tbl[0] + (f32)jx;\n"
         "    state.y = tbl[1] + (f32)jy;"),
    ])

# W3: conversion via temps for x only before y expr
def w3(t):
    return repl(t, [
        (B1X + "\n    " + B1Y,
         "f32 cx = (f32)lbl_804C87E4[1].x;\n"
         "    f32 cy = (f32)lbl_804C87E4[1].y;\n"
         "    state.x = tbl[2] + cx;\n"
         "    state.y = tbl[3] + cy;"),
        (B2X + "\n    " + B2Y,
         "f32 dx = (f32)lbl_804C87E4[0].x;\n"
         "    f32 dy = (f32)lbl_804C87E4[0].y;\n"
         "    state.x = tbl[0] + dx;\n"
         "    state.y = tbl[1] + dy;"),
    ])

# W4: y-expr BEFORE x-expr, stores x then y
def w4(t):
    return repl(t, [
        (B1X + "\n    " + B1Y,
         "f32 fy = tbl[3] + (f32)lbl_804C87E4[1].y;\n"
         "    f32 fx = tbl[2] + (f32)lbl_804C87E4[1].x;\n"
         "    state.x = fx;\n    state.y = fy;"),
        (B2X + "\n    " + B2Y,
         "f32 gy = tbl[1] + (f32)lbl_804C87E4[0].y;\n"
         "    f32 gx = tbl[0] + (f32)lbl_804C87E4[0].x;\n"
         "    state.x = gx;\n    state.y = gy;"),
    ])

# W5: y computed and stored first (store order flipped too — risky, tests pairing)
def w5(t):
    return repl(t, [
        (B1X + "\n    " + B1Y,
         "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;\n"
         "    state.x = tbl[2] + (f32)lbl_804C87E4[1].x;"),
        (B2X + "\n    " + B2Y,
         "state.y = tbl[1] + (f32)lbl_804C87E4[0].y;\n"
         "    state.x = tbl[0] + (f32)lbl_804C87E4[0].x;"),
    ])

VARIANTS = {
    "w01": w1, "w02": w2, "w03": w3, "w04": w4, "w05": w5,
    "w06": lambda t: repl(t, [
        (B1X + "\n    " + B1Y,
         "s32 ix = lbl_804C87E4[1].x;\n"
         "    s32 iy = lbl_804C87E4[1].y;\n"
         "    f32 cx = (f32)ix;\n"
         "    f32 cy = (f32)iy;\n"
         "    state.x = tbl[2] + cx;\n"
         "    state.y = tbl[3] + cy;"),
    ]),
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
        print(f"{n}: COMPILE FAIL {r.stderr[-300:]}"); continue
    outs.append(o)
if outs:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + outs, capture_output=True, text=True)
    seen = set()
    for ln in r.stdout.splitlines():
        if ln not in seen: print(ln); seen.add(ln)
