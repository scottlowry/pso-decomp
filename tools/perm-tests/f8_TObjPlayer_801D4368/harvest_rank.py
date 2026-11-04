#!/usr/bin/env python3.14
"""Harvest-rank for f8 TObjPlayer__sub_801D4368: compile each output-*/source.c,
nm SIZE GATE (0x248=584) FIRST, arg-identity semantic check, then calibrated objdiff."""
import subprocess, json, sys, os, glob, tempfile

GNM = "/opt/homebrew/opt/binutils/bin/gnm"
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
D = f"{REPO}/tools/perm-tests/f8_TObjPlayer_801D4368"
TARGET = f"{D}/target.o"
SYM = "TObjPlayer__sub_801D4368"
EXPECT = 584
OBJDUMP = f"{REPO}/build/binutils/powerpc-eabi-objdump"

def fn_size(obj):
    out = subprocess.run([GNM, "-S", obj], capture_output=True, text=True).stdout
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 4 and parts[-1] == SYM and parts[2] in "tT":
            return int(parts[1], 16)
    return None

def bl_targets(obj, lo=None, hi=None):
    """multiset of callee names from R_PPC_REL24 relocs (sorted)."""
    cmd = [OBJDUMP, "-dr", obj]
    if lo:
        cmd += [f"--start-address={lo}", f"--stop-address={hi}"]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    return sorted(l.split()[-1] for l in out.splitlines() if "R_PPC_REL24" in l)

def score(obj):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", TARGET, "-2", obj,
                    SYM, "--format", "json", "-o", p], capture_output=True, text=True, cwd=REPO)
    try:
        d = json.load(open(p))
    except Exception:
        return None
    finally:
        os.unlink(p)
    for side in ("left", "right"):
        for s in d.get(side, {}).get("symbols", []):
            if isinstance(s, dict) and SYM in str(s.get("name", "")):
                mp = s.get("match_percent")
                if mp is not None:
                    return float(mp)
    return None

def main():
    champ = f"{REPO}/build/GPOE8P/src/pso/unk/text_801D40D4.o"
    champ_bl = bl_targets(champ, "0x294", "0x4dc")
    print("champ callee multiset:", champ_bl)
    results = []
    dirs = [d for d in glob.glob(f"{D}/output-*") + glob.glob(f"{D}/r*-output-*") if os.path.isdir(d)]
    for od in sorted(dirs, key=os.path.getmtime):
        srcf = os.path.join(od, "source.c")
        if not os.path.exists(srcf):
            continue
        obj = od + ".o"
        if not os.path.exists(obj) or os.path.getmtime(obj) < os.path.getmtime(srcf):
            r = subprocess.run(["bash", f"{D}/compile.sh", srcf, "-o", obj],
                               capture_output=True, text=True)
            if r.returncode != 0 or not os.path.exists(obj):
                results.append((od, "COMPILE-FAIL", None, None))
                continue
        sz = fn_size(obj)
        if sz != EXPECT:
            results.append((od, "SIZE", sz, None))
            continue
        bl = bl_targets(obj)
        if bl != champ_bl:
            results.append((od, "ARG/CALLEE-IDENTITY-FAIL", sz, None))
            continue
        sc = score(obj)
        results.append((od, "OK", sz, sc))
    ok = [r for r in results if r[1] == "OK"]
    ok.sort(key=lambda r: -(r[3] or 0))
    print(f"total={len(results)} size-fail={sum(1 for r in results if r[1]=='SIZE')} "
          f"compile-fail={sum(1 for r in results if r[1]=='COMPILE-FAIL')} "
          f"identity-fail={sum(1 for r in results if r[1]=='ARG/CALLEE-IDENTITY-FAIL')} "
          f"scored={len(ok)}")
    for r in ok[:15]:
        print(f"  {r[3]:.5f}  {os.path.basename(r[0])}")
    json.dump([{"dir": r[0], "status": r[1], "size": r[2], "score": r[3]} for r in results],
              open(f"{D}/harvest.json", "w"), indent=1)

if __name__ == "__main__":
    main()
