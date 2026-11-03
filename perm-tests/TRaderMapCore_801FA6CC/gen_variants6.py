#!/opt/homebrew/bin/python3.14
"""gen_variants6.py — scratch-renumber probes (slwi/add r5->r6) on the 99.63 champ."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
CH = open(f"{REPO}/src/pso/misc/TRaderMapCore.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

# extract fn body, C-ify (same transforms as base.c re-root)
import re
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

TBL = "f32 *tbl = lbl_804C87B4[mode];"

def sub(t, old, new):
    assert old in t, old[:70]
    return t.replace(old, new)

def z1(t):  # mode self-assign before tbl
    return sub(t, TBL, "mode = mode;\n    " + TBL)

def z2(t):  # explicit shift var
    return sub(t, TBL, "s32 sh = mode << 4;\n    f32 *tbl = (f32 *)lbl_804C87B4 + sh;")

def z3(t):  # byte-pointer arithmetic
    return sub(t, TBL, "f32 *tbl = (f32 *)((u8 *)lbl_804C87B4 + (mode << 4));")

def z4(t):  # tbl via int index cast on flat base
    return sub(t, TBL, "f32 *tbl = &(lbl_804C87B4[mode][0]);")

def z5(t):  # filler s32 self-assign of m_174 near frame-base re-materialize
    return sub(t, "begin_effect_render__13TParticleCtrlFv();\n    " + TBL,
                  "begin_effect_render__13TParticleCtrlFv();\n    self->m_174 = self->m_174;\n    " + TBL)

def z6(t):  # move state.sprs store later (freed r3?) — sprs store right before tbl
    return sub(sub(t, "    state.sprs = lbl_804C87E4;\n", ""),
                  TBL, "    state.sprs = lbl_804C87E4;\n    " + TBL)

VARIANTS = {"z01": z1, "z02": z2, "z03": z3, "z04": z4, "z05": z5, "z06": z6}
names = sys.argv[1:] or sorted(VARIANTS)
outs = []
for n in names:
    try:
        body = VARIANTS[n](BODY)
    except AssertionError as e:
        print(f"{n}: MISS {e}"); continue
    src = HEAD + body + "\n"
    src = 'extern "C" {\n' + src + '\n}\n'
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
