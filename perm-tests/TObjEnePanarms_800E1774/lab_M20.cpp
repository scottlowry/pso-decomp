extern "C" {
typedef signed long s32; typedef unsigned char u8;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern const f64 g_c; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);

s32 m20(f32 sum) {
    Vec v;
    if (g_closed) { if (consume(1,(s32)(g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0; }
    if (consume(2,(s32)(*(volatile f64 *)&g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z)))<0x400) return 1; return 0;
}
}