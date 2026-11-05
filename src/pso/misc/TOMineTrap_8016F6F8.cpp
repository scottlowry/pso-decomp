#include "pso/TParticleCtrl.h"
#include "types.h"
#include "pso/system/vector.h"
#include "pso/player/TObjChara.h"
#include "pso/object/TObjMotion.h"
#include "pso/misc/TOMine.h"
#include "pso/misc/TOMineTrap.h"
#include "pso/TObject.h"
#include "pso/misc/TLobby.h"
#include "pso/player/TObjPlayer.h"
#include "pso/map/FloorArea.h"

struct Trap_8016F704 { u8 pad0[0x38]; f32 pos[3]; u8 pad44[0x84 - 0x44]; s32 delay; u8 pad88[0x2A8 - 0x88]; void *target; u8 pad2AC[0x34C - 0x2AC]; f32 range; u8 pad350[0x35C - 0x350]; u16 targetId; };

extern "C" {
s32 obj_testFlags30__14TObjCollidableFUl(void *, u32);
s32 get_current_floor(void);
f32 horizontal_distance_squared(void *, void *);
extern u8 lobby_rule_settings[];
s32 get_entity_id(void *);
u8 *TOMineTrap__ct(u8 *, u8 *, s32, s32);
void *get_player_by_client_id(s32 i);
void *__nw__7TObjectFUl(u32);
extern s32 enable_v2_features;
s32 create_placed_trap__10TOMineTrapFUiss(u32 arg0, s16 arg1, s16 arg2);
s32 is_split_screen();
void *TOMineDisp__ct(void *, void *, u16);
extern s32 local_client_id;
}

struct VBase_18_33b813
{
  char pad[0x18];
};

struct VObj_18_33b813 : VBase_18_33b813 {
    virtual void m0();
    virtual void m1();
    virtual void m2();
    virtual void m3();
    virtual void m4();
    virtual void m5();
    virtual void m6();
    virtual void m7();
    virtual void m8();
    virtual void m9();
    virtual void m10();
    virtual void m11();
    virtual void m12();
    virtual void m13();
    virtual void m14();
    virtual void m15();
    virtual void m16();
    virtual void m17();
    virtual void m18();
    virtual void m19();
    virtual s32 m20(s32, f32);
};

struct Stack_80170AC8
{
  f32 sp8;
  f32 spC;
  f32 sp10;
};

struct Node_801702C8 { u8 pad[0xC]; Node_801702C8 *next; };

struct VBase_18_1da615 { char pad[0x18]; };

struct VObj_18_1da615 : VBase_18_1da615 {
    virtual void m0();
    virtual void m1();
    virtual void m2();
    virtual void m3();
    virtual void m4();
    virtual void m5();
    virtual void m6();
    virtual void m7();
    virtual void m8();
    virtual void m9();
    virtual void m10();
    virtual void m11();
    virtual void m12();
    virtual void m13();
    virtual void m14();
    virtual void m15();
    virtual void m16();
    virtual void m17();
    virtual void m18();
    virtual void m19();
    virtual s32 m20(s32, f32);
    virtual f32 m21(void *, void *, s32, s32, s32);
    virtual void m22();
    virtual s32 m23(void *, f32);
};

struct Pair_80170DD8 { s32 a; s32 b; };

// View of the trap for the ctor's member writes.
extern "C" s32 get_trap_type__10TOMineTrapFv(void *);
extern "C" void sub_80171348__10TOMineTrapFv(void *, s32);

struct Trap_8016FE98 {
    s32 f0;
    u8 pad4[0x18 - 0x4];
    void *vt;
    u8 pad1C[0x24 - 0x1C];
    s32 f24;
    s16 f28;
    u8 pad2A[0x2E - 0x2A];
    s16 f2E;
    s32 f30;
    s32 f34;
    u8 pad38[0x84 - 0x38];
    s32 f84;
    s32 f88;
    u8 pad8C[0x2D8 - 0x8C];
    u16 f2D8;
    u8 pad2DA[0x326 - 0x2DA];
    u16 f326;
    u8 pad328[0x344 - 0x328];
    u32 f344;
    u8 pad348[0x34C - 0x348];
    f32 f34C;
    f32 f350;
    s32 f354;
    f32 f358;
    u16 f35C;
    u8 pad35E[0x370 - 0x35E];
    u32 f370;
    u32 f374;
    u32 f378;
    u8 pad37C[2];
    u16 f37E;
    u32 f380;
};

// The trap's vtable slot 0x14C (called by the ctor after calc_attach_pos).
struct VObj_18_fe98s {
    char pad[0x18];
    virtual void m0();
    virtual void m1();
    virtual void m2();
    virtual void m3();
    virtual void m4();
    virtual void m5();
    virtual void m6();
    virtual void m7();
    virtual void m8();
    virtual void m9();
    virtual void m10();
    virtual void m11();
    virtual void m12();
    virtual void m13();
    virtual void m14();
    virtual void m15();
    virtual void m16();
    virtual void m17();
    virtual void m18();
    virtual void m19();
    virtual void m20();
    virtual void m21();
    virtual void m22();
    virtual void m23();
    virtual void m24();
    virtual void m25();
    virtual void m26();
    virtual void m27();
    virtual void m28();
    virtual void m29();
    virtual void m30();
    virtual void m31();
    virtual void m32();
    virtual void m33();
    virtual void m34();
    virtual void m35();
    virtual void m36();
    virtual void m37();
    virtual void m38();
    virtual void m39();
    virtual void m40();
    virtual void m41();
    virtual void m42();
    virtual void m43();
    virtual void m44();
    virtual void m45();
    virtual void m46();
    virtual void m47();
    virtual void m48();
    virtual void m49();
    virtual void m50();
    virtual void m51();
    virtual void m52();
    virtual void m53();
    virtual void m54();
    virtual void m55();
    virtual void m56();
    virtual void m57();
    virtual void m58();
    virtual void m59();
    virtual void m60();
    virtual void m61();
    virtual void m62();
    virtual void m63();
    virtual void m64();
    virtual void m65();
    virtual void m66();
    virtual void m67();
    virtual void m68();
    virtual void m69();
    virtual void m70();
    virtual void m71();
    virtual void m72();
    virtual void m73();
    virtual void m74();
    virtual void m75();
    virtual void m76();
    virtual void m77();
    virtual void m78();
    virtual void m79();
    virtual void m80();
    virtual void m81();
};

// The owning player's vtable slot 0x40, read by the ctor's scale formula.
struct VObj_18_fe98p {
    char pad[0x18];
    virtual void m0();
    virtual void m1();
    virtual void m2();
    virtual void m3();
    virtual void m4();
    virtual void m5();
    virtual void m6();
    virtual void m7();
    virtual void m8();
    virtual void m9();
    virtual void m10();
    virtual void m11();
    virtual void m12();
    virtual void m13();
    virtual s32 m14();
};

extern "C" {
s32 is_locally_controlled__10TObjPlayerFPv(u32 a0);
s32 get_localized_text_entry(s32 arg0, s32 arg1);
s32 get_main_phase();
s32 play_sound_effect(s32, s32, s32, s32);
extern s8 mine_trap_effect_table[];
extern s8 mine_trap_keymachine_table[];
void *spawn_particle_effect(void *pos, s32 id);
extern f32 lbl_805DB864;
extern f32 lbl_805DB85C;
extern const f32 TOMineTrap__data_805DB868;
void TOMineTrap__sub_80170CD4(void* p);
f32 sin_table_lookup(s32);
extern const f32 lbl_805DB884;
extern const f32 lbl_805DB888;
f32 atan2_float(f32 y, f32 x);
f32 vec3_add_to(void *, void *);
f32 vec_squared_length(u8 *arg0);
f32 subtract_vector(void *, void *);
f32 normalize_vector(void *);
extern const f64 lbl_80442200;
extern const f32 lbl_805DB870;
void queue_destruction__7TObjectFv(void *arg0);
int get_player_data__10TObjPlayerFi(int a0);
s32 check_value_equals__13TUnk_804B6C24Fl(void *, s32);
extern s32 TOMineTrap__data_805D3080;
extern s32 registered_player_count;
extern s32 lbl_805D5870;
extern s32 lbl_805D5868;
extern s32 TOMineIcon01__name;
extern s32 TOMineIcon02__name;
extern s32 TOMineIcon03__name;
extern s32 TOMineIcon04__name;
u8 *get_battle_param__10TObjPlayerFi(s32);
void check_enemy_body_collisions(void *);
extern const f32 lbl_805DB874;
void *__dt__10TOMineTrapFv(void *arg0, s16 arg1);
s32 free_collision_body_parts(void *);
s32 is_locally_controlled__10TObjPlayerFPv(u32 a0 = 0);
s32 __dl__7TObjectFPv(void *);
void *__dt__6TOMineFv(void *arg0, s16 arg1);
void TOMine__ct(void *, void *);
extern void *tl_05;
s32 get_bml_model(void *, s32);
s32 TObjFish__sub_8001EDB0(void *, s32);
void init_collision_body_parts(void *, void *, s32);
void init_position_vectors__10TObjPlayerFv(void *);
extern u8 mine_collision_body_parts[];
extern s32 game_difficulty_selection;
extern void *lbl_805D5A50;
extern const f32 lbl_805D307C;
extern const f32 lbl_805DB86C;
extern const f32 lbl_805DB878;
extern const f32 lbl_805DB87C;
extern const f32 lbl_805DB880;
extern const f32 lbl_80442138[];
extern const f64 lbl_804421F8;

void TOMineTrap::set_state() { this->mode = 4; }

s32 TOMineTrap::find_target_in_range() {
    Trap_8016F704 *self = (Trap_8016F704 *)this;
    u8 *p;
    s32 i;
    s32 id;

    self->targetId = 0xFFFF;
    self->target = 0;
    if (self->delay > 0) {
        self->delay--;
        return 0;
    }
    for (i = 0; i < registered_player_count + lbl_805D5870; i++) {
        p = (u8 *)get_player_data__10TObjPlayerFi(i);
        if (p == 0 || p == (u8 *)self || obj_testFlags30__14TObjCollidableFUl(p, 0x800) != 0) {
            continue;
        }
        id = get_entity_id(p);
        if ((u16)id == 0xFFFF) {
            continue;
        }
        if ((u16)id == (u16)((TOMineTrap *)self)->get_trap_type() && TOMineTrap::get_trap_count() != 1 &&
            ((TLobby *)lobby_rule_settings)->get_rule_field_0() != 0) {
            continue;
        }
        if ((u16)id < 0x1000) {
            if (((TObjPlayer *)p)->get_floor() != get_current_floor()) {
                continue;
            }
            if (horizontal_distance_squared(self->pos, p + 0x38) < self->range * self->range) {
                self->targetId = id;
                self->target = p;
                return 1;
            }
        } else if ((u16)id < 0x4000) {
            if (horizontal_distance_squared(self->pos, p + 0x38) < self->range * self->range) {
                self->targetId = id;
                self->target = p;
                return 1;
            }
        }
    }
    return 0;
}

void TOMineTrap::set_triggered() {
    u8 *arg0 = (u8 *)this;
    this->mode = 3;
    ((TObjCollidable *)arg0)->set_indexed_flags(0, 1);
    this->actorFlags = (s32) (this->actorFlags & 0xFFFBFFFF);
}

void TOMineTrap::vfunc_86() {
    u8 *arg0 = (u8 *)this;
    this->mode = 2;
    ((TObjCollidable *)arg0)->set_indexed_flags(0, 1);
    this->actorFlags = (s32) (this->actorFlags & 0xFFFBFFFF);
}

void TOMineTrap::destroy_matching_traps() {
    void *p;
    s32 i;
    for (i = registered_player_count + lbl_805D5870; i < lbl_805D5868; i++) {
        p = (void *)get_player_data__10TObjPlayerFi(i);
        if (p != 0 && check_value_equals__13TUnk_804B6C24Fl(p, TOMineTrap__data_805D3080) != 0) {
            queue_destruction__7TObjectFv(p);
        }
    }
}

s32 create_placed_trap__10TOMineTrapFUiss(u32 arg0, s16 arg1, s16 arg2) {
    u16 id;
    void *player;
    void *obj;
    if (enable_v2_features != 1 || arg0 == 0 || (id = get_entity_id((void *)arg0)) == 0xFFFF || id >= 0x1000 ||
        (player = (void *)get_player_by_client_id(id)) == 0 || ((TObjPlayer *)player)->get_floor() != get_current_floor() ||
        arg1 < 0 || arg1 >= 4 || arg2 < 0 || arg2 > 0x14) {
        return 0;
    }
    if (is_boss_area() == 1 || is_current_area_item_enabled() == 0) {
        return 0;
    }
    obj = __nw__7TObjectFUl(0x384);
    if (obj != 0) {
        obj = ((u8 *(*)(u8 *, u8 *, s16, s16))TOMineTrap__ct)((u8 *)obj, (u8 *)arg0, arg1, arg2);
    }
    return (s32)obj;
}

void*TOMineTrap::get_mine_data_ptr() { return (char*)this + 0x334; }

extern s32 __vt__10TOMineTrap[];

void *__dt__10TOMineTrapFv(void *arg0, s16 arg1) {
    if (arg0 != NULL) {
        *(s32 **)((s8 *)arg0 + 0x18) = __vt__10TOMineTrap;
        ((TObjCollidable *)arg0)->unregister_object_by_id();
        free_collision_body_parts(arg0);
        __dt__6TOMineFv(arg0, 0);
        if (arg1 > 0) {
            __dl__7TObjectFPv(arg0);
        }
    }
    return arg0;
}

#pragma push
#pragma fp_contract on
u8 *TOMineTrap__ct(u8 *arg0, u8 *arg1, s32 arg2, s32 arg3) {
    Trap_8016FE98 *self = (Trap_8016FE98 *)arg0;
    Vec *copied;
    s32 floor;
    s32 area;
    s32 kind;
    s16 trap_kind;

    TOMine__ct(arg0, tl_05);
    self->vt = (void *)__vt__10TOMineTrap;
    self->f0 = TOMineTrap__data_805D3080;
    self->f380 = 0;
    if (arg1 != 0) {
        sub_80171348__10TOMineTrapFv(arg0, get_entity_id(arg1));
    } else {
        self->f2D8 = 0xFFFF;
    }
    void *player = 0;
    if ((u16)get_trap_type__10TOMineTrapFv(arg0) != 0xFFFF &&
        (u16)get_trap_type__10TOMineTrapFv(arg0) < 0x1000) {
        player = get_player_by_client_id((u16)get_trap_type__10TOMineTrapFv(arg0));
    }
    get_current_floor_area();
    floor = get_current_floor();
    if (enable_v2_features != 1 || arg1 == 0 || player == 0 ||
        ((TObjPlayer *)player)->get_floor() != floor || is_current_area_item_enabled() != 1 || is_boss_area() != 0) {
        queue_destruction__7TObjectFv(arg0);
        return arg0;
    }
    trap_kind = (s16)arg2;
    switch (trap_kind) {
    default:
        trap_kind = 0;
        // fall through
    case 0:
        self->f354 = 1;
        if (((TLobby *)lobby_rule_settings)->get_rule_field_0() == 1) {
            self->f358 = lbl_805D307C;
        } else {
            area = get_current_floor_area();
            f32 tbl = lbl_80442138[area];
            self->f358 = lbl_805DB86C * tbl *
                          (lbl_805DB870 * (lbl_805DB878 *
                                ((f64)((u16)(((s32)((VObj_18_fe98p *)player)->m14()) ^ 0x8000)) - lbl_804421F8) + lbl_805DB874));
        }
        if (self->f358 < lbl_805DB85C) {
            self->f358 = lbl_805DB85C;
        }
        break;
    case 1:
        self->f354 = 2;
        self->f358 = lbl_805DB85C;
        break;
    case 2:
        self->f354 = 0x11;
        self->f358 = lbl_805DB85C;
        break;
    case 3:
        self->f354 = 0x12;
        self->f358 = lbl_805DB85C;
        break;
    }
    self->f37E = (u16)((u16)get_trap_type__10TOMineTrapFv(arg0) * 0x50 + trap_kind * 0x14 + (s16)arg3);
    copied = VecCopy((Vec *)(arg0 + 0x38), (const Vec *)(arg1 + 0x38));
    copied = VecCopy((Vec *)(arg0 + 0x50), copied);
    VecCopy((Vec *)(arg0 + 0x334), copied);
    init_position_vectors__10TObjPlayerFv(arg0);
    ((TObjChara *)arg0)->calc_attach_pos();
    ((VObj_18_fe98s *)arg0)->m81();
    self->f370 = *(s32 *)(arg1 + 0x60);
    self->f2E = *(s16 *)(arg1 + 0x2E);
    self->f28 = *(s16 *)(arg1 + 0x28);
    kind = (s32)self->f354;
    if (kind >= 0xf && kind <= 0x12) {
        self->f34 = get_bml_model(lbl_805D5A50, 5);
        self->f24 = TObjFish__sub_8001EDB0(lbl_805D5A50, 5);
        self->f374 = get_bml_model(lbl_805D5A50, 0);
        self->f378 = TObjFish__sub_8001EDB0(lbl_805D5A50, 0);
    } else {
        if (kind != 0x13 && (kind < 0 || kind > 5)) {
            self->f354 = 1;
        }
        self->f34 = get_bml_model(lbl_805D5A50, 4);
        self->f24 = TObjFish__sub_8001EDB0(lbl_805D5A50, 4);
        self->f374 = get_bml_model(lbl_805D5A50, 1);
        self->f378 = TObjFish__sub_8001EDB0(lbl_805D5A50, 1);
    }
    self->f326 = 0;
    self->f34C = lbl_805DB87C;
    self->f350 = lbl_805DB87C;
    self->f84 = 0x96;
    self->f88 = 0x1E;
    if (game_difficulty_selection == 3 && ((TLobby *)lobby_rule_settings)->get_rule_field_0() != 0) {
        self->f84 = 0x3C;
        self->f350 = lbl_805DB880;
        TOMineTrap::set_trap_count(0);
        TOMineTrap::set_instance(1);
    }
    self->f344 = 0;
    self->f35C = 0xFFFF;
    self->f30 = (s32)(self->f30 | 0x6000);
    init_collision_body_parts(arg0, mine_collision_body_parts, 1);
    ((TObjCollidable *)arg0)->register_object_by_id();
    return arg0;
}
#pragma pop

s32 TOMine::is_target_in_list(void *obj) {
    TOMine *self = this;
    if (obj != 0) {
        u32 id = get_entity_id(obj);
        if (id < 4) {
            Node_801702C8 *n;
            for (n = *(Node_801702C8 * *)&self->m_down; n != 0; n = n->next) {
                if (((TOMineTrap *)n)->matches_id(id) != 0) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

s32 TOMine::roll_physical_accuracy(void *, s32, f32) { return 1; }
s32 TOMine::try_start_action(s32, s32) { return 1; }
void TOMine::apply_knockback_from_attacker(u8 *, f32) {  }
void TOMine::vfunc_79() {  }
s32 TOMineTrap::check_trigger(u32 arg1) {
    if (is_target_in_list((void *)arg1) == 1) {
        return 0;
    }
    if (((s32) this->m_344 == 2) && (arg1 == (u32) this->target)) {
        return 0;
    }
    if (is_locally_controlled__10TObjPlayerFPv(arg1) != 0) {
        return 1;
    }
    return 0;
}
s32 TOMineTrap::can_trigger(u32 arg1) {
    if (is_target_in_list((void *)arg1) == 1) {
        return 0;
    }
    if (((s32) this->m_344 == 2) && (arg1 == (u32) this->target)) {
        return 0;
    }
    if (is_locally_controlled__10TObjPlayerFPv(arg1) != 0) {
        return 1;
    }
    return 0;
}

void TOMine::spawn_disp_objects() {
    u8 *obj;
    u16 i;
    u8 *arg0 = (u8 *)this;
    if (is_split_screen() == 0) {
        obj = (u8 *)__nw__7TObjectFUl(0xAC);
        if (obj != NULL) {
            obj = (u8 *)TOMineDisp__ct(obj, arg0, (u16)local_client_id);
        }
        if (obj != NULL) {
            VecCopy((Vec *)(obj + 0x50), (const Vec *)(arg0 + 0x50));
            VecCopy((Vec *)(obj + 0x38), (const Vec *)(arg0 + 0x38));
        }
    } else {
        for (i = 0; i != 4; i++) {
            obj = (u8 *)__nw__7TObjectFUl(0xAC);
            if (obj != NULL) {
                obj = (u8 *)TOMineDisp__ct(obj, arg0, i);
            }
            if (obj != NULL) {
                VecCopy((Vec *)(obj + 0x50), (const Vec *)(arg0 + 0x50));
                VecCopy((Vec *)(obj + 0x38), (const Vec *)(arg0 + 0x38));
            }
        }
    }
}

void TOMine::apply_object_set_data(void *set_data) {
    u8 *arg0 = (u8 *)this;
    TObjBase::apply_object_set_data(set_data);
    this->spawn_disp_objects();
    VecCopy((Vec *)(arg0 + 0x334), (const Vec *)(arg0 + 0x38));
}
void TOMine::vfunc_85() {  }
const char *TOMine::get_name() { return (const char *)get_localized_text_entry(16, 16); }
void TOMine::update_state() {
    s32 temp_r0;
    *(s32 *)((s8 *)this + 0x348) = (s32) this->scale.z;
    temp_r0 = *(s32 *)((s8 *)this + 0x348);
    if (temp_r0 < 0) {
        *(s32 *)&this->m_344 = 0;
        return;
    }
    if (temp_r0 > 0) {
        *(s32 *)&this->m_344 = 1;
        return;
    }
    if (get_main_phase() == 0xE) {
        *(s32 *)&this->m_344 = 0;
        *(s32 *)&this->set_params[2] = 0x1E;
        return;
    }
    *(s32 *)&this->m_344 = 2;
}
void TOMineTrap::spawn_effect() {
    s32 arg0 = (s32)this;
    s32 area = get_current_floor_area();
    s32 elem = *(s32 *)(mine_trap_effect_table + area * 4);
    if (elem != -1) {
        play_sound_effect(elem, arg0 + 0x38, 0, 0);
    }
}
void TOMineTrap::attach_to_keymachine() {
    s32 arg0 = (s32)this;
    s32 area = get_current_floor_area();
    s32 elem = *(s32 *)(mine_trap_keymachine_table + area * 4);
    if (elem != -1) {
        play_sound_effect(elem, arg0 + 0x38, 0, 0);
    }
}
void TOMineTrap::detonate_if_triggered() {
    s32 arg0 = (s32)this;
    {
        TParticleCtrl *particle = (TParticleCtrl *)spawn_particle_effect((void *)(arg0 + 0x2FC), 0x45);
        if (particle != NULL) {
            particle->set_scale(lbl_805DB864, lbl_805DB864);
        }
    }
}
void TOMine::sub_8017070C() {
    spawn_particle_effect(((void *) (((u8 *)this) + 0x2FC)), 0x47);
    this->vfunc_82();
    this->vfunc_80();
}

void TOMine::vfunc_6(s16 *arg1, s32 arg2) {
    s16 temp_r0;
    temp_r0 = *(s16 *)((s8 *)arg1 + 0);
    if (temp_r0 == 5) {
        if (arg2 == 1) {
            sub_8017070C();
        }
        set_flag8();
        queue_destruction__7TObjectFv((this));
        access_object_saved_state(arg1, 0);
        return;
    }
    if (temp_r0 == 3) {
        this->mode = temp_r0;
        set_indexed_flags(0, 1);
        this->actorFlags = (s32) (this->actorFlags & 0xFFFBFFFF);
        this->calc_attach_pos();
        refresh_collision_body_centers();
        this->vfunc_81();
        access_object_saved_state(arg1, 0);
        this->queue_destruction_for_each_node();
    }
}

f32 TOMine::receive_physical_attack(void *, f32) {
    s16 sp8;
    if (((u16) this->entity_id >= 0x4000U) && ((u32) this->set_entry != 0U) && (access_object_saved_state(&sp8, 1) != 0)) {
        this->mode = 5;
        sp8 = this->mode;
        send_object_state_update(&sp8);
    }
    return lbl_805DB85C;
}
f32 TOMine::receive_weapon_special_attack(void *arg1, void *) {
    if (is_target_in_list(arg1) == 1) {
        return lbl_805DB85C;
    }
    if ((is_locally_controlled__10TObjPlayerFPv((u32)arg1) != 0) && (((TObjPlayer *)arg1)->obj_getS16_116() != 0)) {
        this->receive_physical_attack(0, TOMineTrap__data_805DB868);
    }
    return lbl_805DB85C;
}

typedef struct VBase_18_33b813 VBase_18_33b813;
typedef struct VObj_18_33b813 VObj_18_33b813;
f32 TOMine::receive_direct_attack(void *arg1, DirectAttackPayload payload, void *, s32, s32) {
  s32 temp_r0;
  s32 var_r31;
  if (arg1 == 0)
  {
    return (*(const f32 *)&lbl_805DB85C);
  }
  if (this->is_target_in_list(arg1) == 1)
  {
    return (*(const f32 *)&lbl_805DB85C);
  }
  var_r31 = 0;
  if ((get_entity_id((void *) arg1) < 4U) && (is_locally_controlled__10TObjPlayerFPv((u32)((void *) arg1)) != 0))
  {
    var_r31 = 1;
  }
  if (var_r31 != 0)
  {
    temp_r0 = payload.kind;
    if (temp_r0 != 0x13)
    {
      if ((temp_r0 < 0x13) && (temp_r0 < 5))
      {
        if (temp_r0 < 0)
        {
          if ((temp_r0 && temp_r0) && temp_r0)
          {
          }
        }
        else
        {
          goto block_13;
        }
      }
    }
    else
    {
      block_13:
      (this->receive_physical_attack(0, ((*(const f32 *)&TOMineTrap__data_805DB868))));
    }
  }
  return (*(const f32 *)&lbl_805DB85C);
}

void TOMine::update_trigger() {
    s16 sp8;
    if (((u16) this->entity_id >= 0x4000U) && ((u32) this->set_entry != 0U) && (access_object_saved_state(&sp8, 1) != 0)) {
        this->mode = 3;
        sp8 = this->mode;
        send_object_state_update(&sp8);
    }
}
void TOMine::vfunc_86() {
    u8 *arg0 = (u8 *)this;
    this->mode = 2;
    ((TObjCollidable *)arg0)->set_indexed_flags(0, 1);
    this->actorFlags = (s32) (this->actorFlags & 0xFFFBFFFF);
    ((TObjChara *)arg0)->calc_attach_pos();
    ((TObjCollidable *)arg0)->refresh_collision_body_centers();
    ((TOMine *)(arg0))->vfunc_81();
}

typedef struct Stack_80170AC8 Stack_80170AC8;
#pragma fp_contract on
void TOMine::follow_target() {
    u8 *arg0 = (u8 *)this;
  unsigned short new_var;
  Stack_80170AC8 stack;
  f32 temp_f2;
  new_var = -1U;
  if (((this->m_35c) == new_var) || ((this->target) == 0))
  {
    this->mode = 2;
    return;
  }
  VecCopy((Vec *)(arg0 + 0x44), (const Vec *)(arg0 + 0x38));
  VecCopy((Vec *)(&stack.sp8), (const Vec *)((this->target) + 0x38));
  stack.spC = *((f32 *) (((s8 *) arg0) + 0x3C));
  subtract_vector(&stack.sp8, (u8 *)&this->position);
  if (lbl_805DB870 < vec_squared_length((u8 *)&stack.sp8))
  {
    normalize_vector(&stack.sp8);
    stack.sp8 *= lbl_805DB870;
    stack.sp10 *= lbl_805DB870;
  }
  vec3_add_to((u8 *)&this->position, &stack.sp8);
  ((TObjPlayer *)arg0)->update_enemy_collision_flags();
  temp_f2 = *((f32 *) (((s8 *) arg0) + 0x48));
  *((f32 *) (((s8 *) arg0) + 0x3C)) = (f32) ((lbl_805DB884 * ((lbl_805DB888 + (*((f32 *) ((this->target) + 0x3C)))) - temp_f2)) + temp_f2);
  ((TObjChara *)arg0)->calc_attach_pos();
  this->rotation_y = (s32) (lbl_80442200 * atan2_float((f64) stack.sp8, (f64) stack.sp10));
  ((TObjCollidable *)arg0)->refresh_collision_body_centers();
}

void TOMine::sub_80170BEC() {
    u8 *p;
    s32 i;
    switch (this->phase) {
    case 0:
        this->phase = 1;
        for (i = lbl_805D5870; i < lbl_805D5868; i++) {
            p = (u8 *)get_player_data__10TObjPlayerFi(i);
            if (p != NULL && p != ((u8 *)this) &&
                (check_value_equals__13TUnk_804B6C24Fl(p, TOMineIcon01__name) != 0 ||
                 check_value_equals__13TUnk_804B6C24Fl(p, TOMineIcon02__name) != 0 ||
                 check_value_equals__13TUnk_804B6C24Fl(p, TOMineIcon03__name) != 0 ||
                 check_value_equals__13TUnk_804B6C24Fl(p, TOMineIcon04__name) != 0) &&
                *(s32 *)(p + 0x344) == 1 && *(s32 *)(p + 0x348) == *(s32 *)(((u8 *)this) + 0x348)) {
                ((TOMine *)p)->update_trigger();
            }
        }
        break;
    }
    ((TOMineTrap *)((u8 *)this))->sync_position();
}

void TOMineTrap__sub_80170CD4(void* p) { ((TOMineTrap *)p)->sync_position(); }

#pragma push
#pragma fp_contract on
void TOMine::update_float_height() {
    u8 *arg0 = (u8 *)this;
    f32 temp_f1;
    f32 temp_f4;
    if (!(this->m_340 & 2)) {
        temp_f4 = *(f32 *)((s8 *)arg0 + 0x338);
        *(f32 *)((s8 *)arg0 + 0x338) = (f32) (temp_f4 + ((lbl_805DB884 * ((lbl_805DB888 + this->home_position.y) - temp_f4)) + (*(const f32 *)&TOMineTrap__data_805DB868)));
        temp_f1 = lbl_805DB888 + this->home_position.y;
        if (temp_f1 <= *(f32 *)((s8 *)arg0 + 0x338)) {
            *(f32 *)((s8 *)arg0 + 0x338) = temp_f1;
            this->m_340 = (s32) (this->m_340 | 2);
        }
    } else {
        *(s32 *)&this->rotation_x = (s32) (*(s32 *)&this->rotation_x + 0x800);
        *(f32 *)((s8 *)arg0 + 0x338) = (f32) (*(f32 *)((s8 *)arg0 + 0x338) + sin_table_lookup(*(s32 *)&this->rotation_x));
    }
}
#pragma pop

void TOMineTrap::sync_position() { VecCopy((Vec *)((char*)this + 0x38), (const Vec *)((char*)this + 0x334)); refresh_collision_body_centers(); }
void TOMine::detonate() {
    s32 i;
    u8 *obj;
    set_indexed_flags(0, 2);
    *(f32 *)(*(u8 * *)&this->bodies + 0xC) = this->m_350;
    TObjPlayer::init_all_slots();
    ((TObjPlayer *)((u8 *)this))->check_object_collisions();
    check_enemy_body_collisions(this);
    for (i = 0; i < 0x10; i++) {
        obj = get_battle_param__10TObjPlayerFi(i);
        if (TObjPlayer::is_valid_and_active((u32)obj) != 0) {
            Pair_80170DD8 pair = *(Pair_80170DD8 *)(((u8 *)this) + 0x354);
            f32 r = ((VObj_18_1da615 *)obj)->m21(this, &pair, 0, -1, -1);
            if (*(s32 *)&this->m_354 < 5) {
                ((VObj_18_1da615 *)obj)->m23(this, lbl_805DB874 * r);
            }
        }
    }
    this->mode = 6;
    this->clear_player_status_flag(0, 1);
    this->receive_physical_attack(0, TOMineTrap__data_805DB868);
}

}
