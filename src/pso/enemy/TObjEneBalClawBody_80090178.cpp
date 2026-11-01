#include "types.h"
#include "pso/enemy/TObjEneBalClawClaw.h"
#include "pso/player/TObjPlayer.h"
#include "pso/enemy/TObjEneBalClaw.h"
#include "pso/enemy/TObjEneBalClawBody.h"
struct E_80090418 { u8 pad[8]; s32 x8; s32 xc; };

struct G_80090418 { u8 pad[0x42c]; E_80090418 *tbl; };

struct O_80090418 { u8 pad[0x24]; s32 x24; u8 pad2[0xc]; s32 x34; };

struct Body_80090178 {
    u8 pad0[0x18];
    void *vtable;
    u8 pad1C[0x3C4 - 0x1C];
    s32 ids[5];
    s16 count;
    u8 pad3DA[2];
    void *parts[4];
};

extern "C" {
extern G_80090418 *lbl_805D4F20;
void queue_destruction__7TObjectFv(void *);
void *__dt__14TObjEneBalClawFv(void *arg0, s16 arg1);
void *find_entity_by_id(u16);
void free_collision_body_parts(void *);
void __dl__7TObjectFPv(void *);
extern u8 lbl_8048EF0C[];
Body_80090178 *TObjEneBalClawBody__sub_80090178(Body_80090178 *self, s16 flag);


extern s32 lbl_805D2970;
extern u8 lbl_8048EDE8[];
extern u8 lbl_805007A8[];
extern f32 lbl_805D9620;
extern f32 lbl_805D9680;
extern f32 lbl_805D9684;

void *VecCopy__FP3VecPC3Vec(void *, void *);
void set_field_d8__10TObjMotionFl(void *, s32);
void init_collision_body_parts(void *, void *, s32);
void set_animation__10TObjMotionFs(void *, s16);
void set_field_b8__10TObjMotionFs(void *, s16);
void update_prev_position__9TObjEnemyFv(void *);
void initialize_enemy_photon_effect__FPv(void *);
void clear_attack_flag__14TObjEneBalClawFv(void *);
void sub_800C7860__15TObjEnemyCustomFv(void *);
void TObjPlayer__sub_8008E934(void *, s32);
void bind_enemy_combat_stats__9TObjEnemyFPUcPUcPUc(void *, u8 *, u8 *, u8 *);

#pragma opt_propagation off
void *TObjEneBalClawBody__ct(void *self, void *arg1, void *arg2) {
    s8 *b = (s8 *)self;
    u8 *stats = lbl_805007A8;
    s32 i;
    f32 ph;
    u8 *edata = lbl_8048EDE8;

    (void)TObjEneBalClaw__ct((TObjEneBalClaw *)self);
    *(s32 **)(b + 0x18) = (s32 *)(edata + 0x124);
    *(s32 *)b = lbl_805D2970;
    ((TObjEneBalClawBody *)self)->apply_set_data(arg2);
    VecCopy__FP3VecPC3Vec(b + 0x290, VecCopy__FP3VecPC3Vec(b + 0x29c, b + 0x38));
    *(s32 *)(b + 0xdc) = *(s32 *)((u8 *)lbl_805D4F20 + 0x430);
    *(s32 *)(b + 0xd8) = (s32)edata;
    set_field_d8__10TObjMotionFl(self, *(s32 *)(b + 0xd8));
    init_collision_body_parts(self, edata + 0xf8, 1);
    *(s16 *)(b + 0xb8) = 0;
    set_animation__10TObjMotionFs(self, *(s16 *)(b + 0xb8));
    set_field_b8__10TObjMotionFs(self, *(s16 *)(b + 0xb8));
    *(s16 *)(b + 0x32c) = *(s16 *)(b + 0x2b8);
    *(s16 *)(b + 0x32e) = *(s16 *)(b + 0x2ba);
    *(s16 *)(b + 0x33e) = *(s16 *)(b + 0x32c);
    update_prev_position__9TObjEnemyFv(self);
    initialize_enemy_photon_effect__FPv(self);
    ph = lbl_805D9620;
    *(s32 *)(b + 0x3b8) = 0;
    *(f32 *)(b + 0x3bc) = ph;
    clear_attack_flag__14TObjEneBalClawFv(self);
    if (*(s16 *)((s8 *)arg2 + 0xa) != 0) {
        sub_800C7860__15TObjEnemyCustomFv(self);
    }
    *(f32 *)(b + 0x3ac) = lbl_805D9680;
    *(f32 *)(b + 0x3b0) = lbl_805D9684;
    *(f32 *)(b + 0x3b4) = *(f32 *)(b + 0x3ac);
    *(s16 *)(b + 0x3d8) = 4;
    for (i = 0; i < 4; i++) {
        *(u32 *)(b + 0x3c4 + 4 * i) = 0xFFFF;
    }
    TObjPlayer__sub_8008E934(self, 1);
    bind_enemy_combat_stats__9TObjEnemyFPUcPUcPUc(self, *(u8 **)(stats), *(u8 **)(stats + 8), *(u8 **)(stats + 0x10));
    *(s32 *)(b + 0x3dc) = 0;
    *(s32 *)(b + 0x3e0) = 0;
    *(s32 *)(b + 0x3e4) = 0;
    *(s32 *)(b + 0x3e8) = 0;
    ((TObjEneBalClawBody *)self)->clear_lobby_object_state();
    return self;
}
#pragma opt_propagation reset

Body_80090178 *TObjEneBalClawBody__sub_80090178(Body_80090178 *self, s16 flag) {
    s32 i;
    void *p;
    if (self != NULL) {
        self->vtable = lbl_8048EF0C;
        free_collision_body_parts(self);
        if (self->parts[0] != NULL) {
            queue_destruction__7TObjectFv(self->parts[0]);
        }
        if (self->parts[1] != NULL) {
            queue_destruction__7TObjectFv(self->parts[1]);
        }
        if (self->parts[2] != NULL) {
            queue_destruction__7TObjectFv(self->parts[2]);
        }
        if (self->parts[3] != NULL) {
            queue_destruction__7TObjectFv(self->parts[3]);
        }
        if (((TObjPlayer *)self)->get_flag_0x388_b24() != 0) {
            for (i = 0; i < self->count; i++) {
                p = find_entity_by_id(self->ids[i]);
                if (p != NULL) {
                    queue_destruction__7TObjectFv(p);
                }
            }
        }
        __dt__14TObjEneBalClawFv(self, 0);
        if (flag > 0) {
            __dl__7TObjectFPv(self);
        }
    }
    return self;
}

void TObjEneBalClawClaw::sub_80090418(s32 i) {
    O_80090418 *self = (O_80090418 *)this;
    self->x34 = lbl_805D4F20->tbl[i].x8;
    self->x24 = lbl_805D4F20->tbl[i].xc;
}

}
