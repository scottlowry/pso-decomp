typedef signed char s8;
typedef unsigned char u8;
typedef unsigned short u16;
typedef signed long s32;
typedef float f32;
typedef double f64;

typedef struct { f32 x, y, z; } Vec_800E0A44;

extern const f64 TObjEnePanarms__data_8043CDD0;
extern f32 lbl_8043CD80[];

s32 get_state_flag__14TObjEnePanarmsFv(void *);
s32 TObjEnePanarms__sub_800E2FB4(void *);
s32 find_nearest_enemy_with_flag_alt_target__14TObjEnePanarmsFlf(void *, s32, f32);
u16 find_nearest_visible_player(void *, Vec_800E0A44 *, f32);
f64 atan2_float(f32, f32, f32);
s32 angle_difference_abs(s32, s32);

#pragma push
#pragma fp_contract on
#pragma opt_propagation off
#pragma opt_lifetimes off
s32 TObjEnePanarms__sub_800E1774(void *arg0) {
    Vec_800E0A44 v;
    s32 idx;
    s32 ok;
    f64 d1;
    f64 d2;

    if (get_state_flag__14TObjEnePanarmsFv(arg0) != 0) {
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4(*(void **)((s8 *)arg0 + 0x3A0)) == 0) {
            idx = find_nearest_enemy_with_flag_alt_target__14TObjEnePanarmsFlf(arg0, (s32)&v, lbl_8043CD80[*(s32 *)((s8 *)arg0 + 0x380)]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {
                d1 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(v.x, v.z);
                if (angle_difference_abs(*(s32 *)((s8 *)arg0 + 0x60), (s32)d1) < 0x400) {
                    ok = 1;
                }
            }
        }
        return (u8)ok;
    }
    {
        ok = 0;
        if (TObjEnePanarms__sub_800E2FB4(*(void **)((s8 *)arg0 + 0x3A0)) == 0) {
            idx = find_nearest_visible_player(arg0, &v, lbl_8043CD80[*(s32 *)((s8 *)arg0 + 0x380)]);
            *(s32 *)((s8 *)arg0 + 0x3B8) = idx;
            if (idx != 0xFFFF) {
                d2 = TObjEnePanarms__data_8043CDD0 * ((f64 (*)(f32, f32))atan2_float)(*(f32 *)((s8 *)&v), *(f32 *)((s8 *)&v + 8));
                if (angle_difference_abs(*(s32 *)((s8 *)arg0 + 0x60), (s32)d2) < 0x400) {
                    ok = 1;
                }
            }
        }
        return (u8)ok;
    }
}
#pragma pop
