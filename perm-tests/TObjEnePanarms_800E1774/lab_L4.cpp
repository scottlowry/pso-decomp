extern "C" {
typedef signed long s32; typedef unsigned char u8;
typedef float f32; typedef double f64;
typedef struct { f32 x, y, z; } Vec;
extern Vec *g_e; extern const f64 g_c; extern const f64 g_c2; extern s32 g_closed;
extern s32 consume(s32, s32);
extern f64 atan2_float(f32, f32, f32);
extern s32 rand(void);

s32 l4(void *it) {
    u8 v;
    if (g_closed) { v = (s32)(g_c * ((f64(*)(s32))rand)(0)); if ((s32)v < 3) v = 3; }
    else { v = (s32)(g_c2 * ((f64(*)(s32))rand)(0)); if ((s32)v < 2) v = 2; }
    return v;
}
}