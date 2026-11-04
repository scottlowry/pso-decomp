#!/opt/homebrew/bin/python3.14
"""Offline probe rig for TObjEnePanarms__sub_800E1774 on fleet/f8 (zero repo builds).
Port of f3 kit probe.py. Usage: probe8.py cand1.cpp [cand2.cpp ...]
Each arg = FULL unit cpp. Compiles via wibo with unit flags, prints
fn insn-count, stfd slots, and official symbol-mode objdiff match%.
Calibration: champ copy must print size=79 match=99.974686 stfd=[0x18, 0x18].
"""
import json, os, re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
KIT = f"{REPO}/tools/perm-tests/f8_TObjEnePanarms_800E1774"
GRID = f"{KIT}/grid"
os.makedirs(GRID, exist_ok=True)
SYM = "TObjEnePanarms__sub_800E1774"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/enemy/TObjEnePanarms.o"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"
OBJDUMP = "/opt/homebrew/opt/binutils/bin/objdump"

FLAGS = ("-nodefaults -proc gekko -align powerpc -enum int -fp hardware "
         "-Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath "
         "-i build/GPOE8P/include -i include -i src -i libs/dolphin/include "
         "-i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on "
         "-O4,s -inline off -sdata2 4 -lang=c++").split()

for cpp in sys.argv[1:]:
    name = os.path.basename(cpp).replace(".cpp", "")
    obj = f"{GRID}/{name}.o"
    p = subprocess.run([f"{REPO}/build/tools/wibo", f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",
                        *FLAGS, "-c", cpp, "-o", obj],
                       cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(obj):
        print(f"{name}: COMPILE_FAIL rc={p.returncode}\n{p.stdout[:400]}\n{p.stderr[:200]}")
        continue
    nm = subprocess.run([GNM, "-S", obj], capture_output=True, text=True).stdout
    m = re.search(r"^([0-9a-f]{8}) ([0-9a-f]{8}) T " + SYM + r"$", nm, re.M)
    if not m:
        print(f"{name}: NO_SYM")
        continue
    start, fsize = int(m.group(1), 16), int(m.group(2), 16)
    d = subprocess.run([OBJDUMP, "-d", "--no-show-raw-insn", obj], capture_output=True, text=True)
    block = []
    for line in d.stdout.splitlines():
        mm = re.match(r"^\s*([0-9a-f]+):\s+(\S.*)$", line)
        if mm and start <= int(mm.group(1), 16) < start + fsize:
            block.append(mm.group(2).strip())
    stfd = [l.split()[-1] for l in block if l.startswith("stfd")]
    ninsn = fsize // 4
    q = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", ORIG_O, "-2", obj,
                        SYM, "--format", "json", "-o", "-"],
                       cwd=REPO, capture_output=True, text=True)
    pct, ndiff = "RC_FAIL", None
    if q.returncode == 0:
        try:
            d = json.loads(q.stdout)
            for s in d.get("right", {}).get("symbols", []):
                if isinstance(s, dict) and SYM in str(s.get("name", "")):
                    pct = s.get("match_percent")
                    ndiff = sum(1 for r in s.get("instructions", [])
                                if isinstance(r, dict) and r.get("diff_kind") not in (None, "none"))
        except Exception as e:
            pct = f"JSONFAIL:{e}"
    gate = "SIZEOK" if fsize == 316 else f"SIZEKILL(0x{fsize:X})"
    print(f"{name}: insn={ninsn} bytes={fsize} {gate} match={pct} rows={ndiff} stfd={stfd}")
