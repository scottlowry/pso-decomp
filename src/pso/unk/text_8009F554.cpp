#include "types.h"

// TObjEneMe1Canadin boss static resources (floor_resource_callbacks pair with
// fn_8009F410 = free; descriptor bm_ene_me1_mb; spawns npc pair 0x17/0x18).

extern "C" {

// data pools (owned by other units; referenced only)
struct CanadinFloorState {
    s32 boss_param_ids[3];
    s32 handler_b_ids[3];
    s32 object_param_ids[3];
    s32 handler_a_ids[3];
    f32 fade_vals[3];
};
extern CanadinFloorState lbl_80500930;
extern const f32 lbl_805D9898; // 0.0f
extern const f32 lbl_805D98A4; // 15.0f
extern const f32 lbl_805D9930; // 8.0f
extern const u32 lbl_805D9888; // packed s16 npc id pair (0x00170018)
extern s32 lbl_8043A180[3];
extern s32 lbl_8043A18C[3];
extern s32 lbl_8043A198[3];
extern s32 lbl_8043A1A4[3];
extern s32 lbl_8043A380[4];
extern const char lbl_8043A3D0[]; // "bm_ene_me1_mb_a.bml"
extern void *bm_ene_me1_mb_resource_descriptor[4];

extern void *lbl_805D4FD0;
extern u32 lbl_805D4FD4;
extern u32 lbl_805D4FDC;
extern u32 lbl_805D4FE0;
extern u32 lbl_805D4FE4;
extern u32 lbl_805D4FE8;
extern u32 lbl_805D4FEC;
extern u32 lbl_805D4FF0;

s32 check_v2_mode__9TObjEneDDFv();
void *load_enemy_bml_resource_named(void *, const char *);
void *load_enemy_bml_resource(void *);
s32 register_boss__6TLobbyFl(s32);
s32 dispatch_shared_handler_b__6TLobbyFl(s32);
s32 register_object__6TLobbyFl(s32);
s32 dispatch_shared_handler_a__6TLobbyFl(s32);
void *__nw__FUl(u32);
s32 init_from_model__11TBreakUpMdlFl(s32, s32);
void *find_model_node__FUll(void *, s32);
void TObjPlayer__sub_800F0928();
s32 spawn_npc_enemy__6TLobbyFsllPvff(s16, s32, s32, void *, f32, f32);

void load_resources__17TObjEneMe1CanadinFv(void) {
    void *res;
    s32 i;
    s32 p;
    void *mdl;
    void *n;
    s32 ids;
    s32 sp[4];

    f32 z = lbl_805D9898;
    f32 *fade = lbl_80500930.fade_vals;
    lbl_80500930.fade_vals[0] = z;
    fade[1] = z;
    fade[2] = z;
    if (check_v2_mode__9TObjEneDDFv() != 0) {
        res = load_enemy_bml_resource_named(bm_ene_me1_mb_resource_descriptor, lbl_8043A3D0);
    } else {
        res = load_enemy_bml_resource(bm_ene_me1_mb_resource_descriptor);
    }
    lbl_805D4FD0 = res;
    s32 *s0 = lbl_8043A180;
    s32 *d0 = lbl_80500930.boss_param_ids;
    s32 *s1 = lbl_8043A18C;
    s32 *d1 = lbl_80500930.handler_b_ids;
    s32 *s2 = lbl_8043A198;
    s32 *d2 = lbl_80500930.object_param_ids;
    s32 *s3 = lbl_8043A1A4;
    s32 *d3 = lbl_80500930.handler_a_ids;
    for (i = 0; i < 3; i++) {
        d0[i] = register_boss__6TLobbyFl(s0[i]);
        d1[i] = dispatch_shared_handler_b__6TLobbyFl(s1[i]);
        d2[i] = register_object__6TLobbyFl(s2[i]);
        d3[i] = dispatch_shared_handler_a__6TLobbyFl(s3[i]);
    }
    lbl_805D4FD4 = 0;
    p = (s32)__nw__FUl(0x10);
    if (p != 0) {
        p = init_from_model__11TBreakUpMdlFl(p, *(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 0x18));
    }
    lbl_805D4FDC = p;
    p = (s32)__nw__FUl(0x10);
    if (p != 0) {
        p = init_from_model__11TBreakUpMdlFl(p, *(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 8));
    }
    lbl_805D4FE0 = p;
    mdl = (void *)*(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 0x18);
    n = find_model_node__FUll(mdl, 3);
    lbl_805D4FE4 = *(s32 *)(*(s32 *)((s32)n + 4) + 4) + 4;
    n = find_model_node__FUll(mdl, 2);
    lbl_805D4FE8 = *(s32 *)(*(s32 *)((s32)n + 4) + 4) + 4;
    mdl = (void *)*(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 8);
    n = find_model_node__FUll(mdl, 3);
    lbl_805D4FEC = *(s32 *)(*(s32 *)((s32)n + 4) + 4) + 4;
    n = find_model_node__FUll(mdl, 2);
    lbl_805D4FF0 = *(s32 *)(*(s32 *)((s32)n + 4) + 4) + 4;
    TObjPlayer__sub_800F0928();
    ids = lbl_805D9888;
    sp[0] = lbl_8043A380[0];
    sp[1] = lbl_8043A380[1];
    sp[2] = lbl_8043A380[2];
    sp[3] = lbl_8043A380[3];
    sp[0] = *(s32 *)((s32)lbl_805D4FD0 + 0x430);
    for (i = 0; i < 2; i++) {
        spawn_npc_enemy__6TLobbyFsllPvff(((s16 *)&ids)[i],
            *(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 8 + i * 0x10),
            *(s32 *)(*(s32 *)((s32)lbl_805D4FD0 + 0x42C) + 0x1C),
            &sp[0], lbl_805D9930, lbl_805D98A4);
    }
}
}
