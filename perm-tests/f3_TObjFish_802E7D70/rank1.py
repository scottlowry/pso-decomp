#!/usr/bin/env python3
"""Rank round-1 harvests: compile source.c, gate size==0x130, reject new symbols,
score raw objdiff -1 target.o -2 cand.o (ORIG-left match_percent), UB-screen, print sorted."""
import glob, json, os, re, subprocess, sys
KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/f3_TObjFish_802E7D70"
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
NM = "/opt/homebrew/opt/binutils/bin/gnm"
SYM = "TObjFish__sub_802E7D70"
GATE = 0x130
CHAMP = 99.86842

def size_of(obj):
    out = subprocess.run([NM, "-S", obj], capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM and p[2] in "tT":
            return int(p[1], 16)
    return None

def syms(obj):
    out = subprocess.run([NM, obj], capture_output=True, text=True).stdout
    return set(l.split()[-1] for l in out.splitlines() if len(l.split()) in (3, 4) and l.split()[-2] in "TtDdBbRrWw")

BASE_SYMS = syms(f"{KIT}/base_direct.o")

def ub_poison(txt):
    """any named local read at brace-depth 0 after last assign whose assigns are all
    inside non-returning branches OR first read precedes any assign (def-dominance violation)."""
    m = re.search(r"TObjFish__sub_802E7D70\s*\([^)]*\)\s*\{(.*)\}", txt, re.S)
    if not m: return False
    body = m.group(1)
    decls = re.findall(r"^\s*(?:Stack_802E7D70|s16|u16|u32|s32|TKtObj)\s*\*?\s*(\w+)\s*(?:=|;)", body, re.M)
    def depth_at(pos): return body.count("{", 0, pos) - body.count("}", 0, pos)
    for v in decls:
        if v == "block": continue
        assigns = [a.start() for a in re.finditer(rf"\b{v}\s*=", body)]
        uses = [u.start() for u in re.finditer(rf"\b{v}\b\s*(?:[-+.)\],;=]|$)", body) if body[u.start():u.start()+len(v)].strip() == v]
        uses = [u for u in uses if not any(abs(u-a) < 2 for a in assigns)]
        if not uses: continue
        if not assigns: return True  # never assigned, yet used
        first_use = min(uses)
        if first_use < min(assigns) and depth_at(first_use) <= depth_at(min(assigns)):
            return True  # read before any write
    return False

def official(obj):
    p = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", f"{KIT}/target.o", "-2", obj, "--format", "json", "-o", "-"], capture_output=True, text=True)
    if p.returncode != 0: return None
    try:
        d = json.loads(p.stdout)
        L = d.get("left") or {}
        best = None
        for s in L.get("symbols", []):
            if SYM in str(s.get("name", "")):
                mp = s.get("match_percent")
                if mp is not None: best = mp if best is None else max(best, mp)
        return best
    except Exception:
        return None

rows = []
dirs = [d for d in glob.glob(f"{KIT}/output-*") if os.path.isdir(d)]
for d in sorted(dirs):
    src = f"{d}/source.c"
    if not os.path.exists(src): continue
    o = d + ".o"
    if os.path.exists(o) and os.path.getmtime(o) > os.path.getmtime(src):
        pass
    else:
        r = subprocess.run(["bash", f"{KIT}/compile.sh", src, "-o", o], capture_output=True, cwd=REPO)
        if r.returncode != 0 or not os.path.exists(o):
            rows.append((d, "COMPILEFAIL", None)); continue
    sz = size_of(o)
    if sz != GATE:
        rows.append((d, f"SIZE-GATE {sz}", None)); continue
    extra = syms(o) - BASE_SYMS - {SYM}
    if extra:
        rows.append((d, f"NEWSYM {sorted(extra)}", None)); continue
    txt = open(src).read()
    if ub_poison(txt):
        rows.append((d, "UB-POISON", None)); continue
    pct = official(o)
    rows.append((d, pct, txt.count("\n")))

rows.sort(key=lambda x: (x[1] is None, -(x[1] or 0) if isinstance(x[1], float) else 0))
beats = [r for r in rows if isinstance(r[1], float) and r[1] > CHAMP]
for d, v, _ in rows[:25]:
    print(f"{os.path.basename(d):28} {v}")
print(f"total {len(rows)} dirs; beats>{CHAMP}: {len(beats)}")
for d, v, _ in beats[:5]:
    print("BEAT:", d, v)
