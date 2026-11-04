import os
D = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjPlayer_801D4368"
base = open(f"{D}/base.c").read()
CH = ["obj","down","cnt","rec","down_4","cnt_2","owner","rec_2","rec_3","down_3","down_2","cnt_3"]
DEC = {"obj":"u8 *obj;","down":"void *down;","cnt":"s32 cnt;","rec":"u32 *rec;","down_4":"void *down_4;",
       "cnt_2":"s32 cnt_2;","owner":"s32 owner;","rec_2":"u32 *rec_2;","down_3":"void *down_3;",
       "down_2":"void *down_2;","cnt_3":"s32 cnt_3;","rec_3":"u32 *rec_3;"}
declblock = "\n".join("    "+DEC[n] for n in CH)
assert declblock in base, "decl block mismatch vs current base.c"
def redecl(names):
    assert len(names)==12 and all(n in DEC for n in names)
    return "\n".join("    "+DEC[n] for n in names)
def withmoved(var, pos):
    names = [n for n in CH if n != var]
    names.insert(pos, var)
    return names
ORD = {}
for pos in [3,8,9,10,11]:
    ORD["Y1_down_p"+str(pos+1)] = withmoved("down", pos)
ORD["Y7_cntfirst"] = withmoved("cnt", 1)
ORD["Y8_d2d3swap"] = withmoved("down_3", 10)  # yields ..., rec_3, down_2, down_3, cnt_3
ORD["Y10_cnt2first"] = withmoved("cnt_2", 4)
for name, order in ORD.items():
    out = base.replace(declblock, redecl(order))
    assert out != base
    open(f"{D}/variants/{name}.c","w").write(out)
# def-swap variants (statement order in preheaders; semantically = load/comma moves, safe: independent defs)
a1 = """    cnt = 0;
    down = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);"""
b1 = """    down = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);
    cnt = 0;"""
assert a1 in base
out = base.replace(a1, b1)
open(f"{D}/variants/Z1_p1defswap.c","w").write(out)
out2 = redecl(withmoved("down", 11))
body2 = base.replace(declblock, out2)
open(f"{D}/variants/Z2_p1swap_downlast.c","w").write(body2.replace(a1,b1))
print("wrote", len(ORD)+2, "variants for current champ")
