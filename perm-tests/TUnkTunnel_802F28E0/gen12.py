#!/opt/homebrew/bin/python3.14
"""v12: champion body × optimization_level / exotic pragmas."""
import re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
SCR = "/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/tunnel_802F28E0"
SRC = f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp"

FN = open(f"{SCR}/pv6_1p.cpp").read()
_rs = FN.index("void TUnk_804E4B3C::run_task() {")
_pe = FN.index("#pragma pop", _rs)
fn_body = FN[_rs:_pe].rstrip()

PRAGS = {
    "o2": "#pragma optimization_level 2",
    "o1": "#pragma optimization_level 1",
    "o3": "#pragma optimization_level 3",
    "dp": "#pragma opt_def_proc off",
    "sr": "#pragma opt_strength_reduction off",
    "o2p": "#pragma optimization_level 2\n#pragma opt_propagation off",
    "o1p": "#pragma optimization_level 1\n#pragma opt_propagation off",
    "ali": "#pragma opt_align_access_threshold 0",
    "p": "#pragma opt_propagation off",
}

def main():
    src = open(SRC).read()
    start = src.index("void TUnk_804E4B3C::run_task() {")
    end = src.index("void *TUnk_804E4B3C::destroy")
    anchor = "union StepPtuf_802F28E0 { s32 words[3]; void (TUnk_804E4B3C::*fn)(); };"
    types = """
struct Words3_802F28E0 { s32 delta; s32 delta2; void *f; };
union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };
"""
    for nm in sys.argv[1:]:
        p = PRAGS[nm]
        probe = src[:start] + f"#pragma push\n{p}\n" + fn_body + "\n#pragma pop\n" + src[end:]
        probe = probe.replace(anchor, anchor + types)
        path = f"{SCR}/pvC_{nm}.cpp"
        open(path, "w").write(probe)
        r = subprocess.run(["sh", "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh",
                            path, f"{SCR}/pvC_{nm}.o",
                            "build/GPOE8P/src/pso/boss/TObjBoss2Tunnel_802F2070.o"],
                           capture_output=True, text=True, cwd=REPO)
        if r.returncode != 0:
            print(f"{nm}: COMPILE FAIL: {(r.stderr or r.stdout)[-150:]}", flush=True)
            continue
        out = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCR}/probe_score.py", f"{SCR}/pvC_{nm}.o"],
                             capture_output=True, text=True, cwd=REPO).stdout.strip()
        od = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr",
                             "--disassemble=run_task__13TUnk_804E4B3CFv", f"{SCR}/pvC_{nm}.o"],
                            capture_output=True, text=True, cwd=REPO).stdout
        defs = re.findall(r"addi r(\d+), r\d+, 264", od)
        m = re.search(r"([\d.]+), '(\d+)'\)\]$", out)
        print(f"{nm}: score={m.groups() if m else out[-90:]} base-defs={defs}", flush=True)
        open(f"{SCR}/dC_{nm}.txt", "w").write(od)

main()
