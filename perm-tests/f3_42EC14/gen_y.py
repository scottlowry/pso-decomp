#!/usr/bin/env python3
"""Y-series (clean rewrite).

X05 result: volatile guard + cast volatile load moved slots 7-9 into place; 5
rows remain at slots 2-6. ORIG wants the E11F0 load at slot 2 (above the frame
saves) with its store still at slot 8 -> the read must be pinned while the store
stays free. Levers: s32 temp for the read, s32 temp for the guard, and
`#pragma opt_propagation off` to stop MWCC fusing the read into the store.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()

SIG = 'void TAdTrialModemChkGC__sub_8042EC14(int arg0, int arg1) {\n'
i = base.index(SIG)
j = base.index('    if ((s32) lbl_805D7CA8 == 0) {', i)
HEAD, TAIL = base[:i], base[j + len('    if ((s32) lbl_805D7CA8 == 0) {'):]

# global extern block edits
EDITS = {
    'vol_guard': ('extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;'),
    'vol_e11': ('extern u32 lbl_805E11F0;', 'extern volatile u32 lbl_805E11F0;'),
    'vol_cb4': ('extern u32 lbl_805D7CB4;', 'extern volatile u32 lbl_805D7CB4;'),
}

V = {}


def add(name, decls, stmts, guard_cond='(s32) lbl_805D7CA8 == 0', pragma=None, keys=()):
    body = SIG
    if pragma:
        body += '#pragma push\n#pragma %s off\n' % pragma
    if decls:
        body += decls + '\n'
    body += '\n'.join('    ' + s for s in stmts) + '\n'
    body += '    if (%s) {\n' % guard_cond + TAIL
    if pragma:
        # close the pragma pop before the function's own #pragma pop
        body = body.replace('\n}\n#pragma pop', '\n#pragma pop\n}\n#pragma pop', 1)
    src = HEAD + body
    for k in keys:
        old, new = EDITS[k]
        assert old in src, (name, k)
        src = src.replace(old, new, 1)
    V[name] = src


D = '    u8 *p;\n    char *msgs;\n    s32 v;\n    s32 g;'

add('Y01_propoff_vtemp_gtemp', D,
    ['v = *(volatile u32 *)&lbl_805E11F0;', 'msgs = lbl_80480240;',
     'g = lbl_805D7CA8;', 'lbl_805D7CB4 = v;'], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard',))
add('Y02_propoff_ptemp_gtemp', D,
    ['v = lbl_805E11F0;', 'msgs = lbl_80480240;', 'g = lbl_805D7CA8;',
     'lbl_805D7CB4 = v;'], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard',))
add('Y03_propoff_vtemp_direct', D,
    ['v = *(volatile u32 *)&lbl_805E11F0;', 'msgs = lbl_80480240;',
     'g = lbl_805D7CA8;', 'lbl_805D7CB4 = v;', ''], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard',))
add('Y04_noprop_vtemp_gtemp', D,
    ['v = *(volatile u32 *)&lbl_805E11F0;', 'msgs = lbl_80480240;',
     'g = lbl_805D7CA8;', 'lbl_805D7CB4 = v;'], guard_cond='g == 0',
    keys=('vol_guard',))
add('Y05_propoff_msgs_late', D,
    ['v = *(volatile u32 *)&lbl_805E11F0;', 'g = lbl_805D7CA8;',
     'lbl_805D7CB4 = v;', 'msgs = lbl_80480240;'], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard',))
add('Y06_propoff_declvol_nocast', D,
    ['v = lbl_805E11F0;', 'msgs = lbl_80480240;', 'g = lbl_805D7CA8;',
     'lbl_805D7CB4 = v;'], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard', 'vol_e11'))
add('Y07_propoff_declvol_all', D,
    ['v = lbl_805E11F0;', 'msgs = lbl_80480240;', 'g = lbl_805D7CA8;',
     'lbl_805D7CB4 = v;'], guard_cond='g == 0',
    pragma='opt_propagation', keys=('vol_guard', 'vol_e11', 'vol_cb4'))
add('Y08_x05_plus_gtemp', '    u8 *p;\n    char *msgs;\n    s32 g;',
    ['msgs = lbl_80480240;', 'lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;',
     'g = lbl_805D7CA8;'], guard_cond='g == 0', keys=('vol_guard',))

for n, s in V.items():
    open(os.path.join(HERE, n + '.cpp'), 'w').write(s)
    print('wrote', n)
