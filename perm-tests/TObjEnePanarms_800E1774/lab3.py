
import subprocess, re
REPO="/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K="/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
FLAGS=("-nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -char signed -use_lmw_stmw on -O4,s -inline off -sdata2 4 -lang=c++").split()
PRE="""
typedef signed long s32; typedef unsigned char u8;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern Vec *g_e; extern const f64 g_c; extern const f64 g_c2; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);
extern s32 rand(void);
"""
def conv(tag, body):
    cpp=f"{K}/lab_{tag}.cpp"; open(cpp,"w").write('extern "C" {'+PRE+body+'}')
    obj=f"{K}/lab_{tag}.o"
    p=subprocess.run([f"{REPO}/build/tools/wibo",f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",*FLAGS,"-c",cpp,"-o",obj],cwd=REPO,capture_output=True,text=True)
    if p.returncode!=0: print(tag,"FAIL"); return
    d=subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump","-d","--no-show-raw-insn",obj],capture_output=True,text=True).stdout
    stfd=re.findall(r"stfd\s+f\d+,(\d+)\(r1\)",d); ni=len(re.findall(r"^\s+[0-9a-f]+:",d,re.M))
    print(f"{tag}: ins={ni} stfd={stfd}")
# L2: same shape both arms, different literal constants in mul tree
conv("L2","""
s32 l2(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z) * 2.0)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z) * 3.0))<0x400) return 1; return 0;
}
""")
# L3: roll_shop mirror — same shape, different global const identity (g_c vs g_c2)
conv("L3","""
s32 l3(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(g_c2*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0;
}
""")
# L4: roll_shop exact mirror structure with named s32 v + clamp after
conv("L4","""
s32 l4(void *it) {
    u8 v;
    if (g_closed) { v = (s32)(g_c * ((f64(*)(s32))rand)(0)); if ((s32)v < 3) v = 3; }
    else { v = (s32)(g_c2 * ((f64(*)(s32))rand)(0)); if ((s32)v < 2) v = 2; }
    return v;
}
"""  )
# L5: two conversions in SAME nested if but through different local f64 homes? (our shape + locals)
conv("L5","""
s32 l5(f32 sum) {
    Vec v;
    s32 ok;
    f64 d1;
    f64 d2;
    if (g_closed) { ok=0; d1=g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z); if(consume(1,(s32)d1)<0x400) ok=1; return (u8)ok; }
    ok=0; d2=g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z); if(consume(2,(s32)d2)<0x400) ok=1; return (u8)ok;
}
"""  )
