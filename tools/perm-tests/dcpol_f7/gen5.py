#!/usr/bin/env python3
"""Round-5 grid (16 variants): s32 cmd + op/color, info temp, big-arg form, decl order."""
import itertools
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "probe.cpp")).read()
VDIR = os.path.join(HERE, "variants5")
os.makedirs(VDIR, exist_ok=True)

DECL_CHAMP = """    s16 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 n;
    s32 info;
    s32 changed;
"""
SLOT = "    s16 slot;\n"
BIGDECL = "    s32 big;\n"

ORD = {
    "A_n": """    s32 cmd;
    s16 op;
    s16 slot;
    s32 n;
    u32 count;
    s32 info;
    u32 changed;
""",
    "B_n": """    s32 cmd;
    s32 n;
    u32 count;
    s32 info;
    s16 op;
    s16 slot;
    u32 changed;
""",
    "A_o": """    s32 cmd;
    s16 op;
    s16 slot;
    u32 count;
    s32 info;
    u32 changed;
""",
    "B_o": """    s32 cmd;
    u32 count;
    s32 info;
    s16 op;
    s16 slot;
    u32 changed;
""",
}
COLOR = {
    "n": """            n = *list++;
            set_chunk_blend(cmd);
            submit_chunk_material_color__FUcPs(cmd, list);
            list += n;
""",
    "o": """            op = *list++;
            set_chunk_blend(cmd);
            submit_chunk_material_color__FUcPs(cmd, list);
            list += op;
""",
}
INFO = {
    "D": """            count = *(u16 *)list;
            info = list[1];
            list += 2;
""",
    "T": """            count = *(u16 *)list;
            t = list[1];
            list += 2;
            info = t;
""",
}
INFO_C = {
    "D": """            count = *(u16 *)list;
            info = list[1];
            list += 2;
""",
    "T": """            count = *(u16 *)list;
            t = list[1];
            list += 2;
            info = t;
""",
}
BIG = {
    "eq": [("op == 0x42", "op == 0x42")],
    "ter": [("(s32)(op == 0x42)", "(s32)(op == 0x42)")],
    "var": [("op == 0x42", "big")],
}
CHUNK_EQ = "info, op == 0x42)"
PRAG = "#pragma push\n#pragma scheduling off\nvoid dispatch_chunk_polygon_list"
LMW = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
BIT = ("if ((u32)(model_render_flags & 0x80000) != 0) {", "if ((u32)(model_render_flags & 0x800) != 0) {")
CHANGE = ("            changed = (cmd ^ chunk_previous_strip_flags) | chunk_strip_dirty_flags;\n",
          "            changed = cmd ^ chunk_previous_strip_flags;\n            changed = changed | chunk_strip_dirty_flags;\n")
ALIAS_OLD = "void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\n"
ALIAS_NEW = ("void draw_chunk_color_tex_strips(s16 *, void *, u32, s32);\n"
             "void submit_chunk_material_color__FUcPs(s32, s16 *);\n")

made = 0
for oa, ca, ia, ba in itertools.product("AB", "no", "DT", "eqter"[:2] + "v"):
    pass
for oa, ca, ia, ba in itertools.product(["A", "B"], ["n", "o"], ["D", "T"], ["eq", "ter", "var"]):
    name = f"{oa}{ca}{ia}{ba}"
    txt = base
    subs = [
        (DECL_CHAMP, ORD[oa + "_" + ca]),
        (COLOR["n"] if False else """            n = *list++;
            set_chunk_blend(cmd);
            submit_chunk_material_color(cmd, list);
            list += n;
""", COLOR[ca]),
        (INFO_C["D"], INFO[ia]),
        BIT, CHANGE, (PRAG, LMW), (ALIAS_OLD, ALIAS_NEW),
    ]
    if ba == "ter":
        subs.append((CHUNK_EQ, "info, (op == 0x42) ? 1 : 0))"))
    elif ba == "var":
        subs.append((CHUNK_EQ, "info, big)"))
        subs.append(("    u32 changed;\n", "    u32 changed;\n" + BIGDECL))
        subs.append(("            switch (op) {\n            case 0x40:",
                     "            big = (op == 0x42);\n            switch (op) {\n            case 0x40:"))
    for old, new in subs:
        assert old in txt, (name, old[:60])
        txt = txt.replace(old, new)
    if ia == "T":
        txt = txt.replace("    u32 changed;\n", "    u32 changed;\n    s16 t;\n")
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    made += 1
print("wrote", made)
