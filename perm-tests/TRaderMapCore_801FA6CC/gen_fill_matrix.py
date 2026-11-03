#!/opt/homebrew/bin/python3.14
"""gen_fill_matrix.py — filler-position/target probes for the scratch home flip."""
import subprocess, sys, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

CH = open(f"{REPO}/src/pso/misc/TRaderMapCore.cpp").read()
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
BL  = "set_default_alpha_blend__Fv();"
A   = "((u8 *)&color)[3] = (u8)(s32)self->m_19c;"
TBL = "f32 *tbl = lbl_804C87B4[mode];"
FILL = "self->m_19c = self->m_19c;"
CUR = FILL + "\n    " + BL

def sub(t, old, new):
    assert old in t, old[:50]
    return t.replace(old, new, 1)

def place(fill_stmt, anchor_after):
    def f(t):
        t = sub(t, CUR, BL)
        return sub(t, anchor_after, anchor_after + "\n    " + fill_stmt)
    return f

VARIANTS = {
    "f1_after_tbl":  place(FILL, TBL),
    "f2_after_c1x":  place(FILL, C1X),
    "f3_after_bl":   place(FILL, BL),
    "f4_after_a":    place(FILL, A),
    "f5_color_self": sub(BODY, BL, "color = color;\n    " + BL) if False else (lambda t: sub(sub(t, CUR, BL), BL, BL + "\n    color = color;", ) if False else sub(t, CUR + "\n    " + A, FILL + "\n    " + BL + "\n    color = color;\n    " + A)),
    "f6_extra_mode": lambda t: sub(t, CUR, FILL + "\n    s32 mv = mode;\n    " + BL + "\n    mv = mv;"),
}
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
        print(f"{n}: FAIL {r.stderr[-120:]}"); continue
    outs.append(o)
if outs:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + outs,
                       capture_output=True, text=True)
    seen = set()
    for ln in r.stdout.splitlines():
        if ln not in seen: print(ln); seen.add(ln)
    for o in outs:
        out = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d",
                              "--disassemble=draw_compass__13TRaderMapCoreFv", o],
                             capture_output=True, text=True).stdout
        sl = [l.split("\t")[-1].strip() for l in out.splitlines() if "slwi" in l]
        print(os.path.basename(o), "slwi:", sl[:2])
