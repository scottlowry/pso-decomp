#!/opt/homebrew/bin/python3.14
"""Night-era interaction/attractor/restage grid for panarms scratch-slot wall.
Emits full-unit cpp variants (single + multi moves) into kit/grid/, prints list.
Replaces ONLY inside the sub_800E1774 body region (uniqueness-checked, 1 occurrence)."""
import os, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
SRC = f"{REPO}/src/pso/enemy/TObjEnePanarms.cpp"
KIT = f"{REPO}/tools/perm-tests/f8_TObjEnePanarms_800E1774"
GRID = f"{KIT}/grid"
os.makedirs(GRID, exist_ok=True)

txt = open(SRC).read()
sig = "s32 TObjEnePanarms__sub_800E1774(void *arg0) {"
i0 = txt.index(sig)
i1 = txt.index("\n}\n", i0) + 3
BODY = txt[i0:i1]
assert BODY.count("d1 = ") == 1 and BODY.count("d2 = ") == 1

def rep(s, old, new, cnt=1):
    assert s.count(old) == cnt, f"anchor not unique ({s.count(old)}): {old[:60]}"
    return s.replace(old, new, 1)

V = {}
V["champ"] = BODY
# singles
V["bothpun"] = rep(BODY, ")(v.x, v.z);", ")(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
V["bothmem"] = rep(BODY, ")(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));", ")(v.x, v.z);")
d4 = BODY
for a, b in (("f64 d1;\n    f64 d2;", "f64 d;"), ("d1 = ", "d = "), ("d2 = ", "d = "),
             ("(s32)d1", "(s32)d"), ("(s32)d2", "(s32)d")):
    d4 = rep(d4, a, b, d4.count(a) if a in ("d1 = ", "d2 = ") else 1) if a in d4 else rep(d4, a, b)
V["shared_d"] = d4
V["ok_u8"] = rep(BODY, "    s32 ok;", "    u8 ok;")
nc = rep(BODY, "    f64 d2;\n", "    f64 d2;\n    s32 k400;\n    k400 = 0x400;\n")
nc = rep(nc, "< 0x400) {\n                    ok = 1;\n                }\n            }\n        }\n        return (u8)ok;\n    }\n    {", "< k400) {\n                    ok = 1;\n                }\n            }\n        }\n        return (u8)ok;\n    }\n    {")
nc = nc.replace("< 0x400", "< k400")
V["namedconst"] = nc
V["sentinel"] = BODY.replace("idx != 0xFFFF", "idx != -1")
# attractor: hoist shared def (ok0) above the branch split — def-completion order lever
outer = BODY
outer = rep(outer, "    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {", "    ok = 0;\n    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {")
outer = outer.replace("        ok = 0;\n", "")
assert "ok = 0;" in outer and outer.count("ok = 0;") == 1
V["ok0_outer"] = outer
# pairs (D4368 interaction cascade doctrine: multi-move, not single)
V["p_ok0_shared"] = rep(outer, "f64 d1;\n    f64 d2;", "f64 d;").replace("d1", "d").replace("d2", "d")
V["p_ok0_pun"] = rep(outer, ")(v.x, v.z);", ")(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
V["p_shared_pun"] = rep(V["shared_d"], ")(v.x, v.z);", ")(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
V["p_sentinel_shared"] = V["shared_d"].replace("idx != 0xFFFF", "idx != -1")
# restage: recompute same value through the dead earlier-named d1 carrier in arm B
rest = BODY.replace("d2 = ", "d1 = d1; d2 = ", 1)
V["restage_self"] = rest
# u8 return-type spelling (wave7 form): fwd-decl + sig + plain return
u8b = BODY.replace("return (u8)ok;", "return ok;")
full = txt[:i0] + "u8 TObjEnePanarms__sub_800E1774(void *arg0) {" + u8b[len(sig):] + txt[i1:]
full = full.replace("s32 TObjEnePanarms__sub_800E1774(void *);", "u8 TObjEnePanarms__sub_800E1774(void *);")
V["u8ret"] = None  # handled specially (full-file)
# cast f32 args explicitly
V["f32casts"] = rep(BODY, "((f64 (*)(f32, f32))atan2_float)(v.x, v.z)", "((f64 (*)(f32, f32))atan2_float)((f32)v.x, (f32)v.z)")

out = []
for k, b in V.items():
    if k == "u8ret":
        f = f"{GRID}/{k}.cpp"
        open(f, "w").write(full)
        out.append(f)
        continue
    if b == BODY:
        f = f"{GRID}/{k}.cpp"
        open(f, "w").write(txt)
        out.append(f)
        continue
    f = f"{GRID}/{k}.cpp"
    open(f, "w").write(txt[:i0] + b + txt[i1:])
    out.append(f)
print("\n".join(out))
