#!/usr/bin/env python3
"""W-series: attack the EC14 8-row prologue-order wall.

f8's 22 variants all kept `extern u32 lbl_805E11F0` NON-volatile.  The 6
100%-matched Rosetta fns that DO emit a pre-frame-save integer lwz
(sj_ring_buffer_init, gcrna_initialize, TLobby::init_afs_adxf_state,
TLobby::init_and_add_ref, TBoss6Type1/2) all read the symbol into a TEMP in a
statement separate from the consuming store, and three of them carry a
volatile-qualified declaration.  So: volatile extern + temp + separated store,
crossed with statement order and guard-temp placements.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()

FN = 'void TAdTrialModemChkGC__sub_8042EC14(int arg0, int arg1) {'
i = base.index(FN)
j = base.index('    if ((s32) lbl_805D7CA8 == 0) {', i)
GUARD = base[j:]                      # guard onward (unchanged tail)
PREFIX = base[:i]                     # includes the signature at the end

# the prologue region we replace = text between signature '{' and the guard if
OLD_PROLOGUE = base[base.index('{', i) + 1:j]

DECL_VOL = 'extern volatile u32 lbl_805E11F0;'
DECL_PLAIN = 'extern u32 lbl_805E11F0;'
assert DECL_PLAIN in PREFIX, "plain E11F0 extern not found"

VARIANTS = {
    # name: (volatile_extern?, decls, statements, guard-text-override)
    'W01_vol_temp_first': (True,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n\n',
        'v = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    lbl_805D7CB4 = v;\n', None),
    'W02_vol_temp_after_msgs': (True,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n\n',
        'msgs = lbl_80480240;\n'
        '    v = lbl_805E11F0;\n'
        '    lbl_805D7CB4 = v;\n', None),
    'W03_vol_store_before_msgs': (True,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n\n',
        'v = lbl_805E11F0;\n'
        '    lbl_805D7CB4 = v;\n'
        '    msgs = lbl_80480240;\n', None),
    'W04_vol_gtemp_after': (True,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n    s32 g;\n\n',
        'v = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    g = lbl_805D7CA8;\n'
        '    lbl_805D7CB4 = v;\n',
        '    if (g == 0) {'),
    'W05_vol_gtemp_first': (True,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n    s32 g;\n\n',
        'g = lbl_805D7CA8;\n'
        '    v = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    lbl_805D7CB4 = v;\n',
        '    if (g == 0) {'),
    'W06_vol_direct_copy': (True,
        '    u8 *p;\n    char *msgs;\n\n',
        'lbl_805D7CB4 = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n', None),
    'W07_plain_temp_first': (False,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n\n',
        'v = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    lbl_805D7CB4 = v;\n', None),
    'W08_vol_temp_msgs_init': (True,
        '    u8 *p;\n    s32 v;\n\n    char *msgs = lbl_80480240;\n\n',
        'v = lbl_805E11F0;\n'
        '    lbl_805D7CB4 = v;\n', None),
    'W09_vol_temp_u32type': (True,
        '    u8 *p;\n    char *msgs;\n    u32 v;\n\n',
        'v = lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    lbl_805D7CB4 = v;\n', None),
    'W10_vol_cast_temp_first': (False,
        '    u8 *p;\n    char *msgs;\n    s32 v;\n\n',
        'v = *(volatile s32 *)&lbl_805E11F0;\n'
        '    msgs = lbl_80480240;\n'
        '    lbl_805D7CB4 = v;\n', None),
}

names = []
for name, (isvol, decls, stmts, guard_override) in VARIANTS.items():
    pre = PREFIX
    if isvol:
        pre = pre.replace(DECL_PLAIN, DECL_VOL)
    guard = GUARD
    if guard_override:
        guard = guard_override + GUARD[len('    if ((s32) lbl_805D7CA8 == 0) {'):]
    src = pre + FN + '\n' + decls + stmts + '\n' + guard
    p = os.path.join(HERE, name + '.cpp')
    open(p, 'w').write(src)
    names.append(name)
    print('wrote', name, 'vol=%s' % isvol)

open(os.path.join(HERE, 'wlist.txt'), 'w').write('\n'.join(names) + '\n')
