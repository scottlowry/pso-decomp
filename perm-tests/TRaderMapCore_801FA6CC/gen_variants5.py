#!/opt/homebrew/bin/python3.14
"""gen_variants5.py — hybrid orderings. p2-p4 on v14 base; p5-p7 on 310-1 base."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
V14 = open(f"{HERE}/v14_c1sd2.cpp").read()
C310 = open(f"{HERE}/perm/output-310-1/source.c").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

B1X = "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;"
B1Y = "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;"
B1 = B1X + "\n    " + B1Y
B1P = "state.x = tbl[2] + ((f32) lbl_804C87E4[1].x);\n  state.y = tbl[3] + ((f32) lbl_804C87E4[1].y);"
A = "((u8 *)&color)[3] = (u8)(s32)self->m_19c;"
AP = "((u8 *) (&color))[3] = (u8) ((s32) self->m_19c);"
BL = "set_default_alpha_blend__Fv();"
TBL = "f32 *tbl = lbl_804C87B4[mode];"

def sub(t, old, new):
    assert old in t, old[:60]
    return t.replace(old, new)

def p2(t):  # alpha, conv, blend  (v14 base)
    return sub(t, B1 + "\n    " + BL + "\n    " + A, A + "\n    " + B1 + "\n    " + BL)

def p3(t):  # hoisted f32 av read before conv; store after blend
    return sub(t, B1 + "\n    " + BL + "\n    " + A,
               "f32 av = self->m_19c;\n    " + B1 + "\n    " + BL + "\n    ((u8 *)&color)[3] = (u8)(s32)av;")

def p4(t):  # blend, conv, alpha (v14 base)
    return sub(t, B1 + "\n    " + BL + "\n    " + A, BL + "\n    " + B1 + "\n    " + A)

def p5(t):  # 310 base: alpha BEFORE tbl+conv window, blend after conv
    old = TBL + "\n  " + B1P + "\n  " + AP + "\n  " + BL
    new = AP + "\n  " + TBL + "\n  " + B1P + "\n  " + BL
    return sub(t, old, new)

def p6(t):  # 310 base: alpha between convx and convy
    old = B1P + "\n  " + AP + "\n  " + BL
    new = "state.x = tbl[2] + ((f32) lbl_804C87E4[1].x);\n  " + AP + "\n  state.y = tbl[3] + ((f32) lbl_804C87E4[1].y);\n  " + BL
    return sub(t, old, new)

def p7(t):  # 310 base: blend before alpha, i.e. conv, blend, alpha (revert to v14 tail but keep 310 paren style)
    old = B1P + "\n  " + AP + "\n  " + BL
    new = B1P + "\n  " + BL + "\n  " + AP
    return sub(t, old, new)

VARIANTS = {"y02": (V14, p2), "y03": (V14, p3), "y04": (V14, p4),
            "y05": (C310, p5), "y06": (C310, p6), "y07": (C310, p7)}

names = sys.argv[1:] or sorted(VARIANTS)
outs = []
for n in names:
    base, fn = VARIANTS[n]
    try:
        src = fn(base)
    except AssertionError as e:
        print(f"{n}: PATTERN MISS {e}"); continue
    if base is not V14:
        src = 'extern "C" {\n' + src + '\n}\n'
    open(f"{HERE}/{n}.cpp", "w").write(src)
    o = f"{HERE}/{n}.o"
    r = subprocess.run(["sh", PCC, f"{HERE}/{n}.cpp", o, "build/GPOE8P/src/pso/misc/TRaderMapCore.o"],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(o):
        print(f"{n}: COMPILE FAIL {r.stderr[-150:]}"); continue
    outs.append(o)
if outs:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + outs, capture_output=True, text=True)
    seen = set()
    for ln in r.stdout.splitlines():
        if ln not in seen: print(ln); seen.add(ln)
