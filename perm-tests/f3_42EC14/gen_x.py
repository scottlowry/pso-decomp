#!/usr/bin/env python3
"""X-series: store-side / guard-side volatile pinning (W-series showed the
volatile LOAD does not hoist -- it re-homes the pair to r4 and stays at slot 7).
Each variant applies a list of (old,new) text substitutions."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()
FN = 'void TAdTrialModemChkGC__sub_8042EC14(int arg0, int arg1) {'
i = base.index(FN)
j = base.index('    if ((s32) lbl_805D7CA8 == 0) {', i)

CH = '    char *msgs = lbl_80480240;\n    lbl_805D7CB4 = lbl_805E11F0;\n'
assert CH in base[i:j], base[i:j][:900]

VARIANTS = {
    'X01_vol_store_cb4':  [('extern u32 lbl_805D7CB4;', 'extern volatile u32 lbl_805D7CB4;')],
    'X02_vol_both':       [('extern u32 lbl_805D7CB4;', 'extern volatile u32 lbl_805D7CB4;'),
                           ('extern u32 lbl_805E11F0;', 'extern volatile u32 lbl_805E11F0;')],
    'X03_vol_guard':      [('extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;')],
    'X04_vol_msgs':       [('extern char lbl_80480240[];', 'extern volatile char lbl_80480240[];')],
    'X05_vol_guard_cast': [('extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;'),
                           (CH, '    char *msgs = lbl_80480240;\n'
                               '    lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;\n')],
    # guard read as a separate top statement (its load must then precede the copy's)
    'X06_guard_read_top': [(CH, '    s32 g = lbl_805D7CA8;\n'
                                '    char *msgs = lbl_80480240;\n'
                                '    lbl_805D7CB4 = lbl_805E11F0;\n'),
                           ('    if ((s32) lbl_805D7CA8 == 0) {', '    if (g == 0) {')],
    # Rosetta shape verbatim: dead volatile read FIRST, then msgs init, then plain copy
    'X07_dead_read_top':  [(CH, '    *(volatile u32 *)&lbl_805E11F0;\n'
                                '    char *msgs = lbl_80480240;\n'
                                '    lbl_805D7CB4 = lbl_805E11F0;\n')],
    # dead read via declared-volatile extern (no cast)
    'X08_dead_read_decl': [('extern u32 lbl_805E11F0;', 'extern volatile u32 lbl_805E11F0;'),
                           (CH, '    lbl_805E11F0;\n'
                               '    char *msgs = lbl_80480240;\n'
                               '    lbl_805D7CB4 = lbl_805E11F0;\n')],
    # copy moved AFTER the guard body opens? no -- keep unconditional, but move it last
    'X09_copy_last_before_guard': [(CH, '    char *msgs = lbl_80480240;\n'
                                        '    (void)0;\n'
                                        '    lbl_805D7CB4 = lbl_805E11F0;\n')],
}

for name, subs in VARIANTS.items():
    src = base
    for old, new in subs:
        assert old in src, (name, old[:60])
        src = src.replace(old, new, 1)
    open(os.path.join(HERE, name + '.cpp'), 'w').write(src)
    print('wrote', name)
