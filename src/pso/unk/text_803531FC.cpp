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

struct Z108 {
    u32 w[27];
};

void TUnk_804F112C::apply_use_effect() {
    union PmfRow {
        UseEffectFn fn;
        u32 w[3];
    };
    union Buf27 {
        Z108 s;
        u32 w[27];
    };
    Buf27 buf;
    const u32 *t = (const u32 *)lbl_804F10C0;

    buf.s = *(const Z108 *)lbl_80479100;

    buf.w[0] = t[0];
    buf.w[1] = t[1];
    buf.w[2] = t[2];
    buf.w[3] = t[3];
    buf.w[4] = t[4];
    buf.w[5] = t[5];
    buf.w[6] = t[6];
    buf.w[7] = t[7];
    buf.w[8] = t[8];
    buf.w[9] = t[9];
    buf.w[10] = t[10];
    buf.w[11] = t[11];
    buf.w[12] = t[12];
    buf.w[13] = t[13];
    buf.w[14] = t[14];
    buf.w[15] = t[15];
    buf.w[16] = t[16];
    buf.w[17] = t[17];
    buf.w[18] = t[18];
    buf.w[19] = t[19];
    buf.w[20] = t[20];
    buf.w[21] = t[21];
    buf.w[22] = t[22];
    buf.w[23] = t[23];
    buf.w[24] = t[24];
    buf.w[25] = t[25];
    buf.w[26] = t[26];

    u8 tech = (u8)get_technique__11TItemObjectFv((TItemObject *)this);
    if (tech < 9) {
        u32 *e = &buf.w[tech * 3];
        PmfRow row;
        row.w[0] = e[0];
        row.w[1] = e[1];
        row.w[2] = e[2];
        ((TEndingPic *)this->*(row.fn))(row.w[1], row.w[2]);
    }
}
