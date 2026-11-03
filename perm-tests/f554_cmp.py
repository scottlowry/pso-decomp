#!/usr/bin/env python3
# Compare OURS vs era PPC .o .text disassembly line-by-line, folding relocations into operands.
import subprocess, sys, re
OD = "/opt/homebrew/opt/binutils/bin/objdump"

def dis(obj, sym):
    out = subprocess.run([OD, "-dr", obj], capture_output=True, text=True).stdout
    ins = []
    inside = False
    for ln in out.splitlines():
        if f"<{sym}>:" in ln:
            inside = True
            continue
        if not inside:
            continue
        m = re.match(r"^\s+[0-9a-f]+:\t([0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2} [0-9a-f]{2})\s*\t(\S+)\s+(.*)$", ln)
        if m:
            ins.append([m.group(2), m.group(3).strip(), None])
            continue
        r = re.match(r"^\t+\w+: R_PPC\S*\t(\S+)", ln)
        if r and ins:
            ins[-1][2] = r.group(1)
        elif re.match(r"^\S", ln) and ins:
            break
    rows = []
    for op, args, rel in ins:
        if rel:
            if op in ("lis", "addi"):
                args = re.sub(r",0\s*$", "," + rel, args)
            elif op in ("bl", "b"):
                args = rel
            else:
                args = re.sub(r"^0\(", rel + "(", args)
                args = re.sub(r"0\(0\)", rel, args)
        args = re.sub(r"\s+", " ", args)
        args = re.sub(r"\s+0x[0-9a-f]+ <.*$", "", args)  # branch target offsets
        args = re.sub(r"^\d+(?:\.\d+)? <.*$", "TGT", args)
        rows.append(op + " " + args)
    return rows

era = dis("build/GPOE8P/obj/pso/unk/text_8009F554.o", "fn_8009F554")
oursym = sys.argv[2] if len(sys.argv) > 2 else "load_resources__17TObjEneMe1CanadinFv"
ours = dis(sys.argv[1] if len(sys.argv) > 1 else "build/GPOE8P/src/pso/unk/text_8009F554.o", oursym)
n = max(len(era), len(ours))
bad = 0
for i in range(n):
    e = era[i] if i < len(era) else "--"
    o = ours[i] if i < len(ours) else "--"
    if e != o:
        bad += 1
        print(f"{i:3d} E| {e:<50} O| {o}")
print(f"era={len(era)} ours={len(ours)} diffrows={bad}")
