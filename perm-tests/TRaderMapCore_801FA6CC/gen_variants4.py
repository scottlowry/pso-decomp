#!/opt/homebrew/bin/python3.14
"""gen_variants4.py — deeper block-1 ordering probes on v14 base."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
BASE = open(f"{HERE}/v14_c1sd2.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

B1 = "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;\n    state.y = tbl[3] + (f32)lbl_804C87E4[1].y;"
B2 = "state.x = tbl[0] + (f32)lbl_804C87E4[0].x;\n    state.y = tbl[1] + (f32)lbl_804C87E4[0].y;"
TBL = "f32 *tbl = lbl_804C87B4[mode];\n    "

def x2(t):  # inline-index tbl at every use (no hoisted pointer var)
    t = t.replace("f32 *tbl = lbl_804C87B4[mode];\n    state.x = tbl[2]", "state.x = lbl_804C87B4[mode][2]")
    t = t.replace("state.y = tbl[3]", "state.y = lbl_804C87B4[mode][3]")
    t = t.replace("state.x = tbl[0]", "state.x = lbl_804C87B4[mode][0]")
    t = t.replace("state.y = tbl[1]", "state.y = lbl_804C87B4[mode][1]")
    return t

def x3(t):  # convert temps interleaved: x-conv, store x, y-conv, store y
    t = t.replace(B1, "f32 cx1 = (f32)lbl_804C87E4[1].x;\n    state.x = tbl[2] + cx1;\n"
                      "    f32 cy1 = (f32)lbl_804C87E4[1].y;\n    state.y = tbl[3] + cy1;")
    t = t.replace(B2, "f32 cx2 = (f32)lbl_804C87E4[0].x;\n    state.x = tbl[0] + cx2;\n"
                      "    f32 cy2 = (f32)lbl_804C87E4[0].y;\n    state.y = tbl[1] + cy2;")
    return t

def x4(t):  # conv temps for BOTH fields before either store
    t = t.replace(B1, "f32 cx1 = (f32)lbl_804C87E4[1].x;\n    f32 cy1 = (f32)lbl_804C87E4[1].y;\n"
                      "    state.x = tbl[2] + cx1;\n    state.y = tbl[3] + cy1;")
    t = t.replace(B2, "f32 cx2 = (f32)lbl_804C87E4[0].x;\n    f32 cy2 = (f32)lbl_804C87E4[0].y;\n"
                      "    state.x = tbl[0] + cx2;\n    state.y = tbl[1] + cy2;")
    return t

def x5(t):  # x fully (conv+store) BEFORE y begins, with s32 loads split out
    t = t.replace(B1, "s32 fx1 = lbl_804C87E4[1].x;\n    state.x = tbl[2] + (f32)fx1;\n"
                      "    s32 fy1 = lbl_804C87E4[1].y;\n    state.y = tbl[3] + (f32)fy1;")
    t = t.replace(B2, "s32 gx1 = lbl_804C87E4[0].x;\n    state.x = tbl[0] + (f32)gx1;\n"
                      "    s32 gy1 = lbl_804C87E4[0].y;\n    state.y = tbl[1] + (f32)gy1;")
    return t

def x6(t):  # hoist state.x store expression through pointer alias CS *sp
    t = t.replace("CS state;\n", "CS state;\n    CS *sp;\n")
    t = t.replace(TBL + B1, TBL + "sp = &state;\n    " + B1.replace("state.x", "sp->x").replace("state.y", "sp->y"))
    return t

VARIANTS = {"x02": x2, "x03": x3, "x04": x4, "x05": x5, "x06": x6}

names = sys.argv[1:] or sorted(VARIANTS)
outs = []
for n in names:
    src = VARIANTS[n](BASE)
    if src == BASE:
        print(f"{n}: NO-OP"); continue
    open(f"{HERE}/{n}.cpp", "w").write(src)
    o = f"{HERE}/{n}.o"
    r = subprocess.run(["sh", PCC, f"{HERE}/{n}.cpp", o, "build/GPOE8P/src/pso/misc/TRaderMapCore.o"],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(o):
        print(f"{n}: COMPILE FAIL {r.stderr[-200:]}"); continue
    outs.append(o)
if outs:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + outs, capture_output=True, text=True)
    seen = set()
    for ln in r.stdout.splitlines():
        if ln not in seen: print(ln); seen.add(ln)
