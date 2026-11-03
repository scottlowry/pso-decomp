#!/usr/bin/env python3
"""4+ version rosetta at the unit's exact flags: does ANY installed MWCC emit
era's in-place 'addi rX,rX,0xe' + dest-addr merge for the case-2 chain?"""
import re, subprocess, os, sys
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
NINJA_CMD = subprocess.run(["ninja","-t","commands","build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],cwd=REPO,capture_output=True,text=True).stdout.strip().splitlines()[-1]
base = NINJA_CMD.split(" -MMD")[0]
f2 = open("/tmp/cand_F2_rowadd_plain.cpp").read()
g1 = open("/tmp/cand_G1_off_hoist.cpp").read() if os.path.exists("/tmp/cand_G1_off_hoist.cpp") else None

PRE = """#include "types.h"
struct Seg_80406BD8 { s16 len; u16 f2; u32 word; u8 kind; u8 pad[2]; };
struct BufPool_80406BD8 { s16 count; s16 size; void *rows; };
extern RecoveredGlobal_80415650_lbl_805C1BF8 network_buffer_pool_state;
u16 TUdpSocket__sub_80419864(void *buf, s16 len);

"""
def extract(src):
    FN = "u16 TLobby__sub_80406BD8(void *arg0, s16 arg1) {"
    i = src.index(FN); e = src.index("\n}\n", i)+3
    return src[i:e]
import shutil
def probe_file(tag, src):
    # need the global struct type: copy the full TU instead (simplest = compile real file with version swap)
    path = f"/tmp/rosetta_{tag}.cpp"
    open(path,"w").write(src)
    return path

os.makedirs("/tmp/rosetta6bd8", exist_ok=True)
versions = ["1.2.5n","1.3.2","2.0p1","2.6","2.7","2.5","1.3","1.0","1.1p1","1.2.5","3.0a5"]
ERA = re.compile(r"addi\s+(r\d+),\s*\1,\s*0xe")
for tag, src in (("F2", f2), ("G1", g1)):
    if src is None: continue
    pf = probe_file(tag, src)
    for v in versions:
        cmd = re.sub(r"compilers/GC/\S+/", f"compilers/GC/{v}/", base)
        ouf = f"/tmp/rosetta6bd8/{tag}_{v}.o"
        r = subprocess.run(cmd + f" -c {pf} -o {ouf}", cwd=REPO, shell=True, capture_output=True, text=True)
        if r.returncode: print(f"{tag} {v} COMPILE_FAIL {r.stderr[:120]}"); continue
        d = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump","-d",ouf],capture_output=True,text=True)
        txt = d.stdout
        has_inplace = bool(ERA.search(txt))
        has_fold = bool(re.search(r"lhz\s+r\d+,\s*0xe\(", txt))
        sz = re.search(r"TLobby__sub_80406BD8[>:]", txt)
        # function size: count insns
        blk = re.search(r"<TLobby__sub_80406BD8>:\n(.*?)(?:\n\n|$)", txt, re.S)
        n = len(re.findall(r"\n\s+[0-9a-f]+:", blk.group(1))) if blk else 0
        print(f"{tag} {v:8} rows~{n:3} inplace_addi_0xe={has_inplace} lhz_disp_fold={has_fold}")
