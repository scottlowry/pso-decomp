#!/usr/bin/env python3
"""Materialize spelling variants of dispatch_chunk_polygon_list from the champ TU."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CHAMP = os.path.join(HERE, "probe.cpp")
VDIR = os.path.join(HERE, "variants")
os.makedirs(VDIR, exist_ok=True)

base = open(CHAMP).read()

# --- body fragments (exact strings in the repo TU) ---
DECL_N = "    u32 count;\n    s32 n;\n"
DECL_N2 = "    u32 count;\n"
COLOR_N = "            n = *list++;\n            set_chunk_blend(cmd);\n            submit_chunk_material_color(cmd, list);\n            list += n;\n"
COLOR_OP = "            op = *list++;\n            set_chunk_blend(cmd);\n            submit_chunk_material_color(cmd, list);\n            list += op;\n"
DC_INFO = "            count = *(u16 *)list;\n            info = list[1];\n"
DC_INFO2 = "            info = list[1];\n            count = *(u16 *)list;\n"
MASK3 = """                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);
                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);
            }
            cmd = (s16)(cmd >> 8);
"""
MASK3C = """                cmd &= chunk_polygon_flags_and_mask;
                cmd |= chunk_polygon_flags_or_mask;
            }
            cmd >>= 8;
"""
SUBMIT = "submit_chunk_material_color(cmd, list);"
SUBMIT_M = "submit_chunk_material_color__FUcPs(cmd, list);"
DECL_ALIAS = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\n"
ALIAS = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\nvoid submit_chunk_material_color__FUcPs(s32, s16 *);\n"
EQ = "op == 0x42"
NE = "op != 0x41"
EQCAST = "(s32)(op == 0x42)"
CHANGED = "            changed = (cmd ^ chunk_previous_strip_flags) | chunk_strip_dirty_flags;\n"
CHANGED2 = "            changed = cmd ^ chunk_previous_strip_flags;\n            changed = changed | chunk_strip_dirty_flags;\n"

variants = {
    "v1": [],
    "v2a": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP)],
    "v2b": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2)],
    "v2c": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (MASK3, MASK3C)],
    "v2d": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C)],
    "v3a": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C),
            (SUBMIT, SUBMIT_M), (DECL_ALIAS, ALIAS)],
    "v4a": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C),
            (SUBMIT, SUBMIT_M), (DECL_ALIAS, ALIAS), (CHANGED, CHANGED2)],
    "v5_ne": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C),
              (SUBMIT, SUBMIT_M), (DECL_ALIAS, ALIAS), (EQ, NE)],
    "v5_cast": [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C),
                (SUBMIT, SUBMIT_M), (DECL_ALIAS, ALIAS), (EQ, EQCAST)],
}

pass
for name, subs in []:
    txt = base
    for old, new in subs:
        if old not in txt:
            raise SystemExit(f"{name}: fragment not found: {old[:60]!r}")
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)

# --- round 2: prologue/bank levers built on v4a ---
v4a = base
for old, new in [(DECL_N, DECL_N2), (COLOR_N, COLOR_OP), (DC_INFO, DC_INFO2), (MASK3, MASK3C),
                 (SUBMIT, SUBMIT_M), (DECL_ALIAS, ALIAS), (CHANGED, CHANGED2)]:
    v4a = v4a.replace(old, new)
PRAG = "#pragma push\n#pragma scheduling off\nvoid dispatch_chunk_polygon_list"
LMW = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
PEEP = "#pragma push\n#pragma scheduling off\n#pragma peephole on\nvoid dispatch_chunk_polygon_list"
r2 = {
    "w1_lmw": [(PRAG, LMW)],
    "w2_peep": [(PRAG, PEEP)],
    "w3_both": [(PRAG, LMW.replace("\nvoid", "\n#pragma peephole on\nvoid"))],
}
# rebuild round2 from v4a text: simplest = read variants/v4a.cpp and apply pragma
src4 = open(os.path.join(VDIR, "v4a.cpp")).read()
for nm, pp in [("w1_lmw", LMW), ("w2_peep", PEEP), ("w3_both", LMW.replace("\nvoid dispatch", "\n#pragma peephole on\nvoid dispatch"))]:
    assert PRAG in src4, nm
    open(os.path.join(VDIR, nm + ".cpp"), "w").write(src4.replace(PRAG, pp))
    print("wrote", nm)
