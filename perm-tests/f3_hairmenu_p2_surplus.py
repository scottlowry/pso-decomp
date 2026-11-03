#!/usr/bin/env python3
"""f3 p2: locate the +5w surplus. difflib on masked keys (mnemonic + operands
with register numbers stripped) between era .s rows and ours objdump rows.
Prints every insert/delete hunk with slot indices and raw text."""
import re

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_p2.asm"

def era_rows():
    rows, in_fn = [], False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'):
            break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s+(\S+)(.*)', line)
        if mm:
            rows.append((mm.group(1), mm.group(3), mm.group(4).strip()))
    return rows

def ours_rows():
    rows, in_fn = [], False
    for line in open(OURS_ASM):
        if re.match(r'^[0-9a-f]+ <', line):
            if 'render__14TObjCMHairMenuFv' in line: in_fn = True
            elif in_fn: break
            continue
        if not in_fn: continue
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            txt = mm.group(4).strip()
            txt = re.sub(r'\s*<render__14TObjCMHairMenuFv\+(0x[0-9a-f]+|\d+)>', '', txt)  # local branch targets
            txt = re.sub(r'\s*<\S+>', '', txt)  # named targets -> reloc carries name
            rows.append((mm.group(1), mm.group(3), txt))
    return rows

def mask(mn, op):
    k = op
    k = re.sub(r'\br\d+\b', 'R', k)
    k = re.sub(r'\bf\d+\b', 'F', k)
    k = re.sub(r'0x[0-9A-Fa-f]+', 'N', k)
    k = re.sub(r'\b[0-9A-Fa-f]+\b', 'N', k)
    return f"{mn} {k}"

era = era_rows(); ours = ours_rows()
ek = [mask(m, o) for _, m, o in era]
ok = [mask(m, o) for _, m, o in ours]
print(f"era rows={len(era)} ours rows={len(ours)} surplus={len(ours)-len(era)}")
sm = re  # placeholder
import difflib
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ek, ok, autojunk=False).get_opcodes():
    if tag == 'equal': continue
    print(f"\n== {tag} era[{i1}:{i2}] ours[{j1}:{j2}]  net {j2-j1-(i2-i1):+d}")
    for s in range(i1, i2):
        a, m, o = era[s]; print(f"  O-{s:3d} {a}: {m:8s} {o}")
    for s in range(j1, j2):
        a, m, o = ours[s]; print(f"  N-{s:3d} {a}: {m:8s} {o}")
