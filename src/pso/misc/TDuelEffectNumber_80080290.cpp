#include "types.h"
#include "pso/TDuelEffectNumber.h"
#include "pso/misc/TCameraCtrl.h"
#include "pso/misc/TWindowSubStatusDisp_803DEE6C.h"

struct RecoveredGlobal_80080438_lbl_80438DD4 {
    s32 value;
    u8 remaining[0x14];
};

struct Entry_800803D4 { u8 data[0x18]; };

extern "C" {
void TDuelEffectNumber__sub_800802F8(void *, void *, f32);
f32 get_scale__15TWindowCtrlMainFv(s32);
extern const f32 lbl_805D9308;
extern const f32 lbl_805D930C;
extern RecoveredGlobal_80080438_lbl_80438DD4 duel_number_default_layout;
extern Entry_800803D4 duel_number_pair_layout[];
}

extern void *TDuelEffectNumber__class_name;
TDuelEffectNumber::TDuelEffectNumber(TObject *object, void *arg2, void *arg3) : TObject(object) {
    *(void * *)&this->m_name = TDuelEffectNumber__class_name;
    *(f32 *)((s8 *)this + 0x1C) = *(f32 *)((s8 *)arg2 + 0x0);
    *(f32 *)((s8 *)this + 0x20) = *(f32 *)((s8 *)arg2 + 0x4);
    *(void **)((s8 *)this + 0x24) = arg3;
    *(u32 *)((s8 *)this + 0x28) = 0;
}

typedef char RecoveredGlobal_80080438_lbl_80438DD4_size[sizeof(RecoveredGlobal_80080438_lbl_80438DD4) == 0x18 ? 1 : -1];

#pragma push
#pragma fp_contract on
void TDuelEffectNumber__sub_800802F8(void *self, void *layout, f32 f)
{
  f32 q[8];
  f32 *l = (f32 *) layout;
  s8 *new_var2;
  get_scale__15TWindowCtrlMainFv(TCameraCtrl::get_camera_no());
  f32 d = lbl_805D9308 / f;
  float new_var;
  f32 l0 = l[0];
  new_var2 = (s8 *) self;
  f32 cx = *((f32 *) (new_var2 + 0x1C));
  f32 l4 = l[4];
  f32 l5 = l[5];
  f32 l3 = l[3];
  f32 cy;
  f32 l2 = l[2];
  f32 u1;
  f32 u2 = l4 + l2;
  f32 u3 = l5 + l3;
  new_var = (f * l0) + cx;
  f32 l1 = l[1];
  f32 t0 = l1 + l3;
  u1 = l0 + l2;
  if ((l && l) && l)
  {
  }
  q[0] = new_var;
  cy = *((f32 *) (((s8 *) self) + 0x20));
  q[1] = (l1 * f) + cy;
  q[2] = (f * u1) + cx;
  q[3] = (f * t0) + cy;
  if (!l5)
  {
  }
  q[4] = l4;
  q[5] = l5;
  q[5] *= lbl_805D930C;
  q[6] = u2;
  q[6] = q[6] * lbl_805D930C;
  q[7] = u3;
  q[4] = q[4] * lbl_805D930C;
  q[7] *= lbl_805D930C;
  if (!q)
  {
  }
  draw_textured_quad_at_depth(q, d);
}
#pragma pop

void TDuelEffectNumber::render_pair(f32 f) {
    s32 i;
    for (i = 0; i < 2; i++) {
        TDuelEffectNumber__sub_800802F8(this, &duel_number_pair_layout[i], f);
    }
}

void TDuelEffectNumber::render_number_default(f32 farg0) {
    u8 *arg0 = (u8 *)this;
    TDuelEffectNumber__sub_800802F8(arg0, &duel_number_default_layout.value, farg0);
}
