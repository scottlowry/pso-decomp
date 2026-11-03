
typedef unsigned char u8;
typedef signed short s16;
typedef signed long s32;
typedef unsigned long u32;
typedef signed long long s64;
typedef unsigned long long u64;
typedef float f32;
typedef double f64;
typedef struct RM
{
  u8 pad0[0x90];
  s32 m_90;
  u8 pad94[0xE0];
  s32 m_174;
  u8 pad178[0x24];
  f32 m_19c;
} RM;
typedef struct SF
{
  s16 w;
  s16 h;
  s16 x;
  s16 y;
  s16 u0;
  s16 v0;
  s16 u1;
  s16 v1;
  s16 a;
  s16 b;
} SF;
typedef struct CS
{
  f32 x;
  f32 y;
  f32 z;
  f32 sx;
  f32 sy;
  s32 rot;
  u32 unk18;
  SF *sprs;
} CS;
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
void draw_compass__13TRaderMapCoreFv(RM *self, s32 mode)
{
  u32 new_var;
  CS state;
  u32 color;
  new_var = ~0xFF000000;
  if (apply_compass_param__13TRaderMapCoreFv((void *) (&self->m_90)) == 0)
  {
    return;
  }
  f32 b = TRaderMapCore__data_805DC534;
  f32 a = TRaderMapCore__data_805DC528;
  state.x = a;
  state.y = a;
  state.z = a;
  state.sx = b;
  state.sy = b;
  state.rot = 0;
  state.sprs = lbl_804C87E4;
  TRaderMapCore__data_805D5F4C = TRaderMapCore__data_805D5F4C;
  state.unk18 = TRaderMapCore__data_805D5F4C;
  color = -1;
  begin_effect_render__13TParticleCtrlFv();
  f32 *tbl = lbl_804C87B4[mode];
  state.x = tbl[2] + ((f32) lbl_804C87E4[1].x);
  state.y = tbl[3] + ((f32) lbl_804C87E4[1].y);
  self->m_19c = self->m_19c;
  set_default_alpha_blend__Fv();
  ((u8 *) (&color))[3] = (u8) ((s32) self->m_19c);
  draw_compass_sprite__10TObjPlayerFlllf((void *) (&state), 1, (s32) (((((color >> 0x10U) & new_var) | ((color << 0x10) & 0xFF000000)) & (~0xFF0000)) | ((color << 0x10) & 0xFF0000)), 0x21, TRaderMapCore__data_805DC58C);
  state.x = tbl[0] + ((f32) lbl_804C87E4[0].x);
  state.y = tbl[1] + ((f32) lbl_804C87E4[0].y);
  state.rot = self->m_174;
  set_additive_blend__Fv();
  draw_compass_sprite__10TObjPlayerFlllf((void *) (&state), 0, -1, 0x21, TRaderMapCore__data_805DC58C);
  end_effect_render__13TParticleCtrlFv();
}
