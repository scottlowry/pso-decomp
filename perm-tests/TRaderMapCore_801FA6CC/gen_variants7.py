#!/opt/homebrew/bin/python3.14
"""gen_variants7.py — scratch r5/r6 home-flip probes on the pool-form champ (99.63)."""
import subprocess, sys, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
CH = open(f"{REPO}/src/pso/misc/TRaderMapCore.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

m = re.search(r"void draw_compass__13TRaderMapCoreFv\(TRaderMapCore \*self, s32 mode\) \{.*?\n\}", CH, re.S)
BODY = m.group(0)
BODY = (BODY.replace("(TRaderMapCore *)&self->m_90", "(void *)&self->m_90")
            .replace("TRaderMapCore *self", "RM *self")
            .replace("CompassState_801FA7E8 state", "CS state")
            .replace("state.unk8", "state.z")
            .replace("TParticleCtrl::begin_effect_render()", "begin_effect_render__13TParticleCtrlFv()")
            .replace("TParticleCtrl::end_effect_render()", "end_effect_render__13TParticleCtrlFv()")
            .replace("set_default_alpha_blend()", "set_default_alpha_blend__Fv()")
            .replace("set_additive_blend()", "set_additive_blend__Fv()")
            .replace("((TObjPlayer *)&state)->draw_compass_sprite(1, ", "draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 1, ")
            .replace("((TObjPlayer *)&state)->draw_compass_sprite(0, ", "draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 0, "))
HEAD = open(f"{HERE}/perm/base.c").read().split("void draw_compass__13")[0]

C1X = "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;"
C1Y = "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;"
C2X = "state.x = tbl[0] + (f32)lbl_804C87E4[0].x;"
C2Y = "state.y = tbl[1] + (f32)lbl_804C87E4[0].y;"
TBL = "f32 *tbl = lbl_804C87B4[mode];"
FILL = "self->m_19c = self->m_19c;"

def sub(t, old, new):
    assert old in t, old[:60]
    return t.replace(old, new)

def w1(t):  # lfs results into temps (both blocks)
    t = sub(t, C1X + "\n    " + C1Y,
            "f32 t2 = tbl[2];\n    f32 t3 = tbl[3];\n    state.x = t2 + (f32)lbl_804C87E4[1].x;\n    state.y = t3 + (f32)lbl_804C87E4[1].y;")
    t = sub(t, C2X + "\n    " + C2Y,
            "f32 t0 = tbl[0];\n    f32 t1 = tbl[1];\n    state.x = t0 + (f32)lbl_804C87E4[0].x;\n    state.y = t1 + (f32)lbl_804C87E4[0].y;")
    return t

def w2(t):  # temps block1 only
    return sub(t, C1X + "\n    " + C1Y,
               "f32 t2 = tbl[2];\n    f32 t3 = tbl[3];\n    state.x = t2 + (f32)lbl_804C87E4[1].x;\n    state.y = t3 + (f32)lbl_804C87E4[1].y;")

def w3(t):  # y-conv flipped back to conv+tbl order in block1 only (pressure asymmetry)
    return sub(t, C1Y, "state.y = (f32)lbl_804C87E4[1].y + tbl[3];")

def w4(t):  # fill self-assign moved between convx and convy
    return sub(sub(t, "\n    " + FILL, ""), C1X, C1X + "\n    " + FILL)

def w5(t):  # dup-fill: two fillers around blend
    return sub(t, FILL, FILL + "\n    s32 md = mode;")

def w6(t):  # index via separate s32 row offset var (keeps tbl arithmetic but named shift var)
    return sub(t, TBL, "s32 ro = mode << 4;\n    f32 *tbl = (f32 *)(ro + (u8 *)lbl_804C87B4);")

VARIANTS = {"u01": w1, "u02": w2, "u03": w3, "u04": w4, "u05": w5, "u06": w6}
names = sys.argv[1:] or sorted(VARIANTS)
outs = []
for n in names:
    try:
        body = VARIANTS[n](BODY)
    except AssertionError as e:
        print(f"{n}: MISS {e}"); continue
    src = 'extern "C" {\n' + HEAD + body + "\n}\n"
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
    for o in outs:
        out = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump","-d","--disassemble=draw_compass__13TRaderMapCoreFv",o],capture_output=True,text=True).stdout
        sl = [l.split("\t")[1].strip() for l in out.splitlines() if "slwi" in l or re.search(r"\tadd\s", l)]
        print(os.path.basename(o), "->", sl[:4])
