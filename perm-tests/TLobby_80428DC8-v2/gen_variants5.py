#!/usr/bin/env python3.14
"""Grid round-3: inside the m3/m4 nbad=1 basin, flip the add operand token
(ch + entry vs entry + ch) and its fold/assign spellings, hunt add r7,r0,r7.
"""
import os, re, subprocess, json, itertools

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
BASE_SRC = f"{KIT}/gen_v44_subfirst.c"
orig = open(BASE_SRC).read()
ORIG_DECL = "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n"
ORIG_PRE = "n = *num_cnt;\n    i = 0;\n    entry = 0;"
ORIG_E = "entry = entry * 10 - '0' + ch;"

Q = {
 "q1":  "entry = entry * 10;\n      entry = ch + entry;\n      entry = entry - '0';",
 "q2":  "entry = entry * 10;\n      entry = ch + entry;\n      entry -= '0';",
 "q3":  "entry *= 10;\n      entry = ch + entry;\n      entry = entry - '0';",
 "q4":  "entry = entry * 10;\n      entry = ch + entry;\n      entry -= 48;",
 "q5":  "entry = entry * 10;\n      entry = ch + entry - '0';",
 "q6":  "entry = entry * 10;\n      entry = ch + (entry - '0');",
 "q7":  "entry *= 10;\n      entry = ch + entry - '0';",
 "q8":  "entry = entry * 10;\n      entry = ch + entry;\n      entry = entry - 48;",
 "q9":  "entry = entry * 10;\n      entry = (ch + entry) - '0';",
 "q10": "entry = entry * 10 - '0';\n      entry = ch + entry;",
 "q11": "entry = entry * 10 - '0';\n      entry += ch;",
 "q12": "entry = entry * 10;\n      entry = ch + entry;\n      entry = '0' ^ entry ^ '0';\n      entry -= '0';",  # noise-guard, will fail size
}
PRES = {
 "nie": "n = *num_cnt;\n    i = 0;\n    entry = 0;",
 "ien": "i = 0;\n    entry = 0;\n    n = *num_cnt;",
 "ine": "i = 0;\n    n = *num_cnt;\n    entry = 0;",
}
DECLS = {
 "d0": ORIG_DECL,
 "d2":  "  s16 c;\n  s16 n;\n  s16 i;\n  char *dest;\n  u8 ch;\n",
 "d3":  "  s16 c;\n  s16 n;\n  u8 ch;\n  char *dest;\n  s16 i;\n",
}

def words(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)\s*(.*)", l)
        if not m:
            if out and not l.strip().startswith("R_PPC"):
                break
            continue
        out.append((m.group(1).replace(" ", "").rstrip(), m.group(2).split("#")[0].strip()))
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

results = []
for (qk, pk, dk) in itertools.product(Q, PRES, DECLS):
    if (qk, pk, dk) == ("q1", "nie", "d0"):
        pass
    name = f"h_{qk}_{pk}_{dk}"
    src = orig.replace(ORIG_DECL, DECLS[dk]).replace(ORIG_PRE, PRES[pk]).replace(ORIG_E, Q[qk])
    c = f"{KIT}/gridsrc_{name}.c"; o = f"{KIT}/grid_{name}.o"
    open(c, "w").write(src)
    r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o], capture_output=True, text=True, cwd=KIT)
    if r.returncode != 0:
        results.append((name, "FAIL", None)); continue
    sz = size_of(o)
    try:
        w = words(o)
    except StopIteration:
        results.append((name, "NOSYM", None)); continue
    if sz != 248 or len(w) != 62:
        results.append((name, f"SZ{sz}/{len(w)}", None)); continue
    bad = [k for k in range(62) if w[k][0] != tw[k][0]]
    results.append((name, "OK", bad))

hits = [r for r in results if r[2] == []]
for name, st, bad in sorted(results, key=lambda r: (len(r[2]) if isinstance(r[2], list) else 99)):
    if isinstance(bad, list) and len(bad) <= 4 or hits:
        pass
    print(f"{name:18} {st:8} bad={bad}")
print(f"\nEXACT-MATCH: {len(hits)} -> {[h[0] for h in hits]}")
