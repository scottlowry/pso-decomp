// f3 lane offline probe: pure-C replica of draw_compass__13TRaderMapCoreFv (VARIANTS edited by gen script)
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
s32 apply_compass_param__13TRaderMapCoreFv(void *);
void begin_effect_render__13TParticleCtrlFv(void);
void end_effect_render__13TParticleCtrlFv(void);
void set_default_alpha_blend__Fv(void);
void set_additive_blend__Fv(void);
void draw_compass_sprite__10TObjPlayerFlllf(void *, s32, s32, s32, f32);

void draw_compass__13TRaderMapCoreFv(RM *self, s32 mode) {
    CS state;
    u32 color;

    if (apply_compass_param__13TRaderMapCoreFv((void *)&self->m_90) == 0) {
        return;
    }
    state.x = TRaderMapCore__data_805DC528;
    state.y = TRaderMapCore__data_805DC528;
    state.z = TRaderMapCore__data_805DC528;
    state.sx = TRaderMapCore__data_805DC534;
    state.sy = TRaderMapCore__data_805DC534;
    state.rot = 0;
    state.unk18 = TRaderMapCore__data_805D5F4C;
    state.sprs = lbl_804C87E4;
    color = -1;
    begin_effect_render__13TParticleCtrlFv();
    f32 *tbl = lbl_804C87B4[mode];
    state.x = (f32)lbl_804C87E4[1].x + tbl[2];
    state.y = (f32)lbl_804C87E4[1].y + tbl[3];
    set_default_alpha_blend__Fv();
    ((u8 *)&color)[3] = (u8)(s32)self->m_19c;
    draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 1, (s32)((color << 16) | (color >> 16)), 0x21, TRaderMapCore__data_805DC58C);
    state.x = (f32)lbl_804C87E4[0].x + tbl[0];
    state.y = (f32)lbl_804C87E4[0].y + tbl[1];
    state.rot = self->m_174;
    set_additive_blend__Fv();
    draw_compass_sprite__10TObjPlayerFlllf((void *)&state, 0, -1, 0x21, TRaderMapCore__data_805DC58C);
    end_effect_render__13TParticleCtrlFv();
}
}
