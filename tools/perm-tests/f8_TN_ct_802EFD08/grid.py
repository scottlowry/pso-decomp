#!/usr/bin/env python3
"""Variant grid for TBoss7TentacleNeedle__ct copy-block staging.
Zero repo builds: compiles via probe_compile.sh (verbatim TU flags).
PASS = size 104 words AND raw-word diff vs ORIG dtk == {20,21,39,40,58,59} (cosmetic pool imm fields)."""
import re, struct, subprocess, sys, os

KIT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KIT, '..', '..', '..'))
SKILL = '/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts'
UNIT_O = f'{REPO}/build/GPOE8P/src/pso/boss/TBoss7TentacleNeedle.o'
FN = 'TBoss7TentacleNeedle__ct'
CT_VA, UNIT_TEXT_VA, O_TEXT = 0x802EFD08, 0x802EF800, 0x34

def elf_text(path):
    out = subprocess.run([f'{REPO}/build/binutils/powerpc-eabi-objdump', '-h', path],
                         capture_output=True, text=True).stdout
    m = re.search(r'^\s*0\s+\.text\s+([0-9a-f]+)\s+[0-9a-f]+\s+[0-9a-f]+\s+([0-9a-f]+)', out, re.M)
    size, off = int(m.group(1), 16), int(m.group(2), 16)
    b = open(path, 'rb').read()
    return b[off:off+size]

def symval(path):
    out = subprocess.run(['/opt/homebrew/opt/binutils/bin/gnm', '-S', path],
                         capture_output=True, text=True).stdout
    for l in out.splitlines():
        p = l.split()
        if len(p) >= 4 and p[3] == FN:
            return int(p[0], 16), int(p[1], 16)
    return None, None

# orig words from dtk block
s = open(f'{REPO}/build/GPOE8P/asm/pso/boss/TBoss7TentacleNeedle.s').read()
blk = s[s.index(f'.fn {FN}'):]
orig = []
for l in blk.splitlines():
    if l.strip().startswith('.endfn'): break
    m = re.match(r'/\* (8[0-9A-F]{7}) [0-9A-F ]+((?: [0-9A-F]{2}){4}) \*/', l)
    if m: orig.append(struct.unpack('>I', bytes.fromhex(m.group(2).replace(' ', '')))[0])
assert len(orig) == 104, len(orig)
POOL = {20, 21, 39, 40, 58, 59}

STAGING = """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w2 = ((s32 *)pos)[2];
    w1 = ((s32 *)pos)[1];
    w0 = ((s32 *)pos)[0];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;"""

VARIANTS = {
 'champ_c3': STAGING,
 'V1_natural': """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w0 = ((s32 *)pos)[0];
    w1 = ((s32 *)pos)[1];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V2_natdeclrev': """    s32 w2; s32 w1; s32 w0; s32 v[3];
    w0 = ((s32 *)pos)[0];
    w1 = ((s32 *)pos)[1];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V3_f7adapt': """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w2 = ((s32 *)pos)[0];
    w0 = w2;
    w1 = ((s32 *)pos)[1];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V4_midfirst': """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w1 = ((s32 *)pos)[1];
    w0 = ((s32 *)pos)[0];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V5_direct': """    s32 v[3];
    v[0] = ((s32 *)pos)[0];
    v[1] = ((s32 *)pos)[1];
    v[2] = ((s32 *)pos)[2];""",
 'V6_nat_revstore': """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w0 = ((s32 *)pos)[0];
    w1 = ((s32 *)pos)[1];
    w2 = ((s32 *)pos)[2];
    v[2] = w2;
    v[1] = w1;
    v[0] = w0;""",
 'V7_commanat': """    s32 w0; s32 w1; s32 w2; s32 v[3];
    w0 = (0, ((s32 *)pos)[0]);
    w1 = (0, ((s32 *)pos)[1]);
    w2 = (0, ((s32 *)pos)[2]);
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V8_f7declrev': """    s32 w2; s32 w1; s32 w0; s32 v[3];
    w2 = ((s32 *)pos)[0];
    w0 = w2;
    w1 = ((s32 *)pos)[1];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;""",
 'V9_c3revstore': STAGING.replace('v[0] = w0;\n    v[1] = w1;\n    v[2] = w2;', 'v[2] = w2;\n    v[1] = w1;\n    v[0] = w0;'),
}

base = open(f'{KIT}/base.cpp').read()
champ = struct.unpack('>104I', elf_text(UNIT_O)[CT_VA - UNIT_TEXT_VA:CT_VA - UNIT_TEXT_VA + 416])
print('champ-vs-orig diff slots:', [i for i in range(104) if champ[i] != orig[i]])

for name, stag in VARIANTS.items():
    assert STAGING in base
    src = base.replace(STAGING, stag)
    cpp = f'{KIT}/cand_{name}.cpp'; obj = f'{KIT}/cand_{name}.o'
    open(cpp, 'w').write(src)
    r = subprocess.run(['sh', f'{SKILL}/probe_compile.sh', cpp, obj,
                        f'build/GPOE8P/src/pso/boss/TBoss7TentacleNeedle.o'],
                       capture_output=True, text=True, cwd=REPO)
    if r.returncode != 0:
        print(f'{name}: COMPILEFAIL {r.stderr[-200:]}'); continue
    val, size = symval(obj)
    if size != 416:
        print(f'{name}: size=0x{size:x} SKIP'); continue
    t = elf_text(obj)
    words = struct.unpack('>104I', t[val:val+416])
    copyok = all(words[i] == orig[i] for i in (76, 78, 79, 81))
    cascade = [i for i in range(104) if i not in (76, 78, 79, 81) and words[i] != champ[i]]
    if name == 'champ_c3':
        good = (not cascade) and not copyok
        print(f'champ_c3 BASE-VERIFY: diff-vs-repo-outer={cascade} copywords={copyok} -> ' +
              ('OK mirror trustworthy' if good else 'MIRROR MISMATCH'))
        continue
    tag = 'PASS-100' if copyok and not cascade else 'fail'
    print(f'{name}: copywords={copyok} cascade={cascade[:12]} {tag}')
