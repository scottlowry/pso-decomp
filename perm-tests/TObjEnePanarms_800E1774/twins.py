import re, glob, os, subprocess
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
targets = ["TWindowSubComCard__sub_80245320", "roll_shop_weapon_grind", "fn_8034D3D0",
           "TObjBoss2CeilJunk__ct", "TObjEneSaver__ct", "vfunc_74__9TObjEnemyFl",
           "calc_stat_threshold__10TObjPlayerFPv", "update_extension__18TOTrapChainSawEdgeFv",
           "TBoss4Type1__ct", "TBoss2DeRolLe__sub_80030DFC", "TObjFish__sub_802E979C"]
for name in targets:
    # find asm block
    asm = None
    for s in glob.glob(f"{REPO}/build/GPOE8P/asm/pso/**/*.s", recursive=True):
        txt = open(s).read()
        m = re.search(r"^\.fn " + re.escape(name) + r"[^\n]*\n(.*?)^\.endfn", txt, re.S | re.M)
        if m:
            lines = []
            for l in m.group(1).splitlines():
                if '*/' in l:
                    lines.append(l.split('*/', 1)[1].strip())
                elif l.strip().endswith(':'):
                    lines.append(l.strip())
            # find stfd/lwz pairs + fctiwz context
            ctx = []
            for i, l in enumerate(lines):
                if re.match(r"stfd f\d+, 0x[0-9a-f]+\(r1\)", l):
                    ctx.append("  ...")
                    ctx.extend("  " + x for x in lines[max(0, i - 3):i + 3])
            print(f"##### {name}")
            print("\n".join(ctx))
            # locate C source function
            r = subprocess.run(["grep", "-rln", name + "(", f"{REPO}/src"], capture_output=True, text=True)
            files = [f for f in r.stdout.splitlines() if f.endswith(".cpp")]
            for f in files:
                src = open(f).read()
                mm = re.search(r"^[^\n;{}()]*" + re.escape(name) + r"\s*\([^;]*\)\s*\{", src, re.M)
                if mm:
                    print(f"  SRC {f}")
                    # print body up to 60 lines
                    body = src[mm.start():].splitlines()[:60]
                    print("\n".join("    |" + b for b in body))
                    break
            print()
