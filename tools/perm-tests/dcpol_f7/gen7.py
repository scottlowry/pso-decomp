#!/usr/bin/env python3
"""Round-7: bool-param axis for the 0/1 draw arg (kills the caller-side clrlwi)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
champ = open(os.path.join(HERE, "variants5", "BoTeq.cpp")).read()
VDIR = os.path.join(HERE, "variants7")
os.makedirs(VDIR, exist_ok=True)

DECL_TX = "void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, s32 large);"
DEF_TX = "void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, s32 large) {"
DECL_CU = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);"
B_TXT = DECL_TX.replace("s32 large", "bool large")
B_DEF = DEF_TX.replace("s32 large", "bool large")
B_CU = DECL_CU.replace("s32)", "bool)")


def build(name, subs):
    txt = champ
    for old, new in subs:
        assert old in txt, (name, old[:60])
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


build("t1_bothbool", [(DECL_TX, B_TXT), (DEF_TX, B_DEF), (DECL_CU, B_CU)])
build("t2_cubool", [(DECL_CU, B_CU)])
build("t3_txtbool", [(DECL_TX, B_TXT), (DEF_TX, B_DEF)])
build("t4_t1_swapand", [(DECL_TX, B_TXT), (DEF_TX, B_DEF), (DECL_CU, B_CU),
                        ("cmd = (s16)(cmd & chunk_polygon_flags_and_mask);",
                         "cmd = (s16)(chunk_polygon_flags_and_mask & cmd);")])
build("t5_t1_u32mask", [(DECL_TX, B_TXT), (DEF_TX, B_DEF), (DECL_CU, B_CU),
                        ("extern s32 chunk_polygon_flags_and_mask;", "extern u32 chunk_polygon_flags_and_mask;"),
                        ("extern s32 chunk_polygon_flags_or_mask;", "extern u32 chunk_polygon_flags_or_mask;")])
# t6: keep int params but assign the 0/1 through an int var inside each arm
build("t7_intvar", [("    u32 changed;\n", "    u32 changed;\n    s32 big;\n"),
                    ("info, op == 0x42)", "info, big)"),
                    ("            switch (op) {\n            case 0x40:",
                     "            big = (op == 0x42) ? 1 : 0;\n            switch (op) {\n            case 0x40:")])
# t8: bool for color only + hoisted int big for textured?  (skip) -- instead: u8 arg for color
build("t9_booland_t", [(DECL_TX, B_TXT), (DEF_TX, B_DEF), (DECL_CU, B_CU),
                       ("    s16 t;\n", "    s16 t;\n    s16 unused_t2;\n")])
