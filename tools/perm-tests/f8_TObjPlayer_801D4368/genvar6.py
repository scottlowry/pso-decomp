import os
D = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjPlayer_801D4368"
base = open(f"{D}/base.c").read()
CH = ["obj","cnt_2","cnt","rec","down_4","owner","rec_2","rec_3","down_3","down_2","down","cnt_3"]
DEC = {"obj":"u8 *obj;","down":"void *down;","cnt":"s32 cnt;","rec":"u32 *rec;","down_4":"void *down_4;",
       "cnt_2":"s32 cnt_2;","owner":"s32 owner;","rec_2":"u32 *rec_2;","down_3":"void *down_3;",
       "down_2":"void *down_2;","cnt_3":"s32 cnt_3;","rec_3":"u32 *rec_3;"}
declblock = "\n".join("    "+DEC[n] for n in CH)
assert declblock in base, "decl block mismatch"
def redecl(names):
    assert len(names)==12 and all(n in DEC for n in names)
    return "\n".join("    "+DEC[n] for n in names)
def withmoved(var, pos):
    names = [n for n in CH if n != var]
    names.insert(pos, var)
    return names
V = {}
for pos in [1,3,4,5,6,7,8,9,10,11]:
    V["A_cnt_p"+str(pos+1)] = base.replace(declblock, redecl(withmoved("cnt", pos)))
# A20: p1 def swap on new champ (down load before cnt=0)
a1 = """    cnt = 0;
    down = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);"""
b1 = """    down = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);
    cnt = 0;"""
assert a1 in base
V["A20_p1defswap"] = base.replace(a1, b1)
# A21: cnt=0 hoisted to first statement
V["A21_cnthoist"] = base.replace(a1, b1).replace("    cnt = 0;\n", "", 1)
# re-add cnt=0 as first stmt after decls
V["A21_cnthoist"] = V["A21_cnthoist"].replace(declblock + "\n", declblock + "\n    cnt = 0;\n", 1)
# A22: cnt_3 moved to pos 2 (mirror of r3 winner trick on the other counter)
V["A22_cnt3_p2"] = base.replace(declblock, redecl(withmoved("cnt_3", 2)))
# A23: both counters up: cnt_2@2 cnt@3 (champ) with owner first? owner@2:
V["A23_owner_p2"] = base.replace(declblock, redecl(withmoved("owner", 2)))
for name, src in V.items():
    assert "cnt = 0;" in src or name == "A21_broken"
    open(f"{D}/variants/{name}.c","w").write(src)
print("wrote", len(V))
