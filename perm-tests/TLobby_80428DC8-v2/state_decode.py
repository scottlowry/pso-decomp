#!/usr/bin/env python3.14
"""Decode the exact loop-pool HOME STATE of a candidate .o for TLobby__sub_80428DC8
by extracting the instruction sequence from the 'b' (loop skip) to the 'sth' (num_cnt
store), and diffing it against the original disassembly block."""
import re, subprocess, sys, os

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
ORIG = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/GPOE8P/asm/pso/misc/TLobby_80428374.s"

def load_orig():
    txt = open(ORIG).read()
    m = re.search(r"^\.fn TLobby__sub_80428DC8[^\n]*\n(.*?)^\.endfn", txt, re.S | re.M)
    out = []
    for l in m.group(1).splitlines():
        after = l.split("*/")[-1]
        if after.strip():
            out.append(re.sub(r"\s+", " ", after.strip()))
    return out

def disasm(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)", l)
        if not m:
            break
        rest = l[m.end():].strip()
        rest = re.sub(r"0x[0-9a-f]+<[^>]*>", lambda g: g.group(0).split("<")[0], rest)
        rest = re.sub(r"\s+#\s*[0-9a-f]+.*$", "", rest)
        rest = re.sub(r"\s+", " ", rest).strip()
        if rest:
            out.append(rest)
    return out

def norm(t):
    return re.sub(r"(?<![\w])(?:0x)?([0-9a-fA-F]+)(?![\w(])",
                  lambda m: hex(int(m.group(1), 16)) if not m.group(1).isalpha() else m.group(0),
                  t)

def loop_block(insns):
    """from first li after the second cmpwi/bne to the final 'sth' — the volatile pool."""
    start = None
    for k, t in enumerate(insns):
        if t.startswith("lha") and "(r30)" in t:
            start = k
    end = max(k for k, t in enumerate(insns) if t.startswith("sth "))
    return [norm(x) for x in insns[start:end + 1]]

ORIG_INS = load_orig()
print("ORIG loop pool block:")
for t in loop_block(ORIG_INS):
    print("   ", t)
for path in sys.argv[1:]:
    name = os.path.basename(path)
    ins = disasm(path)
    print(f"\n{name} ({len(ins)} insns):")
    ob, cb = loop_block(ORIG_INS), loop_block(ins)
    n = max(len(ob), len(cb))
    for k in range(n):
        o = ob[k] if k < len(ob) else "--"
        c = cb[k] if k < len(cb) else "--"
        flag = "   " if o == c else " ! "
        print(f" {flag}{o:38} | {c}")
