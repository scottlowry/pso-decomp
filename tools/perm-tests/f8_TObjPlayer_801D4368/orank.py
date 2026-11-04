#!/usr/bin/env python3
"""orank.py — official objdiff % for kit-compiled candidates (zero repo builds).
Ported from TLobby_803C0238 kit (REPO fixed to f8 worktree).
Usage: orank.py <name> [...] (uses v/<name>/out.o)  or  orank.py --all  or  orank.py <file.o>...
"""
import json, os, subprocess, sys, glob, tempfile

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
D = f"{REPO}/tools/perm-tests/f8_TObjPlayer_801D4368"
TARGET = f"{D}/target.o"
SYM = "TObjPlayer__sub_801D4368"
GATE = 0x248
NM = "/opt/homebrew/opt/binutils/bin/gnm"


def fn_size(obj):
    out = subprocess.run([NM, "-S", obj], capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM and p[2] in "tT":
            return int(p[1], 16)
    return None


def score(obj):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", TARGET, "-2", obj,
                    SYM, "--format", "json", "-o", p], capture_output=True, text=True, cwd=REPO)
    try:
        d = json.load(open(p))
    except Exception:
        return None, None
    finally:
        os.unlink(p)
    for s in d.get("right", {}).get("symbols", []):
        if isinstance(s, dict) and SYM in str(s.get("name", "")):
            ndiff = 0
            for r in s.get("instructions", []):
                if isinstance(r, dict) and r.get("diff_kind") not in (None, "none"):
                    ndiff += 1
            return s.get("match_percent"), ndiff
    return None, None


def main():
    objs = []
    names = sys.argv[1:]
    if names == ["--all"]:
        names = sorted(os.path.basename(os.path.dirname(x)) for x in glob.glob(f"{D}/v/*/out.o"))
    for nm in names:
        if nm.endswith(".o"):
            objs.append((nm, nm))
        else:
            objs.append((nm, f"{D}/v/{nm}/out.o"))
    rows = []
    for nm, o in objs:
        if not os.path.exists(o):
            print(f"{nm}: NO .o")
            continue
        sz = fn_size(o)
        if sz is None:
            print(f"{nm}: symbol missing")
            continue
        mp, nd = score(o)
        rows.append((nm, sz, mp, nd))
        flag = "GATE-OK" if sz == GATE else "size-bad"
        print(f"{nm:28} 0x{sz:X} {flag:8} objdiff={mp} diff_rows={nd}")
    print("\n=== ranked by official % (gate-passers first) ===")
    for r in sorted(rows, key=lambda x: (x[1] != GATE, -(x[2] or 0))):
        print(f"  {r[0]:28} 0x{r[1]:X} objdiff={r[2]} diff_rows={r[3]}")


if __name__ == "__main__":
    main()
