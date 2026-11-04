#!/opt/homebrew/bin/python3.14
"""Minimality proof (pulsing template): patch ONLY the 2 residual displacement
words in a copy of the repo unit .o; if the fn becomes byte-identical to ORIG
and the calibrated symbol-mode oracle prints 100.0, the floor is a single tie.
Fields: stfd f0,0x18(r1) D8010018->D8010020 ; lwz r4,0x1c(r1) 8081001C->80810024
(arm-B conversion scratch: 0x18->0x20, 0x1c->0x24)."""
import json, os, re, shutil, struct, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
KIT = f"{REPO}/tools/perm-tests/f8_TObjEnePanarms_800E1774"
SYM = "TObjEnePanarms__sub_800E1774"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/enemy/TObjEnePanarms.o"
OURS_O = f"{REPO}/build/GPOE8P/src/pso/enemy/TObjEnePanarms.o"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"

def sym_off(obj):
    out = subprocess.run([GNM, "-S", obj], capture_output=True, text=True).stdout
    m = re.search(r"^([0-9a-f]{8}) ([0-9a-f]{8}) T " + SYM + r"$", out, re.M)
    return int(m.group(1), 16), int(m.group(2), 16)

def read(obj, off, n):
    b = open(obj, "rb").read()
    return b[off:off + n]

ov, osz = sym_off(OURS_O)
rv, rsz = sym_off(ORIG_O)
assert osz == rsz == 316, (osz, rsz)

# .text sh_offset: locate file offset for vaddr ov (sh_addr==0 in .o typically)
b = open(OURS_O, "rb").read()
e_shoff = struct.unpack_from(">I", b, 0x20)[0]
e_shnum = struct.unpack_from(">H", b, 0x30)[0]
e_shentsize = struct.unpack_from(">H", b, 0x2e)[0]
e_shstrndx = struct.unpack_from(">H", b, 0x32)[0]
secs = []
for i in range(e_shnum):
    off = e_shoff + i * e_shentsize
    (sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size) = struct.unpack_from(">6I", b, off)
    secs.append((sh_addr, sh_offset, sh_size))
shstr_off = secs[e_shstrndx][1]

our_off = None
for sh_addr, sh_offset, sh_size in secs:
    if sh_addr <= ov < sh_addr + sh_size and sh_size >= 0x13c:
        cand = sh_offset + (ov - sh_addr)
        if b[cand:cand + 4] == struct.pack(">I", 0x9421FFD0):
            our_off = cand
assert our_off is not None, "fn file offset not found"

orig_bytes = read(ORIG_O, rv if rv < len(open(ORIG_O,'rb').read()) else 0, 0)  # placeholder
# dtk obj: symbol value is a VA (0x800E1774); map through its section headers
bo = open(ORIG_O, "rb").read()
e_shoff_o = struct.unpack_from(">I", bo, 0x20)[0]
e_shnum_o = struct.unpack_from(">H", bo, 0x30)[0]
e_shent_o = struct.unpack_from(">H", bo, 0x2e)[0]
orig_off = None
for i in range(e_shnum_o):
    off = e_shoff_o + i * e_shent_o
    (sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size) = struct.unpack_from(">6I", bo, off)
    if sh_addr <= rv < sh_addr + sh_size:
        orig_off = sh_offset + (rv - sh_addr)
assert orig_off is not None
orig_fn = bo[orig_off:orig_off + 316]

pat = [(0x1CB0 - 0x1BA4, 0xD8010018, 0xD8010020), (0x1CB4 - 0x1BA4, 0x8081001C, 0x80810024)]
ours_fn = bytearray(b[our_off:our_off + 316])
wdiff = [k for k in range(0, 316, 4) if ours_fn[k:k+4] != orig_fn[k:k+4]]
print(f"pre-patch word-diff slots (idx, hex off, ours, orig): "
      + ", ".join(f"{k//4}@0x{k:X}:{struct.unpack('>I',bytes(ours_fn[k:k+4]))[0]:08X}/{struct.unpack('>I',orig_fn[k:k+4])[0]:08X}" for k in wdiff))

for kidx, old, new in pat:
    cur = struct.unpack(">I", bytes(ours_fn[kidx:kidx+4]))[0]
    assert cur == old, f"slot {kidx}: expected {old:08X} got {cur:08X}"
    struct.pack_into(">I", ours_fn, kidx, new)

patched = f"{KIT}/ours_patched.o"
shutil.copyfile(OURS_O, patched)
with open(patched, "r+b") as f:
    f.seek(our_off)
    f.write(bytes(ours_fn))

ident = bytes(ours_fn) == orig_fn
print(f"post-patch fn bytes vs ORIG: {'IDENTICAL (79/79 words)' if ident else 'DIFFER'}")

q = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", ORIG_O, "-2", patched,
                    SYM, "--format", "json", "-o", "-"],
                   cwd=REPO, capture_output=True, text=True)
d = json.loads(q.stdout)
for s in d.get("right", {}).get("symbols", []):
    if SYM in str(s.get("name", "")):
        rows = sum(1 for r in s.get("instructions", []) if isinstance(r, dict) and r.get("diff_kind") not in (None, "none"))
        print(f"oracle(patched) = {s.get('match_percent')}  rows={rows}  (calib: champ unpatched = 99.974686/2rows)")
