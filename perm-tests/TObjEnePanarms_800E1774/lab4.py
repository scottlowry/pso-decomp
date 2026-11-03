
import subprocess, re
REPO="/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K="/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TObjEnePanarms_800E1774"
FLAGS=("-nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -char signed -use_lmw_stmw on -O4,s -inline off -sdata2 4 -lang=c++").split()
PRE="""
typedef signed long s32; typedef unsigned char u8;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern const f64 g_c; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);
"""
def conv(tag, body, dump=False):
    cpp=f"{K}/lab_{tag}.cpp"; open(cpp,"w").write('extern "C" {'+PRE+body+'}')
    obj=f"{K}/lab_{tag}.o"
    p=subprocess.run([f"{REPO}/build/tools/wibo",f"{REPO}/build/compilers/GC/2.6/mwcceppc.exe",*FLAGS,"-c",cpp,"-o",obj],cwd=REPO,capture_output=True,text=True)
    if p.returncode!=0: print(tag,"FAIL",[l for l in p.stdout.splitlines() if 'Error' in l][:1]); return
    d=subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump","-d","--no-show-raw-insn",obj],capture_output=True,text=True).stdout
    stfd=re.findall(r"stfd\s+f\d+,(\d+)\(r1\)",d); ni=len(re.findall(r"^\s+[0-9a-f]+:",d,re.M))
    print(f"{tag}: ins={ni} stfd={stfd}")
    if dump:
        for l in d.splitlines():
            if re.search(r'fctiwz|stfd|lwz|lfd|fmul|bl  ',l): print("   ",l.strip())
conv("M20","""
s32 m20(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(*(volatile f64 *)&g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0;
}
""", dump=True)
conv("M21","""
s32 m21(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(*(volatile f64 *)&g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(*(volatile f64 *)&g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0;
}
"""  )
