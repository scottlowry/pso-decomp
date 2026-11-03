#!/usr/bin/env python3
"""Fingerprint a .o (or pre-dumped .asm): frame size, loop-2 ch2/off2 regs, case-0 px/py regs."""
import re, subprocess, sys, tempfile, os

def load_lines(path, sym='TAdPlayerLoadGC__sub_803F2F1C'):
    if path.endswith('.o'):
        fd, asm = tempfile.mkstemp(suffix='.asm'); os.close(fd)
        subprocess.run(['/opt/homebrew/opt/binutils/bin/objdump', '-d', path],
                       stdout=open(asm, 'w'), check=True)
    else:
        asm = path
    ins, inblock = [], False
    for l in open(asm):
        if re.match(r'^[0-9a-f]+ <.*>:', l):
            inblock = sym in l; continue
        if not inblock: continue
        m = re.match(r'^\s*[0-9a-f]+:\s+(?:[0-9a-f]{2} )+\t\s*(\S+)\s+(.*)$', l)
        if m: ins.append((m.group(1), m.group(2).strip()))
        elif re.match(r'^\s*[0-9a-f]+:\s+0 ?\t?\s*$', l): continue
    if asm != path: os.unlink(asm)
    return ins

def fp(path, label):
    ins = load_lines(path)
    frame = '?'
    for mn, op in ins:
        if mn == 'stwu':
            m = re.match(r'r1,(-?\d+)\(r1\)', op); frame = m.group(1) if m else '?'
            break
    ch2 = off2 = 'x'
    k68 = [k for k, (mn, op) in enumerate(ins) if mn == 'addi' and re.match(r'r(\d+),r\1,104$', op)]
    if k68:
        k = k68[0]; off2 = 'r' + re.match(r'r(\d+)', ins[k][1]).group(1)
        for j in range(max(0, k - 5), k):
            m = re.match(r'r(\d+),r\1,1$', ins[j][1])
            if m and ins[j][0] == 'addi': ch2 = 'r' + m.group(1)
        if ch2 == 'x': ch2 = '?'
    else:
        ch2 = 'no104'
    px = py = 'x'
    mtc = [k for k, (mn, op) in enumerate(ins) if mn == 'mtctr']
    if mtc:
        k = mtc[-1]  # last indirect call = case-0 arm (label 7948); -3 arm call precedes it
        for j in range(max(0, k - 40), k):
            mn, op = ins[j]
            m = re.match(r'r(\d+),r\d+,4$', op)
            if mn == 'addi' and m: px = 'r' + m.group(1)
            m = re.match(r'r(\d+),r\d+,8$', op)
            if mn == 'addi' and m: py = 'r' + m.group(1)
    else:
        px = 'nomtctr'
    print(f"{label:9s} frame={frame:>4s} ch2={ch2:>5s} off2={off2:>4s} px={px:>7s} py={py:>4s} rows={len(ins)}")

if __name__ == '__main__':
    for a in sys.argv[1:]:
        lab, p = a.split('=')
        fp(p, lab)
