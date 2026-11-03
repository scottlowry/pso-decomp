#!/opt/homebrew/bin/python3.14
"""Splice a candidate function (from kit-compiled .o) into a copy of the repo unit .o,
score with objdiff-cli (one_shot_diff), then restore. Only 316B candidates.
Usage: score_splice.py candidate.o [candidate2.o ...]
"""
import struct, subprocess, sys, os, shutil, re

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
UNIT_O = f"{REPO}/build/GPOE8P/src/pso/enemy/TObjEnePanarms.o"
FN = "TObjEnePanarms__sub_800E1774"
SCRIPTS = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts"

def parse_elf(path):
    b = open(path, "rb").read()
    assert b[:4] == b"\x7fELF" and b[4] == 1  # 32-bit
    endian = "<" if b[5] == 1 else ">"
    # ELF32: e_shoff 0x20, e_shentsize 0x2e, e_shstrndx 0x30
    e_shoff = struct.unpack_from(endian + "I", b, 0x20)[0]
    e_shnum = struct.unpack_from(endian + "H", b, 0x30)[0]
    e_shentsize = struct.unpack_from(endian + "H", b, 0x2e)[0]
    e_shstrndx = struct.unpack_from(endian + "H", b, 0x32)[0]
    secs = []
    for i in range(e_shnum):
        off = e_shoff + i * e_shentsize
        if off + 40 > len(b):
            break
        (sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size,
         sh_link, sh_info, sh_addralign, sh_entsize) = struct.unpack_from(endian + "10I", b, off)
        secs.append(dict(name=sh_name, type=sh_type, off=sh_offset, size=sh_size,
                         link=sh_link, entsize=sh_entsize))
    shstr_off = secs[e_shstrndx]["off"]
    for s in secs:
        s["sname"] = b[shstr_off + s["name"]:b.index(b"\0", shstr_off + s["name"])].decode()
    return b, endian, secs

def symtab_info(path):
    b, endian, secs = parse_elf(path)
    st = next(s for s in secs if s["sname"] == ".symtab")
    strb = secs[st["link"]]
    syms = []
    for i in range(st["size"] // 16):
        name, value, size, info, other, shndx = struct.unpack_from(endian + "3IBBh", b, st["off"] + i * 16)
        nm = b[strb["off"] + name:b.index(b"\0", strb["off"] + name)].decode()
        syms.append((nm, value, size, shndx))
    return syms

def rela_entries(path):
    b, endian, secs = parse_elf(path)
    rt = next(s for s in secs if s["sname"] == ".rela.text")
    out = []
    for i in range(rt["size"] // 12):
        r_off, r_info, r_add = struct.unpack_from(endian + "3I", b, rt["off"] + i * 12)
        out.append((r_off, r_info >> 8, r_info & 0xff, r_add, i))
    return rt, out

def main():
    backup = UNIT_O + ".f3bak"
    if not os.path.exists(backup):
        shutil.copy2(UNIT_O, backup)
    try:
        for cand in sys.argv[1:]:
            # candidate function loc
            csyms = symtab_info(cand)
            cf = next(s for s in csyms if s[0] == FN)
            cval, csize = cf[1], cf[2]
            if csize == 0:
                csize = ctext_size = next(s["size"] for s in parse_elf(cand)[2] if s["sname"] == ".text")
            if csize != 0x13C:
                print(f"{cand}: SKIP size={csize}")
                continue
            cb, cendian, csecs = parse_elf(cand)
            ctext = next(s for s in csecs if s["sname"] == ".text")
            cbytes = cb[ctext["off"] + cval:ctext["off"] + cval + csize]
            crela_sect, crelas = rela_entries(cand)
            cfuncrel = [r for r in crelas if cval <= r[0] < cval + csize]
            # map candidate reloc symbol indices -> names
            cnames = [s[0] for s in csyms]
            crel_named = [(r[0] - cval, cnames[r[1]], r[2], r[3]) for r in cfuncrel]
            # repo
            rb, rendian, rsecs = parse_elf(backup)
            rsyms = symtab_info(backup)
            rf = next(s for s in rsyms if s[0] == FN)
            rval, rsize = rf[1], rf[2]
            assert rsize == 0x13C, f"repo func size {rsize}"
            rtext = next(s for s in rsecs if s["sname"] == ".text")
            rrela_sect, rrelas = rela_entries(backup)
            rnames = [s[0] for s in rsyms]
            rindex = {n: i for i, n in enumerate(rnames)}
            new_funcrel = []
            for off, nm, typ, add in crel_named:
                assert nm in rindex, f"missing sym {nm}"
                new_funcrel.append((rval + off, rindex[nm], typ, add))
            # rebuild rela.text: drop old func-range, insert new (keep global order sorted by offset)
            keep = [r for r in rrelas if not (rval <= r[0] < rval + rsize)]
            allrel = sorted(keep + new_funcrel, key=lambda r: r[0])
            assert len(allrel) == len(rrelas), f"reloc count {len(allrel)} vs {len(rrelas)} — skip"
            out = bytearray(rb)
            # patch .text bytes
            p = rtext["off"] + rval
            out[p:p + csize] = cbytes
            # patch rela.text in place (same count)
            for i, relrow in enumerate(allrel):
                r_off, sym, typ, add = relrow[0], relrow[1], relrow[2], relrow[3]
                struct.pack_into(rendian + "3I", out, rrela_sect["off"] + i * 12, r_off, (sym << 8) | typ, add)
            open(UNIT_O, "wb").write(out)
            proc = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCRIPTS}/one_shot_diff.py",
                                   "psov3/pso/enemy/TObjEnePanarms", FN],
                                  capture_output=True, text=True, cwd=REPO)
            m = re.search(r"match=([\d.]+)", proc.stdout)
            rows = re.search(r"rows: orig (\d+) ours (\d+)", proc.stdout)
            ndiff = len([l for l in proc.stdout.splitlines() if l.strip().startswith("slot")])
            print(f"{cand}: objdiff={m.group(1) if m else 'ERR'} rows={rows.groups() if rows else '?'} diffslots={ndiff}")
            for l in proc.stdout.splitlines():
                if l.strip().startswith("slot"):
                    print("   ", l[:88])
    finally:
        shutil.copy2(backup, UNIT_O)
        os.remove(backup)

main()
