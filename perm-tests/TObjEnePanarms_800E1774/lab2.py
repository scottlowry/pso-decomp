
import subprocess, re, os
REPO="/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K="/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
FLAGS=("-nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -char signed -use_lmw_stmw on -O4,s -inline off -sdata2 4 -lang=c++").split()
PRE="""
typedef signed char s8; typedef unsigned char u8;
typedef signed long s32; typedef unsigned long u32;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern Vec *g_e; extern const f64 g_c; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);
"""
def conv(tag, body):
    cpp=f"{K}/lab_{tag}.cpp"; open(cpp,"w").write('extern "C" {'+PRE+body+'}')
    obj=f"{K}/lab_{tag}.o"
    p=subprocess.run([f"{REPO}/build/tools/wibo",f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",*FLAGS,"-c",cpp,"-o",obj],cwd=REPO,capture_output=True,text=True)
    if p.returncode!=0: print(tag,"FAIL"); return
    d=subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump","-d","--no-show-raw-insn",obj],capture_output=True,text=True).stdout
    stfd=re.findall(r"stfd\s+f\d+,(\d+)\(r1\)",d); n=len(re.findall(r"^\s*[0-9a-f]+:",d,re.M))
    print(f"{tag}: ins={n} stfd={stfd}")
# M12: +0.0 peephole-foldable extra node on arm B
conv("M12", """
s32 m12(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z) + 0.0))<0x400) return 1; return 0;
}
""")
# M13: double negation
conv("M13", """
s32 m13(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,-(s32)(-(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z))))<0x400) return 1; return 0;
}
""")
# M14: *1.0 on arm B
conv("M14", """
s32 m14(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(1.0*(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z))))<0x400) return 1; return 0;
}
""")
# M15: same trees, arm B conv feeds var used at join
conv("M15", """
s32 m15(f32 sum) {
    Vec v;
    s32 r;
    if (g_closed) { r = consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z))); return r; }
    r = consume(2,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z))); return r;
}
""")
# M16: arm B multiplies by 2.0 with /2.0 — visible; instead arm B via f64 array element g_c
conv("M16", """
s32 m16(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(((f64(*)(f32,f32))atan2_float)(v.x,v.z)*g_c))<0x400) return 1; return 0;
}
"""  )
# M17: arm B: cast source is parenthesized via intermediate comma
conv("M17", """
s32 m17(f32 sum) {
    Vec v;
    f64 d1;
    if (g_closed) { d1 = g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z); if (consume(1,(s32)d1)<0x400) return 1; return 0; }
    if (consume(2,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0;
}
"""  )
