#!/usr/bin/env python3
"""Round-4 grid: bit-fix + peephole axis + decl-order axis."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "probe.cpp")).read()
VDIR = os.path.join(HERE, "variants4")
os.makedirs(VDIR, exist_ok=True)

DECLS = """    s16 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 n;
    s32 info;
    s32 changed;
"""
MASK = """                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);
                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);
            }
            cmd = (s16)(cmd >> 8);
"""
MASKC = """                cmd &= chunk_polygon_flags_and_mask;
                cmd |= chunk_polygon_flags_or_mask;
            }
            cmd >>= 8;
"""
BIT_OLD = "if ((u32)(model_render_flags & 0x80000) != 0) {\n                cmd"
BIT_NEW = "if ((u32)(model_render_flags & 0x800) != 0) {\n                cmd"
SUBMIT = "            submit_chunk_material_color(cmd, list);\n"
SUBMIT_M = "            submit_chunk_material_color__FUcPs(cmd, list);\n"
ALIAS_OLD = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\n"
ALIAS_NEW = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\nvoid submit_chunk_material_color__FUcPs(s32, s16 *);\n"
CHANGE = "            changed = (cmd ^ chunk_previous_strip_flags) | chunk_strip_dirty_flags;\n"
CHANGE2 = "            changed = cmd ^ chunk_previous_strip_flags;\n            changed = changed | chunk_strip_dirty_flags;\n"
PRAG = "#pragma push\n#pragma scheduling off\nvoid dispatch_chunk_polygon_list"
LMW = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
LMWP = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\n#pragma peephole on\nvoid dispatch_chunk_polygon_list"

common = [
    (MASK, MASKC),
    (BIT_OLD, BIT_NEW),
    (SUBMIT, SUBMIT_M),
    (ALIAS_OLD, ALIAS_NEW),
    (CHANGE, CHANGE2),
    (PRAG, LMW),
]

ORDER = {
    "d0": DECLS,
    "d1": """    s16 cmd;
    s16 op;
    s16 slot;
    s32 info;
    u32 count;
    s32 n;
    s32 changed;
""",
    "d2": """    s16 cmd;
    s32 n;
    u32 count;
    s32 info;
    s16 op;
    s16 slot;
    s32 changed;
""",
    "d3": """    s32 changed;
    s32 info;
    u32 count;
    s32 n;
    s16 slot;
    s16 op;
    s16 cmd;
""",
}


def build(name, pragma, declkey, extra=()):
    txt = base
    subs = common + [(PRAG + "X", "IMPOSSIBLE")] if False else [s for s in common if s[0] != PRAG]
    txt = txt.replace(PRAG, pragma)
    for old, new in subs:
        assert old in txt, (name, old[:50])
        txt = txt.replace(old, new)
    txt = txt.replace(DECLS, ORDER[declkey])
    for old, new in extra:
        assert old in txt, (name, old[:50])
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)


for pk, pv in [("lmw", LMW), ("peep", LMWP)]:
    for dk in ORDER:
        build(f"{pk}_{dk}", pv, dk)
print("wrote", len(os.listdir(VDIR)), "variants")
