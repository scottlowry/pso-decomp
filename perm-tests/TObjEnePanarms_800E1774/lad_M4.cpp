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
}