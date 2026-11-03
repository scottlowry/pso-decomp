#!/usr/bin/env python3
"""Z-series -- closing the last 5 rows of EC14.

X05 (volatile guard + use-site cast volatile load) fixed slots 7-9:
  OURS now:  lis r4(msgs@ha) stw r0 stw r31 addi r31 | lwz r3,E11 | lwz r0,CA8 stw r3,CB4 cmpwi
  ORIG:     lwz r3,E11 | lis r4 stw r0 stw r31 addi r31 | lwz r0,CA8 stw r3,CB4 cmpwi
=> ONE move left: the volatile E11F0 load must be emitted ABOVE the msgs
   lis/addi pair. Hypothesis: source-order priority -- put the copy statement
   FIRST (before the msgs init). Crossed with temp/direct, declared-vs-cast
   volatility, and lifetime/dead-assignment pragmas.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()
SIG = 'void TAdTrialModemChkGC__sub_8042EC14(int arg0, int arg1) {\n'
i = base.index(SIG)
j = base.index('    if ((s32) lbl_805D7CA8 == 0) {', i)
HEAD, TAIL = base[:i], base[j:]

VG = ('extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;')
VE = ('extern u32 lbl_805E11F0;', 'extern volatile u32 lbl_805E11F0;')
VB = ('extern u32 lbl_805D7CB4;', 'extern volatile u32 lbl_805D7CB4;')

C = {}


def add(name, stmts, keys=('VG',), pragma=None, decls='    u8 *p;\n    char *msgs;\n'):
    src = HEAD
    body = SIG
    if pragma:
        body += '#pragma push\n#pragma %s off\n' % pragma
    body += decls + '\n' + '\n'.join('    ' + s for s in stmts) + '\n' + TAIL
    if pragma:
        body = body.replace('\n}\n#pragma pop', '\n#pragma pop\n}\n#pragma pop', 1)
    src = src + body
    for k in keys:
        old, new = {'VG': VG, 'VE': VE, 'VB': VB}[k]
        assert old in src, (name, k)
        src = src.replace(old, new, 1)
    C[name] = src


COPY_CAST = 'lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;'
COPY_DECL = 'lbl_805D7CB4 = lbl_805E11F0;'

# Z01: copy FIRST (cast), msgs after  -- the key probe
add('Z01_copyfirst_cast', [COPY_CAST, 'msgs = lbl_80480240;'])
# Z02: copy FIRST declared-volatile, no cast
add('Z02_copyfirst_declvol', [COPY_DECL, 'msgs = lbl_80480240;'], keys=('VG', 'VE'))
# Z03: copy first + msgs as init-decl placed after the statement (mixed)
add('Z03_copyfirst_msgsinit_late',
    [COPY_CAST], keys=('VG',),
    decls='    u8 *p;\n')
# Z04: Z01 + opt_lifetimes off
add('Z04_copyfirst_lifetime', [COPY_CAST, 'msgs = lbl_80480240;'], pragma='opt_lifetimes')
# Z05: Z01 + opt_dead_assignments off
add('Z05_copyfirst_deadassign', [COPY_CAST, 'msgs = lbl_80480240;'], pragma='opt_dead_assignments')
# Z06: Z01 + opt_common_subs off
add('Z06_copyfirst_comsubs', [COPY_CAST, 'msgs = lbl_80480240;'], pragma='opt_common_subs')
# Z07: Z01 + opt_propagation off
add('Z07_copyfirst_propoff', [COPY_CAST, 'msgs = lbl_80480240;'], pragma='opt_propagation')
# Z08: temp read first, store after msgs
add('Z08_tempfirst_storeafter',
    ['s32 v = *(volatile u32 *)&lbl_805E11F0;', 'msgs = lbl_80480240;', 'lbl_805D7CB4 = v;'],
    decls='')
# Z09: copy first + store target volatile too
add('Z09_copyfirst_volboth', [COPY_DECL, 'msgs = lbl_80480240;'], keys=('VG', 'VE', 'VB'))
# Z10: X05 baseline order kept, but msgs materialized via a later first use (decl only)
add('Z10_x05_order_castvol', ['msgs = lbl_80480240;', COPY_CAST])

for n, s in C.items():
    open(os.path.join(HERE, n + '.cpp'), 'w').write(s)
    print('wrote', n)
