// Mirror of TBoss7TentacleNeedle__ct (0x802EFD08, 416B) — single-fn probe base.
// BASE-VERIFY gate: raw .text words must equal repo .o __ct block 0-diff.
#include "types.h"

struct V_802F0A5C { f32 x, y, z; };
struct RecoveredGlobal_802EFB1C_lbl_80541918 { s32 value; u8 remaining[0xC]; };

extern "C" {
void __ct__7TObjectFP7TObject(void *, void *);
void *create_particle_emitter(void *pos, s32 id);
s32 rand(void);
extern s32 __vt__20TBoss7TentacleNeedle[];
extern s32 boss7_tentacle_needle_name_ptr;
extern const f32 lbl_805DEC20;
extern const f32 lbl_805DEC24;
extern const f32 lbl_805DEC28;
extern const f32 lbl_805DEC2C;
extern const f32 lbl_805DEC30;
extern const f32 TBoss7Tentacle__data_805DEC04;
extern RecoveredGlobal_802EFB1C_lbl_80541918 boss7_tentacle_needle_target_state;

struct TBoss7TentacleNeedle;
struct Arr_802EFD08 { u8 pad[0x44]; s32 a[12]; };

#pragma push
#pragma fp_contract on
u8 *TBoss7TentacleNeedle__ct(TBoss7TentacleNeedle *self, void *parent, V_802F0A5C *pos) {
    __ct__7TObjectFP7TObject((void *)self, parent);
    *(s32 **)((s8 *)self + 0x18) = __vt__20TBoss7TentacleNeedle;
    *(s32 *)((s8 *)self + 0x0) = boss7_tentacle_needle_name_ptr;
    *(f32 *)((s8 *)self + 0x34) = lbl_805DEC20;
    *(s32 *)((s8 *)self + 0x28) = 0;
    *(s32 *)((s8 *)self + 0x2C) = (s32)(lbl_805DEC24 * (lbl_805DEC28 * (f32)rand()));
    *(s32 *)((s8 *)self + 0x30) = 0;
    *(f32 *)((s8 *)self + 0x1C) = lbl_805DEC2C * (lbl_805DEC28 * (f32)rand()) + pos->x - lbl_805DEC30;
    *(f32 *)((s8 *)self + 0x20) = pos->y;
    *(f32 *)((s8 *)self + 0x24) = lbl_805DEC2C * (lbl_805DEC28 * (f32)rand()) + pos->z - lbl_805DEC30;
    *(s32 *)((s8 *)self + 0x38) = 0;
    *(s32 *)((s8 *)self + 0x3C) = 0;
    s32 w0; s32 w1; s32 w2; s32 v[3];
    w1 = ((s32 *)pos)[1];
    w0 = ((s32 *)pos)[0];
    w2 = ((s32 *)pos)[2];
    v[0] = w0;
    v[1] = w1;
    v[2] = w2;
    *(s32 *)((s8 *)self + 0x40) = (s32)create_particle_emitter(v, 0x212);
    for (s32 i = 0; i < 12; i++) {
        ((Arr_802EFD08 *)self)->a[i] = 0;
    }
    *(s32 *)((s8 *)self + 0x78) = boss7_tentacle_needle_target_state.value;
    *(f32 *)((s8 *)self + 0x74) = TBoss7Tentacle__data_805DEC04;
    return (u8 *)self;
}
#pragma pop
}
