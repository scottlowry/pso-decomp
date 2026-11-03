#!/usr/bin/env python3.14
"""Hand order-grid scanner: fingerprint every gen_*.o battery artifact against
the TARGET loop rows (words 39,40,44,45 = mulli inplace r7 / add r7,r0,r7 /
lbzx r0 / cmplwi r0) and score vs target.o. Zero repo builds. Prints table +
control (repo champ raw) so promotion threshold is calibrated to 99.677-era.
"""
import glob, os, re, subprocess, sys, json, tempfile

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
TARGET = f"{KIT}/target.o"
REPO_OBJ = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/GPOE8P/src/pso/misc/TLobby_80428374.o"

def words(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)", l)
        if not m:
            if out and not l.strip().startswith(("R_PPC", "0")) and "<" not in l:
                continue
            if out and "<" in l and not l[0].isspace():
                break
            if out:
                break
            continue
        out.append(m.group(1).replace(" ", "").rstrip())
    return out

def size_of(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

def raw(obj):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run(["/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/tools/objdiff-cli",
                    "diff", "-1", TARGET, "-2", obj, SYM, "--format", "json", "-o", p],
                   capture_output=True, text=True,
                   cwd="/Users/scott/Hermes/pso-decomp/pso-decomp-f3")
    try:
        d = json.load(open(p))
        for side in ("left", "right"):
            for s in d.get(side, {}).get("symbols", []):
                if isinstance(s, dict) and SYM in str(s.get("name", "")) and s.get("match_percent") is not None:
                    return float(s["match_percent"])
    except Exception:
        return None
    finally:
        os.unlink(p)
    return None

TW = words(TARGET)
control = words(REPO_OBJ)
ctrl_bad = sorted({k for k in range(62) if TW[k] != control[k]})
print(f"TARGET words={len(TW)} control(repo champ) bad words vs target: {ctrl_bad}")
print(f"control raw kit score: {raw(REPO_OBJ)}  size={size_of(REPO_OBJ)}")

rows = []
for o in sorted(glob.glob(f"{KIT}/gen_*.o")):
    name = os.path.basename(o)[:-2]
    sz = size_of(o)
    w = words(o)
    if len(w) != len(TW):
        rows.append((name, sz, None, f"WORDCNT-{len(w)}", None)); continue
    bad = sorted({k for k in range(len(TW)) if TW[k] != w[k]})
    loop_bad = [k for k in bad if k in (39, 40, 44, 45)]
    sc = raw(o) if sz == 248 else None
    rows.append((name, sz, sc, len(bad), loop_bad))

rows.sort(key=lambda r: (r[3] if isinstance(r[3], int) else 99, -(r[2] or 0)))
print(f"{'variant':24} {'sz':5} {'raw':10} {'badw':5} loop-bad(39/40/44/45)")
for name, sz, sc, bad, lb in rows:
    print(f"{name:24} {str(sz):5} {(('%.5f'%sc) if sc else '-'):10} {str(bad):5} {lb}")
