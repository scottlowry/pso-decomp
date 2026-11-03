import subprocess, re, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K = f"{REPO}/perm-tests/TObjEnePanarms_800E1774"
SYM = "TObjEnePanarms__sub_800E1774"
BASE_FLAGS = ("-nodefaults -proc gekko -align powerpc -enum int -fp hardware "
    "-Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath "
    "-i build/GPOE8P/include -i include -i src -i libs/dolphin/include "
    "-i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on "
    "-sdata2 4 -lang=c++").split()

def words(obj):
    nm = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", obj], capture_output=True, text=True).stdout
    m = re.search(r"^([0-9a-f]+) [0-9a-f]+ T " + SYM + "$", nm, re.M) or \
        re.search(r"^([0-9a-f]+) T " + SYM + "$", nm, re.M)
    if not m: return None
    start = int(m.group(1), 16)
    d = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-d", "--no-show-raw-insn", obj],
                       capture_output=True, text=True).stdout
    out = []
    for line in d.splitlines():
        mm = re.match(r"^\s*([0-9a-f]+):\s+(\S.*)$", line)
        if mm and start <= int(mm.group(1), 16) < start + 316:
            out.append(mm.group(2).strip())
    return out

champ = words(f"{REPO}/build/GPOE8P/src/pso/enemy/TObjEnePanarms.o")
orig = [l for l in subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-d", "--no-show-raw-insn",
        f"{K}/target.o"], capture_output=True, text=True).stdout.splitlines()
        if re.match(r"^\s*[0-9a-f]+:\s+\S", l)]
orig = [l.split("\t")[-1].replace(" ", "").strip() for l in orig]

FLAGS_SETS = {
    "O4s":      ["-O4,s"],
    "O4":       ["-O4"],
    "O3":       ["-O3"],
    "O4s_nocse_opt":["-O4,s", "-opt,cse=off"],
    "O4s_peepoff":   ["-O4,s", "-opt,peep=off"],
    "O4s_p":    ["-O4,p"],
    "O4s_csecomma":   ["-O4,s", "-opt,commonsubs=off"],
}
for tag, extra in FLAGS_SETS.items():
    obj = f"{K}/flag_{tag}.o"
    p = subprocess.run([f"{REPO}/build/tools/wibo", f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",
                        *BASE_FLAGS, *extra, "-c", f"{K}/c0_champ.cpp", "-o", obj],
                       cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(obj):
        err = [l for l in p.stdout.splitlines() if "Error" in l][:2]
        print(f"{tag}: FAIL {err}")
        continue
    w = words(obj)
    if w is None:
        print(f"{tag}: NO-SYM (size {os.path.getsize(obj)})"); continue
    dif_champ = sum(1 for a, b in zip(champ, w) if a != b) if len(w) == len(champ) else -1
    dif_orig  = sum(1 for a, b in zip(orig, w) if a.replace(" ","") != b.replace(" ","")) if len(w) == len(orig) else -1
    stfd = [l for l in w if l.startswith("stfd")]
    print(f"{tag}: ins={len(w)} dif_vs_champ={dif_champ} dif_vs_orig={dif_orig} stfd={stfd}")
