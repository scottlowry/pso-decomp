#!/usr/bin/env python3
"""Fast offline oracle for dispatch_chunk_polygon_list spelling variants.

Compiles a variant TU copy with the unit's EXACT ninja MWCC command
(skills/probe_compile.sh), then compares the function's raw instruction WORDS
against the orig disasm, reloc-aware:
  R_PPC_REL24 (bl)   -> compare opcode|AA|LK bits only, require same target symbol
  R_PPC_ADDR16_HA/LO, R_PPC_EMB_SDA21, R_PPC_ADDR16 -> compare the upper 16 bits
                        (opcode+regs), require the orig line names the same symbol
Prints: size gate, per-slot mismatches (both texts), and a longest-common-run
similarity for ranking. Exit code = mismatch count (capped).

Usage: python3 wprobe2.py [variant ...]     (VDIR env selects the variant dir)
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SKILL = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"
SYM = "dispatch_chunk_polygon_list"
ASM = os.path.join(REPO, "build/GPOE8P/asm/pso/unk/text_803E2D70.s")
TU = "build/GPOE8P/src/pso/unk/text_803E2D70.o"
TARGET = 0x304
env = dict(os.environ)
env["PATH"] = "/opt/homebrew/opt/binutils/bin:" + os.path.join(REPO, "build/binutils") + ":" + env["PATH"]

RE_LOC = re.compile(r"/\*\s*([0-9A-F]{8})\s+[0-9A-F]{8}\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\t(.*)$")
MASKS = {
    "R_PPC_REL24": (0xFC000001, "call"),
    "R_PPC_ADDR16_HA": (0xFFFF0000, "ha"),
    "R_PPC_ADDR16_LO": (0xFFFF0000, "lo"),
    "R_PPC_ADDR16": (0xFFFF0000, "abs"),
    "R_PPC_EMB_SDA21": (0xFFE00000, "sda21"),
    "R_PPC_EMB_SDAI16": (0xFFE00000, "sdai"),
}
sym_cache = {}


def orig_rows():
    txt = open(ASM).read()
    m = re.search(r"^\.fn " + SYM + r",.*?\n(.*?)^\.endfn", txt, re.M | re.S)
    rows = []
    for ln in m.group(1).splitlines():
        mm = RE_LOC.match(ln.rstrip())
        if mm:
            rows.append((int(mm.group(2).replace(" ", ""), 16), mm.group(3).strip()))
    return rows


def our_rows(o):
    p = subprocess.run(["powerpc-eabi-objdump", "-dr", o], capture_output=True, text=True, env=env)
    rows, inside, pend = [], False, None

    def flush():
        if pend:
            rows.append(pend)

    for ln in p.stdout.splitlines():
        if "<" + SYM + ">:" in ln:
            inside = True
            continue
        if not inside:
            continue
        if re.match(r"^\s*$", ln):
            break
        mm = re.match(r"\s*[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(.*)", ln)
        if mm:
            flush()
            pend = [int(mm.group(1).replace(" ", ""), 16), mm.group(2).strip(), None]
            continue
        rm = re.match(r"\s*(?:[0-9a-f]+:\s+)?(R_PPC_\S+)\s+(\S+)", ln)
        if rm and pend and pend[2] is None:
            pend[2] = (rm.group(1), rm.group(2))
    flush()
    return rows


def orig_symbol(text):
    m = re.search(r"([A-Za-z_.$][\w.$]*)@(ha|l|sda21|sdai)", text)
    if m:
        return m.group(1)
    if text.startswith("bl "):
        return text.split()[1]
    return None


def orig_kind(text):
    m = re.search(r"@(ha|l|sda21|sdai)\b", text)
    if m:
        return {"ha": "ha", "l": "lo", "sda21": "sda21", "sdai": "sdai"}[m.group(1)]
    if text.startswith("bl "):
        return "call"
    return None


def canon(w, text, rel):
    """Word with internal-branch targets masked (they can never match)."""
    t = text.strip()
    mn = t.split()[0] if t else ""
    if rel is None and mn.startswith("b") and not mn.startswith("bl") and not mn.startswith("bd"):
        return w & 0xFC000003
    return w



def key(w, text, rel=None):
    """Canonical comparable token for one row, either side."""
    t = text.strip()
    mn = t.split()[0] if t else ""
    if rel:
        kind, sym = rel
        mask, tag = MASKS.get(kind, (0xFFFFFFFF, "?"))
        regs = re.findall(r"r\d+", t)
        if tag == "call":
            return f"call|{sym}"
        if tag == "ha":
            return f"ha|{regs[0] if regs else ''}|{sym}"
        if tag == "lo":
            return f"lo|{','.join(regs[:2])}|{sym}"
        return f"sda21|{mn}|{regs[0] if regs else ''}|{sym}"
    m = re.search(r"([A-Za-z_.$][\w.$]*)@(ha|l|sda21|sdai)\b", t)
    if m:
        regs = re.findall(r"r\d+", t)
        tag = m.group(2)
        if tag == "ha":
            return f"ha|{regs[0]}|{m.group(1)}"
        if tag == "l":
            return f"lo|{','.join(regs[:2])}|{m.group(1)}"
        return f"sda21|{mn}|{regs[0]}|{m.group(1)}"
    if mn == "bl":
        return "call|" + t.split()[1]
    if mn.startswith("b"):
        return mn
    return hex(w & 0xFFFFFFFF)


def canon(w, text, rel):
    return key(w, text, rel)


def size_of(o):
    r = subprocess.run([GNM, "-S", o], capture_output=True, text=True, env=env)
    for ln in r.stdout.splitlines():
        if ln.endswith("T " + SYM):
            return int(ln.split()[1], 16)
    return None




def siblings_diff(o):
    """Return symbols (other than SYM) whose instruction words changed vs the repo .o."""
    repo = os.path.join(REPO, TU)
    def symwords(path):
        pr = subprocess.run(["gnm", "-S", path], capture_output=True, text=True, env=env)
        syms = {}
        for ln in pr.stdout.splitlines():
            m = re.match(r"([0-9a-f]{8}) ([0-9a-f]{8}) T (\S+)$", ln.strip())
            if m:
                syms[m.group(3)] = (int(m.group(1), 16), int(m.group(2), 16))
        pd = subprocess.run(["powerpc-eabi-objdump", "-d", path], capture_output=True, text=True, env=env)
        cur = None
        words = {}
        for ln in pd.stdout.splitlines():
            m = re.match(r"^[0-9a-f]+ <(.+)>:$", ln.strip())
            if m:
                cur = m.group(1)
                words[cur] = []
                continue
            mm = re.match(r"\s*[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})", ln)
            if mm and cur:
                words[cur].append(mm.group(1).replace(" ", ""))
        return syms, words
    s1, w1 = symwords(repo)
    s2, w2 = symwords(o)
    out = []
    for name, (v, sz) in s1.items():
        if name == SYM or name not in s2:
            continue
        if w1.get(name) != w2.get(name):
            out.append(name)
    return out


def run(name):
    vdir = os.environ.get("VDIR", "variants")
    src = os.path.join(HERE, vdir, name + ".cpp")
    out = os.path.join(HERE, "out2", name)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "compile.log"), "w") as fh:
        subprocess.run(["sh", os.path.join(SKILL, "scripts/probe_compile.sh"), src, out, TU],
                       cwd=REPO, stdout=fh, stderr=subprocess.STDOUT)
    o = os.path.join(out, os.path.basename(src).replace(".cpp", ".o"))
    if not os.path.exists(o):
        print(f"{name:14s} COMPILE-FAIL")
        print(open(os.path.join(out, "compile.log")).read()[-700:])
        return None
    sz = size_of(o)
    ours = our_rows(o)
    orig = orig_rows()
    bad = []
    if os.environ.get("ALIGN"):
        import difflib
        A = [key(w, t) for w, t in orig]
        B = [key(r[0], r[1], r[2]) for r in ours]
        sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                continue
            if tag in ("replace", "delete"):
                for k in range(i1, i2):
                    print(f"   ORIGONLY/MISS {k:3d} {orig[k][1]}")
            if tag in ("replace", "insert"):
                for k in range(j1, j2):
                    print(f"   OURS-EXTRA    {k:3d} {ours[k][1]}")
        print(f"   align: orig={len(A)} ours={len(B)} same={sum(1 for t,i1,i2,j1,j2 in sm.get_opcodes() if t=='equal' for _ in range(i2-i1))}")
    if sz == TARGET or os.environ.get("ALWAYS"):
        for i in range(len(orig)):
            ow, ot = orig[i]
            if i >= len(ours):
                bad.append((i, ot, "<missing>", "len"))
                continue
            nw, nt, rel = ours[i]
            if rel:
                kind, symname = rel[0], rel[1]
                mask, tag = MASKS.get(kind, (0xFFFFFFFF, "?"))
                if key(ow, ot, None) != key(nw, nt, rel):
                    bad.append((i, ot, nt + " reloc=" + kind + " " + symname, "diff"))
            elif key(ow, ot, None) != key(nw, nt, None):
                bad.append((i, ot, nt, "word"))
    # similarity: longest common subsequence of words (objdiff-like proxy)
    a = [canon(w, t, None) for w, t in orig]
    b = [canon(r[0], r[1], r[2]) for r in ours]
    m = len(a)
    n = len(b)
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        prev = 0
        for j in range(1, n + 1):
            tmp = dp[j]
            dp[j] = prev + 1 if a[i - 1] == b[j - 1] else max(dp[j], dp[j - 1])
            prev = tmp
    lcs = dp[n]
    pct = 100.0 * lcs / max(m, n)
    frame = None
    bank = "?"
    for w, t, r in ours[:8]:
        m = re.search(r"stwu\s+r1,(-?\d+)\(r1\)", t)
        if m:
            frame = -int(m.group(1))
        m = re.search(r"(stmw\s+r(\d+)|savegpr_(\d+))", t)
        if m:
            bank = "r" + (m.group(2) or m.group(3)) + ("-31")
        if re.search(r"bl\s+.*savegpr", t) or (r and "savegpr" in r[1]):
            bank = "r" + re.sub(r".*savegpr_", "", r[1]) + "-31"
    sib = siblings_diff(o) if os.environ.get("SIB") else []
    if sib:
        print(f"{name}: SIBLING-DRIFT: {sib}")
    print(f"{name:14s} size={sz if sz is None else hex(sz)} {'GATE-OK' if sz == TARGET else 'GATE-FAIL'} frame={frame} bank={bank} insns={n} bad={len(bad)} lcs={lcs} ({pct:.3f}%)")
    if os.environ.get("SHOW"):
        for i, ot, nt, why in bad[:int(os.environ.get("SHOW"))]:
            print(f"   {i:3d} {why:5s} O: {ot}\n       {'':>5} N: {nt}")
    return (name, sz, len(bad) if sz == TARGET else 10 ** 6, pct)


def main():
    names = sys.argv[1:]
    if not names:
        vdir = os.environ.get("VDIR", "variants")
        names = sorted(f[:-4] for f in os.listdir(os.path.join(HERE, vdir)) if f.endswith(".cpp"))
    res = [run(n) for n in names]
    res = [r for r in res if r]
    print("--- ranked (gate pass first, then fewest bad, then lcs) ---")
    for r in sorted(res, key=lambda x: (x[1] != TARGET, x[2], -x[3])):
        print(f"{r[0]:14s} size={hex(r[1]) if r[1] else None} bad={r[2] if r[2] < 10**6 else 'gatefail'} lcs={r[3]:.3f}")


if __name__ == "__main__":
    main()
