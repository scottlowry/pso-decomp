#!/usr/bin/env python3
"""P-series -- the last 5 rows of EC14 (slots 2-6).

Champion so far: X05 = volatile-qualified guard extern + use-site cast load:
  OURS:  lis(msgs@ha) stw r0 stw r31 addi r31 | lwz r3,E11 | lwz r0,CA8 stw r3,CB4 cmpwi
  ORIG: lwz r3,E11 | lis(msgs@ha) stw r0 stw r31 addi r31 | lwz r0,CA8 stw r3,CB4 cmpwi
ONE instruction must rise to slot 2 (above the frame saves).

Declaration-form mining from the 6 integer-load Rosetta precedents that ARE
100%-matched (f8's corpus screen missed these because it only looked for the
shape among matched fns, never read their decls):
  init_and_add_ref__6TLobbyFv  : `extern const s32 lbl_805E0D30;`  + `s32 v = <sym>;`
  sj_ring_buffer_init          : `__declspec(section ".sdata2") extern const char* const volatile`
  gcrna_initialize             : `extern "C" const char *const volatile` + bare read
  init_afs_adxf_state          : `extern const char *const volatile` + bare read
So CONST-qualified and .sdata2-declspec externs are the untried classes here.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, 'base.cpp')).read()
SIG = 'void TAdTrialModemChkGC__sub_8042EC14(int arg0, int arg1) {\n'
i = base.index(SIG)
j = base.index('    if ((s32) lbl_805D7CA8 == 0) {', i)
HEAD, TAIL = base[:i], base[j:]
CH = '    char *msgs = lbl_80480240;\n    lbl_805D7CB4 = lbl_805E11F0;\n'
assert CH in base[i:j]

VOL_GUARD = ('extern s32 lbl_805D7CA8;', 'extern volatile s32 lbl_805D7CA8;')
P = {}


def add(name, body_subs, e11_decl=None, guard_volatile=True, pragma=None):
    src = HEAD
    if guard_volatile:
        old, new = VOL_GUARD
        src = src.replace(old, new, 1)
    if e11_decl:
        src = src.replace('extern u32 lbl_805E11F0;', e11_decl, 1)
    body = base[i:j]
    for old, new in body_subs:
        assert old in body, (name, old[:60])
        body = body.replace(old, new, 1)
    if pragma:
        body = body.replace(SIG, SIG + '#pragma push\n#pragma %s off\n' % pragma, 1)
        body = body + ''
    src = src + body + TAIL
    if pragma:
        src = src.replace('\n}\n#pragma pop', '\n#pragma pop\n}\n#pragma pop', 1)
    P[name] = src


CAST = '    char *msgs = lbl_80480240;\n    lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;\n'

# P01: X05 verbatim (re-anchor the champion in this generator)
add('P01_x05_reanchor', [(CH, CAST)])
# P02: const-qualified extern (init_and_add_ref form), plain read
add('P02_const_extern', [(CH, '    char *msgs = lbl_80480240;\n    s32 v = lbl_805E11F0;\n    lbl_805D7CB4 = v;\n')],
    e11_decl='extern const s32 lbl_805E11F0;', pragma=None)
# P03: const + volatile extern (sj/gcrna/afs form), plain read into temp
add('P03_constvol_decl', [(CH, '    char *msgs = lbl_80480240;\n    s32 v = lbl_805E11F0;\n    lbl_805D7CB4 = v;\n')],
    e11_decl='extern const volatile u32 lbl_805E11F0;')
# P04: .sdata2 declspec + const volatile (sj verbatim form)
add('P04_sdata2_declspec', [(CH, '    char *msgs = lbl_80480240;\n    s32 v = lbl_805E11F0;\n    lbl_805D7CB4 = v;\n')],
    e11_decl='__declspec(section ".sdata2") extern const volatile u32 lbl_805E11F0;')
# P05: X05 cast + msgs materialized LAST (copy first)
add('P05_copyfirst_vguard', [(CH, '    lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;\n    char *msgs = lbl_80480240;\n')])
# P06: X05 + opt_propagation off (pin the hoisted read)
add('P06_x05_propoff', [(CH, CAST)], pragma='opt_propagation')
# P07: X05 + opt_lifetimes off
add('P07_x05_lifetimes', [(CH, CAST)], pragma='opt_lifetimes')
# P08: guard volatile + copy first + const-volatile decl
add('P08_copyfirst_constvol', [(CH, '    lbl_805D7CB4 = lbl_805E11F0;\n    char *msgs = lbl_80480240;\n')],
    e11_decl='extern const volatile u32 lbl_805E11F0;')
# P09: X05 but store BEFORE msgs, msgs as unsigned char*
add('P09_store_then_msgs_u8', [(CH, '    unsigned char *msgs = (unsigned char *)lbl_80480240;\n'
                                    '    lbl_805D7CB4 = *(volatile u32 *)&lbl_805E11F0;\n')])
# P10: X05 shape with the copy reading through a typed const pointer temp
add('P10_ptrtemp', [(CH, '    const volatile u32 *vp = (const volatile u32 *)&lbl_805E11F0;\n'
                         '    char *msgs = lbl_80480240;\n'
                         '    lbl_805D7CB4 = *vp;\n')])

for n, s in P.items():
    open(os.path.join(HERE, n + '.cpp'), 'w').write(s)
    print('wrote', n)
