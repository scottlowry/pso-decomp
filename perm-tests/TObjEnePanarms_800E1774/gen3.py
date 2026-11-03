import re
KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
CPP = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/src/pso/enemy/TObjEnePanarms.cpp"

full = open(CPP).read()
m = re.search(r"^s32 TObjEnePanarms__sub_800E1774\(void \*arg0\) \{\n.*?^\}\n", full, re.S | re.M)
head, tail = full[:m.start()], full[m.end():]

BODY_SCOPED = """s32 TObjEnePanarms__sub_800E1774(void *arg0) {
    s32 idx;
    s32 ok;
    f64 d1;
    f64 d2;

    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {
        Vec_800E0A44 v;
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4((O_800E2FB4 *)*(s32 *)((s8 *)arg0 + 0x3A0)) == 0) {
            idx = ((TObjEnePanarms *)arg0)->find_nearest_enemy_with_flag_alt_target((s32)&v, lbl_8043CD80[((TObjEnePanarms *)arg0)->m_380]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {
                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);
                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d1) < 0x400) {
                    ok = 1;
                }
            }
        }
        return (u8)ok;
    }
    {
        Vec_800E0A44 v;
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4((O_800E2FB4 *)*(s32 *)((s8 *)arg0 + 0x3A0)) == 0) {
            idx = find_nearest_visible_player(arg0, &v, lbl_8043CD80[((TObjEnePanarms *)arg0)->m_380]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {
                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);
                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d2) < 0x400) {
                    ok = 1;
                }
            }
        }
        return (u8)ok;
    }
}
"""

# c20: scoped v + single named s32 angle in both arms (fn_8034D3D0 total pattern)
A1 = "                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d1) < 0x400) {"
A2 = "                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d2) < 0x400) {"
CONV = "                angle = (s32)(TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z));\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, angle) < 0x400) {"
BODY20 = BODY_SCOPED.replace("    f64 d1;\n    f64 d2;\n", "    s32 angle;\n").replace(A1, CONV).replace(A2, CONV)
assert "angle = " in BODY20 and BODY20.count("angle = ") == 2

# c21: top-scope v + single named s32 angle both arms
BODY21 = BODY20.replace("    s32 angle;\n", "    s32 angle;\n    Vec_800E0A44 v;\n").replace("        Vec_800E0A44 v;\n        ok = 0;", "        ok = 0;")

# c22: scoped v + named s32 angle in arm A only (champion d2 in B)
BODY22 = BODY_SCOPED.replace("    f64 d1;\n    f64 d2;\n", "    s32 angle;\n    f64 d2;\n").replace(A1, CONV)

open(f"{KIT}/c19_scoped.cpp", "w").write(head + BODY_SCOPED + tail)
open(f"{KIT}/c20_scoped_angle.cpp", "w").write(head + BODY20 + tail)
open(f"{KIT}/c21_angle_topscope.cpp", "w").write(head + BODY21 + tail)
open(f"{KIT}/c22_angleA_only.cpp", "w").write(head + BODY22 + tail)
print("gen3 written")
