#!/usr/bin/env python3.14
"""Grid round-4: q1 basin (entry=entry*10; entry=ch+entry; entry=entry-'0';)
crossed with ALL 120 decl orders x 6 pre-loop orders, hunting the target pool
(n=r6,i=r3,acc=r7,ch=r0,add r7,r0,r7). Size gate 248. Offline compiles only.
Prune: compile all; print every nbad<=2 and any exact.
"""
import os, re, subprocess, json, itertools

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
orig = open(f"{KIT}/gen_v44_subfirst.c").read()
ORIG_DECL = "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n"
ORIG_PRE = "n = *num_cnt;\n    i = 0;\n    entry = 0;"
ORIG_E = "entry = entry * 10 - '0' + ch;"
BODY = "entry = entry * 10;\n      entry = ch + entry;\n      entry = entry - '0';"

DECL_VARS = ["  s16 c;\n", "  s16 n;\n", "  char *dest;\n", "  s16 i;\n", "  u8 ch;\n"]
PRES = {
 "nie": "n = *num_cnt;\n    i = 0;\n    entry = 0;",
 "ine": "i = 0;\n    n = *num_cnt;\n    entry = 0;",
 "nie2": "n = *num_cnt;\n    entry = 0;\n    i = 0;",
 "eni": "entry = 0;\n    n = *num_cnt;\n    i = 0;",
 "ien": "i = 0;\n    entry = 0;\n    n = *num_cnt;",
 "ein": "entry = 0;\n    i = 0;\n    n = *num_cnt;",
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
        out.append((m.group(1).replace(" ", "").rstrip(), ""))
    return out

tw = [a for a, _ in words(f"{KIT}/target.o")]

def size_of(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

results = []
pi = 0
for perm in itertools.permutations(range(5)):
    decl = "".join(DECL_VARS[k] for k in perm)
    for pk in PRES:
        pi += 1
        name = f"k{''.join(map(str,perm))}_{pk}"
        src = orig.replace(ORIG_DECL, decl).replace(ORIG_PRE, PRES[pk]).replace(ORIG_E, BODY)
        c = f"{KIT}/gs4_{name}.c"; o = f"{KIT}/gs4_{name}.o"
        open(c, "w").write(src)
        r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o], capture_output=True, text=True, cwd=KIT)
        if r.returncode != 0:
            continue
        sz = size_of(o)
        try:
            w = [a for a, _ in words(o)]
        except StopIteration:
            continue
        if sz != 248 or len(w) != 62:
            continue
        bad = [k for k in range(62) if w[k] != tw[k]]
        results.append((name, bad))
        if bad == []:
            print(f"EXACT-MATCH {name}")
os.makedirs(f"{KIT}/gs4_keep", exist_ok=True)
for name, bad in results:
    if len(bad) <= 2:
        os.link(f"{KIT}/gs4_{name}.o", f"{KIT}/gs4_keep/{name}.o")
        os.link(f"{KIT}/gs4_{name}.c", f"{KIT}/gs4_keep/{name}.c")
results.sort(key=lambda r: len(r[1]))
print(f"compiled+gated: {len(results)}")
for name, bad in results[:20]:
    print(f"{name:14} nbad={len(bad)} {bad}")
json.dump([[n, b] for n, b in results], open(f"{KIT}/grid_round4.json", "w"), indent=1)
