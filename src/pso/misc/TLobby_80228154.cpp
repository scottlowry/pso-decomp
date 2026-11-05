#include "types.h"
#include "pso/misc/TLobby.h"
#include "pso/item/TUnk_804CC048.h"
#include "pso/map/FloorArea.h"
#include "pso/misc/TLobby_80207644.h"
#include <stddef.h>
#include "pso/misc/TScene.h"
#include "pso/misc/TLobby_800FD78C.h"


struct RecoveredGlobal_80228634_lbl_804CBE98 {
    s32 value;
    u8 remaining[0x1AC];
};

struct RecoveredGlobal_80228754_lbl_804CBE98 {
    s32 value;
    u8 remaining[0x1AC];
};

struct RecoveredGlobal_802286C4_lbl_804CBE98 {
    s32 value;
    u8 remaining[0x1AC];
};


extern "C" {
s32 select_area_entrance(void *arg0);
s32 lookup_scene_object__6TLobbyFPv(s32, void *);
extern RecoveredGlobal_80228634_lbl_804CBE98 area_initializer_dispatch_table;
void run_area_scene_cleanup(u8 *arg0);
void promote_area_floor(u8 *arg0);
void load_area_scene_and_init(u8 *arg0);
s32 get_floor_map_terrain(s32);
void set_global_param__8TObjFishFl(s32 arg0);
void push_matrix_from(void *arg0);
void rotate_matrix_z(s32 arg0, s32 arg1);
void rotate_vector_by_matrix(s32 arg0, f32 *arg1, f32 *arg2);
void pop_matrix(void);
void begin_screen_draw(s32 arg0);
void set_draw_texture_and_color(s32 arg0, u32 arg1);
void draw_textured_quad_at_depth(f32 *arg0, f32 arg1);
void get_player__20TWindowSubStatusDispFv(void);
extern u8 identity_matrix[];
extern u8 model_material_color[];
extern const f32 lbl_805DC770;
extern const f32 lbl_805DC774;
extern const f32 lbl_805DC778;
extern const f32 lbl_805DC77C;
extern const f32 lbl_805DC780;
extern const f32 lbl_805DC784;

#pragma push
#pragma opt_common_subs off
void TLobby__sub_80228154(void *arg0, s32 arg1, s32 arg2, f32 arg3) {
    u32 color;
    f32 v[3];
    f32 pts[8];
    f32 c4;
    f32 c6;
    f32 c0;
    f32 c2;
    f32 A;
    f32 B;
    s16 *e;
    s32 i0;
    s32 i1;
    s32 i2;
    s32 i3;
    u8 *pb;
    u32 iso;
    u32 lz;

    if (arg0 == 0) {
        return;
    }
    if (*(u32 *)((s8 *)arg0 + 0x18) == 0) {
        return;
    }
    set_global_param__8TObjFishFl(*(s32 *)((s8 *)arg0 + 0x18));
    e = (s16 *)(*(s32 *)((s8 *)arg0 + 0x1c) + arg1 * 0x14);
    c4 = (f32)-(s32)e[2];
    c0 = (f32)(s32)e[0];
    c6 = (f32)-(s32)e[3];
    pts[0] = *(f32 *)((s8 *)arg0 + 0x0) + c4 * *(f32 *)((s8 *)arg0 + 0xc);
    c2 = (f32)(s32)e[1];
    pts[2] = *(f32 *)((s8 *)arg0 + 0x0) + (c4 + c0) * *(f32 *)((s8 *)arg0 + 0xc);
    pts[1] = *(f32 *)((s8 *)arg0 + 0x4) + c6 * *(f32 *)((s8 *)arg0 + 0x10);
    pts[3] = *(f32 *)((s8 *)arg0 + 0x4) + (c6 + c2) * *(f32 *)((s8 *)arg0 + 0x10);
    pts[4] = lbl_805DC770 * (f32)(s32)e[4];
    if (lbl_805DC774 < pts[4]) {
        pts[4] = lbl_805DC774;
    }
    pts[5] = (f32)(s32)e[5] * lbl_805DC770;
    if (lbl_805DC774 < pts[5]) {
        pts[5] = lbl_805DC774;
    }
    pts[6] = (f32)(s32)e[6] * lbl_805DC770;
    if (lbl_805DC774 < pts[6]) {
        pts[6] = lbl_805DC774;
    }
    pts[7] = (f32)(s32)e[7] * lbl_805DC770;
    if (lbl_805DC774 < pts[7]) {
        pts[7] = lbl_805DC774;
    }
    color = 0xFFFFFFFF;
    if (arg2 & 1) {
        A = (pts[2] + pts[0]) * lbl_805DC778;
        B = (pts[3] + pts[1]) * lbl_805DC778;
        v[2] = lbl_805DC77C;
        v[0] = pts[0] - A;
        v[1] = pts[1] - B;
        push_matrix_from(identity_matrix);
        rotate_matrix_z(0, *(s32 *)((s8 *)arg0 + 0x14));
        rotate_vector_by_matrix(0, v, v);
        pop_matrix();
        pts[0] = A + v[0];
        pts[1] = B + v[1];
        pts[2] = A - v[0];
        pts[3] = B - v[1];
    }
    if (arg2 & 2) {
        i3 = (s32)(lbl_805DC780 * ((f32 *)model_material_color)[3]);
        i2 = (s32)(lbl_805DC780 * ((f32 *)model_material_color)[2]);
        i1 = (s32)(lbl_805DC780 * ((f32 *)model_material_color)[1]);
        i0 = (s32)(lbl_805DC780 * ((f32 *)model_material_color)[0]);
        pb = (u8 *)&color;
        pb[3] = (u8)i3;
        pb[2] = (u8)i2;
        pb[1] = (u8)i1;
        pb[0] = (u8)i0;
    }
    if (arg2 & 4) {
        pts[6] = pts[4];
        pts[4] = pts[4];
    }
    if (arg2 & 8) {
        pts[7] = pts[5];
        pts[4] = pts[5];
    }
    arg3 = lbl_805DC784 / arg3;
    iso = (u32)(arg2 & 0x20) - 0x20;
    lz = (u32)__cntlzw((s32)iso);
    begin_screen_draw((s32)((lz >> 5) & 0xFF));
    set_draw_texture_and_color(e[8], color);
    draw_textured_quad_at_depth(pts, arg3);
    get_player__20TWindowSubStatusDispFv();
}
#pragma pop

void TLobby::clear_ready_flag_unless_locked() {
    if (get_current_floor_area() != AREA_LOBBY) {
        *(s32 *)((s8 *)this + 0x20) = (s32) (*(s32 *)((s8 *)this + 0x20) & 0xFFFFFFFE);
    }
}

void TLobby::set_area(s32 arg1) {
    *(s32 *)&this->m_next = arg1;
    *(s32 *)((s8 *)this + 0x18) = get_floor_map_terrain(*(s32 *)&this->m_next);
}

#pragma push
#pragma fp_contract on
s32 select_area_entrance(void *arg0) {
    s32 temp_r0;
    s32 temp_r3;
    if ((s32) *(s32 *)((s8 *)arg0 + 0) > 0x11) {
        return 4;
    }
    if (*(s32 *)((s8 *)arg0 + 0x20) & 1) {
        return 2;
    }
    if ((TLobby::get_instance() == 0) && (get_floor_area(*(s32 *)((s8 *)arg0 + 0)) == 0xD)) {
        switch (get_floor_area(*(s32 *)((s8 *)arg0 + 4))) {
        case 8:
        case 9:
        case 10:
            return 1;
        default:
            return 0;
        }
    }
    temp_r0 = *(s32 *)((s8 *)arg0 + 4) - *(s32 *)((s8 *)arg0 + 0);
    if (temp_r0 >= 0) {
        return 1;
    }
    return (temp_r0 < 0) ? 0 : 4;
}
#pragma pop

typedef char RecoveredGlobal_80228634_lbl_804CBE98_size[sizeof(RecoveredGlobal_80228634_lbl_804CBE98) == 0x1B0 ? 1 : -1];
void run_area_scene_cleanup(u8 *arg0) {
    s32 sp8;
    s32 (*var_r12)(s32);
    s32 *var_r4;
    s32 var_r3;
    u8 *var_r31;
    var_r4 = &sp8;
    var_r31 = arg0;
    var_r3 = *(s32 *)((s8 *)arg0 + 4);
    if (lookup_scene_object__6TLobbyFPv(var_r3, var_r4) != 0) {
        var_r3 = (s32) &area_initializer_dispatch_table.value;
        var_r3 = (s32) &area_initializer_dispatch_table.value;
        var_r3 += sp8 * 0xC;
        var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 8);
        var_r12(var_r3);
    } else {
        var_r3 = (s32) &area_initializer_dispatch_table.value;
        var_r3 = (s32) &area_initializer_dispatch_table.value;
        var_r3 += *(s32 *)((s8 *)var_r31 + 4) * 0xC;
        var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 8);
        var_r12(var_r3);
    }
    *(s32 *)((s8 *)var_r31 + 4) = 0;
    *(s32 *)((s8 *)var_r31 + 8) = 0;
    *(s32 *)((s8 *)var_r31 + 0xC) = 0;
}

typedef char RecoveredGlobal_80228754_lbl_804CBE98_size[sizeof(RecoveredGlobal_80228754_lbl_804CBE98) == 0x1B0 ? 1 : -1];

typedef char RecoveredGlobal_802286C4_lbl_804CBE98_size[sizeof(RecoveredGlobal_802286C4_lbl_804CBE98) == 0x1B0 ? 1 : -1];
void load_area_scene_and_init(u8 *arg0) {
    s32 sp8;
    s32 (*var_r12)(s32);
    s32 *var_r4;
    s32 var_r3;
    u8 *var_r31;
    var_r31 = arg0;
    var_r3 = *(s32 *)((s8 *)arg0 + 4);
    set_current_floor_area((var_r3));
    var_r3 = *(s32 *)((s8 *)var_r31 + 0x10);
    TScene::set_scene(var_r3);
    var_r3 = *(s32 *)((s8 *)var_r31 + 4);
    var_r4 = &sp8;
    if (lookup_scene_object__6TLobbyFPv(var_r3, var_r4) != 0) {
        var_r3 = (s32) &(*(RecoveredGlobal_802286C4_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 = (s32) &(*(RecoveredGlobal_802286C4_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 += sp8 * 0xC;
        var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 4);
        var_r12(var_r3);
        return;
    }
    var_r3 = (s32) &(*(RecoveredGlobal_802286C4_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
    var_r3 = (s32) &(*(RecoveredGlobal_802286C4_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
    var_r3 += *(s32 *)((s8 *)var_r31 + 4) * 0xC;
    var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 4);
    var_r12(var_r3);
}

void promote_area_floor(u8 *arg0) {
    s32 sp8;
    s32 (*var_r12)(s32);
    s32 *var_r4;
    s32 var_r3;
    u8 *var_r31;
    var_r4 = &sp8;
    var_r31 = arg0;
    var_r3 = *(s32 *)((s8 *)arg0 + 4);
    if (lookup_scene_object__6TLobbyFPv(var_r3, var_r4) != 0) {
        var_r3 = (s32) &(*(RecoveredGlobal_80228754_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 = (s32) &(*(RecoveredGlobal_80228754_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 += sp8 * 0xC;
        var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 8);
        var_r12(var_r3);
    } else {
        var_r3 = (s32) &(*(RecoveredGlobal_80228754_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 = (s32) &(*(RecoveredGlobal_80228754_lbl_804CBE98 *)&area_initializer_dispatch_table).value;
        var_r3 += *(s32 *)((s8 *)var_r31 + 4) * 0xC;
        var_r12 = *(s32 (**)(s32))((s8 *)var_r3 + 8);
        var_r12(var_r3);
    }
    *(s32 *)((s8 *)var_r31 + 0) = (s32) *(s32 *)((s8 *)var_r31 + 4);
    *(s32 *)((s8 *)var_r31 + 4) = (s32) *(s32 *)((s8 *)var_r31 + 0xC);
    *(s32 *)((s8 *)var_r31 + 0x10) = (s32) *(s32 *)((s8 *)var_r31 + 0x18);
    TLobby::reset_story_select_state();
}
}

Obj_80515BA0 lbl_80515BA0;
