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

    for (d = 0; d < 27; d++) {
        buf[d] = lbl_80479100[d];
    }

    buf[0] = *(u32 *)&lbl_804F10C0[0];
    buf[1] = *((u32 *)&lbl_804F10C0[0] + 1);
    buf[2] = *((u32 *)&lbl_804F10C0[0] + 2);
    buf[3] = *(u32 *)&lbl_804F10C0[1];
    buf[4] = *((u32 *)&lbl_804F10C0[1] + 1);
    buf[5] = *((u32 *)&lbl_804F10C0[1] + 2);
    buf[6] = *(u32 *)&lbl_804F10C0[2];
    buf[7] = *((u32 *)&lbl_804F10C0[2] + 1);
    buf[8] = *((u32 *)&lbl_804F10C0[2] + 2);
    buf[9] = *(u32 *)&lbl_804F10C0[3];
    buf[10] = *((u32 *)&lbl_804F10C0[3] + 1);
    buf[11] = *((u32 *)&lbl_804F10C0[3] + 2);
    buf[12] = *(u32 *)&lbl_804F10C0[4];
    buf[13] = *((u32 *)&lbl_804F10C0[4] + 1);
    buf[14] = *((u32 *)&lbl_804F10C0[4] + 2);
    buf[15] = *(u32 *)&lbl_804F10C0[5];
    buf[16] = *((u32 *)&lbl_804F10C0[5] + 1);
    buf[17] = *((u32 *)&lbl_804F10C0[5] + 2);
    buf[18] = *(u32 *)&lbl_804F10C0[6];
    buf[19] = *((u32 *)&lbl_804F10C0[6] + 1);
    buf[20] = *((u32 *)&lbl_804F10C0[6] + 2);
    buf[21] = *(u32 *)&lbl_804F10C0[7];
    buf[22] = *((u32 *)&lbl_804F10C0[7] + 1);
    buf[23] = *((u32 *)&lbl_804F10C0[7] + 2);
    buf[24] = *(u32 *)&lbl_804F10C0[8];
    buf[25] = *((u32 *)&lbl_804F10C0[8] + 1);
    buf[26] = *((u32 *)&lbl_804F10C0[8] + 2);

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
