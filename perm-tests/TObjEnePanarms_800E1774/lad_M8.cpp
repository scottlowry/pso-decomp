extern "C" {
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
}