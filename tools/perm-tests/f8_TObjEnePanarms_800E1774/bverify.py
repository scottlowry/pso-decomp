#!/opt/homebrew/bin/python3.14
"""Non-vacuous BASE-VERIFY: word-compare fn bytes of base_direct.o (kit compile)
vs the repo-built unit .o. Fails loudly on empty extraction."""
import re, struct, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
KIT = f"{REPO}/tools/perm-tests/f8_TObjEnePanarms_800E1774"
SYM = "TObjEnePanarms__sub_800E1774"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"

def fn_bytes(obj):
    out = subprocess.run([GNM, "-S", obj], capture_output=True, text=True).stdout
    m = re.search(r"^([0-9a-f]{8}) ([0-9a-f]{8}) T " + SYM + r"$", out, re.M)
    if not m:
        sys.exit(f"NO_SYM in {obj}:\n{out[:300]}")
    val, size = int(m.group(1), 16), int(m.group(2), 16)
    b = open(obj, "rb").read()
    e_shoff = struct.unpack_from(">I", b, 0x20)[0]
    e_shnum = struct.unpack_from(">H", b, 0x30)[0]
    e_shentsize = struct.unpack_from(">H", b, 0x2e)[0]
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        (_, _, _, sh_addr, sh_offset, sh_size, _) = struct.unpack_from(">7I", b, off)
        if sh_addr <= val < sh_addr + sh_size and sh_size >= size:
            return b[sh_offset + (val - sh_addr): sh_offset + (val - sh_addr) + size]
    sys.exit(f"NO_SECTION in {obj}")

base = fn_bytes(f"{KIT}/base_direct.o")
repo = fn_bytes(f"{REPO}/build/GPOE8P/src/pso/enemy/TObjEnePanarms.o")
assert len(base) == len(repo) == 316, (len(base), len(repo))
diffs = [k // 4 for k in range(0, 316, 4) if base[k:k + 4] != repo[k:k + 4]]
print(f"base=316B repo=316B word-diff={len(diffs)} slots={diffs[:8]}")
sys.exit(0 if not diffs else 1)
