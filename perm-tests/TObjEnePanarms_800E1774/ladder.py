import subprocess, re, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K = f"{REPO}/perm-tests/TObjEnePanarms_800E1774"
FLAGS = ("-nodefaults -proc gekko -align powerpc -enum int -fp hardware "
    "-Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath "
    "-char signed -use_lmw_stmw on -O4,s -inline off -sdata2 4 -lang=c++").split()

PRE = """
typedef signed char s8; typedef unsigned char u8;
typedef signed short s16; typedef unsigned short u16;
typedef signed long s32; typedef unsigned long u32;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern Vec *g_e; extern f32 g_tbl[]; extern const f64 g_c;
extern s32 g_closed;
extern f32 call_a(Vec *v);
extern s32 consume(s32, s32);
extern u16 call_b(void *, Vec *, f32);
extern f64 atan2_float(f32, f32, f32);
extern s32 angle_difference_abs(s32, s32);
"""

# M1: faithful fn_8034 shape (if/else, single named s32, join, later use)
M1 = """
s32 m1(f32 sum) {
    s32 total;
    f32 r;
    if (g_closed == 0) {
        total = (s32) (sum - g_e[1].y);
    } else {
        total = (s32) sum;
    }
    r = sum * (f32) total;
    return (s32) (r + 1.5f);
}
"""
# M2: same but arms terminate with returns
M2 = """
s32 m2(f32 sum) {
    s32 total;
    if (g_closed == 0) {
        total = (s32) (sum - g_e[1].y);
        return 0x5A - total;
    }
    total = (s32) sum;
    return 0x3C - total;
}
"""
# M3: converted value consumed immediately in call arg (no named var), join after
M3 = """
s32 m3(f32 sum) {
    s32 res;
    if (g_closed == 0) {
        res = consume(1, (s32) (sum - g_e[1].y));
    } else {
        res = consume(2, (s32) sum);
    }
    return res;
}
"""
# M4: my target shape: outer if/else, arms end in returns, immediate arg consumption
M4 = """
s32 m4(f32 sum) {
    if (g_closed != 0) {
        if (consume(1, (s32) (g_c * sum)) < 0x400) {
            return 1;
        }
        return 0;
    }
    if (consume(2, (s32) (g_c * sum)) < 0x400) {
        return 1;
    }
    return 0;
}
"""
# M5: like M4 but named f64 pair + cast (champion)
M5 = """
s32 m5(f32 sum) {
    f64 d1;
    f64 d2;
    if (g_closed != 0) {
        d1 = g_c * sum;
        if (consume(1, (s32)d1) < 0x400) { return 1; }
        return 0;
    }
    d2 = g_c * sum;
    if (consume(2, (s32)d2) < 0x400) { return 1; }
    return 0;
}
"""
# M6: roll_shop mirror: implicit float->s32 conversion assign single var, no join use
M6 = """
s32 m6(f32 sum) {
    s32 v;
    if (g_closed != 0) {
        v = g_c * sum;
        if (consume(1, v) < 0x400) { return 1; }
        return 0;
    }
    v = g_c * sum;
    if (consume(2, v) < 0x400) { return 1; }
    return 0;
}
"""
# M7: like M6 but conversion arms have distinct operand sources (different globals)
M7 = """
s32 m7(f32 sum) {
    s32 v;
    if (g_closed != 0) {
        v = ((f64 (*)(f32, f32))atan2_float)(sum, g_e[0].x) * g_c;
        if (consume(1, v) < 0x400) { return 1; }
        return 0;
    }
    v = ((f64 (*)(f32, f32))atan2_float)(sum, g_e[1].x) * g_c;
    if (consume(2, v) < 0x400) { return 1; }
    return 0;
}
"""
# M8: my function's FULL structure with nested idx-if and 3 arg calls
M8 = """
s32 m8(void *self) {
    Vec v;
    s32 idx;
    s32 ok;
    if (call_a(&v) != 0) {
        ok = 0;
        if (angle_difference_abs(0, (s32)(g_c * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z))) < 0x400) {
            ok = 1;
        }
        return (u8)ok;
    }
    ok = 0;
    idx = call_b(self, &v, g_tbl[0]);
    if (idx != 0xFFFF) {
        if (angle_difference_abs(1, (s32)(g_c * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z))) < 0x400) {
            ok = 1;
        }
    }
    return (u8)ok;
}
"""

for tag, body in {"M1":M1,"M2":M2,"M3":M3,"M4":M4,"M5":M5,"M6":M6,"M7":M7,"M8":M8}.items():
    cpp = f"{K}/lad_{tag}.cpp"
    open(cpp, "w").write('extern "C" {' + PRE + body + '}')
    obj = f"{K}/lad_{tag}.o"
    p = subprocess.run([f"{REPO}/build/tools/wibo", f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",
                        *FLAGS, "-c", cpp, "-o", obj], cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0 or not os.path.exists(obj):
        err = [l for l in p.stdout.splitlines() if "Error" in l][:2]
        print(f"{tag}: FAIL {err}"); continue
    d = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-d", "--no-show-raw-insn", obj],
                       capture_output=True, text=True).stdout
    stfd = re.findall(r"stfd\s+f\d+,(\d+)\(r1\)", d)
    print(f"{tag}: stfd_slots={stfd}")
