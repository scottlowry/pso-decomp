#include "types.h"
#include "pso/TMath.h"
#include "pso/ui/UISprite.h"

struct VBase_802A2A00 { char pad[0x18]; };

struct OccHeader_802A2A00 : VBase_802A2A00 {
    virtual void m0();
    virtual void m1();
    virtual void m2();
    virtual void m3();
    virtual s32 m4();
    s32 f1c;
    s32 f20;
    f32 f24;
    u8 pad28[0x30 - 0x28];
    f32 f30;
    u8 pad34[0x3C - 0x34];
    s32 f3c;
};

extern "C" {
void draw_ui_sprite_shaded(s32 sprite_id, const vec2f *position, const vec2f *scale,
                           f32 depth, f32 alpha, f32 brightness);
f32 sin_table_lookup(s32);
extern vec2f lbl_80466454[];
extern const f32 lbl_805DDEA8;
extern const f32 lbl_805DDEAC;
extern const f32 lbl_805DDEB0;
extern f32 lbl_805DDEB4;
extern f32 lbl_805DDEB8;
extern const f32 lbl_805DDEBC;
extern const f32 lbl_805DDEC0;
extern const f32 lbl_805DDEC4;
extern const f32 lbl_805DDEC8;

#pragma push
#pragma fp_contract on
void fn_802A2A00(void *p) {
    OccHeader_802A2A00 *self = (OccHeader_802A2A00 *)p;
    vec2f pos = lbl_80466454[0];
    f32 prog = self->f24 * self->f30;
    if (prog <= lbl_805DDEA8) {
        return;
    }
    f32 depth = self->m4() != 0 ? lbl_805DDEAC : lbl_805DDEB0;
    f32 alpha = lbl_805DDEB4;
    alpha = prog / alpha;
    alpha = alpha * alpha;
    f32 cap = lbl_805DDEB8;
    if (alpha > cap) {
        alpha = cap;
    }
    vec2f scale;
    f32 lim = lbl_805DDEB4;
    f32 sv = lbl_805DDEB8;
    scale.y = sv;
    scale.x = sv;
    if (prog < lim) {
        f32 k = (lim - prog) / lim;
        f32 adj = lbl_805DDEBC * k;
        sv = sv + adj;
        scale.x = sv;
        scale.y = sv;
    }
    s32 id = self->f20 < 3 ? self->f20 + 99 : (self->f20 - 3) / 4 + 99;
    draw_ui_sprite_shaded(id, &pos, &scale, depth, alpha, lbl_805DDEB8);
    if (self->m4() == 0) {
        return;
    }
    if (!(prog <= lbl_805DDEB4)) {
        f32 p2 = (prog - lbl_805DDEB4) / lbl_805DDEC0;
        s32 id2 = self->f20 < 3 ? self->f20 + 173 : self->f20 - 3 + 176;
        if (self->m4() != 0) {
            p2 = lbl_805DDEC4 * sin_table_lookup(self->f3c << 9) + p2;
            if (p2 < lbl_805DDEA8) {
                p2 = lbl_805DDEA8;
            } else if (p2 > lbl_805DDEB8) {
                p2 = lbl_805DDEB8;
            }
            draw_ui_sprite_shaded(id2, &pos, &scale, lbl_805DDEC8, p2, lbl_805DDEB8);
        }
    }
}
#pragma pop
}
