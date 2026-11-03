#!/usr/bin/env python3
"""Splice a candidate EC14 (from a full-TU probe .o) into a COPY of the f3 repo unit .o,
score with official objdiff (one_shot_diff.py), restore in finally.
Usage: score_splice.py candidate.o [candidate2.o ...]
FN size gate 0x184."""
import struct, subprocess, sys, os, shutil, re

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
UNIT_O = f"{REPO}/build/GPOE8P/src/pso/unk/text_8042EAD4.o"
UNIT_ARG = "psov3/pso/unk/text_8042EAD4"
FN = "TAdTrialModemChkGC__sub_8042EC14"
FNSIZE = 0x184
SCRIPTS = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts"


def parse_elf(path):
    b = open(path, "rb").read()
    assert b[:4] == b"\x7fELF" and b[4] == 1
    endian = "<" if b[5] == 1 else ">"
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
    made = False
    if not os.path.exists(backup):
        shutil.copy2(UNIT_O, backup)
        made = True
    try:
        for cand in sys.argv[1:]:
            csyms = symtab_info(cand)
            cf = next((s for s in csyms if s[0] == FN), None)
            if cf is None:
                print(f"{os.path.basename(cand)}: SKIP no-fn"); continue
            cval, csize = cf[1], cf[2]
            if csize == 0:
                csize = next(s["size"] for s in parse_elf(cand)[2] if s["sname"] == ".text")
            if csize != FNSIZE:
                print(f"{os.path.basename(cand)}: SKIP size={csize:#x}"); continue
            cb, cendian, csecs = parse_elf(cand)
            ctext = next(s for s in csecs if s["sname"] == ".text")
            cbytes = cb[ctext["off"] + cval:ctext["off"] + cval + csize]
            _, crelas = rela_entries(cand)
            cfuncrel = [r for r in crelas if cval <= r[0] < cval + csize]
            cnames = [s[0] for s in csyms]
            crel_named = [(r[0] - cval, cnames[r[1]], r[2], r[3]) for r in cfuncrel]
            rb, rendian, rsecs = parse_elf(backup)
            rsyms = symtab_info(backup)
            rf = next(s for s in rsyms if s[0] == FN)
            rval, rsize = rf[1], rf[2]
            assert rsize == FNSIZE, f"repo func size {rsize}"
            rtext = next(s for s in rsecs if s["sname"] == ".text")
            rrela_sect, rrelas = rela_entries(backup)
            rnames = [s[0] for s in rsyms]
            rindex = {n: i for i, n in enumerate(rnames)}
            try:
                new_funcrel = [(rval + off, rindex[nm], typ, add) for off, nm, typ, add in crel_named]
            except KeyError as e:
                print(f"{os.path.basename(cand)}: SKIP missing sym {e}"); continue
            keep = [r for r in rrelas if not (rval <= r[0] < rval + rsize)]
            allrel = sorted(keep + new_funcrel, key=lambda r: r[0])
            if len(allrel) != len(rrelas):
                print(f"{os.path.basename(cand)}: SKIP reloc count {len(allrel)} vs {len(rrelas)}"); continue
            rfuncrel_named = sorted((o - rval, rnames[s], t, a) for o, s, t, a, _ in rrelas if rval <= o < rval + rsize)
            identical = rb[rtext["off"] + rval:rtext["off"] + rval + csize] == cbytes and \
                        sorted(crel_named) == rfuncrel_named
            out = bytearray(rb)
            p = rtext["off"] + rval
            out[p:p + csize] = cbytes
            for i, relrow in enumerate(allrel):
                struct.pack_into(rendian + "3I", out, rrela_sect["off"] + i * 12,
                                 relrow[0], (relrow[1] << 8) | relrow[2], relrow[3])
            open(UNIT_O, "wb").write(out)
            proc = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCRIPTS}/one_shot_diff.py",
                                   UNIT_ARG, FN], capture_output=True, text=True, cwd=REPO)
            m = re.search(r"match=([\d.]+)", proc.stdout)
            ndiff = len([l for l in proc.stdout.splitlines() if l.strip().startswith("slot")])
            tag = " BYTE-IDENTICAL-VS-REPO" if identical else ""
            print(f"{os.path.basename(cand)}: objdiff={m.group(1) if m else 'ERR'} diffslots={ndiff}{tag}")
            for l in proc.stdout.splitlines():
                if l.strip().startswith("slot"):
                    print("   ", l[:92])
    finally:
        shutil.copy2(backup, UNIT_O)
        if made:
            os.remove(backup)


main()
