#!/usr/bin/env python3
"""Round-9: pragma knobs + mask-chain/arg tiebreak probes.
Bases: t1 (cmd s32, casts, both callees bool, 193 rows/2 bad) and
       m1b (cmd s16, compound &/|, cast shift, color callee bool, 194)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
VDIR = os.path.join(HERE, "variants9")
os.makedirs(VDIR, exist_ok=True)
t1 = open(os.path.join(HERE, "variants7", "t1_bothbool.cpp")).read()

PUSH = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\n"
KS = {
    "s_on": PUSH,
    "ocs_off": PUSH + "#pragma opt_common_subs off\n",
    "peep_off": PUSH + "#pragma peephole off\n",
    "sched_delayslot": PUSH + "#pragma scheduling off\n#pragma process_defaults\n",
    "no_dflt": PUSH,
}


def w(name, txt):
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


# pragma swaps on the t1 base
w("t1_ctl", t1)
w("t1_son", t1.replace(PUSH + "void dispatch_chunk_polygon_list", "#pragma push\nvoid dispatch_chunk_polygon_list"))
w("t1_ocs", t1.replace(PUSH, PUSH + "#pragma opt_common_subs off\n"))
w("t1_align2", t1.replace("                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n"
                          "                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);",
                          "                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n"
                          "                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n"
                          "                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);"))
# mask chain via an intermediate that forces a store to cmd
w("t1_twostep", t1.replace("                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n"
                          "                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);",
                          "                cmd &= chunk_polygon_flags_and_mask;\n"
                          "                cmd = (s16)(chunk_polygon_flags_or_mask | (s16)cmd);"))
w("t1_twostep2", t1.replace("                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);\n"
                            "                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);",
                            "                cmd = (s32)(s16)(cmd & chunk_polygon_flags_and_mask);\n"
                            "                cmd = (s32)(s16)(cmd | chunk_polygon_flags_or_mask);"))
# use 'flags' var of type s32 written from cmd (era: in-place r26 chain)
w("t1_flagvar", t1.replace("    s32 cmd;\n", "    s32 cmd;\n    s32 flags;\n")
        .replace("""                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);
                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);
            }
            cmd = (s16)(cmd >> 8);""",
                 """                flags = (s16)(cmd & chunk_polygon_flags_and_mask);
                flags = (s16)(flags | chunk_polygon_flags_or_mask);
            } else {
                flags = cmd;
            }
            flags = (s16)(flags >> 8);"""))
# arg spelling with a u32 param declared for textured via a *second* extern-C name is impossible;
# instead: does the era's unmasked form come from an s8/s16 param? try u8 for textured decl+def
w("t1_u8both", t1.replace("void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, bool large);",
                         "void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, u8 large);")
        .replace("void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, bool large) {",
                 "void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, u8 large) {"))
# bool param + callee use spelled as if/else with an int fmt var (target: cmpwi r26,0 = unmasked read)
w("t1_bool_ifelse", t1.replace("GXSetVtxAttrFmt(0, 0xD, 1, 3, large ? 0xC : 8);",
                              "if (large) {\n        GXSetVtxAttrFmt(0, 0xD, 1, 3, 0xC);\n    } else {\n        GXSetVtxAttrFmt(0, 0xD, 1, 3, 8);\n    }"))
w("t1_bool_not", t1.replace("GXSetVtxAttrFmt(0, 0xD, 1, 3, large ? 0xC : 8);",
                            "GXSetVtxAttrFmt(0, 0xD, 1, 3, !large ? 8 : 0xC);"))
w("t1_bool_eq0", t1.replace("GXSetVtxAttrFmt(0, 0xD, 1, 3, large ? 0xC : 8);",
                            "GXSetVtxAttrFmt(0, 0xD, 1, 3, (large == false) ? 8 : 0xC);"))
