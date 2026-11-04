#include "types.h"

#pragma inline_depth(1)
#pragma auto_inline off
#pragma dont_inline off

struct TItemObject;
struct TEndingPic;

extern "C" {
extern const u32 lbl_80479100[28];
typedef void (TEndingPic::*UseEffectFn)(s32, s32);
extern UseEffectFn lbl_804F10C0[9];
u32 get_technique__11TItemObjectFv(TItemObject *self);
}

struct TUnk_804F112C {
    void apply_use_effect();
};

void TUnk_804F112C::apply_use_effect() {
    union PmfRow {
        UseEffectFn fn;
        u32 w[3];
    };
    u32 buf[27];
    u32 d;
    const u32 *z = lbl_80479100;
    const u32 *t = (const u32 *)lbl_804F10C0;

    for (d = 0; d < 13; d++) {
        buf[2 * d] = z[2 * d];
        buf[2 * d + 1] = z[2 * d + 1];
    }
    buf[26] = z[26];

    buf[0] = t[0];
    buf[1] = t[1];
    buf[2] = t[2];
    buf[3] = t[3];
    buf[4] = t[4];
    buf[5] = t[5];
    buf[6] = t[6];
    buf[7] = t[7];
    buf[8] = t[8];
    buf[9] = t[9];
    buf[10] = t[10];
    buf[11] = t[11];
    buf[12] = t[12];
    buf[13] = t[13];
    buf[14] = t[14];
    buf[15] = t[15];
    buf[16] = t[16];
    buf[17] = t[17];
    buf[18] = t[18];
    buf[19] = t[19];
    buf[20] = t[20];
    buf[21] = t[21];
    buf[22] = t[22];
    buf[23] = t[23];
    buf[24] = t[24];
    buf[25] = t[25];
    buf[26] = t[26];

    u8 tech = (u8)get_technique__11TItemObjectFv((TItemObject *)this);
    if (tech < 9) {
        u32 *e = &buf[tech * 3];
        PmfRow row;
        row.w[0] = e[0];
        row.w[1] = e[1];
        row.w[2] = e[2];
        ((TEndingPic *)this->*(row.fn))(row.w[1], row.w[2]);
    }
}
