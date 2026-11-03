#!/usr/bin/env python3
"""Row-dist audit of a specific body file: build, then print real(non-branch) diff rows + count."""
import re, subprocess, sys, os, json, shutil
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
REL = "src/pso/misc/TLobby_804050DC.cpp"
orig = open(os.path.join(REPO, REL)).read()
name, srcfile = sys.argv[1], sys.argv[2]
shutil.copyfile(srcfile, os.path.join(REPO, REL))
try:
    r = subprocess.run(["ninja", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"], cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0: print(name, "BUILD_FAIL"); sys.exit()
    d = json.loads(subprocess.run(["./build/tools/objdiff-cli", "diff", "-p", ".", "-u", "psov3/pso/misc/TLobby_804050DC", "--format", "json", "-o", "-"], cwd=REPO, capture_output=True, text=True).stdout)
    seqs = {}
    for label, key in (("O", "left"), ("N", "right")):
        for s in d[key]['symbols']:
            if '80406BD8' in str(s.get('name', '')):
                seqs[label] = [i['instruction'].get('formatted') for i in s['instructions'] if i.get('instruction')]
    o, n = seqs['O'], seqs['N']
    real = [(i, o[i], n[i]) for i in range(len(o)) if o[i] != n[i] and not (re.match(r'^b\w*\s', o[i]) and re.match(r'^b\w*\s', n[i]) and o[i].split()[0] == n[i].split()[0])]
    print(f"{name} REAL={len(real)} size_ok={len(o)==len(n)}")
    for i, fo, fn in real[:40]: print(f"  {i:3} O:{fo:32} N:{fn}")
finally:
    open(os.path.join(REPO, REL), "w").write(orig)
