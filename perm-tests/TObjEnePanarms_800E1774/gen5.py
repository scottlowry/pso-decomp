
import re
KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
CPP = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/src/pso/enemy/TObjEnePanarms.cpp"
full = open(CPP).read()
m = re.search(r"^s32 TObjEnePanarms__sub_800E1774\(void \*arg0\) \{\n.*?^\}\n", full, re.S | re.M)
head, tail = full[:m.start()], full[m.end():]
src = m.group(0)
A1 = "                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d1) < 0x400) {"
B1 = "                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, (s32)d2) < 0x400) {"
# c25: implicit conversion into single named s32 angle, both arms, top-scope v
c25 = src.replace("    f64 d1;\n    f64 d2;\n", "    s32 angle;\n")
c25 = c25.replace(A1, "                angle = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, angle) < 0x400) {")
c25 = c25.replace(B1, "                angle = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, angle) < 0x400) {")
open(f"{KIT}/c25_implicit_angle.cpp","w").write(head + c25 + tail)
# c26: implicit + two named s32 i1/i2
c26 = src.replace("    f64 d1;\n    f64 d2;\n", "    s32 i1;\n    s32 i2;\n")
c26 = c26.replace(A1, "                i1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, i1) < 0x400) {")
c26 = c26.replace(B1, "                i2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, i2) < 0x400) {")
open(f"{KIT}/c26_implicit_two.cpp","w").write(head + c26 + tail)
# c27: TWindowSub mirror: implicit conv to u8-like s32 with float-literal-different arms impossible; use explicit s32 cast on angle with DIFFERENT mul shape armB: angle via (long double) no. skip-like: implicit conv from f32 expression (drop f64 cast): angle = atan2f-based? must keep fmul f64. Use (s32) on the OUTER in A, implicit in B:
c27 = src.replace("    f64 d1;\n    f64 d2;\n", "    s32 angle;\n")
c27 = c27.replace(A1, "                angle = (s32)(TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z));\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, angle) < 0x400) {")
c27 = c27.replace(B1, "                angle = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);\n                if (angle_difference_abs(((TObjMotion *)arg0)->rotation_y, angle) < 0x400) {")
open(f"{KIT}/c27_mixed_cast.cpp","w").write(head + c27 + tail)
print("gen5 ok")
