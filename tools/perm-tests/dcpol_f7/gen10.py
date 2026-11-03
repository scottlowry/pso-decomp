#!/usr/bin/env python3
"""Round-10: sibling-safe hunt for the last 2 rows + 1 insn.
Base = variants7/t2_cubool.cpp (color callee bool, textured callee s32, cmd s32 + casts,
193+1 insns, bad rows = textured-site clrlwi + extsh r3 pair)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "variants7", "t2_cubool.cpp")).read()
VDIR = os.path.join(HERE, "variants10")
os.makedirs(VDIR, exist_ok=True)

AND_ = "cmd = (s16)(cmd & chunk_polygon_flags_and_mask);"
OR_ = "cmd = (s16)(cmd | chunk_polygon_flags_or_mask);"
SHIFT_ = "cmd = (s16)(cmd >> 8);"
TX = "draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, op == 0x42);"
TDEC = "    s16 t;\n"


def w(name, subs):
    txt = base
    for old, new in subs:
        assert old in txt, (name, old[:50])
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


w("c00_ctl", [])
# --- extsh r3 -> r26 attempts (keep cmd s32) ---
w("c01_andmask_u32", [(AND_, "cmd = (s16)(cmd & (u32)chunk_polygon_flags_and_mask);")])
w("c02_or_mask_cast", [(OR_, "cmd = (s16)(((s32)cmd) | chunk_polygon_flags_or_mask);")])
w("c03_and_or_swap_operand", [(OR_, "cmd = (s16)(chunk_polygon_flags_or_mask | cmd);")])
w("c04_shift_via_t", [(SHIFT_, "cmd = (s16)(t >> 8);\n            t = (s16)cmd;"),
                      (TDEC, TDEC)])
w("c05_store_first", [(AND_ + "\n" + "                " + OR_,
                       "cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n                cmd = cmd | chunk_polygon_flags_or_mask;\n                cmd = (s16)cmd;")])
w("c06_two_and", [(AND_, "cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n                cmd = (s16)cmd;")])
w("c07_wrap_u16", [(AND_, "cmd = (s16)((u16)cmd & (u16)chunk_polygon_flags_and_mask);")])
w("c08_declare_flags_short_chain", [(AND_, "cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n                t = (s16)cmd;"),
                                    (OR_, "cmd = (s16)(t | chunk_polygon_flags_or_mask);")])
# --- textured arg home: try keeping t live to force volatile pressure ---
w("c09_tlive", [(TX, "draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, op == 0x42);\n                t = 0;")])
w("c10_arg_via_t", [(TX, "t = (s16)(op == 0x42);\n                    draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, t);")])
w("c11_arg_via_t32", [("    s16 t;\n", "    s16 t;\n    s32 tt;\n"),
                      (TX, "tt = (op == 0x42);\n                    draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, tt);")])
w("c12_arg_or0", [(TX, TX.replace("op == 0x42", "(op == 0x42) | 0"))])
w("c13_arg_and1", [(TX, TX.replace("op == 0x42", "(op == 0x42) & 1"))])
w("c14_arg_ne0", [(TX, TX.replace("op == 0x42", "(op == 0x42) != 0"))])
w("c15_arg_minus", [(TX, TX.replace("op == 0x42", "(0 != 0x42 - op)"))])
