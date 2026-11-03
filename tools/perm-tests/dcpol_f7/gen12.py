#!/usr/bin/env python3
"""Round-12: peephole-on region on the sibling-safe t2 base (bool->int clamp is a
peephole artifact: with peephole the era emitted srwi r6 directly)."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "variants7", "t2_cubool.cpp")).read()
VDIR = os.path.join(HERE, "variants12")
os.makedirs(VDIR, exist_ok=True)
P = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
PE = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\n#pragma peephole on\nvoid dispatch_chunk_polygon_list"
POP = "            list += count - 1;\n        }\n    }\n}\n#pragma pop"
POP2 = "            list += count - 1;\n        }\n    }\n}\n#pragma pop"


def w(name, txt):
    open(os.path.join(VDIR, name + ".cpp"), "w").write(txt)
    print("wrote", name)


w("p00_ctl", base)
w("p01_peep", base.replace(P, PE))
# also: keep era's callee (draw_chunk_textured_strips) untouched, but make OUR caller
# avoid the clamp by passing the value through a u32 that peephole proves 0/1? -> just peep.
# x-flag: bool param for BOTH callees + peephole (tests whether callee drift disappears under peep)
t1 = open(os.path.join(HERE, "variants7", "t1_bothbool.cpp")).read()
P1 = "#pragma push\n#pragma scheduling off\n#pragma use_lmw_stmw off\nvoid dispatch_chunk_polygon_list"
w("p02_t1_peep", t1.replace(P1, PE))
