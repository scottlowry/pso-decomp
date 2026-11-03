#!/usr/bin/env python3.14
"""Grid round-6: pragma bisection around the m4 body — hunt add-operand-order
flip via opt_lifetimes / opt_common_subs / opt_dead_assignments / propagation.
"""
import os, re, subprocess, itertools

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
base = open(f"{KIT}/rS4m4/base.c").read()

PRAGMAS = ["opt_lifetimes", "opt_common_subs", "opt_dead_assignments", "opt_propagation", "peep", "opt_strict_imaged_conv"]

def words(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)\s*", l)
        if not m:
            if out and not l.strip().startswith("R_PPC"):
                break
            continue
        out.append(m.group(1).replace(" ", "").rstrip())
    return out

tw = words(f"{KIT}/target.o")

def size_of(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

FN_START = "void TLobby__sub_80428DC8(s16 entry, s16 slot, u8 *text, s16 *cnt, s16 *num_cnt)\n{"

results = []
for state in ("on", "off"):
    src = base.replace(FN_START,
        f"#pragma push\n#pragma {PRAG} {state}\n#pragma pop\n\n" + FN_START) if False else None
for combo in [(p, s) for p in PRAGMAS for s in ("off", "on")] + \
             [(["opt_lifetimes", "opt_common_subs"], "off"), (["opt_lifetimes", "opt_dead_assignments"], "off")]:
    p, s = combo
    ps = [p] if isinstance(p, str) else p
    block = "#pragma push\n" + "".join(f"#pragma {q} {s}\n" for q in ps) + "#pragma pop\n\n"
    if FN_START not in base:
        print("FN-MATCH-FAIL"); break
    src = base.replace(FN_START, block + FN_START)
    name = "x_" + "_".join(x.replace("opt_", "") for x in ps) + s
    c = f"{KIT}/gs6_{name}.c"; o = f"{KIT}/gs6_{name}.o"
    open(c, "w").write(src)
    r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o], capture_output=True, text=True, cwd=KIT)
    if r.returncode != 0:
        print(f"{name:30} COMPILE-FAIL {r.stderr.strip().splitlines()[-1] if r.stderr else ''}"); continue
    sz = size_of(o)
    try:
        w = words(o)
    except StopIteration:
        print(f"{name:30} NOSYM"); continue
    bad = [k for k in range(62) if w[k] != tw[k]] if len(w) == 62 else [f"LEN{len(w)}"]
    print(f"{name:30} sz={sz} nbad={len(bad)} {bad}")
