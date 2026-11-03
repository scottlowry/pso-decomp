
import re
KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
CPP = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/src/pso/enemy/TObjEnePanarms.cpp"
full = open(CPP).read()
m = re.search(r"^s32 TObjEnePanarms__sub_800E1774\(void \*arg0\) \{\n.*?^\}\n", full, re.S | re.M)
head, tail = full[:m.start()], full[m.end():]
src = m.group(0)
B1 = "                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));"
A1 = "                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);"
# c33: arm B reads through shadowed local initialized from the global
c33 = src.replace("    {\n        ok = 0;", "    {\n        const f64 Cb = TObjEnePanarms__data_8043CDD0;\n        ok = 0;")
c33 = c33.replace(B1, "                d2 = Cb * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
assert "Cb" in c33
open(f"{KIT}/c33_shadowB.cpp","w").write(head + c33 + tail)
# c34: same but shadow at top scope (declared after d1/d2)
c34 = src.replace("    f64 d1;\n    f64 d2;\n", "    f64 d1;\n    f64 d2;\n    const f64 Cb = TObjEnePanarms__data_8043CDD0;\n")
c34 = c34.replace(B1, "                d2 = Cb * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
open(f"{KIT}/c34_shadowTop.cpp","w").write(head + c34 + tail)
# c35: shadow on arm A instead
c35 = src.replace("    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {\n        ok = 0;", "    if (((TObjEnePanarms *)arg0)->get_state_flag() != 0) {\n        const f64 Ca = TObjEnePanarms__data_8043CDD0;\n        ok = 0;")
c35 = c35.replace(A1, "                d1 = Ca * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);")
open(f"{KIT}/c35_shadowA.cpp","w").write(head + c35 + tail)
# c36: both-arm shadow (Ca in A, Cb in B)
c36 = c35.replace("    {\n        ok = 0;", "    {\n        const f64 Cb = TObjEnePanarms__data_8043CDD0;\n        ok = 0;")
c36 = c36.replace(B1, "                d2 = Cb * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));")
open(f"{KIT}/c36_shadowBoth.cpp","w").write(head + c36 + tail)
print("gen6")
