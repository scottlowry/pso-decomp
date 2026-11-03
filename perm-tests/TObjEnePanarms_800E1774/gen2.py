#!/opt/homebrew/bin/python3.14
"""Gen2: untried pragma knobs + align modes + filler placements."""
import re

KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
CPP = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/src/pso/enemy/TObjEnePanarms.cpp"

full = open(CPP).read()
m = re.search(r"^s32 TObjEnePanarms__sub_800E1774\(void \*arg0\) \{\n.*?^\}\n", full, re.S | re.M)
assert m
FN = m.group(0)

PRAGMAS = [
    ("opt_dead_code", "off"), ("opt_dead_code", "on"),
    ("opt_pointer_analysis", "off"), ("opt_pointer_analysis", "on"),
    ("opt_pointer_analysis_mode", "off"), ("opt_pointer_analysis_mode", "3"),
    ("opt_partial", "off"), ("opt_partial", "on"),
    ("opt_strength_reduction", "off"), ("opt_strength_reduction_strict", "off"),
    ("opt_loop_invariants", "off"), ("peephole", "off"),
]

def wrap(fn, pragmas):
    if not pragmas:
        return fn
    head = "".join(f"#pragma push\n#pragma {n} {v}\n" for n, v in pragmas)
    tail = "".join("#pragma pop\n" for _ in pragmas)
    return head + fn + tail

def align_wrap(fn, mode):
    if not mode:
        return fn
    return f"#pragma push\n#pragma options align={mode}\n" + fn + f"\n#pragma pop\n"

def filler(fn, spec):
    if not spec:
        return fn
    anchor, ins = spec
    assert anchor in fn, anchor[:40]
    return fn.replace(anchor, anchor + ins, 1)

out = {}
for n, v in PRAGMAS:
    out[f"p_{n}_{v}"] = wrap(FN, [(n, v)])
out["p_all_off"] = wrap(FN, [(n, "off") for n, v in PRAGMAS])
for mode in ["double", "natural", "packed", "long"]:
    out[f"al_{mode}"] = align_wrap(FN, mode)
# filler battery: self-assign pins at unique in-scope anchors
A1 = "                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);"
B1 = "                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));"
A_tail = "        }\n        return (u8)ok;\n    }\n    {"
B_head = "    {\n        ok = 0;"
FILL = {"d1": "\n                d1 = d1;", "d2": "\n                d2 = d2;",
        "idx": "\n                idx = idx;", "ok": "\n                ok = ok;",
        "d1b": "\n        d1 = d1;", "d2b": "\n        d2 = d2;"}
def fillat(fn, anchor, ins, before=False):
    assert anchor in fn, anchor[:40]
    return fn.replace(anchor, (ins + anchor if before else anchor + ins), 1)
for ai, atxt in {"A1": A1, "B1": B1, "Atail": A_tail, "Bhead": B_head}.items():
    for fi, ftxt in FILL.items():
        before = ai in ("Atail", "Bhead")
        out[f"f_{ai}_{fi}"] = fillat(FN, atxt, ftxt, before)

# combo: pragma knobs + all_off
for n, v in PRAGMAS[:5]:
    out[f"ca_{n}"] = wrap(FN, [(n, v)] + [("opt_dead_code", "off"), ("opt_pointer_analysis", "off")])

for name, body in out.items():
    open(f"{KIT}/{name}.cpp", "w").write(full[:m.start()] + body + full[m.end():])
print("\n".join(sorted(out)))
