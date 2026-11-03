#!/opt/homebrew/bin/python3.14
"""v9: word-indexed stores via v1 (typed u32*), register keyword, indexed tail-base survival probes."""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

EXTRA_TYPES = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
"""

BODIES = {
    # word-indexed via v1 (u32*), entry0 also via v1 (indices 0..2 = folds same as stores1-3!)
    "W": """    v1 = tblb + 0x108;
    ((s32 *)v1)[0] = ((s32 *)(tblb + 0xE4))[0];
    ((s32 *)v1)[1] = ((s32 *)(tblb + 0xE4))[1];
    ((s32 *)v1)[2] = ((s32 *)(tblb + 0xE4))[2];
    ((s32 *)v1)[3] = ((s32 *)(tblb + 0xE4))[3];
    ((s32 *)v1)[4] = ((s32 *)(tblb + 0xE4))[4];
    ((s32 *)v1)[5] = ((s32 *)(tblb + 0xE4))[5];
    ((s32 *)v1)[6] = ((s32 *)(tblb + 0xE4))[6];
    ((s32 *)v1)[7] = ((s32 *)(tblb + 0xE4))[7];
    ((s32 *)v1)[8] = ((s32 *)(tblb + 0xE4))[8];
    lbl_805D6971 = 1;""",
    # entry0 via tblb literal typed, entries 1-2 word-indexed via v1
    "V": """    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
    v1 = tblb + 0x108;
    ((s32 *)v1)[3] = ((s32 *)(tblb + 0xF0))[0];
    ((s32 *)v1)[4] = ((s32 *)(tblb + 0xF0))[1];
    ((s32 *)v1)[5] = ((s32 *)(tblb + 0xF0))[2];
    ((s32 *)v1)[6] = ((s32 *)(tblb + 0xFC))[0];
    ((s32 *)v1)[7] = ((s32 *)(tblb + 0xFC))[1];
    ((s32 *)v1)[8] = ((s32 *)(tblb + 0xFC))[2];
    lbl_805D6971 = 1;""",
    # Zako: entries 1-2 typed via v1 (v1 is Ov*), loads typed literal
    "T": """    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
    v1 = (Ov_802F28E0 *)(tblb + 0x108);
    v1[1].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[1].pmf;
    v1[2].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[2].pmf;
    lbl_805D6971 = 1;""",
}

TAILS = {
    "m": ["    st = *(s32 *)((s8 *)this + 0x1C);", "    coff = st * 0xC;", "    tp = v1t + coff;"],
    "s": ["    st = *(s32 *)((s8 *)this + 0x1C);", "    tp = v1t + (st * 0xC);"],
}

PRAGS = {
    "x": "",
    "p": "#pragma opt_propagation off",
    "5": "#pragma opt_lifetimes off\n#pragma pool_data off\n#pragma opt_loop_invariants off\n#pragma opt_common_subs off\n#pragma opt_propagation off",
    "g": "#pragma peephole off",
}

def make(name):
    b, rest = name[0], name[1:]
    tk, prag = rest[0], (rest[1:].lstrip("@") or "x")
    v1decl = "    Ov_802F28E0 *v1;" if b == "T" else "    u8 *v1;"
    cast = "v1" if b != "T" else "(u8 *)v1"
    body_ = ["void TUnk_804E4B3C::run_task() {",
             "    u8 *tblb;",
             "    union StepPtuf_802F28E0 step;",
             "    u8 *tp;",
             v1decl,
             "    s32 st;",
             "    s32 coff;",
             "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
             "    update_phase_motion();",
             "    if (lbl_805D6971 == 0) {",
             re.sub(r"^    ", "        ", BODIES[b], flags=re.M),
             "    }"] + [t.replace("v1t", cast) for t in TAILS[tk]] + [
             "    step.words[0] = *(s32 *)(tp + 0);",
             "    step.words[1] = *(s32 *)(tp + 4);",
             "    step.words[2] = *(s32 *)(tp + 8);",
             "    (this->*step.fn)();",
             "    ((void (*)(void *))TObjBoss2Tunnel__sub_802F273C)(this);",
             "}"]
    fn = "\n".join(body_)
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
        path = f"{SCR}/pv9_{nm}.cpp"
        open(path, "w").write(make(nm))
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pv9_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        sz = subprocess.run(["build/binutils/powerpc-eabi-nm", "-S", f"{SCR}/pv9_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        size = re.findall(r"\b[0-9a-f]{8} ([0-9a-f]{8}) \S run_task", sz)
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pv9_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        defs = re.findall(r"addi r(\d+), r\d+, 264", od)
        stw9 = len(re.findall(r"stw r\d+,\s*(12|16|20|24|28|32)\(r9\)", od))
        c2 = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_vs_target.py",
                             f"{SCR}/pv9_{nm}.o"], capture_output=True, text=True)
        last = c2.stdout.strip().splitlines()[-1]
        print(f"{nm}: size={size} base-defs={defs} stw-r9={stw9} {last}", flush=True)
        open(f"{SCR}/d9_{nm}.txt", "w").write(c2.stdout)

main()
