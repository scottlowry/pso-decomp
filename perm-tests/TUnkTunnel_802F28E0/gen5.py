#!/opt/homebrew/bin/python3.14
"""v5: M-shape — p08 shared value (def in if, uses in entry1/2 stores + tail). Guard spellings + bool pragma.
Usage: gen5.py NAME... where NAME = <guard><pragmaflag> e.g. M1 M2 M3 xM...
Simpler: pass names from a dict.
"""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

GUARD = {
    "1": "if (lbl_805D6971 == 0) {{\n{BODY}\n    }}",
    "2": "if (!lbl_805D6971) {{\n{BODY}\n    }}",
    "3": "if ((s32) lbl_805D6971 == 0) {{\n{BODY}\n    }}",
}

BODY_M = """    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
    p08 = tblb + 0x108;
    ((Ov_802F28E0 *)(p08 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
    ((Ov_802F28E0 *)(p08 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
    lbl_805D6971 = 1;"""
# NOTE (p08+0xC)[0] = +C entries 1.. ; (p08+0x18)[0] = entry2 ✓

TAIL_M = """    st = *(s32 *)((s8 *)this + 0x1C);
    coff = st * 0xC;
    tp = p08 + coff;"""

EXTRA_TYPES = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
"""

def make(name):
    g = name[0]
    prag = name[1:]
    PRAG = {
        "x": "", "g": "#pragma peephole off", "b": "#pragma bool off",
        "gb": "#pragma peephole off\n#pragma bool off", "bg": "#pragma bool off\n#pragma peephole off",
        "c": "#pragma opt_common_subs off",
    }
    body = ["void TUnk_804E4B3C::run_task() {",
            "    u8 *tblb;",
            "    union StepPtuf_802F28E0 step;",
            "    u8 *tp;",
            "    u8 *p08;",
            "    s32 st;",
            "    s32 coff;",
            "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
            "    update_phase_motion();",
            GUARD[g].format(BODY=re.sub(r"^    ", "        ", BODY_M, flags=re.M)),
            TAIL_M,
            "    step.words[0] = *(s32 *)(tp + 0);",
            "    step.words[1] = *(s32 *)(tp + 4);",
            "    step.words[2] = *(s32 *)(tp + 8);",
            "    (this->*step.fn)();",
            "    ((void (*)(void *))TObjBoss2Tunnel__sub_802F273C)(this);",
            "}"]
    fn = "\n".join(body)
    src = open(SRC).read()
    start = src.index("void TUnk_804E4B3C::run_task() {")
    end = src.index("void *TUnk_804E4B3C::destroy")
    anchor = "union StepPtuf_802F28E0 { s32 words[3]; void (TUnk_804E4B3C::*fn)(); };"
    probe = src[:start] + fn + "\n" + src[end:]
    probe = probe.replace(anchor, anchor + EXTRA_TYPES)
    i = probe.index("void TUnk_804E4B3C::run_task() {")
    j = probe.index("void *TUnk_804E4B3C::destroy")
    pre = f"#pragma push\n{PRAG[prag]}\n" if PRAG.get(prag) else ""
    post = "#pragma pop\n" if PRAG.get(prag) else ""
    probe = probe[:i] + pre + probe[i:j] + post + probe[j:]
    return probe

def main():
    for nm in sys.argv[1:]:
        path = f"{SCR}/pv5_{nm}.cpp"
        open(path, "w").write(make(nm))
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pv5_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        sz = subprocess.run(["build/binutils/powerpc-eabi-nm", "-S", f"{SCR}/pv5_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        size = re.findall(r"\b[0-9a-f]{8} ([0-9a-f]{8}) \S run_task", sz)
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pv5_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        has9 = "yes" if "addi r9" in od else "NO"
        c2 = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_vs_target.py",
                             f"{SCR}/pv5_{nm}.o"], capture_output=True, text=True)
        last = c2.stdout.strip().splitlines()[-1]
        print(f"{nm}: size={size} r9={has9} {last}", flush=True)
        open(f"{SCR}/d5_{nm}.txt", "w").write(c2.stdout)

main()
