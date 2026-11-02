#!/usr/bin/env python3
# Variant grid for text_802E34AC __sinit synthesis: K decl position x g-expression form.
import subprocess, re, itertools, os

R = '/Users/scott/Hermes/pso-decomp/pso-decomp-f7/'
KIT = R + 'tools/perm-tests/text_802E34AC_sinit/'
FLAGS = ['-nodefaults', '-proc', 'gekko', '-align', 'powerpc', '-enum', 'int', '-fp', 'hardware',
         '-Cpp_exceptions', 'off', '-RTTI', 'off', '-str', 'reuse', '-maxerrors', '1', '-nosyspath',
         '-i', 'build/GPOE8P/include', '-i', 'include', '-i', 'src', '-i', 'libs/dolphin/include',
         '-i', 'libs/dolphin/include/dolphin', '-char', 'signed', '-use_lmw_stmw', 'on', '-O4,s',
         '-inline', 'off', '-sdata2', '4', '-lang', 'c++']

base = open(KIT + 'probe_802E34AC_v1.cpp').read()
# carve out the data-objects section between the Handler typedef and the table
mt = re.search(r'typedef void \(TAdSinglePlyChrSelectGC::\*Handler\)\(\);\n', base)
mo = re.search(r'// 50-slot state-action', base)
assert mt and mo, 'carve'
head, typedef_blk, tail = base[:mt.start()], mt.group(0), base[mo.start():]
OBJ = '''__declspec(section ".data") static f32 lbl_804E3040[2] = {
    0.5f * (640.0f - lbl_80472930[0]), 90.0f,
};
__declspec(section ".data") static f32 lbl_804E3048[2] = {
    20.0f + lbl_804E3040[0], 10.0f + (lbl_804E3040[1] + lbl_80472930[1]),
};
__declspec(section ".data") static f32 lbl_804E3050[2] = {
    %G%, lbl_804E3048[1] - 85.0f,
};
'''
KOBJ = 'static f32 lbl_805D68E0 = lbl_80472930[0] - 40.0f;\n'
GSWAP = 'lbl_804E3040[0] + 0.5f * lbl_80472930[0]'
GORIG = '0.5f * lbl_80472930[0] + lbl_804E3040[0]'
GWIDE = 'lbl_804E3040[0] + lbl_80472930[0] * 0.5f'

results = []
for kpos, (gname, gexpr) in itertools.product(
        ['first', 'after040', 'after048', 'last'],
        [('orig', GORIG), ('swap', GSWAP), ('wide', GWIDE)]):
    objs = OBJ.replace('%G%', gexpr)
    if kpos == 'first': src = head + '\n' + typedef_blk + '\n' + KOBJ + objs + tail
    elif kpos == 'after040':
        a, b = objs.split('__declspec(section ".data") static f32 lbl_804E3048')
        src = head + '\n' + typedef_blk + '\n' + a + KOBJ + '__declspec(section ".data") static f32 lbl_804E3048' + b + tail
    elif kpos == 'after048':
        a, b = objs.split('__declspec(section ".data") static f32 lbl_804E3050')
        src = head + '\n' + typedef_blk + '\n' + a + KOBJ + '__declspec(section ".data") static f32 lbl_804E3050' + b + tail
    else:
        src = head + '\n' + typedef_blk + '\n' + objs + KOBJ + tail
    name = f'grid_k{kpos}_g{gname}'
    p = KIT + name + '.cpp'
    open(p, 'w').write(src)
    o = KIT + name + '.o'
    r = subprocess.run([R + 'build/tools/wibo', R + 'build/compilers/GC/2.6/mwcceppc.exe'] + FLAGS + ['-c', p, '-o', o], cwd=R, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(o):
        print(name, 'COMPILE FAIL', r.stdout[-300:], r.stderr[-200:]); continue
    g = subprocess.run(['/opt/homebrew/opt/binutils/bin/gnm', '-S', o], capture_output=True, text=True).stdout
    sz = re.search(r'00000000 ([0-9a-f]{8}) t __sinit', g)
    size = int(sz.group(1), 16) if sz else -1
    has_fma = 'fmadds' in subprocess.run([R + 'build/binutils/powerpc-eabi-objdump', '-d', o], capture_output=True, text=True).stdout
    print(name, 'size=', hex(size), 'fma=', has_fma, 'GATE' if size == 0x638 else '')
    results.append((name, size, has_fma))
