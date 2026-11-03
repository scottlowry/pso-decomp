#!/usr/bin/env python3
"""Grid: decl-order perms x rel-assign spellings on the v07 (store-swap) base.
Triages per candidate: word size, addi-home of (arg1+11), and full REGDIFF set
vs target.o (same row model as score.py)."""
import itertools, os, re, subprocess, sys

KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/f3_TObjFish_802E7D70"
R = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
OBJD = "/opt/homebrew/bin/powerpc-eabi-objdump"

PRELUDE = open(KIT + "/v00_base.cpp").read().split("extern \"C\" {\nu8 *TBoss7Crawfish__ct")[0]
_pre = open(KIT + "/v00_base.cpp").read()
_si = _pre.index("extern \"C\" {\nu8 *TBoss7Crawfish__ct")
_se = _pre.index("void TObjFish__sub_802E7D70", _si)
STACK_EXT = _pre[_si:_se]
POST = open(KIT + "/v00_base.cpp").read().split("#undef lbl_805DEA10",1)[1]
POST = "\n\n#undef lbl_805DEA10" + POST
PROTO = 'extern "C" {\nvoid TObjFish__sub_802E7D70(void *self, s16 arg1, void *arg2, void *arg3, s32 arg4);\n}\n\n'

FN_TMPL = """void TObjFish__sub_802E7D70(void *self, s16 arg1, void *arg2, void *arg3, s32 arg4) {{
    Stack_802E7D70 block;
{decls}
    if (((Boss_802E7CC4 *)self)->group == NULL) {{
        return;
    }}
    if (arg1 <= 0) {{
        return;
    }}
{relassign}    target = (u16)(get_entity_id(self) + rel);
    for (child = ((Boss_802E7CC4 *)self)->group->m_down; child != NULL; child = child->m_next) {{
        if (get_entity_id(child) == target) {{
            return;
        }}
    }}
    f2c = *(s16 *)((u8 *)self + 0x2c);
    block.sp8 = (u16)(f2c + rel);
    block.spA = 1;
    block.spC = 0;
    block.spE = target;
    block.sp10 = (u16)*(s16 *)((u8 *)self + 0x28);
    block.sp12 = 0;
    block.sp14 = 0;
    block.sp16 = 0;
    ((void (*)(void *, void *))VecCopy__FP3VecPC3Vec)(&block.sp18, arg2);
    copy_xyz(&block.sp24, arg3);
    if (arg4 & 1) {{
        block.sp30 = lbl_805DEA10;
    }} else {{
        block.sp30 = lbl_805DEA18;
    }}
    block.sp34 = lbl_805DEA10;
    block.sp38 = lbl_805DEA10;
    block.sp3C = lbl_805DEA10;
    block.sp40 = lbl_805DEA10;
    block.sp44 = 0;
    block.sp46 = 0;
    spawned = __nw__7TObjectFUl(0x3d0);
    if (spawned != 0U) {{
        TBoss7Crawfish__ct((u8 *)spawned, (u8 *)((Boss_802E7CC4 *)self)->group, (u8 *)&block);
    }}
}}
"""

DECLS = ["s16 rel;", "s16 f2c;", "u16 target;", "TObject *child;", "u32 spawned;"]
SPELL = {
    's1': "    rel = (s16)(arg1 + 11);\n",
    's2': "    rel = arg1 + 11;\n",
    's3': "    rel = (s16)(11 + arg1);\n",
    's4': "    rel = (s16)((s32)arg1 + (s32)11);\n",
}

def rows(o):
    txt = subprocess.run([OBJD, "-d", o], capture_output=True, text=True).stdout
    out = []; started = False
    for l in txt.splitlines():
        if "<TObjFish__sub_802E7D70>" in l and "00000000" in l:
            started = True; continue
        if started:
            if re.match(r'^[0-9a-f]+ <', l): break
            m = re.match(r'\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(.*)', l)
            if m: out.append((m.group(1).replace(' ', '').strip(), m.group(2).strip()))
    return out

T = rows(KIT + "/target.o")
EXT = lambda txt: ('@sda21' in txt) or txt.startswith('bl ') or txt.startswith('b ')

best = []
for sn, asg in SPELL.items():
    for perm in itertools.permutations(range(5)):
        decls = "\n".join(f"    {DECLS[i]}" for i in perm)
        # s2 (no cast) needs rel decl; keep same decls
        fn = FN_TMPL.format(decls=decls, relassign=asg)
        # drop decl of f2c if never... all used; ok
        src = PRELUDE + PROTO + STACK_EXT + fn + POST
        name = f"g_{sn}_{''.join(map(str, perm))}"
        cpp = f"{KIT}/probe.cpp"
        open(cpp, "w").write(src)
        rc = subprocess.run(["bash", f"{KIT}/compile.sh", cpp, f"{KIT}/probe.o"], capture_output=True, cwd=R).returncode
        if rc != 0:
            print(name, "COMPILEFAIL"); continue
        C = rows(f"{KIT}/probe.o")
        if len(C) != 76:
            print(name, f"SIZE {len(C)}"); continue
        diff = [i for i in range(76) if T[i][0] != C[i][0] and not EXT(T[i][1]) and not EXT(C[i][1])]
        addihome = next((c[1] for c in C if re.match(r'addi\s+r(\d+),\s*r28, 11$', c[1])), "?")
        if len(diff) < 7:
            print("BEAT:", name, diff, addihome); best.append((name, diff))
        else:
            print(name, len(diff), addihome)
print("BEST:", best)
