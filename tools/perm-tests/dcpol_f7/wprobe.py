#!/usr/bin/env python3
"""Offline spelling-probe harness for dispatch_chunk_polygon_list (lane f7).

Compiles variants of the WHAREHOUSE TU (a copy of src/pso/unk/text_803E2D70.cpp)
with the unit's exact ninja MWCC command (via skills/probe_compile.sh) and scores
the target symbol against the orig asm with skills/probe_diff.py.

Usage:
  python3 wprobe.py                 # compile+score every variant in variants/
  python3 wprobe.py name1 name2     # subset
Base truth: ../probe.cpp (must be BASE-VERIFIED identical to the repo .o).
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
ORIG_WORDS = 0x304
env = dict(os.environ)
env["PATH"] = "/opt/homebrew/opt/binutils/bin:" + os.path.join(REPO, "build/binutils") + ":" + env["PATH"]


def orig_lines():
    txt = open(ASM).read()
    m = re.search(r"^\.fn " + SYM + r",.*?\n(.*?)^\.endfn", txt, re.M | re.S)
    return [l for l in m.group(1).splitlines()]


def ours_lines(o):
    p = subprocess.run(["powerpc-eabi-objdump", "-dr", o], capture_output=True, text=True, env=env)
    out, inside = [], False
    for ln in p.stdout.splitlines():
        if "<" + SYM + ">:" in ln:
            inside = True
            continue
        if inside:
            if re.match(r"^\s*$", ln):
                break
            mm = re.match(r"\s*[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(.*)", ln)
            if mm:
                out.append([mm.group(2).strip(), ""])
                continue
            rm = re.match(r"\s*(?:[0-9a-f]+:\s+)?R_PPC_\S+\s+(\S+)", ln)
            if rm and out and not out[-1][1]:
                out[-1][1] = rm.group(1)
    return ["\t" + t + (" {" + r + "}" if r else "") for t, r in out]


def norm(t):
    """Canonical form of one row, either side.

    Symbol-bearing rows (dtk 'sym@ha/@l/@sda21' or objdump reloc trailer
    '{name}') collapse to  mnemonic|regs|{NAME}  (displacements differ
    cosmetically between the two renderings). Plain rows keep their text
    with whitespace collapsed and internal branch targets -> BR.
    """
    t = t.strip()
    sym = None
    m = re.search(r"\{(\S+)\}\s*$", t)
    if m:
        sym = m.group(1)
        t = t[: m.start()]
    else:
        m = re.search(r"([A-Za-z_.$][\w.$]*)@(ha|l|sda21|sdai|toc|tocl|lcs)", t)
        if m:
            sym = m.group(1)
    if t.startswith("b") and re.match(r"^b\w*\s", t):
        mn = t.split()[0]
        if mn == "bl":
            if sym is None:
                tok = t.split()[-1]
                if not tok.startswith("0x") and not tok.startswith("{"):
                    sym = tok
            return f"bl|{{{sym}}}" if sym else "bl|TGT"
        if sym is None:
            t = "BR"
    if sym:
        mn = t.split()[0]
        regs = ",".join(re.findall(r"\br\d+\b", t))
        return f"{mn}|{regs}|{{{sym}}}"
    t = re.sub(r"\(\s*", "(", t)
    t = re.sub(r"\s*\)", ")", t)
    t = re.sub(r"\s+", " ", t)
    return t


def size_of(o):
    r = subprocess.run([GNM, "-S", o], capture_output=True, text=True, env=env)
    for ln in r.stdout.splitlines():
        if ln.endswith("T " + SYM):
            return int(ln.split()[1], 16)
    return None


def score(name):
    src = os.path.join(HERE, os.environ.get("VDIR", "variants"), name + ".cpp")
    out = os.path.join(HERE, "out", name)
    os.makedirs(out, exist_ok=True)
    log = os.path.join(out, "compile.log")
    with open(log, "w") as fh:
        subprocess.run(["sh", os.path.join(SKILL, "scripts/probe_compile.sh"), src, out,
                        "build/GPOE8P/src/pso/unk/text_803E2D70.o"],
                       cwd=REPO, stdout=fh, stderr=subprocess.STDOUT)
    o = os.path.join(out, os.path.basename(src).replace(".cpp", ".o"))
    if not os.path.exists(o):
        return (name, None, -1, -1, ["COMPILE-FAIL: " + open(os.path.join(out, "compile.log")).read()[-800:]])
    sz = size_of(o)
    # fleet truth: word-level reloc-aware diff via skills/probe_diff.py
    pr = subprocess.run(["python3", os.path.join(SKILL, "scripts/probe_diff.py"), o, SYM, ASM,
                         "0", str(ORIG_WORDS // 4 - 1)],
                        cwd=REPO, capture_output=True, text=True, env=env)
    rows = -1
    cosmetic = -1
    m = re.search(r"verdict: (\d+) REAL mismatches", pr.stdout)
    if m:
        rows = int(m.group(1))
        mc = re.search(r"(\d+) cosmetic", pr.stdout)
        cosmetic = int(mc.group(1)) if mc else 0
    else:
        m = re.search(r"verdict: (\d+) real mismatch\(es\), (\d+) cosmetic", pr.stdout)
        if m:
            rows, cosmetic = int(m.group(1)), int(m.group(2))
    detail = [ln for ln in pr.stdout.splitlines() if "MISMATCH" in ln]
    return (name, sz, cosmetic, rows, detail)


def main():
    names = sys.argv[1:]
    if not names:
        names = sorted(f[:-4] for f in os.listdir(os.path.join(HERE, "variants")) if f.endswith(".cpp"))
    for n in names:
        name, sz, cosmetic, rows, detail = score(n)
        flag = "SIZE-OK" if sz == ORIG_WORDS else ("no-symbol/compile-fail" if sz is None else "SIZE-GATE-FAIL-0x%x" % sz)
        print(f"{name:22s} {flag:22s} real={rows} cosmetic={cosmetic}")
        if detail and rows >= 0:
            print("\n".join(detail[:60]))


if __name__ == "__main__":
    main()
