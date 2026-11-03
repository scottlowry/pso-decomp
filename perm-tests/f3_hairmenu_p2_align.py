#!/usr/bin/env python3
"""f3 p2: word-level structural alignment era-vs-ours.
Fixes objdump psq artifacts (xxsel/lq -> psq_st/psq_l), masks regs, keeps
offsets/immediates, binds reloc names for bl/lis/addi/lfs targets.
Insert/delete hunks = the actual size surplus."""
import re, difflib

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_p2.asm"
BRA = {"b","bl","ba","bla","bc","bcl","bca","bcla","bdnz","bdnz-","beq","bne","blt","bgt","bge","ble","bfp","bls","bgt"}

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
        if hm:
            in_fn = 'render__14TObjCMHairMenuFv' in hm.group(1)
            continue
        if not in_fn: continue
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            if pend is not None: rows[pend][4] = rows[pend][4]  # (flush later)
            rows.append([mm.group(1), int(mm.group(2).replace(" ",""),16), mm.group(3), mm.group(4).strip(), None]); pend = len(rows)-1
        else:
            m3 = re.match(r'\s+([0-9a-f]+):\s+(R_PPC_\S+)\s*(\S*)', line)
            if m3 and pend is not None:
                rows[pend][4] = (m3.group(2), m3.group(3))
    return rows

def fix_artifact(mn, word):
    top = word >> 26
    if mn in ("xxsel","xsmaddadp","xsmsubmsp","xxsel-") and top == 60: return "psq_st"
    if mn == "lq" and top == 56: return "psq_l"
    return mn

def norm(mn, op, word, reloc):
    mn = fix_artifact(mn, word)
    op = op.replace('(', ' ').replace(')', ' ')
    t = []
    for tok in re.split(r'[\s,]+', op):
        if not tok: continue
        if re.fullmatch(r'[rf]\d+', tok): t.append('R')
        elif re.fullmatch(r'0x[0-9A-Fa-f]+|-?\d+', tok): t.append(str(int(tok,0)))
        elif tok == 'qr0': t.append('0')
        elif '@' in tok or tok.startswith('lbl_') or tok.startswith('.L') or re.fullmatch(r'[0-9a-f]{4,}', tok): t.append('S')
        else: t.append(tok)  # cr0, eq, lt
    k = ' '.join(t)
    if reloc:
        rt, sym = reloc
        if rt == 'R_PPC_REL24': k = sym
        elif 'SDA21' in rt: k = f"S21:{sym.split('+')[0]}+{sym.split('+')[1] if '+' in sym else '?'}"
        elif 'ADDR16' in rt: k = f"@{sym}"
        elif 'REL' in rt: k = "S"
    return f"{mn} {k}"

era = era_rows(); ours = ours_rows()
ek = [norm(m, o, w, None) for _, w, m, o in era]
ok = [norm(r[2], r[3], r[1], r[4]) for r in ours]
print(f"era={len(era)} ours={len(ours)} surplus={len(ours)-len(era):+d}")
sm = difflib.SequenceMatcher(None, ek, ok, autojunk=False)
tot = 0
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag == 'equal': continue
    n = (j2-j1)-(i2-i1); tot += n
    print(f"\n== {tag} era[{i1}:{i2}] ours[{j1}:{j2}] net {n:+d}")
    for s in range(i1,i2): print(f"  O-{s:3d} {era[s][0]}: {era[s][2]:8s} {era[s][3]}")
    for s in range(j1,j2): print(f"  N-{s:3d} {ours[s][0]}: {ours[s][2]:8s} {ours[s][3]}   r={ours[s][4]}")
print(f"\nTOTAL NET {tot:+d}")
