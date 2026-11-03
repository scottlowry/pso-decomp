#!/opt/homebrew/bin/python3.14
"""Offline probe rig for TObjEnePanarms__sub_800E1774 (zero repo builds).
Usage: probe.py cand1.cpp [cand2.cpp ...]   (each is a FULL unit cpp)
Compiles via wibo with unit flags, checks .text identity of siblings,
prints stfd/lwz slots + objdiff match% for the target symbol.
Calibration: champion copy must print match=99.974686 stfd=[0x18, 0x18].
"""
import json, os, re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
KIT = f"{REPO}/perm-tests/TObjEnePanarms_800E1774"
SYM = "TObjEnePanarms__sub_800E1774"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/enemy/TObjEnePanarms.o"
REPO_O = f"{REPO}/build/GPOE8P/src/pso/enemy/TObjEnePanarms.o"

FLAGS = ("-nodefaults -proc gekko -align powerpc -enum int -fp hardware "
         "-Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath "
         "-i build/GPOE8P/include -i include -i src -i libs/dolphin/include "
         "-i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on "
         "-O4,s -inline off -sdata2 4 -lang=c++").split()

for cpp in sys.argv[1:]:
    name = os.path.basename(cpp).replace(".cpp", "")
    obj = f"{KIT}/{name}.o"
    p = subprocess.run([f"{REPO}/build/tools/wibo", f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",
                        *FLAGS, "-c", cpp, "-o", obj],
                       cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(obj):
        print(f"{name}: COMPILE_FAIL rc={p.returncode}\n{p.stdout[:600]}\n{p.stderr[:300]}")
        continue
    # objdump the function block
    d = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-d", "--no-show-raw-insn", obj],
                       capture_output=True, text=True)
    # find symbol start via nm
    nm = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", obj], capture_output=True, text=True)
    m = re.search(r"^([0-9a-f]+) T " + SYM + r"$", nm.stdout, re.M)
    if not m:
        # size form: gnm -S not needed; symbol may show with size
        m = re.search(r"^([0-9a-f]+) [0-9a-f]+ T " + SYM + r"$", nm.stdout, re.M)
    block = []
    if m:
        start = int(m.group(1), 16)
        for line in d.stdout.splitlines():
            mm = re.match(r"^\s*([0-9a-f]+):\s+(\S.*)$", line)
            if mm and start <= int(mm.group(1), 16) < start + 316:
                block.append(mm.group(2).strip())
    stfd = [l for l in block if l.startswith("stfd")]
    size = len(block)
    # objdiff official score
    q = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", ORIG_O, "-2", obj,
                        SYM, "--format", "json", "-o", "-"],
                       cwd=REPO, capture_output=True, text=True)
    pct = "RC_FAIL"
    if q.returncode == 0:
        mm = re.search(r'"match_percent":\s*([\d.]+)', q.stdout)
        if mm:
            pct = mm.group(1)
    print(f"{name}: size={size} match={pct} stfd={stfd}")
