#!/usr/bin/env python3
"""harvest_dcpol.py — dcpol_f7 perm round screener.
Pipeline per output-*/source.c: compile via kit compile.sh -> gnm size (gate 0x304 FIRST),
NEWSYM screen (defined-symbol diff vs base_direct.o), ub_poison def-dominance screen
(fleet law, copied from scripts/harank_shared.py), then rank survivors with the
wprobe2.py reloc-aware oracle (rows vs era dtk block; bad + lcs + perm score from dir name).
BASE-VERIFY non-vacuous: require .o exists, >0 fn rows, size non-None per candidate.
Usage: python3.14 harvest_dcpol.py   (run from kit perm/ dir)
"""
import os, re, subprocess, sys, glob, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
KITSRC = os.path.abspath(os.path.join(HERE, ".."))   # dcpol_f7/ (holds wprobe2.py)
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f7"
SYM = "dispatch_chunk_polygon_list"
GATE = 0x304
NM = REPO + "/build/binutils/powerpc-eabi-nm"
env = dict(os.environ)
env["PATH"] = "/opt/homebrew/opt/binutils/bin:" + REPO + "/build/binutils:" + env["PATH"]

# load wprobe2 as module for the row oracle
spec = importlib.util.spec_from_file_location("wprobe2", os.path.join(KITSRC, "wprobe2.py"))
wp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wp)

def defined_syms(obj):
    out = subprocess.run([NM, obj], capture_output=True, text=True).stdout
    return set(l.split()[-1] for l in out.splitlines()
               if len(l.split()) == 3 and l.split()[1] in "TtDdBbRrWw")

BASE_SYMS = defined_syms(os.path.join(HERE, "base_direct.o"))

# ---- ub_poison (fleet law — exact depth-dominance logic from scripts/harank_shared.py,
# generalized to this unit's decl types) ----
def ub_poison(txt):
    """An alias local whose only assignments sit inside nested blocks while it is read
    at top level afterwards -> non-dominating def, UB. Conservative over-approx."""
    import re as _re
    m = _re.search(r"dispatch_chunk_polygon_list\s*\([^)]*\)\s*\{(.*)\}\s*$", txt, _re.S)
    if not m:
        return False
    body = m.group(1)
    decls = set(x.strip().rstrip("* ").split()[-1] for x in _re.findall(
        r"^\s*(?:signed|unsigned|int|char|short|long|float|s8|u8|s16|u16|s32|u32|permbool|Vtx_\w+|void)\s*\*?\s*(\w+)\s*;",
        body, _re.M))
    decls |= set(_re.findall(r"\b(new_var\w*|temp\w*|alias\w*)\b(?=\s*[=.)\[])", body))
    for v in decls:
        if v in ("if", "while", "for", "switch", "return", "else", "case", "break"):
            continue
        assigns = [a.start() for a in _re.finditer(rf"\b{v}\s*=\s*[^=]", body)]
        if not assigns:
            continue
        uses = [u.start() for u in _re.finditer(rf"\b{v}\b", body)
                if _re.match(rf"\b{v}\s*=", body[u.start():u.start()+len(v)+2]) is None]
        def depth_at(pos):
            return body.count("{", 0, pos) - body.count("}", 0, pos)
        late_uses = [u for u in uses if u > max(assigns) and depth_at(u) == 0]
        if late_uses and all(depth_at(a) >= 1 for a in assigns):
            return True
    return False
# -------------------------------------------------------------------------

def fn_rows(o):
    return wp.our_rows(o)

def score_perm(dirname):
    m = re.search(r"output-(\d+)-", dirname)
    return int(m.group(1)) if m else None

def main():
    champ_perm = int(sys.argv[1]) if len(sys.argv) > 1 else 115
    cands = sorted(glob.glob(os.path.join(HERE, "output-*")), key=lambda p: os.path.getmtime(p))
    cands = [c for c in cands if os.path.isdir(c)]
    orig = wp.orig_rows()
    rows = []
    for c in cands:
        name = os.path.basename(c)
        csrc = os.path.join(c, "source.c")
        if not os.path.exists(csrc):
            continue
        co = c + ".o"
        if os.path.exists(co) and os.path.getmtime(co) > os.path.getmtime(csrc):
            pass  # fresh object reuse OK
        else:
            r = subprocess.run(["bash", os.path.join(HERE, "compile.sh"), csrc, "-o", co],
                               cwd=HERE, env=env, capture_output=True, text=True)
            if r.returncode != 0 or not os.path.exists(co):
                print(f"{name}: COMPILE-FAIL", r.stdout[-300:] if r.stdout else r.stderr[-300:])
                continue
        sz = wp.size_of(co)
        rows_ = fn_rows(co)
        # BASE-VERIFY non-vacuous
        if sz is None or len(rows_) < 150:
            print(f"{name}: BAD-OBJ sz={sz} rows={len(rows_)}")
            continue
        new = defined_syms(co) - BASE_SYMS
        txt = open(csrc).read()
        poison = ub_poison(txt)
        # oracle: bad rows vs era + lcs pct
        ours = rows_
        bad = 0
        for i in range(len(orig)):
            ow, ot = orig[i]
            if i >= len(ours):
                bad += 1; continue
            nw, nt, rel = ours[i]
            if wp.key(ow, ot, None) != wp.key(nw, nt, rel):
                bad += 1
        a = [wp.canon(w, t, None) for w, t in orig]
        b = [wp.canon(r[0], r[1], r[2]) for r in ours]
        m_, n_ = len(a), len(b)
        dp = [0]*(n_+1)
        for i in range(1, m_+1):
            prev = 0
            for j in range(1, n_+1):
                tmp = dp[j]
                dp[j] = prev+1 if a[i-1]==b[j-1] else max(dp[j], dp[j-1])
                prev = tmp
        lcs = dp[n_]
        pct = 100.0*lcs/max(m_, n_)
        flags = []
        if new: flags.append("NEWSYM:" + ",".join(sorted(new)))
        if poison: flags.append("UB_POISON")
        perm = score_perm(name)
        gate = (sz == GATE)
        rows.append((perm, gate, sz, bad, pct, name, flags))
        print(f"{name}: perm={perm} {'GATE-304' if gate else 'size=0x%X' % sz} bad={bad} lcs={pct:.3f}% {' '.join(flags)}")
    print("--- ranked: gate304 first, then bad-rows, then oracle-lcs ---")
    for perm, gate, sz, bad, pct, name, flags in sorted(rows, key=lambda x: (not x[1], x[3], -x[4], x[0] if x[0] is not None else 9999)):
        rej = " ".join(flags)
        mark = "REJECT" if flags else ("BEAT-CHAMP" if (perm is not None and perm < champ_perm) else "")
        print(f"{name:24s} gate={'Y' if gate else 'N(0x%X)'%sz} bad={bad:3d} lcs={pct:7.3f} perm={perm} {mark} {rej}")

if __name__ == "__main__":
    main()
