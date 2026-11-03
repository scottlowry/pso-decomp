#!/usr/bin/env python3
"""Round-11: register-hint spellings on the sibling-safe 194 base (t2_cubool)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "variants7", "t2_cubool.cpp")).read()
VDIR = os.path.join(HERE, "variants11")
os.makedirs(VDIR, exist_ok=True)

DECLS = """    s32 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 info;
    u32 changed;
    s16 t;
"""
SIG = "void dispatch_chunk_polygon_list(s16 *list, s32 buffer) {"


def w(name, subs):
    txt = base
    for old, new in subs:
        assert old in txt, (name, old[:50])
        txt = txt.replace(old, new)
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


w("r00_ctl", [])
w("r01_reg_all", [(DECLS, DECLS.replace("    s", "    register s").replace("    u", "    register u")),
                  (SIG, "void dispatch_chunk_polygon_list(register s16 *list, register s32 buffer) {")])
w("r02_reg_cmd", [(DECLS, DECLS.replace("    s32 cmd;", "    register s32 cmd;"))])
w("r03_reg_param", [(SIG, "void dispatch_chunk_polygon_list(register s16 *list, register s32 buffer) {")])
w("r04_reg_locals_noparam", [(DECLS, DECLS.replace("    s", "    register s").replace("    u", "    register u"))])
w("r05_reg_cmdop", [(DECLS, DECLS.replace("    s32 cmd;", "    register s32 cmd;").replace("    s16 op;", "    register s16 op;"))])
w("r06_reg_ci", [(DECLS, DECLS.replace("    u32 count;", "    register u32 count;").replace("    s32 info;", "    register s32 info;"))])
