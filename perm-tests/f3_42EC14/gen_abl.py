#!/usr/bin/env python3
"""Ablation of the P02 winner: which of the three edits are necessary?
  (1) guard extern  s32 -> volatile s32
  (2) E11F0 extern  u32 -> const s32
  (3) fused copy -> s32 temp + store
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()
COPY_OLD = '    lbl_805D7CB4 = lbl_805E11F0;\n'
COPY_NEW = '    s32 v = lbl_805E11F0;\n    lbl_805D7CB4 = v;\n'
G_OLD, G_NEW = 'extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;'
E_OLD, E_NEW = 'extern u32 lbl_805E11F0;', 'extern const s32 lbl_805E11F0;'
assert COPY_OLD in base and G_OLD in base and E_OLD in base

COMBOS = {
    'A00_champ':      (False, False, False),
    'A01_guard_only': (True, False, False),
    'A02_const_only': (False, True, False),
    'A03_temp_only':  (False, False, True),
    'A04_guard_temp': (True, False, True),
    'A05_const_temp': (False, True, True),
    'A06_guard_const': (True, True, False),
    'A07_all3':       (True, True, True),
}
for name, (g, e, t) in COMBOS.items():
    s = base
    if g:
        s = s.replace(G_OLD, G_NEW)
    if e:
        s = s.replace(E_OLD, E_NEW)
    if t:
        s = s.replace(COPY_OLD, COPY_NEW)
    open(os.path.join(HERE, name + '.cpp'), 'w').write(s)
    print('wrote', name, (g, e, t))
