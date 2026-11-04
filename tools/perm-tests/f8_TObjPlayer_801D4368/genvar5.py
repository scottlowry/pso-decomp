import os
D = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjPlayer_801D4368"
base = open(f"{D}/base.c").read()
CH = ["obj","down","cnt","rec","down_4","cnt_2","owner","rec_2","rec_3","down_3","down_2","cnt_3"]
DEC = {"obj":"u8 *obj;","down":"void *down;","cnt":"s32 cnt;","rec":"u32 *rec;","down_4":"void *down_4;",
       "cnt_2":"s32 cnt_2;","owner":"s32 owner;","rec_2":"u32 *rec_2;","down_3":"void *down_3;",
       "down_2":"void *down_2;","cnt_3":"s32 cnt_3;","rec_3":"u32 *rec_3;"}
declblock = "\n".join("    "+DEC[n] for n in CH)
assert declblock in base
def redecl(names):
    assert len(names)==12 and all(n in DEC for n in names)
    return "\n".join("    "+DEC[n] for n in names)
def withmoved(var, pos):
    names = [n for n in CH if n != var]
    names.insert(pos, var)
    return names
out = {}
# Y11: comma-def at p1 down (tie lever; verify no extra mr offline)
a = "    down = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);\n    while (down != 0)"
assert a in base
out["Y11_comma_p1"] = base.replace(a, "    down = (0, *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14));\n    while (down != 0)")
# Y12: comma-def on cnt init instead
out["Y12_comma_cnt"] = base.replace("    cnt = 0;\n", "    cnt = (0, 0);\n", 1)
# W1b: merge walker p1-p3 on CURRENT champ; W10b merge p1-p2; W11b merge p2-p3
v = base.replace("    void *down_3;\n","").replace("    void *down_2;\n","")
out["W1b_walker3"] = v.replace("down_3","down").replace("down_2","down")
v = base.replace("    void *down_2;\n","").replace("down_2","down")
out["W10b_merge12"] = v
v = base.replace("    void *down_3;\n","").replace("down_3","down_2")
out["W11b_merge23"] = v
# Y13: p4 def swap (down_4 before rec_3)
c = """    rec_3 = (u32 *)*(s32 *)(obj + 4);
    down_4 = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);"""
d = """    down_4 = *(void **)((s8 *)*(s32 *)((s8 *)arg0 + 0x1c4) + 0x14);
    rec_3 = (u32 *)*(s32 *)(obj + 4);"""
assert c in base
out["Y13_p4defswap"] = base.replace(c, d)
# Y14: p1+rec_3 down-at-9 decl + comma p1
out["Y14_d10comma"] = out["Y11_comma_p1"].replace(declblock, redecl(withmoved("down", 10)))
# Y15: down after owner (pos 7)
out["Y15_down_p8"] = base.replace(declblock, redecl(withmoved("down", 7)))
for name, src in out.items():
    open(f"{D}/variants/{name}.c","w").write(src)
print("wrote", len(out))
