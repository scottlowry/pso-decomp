#!/opt/homebrew/bin/python3.14
"""v11: register-keyword pinned v1 (M-shape family). Names: K<tail>@<prag>
K: v1 register-pinned; tail a=v1+coff(named), b=v1+(st*0xC) inline.
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

TAIL = {
    "a": ["    st = *(s32 *)((s8 *)this + 0x1C);", "    coff = st * 0xC;", "    tp = v1 + coff;"],
    "b": ["    st = *(s32 *)((s8 *)this + 0x1C);", "    tp = v1 + (st * 0xC);"],
}
PRAGS = {"x": "", "p": "#pragma opt_propagation off", "d": "#pragma opt_dead_code off",
         "pd": "#pragma opt_propagation off\n#pragma opt_dead_code off"}

def make(name):
    parts = name.split("@")
    tk = parts[0][1]
    prag = parts[1] if len(parts) > 1 else "x"
    regkw = "register " if parts[0][0] == "R" else ""
    stmts = [f"void TUnk_804E4B3C::run_task() {{",
             "    u8 *tblb;",
             "    union StepPtuf_802F28E0 step;",
             "    u8 *tp;",
             f"    {regkw}u8 *v1;",
             "    s32 st;",
             "    s32 coff;",
             "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
             "    update_phase_motion();",
             "    if (lbl_805D6971 == 0) {",
             re.sub(r"^    ", "        ", BODY, flags=re.M),
             "    }"] + TAIL[tk] + [
             "    step.words[0] = *(s32 *)(tp + 0);",
             "    step.words[1] = *(s32 *)(tp + 4);",
             "    step.words[2] = *(s32 *)(tp + 8);",
             "    (this->*step.fn)();",
             "    ((void (*)(void *))TObjBoss2Tunnel__sub_802F273C)(this);",
             "}"]
    fn = "\n".join(stmts)
    src = open(SRC).read()
    start = src.index("void TUnk_804E4B3C::run_task() {")
    end = src.index("void *TUnk_804E4B3C::destroy")
    anchor = "union StepPtuf_802F28E0 { s32 words[3]; void (TUnk_804E4B3C::*fn)(); };"
    probe = src[:start] + fn + "\n" + src[end:]
    probe = probe.replace(anchor, anchor + EXTRA_TYPES)
    i = probe.index("void TUnk_804E4B3C::run_task() {")
    j = probe.index("void *TUnk_804E4B3C::destroy")
    p = PRAGS[prag]
    pre = f"#pragma push\n{p}\n" if p else ""
    post = "#pragma pop\n" if p else ""
    return probe[:i] + pre + probe[i:j] + post + probe[j:]

def main():
    for nm in sys.argv[1:]:
        path = f"{SCR}/pvB_{nm}.cpp"
        open(path, "w").write(make(nm))
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pvB_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        out = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_score.py", f"{SCR}/pvB_{nm}.o"],
                             capture_output=True, text=True, cwd=REPO).stdout.strip()
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pvB_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        defs = re.findall(r"addi r(\d+), r\d+, 264", od)
        stwr9 = len(re.findall(r"stw r\d+,\s*0x[0-9a-f]+\(r9\)", od))
        m = re.search(r"([\d.]+), '(\d+)'\)\]$", out)
        print(f"{nm}: score={m.groups() if m else out[-90:]} base-defs={defs} stw-r9={stwr9}", flush=True)
        open(f"{SCR}/dB_{nm}.txt", "w").write(od)

main()
