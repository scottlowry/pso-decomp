// v11: explicit f64 double-staging with named extern bias + per-block bp remat,
//     tbl-operand-left adds (orig fadds order), twin color expr, declflip2 fill.
typedef unsigned char u8; typedef unsigned short u16; typedef unsigned int u32; typedef unsigned long u64;
typedef signed char s8; typedef short s16; typedef int s32; typedef long s64;
typedef float f32; typedef double f64;

struct RM { u8 pad0[0x90]; s32 m_90; u8 pad94[0xE0]; s32 m_174; u8 pad178[0x24]; f32 m_19c; };
struct SF { s16 w, h, x, y, u0, v0, u1, v1, a, b; };
struct CS { f32 x, y, z, sx, sy; s32 rot; u32 unk18; SF *sprs; };

extern "C" {
extern const f32 TRaderMapCore__data_805DC528;
extern const f32 TRaderMapCore__data_805DC534;
extern const f32 TRaderMapCore__data_805DC58C;
extern u32 TRaderMapCore__data_805D5F4C;
extern SF lbl_804C87E4[];
extern f32 lbl_804C87B4[][4];
extern const f64 lbl_8044A7A8;
s32 apply_compass_param__13TRaderMapCoreFv(void *);
void begin_effect_render__13TParticleCtrlFv(void);
void end_effect_render__13TParticleCtrlFv(void);
void set_default_alpha_blend__Fv(void);
void set_additive_blend__Fv(void);
void draw_compass_sprite__10TObjPlayerFlllf(void *, s32, s32, s32, f32);

#pragma push
#pragma fp_contract off
void draw_compass__13TRaderMapCoreFv(RM *self, s32 mode) {
    u32 b2y[2];
    u32 b2x[2];
    u32 b1y[2];
    u32 b1x[2];
    CS state;
    u32 color;
    f32 b;
    f32 a;
    const f64 *bp;
    f64 cx;
    f64 cy;
    f32 *tbl;

    if (apply_compass_param__13TRaderMapCoreFv((void *)&self->m_90) == 0) {
        return;
    }
    b = TRaderMapCore__data_805DC534;
    a = TRaderMapCore__data_805DC528;
    state.x = a;
    state.y = a;
    state.z = a;
    state.sx = b;
    state.sy = b;
    state.rot = 0;
    state.unk18 = TRaderMapCore__data_805D5F4C;
    state.sprs = lbl_804C87E4;
    color = -1;
    begin_effect_render__13TParticleCtrlFv();
    tbl = lbl_804C87B4[mode];
    bp = &lbl_8044A7A8;
    b1x[0] = 0x43300000U;
    b1x[1] = (u32)(s32)lbl_804C87E4[1].x ^ 0x80000000U;
    b1y[0] = 0x43300000U;
    b1y[1] = (u32)(s32)lbl_804C87E4[1].y ^ 0x80000000U;
    cx = *(f64 *)b1x - *bp;
    cy = *(f64 *)b1y - *bp;
    state.x = tbl[2] + cx;
    state.y = tbl[3] + cy;
    set_default_alpha_blend__Fv();
    ((u8 *)&color)[3] = (u8)(s32)self->m_19c;
    draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 1,
        (s32)(((((color >> 16U) & ~0xFF000000U) | ((color << 16) & 0xFF000000U)) & (~0xFF0000U)) | ((color << 16) & 0xFF0000U)),
        0x21, TRaderMapCore__data_805DC58C);
    bp = &lbl_8044A7A8;
    b2x[0] = 0x43300000U;
    b2x[1] = (u32)(s32)lbl_804C87E4[0].x ^ 0x80000000U;
    b2y[0] = 0x43300000U;
    b2y[1] = (u32)(s32)lbl_804C87E4[0].y ^ 0x80000000U;
    cx = *(f64 *)b2x - *bp;
    cy = *(f64 *)b2y - *bp;
    state.x = tbl[0] + cx;
    state.y = tbl[1] + cy;
    state.rot = self->m_174;
    set_additive_blend__Fv();
    draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 0, -1, 0x21, TRaderMapCore__data_805DC58C);
    end_effect_render__13TParticleCtrlFv();
}
#pragma pop
}
