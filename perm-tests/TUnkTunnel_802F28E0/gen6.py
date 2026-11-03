#!/opt/homebrew/bin/python3.14
"""v6: dual-base shape. V1 (in-if, stores 4-9), V2 (tail, remat). propoff.
Usage: gen6.py NAME... ; NAME = flags from: p(propoff) x(none), tailv 1|2, guard 0.
"""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

EXTRA_TYPES = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
"""

BODY = """    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
    v1 = tblb + 0x108;
    ((Ov_802F28E0 *)(v1 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
    ((Ov_802F28E0 *)(v1 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
    lbl_805D6971 = 1;"""

def tail_form(k):
    if k == "1":
        return ["    v2 = tblb + 0x108;",
                "    st = *(s32 *)((s8 *)this + 0x1C);",
                "    coff = st * 0xC;",
                "    tp = v2 + coff;"]
    if k == "2":
        return ["    v2 = tblb + 0x108;",
                "    tp = v2 + ((*(s32 *)((s8 *)this + 0x1C)) * 0xC);"]
    if k == "3":
        return ["    st = *(s32 *)((s8 *)this + 0x1C);",
                "    v2 = tblb + 0x108;",
                "    coff = st * 0xC;",
                "    tp = v2 + coff;"]
    # 4: v2 after st/coff
    return ["    st = *(s32 *)((s8 *)this + 0x1C);",
            "    coff = st * 0xC;",
            "    v2 = tblb + 0x108;",
            "    tp = v2 + coff;"]

def make(name):
    tk = name[0]          # tail form
    prag = name[1:] or "x"
    PRAG = {"x": "", "p": "#pragma opt_propagation off",
            "g": "#pragma peephole off",
            "pg": "#pragma opt_propagation off\n#pragma peephole off"}
    decls = ["    u8 *tblb;", "    union StepPtuf_802F28E0 step;", "    u8 *tp;",
             "    u8 *v1;", "    u8 *v2;", "    s32 st;", "    s32 coff;"]
    body = ["void TUnk_804E4B3C::run_task() {"] + decls + [
        "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
        "    update_phase_motion();",
        "    if (lbl_805D6971 == 0) {",
        re.sub(r"^    ", "        ", BODY, flags=re.M),
        "    }",
    ] + tail_form(tk) + [
        "    step.words[0] = *(s32 *)(tp + 0);",
        "    step.words[1] = *(s32 *)(tp + 4);",
        "    step.words[2] = *(s32 *)(tp + 8);",
        "    (this->*step.fn)();",
        "    ((void (*)(void *))TObjBoss2Tunnel__sub_802F273C)(this);",
        "}",
    ]
    fn = "\n".join(body)
    src = open(SRC).read()
    start = src.index("void TUnk_804E4B3C::run_task() {")
    end = src.index("void *TUnk_804E4B3C::destroy")
    anchor = "union StepPtuf_802F28E0 { s32 words[3]; void (TUnk_804E4B3C::*fn)(); };"
    probe = src[:start] + fn + "\n" + src[end:]
    probe = probe.replace(anchor, anchor + EXTRA_TYPES)
    i = probe.index("void TUnk_804E4B3C::run_task() {")
    j = probe.index("void *TUnk_804E4B3C::destroy")
    p = PRAG[prag]
    pre = f"#pragma push\n{p}\n" if p else ""
    post = "#pragma pop\n" if p else ""
    return probe[:i] + pre + probe[i:j] + post + probe[j:]

def main():
    for nm in sys.argv[1:]:
        path = f"{SCR}/pv6_{nm}.cpp"
        open(path, "w").write(make(nm))
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pv6_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        sz = subprocess.run(["build/binutils/powerpc-eabi-nm", "-S", f"{SCR}/pv6_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        size = re.findall(r"\b[0-9a-f]{8} ([0-9a-f]{8}) \S run_task", sz)
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pv6_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        has9 = "r9" if "addi r9" in od else ("rX" if re.search(r"addi r\d+, r30, 0x108", od) else "NO")
        c2 = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_vs_target.py",
                             f"{SCR}/pv6_{nm}.o"], capture_output=True, text=True)
        last = c2.stdout.strip().splitlines()[-1]
        print(f"{nm}: size={size} p08def={has9} {last}", flush=True)
        open(f"{SCR}/d6_{nm}.txt", "w").write(c2.stdout)

main()
