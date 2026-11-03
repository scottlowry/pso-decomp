extern "C" {
typedef signed long s32; typedef unsigned char u8;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern Vec *g_e; extern const f64 g_c; extern const f64 g_c2; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);
extern s32 rand(void);

s32 l5(f32 sum) {
    Vec v;
    s32 ok;
    f64 d1;
    f64 d2;
    if (g_closed) { ok=0; d1=g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z); if(consume(1,(s32)d1)<0x400) ok=1; return (u8)ok; }
    ok=0; d2=g_c*((f64(*)(f32,f32))atan2_float)(v.x,v.z); if(consume(2,(s32)d2)<0x400) ok=1; return (u8)ok;
}
}