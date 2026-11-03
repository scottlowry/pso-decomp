#!/usr/bin/env python3
"""Round-3 variant grid for dispatch_chunk_polygon_list (callee-bank hunt)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "probe.cpp")).read()
VDIR = os.path.join(HERE, "variants3")
os.makedirs(VDIR, exist_ok=True)

DECLS = """    s16 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 n;
    s32 info;
    s32 changed;
"""
DECLS6 = """    s16 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 info;
    s32 changed;
"""
COLOR = """            n = *list++;
            set_chunk_blend(cmd);
            submit_chunk_material_color(cmd, list);
            list += n;
"""
COLOR_OP = """            op = *list++;
            set_chunk_blend(cmd);
            submit_chunk_material_color__FUcPs(cmd, list);
            list += op;
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
FMASKC = """                flags &= chunk_polygon_flags_and_mask;
                flags |= chunk_polygon_flags_or_mask;
            }
            flags >>= 8;
"""
CHANGE = "            changed = (cmd ^ chunk_previous_strip_flags) | chunk_strip_dirty_flags;\n"
CHANGE2 = "            changed = cmd ^ chunk_previous_strip_flags;\n            changed = changed | chunk_strip_dirty_flags;\n"
FCHANGE2 = "            changed = flags ^ chunk_previous_strip_flags;\n            changed = changed | chunk_strip_dirty_flags;\n"
SUBMIT = "            submit_chunk_material_color(cmd, list);\n"
SUBMIT_M = "            submit_chunk_material_color__FUcPs(cmd, list);\n"
ALIAS_OLD = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\n"
ALIAS_NEW = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\nvoid submit_chunk_material_color__FUcPs(s32, s16 *);\n"
PRAG = "#pragma push\n#pragma scheduling off\nvoid dispatch_chunk_polygon_list"
LMW = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
PEEP = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\n#pragma peephole on\nvoid dispatch_chunk_polygon_list"
SLOTDECL = "    s16 slot;\n"

common = [
    (DECLS, DECLS6),
    (COLOR, COLOR_OP),
    (MASK, MASKC),
    (ALIAS_OLD, ALIAS_NEW),
    (CHANGE, CHANGE2),
    (PRAG, LMW),
]
# pieces that reference the draw-arm flags value (used by x3 to rename)
USES = []


def rep(txt, old, new):
    if old not in txt:
        raise SystemExit("MISSING: " + old[:70])
    return txt.replace(old, new)


def build(name, extra):
    txt = base
    for old, new in common + extra:
        txt = rep(txt, old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


build("r0", [])
build("r0_peep", [(LMW, PEEP)])
# x1: keep a separate 'n' local in the color arm
build("x1_sepN", [(DECLS6, DECLS), (COLOR_OP, COLOR.replace("submit_chunk_material_color(cmd", "submit_chunk_material_color__FUcPs(cmd"))])
# x3: separate 'flags' var; cmd untouched after the loop head
build("x3_flagsvar", [
    (MASKC, FMASKC),
    ("            count = *(u16 *)list;\n", "            s16 flags = cmd;\n            count = *(u16 *)list;\n"),
    ("            changed = cmd ^ chunk_previous_strip_flags;", "            changed = flags ^ chunk_previous_strip_flags;"),
    ("            chunk_previous_strip_flags = cmd;", "            chunk_previous_strip_flags = flags;"),
    ("set_strip_lighting_chan_ctrl(cmd);", "set_strip_lighting_chan_ctrl(flags);"),
    ("if ((cmd & 0x40) != 0) {", "if ((flags & 0x40) != 0) {"),
    ("set_chunk_blend_depth_mode(cmd, 1);", "set_chunk_blend_depth_mode(flags, 1);"),
    ("set_chunk_blend_depth_mode(cmd, 0);", "set_chunk_blend_depth_mode(flags, 0);"),
])
# x5: no 'slot' variable
build("x5_noslot", [
    (SLOTDECL, ""),
    ("                slot = (cmd >> 8) & 0xFF;\n                chunk_polygon_list_cache[slot] = list;",
     "                chunk_polygon_list_cache[(cmd >> 8) & 0xFF] = list;"),
    ("                slot = (cmd >> 8) & 0xFF;\n                dispatch_chunk_polygon_list(chunk_polygon_list_cache[slot], buffer);",
     "                dispatch_chunk_polygon_list(chunk_polygon_list_cache[(cmd >> 8) & 0xFF], buffer);"),
])
# x8 / x9: type tweaks
build("x8_infou32", [("    s32 info;", "    u32 info;")])
build("x9_count32", [("    u32 count;", "    s32 count;")])
build("x10_ops32", [("    s16 op;", "    s32 op;")])
# x6: draw-arm switch -> if chain
build("x6_ifdraw", [
    ("""            switch (op) {
            case 0x40:
                if""", """            if (op == 0x40) {
                if"""),
    ("""                }
                break;
            case 0x41:
            case 0x42:
                set_chunk_blend_depth_mode(cmd, 1);""",
     """                }
            } else if (op == 0x41 || op == 0x42) {
                set_chunk_blend_depth_mode(cmd, 1);"""),
    ("""                    draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, op == 0x42);
                }
                break;
            }""",
     """                    draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, op == 0x42);
                }
            }"""),
])
# x7: small-op switch -> if chain
build("x7_ifsmall", [
    ("""            switch (op) {
            case 1:
                set_chunk_blend(cmd);
                break;
            case 4:""", """            if (op == 4) {"""),
    ("""                lbl_805D7798++;
                return;
            case 5:
                slot""", """                lbl_805D7798++;
                return;
            }
            if (op == 5) {
                slot"""),
    ("""                lbl_805D7798--;
                break;
            }""", """                lbl_805D7798--;
            } else if (op == 1) {
                set_chunk_blend(cmd);
            }"""),
])
# x11: x3 + x5 combined
build("x11_fx3x5", [
    (MASKC, FMASKC),
    ("            count = *(u16 *)list;\n", "            s16 flags = cmd;\n            count = *(u16 *)list;\n"),
    ("            changed = cmd ^ chunk_previous_strip_flags;", "            changed = flags ^ chunk_previous_strip_flags;"),
    ("            chunk_previous_strip_flags = cmd;", "            chunk_previous_strip_flags = flags;"),
    ("set_strip_lighting_chan_ctrl(cmd);", "set_strip_lighting_chan_ctrl(flags);"),
    ("if ((cmd & 0x40) != 0) {", "if ((flags & 0x40) != 0) {"),
    ("set_chunk_blend_depth_mode(cmd, 1);", "set_chunk_blend_depth_mode(flags, 1);"),
    ("set_chunk_blend_depth_mode(cmd, 0);", "set_chunk_blend_depth_mode(flags, 0);"),
    (SLOTDECL, ""),
    ("                slot = (cmd >> 8) & 0xFF;\n                chunk_polygon_list_cache[slot] = list;",
     "                chunk_polygon_list_cache[(cmd >> 8) & 0xFF] = list;"),
    ("                slot = (cmd >> 8) & 0xFF;\n                dispatch_chunk_polygon_list(chunk_polygon_list_cache[slot], buffer);",
     "                dispatch_chunk_polygon_list(chunk_polygon_list_cache[(cmd >> 8) & 0xFF], buffer);"),
])
