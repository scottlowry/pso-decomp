#!/opt/homebrew/bin/python3.14
"""v8: force base-addi materialization (ZERO-DISP ADDRESS-COPY class).
Knobs: v1-origin (t=tblb expr, s=symbol expr), pragma set, tail v2 origin.
Name: <v1o><v2o>@<prag>
"""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

EXTRA_TYPES = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
"""

def body(v1o):
    base = "((u8 *)&boss2_tunnel_effect_name_table.value + 0x108)" if v1o == "s" else "(tblb + 0x108)"
    return f"""    ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
    v1 = {base};
    ((Ov_802F28E0 *)(v1 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
    ((Ov_802F28E0 *)(v1 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
    lbl_805D6971 = 1;"""

def tail(v2o):
    base = "((u8 *)&boss2_tunnel_effect_name_table.value + 0x108)" if v2o == "s" else "(tblb + 0x108)"
    return [f"    v2 = {base};",
            "    st = *(s32 *)((s8 *)this + 0x1C);",
            "    coff = st * 0xC;",
            "    tp = v2 + coff;"]

PRAGS = {
    "x": "",
    "p": "#pragma opt_propagation off",
    "pc": "#pragma opt_propagation off\n#pragma opt_common_subs off",
    "5": "#pragma opt_lifetimes off\n#pragma pool_data off\n#pragma opt_loop_invariants off\n#pragma opt_common_subs off\n#pragma opt_propagation off",
    "5g": "#pragma opt_lifetimes off\n#pragma pool_data off\n#pragma opt_loop_invariants off\n#pragma opt_common_subs off\n#pragma opt_propagation off\n#pragma peephole off",
    "5gs": "#pragma opt_lifetimes off\n#pragma pool_data off\n#pragma opt_loop_invariants off\n#pragma opt_common_subs off\n#pragma opt_propagation off\n#pragma peephole off\n#pragma scheduling off",
    "g": "#pragma peephole off",
}

def make(name):
    v1o, rest = name[0], name[1:]
    v2o = rest[0]
    prag = (rest[1:].lstrip("@") or "x")
    body_ = ["void TUnk_804E4B3C::run_task() {",
             "    u8 *tblb;",
             "    union StepPtuf_802F28E0 step;",
             "    u8 *tp;",
             "    u8 *v1;",
             "    u8 *v2;",
             "    s32 st;",
             "    s32 coff;",
             "    tblb = (u8 *)&boss2_tunnel_effect_name_table.value;",
             "    update_phase_motion();",
             "    if (lbl_805D6971 == 0) {",
             re.sub(r"^    ", "        ", body(v1o), flags=re.M),
             "    }"] + tail(v2o) + [
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
        path = f"{SCR}/pv8_{nm}.cpp"
        open(path, "w").write(make(nm))
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pv8_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        sz = subprocess.run(["build/binutils/powerpc-eabi-nm", "-S", f"{SCR}/pv8_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        size = re.findall(r"\b[0-9a-f]{8} ([0-9a-f]{8}) \S run_task", sz)
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pv8_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        defs = re.findall(r"addi r(\d+), r\d+, 264", od)
        c2 = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_vs_target.py",
                             f"{SCR}/pv8_{nm}.o"], capture_output=True, text=True)
        last = c2.stdout.strip().splitlines()[-1]
        print(f"{nm}: size={size} base-defs={defs} {last}", flush=True)
        open(f"{SCR}/d8_{nm}.txt", "w").write(c2.stdout)

main()
