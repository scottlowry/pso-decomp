#!/opt/homebrew/bin/python3.14
"""Variant matrix v2 for run_task — copy/tail/pragma knobs. Compile offline, compare rows.
Usage: gen_variants2.py name1 name2 ... | (no args = all)
"""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

# PRAG: x=none, s=scheduling off, p=opt_propagation off, b=both
PRAGMAS = {
    "x": "",
    "s": "#pragma push\n#pragma scheduling off\n",
    "p": "#pragma push\n#pragma opt_propagation off\n",
    "b": "#pragma push\n#pragma scheduling off\n#pragma opt_propagation off\n",
}

W = lambda i: f"w{i}"

def copy_block(kind):
    loads_f = [f"    {W(i)} = *(s32 *)(tblb + 0x{0xE4+4*i:X});" for i in range(9)]
    if kind == "A":  # current plain
        return "\n".join(loads_f + [f"    *(s32 *)(tblb + 0x{0x108+4*i:X}) = {W(i)};" for i in range(9)]
                         + ["    lbl_805D6971 = 1;"])
    if kind == "B":  # target-order split: li early via g, dstp after w1, mixed stores
        s = [loads_f[0], "    g = 1;", loads_f[1], "    dstp = tblb + 0x108;"] + loads_f[2:]
        s += ["    *(s32 *)(tblb + 0x108) = w0;",
              "    *(s32 *)(tblb + 0x10C) = w1;",
              "    *(s32 *)(tblb + 0x110) = w2;"]
        s += [f"    *(s32 *)(dstp + 0x{4*(i-3):X}) = {W(i)};" for i in range(3, 9)]
        s += ["    lbl_805D6971 = g;"]
        return "\n".join(s)
    if kind == "C":  # Zako typed-pmf overlay copies, 3 statements
        s = ["    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;",
             "    ((Ov_802F28E0 *)(tblb + 0x108))[1].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[1].pmf;",
             "    ((Ov_802F28E0 *)(tblb + 0x108))[2].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[2].pmf;",
             "    lbl_805D6971 = 1;"]
        return "\n".join(s)
    if kind == "D":  # single 9-word struct copy
        s = ["    (*(S9_802F28E0 *)(tblb + 0x108)) = (*(S9_802F28E0 *)(tblb + 0xE4));",
             "    lbl_805D6971 = 1;"]
        return "\n".join(s)

def tail_block(kind):
    if kind == "0":
        return "    tp = tblb + 0x108 + (*(s32 *)((s8 *)this + 0x1C)) * 0xC;"
    if kind == "1":  # state first, p08 named, coff named
        return ("    s32 st = *(s32 *)((s8 *)this + 0x1C);\n"
                "    p08 = tblb + 0x108;\n"
                "    coff = st * 0xC;\n"
                "    tp = p08 + coff;")
    if kind == "2":  # p08 first
        return ("    p08 = tblb + 0x108;\n"
                "    tp = p08 + (*(s32 *)((s8 *)this + 0x1C)) * 0xC;")

EXTRA_DECLS = {
    "A": "", "0": "",
    "B": "    u8 *dstp;\n    s8 g;\n",
    "C": "",
    "D": "",
}
EXTRA_TAIL_DECLS = {"1": "    s32 st;\n    u8 *p08;\n    s32 coff;\n", "2": "    u8 *p08;\n", "0": ""}
KIND_NEEDS_T = {"C": ["Ov_802F28E0"], "D": ["S9_802F28E0"]}

EXTRA_TYPES = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
struct S9_802F28E0 { s32 w[9]; };
"""

def make_fn(copyk, tailk):
    body = ["void TUnk_804E4B3C::run_task() {"]
    body.append("    u8 *tblb;")
    body.append("    union StepPtuf_802F28E0 step;")
    body.append("    u8 *tp;")
    body.append(EXTRA_DECLS[copyk].replace("    s8 g;", "").replace("    u8 *dstp;", "").replace("    u8 *p08;", ""))
    if copyk == "B":
        body.append("    s8 g;")
        body.append("    u8 *dstp;")
    body.append(EXTRA_TAIL_DECLS[tailk])
    body += [f"    s32 w{i};" for i in range(9)]
    body += [
        "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
        "    update_phase_motion();",
        "    if (lbl_805D6971 == 0) {",
        re.sub(r"^    ", "        ", copy_block(copyk), flags=re.M),
        "    }",
        tail_block(tailk).replace("    s32 st = *(s32 *)((s8 *)this + 0x1C);",
                                  "    st = *(s32 *)((s8 *)this + 0x1C);"),
        "    step.words[0] = *(s32 *)(tp + 0);",
        "    step.words[1] = *(s32 *)(tp + 4);",
        "    step.words[2] = *(s32 *)(tp + 8);",
        "    (this->*step.fn)();",
        "    ((void (*)(void *))TObjBoss2Tunnel__sub_802F273C)(this);",
        "}",
    ]
    return "\n".join(b for b in body if b.strip())

def main():
    src = open(SRC).read()
    start = src.index("void TUnk_804E4B3C::run_task() {")
    end = src.index("void *TUnk_804E4B3C::destroy")
    # add helper types once
    anchor = "union StepPtuf_802F28E0 { s32 words[3]; void (TUnk_804E4B3C::*fn)(); };"
    names = sys.argv[1:] or [f"{p}-{c}{t}" for p in "xspb" for c in "ABCD" for t in "012"]
    for nm in names:
        p, rest = nm[0], nm[2:]
        c, t = rest[0], rest[1]
        fn = make_fn(c, t)
        probe = src[:start] + fn + "\n" + src[end:]
        # inject pragmas around the fn
        i = probe.index("void TUnk_804E4B3C::run_task() {")
        j = probe.index("void *TUnk_804E4B3C::destroy")
        probe = probe[:i] + PRAGMAS[p] + probe[i:j] + ("#pragma pop\n" if p != "x" else "") + probe[j:]
        if c in KIND_NEEDS_T:
            probe = probe.replace(anchor, anchor + EXTRA_TYPES)
        path = f"{SCR}/pv2_{nm}.cpp"
        open(path, "w").write(probe)
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pv2_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-200:]}", flush=True)
            continue
        sz = subprocess.run(["build/binutils/powerpc-eabi-nm", "-S", f"{SCR}/pv2_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        m = re.search(r"run_task__13TUnk_804E4B3CFv$|run_task\S* ", sz)
        size = re.findall(r"\b[0-9a-f]{8} ([0-9a-f]{8}) \S run_task", sz)
        c = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_vs_target.py",
                            f"{SCR}/pv2_{nm}.o"], capture_output=True, text=True)
        last = c.stdout.strip().splitlines()[-1]
        print(f"{nm}: size={size} {last}", flush=True)
        open(f"{SCR}/d2_{nm}.txt", "w").write(c.stdout)

main()
