#!/usr/bin/env python3
"""f3 p7 row-map (official objdiff slot space). Classes:
 (a) pure-color permutation  (b) @NNN pool/display-only (+hybrid sub-count)
 (c) real value/order diff   (d) link-resident @ha/@l
Priority: d > b > a > c. Census = per-slot reg-pair diff map (pair-swap vs ring)."""
import re
from collections import Counter

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_p2.asm"
SCORE = f"{REPO}/perm-tests/f3_hairmenu_p7_score_base.txt"

def era_rows():
    rows, in_fn = [], False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'): in_fn = True; continue
        if in_fn and line.startswith('.endfn'): break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s+(\S+)\s*(.*)', line)
        if mm: rows.append((mm.group(1), int(mm.group(2).replace(" ",""),16), mm.group(3), mm.group(4).strip()))
    return rows

def ours_rows():
    rows, in_fn, pend = [], False, None
    for line in open(OURS_ASM):
        hm = re.match(r'^[0-9a-f]+ <(.*)>:', line)
        if hm: in_fn = 'render__14TObjCMHairMenuFv' in hm.group(1); continue
        if not in_fn: continue
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            rows.append([mm.group(1), int(mm.group(2).replace(" ",""),16), mm.group(3), mm.group(4).strip(), None]); pend=len(rows)-1
        else:
            m3 = re.match(r'\s+([0-9a-f]+):\s+(R_PPC_\S+)\s*(\S*)', line)
            if m3 and pend is not None: rows[pend][4] = (m3.group(2), m3.group(3))
    return rows

def fix_artifact(mn, word):
    top = word >> 26
    if mn in ("xxsel","xsmaddadp","xsmsubmsp","xxsel-") and top == 60: return "psq_st"
    if mn == "lq" and top == 56: return "psq_l"
    return mn

MASK = 0x03E00000 | 0x001F0000 | 0x0000F800
def mask_regs(w): return w & ~MASK

era = era_rows(); ours = ours_rows()
assert len(era) == len(ours) == 460

rows = []
for line in open(SCORE):
    mm = re.match(r'\s+slot\s*(\d+) O: (.*?)\s+N: (.*?)\s*$', line)
    if mm: rows.append((int(mm.group(1)), mm.group(2), mm.group(3)))
print(f"one_shot parsed slot rows: {len(rows)}")

cls = {"a":[], "b":[], "c":[], "d":[]}
cen_full = Counter()   # all reg-pair diffs across same-mnemonic rows (incl hybrids)
b_hybrid = 0
for slot, o, n in rows:
    e = era[slot]; u = ours[slot]
    ew, uw = e[1], u[1]
    emn, omn = fix_artifact(e[2], ew), fix_artifact(u[2], uw)
    reloc = u[4]
    ha = bool(re.search(r'@(ha|l)\b', e[3])) or bool(re.search(r'@(ha|l)\b', u[3])) or \
         (reloc and reloc[0] in ("R_PPC_ADDR16_HA","R_PPC_ADDR16_LO"))
    pool = bool(reloc and "SDA21" in reloc[0] and reloc[1].startswith("@"))
    eregs = re.findall(r'\b([rf]\d+)\b', e[3]); uregs = re.findall(r'\b([rf]\d+)\b', u[3])
    same_len = emn == omn and len(eregs) == len(uregs) and eregs and uregs
    if same_len:
        for a_,b_ in zip(eregs,uregs):
            if a_ != b_: cen_full[(a_,b_)] += 1
    regdiff = same_len and eregs != uregs
    imm_same_nomask = emn == omn and mask_regs(ew) == mask_regs(uw)
    if ha:
        c, why = "d", ("@ha/@l" + ("+color" if regdiff else ""))
    elif ew == uw:
        c, why = "b", "word-identical(display-artifact)"
    elif pool and emn == omn and not regdiff:
        c, why = "b", f"pool-name-only({reloc[1]})"
    elif pool and emn == omn and regdiff and eregs and len(eregs)==len(uregs):
        c, why = "b", f"pool+color-hybrid({reloc[1]})"; b_hybrid += 1
    elif imm_same_nomask and regdiff:
        c, why = "a", "reg-color-only"
    else:
        c, why = "c", "value/order/mnemonic diff"
    cls[c].append((why, slot, f"O-{slot:3d} {e[2]:8s} {e[3]}", f"N-{slot:3d} {u[2]:8s} {u[3]}  r={reloc}"))

print("CLASS COUNTS (official 460-slot space):")
for c in "abcd":
    sub = Counter(w.split('(')[0].split('+')[0] for w,_,_,_ in cls[c])
    print(f"  ({c}) = {len(cls[c]):3d}   {dict(sub)}")
print(f"  TOTAL = {sum(len(v) for v in cls.values())}   (pool+color hybrids inside b: {b_hybrid})")

gpr_c, fpr_c = Counter(), Counter()
for k,v in cen_full.items():
    if k[0][0]=='r': gpr_c[k]+=v
    else: fpr_c[k]+=v
print("\n--- COLOR PAIR CENSUS (eraReg->oursReg, all same-mnemonic rows incl hybrids) ---")
print("GPR:"); [print(f"  {v:3d}x {k[0]}->{k[1]}") for k,v in gpr_c.most_common(15)]
print("FPR:"); [print(f"  {v:3d}x {k[0]}->{k[1]}") for k,v in fpr_c.most_common(25)]

with open(f"{REPO}/perm-tests/f3_hairmenu_p7_rows.txt","w") as f:
    f.write("f3 p7 ROW MAP @ champ 4cf63208 (460w gate-exact, one_shot 84.097824)\n")
    f.write(f"one_shot diff rows={len(rows)}: classA={len(cls['a'])} classB={len(cls['b'])} classC={len(cls['c'])} classD={len(cls['d'])}\n")
    f.write(f"(b sub: pool+color hybrids={b_hybrid}; word-identical artifacts={sum(1 for w,_,_,_ in cls['b'] if w.startswith('word'))})\n")
    f.write("aligner LCS(reg-masked) skeleton=328 printed rows: pool-display~84 value/order~107 @ha/@l~24 (color INVISIBLE under reg-masking)\n")
    f.write("\n--- COLOR PAIR CENSUS GPR ---\n")
    for k,v in gpr_c.most_common(): f.write(f"  {v:3d}x {k[0]}->{k[1]}\n")
    f.write("--- COLOR PAIR CENSUS FPR ---\n")
    for k,v in fpr_c.most_common(): f.write(f"  {v:3d}x {k[0]}->{k[1]}\n")
    for c in "abcd":
        f.write(f"\n######## CLASS ({c}) n={len(cls[c])} ########\n")
        for why, slot, eo, no in cls[c]:
            f.write(f"[{why}] {eo}\n          {no}\n")
print("\nwrote perm-tests/f3_hairmenu_p7_rows.txt")
print("\n--- (c) REAL VALUE-DIFF ROWS ---")
for w,s,eo,no in cls["c"]:
    print(f"[{w}] {eo}\n{'':11}{no}")
