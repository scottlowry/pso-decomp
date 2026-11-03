#!/opt/homebrew/bin/python3.14
"""Emit variant full-unit cpps for the branched-scratch-split probe battery."""
import re, os

KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
CPP = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/src/pso/enemy/TObjEnePanarms.cpp"

full = open(CPP).read()
m = re.search(r"^s32 TObjEnePanarms__sub_800E1774\(void \*arg0\) \{\n.*?^\}\n", full, re.S | re.M)
assert m, "fn region not found"
head, tail = full[:m.start()], full[m.end():]

ATAN = '((f64 (*)(f32, f32))atan2_float)'
C = 'TObjEnePanarms__data_8043CDD0'

def make(a_spec, b_spec, extra_decls=""):
    # a_spec/b_spec: (assign_stmts, use_expr)
    return f'''s32 TObjEnePanarms__sub_800E1774(void *arg0) {{
    Vec_800E0A44 v;
    s32 idx;
    s32 ok;
{extra_decls}
    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {{
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4((O_800E2FB4 *)*(s32 *)((s8 *)arg0 + 0x3A0)) == 0) {{
            idx = ((TObjEnePanarms *)arg0)->find_nearest_enemy_with_flag_alt_target((s32)&v, lbl_8043CD80[((TObjEnePanarms *)arg0)->m_380]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {{
{a_spec[0]}
                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, {a_spec[1]}) < 0x400) {{
                    ok = 1;
                }}
            }}
        }}
        return (u8)ok;
    }}
    {{
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4((O_800E2FB4 *)*(s32 *)((s8 *)arg0 + 0x3A0)) == 0) {{
            idx = find_nearest_visible_player(arg0, &v, lbl_8043CD80[((TObjEnePanarms *)arg0)->m_380]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {{
{b_spec[0]}
                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, {b_spec[1]}) < 0x400) {{
                    ok = 1;
                }}
            }}
        }}
        return (u8)ok;
    }}
}}
'''

A_f64 = (f"                d1 = {C} * {ATAN}(v.x, v.z);", "(s32)d1")
A_s32 = (f"                i1 = (s32)({C} * {ATAN}(v.x, v.z));", "i1")
A_tmp = (f"                t1 = {ATAN}(v.x, v.z);\n                d1 = {C} * t1;", "(s32)d1")
B_f64ptr = (f"                d2 = {C} * {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));", "(s32)d2")
B_f64dot = (f"                d2 = {C} * {ATAN}(v.x, v.z);", "(s32)d2")
B_s32 = (f"                i2 = (s32)({C} * {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8)));", "i2")
B_swap = (f"                d2 = {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8)) * {C};", "(s32)d2")
B_comma = (f"                d2 = (0, {C} * {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8)));", "(s32)d2")
B_tmp = (f"                t2 = {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));\n                d2 = {C} * t2;", "(s32)d2")
B_fill = (f"                d2 = {C} * {ATAN}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));\n                d2 = d2;", "(s32)d2")
B_s32samedot = (f"                i2 = (s32)({C} * {ATAN}(v.x, v.z));", "i2")

D_full = "    f64 d1;\n    f64 d2;\n"
D_i = "    f64 d1;\n    f64 d2;\n    s32 i1;\n    s32 i2;\n"
D_itmp = "    f64 d1;\n    f64 d2;\n    s32 i1;\n    s32 i2;\n    f64 t1;\n    f64 t2;\n"

VARIANTS = {
    "c0_champ": make(A_f64, B_f64ptr, D_full),
    "c1_Bs32": make(A_f64, B_s32, D_i),
    "c2_Abs32": make(A_s32, B_f64ptr, D_i),
    "c3_Boths32": make(A_s32, B_s32, D_i),
    "c4_Bswap": make(A_f64, B_swap, D_full),
    "c5_Bcomma": make(A_f64, B_comma, D_full),
    "c6_Btmp": make(A_f64, B_tmp, D_itmp),
    "c7_Atmp": make(A_tmp, B_f64ptr, D_itmp),
    "c8_Bfill": make(A_f64, B_fill, D_full),
    "c9_Bdot": make(A_f64, B_f64dot, D_full),
    "c10_Bs32dot": make(A_f64, B_s32samedot, D_i),
    "c11_Abs32dot": make(A_s32, B_f64dot, D_i),
    "c12_Boths32dot": make(A_s32, B_s32samedot, D_i),
}


# --- addendum battery: call-node differentiation ---
ATAN64 = '((f64 (*)(f64, f64))atan2_float)'
B_atan64 = (f"                d2 = {C} * {ATAN64}(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));", "(s32)d2")
A_atan64 = (f"                d1 = {C} * {ATAN64}(v.x, v.z);", "(s32)d1")
B_atan3 = (f"                d2 = {C} * ((f64 (*)(f32, f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8), 0.0f);", "(s32)d2")
VARIANTS.update({
    "c13_Batan64": make(A_f64, B_atan64, D_full),
    "c14_Aatan64": make(A_atan64, B_f64ptr, D_full),
    "c15_Both64": make(A_s32, B_atan64, D_i),
    "c16_Bdot64": make(A_f64, (f"                d2 = {C} * {ATAN64}(v.x, v.z);", "(s32)d2"), D_full),
})

for name, body in VARIANTS.items():
    open(f"{KIT}/{name}.cpp", "w").write(head + body + tail)
print("\n".join(sorted(VARIANTS)))
