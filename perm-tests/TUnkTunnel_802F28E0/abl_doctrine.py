#!/opt/homebrew/bin/python3.14
"""Declaration-doctrine ablation battery for run_task__13TUnk_804E4B3CFv.
Edits HEAD src copy (body + extern decls), offline MWCC probe compile, score.
"""
import json, os, re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
KIT = f"{REPO}/perm-tests/TUnkTunnel_802F28E0"
SRC = open(f"{REPO}/src/pso/boss/TObjBoss2Tunnel_802F2070.cpp").read()
CMD = open("/tmp/tu_cmd_f3.txt").read().strip()

GUARD_CHAMP = """    if (lbl_805D6971 == 0) {
        ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        v1 = tblb + 0x108;
        ((Ov_802F28E0 *)(v1 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
        ((Ov_802F28E0 *)(v1 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
        lbl_805D6971 = 1;
    }
"""

DECLS = "union Ov_802F28E0 { Words3_802F28E0 w; void (TUnk_804E4B3C::*pmf)(); };"  # anchor

def mk(guard, extra_decls="", decl_edits=(), name=""):
    s = SRC
    assert GUARD_CHAMP in s, "guard anchor missing"
    s = s.replace(GUARD_CHAMP, guard)
    s = s.replace(DECLS, DECLS + "\n" + extra_decls)
    for old, new in decl_edits:
        assert old in s, f"{name}: decl anchor missing: {old[:40]}"
        s = s.replace(old, new)
    return s

# fresh-typed window macros (C++ in-file; keep extern C decls intact by using casts)
OVC = "((Ov_802F28E0 *)({b}))[{i}].pmf"

V = {}
# A1: volatile guard extern
V["A1_volguard"] = mk(GUARD_CHAMP, decl_edits=[("extern s8 lbl_805D6971;", "extern volatile s8 lbl_805D6971;")])
# A2: volatile pointee for copies 2&3
V["A2_voldst23"] = mk("""    if (lbl_805D6971 == 0) {
        ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        v1 = tblb + 0x108;
        ((volatile Ov_802F28E0 *)v1)[1].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
        ((volatile Ov_802F28E0 *)v1)[2].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
        lbl_805D6971 = 1;
    }
""")
# A3: volatile POINTER var feeding copies 2&3
V["A3_volptr"] = mk("""    if (lbl_805D6971 == 0) {
        ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        { u8 * volatile vp = tblb + 0x108;
          ((Ov_802F28E0 *)(vp + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
          ((Ov_802F28E0 *)(vp + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf; }
        lbl_805D6971 = 1;
    }
""")
# A4: blob-view struct, volatile dst window, all 3 copies
V["A4_blob_vol"] = mk("""    if (lbl_805D6971 == 0) {
        { struct BlobView { u8 pre[0xE4]; Ov_802F28E0 img[3]; volatile Ov_802F28E0 dst[3]; };
          BlobView *bv = (BlobView *)tblb;
          bv->dst[0].pmf = bv->img[0].pmf;
          bv->dst[1].pmf = bv->img[1].pmf;
          bv->dst[2].pmf = bv->img[2].pmf; }
        lbl_805D6971 = 1;
    }
""")
# A5: blob-view, volatile dst + const img
V["A5_blob_volconst"] = mk("""    if (lbl_805D6971 == 0) {
        { struct BlobViewC { u8 pre[0xE4]; const Ov_802F28E0 img[3]; volatile Ov_802F28E0 dst[3]; };
          BlobViewC *bv = (BlobViewC *)tblb;
          bv->dst[0].pmf = bv->img[0].pmf;
          bv->dst[1].pmf = bv->img[1].pmf;
          bv->dst[2].pmf = bv->img[2].pmf; }
        lbl_805D6971 = 1;
    }
""")
# A6: fold-split exactly like orig: copy1 plain, copies 2&3 via volatile window
V["A6_foldsplit"] = V["A2_voldst23"]  # same shape; keep for rowdiff focus
# A7: copy1 via window0 volatile, copies 2&3 plain (inverse split)
V["A7_volfirst"] = mk("""    if (lbl_805D6971 == 0) {
        v1 = tblb + 0x108;
        ((volatile Ov_802F28E0 *)v1)[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        ((Ov_802F28E0 *)(v1 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
        ((Ov_802F28E0 *)(v1 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
        lbl_805D6971 = 1;
    }
""")
# A8: volatile st read in tail
V["A8_volst"] = mk(GUARD_CHAMP).replace("    st = *(s32 *)((s8 *)this + 0x1C);", "    st = *(volatile s32 *)((s8 *)this + 0x1C);")
# A9: A1+A2 combo
V["A9_volguard_dst"] = mk(V["A2_voldst23"].split("void TUnk_804E4B3C::run_task() {")[1], decl_edits=[("extern s8 lbl_805D6971;", "extern volatile s8 lbl_805D6971;")]) if False else None
# A10: non-volatile blob-view control (folding expected? typed field paths tried before but plain struct w/ named bv var)
V["A10_blob_plain"] = mk("""    if (lbl_805D6971 == 0) {
        { struct BlobView { u8 pre[0xE4]; Ov_802F28E0 img[3]; Ov_802F28E0 dst[3]; };
          BlobView *bv = (BlobView *)tblb;
          bv->dst[0].pmf = bv->img[0].pmf;
          bv->dst[1].pmf = bv->img[1].pmf;
          bv->dst[2].pmf = bv->img[2].pmf; }
        lbl_805D6971 = 1;
    }
""")
V["A2_voldst23"] = mk("""    if (lbl_805D6971 == 0) {
        ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        v1 = tblb + 0x108;
        ((volatile Ov_802F28E0 *)v1)[1].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
        ((volatile Ov_802F28E0 *)v1)[2].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
        lbl_805D6971 = 1;
    }
""")
del V["A6_foldsplit"]
V.pop("A9_volguard_dst", None)
# A9: guard window via volatile Ov* v1 = window (volatile pointer to union), copies indexed [1],[2]
V["A9_volwind"] = mk("""    if (lbl_805D6971 == 0) {
        { Ov_802F28E0 volatile *vw = (Ov_802F28E0 volatile *)tblb + 0xD; /* 0xD*12 = 0x9C? NO — 0x108/12=0x14 */ }
        ((Ov_802F28E0 *)(tblb + 0x108))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xE4))[0].pmf;
        v1 = tblb + 0x108;
        ((Ov_802F28E0 *)(v1 + 0xC))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xF0))[0].pmf;
        ((Ov_802F28E0 *)(v1 + 0x18))[0].pmf = ((Ov_802F28E0 *)(tblb + 0xFC))[0].pmf;
        lbl_805D6971 = 1;
    }
""") if False else None
V.pop("A9_volwind", None)

results = {}
for name, src in sorted(V.items()):
    cpp = f"{KIT}/abl_{name}.cpp"
    obj = f"{KIT}/abl_{name}.o"
    open(cpp, "w").write(src)
    p = subprocess.run(["sh", "-c", f"cd {REPO} && {CMD} -c {cpp} -o {obj}"],
                       capture_output=True, text=True)
    if p.returncode != 0:
        results[name] = ("COMPILE_FAIL", p.stderr.strip().splitlines()[:3])
        continue
    sc = subprocess.run([sys.executable, f"{KIT}/probe_score.py", obj], capture_output=True, text=True)
    g = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", "-n", obj], capture_output=True, text=True)
    m = re.search(r"run_task__13TUnk_804E4B3CFv", g.stdout)
    size = g.stdout.split()[0][8:16] if m and len(g.stdout) > 16 else "?"
    for line in g.stdout.splitlines():
        if "run_task" in line:
            size = line.split()[1]
    results[name] = (sc.stdout.strip().splitlines()[0][:120], size)

for k, v in results.items():
    print(f"{k:22} {v[1]:>6}  {v[0]}")
