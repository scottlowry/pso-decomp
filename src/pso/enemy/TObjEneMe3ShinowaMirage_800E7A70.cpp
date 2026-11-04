#include "pso/misc/SampledMotionPoints.h"
#include "types.h"
#include "pso/enemy/TObjEneMe3ShinowaMirage_800E7A70.h"
#include "pso/enemy/TObjEneMe3ShinowaMirage.h"
#include "pso/system/NinjaUtil.h"

struct Node_800E7B94 { s32 f0; s32 f4; };
struct Vec3i_800E7B94 { s32 x, y, z; };
struct MotArr_800E7B94 { Vec3i_800E7B94 *p; u32 n; };
struct Bml_800E7B94 { u8 pad[0x42C]; u8 *f42C; Node_800E7B94 *f430; };
struct MirTbl_800E7B94 { u8 pad[0x44]; s32 f44; u8 pad48[0xC]; s32 f54; u8 pad58[0xC]; s32 f64; };

struct RecoveredGlobal_8031B170_lbl_804E8880
{
  s32 value;
  u8 remaining[0xCC];
};

struct VB_800E7A98 { u8 pad[0xC]; };

struct VO_800E7A98 : VB_800E7A98 { virtual ~VO_800E7A98(); };

extern "C" {
extern RecoveredGlobal_8031B170_lbl_804E8880 shinowa_mirage_motion_param_table;
extern const f32 TObjEneMe3ShinowaMirage__data_805DA5C4;
s32 TLobby__sub_8001FE7C(void *, s32);
void mem_free(void *p);
extern void *lbl_80500FEC[];
extern void *TObjEneMe3ShinowaMirage__data_805D5298;
extern VO_800E7A98 *TObjEneMe3ShinowaMirage__data_805D52A0;
extern void *TObjEneMe3ShinowaMirage__data_805D52A4;
extern void *TObjEneMe3ShinowaMirage__data_805D52A8;
extern void *TObjEneMe3ShinowaMirage__data_805D52AC;
int create__21TObjEneMe3ShinowaRealFv(void*);

typedef struct RecoveredGlobal_8031B170_lbl_804E8880 RecoveredGlobal_8031B170_lbl_804E8880;
typedef char RecoveredGlobal_8031B170_lbl_804E8880_size[((sizeof(RecoveredGlobal_8031B170_lbl_804E8880)) == 0xD0) ? (1) : (-1)];
void TObjEneMe3ShinowaMirage::set_slot_min_clamped_value(s32 arg0, f32 farg0) {
  u8 *new_var;
  f32 var_f1;
  var_f1 = farg0;
  if (var_f1 < TObjEneMe3ShinowaMirage__data_805DA5C4)
  {
    var_f1 = TObjEneMe3ShinowaMirage__data_805DA5C4;
  }
  new_var = (u8 *)&shinowa_mirage_motion_param_table.value;
  new_var = new_var + (arg0 * 0x10);
  *((f32 *) (((s8 *) new_var) + 8)) = var_f1;
}

void TObjEneMe3ShinowaMirage::free_shared_resources() {
    if (TObjEneMe3ShinowaMirage__data_805D52A8 != 0) {
        delete (SampledMotionPoints *)TObjEneMe3ShinowaMirage__data_805D52A8;
        TObjEneMe3ShinowaMirage__data_805D52A8 = 0;
    }
    if (TObjEneMe3ShinowaMirage__data_805D52A4 != 0) {
        delete (SampledMotionPoints *)TObjEneMe3ShinowaMirage__data_805D52A4;
        TObjEneMe3ShinowaMirage__data_805D52A4 = 0;
    }
    if (TObjEneMe3ShinowaMirage__data_805D52AC != 0) {
        delete (SampledMotionPoints *)TObjEneMe3ShinowaMirage__data_805D52AC;
        TObjEneMe3ShinowaMirage__data_805D52AC = 0;
    }
    if (TObjEneMe3ShinowaMirage__data_805D52A0 != 0) {
        delete TObjEneMe3ShinowaMirage__data_805D52A0;
        TObjEneMe3ShinowaMirage__data_805D52A0 = 0;
    }
    if (lbl_80500FEC[0] != 0) {
        mem_free(lbl_80500FEC[0]);
        lbl_80500FEC[0] = 0;
    }
    if (TObjEneMe3ShinowaMirage__data_805D5298 != 0) {
        TLobby__sub_8001FE7C(TObjEneMe3ShinowaMirage__data_805D5298, 1);
        TObjEneMe3ShinowaMirage__data_805D5298 = 0;
    }
}

int TObjEneMe3ShinowaMirage__sub_800E7B74(void* p) { return create__21TObjEneMe3ShinowaRealFv(p); }

extern f32 TObjEneMe3ShinowaMirage__data_80500FC0[20];
extern s32 TObjEneMe3ShinowaMirage__render_node_index;
extern s32 lbl_8043CE1C[];
extern s32 lbl_8043CE24[];
extern s32 lbl_8043CE2C[];
extern s32 lbl_8043CE34[];
extern s32 lbl_8043CF84[];
extern const f64 lbl_8043CFA0;
extern const u8 lbl_8043CFE8[];
extern const f32 TObjEneMe3ShinowaMirage__data_805DA5B8;
extern const f32 lbl_805DA5D0;
extern const f32 TObjEneMe3ShinowaMirage__data_805DA5E8;
extern const f32 lbl_805DA614;
extern const f32 lbl_805DA61C;
extern const f32 lbl_805DA650;
extern const f32 lbl_805DA654;
extern const f32 lbl_805DA658;
extern const f32 lbl_805DA65C;
extern const f32 lbl_805DA660;
extern const f32 lbl_805DA664;
extern void *TObjEneMe3ShinowaMirage__data_805D52A4;
extern void *TObjEneMe3ShinowaMirage__data_805D52A8;
extern void *TObjEneMe3ShinowaMirage__data_805D52AC;
extern void *shinowa_mirage_resource_descriptor[4];
s32 check_v2_mode__9TObjEneDDFv(void);
s32 load_enemy_bml_resource(void *desc);
s32 load_enemy_bml_resource_named(void *desc, const void *name);
void *mem_alloc(u32 size);
void copy_vec3__10TObjPlayerFPv(void *self, void *src);
s32 register_boss__6TLobbyFl(s32);
s32 dispatch_shared_handler_b__6TLobbyFl(s32);
s32 register_object__6TLobbyFl(s32);
s32 dispatch_shared_handler_a__6TLobbyFl(s32);
void *init__11TBreakUpMdlFPviif(void *self, s32 arg1, s32 arg2, f32 farg0);

#define mirage_list (sh + 11)
#define mirage_f32 ((f32 *)sh)
#define mirage_s32 sh
#define mirage_info (sh + 9)
#define mirage_spawn ((f32 *)sh + 13)
#define mirage_colors (sh + 16)
s32 spawn_npc_enemy__6TLobbyFsllPvff(s16, s32, s32, void *, f32, f32);

void TObjEneMe3ShinowaMirage__sub_800E7B94(void) {
    s32 *sh;
    s32 i;
    s32 n;
    s32 idx;
    MotArr_800E7B94 *src;
    Bml_800E7B94 *res;
    s32 *d;
    u32 mdl;
    s32 *q;
    u8 *ent;
    void *p;
    f32 step;
    Vec first;
    Vec second;
    s32 desc[4];

    sh = (s32 *)TObjEneMe3ShinowaMirage__data_80500FC0;
    mirage_f32[0] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    mirage_f32[1] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    mirage_f32[2] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    if (check_v2_mode__9TObjEneDDFv() != 0) {
        TObjEneMe3ShinowaMirage__data_805D5298 = (void *)load_enemy_bml_resource_named(shinowa_mirage_resource_descriptor, lbl_8043CFE8);
    } else {
        TObjEneMe3ShinowaMirage__data_805D5298 = (void *)load_enemy_bml_resource(shinowa_mirage_resource_descriptor);
    }
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    src = *(MotArr_800E7B94 **)(res->f42C + 0xC);
    n = src->n;
    mirage_list[1] = n;
    mirage_list[0] = (s32)mem_alloc(n * 0xC);
    for (i = 0; i < n; i++) {
        copy_vec3__10TObjPlayerFPv((void *)&((Vec3i_800E7B94 *)mirage_list[0])[i], (void *)&src->p[i]);
    }
    for (i = 0; i < 3; i++) {
        ((Vec3i_800E7B94 *)mirage_list[0])[i + 3].z = ((Vec3i_800E7B94 *)mirage_list[0])[i].z;
    }
    for (i = 0; i < 2; i++) {
        mirage_s32[3 + i] = register_boss__6TLobbyFl(lbl_8043CE1C[i]);
    }
    for (i = 0; i < 2; i++) {
        mirage_s32[5 + i] = dispatch_shared_handler_b__6TLobbyFl(lbl_8043CE24[i]);
    }
    for (i = 0; i < 2; i++) {
        mirage_s32[7 + i] = register_object__6TLobbyFl(lbl_8043CE2C[i]);
    }
    for (i = 0; i < 2; i++) {
        mirage_s32[9 + i] = dispatch_shared_handler_a__6TLobbyFl(lbl_8043CE34[i]);
    }
    d = (s32 *)mirage_info[0];
    TObjEneMe3ShinowaMirage::set_slot_min_clamped_value(6, *(f32 *)((s8 *)d + 0xC));
    TObjEneMe3ShinowaMirage::set_slot_min_clamped_value(3, *(f32 *)((s8 *)d + 0x10));
    TObjEneMe3ShinowaMirage__render_node_index = 0;
    mirage_spawn[0] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    mirage_spawn[1] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    mirage_spawn[2] = TObjEneMe3ShinowaMirage__data_805DA5B8;
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    mdl = *(u32 *)(res->f42C + 8);
    q = (s32 *)((NJS_OBJECT *)find_model_node(mdl, 9))->model;
    if (q != NULL) {
        mirage_colors[0] = q[1] + 4;
    } else {
        mirage_colors[0] = 0;
    }
    q = (s32 *)((NJS_OBJECT *)find_model_node(mdl, 0xD))->model;
    if (q != NULL) {
        mirage_colors[1] = q[1] + 4;
    } else {
        mirage_colors[1] = 0;
    }
    q = (s32 *)((NJS_OBJECT *)find_model_node(mdl, 0x26))->model;
    if (q != NULL) {
        mirage_colors[2] = q[1] + 4;
    } else {
        mirage_colors[2] = 0;
    }
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    ent = (u8 *)(res->f430 + ((MirTbl_800E7B94 *)&shinowa_mirage_motion_param_table)->f44)->f4;
    p = ::operator new(0x10);
    if (p != NULL) {
        p = init__11TBreakUpMdlFPviif(p, *(s32 *)(res->f42C + 8), (s32)ent, (f32)(*(u32 *)(ent + 4) - 1));
    }
    TObjEneMe3ShinowaMirage__data_805D52A0 = (VO_800E7A98 *)p;
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    idx = ((MirTbl_800E7B94 *)&shinowa_mirage_motion_param_table)->f54;
    mdl = *(u32 *)(res->f42C + 8);
    first.x = TObjEneMe3ShinowaMirage__data_805DA5B8;
    first.y = TObjEneMe3ShinowaMirage__data_805DA5B8;
    first.z = TObjEneMe3ShinowaMirage__data_805DA5B8;
    second.x = lbl_805DA654;
    second.y = TObjEneMe3ShinowaMirage__data_805DA5B8;
    second.z = TObjEneMe3ShinowaMirage__data_805DA5B8;
    ent = (u8 *)(res->f430 + idx)->f4;
    p = new SampledMotionPoints(2, lbl_805DA658, lbl_805DA65C, lbl_805DA660);
    TObjEneMe3ShinowaMirage__data_805D52AC = p;
    ((SampledMotionPoints *)p)->sample_node_offsets((NJS_OBJECT *)mdl, (NJS_MOTION *)ent, 0x22, (const Vec *)&first, (const Vec *)&second);
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    ent = (u8 *)(res->f430 + ((MirTbl_800E7B94 *)&shinowa_mirage_motion_param_table)->f64)->f4;
    d = (s32 *)mirage_info[0];
    step = *(f32 *)((s8 *)d + 0xC);
    if (step < TObjEneMe3ShinowaMirage__data_805DA5C4) {
        step = TObjEneMe3ShinowaMirage__data_805DA5C4;
    }
    first.x = TObjEneMe3ShinowaMirage__data_805DA5B8;
    first.y = TObjEneMe3ShinowaMirage__data_805DA5B8;
    first.z = TObjEneMe3ShinowaMirage__data_805DA5B8;
    second.x = lbl_805DA654;
    second.y = TObjEneMe3ShinowaMirage__data_805DA5B8;
    second.z = TObjEneMe3ShinowaMirage__data_805DA5B8;
    p = new SampledMotionPoints(2, lbl_805DA664, lbl_805DA614, step);
    TObjEneMe3ShinowaMirage__data_805D52A4 = p;
    ((SampledMotionPoints *)p)->sample_node_offsets((NJS_OBJECT *)mdl, (NJS_MOTION *)ent, 0x22, (const Vec *)&first, (const Vec *)&second);
    second.x = TObjEneMe3ShinowaMirage__data_805DA5E8;
    second.y = TObjEneMe3ShinowaMirage__data_805DA5B8;
    second.z = TObjEneMe3ShinowaMirage__data_805DA5B8;
    p = new SampledMotionPoints(2, lbl_805DA5D0, lbl_805DA61C, step);
    TObjEneMe3ShinowaMirage__data_805D52A8 = p;
    ((SampledMotionPoints *)p)->sample_node_offsets((NJS_OBJECT *)mdl, (NJS_MOTION *)ent, 0x15, (const Vec *)&first, (const Vec *)&second);
    res = (Bml_800E7B94 *)TObjEneMe3ShinowaMirage__data_805D5298;
    desc[0] = lbl_8043CF84[0];
    desc[1] = lbl_8043CF84[1];
    desc[2] = lbl_8043CF84[2];
    desc[3] = lbl_8043CF84[3];
    desc[0] = *(s32 *)res->f430;
    spawn_npc_enemy__6TLobbyFsllPvff(0x26, *(s32 *)(res->f42C + 8), *(s32 *)(res->f42C + 0xC), desc, lbl_805DA650, TObjEneMe3ShinowaMirage__data_805DA5B8);
    spawn_npc_enemy__6TLobbyFsllPvff(0x27, *(s32 *)(res->f42C + 8), (s32)mirage_list, desc, lbl_805DA650, TObjEneMe3ShinowaMirage__data_805DA5B8);
}
#undef mirage_list
#undef mirage_f32
#undef mirage_s32
#undef mirage_info
#undef mirage_spawn
#undef mirage_colors

}
