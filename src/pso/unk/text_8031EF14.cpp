#include "types.h"
#include "pso/enemy/TObjEneRecon.h"
#include "pso/enemy/TObjEneDD.h"
#include "pso/object/TObjChip.h"
struct Obj_8031EF14 { u8 pad[0x410]; s32 count; u8 pad2[4]; u16 ids[6]; };

struct Obj_8031F0F0 { u8 pad[0x410]; s32 count; u8 pad2[4]; u16 ids[6]; };

struct Obj_8031EFAC { u8 pad[0x410]; s32 count; s32 f414; u16 ids[6]; };

struct Obj_8031F070 { u8 pad[0x410]; s32 count; u8 pad2[4]; u16 ids[6]; };

extern "C" {
u8 *find_entity_by_id(u16);
u16 TObjEneRecon__sub_8031D878();
void remove_tracked_target__12TObjEneReconFPvPv(Obj_8031EFAC *o, u8 *target);
s32 is_anim_5__12TObjEneReconFv();
void TObjEneRecon::remove_child_entity(u8 *arg1) {
    Obj_8031EF14 *arg0 = (Obj_8031EF14 *)this;
    s32 i;
    for (i = 0; i < 6; i++) {
        if (find_entity_by_id(arg0->ids[i]) == arg1) {
            arg0->count--;
            arg0->ids[i] = arg0->ids[arg0->count];
            arg0->ids[arg0->count] = 0xFFFF;
            return;
        }
    }
}

void remove_tracked_target__12TObjEneReconFPvPv(Obj_8031EFAC *o, u8 *target) {
    s32 i;
    for (i = 0; i < 6; i++) {
        if (find_entity_by_id(o->ids[i]) == target) {
            ((TObjEneRecon *)o)->remove_tracked_id(o->ids[i]);
            o->count--;
            o->ids[i] = o->ids[o->count];
            o->ids[o->count] = 0xFFFF;
            o->f414--;
            if (o->f414 < 0) {
                o->f414 = 0;
            }
            return;
        }
    }
}

s32 TObjEneRecon::has_child_in_anim_5() {
    Obj_8031F070 *arg0 = (Obj_8031F070 *)this;
    s32 i;
    if (arg0->count <= 0) {
        return 0;
    }
    for (i = 0; i < 6; i++) {
        if (find_entity_by_id(arg0->ids[i]) != NULL && is_anim_5__12TObjEneReconFv() == 1) {
            return 1;
        }
    }
    return 0;
}

s32 TObjEneRecon::is_below_child_limit(u16 arg1) {
    Obj_8031F0F0 *arg0 = (Obj_8031F0F0 *)this;
    s32 n = 0;
    s32 i;
    for (i = 0; i < arg0->count; i++) {
        if (find_entity_by_id(arg0->ids[i]) != NULL && arg1 == TObjEneRecon__sub_8031D878()) {
            n++;
        }
    }
    if (TObjEneDD::check_v2_mode() != 0) {
        return n < 4;
    }
    return n < 2;
}

struct Rec_8031F1A8 { u8 pad[0x38]; f32 pos[3]; };

void *spawn_particle_effect_with_flags(void *pos, s32 id, s32 flags);
s32 __nw__7TObjectFUl(int);
extern u8 *tl_05;
extern u8 *TObjEneRecobox__static_instance;
extern TObjChipParams lbl_804762F0;
extern TObjChipParams lbl_8047633C;
extern TObjChipParams lbl_80476388;

void TObjEneRecobox__sub_8031F1A8(u8 *arg0) {
    Rec_8031F1A8 *self = (Rec_8031F1A8 *)arg0;
    u8 *inst = TObjEneRecobox__static_instance;
    f32 *posp;
    u8 *res;
    s32 m3;
    s32 m;
    f32 p1;
    s32 t;
    TObjChipParams a = lbl_804762F0;
    u8 *obj2;
    res = *(u8 **)(inst + 0x42C);
    m = *(s32 *)(res + 0x38);
    t = *(s32 *)(res + 0x3C);
    p1 = self->pos[1];
    a.pos[0] = self->pos[0];
    a.pos[1] = p1;
    a.pos[2] = self->pos[2];
    a.pad_38[0] = a.pos[1];
    a.model = m;
    a.textures = t;
    TObjChipParams b = lbl_8047633C;
    res = *(u8 **)(inst + 0x42C);
    m = *(s32 *)(res + 0x48);
    t = *(s32 *)(res + 0x3C);
    b.pos[0] = self->pos[0];
    b.pos[1] = (posp = self->pos)[1];
    b.pos[2] = posp[2];
    b.pad_38[0] = b.pos[1];
    b.model = m;
    b.textures = t;
    TObjChipParams c = lbl_80476388;
    res = *(u8 **)(inst + 0x42C);
    m3 = *(s32 *)(res + 0x58);
    m = m3;
    t = *(s32 *)(res + 0x3C);
    c.pos[0] = posp[0];
    c.pos[1] = posp[1];
    c.pos[2] = posp[2];
    c.pad_38[0] = c.pos[1];
    c.model = m;
    c.textures = t;
    spawn_particle_effect_with_flags(&self->pos[0], 0x45, 0x40);
    spawn_particle_effect_with_flags(&self->pos[0], 0x46, 0x40);
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            construct_debris__8TObjChipFPvPvPv(o, tl_05, (u8 *)&a);
        }
    }
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            construct_debris__8TObjChipFPvPvPv(o, tl_05, (u8 *)&b);
        }
    }
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            obj2 = o;
            construct_debris__8TObjChipFPvPvPv(obj2, tl_05, (u8 *)&c);
        }
    }
}

}
