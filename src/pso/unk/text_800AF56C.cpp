#include "types.h"
#include <stddef.h>
#include "pso/unk/text_800AF56C.h"
#include "pso/misc/SampledMotionPoints.h"
struct TObjEnemy;
#include "pso/object/TObject_80019A50.h"

struct Stack_800AF56C {
    s32 sp8;
    s32 spC;
    s32 sp10;
    s32 sp14;
    s32 sp18;
    s32 sp1C;
    f32 sp20;
    f32 sp24;
    f32 sp28;
    f32 sp2C;
    f32 sp30;
    f32 sp34;
};

typedef char sp8_offset[(offsetof(Stack_800AF56C, sp8) == 0x0) ? 1 : -1];
typedef char spC_offset[(offsetof(Stack_800AF56C, spC) == 0x4) ? 1 : -1];
typedef char sp10_offset[(offsetof(Stack_800AF56C, sp10) == 0x8) ? 1 : -1];
typedef char sp14_offset[(offsetof(Stack_800AF56C, sp14) == 0xC) ? 1 : -1];
typedef char sp18_offset[(offsetof(Stack_800AF56C, sp18) == 0x10) ? 1 : -1];
typedef char sp1C_offset[(offsetof(Stack_800AF56C, sp1C) == 0x14) ? 1 : -1];
typedef char sp20_offset[(offsetof(Stack_800AF56C, sp20) == 0x18) ? 1 : -1];
typedef char sp24_offset[(offsetof(Stack_800AF56C, sp24) == 0x1C) ? 1 : -1];
typedef char sp28_offset[(offsetof(Stack_800AF56C, sp28) == 0x20) ? 1 : -1];
typedef char sp2C_offset[(offsetof(Stack_800AF56C, sp2C) == 0x24) ? 1 : -1];
typedef char sp30_offset[(offsetof(Stack_800AF56C, sp30) == 0x28) ? 1 : -1];
typedef char sp34_offset[(offsetof(Stack_800AF56C, sp34) == 0x2C) ? 1 : -1];

extern "C" {
void *__dt__9TObjEnemyFv(TObjEnemy *arg0, s16 arg1);
void free_collision_body_parts(void *);
void __dl__7TObjectFPv(s32);
s32 __destroy_arr(void *, void *, int, int);
extern s32 __dt__15RenderFadeStateFv[];
extern s32 __vt__11TObjEneMoja[];
u8 *__dt__11TObjEneMojaFv(u8 *arg0, s16 arg1) {
    u8 *object;
    if (arg0 != NULL) {
        *(s32 **)((s8 *)arg0 + 0x18) = __vt__11TObjEneMoja;
        object = (u8 *)(*(u8 **)((s8 *)arg0 + 0x398));
        if (object != NULL) {
            queue_destruction__7TObjectFv(object);
            *(u8 **)((s8 *)arg0 + 0x398) = NULL;
        }
        free_collision_body_parts(arg0);
        __destroy_arr(arg0 + 0x39C, __dt__15RenderFadeStateFv, 0x1C, 4);
        __dt__9TObjEnemyFv((TObjEnemy *)arg0, 0);
        if (arg1 > 0) {
            __dl__7TObjectFPv((s32) arg0);
        }
    }
    return arg0;
}

u8 *load_resource_from_descriptor(void *, s32, void *, s32, s32, s32);
s32 mem_alloc(s32);
s32 register_boss__6TLobbyFl(s32);
s32 register_object__6TLobbyFl(s32);
s32 dispatch_shared_handler_a__6TLobbyFl(s32);
s32 dispatch_shared_handler_b__6TLobbyFl(s32);
s32 spawn_npc_enemy__6TLobbyFsllPvff(s16, s32, s32, void *, f32, f32);
extern s32 game_difficulty_selection;
extern s8 lbl_80491828[];
extern s32 lbl_8043B09C[];
extern s32 lbl_8043B0A4[];
extern s32 lbl_805D50C8;
extern s32 lbl_805D50CC;
extern s32 lbl_805D50D0;
extern s32 lbl_805D50D4;
extern s32 lbl_805D50D8;
extern s32 lbl_805D50DC;
extern f32 lbl_805D9BD8;
extern f32 lbl_805D9BF8;
extern f32 lbl_805D9C28;
extern f32 lbl_805D9C2C;
extern f32 lbl_805D9C5C;

void load_resources__11TObjEneMojaFv(void) {
    s8 *desc;
    u8 *r;
    u8 *res;
    u8 *ents;
    u8 *tbl;
    s8 *mp;
    s16 *ids;
    s32 off;
    s32 i;
    Stack_800AF56C stack;

    desc = lbl_80491828;
    if (game_difficulty_selection == 3) {
        r = (u8 *)::operator new(0x440);
        if (r != NULL) {
            r = load_resource_from_descriptor(r, 1, desc + 0x90, 0, 0, 0);
        }
        lbl_805D50D8 = (s32)r;
    } else {
        r = (u8 *)::operator new(0x440);
        if (r != NULL) {
            r = load_resource_from_descriptor(r, 1, desc + 0x40, 0, 0, 0);
        }
        lbl_805D50D8 = (s32)r;
    }
    r = (u8 *)new SampledMotionPoints(2, lbl_805D9C28, lbl_805D9C2C, lbl_805D9C5C);
    lbl_805D50DC = (s32)r;
    mp = desc + 0xa0;
    res = (u8 *)lbl_805D50D8;
    stack.sp2C = stack.sp30 = stack.sp34 = lbl_805D9BD8;
    stack.sp20 = lbl_805D9BF8;
    stack.sp24 = lbl_805D9BD8;
    stack.sp28 = lbl_805D9BD8;
    ents = *(u8 **)(res + 0x430);
    tbl = *(u8 **)(res + 0x42c);
    ((SampledMotionPoints *)r)->sample_node_offsets((NJS_OBJECT *)*(s32 *)(tbl + 0x18),
                                                    (NJS_MOTION *)(*(s32 *)(ents + *(s32 *)(mp + 0x34) * 8 + 4)),
                                                    0x26, (const Vec *)&stack.sp2C, (const Vec *)&stack.sp20);
    lbl_805D50C8 = mem_alloc(8);
    lbl_805D50CC = mem_alloc(0x18);
    lbl_805D50D0 = mem_alloc(8);
    lbl_805D50D4 = mem_alloc(8);
    ((s32 *)lbl_805D50C8)[0] = register_boss__6TLobbyFl(0x49);
    ((s32 *)lbl_805D50C8)[1] = register_boss__6TLobbyFl(0x4a);
    ((s32 *)lbl_805D50CC)[0] = dispatch_shared_handler_b__6TLobbyFl(0x48);
    ((s32 *)lbl_805D50CC)[1] = dispatch_shared_handler_b__6TLobbyFl(0x49);
    ((s32 *)lbl_805D50CC)[2] = dispatch_shared_handler_b__6TLobbyFl(0x4a);
    ((s32 *)lbl_805D50CC)[3] = dispatch_shared_handler_b__6TLobbyFl(0x4b);
    ((s32 *)lbl_805D50CC)[4] = dispatch_shared_handler_b__6TLobbyFl(0x4c);
    ((s32 *)lbl_805D50CC)[5] = dispatch_shared_handler_b__6TLobbyFl(0x4d);
    ((s32 *)lbl_805D50D0)[0] = register_object__6TLobbyFl(0x48);
    ((s32 *)lbl_805D50D0)[1] = register_object__6TLobbyFl(0x49);
    ((s32 *)lbl_805D50D4)[0] = dispatch_shared_handler_a__6TLobbyFl(0x48);
    ((s32 *)lbl_805D50D4)[1] = dispatch_shared_handler_a__6TLobbyFl(0x49);
    desc = desc + 0x168;
    ids = (s16 *)&stack;
    stack.sp10 = lbl_8043B0A4[0];
    stack.sp14 = lbl_8043B0A4[1];
    stack.sp18 = lbl_8043B0A4[2];
    stack.sp1C = lbl_8043B0A4[3];
    stack.sp8 = lbl_8043B09C[0];
    *(s16 *)&stack.spC = *(s16 *)(lbl_8043B09C + 1);
    stack.sp10 = *(s32 *)((u8 *)lbl_805D50D8 + 0x430);
    off = 0;
    for (i = 0; i < 3; i++) {
        tbl = *(u8 **)((u8 *)lbl_805D50D8 + 0x42c);
        spawn_npc_enemy__6TLobbyFsllPvff(ids[i], *(s32 *)(tbl + off + 8),
                                        *(s32 *)(tbl + off + 0xc), &stack.sp10,
                                        ((f32 *)desc)[3], lbl_805D9BD8);
        off += 0x10;
    }
}

}
