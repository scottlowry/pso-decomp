#include "types.h"
#include "pso/unk/text_802C6DD4.h"

extern "C" {
u8 * TAdChrSelPlyPlateGC__ct(void *, s32, s32);
u8 *__nw__7TObjectFUl(s32);
extern u8 *ad_chr_sel_ply_plate_instance;
u8 *fn_802C6F20(s32 arg0, s32 arg1) {
    u8 *temp_r3;
    u8 *var_r0;
    if ((void *) ad_chr_sel_ply_plate_instance != NULL) {
        return NULL;
    }
    temp_r3 = (u8 *)(__nw__7TObjectFUl(0x538));
    var_r0 = temp_r3;
    if (var_r0 != NULL) {
        var_r0 = (u8 *)(TAdChrSelPlyPlateGC__ct(temp_r3, arg0, arg1));
    }
    ad_chr_sel_ply_plate_instance = var_r0;
    return var_r0;
}


extern s32 lbl_805D3EE0[2];
extern s32 lbl_805D67D0;
extern s32 lbl_805D67D4;
extern s32 TAdMultiPlyChrSelectGC__select_mode;
extern s32 TAdMultiPlyChrSelectGC__selected_slot;
extern s32 TAdMultiPlyChrSelectGC__data_805D67D8;
extern f32 TAdMultiPlyChrSelectGC__data_805DE56C;
extern s32 tl_clipout;
extern u8 TAdMultiPlyChrSelectGC__data_804E0A48[];

s32 __ct__7TObjectFP7TObject(void *);
void copy_vec2__28TWindowSubSymbolChatPartsSetFPv(void *, void *);
s32 TAdMultiPlyChrSelectGC__sub_802C6FA8(void);
s32 get_global_6700__22TAdMultiPlyChrSelectGCFv(void);
void TAdMultiPlyChrSelectGC__sub_802C5F1C(void *);
void reset_slot_selection_table__22TAdMultiPlyChrSelectGCFv(void);
s32 get_instance__19TAdPlyPltAnimCtrlGCFl(s32);

#pragma push
#pragma opt_propagation off
u8 *TAdChrSelPlyPlateGC__ct(void *self, s32 arg1, s32 arg2) {
  s8 *base = (s8 *) self;
  s8 *d = (s8 *) TAdMultiPlyChrSelectGC__data_804E0A48;
  __ct__7TObjectFP7TObject(self);
  *((s32 **) (base + 0x18)) = (s32 *) (d + 0xc8);
  *((s32 *) self) = lbl_805D3EE0[0];
  lbl_805D67D0 = TAdMultiPlyChrSelectGC__sub_802C6FA8();
  lbl_805D67D4 = get_global_6700__22TAdMultiPlyChrSelectGCFv();
  TAdMultiPlyChrSelectGC__select_mode = 0;
  copy_vec2__28TWindowSubSymbolChatPartsSetFPv(base + 0x4a4, (void *) arg2);
  *((s32 *) (base + 0x1c)) = -1;
  *((s32 *) (base + 0x4e8)) = 0;
  TAdMultiPlyChrSelectGC__selected_slot = 0;
  TAdMultiPlyChrSelectGC__data_805D67D8 = 0;
  *((s32 *) (base + 0x4ec)) = 0;
  *((s32 *) (base + 0x4f0)) = 0;
  *((s32 *) (base + 0x4f4)) = 0;
  *((s32 *) (base + 0x4f8)) = 0;
  *((s32 *) (base + 0x4fc)) = 0;
  *((s32 *) (base + 0x20)) = TAdMultiPlyChrSelectGC__data_805D67D8;
  *((s32 *) (base + 0x534)) = 1;
  TAdMultiPlyChrSelectGC__sub_802C5F1C(self);
  f32 fv = TAdMultiPlyChrSelectGC__data_805DE56C;
  s32 *pz = (s32 *) (d + 0x98);
  f32 *pf = (f32 *) (d + 0xa8);
  for (unsigned long i = 0; i < 4; i++)
  {
    for (s32 j = 0; j < 3; j++)
    {
      *((s32 *) (((base + (4 * j)) + 0x474) + (12 * i))) = 0;
      *((s32 *) (((base + (4 * j)) + 0x444) + (12 * i))) = 0;
      *((s32 *) (((base + (4 * j)) + 0x500) - (-(12 * i)))) = 0;
      *((s32 *) (((base + (4 * j)) + 0x4ac) + (12 * i))) = 0;
      *((s32 *) (base + ((4 * j) + 0x4dc))) = 0;
    }

    pz[i] = 0;
    pf[i] = fv;
  }

  reset_slot_selection_table__22TAdMultiPlyChrSelectGCFv();
  get_instance__19TAdPlyPltAnimCtrlGCFl(tl_clipout);
  return (u8 *) self;
}
#pragma pop
}
