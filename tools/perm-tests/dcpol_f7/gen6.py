#!/usr/bin/env python3
"""Round-6: micro-variants on top of BoTeq (order B, s32 cmd, op-reuse color arm,
info via s16 temp, lmw off, 0x800 bit, two-stmt changed)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
champ = open(os.path.join(HERE, "variants5", "BoTeq.cpp")).read()
VDIR = os.path.join(HERE, "variants6")
os.makedirs(VDIR, exist_ok=True)

EQCALL = "info, op == 0x42)"
TERCALL = "info, (op == 0x42) ? 1 : 0)"
AND_OR = """                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);
                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);
"""


def build(name, subs, src=None):
    txt = src if src is not None else champ
    for old, new in subs:
        assert old in txt, (name, old[:60])
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


build("b0", [])  # control == BoTeq
build("b1_ter", [(EQCALL, TERCALL)])
# swap operand order of the and
build("b2_swapand", [("cmd = (s16)(cmd & chunk_polygon_flags_and_mask);",
                      "cmd = (s16)(chunk_polygon_flags_and_mask & cmd);")])
build("b3_swapor", [("cmd = (s16)(cmd | chunk_polygon_flags_or_mask);",
                     "cmd = (s16)(chunk_polygon_flags_or_mask | cmd);")])
build("b4_both_swap", [("cmd = (s16)(cmd & chunk_polygon_flags_and_mask);",
                        "cmd = (s16)(chunk_polygon_flags_and_mask & cmd);"),
                       ("cmd = (s16)(cmd | chunk_polygon_flags_or_mask);",
                        "cmd = (s16)(chunk_polygon_flags_or_mask | cmd);")])
# global types u32
build("b5_u32masks", [("extern s32 chunk_polygon_flags_and_mask;", "extern u32 chunk_polygon_flags_and_mask;"),
                      ("extern s32 chunk_polygon_flags_or_mask;", "extern u32 chunk_polygon_flags_or_mask;")])
# t as s32
build("b6_t_s32", [("    s16 t;\n", "    s32 t;\n")])
# op as s32 (still clrlwi+extsh? no: assigning int -> no extsh) - control test
build("b7_op_s32", [("    s16 op;\n", "    s32 op;\n")])
# slot removed (inline index)
build("b8_noslot", [("    s16 slot;\n", ""),
                    ("slot = (cmd >> 8) & 0xFF;\n                chunk_polygon_list_cache[slot] = list;",
                     "chunk_polygon_list_cache[(cmd >> 8) & 0xFF] = list;"),
                    ("slot = (cmd >> 8) & 0xFF;\n                dispatch_chunk_polygon_list(chunk_polygon_list_cache[slot], buffer);",
                     "dispatch_chunk_polygon_list(chunk_polygon_list_cache[(cmd >> 8) & 0xFF], buffer);")])
# changed as s32
build("b9_changed_s32", [("    u32 changed;\n", "    s32 changed;\n")])
# count as s32 (lhz still?) control
build("b10_count_s32", [("    u32 count;\n", "    s32 count;\n")])
# hoist the info temp def one line earlier (before count)
build("b11_tfirst", [("""            count = *(u16 *)list;
            t = list[1];""", """            t = list[1];
            count = *(u16 *)list;""")])
# assign info from a u16-typed temp
build("b12_t_u16", [("    s16 t;\n", "    u16 t;\n")])
# buffer typed as a pointer (removes casts)
build("b13_bufptr", [("void dispatch_chunk_polygon_list(s16 *list, s32 buffer) {",
                      "void dispatch_chunk_polygon_list(s16 *list, void *buffer) {"),
                     ("(Vtx_803E46FC *)buffer", "buffer"), ("(Vtx_803E36C4 *)buffer", "buffer"),
                     ("(Vtx_803E47E0 *)buffer", "buffer"), ("(Vtx_803E352C *)buffer", "buffer"),
                     ("(void *)buffer", "buffer"),
                     ("void dispatch_chunk_polygon_list(s16*, s32);", "void dispatch_chunk_polygon_list(s16*, void *);"),
                     ("if (model->polygons) dispatch_chunk_polygon_list(model->polygons, cache);",
                      "if (model->polygons) dispatch_chunk_polygon_list(model->polygons, (void *)cache);")])
# b14: ternary + u32 masks combined
build("b14_ter_u32", [(EQCALL, TERCALL),
                      ("extern s32 chunk_polygon_flags_and_mask;", "extern u32 chunk_polygon_flags_and_mask;"),
                      ("extern s32 chunk_polygon_flags_or_mask;", "extern u32 chunk_polygon_flags_or_mask;")])
# b15: assign-and-or through one expression with an inner s16 cast
build("b15_oneline", [(AND_OR, """                cmd = (s16)((s16)(cmd & chunk_polygon_flags_and_mask) | chunk_polygon_flags_or_mask);
""")])
