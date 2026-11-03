#!/opt/homebrew/bin/python3.14
"""run_probes_v3.py — offline probe compile+score+home-classify (no repo builds).
For each ../q*.c: compile.sh -> probe .o, then report match/size + slwi/add homes +
fold-vs-champ verdict + diff-slot list."""
import glob, json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
OD = f"{REPO}/build/binutils/powerpc-eabi-objdump"
ODC = f"{REPO}/build/tools/objdiff-cli"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/misc/TRaderMapCore.o"
SYM = "draw_compass__13TRaderMapCoreFv"

def insns(o, bytes_only=False):
    p = subprocess.run([OD, "-d", o], capture_output=True, text=True).stdout
    m = re.search(r"<" + SYM + r">:|<draw_compass\S*>:", p)
    out = []
    if m:
        for l in p[m.end():].splitlines():
            mm = re.match(r"^\s+[0-9a-f]+:\t((?:[0-9a-f]{2} ){4})\t(.*)$", l)
            if mm:
                w = mm.group(1).replace(" ", "")
                out.append(w if bytes_only else (w, mm.group(2).strip()))
                continue
            if re.match(r"^\s+[0-9a-f]+:\t", l):  # reloc continuation
                continue
            if out and (re.match(r"^[0-9a-f]+ <.*>:", l) or (l.strip() and not l.startswith(" "))):
                break
    return out

def homes(ins):
    slwi, slwi_reg, add_i, addreg = None, "?", None, "?"
    for i, t in enumerate(ins):
        t = t[1] if isinstance(t, tuple) else t
        m = re.match(r"slwi\s+(r\d+)\s*,\s*r30\s*,\s*4", t)
        if m:
            slwi, slwi_reg = i, m.group(1)
            for j in range(i, min(i + 10, len(ins))):
                tj = ins[j][1] if isinstance(ins[j], tuple) else ins[j]
                m2 = re.match(r"add\s+r30\s*,\s*r4\s*,\s*(r\d+)", tj)
                if m2:
                    addreg, add_i = m2.group(1), j
                    break
            return slwi, slwi_reg, add_i, addreg
    return slwi, slwi_reg, add_i, addreg

def objdiff_rows(o):
    p = subprocess.run([ODC, "diff", "-1", ORIG_O, "-2", o, SYM, "--format", "json", "-o", "-"],
                       capture_output=True, text=True)
    d = json.loads(p.stdout)
    def sym(side):
        for s in d[side]["symbols"]:
            if isinstance(s, dict) and SYM in str(s.get("name", "")): return s
    ro, rn = sym("left").get("instructions", []), sym("right").get("instructions", [])
    def fmt(r):
        if not r: return "<none>"
        i = r.get("instruction")
        return str(i.get("formatted") or i.get("text")) if i else f"<{r.get('kind','?')}>"
    diffs = [(i, fmt(a), fmt(b)) for i, (a, b) in enumerate(itertools.zip_longest(ro, rn)) if fmt(a) != fmt(b)]
    match = sym("left").get("match_percent")
    return match, len(rn), diffs

import itertools
champ = insns(f"{REPO}/build/GPOE8P/src/pso/misc/TRaderMapCore.o")
ch_home = homes(champ)
print(f"CHAMP home: slwi@{ch_home[0]} {ch_home[1]}  add@{ch_home[2]} {ch_home[3]}")
for src in sorted(glob.glob(f"{K}/q*.c")):
    o = src[:-2] + ".o"
    if not os.path.exists(o) or os.path.getmtime(o) < os.path.getmtime(src):
        r = subprocess.run(["bash", "compile.sh", src, "-o", o], cwd=HERE, capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(o):
            print(f"{os.path.basename(src)}: COMPILE FAIL {r.stderr[-150:]}"); continue
    ins = insns(o)
    h = homes(ins)
    fold = ([x[0] for x in ins] == [x[0] for x in champ])
    nbytes = len(insns(o, bytes_only=True)) * 4
    match, nsize, diffs = objdiff_rows(o)
    slots = [d[0] for d in diffs]
    nm = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", o], capture_output=True, text=True).stdout
    sz = next((int(l.split()[1], 16) for l in nm.splitlines() if SYM in l and " T " in l), None)
    print(f"{os.path.basename(src):26} match={match} insns={nsize} bytes-to-blr={nbytes} nm={sz} home=({h[1]},{h[3]}) slots={slots} {'FOLD=champ' if fold else 'DISTINCT'}")
