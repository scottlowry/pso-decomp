#!/usr/bin/env python3
"""Round-8: (A) int-typed 0/1 arg spellings, (B) in-place truncation of the mask chain.
Base = variants7/t2_cubool.cpp (color callee bool, cmd s32 + (s16) casts)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "variants7", "t2_cubool.cpp")).read()
VDIR = os.path.join(HERE, "variants8")
os.makedirs(VDIR, exist_ok=True)

TX_EQ = "draw_chunk_textured_strips(list, (Vtx_803E352C *)buffer, info, op == 0x42);"
MASK_S32 = """                cmd = (s16)(cmd & chunk_polygon_flags_and_mask);
                cmd = (s16)(cmd | chunk_polygon_flags_or_mask);
            }
            cmd = (s16)(cmd >> 8);
"""
MASK_S16C = """                cmd &= chunk_polygon_flags_and_mask;
                cmd |= chunk_polygon_flags_or_mask;
            }
            cmd = (s16)(cmd >> 8);
"""
MASK_S16A = """                cmd &= chunk_polygon_flags_and_mask;
                cmd |= chunk_polygon_flags_or_mask;
            }
            cmd >>= 8;
"""
DECL_S32 = "    s32 cmd;\n"
DECL_S16 = "    s16 cmd;\n"

ARGS = {
    "a0": [(TX_EQ, TX_EQ)],
    "a1": [(TX_EQ, TX_EQ.replace("op == 0x42", "(s32)(op == 0x42)"))],
    "a4": [(TX_EQ, TX_EQ.replace("op == 0x42", "(op == 0x42) + 0"))],
    "a9": [(TX_EQ, TX_EQ.replace("op == 0x42", "0x42 == op"))],
    "a2": [(TX_EQ, TX_EQ.replace("op == 0x42", "big")),
           ("            switch (op) {\n            case 0x40:",
            "            big = (op == 0x42);\n            switch (op) {\n            case 0x40:"),
           ("    u32 changed;\n", "    u32 changed;\n    s32 big;\n")],
    "a3": [(TX_EQ, TX_EQ.replace("op == 0x42", "(op == 0x42) ? 1 : 0"))],
    "a5": [(TX_EQ, TX_EQ.replace("op == 0x42", "!(op != 0x42)"))],
}
MASKS = {"m0": [(MASK_S32, MASK_S32)], "m1": [(MASK_S32, MASK_S16C), (DECL_S32, DECL_S16)],
         "m2": [(MASK_S32, MASK_S16A), (DECL_S32, DECL_S16)]}

for an, asub in ARGS.items():
    for mn, msub in MASKS.items():
        name = an + "_" + mn
        txt = base
        if mn != "m0":
            for old, new in msub:
                assert old in txt, (name, old[:40])
                txt = txt.replace(old, new)
        for old, new in asub:
            assert old in txt, (name, old[:40])
            txt = txt.replace(old, new)
        if name.endswith("a0_m0"):
            name = "ctrl"
            open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
            print("wrote", name)
            continue
        open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
        print("wrote", name)
print(len(os.listdir(VDIR)))
