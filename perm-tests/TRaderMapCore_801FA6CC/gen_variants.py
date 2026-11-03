#!/opt/homebrew/bin/python3.14
"""Generate draw_compass spelling variants from probe_dc.cpp, compile each with
the repo TU's exact command, score offline. Usage: gen_variants.py [name ...] (default all)"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
BASE = open(f"{HERE}/probe_dc.cpp").read()
PCC = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh"

TWIN = "(s32)(((((color >> 16U) & ~0xFF000000U) | ((color << 16) & 0xFF000000U)) & (~0xFF0000U)) | ((color << 16) & 0xFF0000U))"
OLDCOL = "(s32)((color << 16) | (color >> 16))"

EXTRN = "extern const f64 lbl_8044A7A8;\n"

def stage(idx, toff, tidx):
    # explicit f64 staging minus named bias, tbl operand LEFT (orig fadds order)
    return ("{ u32 stg[2]; stg[0] = 0x43300000U; stg[1] = (u32)(s32)lbl_804C87E4[%d].x ^ 0x80000000U; "
            "state.x = tbl[%d] + (*(f64 *)stg - lbl_8044A7A8); }\n    "
            "{ u32 stg2[2]; stg2[0] = 0x43300000U; stg2[1] = (u32)(s32)lbl_804C87E4[%d].y ^ 0x80000000U; "
            "state.y = tbl[%d] + (*(f64 *)stg2 - lbl_8044A7A8); }") % (idx, tidx, idx, tidx + 1)

def swap(text):
    return (text.replace("state.x = (f32)lbl_804C87E4[1].x + tbl[2];", "state.x = tbl[2] + (f32)lbl_804C87E4[1].x;")
                .replace("state.y = (f32)lbl_804C87E4[1].y + tbl[3];", "state.y = tbl[3] + (f32)lbl_804C87E4[1].y;")
                .replace("state.x = (f32)lbl_804C87E4[0].x + tbl[0];", "state.x = tbl[0] + (f32)lbl_804C87E4[0].x;")
                .replace("state.y = (f32)lbl_804C87E4[0].y + tbl[1];", "state.y = tbl[1] + (f32)lbl_804C87E4[0].y;"))

def bias(text):
    text = text.replace("extern f32 lbl_804C87B4[][4];", "extern f32 lbl_804C87B4[][4];\n" + EXTRN.rstrip() + ";")
    text = text.replace("state.x = (f32)lbl_804C87E4[1].x + tbl[2];\n    state.y = (f32)lbl_804C87E4[1].y + tbl[3];",
                        stage(1, 0, 2))
    text = text.replace("state.x = (f32)lbl_804C87E4[0].x + tbl[0];\n    state.y = (f32)lbl_804C87E4[0].y + tbl[1];",
                        stage(0, 0, 0))
    return text

def twinswap(text):  # twin color + explicit bias WITHOUT tbl-first operand (converted + tbl)
    text = bias(text)
    text = text.replace("state.x = tbl[%d] + (*(f64 *)stg - lbl_8044A7A8); }" % 2, "state.x = (*(f64 *)stg - lbl_8044A7A8) + tbl[2]; }")
    return text

def declflip(text):
    return text.replace(
        "    state.x = TRaderMapCore__data_805DC528;\n"
        "    state.y = TRaderMapCore__data_805DC528;\n"
        "    state.z = TRaderMapCore__data_805DC528;\n"
        "    state.sx = TRaderMapCore__data_805DC534;\n"
        "    state.sy = TRaderMapCore__data_805DC534;",
        "    f32 a = TRaderMapCore__data_805DC528;\n"
        "    f32 b = TRaderMapCore__data_805DC534;\n"
        "    state.x = a;\n"
        "    state.y = a;\n"
        "    state.z = a;\n"
        "    state.sx = b;\n"
        "    state.sy = b;")

def declflip2(text):
    return text.replace(
        "    state.x = TRaderMapCore__data_805DC528;\n"
        "    state.y = TRaderMapCore__data_805DC528;\n"
        "    state.z = TRaderMapCore__data_805DC528;\n"
        "    state.sx = TRaderMapCore__data_805DC534;\n"
        "    state.sy = TRaderMapCore__data_805DC534;",
        "    f32 b = TRaderMapCore__data_805DC534;\n"
        "    f32 a = TRaderMapCore__data_805DC528;\n"
        "    state.x = a;\n"
        "    state.y = a;\n"
        "    state.z = a;\n"
        "    state.sx = b;\n"
        "    state.sy = b;")

VARIANTS = {
    "v01_twin":   lambda t: t.replace(OLDCOL, TWIN),
    "v02_twinswap": lambda t: swap(t.replace(OLDCOL, TWIN)),
    "v03_twinbias": lambda t: bias(t.replace(OLDCOL, TWIN)),
    "v04_twinswbi": lambda t: bias(swap(t.replace(OLDCOL, TWIN))),
    "v05_swap":   lambda t: swap(t),
    "v06_bias":   lambda t: bias(t),
    "v07_twin_d1": lambda t: declflip(t.replace(OLDCOL, TWIN)),
    "v08_twin_d2": lambda t: declflip2(t.replace(OLDCOL, TWIN)),
    "v09_twinsw_d2": lambda t: declflip2(swap(t.replace(OLDCOL, TWIN))),
    "v10_twinswbi_d2": lambda t: declflip2(bias(swap(t.replace(OLDCOL, TWIN)))),
}

names = sys.argv[1:] or sorted(VARIANTS)
out_list = []
for n in names:
    src = VARIANTS[n](BASE)
    if src == BASE:
        print(f"{n}: NO-OP VARIANT (skip)"); continue
    p = f"{HERE}/{n}.cpp"
    open(p, "w").write(src)
    o = f"{HERE}/{n}.o"
    r = subprocess.run(["sh", PCC, p, o, "build/GPOE8P/src/pso/misc/TRaderMapCore.o"],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(o):
        print(f"{n}: COMPILE FAIL\n{r.stderr[-500:]}"); continue
    out_list.append(o)
if out_list:
    r = subprocess.run(["/opt/homebrew/bin/python3.14", f"{HERE}/probe_score.py"] + out_list,
                       capture_output=True, text=True)
    print(r.stdout)
    if r.stderr: print("ERR:", r.stderr[:300])
