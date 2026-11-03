#include "types.h"
#include "pso/TObject.h"
#include "pso/system/vector.h"

extern "C" {
u16 get_entity_id(void *);
s32 VecCopy__FP3VecPC3Vec(int, void *);
}

extern const f32 lbl_805DEA10[1];
extern const f32 lbl_805DEA18[1];
#define lbl_805DEA10 (lbl_805DEA10[0])
#define lbl_805DEA18 (lbl_805DEA18[0])

struct Boss_802E7CC4 { u8 pad[0x7A4]; TObject *group; };

extern "C" {
void TObjFish__sub_802E7D70(void *self, s16 arg1, void *arg2, void *arg3, s32 arg4);
}

extern "C" {
u8 *TBoss7Crawfish__ct(u8 *a0, u8 *a1, u8 *a2);
u32 __nw__7TObjectFUl(int);
}

struct Stack_802E7D70 {
    u16 sp8;
    u16 spA;
    u16 spC;
    u16 spE;
    u16 sp10;
    u16 sp12;
    u16 sp14;
    u16 sp16;
    f32 sp18;
    f32 sp1C;
    f32 sp20;
    f32 sp24;
    f32 sp28;
    f32 sp2C;
    f32 sp30;
    f32 sp34;
    f32 sp38;
    f32 sp3C;
    f32 sp40;
    u16 sp44;
    u16 sp46;
};

void TObjFish__sub_802E7D70(void *self, s16 arg1, void *arg2, void *arg3, s32 arg4) {
    Stack_802E7D70 block;
    s16 rel;
    s16 f2c;
    u16 target;
    TObject *child;
    u32 spawned;

    if (((Boss_802E7CC4 *)self)->group == NULL) {
        return;
    }
    if (arg1 <= 0) {
        return;
    }
    rel = arg1;
    rel += 11;
    target = (u16)(get_entity_id(self) + rel);
    for (child = ((Boss_802E7CC4 *)self)->group->m_down; child != NULL; child = child->m_next) {
        if (get_entity_id(child) == target) {
            return;
        }
    }
    f2c = *(s16 *)((u8 *)self + 0x2c);
    block.sp8 = (u16)(f2c + rel);
    block.spA = 1;
    block.spC = 0;
    block.spE = target;
    block.sp10 = (u16)*(s16 *)((u8 *)self + 0x28);
    block.sp12 = 0;
    block.sp14 = 0;
    block.sp16 = 0;
    ((void (*)(void *, void *))VecCopy__FP3VecPC3Vec)(&block.sp18, arg2);
    copy_xyz(&block.sp24, arg3);
    if (arg4 & 1) {
        block.sp30 = lbl_805DEA10;
    } else {
        block.sp30 = lbl_805DEA18;
    }
    block.sp34 = lbl_805DEA10;
    block.sp38 = lbl_805DEA10;
    block.sp3C = lbl_805DEA10;
    block.sp40 = lbl_805DEA10;
    block.sp44 = 0;
    block.sp46 = 0;
    spawned = __nw__7TObjectFUl(0x3d0);
    if (spawned != 0U) {
        TBoss7Crawfish__ct((u8 *)spawned, (u8 *)((Boss_802E7CC4 *)self)->group, (u8 *)&block);
    }
}

#undef lbl_805DEA10
__declspec(section ".sdata2") const f32 lbl_805DEA10[1] = { 0.0f };
#define lbl_805DEA10 (lbl_805DEA10[0])
#undef lbl_805DEA18
__declspec(section ".sdata2") const f32 lbl_805DEA18[1] = { 1.0f };
#define lbl_805DEA18 (lbl_805DEA18[0])
