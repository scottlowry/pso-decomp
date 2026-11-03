#!/opt/homebrew/bin/python3.14
"""Compare a probe .o's run_task disasm (objdump -dr, normalized) vs target_rows.txt.
Usage: probe_vs_target.py <probe.o> [rowsfile]
"""
import re, subprocess, sys

FN = "run_task__13TUnk_804E4B3CFv"
OD = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/binutils/powerpc-eabi-objdump"
ROWS = sys.argv[2] if len(sys.argv) > 2 else "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0/target_rows.txt"

def norm_ops(s):
    # decimal (possibly negative) standalone numbers -> lowercase hex 0x form
    def rep(m):
        v = int(m.group(0))
        return ("-0x%x" % -v) if v < 0 else ("0x%x" % v)
    return re.sub(r"(?<![0-9A-Za-z_.])-?\d+(?![0-9A-Za-z_.])", rep, s)

def norm(x):
    x = re.sub(r"\s+", " ", x).strip()
    m = re.match(r"([A-Za-z][\w.]*) (.*)$", x)  # split mnemonic from operands (objdump pads with space or none)
    if m and " " not in m.group(2) and not m.group(2).startswith("<"):
        mn, ops = m.group(1), m.group(2)
    else:
        mn, ops = (m.group(1), m.group(2)) if m else (x, "")
    # unambiguous: split on first space
    sp = x.split(" ", 1)
    if len(sp) == 1:
        mn, ops = sp[0], ""
    # objdump "lwz r12,0xe4(r30)" style: mnemonic then space then comma-glued ops
    x = ops.replace(",", ", ")
    x = f"{mn} {x}".strip()
    # bl with symbol in angle brackets (+ optional reloc-appended name — prefer reloc name)
    x = re.sub(r"bl.*<[^>]*> (\S+)$", r"bl \1", x)
    x = re.sub(r"bl.*<((?:[A-Za-z_][\w.]*)?)(?:\+[0-9a-fx]+)>$", r"bl \1", x)
    x = re.sub(r"bl 0x?[0-9a-f]+ (\S+)$", r"bl \1", x)
    # branches: strip target
    x = re.sub(r"\b(bne|beq|blt|bgt|bge|ble|b) \S.*", lambda m: m.group(1), x)
    # sda-style lbz/stb with reloc name appended after base form
    x = re.sub(r"(l[wb]z|st[wb]) (\w+), \S*\(\S*\) (\S+)$", r"\1 \2 \3", x)
    x = re.sub(r"(l[wb]z|st[wb]) (\w+), \w+@sda21\(r13\)(?: (\S+))?$", r"\1 \2 \3", x)
    # lis r4, 32846 sym
    x = re.sub(r"(lis \w+), \d+ (\S+)", r"\1 \2", x)
    # addi r30, r4, 18808 sym   (reloc-appended symbol)
    x = re.sub(r"addi (\w+), (\w+), -?\d+ (\S+)$", r"addi \1, \2 \3", x)
    x = norm_ops(x)
    x = x.lower()
    # normalize sym offsets: sym+0x8 -> sym
    x = re.sub(r"(\w)\+0x[0-9a-f]+", r"\1", x)
    return x

def rows(obj_path):
    out = subprocess.run([OD, "-dr", "--disassemble=" + FN, obj_path],
                         capture_output=True, text=True).stdout
    lines = out.splitlines()
    result = []
    pending = None
    for l in lines:
        m = re.match(r"\s+[0-9a-f]+:\s+(?:[0-9a-f]{2} )+\s*(.*)$", l)
        if m:
            if pending is not None:
                result.append(pending)
            pending = m.group(1)
            continue
        r = re.match(r"\s+[0-9a-f]+:\s+R_PPC_\w+\s+(\S+)", l)
        if r and pending is not None:
            pending = pending + " " + r.group(1)
            continue
    if pending is not None:
        result.append(pending)
    return [norm(x) for x in result]

tgt = [norm(l) for l in open(ROWS) if l.strip()]
got = rows(sys.argv[1])
n = max(len(tgt), len(got))
bad = 0
for i in range(n):
    t = tgt[i] if i < len(tgt) else "<missing>"
    g = got[i] if i < len(got) else "<missing>"
    t = re.sub(r"\s+", " ", t)
    if t != g:
        bad += 1
        print(f"slot {i:2} O: {t:46} N: {g}")
print(f"--- {len(got)}/{len(tgt)} rows, diffs={bad}")
