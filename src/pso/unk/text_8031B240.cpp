#include "types.h"

extern "C" {

struct SinowZoaCtrl {
    /* 0x00 */ f32 f00[3];
    /* 0x0C */ s32 boss_ids[2];
    /* 0x14 */ s32 handler_b_ids[2];
    /* 0x1C */ s32 object_ids[2];
    /* 0x24 */ s32 handler_a_ids[2];
    /* 0x2C */ void *alloc;
    /* 0x30 */ s32 count;
    /* 0x34 */ f32 f34[3];
    /* 0x40 */ s32 nodes[3];
    /* 0x4C */ u8 pad_4C[0x42C - 0x4C];
    /* 0x42C */ void *res;
    /* 0x430 */ s32 word_430;
};

struct MdlNode {
    u8 pad_0[4];
    u32 node;
};

struct Pos4 {
    s32 w[4];
};

extern SinowZoaCtrl lbl_80542FB0;
extern void *TObjEneMe3SinowZoa_init_params[7];
extern volatile u8 *TObjEneMe3SinowZoa__data_805D6AD8;
extern s32 TObjEneMe3SinowZoa__data_805D6AE0;
extern s32 lbl_805D6ADC;
extern const f32 TObjEneMe3SinowZoa__data_805DF2FC;
extern const f32 TObjEneMe3SinowZoa__data_805DF31C;
extern const f64 lbl_80476098;
extern const s32 lbl_80475E0C[2];
extern const s32 lbl_80475E14[2];
extern const s32 lbl_80475E1C[2];
extern const s32 lbl_80475E24[2];
extern const Pos4 lbl_80475FA8;
extern const Pos4 lbl_80475FB8;

s32 is_split_screen(void);
s32 load_enemy_bml_resource(u8 *arg0);
void *mem_alloc(u32 size);
void copy_vec3__10TObjPlayerFPv(void *self, void *p);
s32 register_boss__6TLobbyFl(s32);
s32 dispatch_shared_handler_b__6TLobbyFl(s32);
s32 register_object__6TLobbyFl(s32);
s32 dispatch_shared_handler_a__6TLobbyFl(s32);
void set_entry_value_clamped__18TObjEneMe3SinowZoaFlf(s32, f32);
void *find_model_node__FUll(void *, s32);
void *init__11TBreakUpMdlFPviif(void *, s32, s32, f64);
s32 spawn_npc_enemy__6TLobbyFsllPvff(s16, s64, s64, void *, f32, f32);

void TObjEneMe3SinowZoa__sub_8031B240(void) {
    u8 *init_base = (u8 *)TObjEneMe3SinowZoa_init_params;
    SinowZoaCtrl *ctrl = &lbl_80542FB0;
    f32 zero_f = TObjEneMe3SinowZoa__data_805DF31C;
    void *res;
    u8 *mgr;
    u8 *tbl;
    s32 count;
    s32 i;
    s32 off;
    void *p;
    MdlNode *mn;
    s32 model;
    s32 mdl2;
    s32 idx;
    volatile s32 *sum;
    volatile s32 *np;
    volatile s32 *cp;
    volatile f32 *w0;
    volatile f32 *w34;
    volatile s32 *fa;
    volatile s32 *desc;
    MdlNode *child;
    Pos4 pos2;
    Pos4 pos1;

    w0 = (volatile f32 *)ctrl->f00;
    ctrl->f00[0] = zero_f;
    w0[1] = zero_f;
    w0[2] = zero_f;
    if (is_split_screen() != 0) {
        res = (void *)load_enemy_bml_resource(init_base + 0xC8);
    } else {
        res = (void *)load_enemy_bml_resource(init_base + 0x80);
    }
    TObjEneMe3SinowZoa__data_805D6AD8 = (u8 *)res;
    cp = (volatile s32 *)&ctrl->alloc;
    mgr = *(u8 **)((u8 *)res + 0x42C);
    tbl = *(u8 **)(mgr + 0xC);
    count = *(s32 *)(tbl + 4);
    cp[1] = count;
    ctrl->alloc = mem_alloc((u32)(count * 12));
    off = 0;
    i = 0;
    for (; i < count; i++, off += 12) {
        copy_vec3__10TObjPlayerFPv((u8 *)ctrl->alloc + off, *(u8 **)tbl + off);
    }
    for (i = 0; i < 3; i++) {
        *(s32 *)((u8 *)ctrl->alloc + (s32)i * 12 + 8) =
            *(s32 *)((u8 *)ctrl->alloc + (s32)i * 12 + 0x2C);
    }
    {
        volatile s32 *dp = ctrl->boss_ids;
        const s32 *sp = lbl_80475E0C;
        for (i = 0; i < 2; i++) {
            dp[i] = register_boss__6TLobbyFl(sp[i]);
        }
    }
    {
        volatile s32 *dp = ctrl->handler_b_ids;
        const s32 *sp = lbl_80475E14;
        for (i = 0; i < 2; i++) {
            dp[i] = dispatch_shared_handler_b__6TLobbyFl(sp[i]);
        }
    }
    {
        volatile s32 *dp = ctrl->object_ids;
        const s32 *sp = lbl_80475E1C;
        for (i = 0; i < 2; i++) {
            dp[i] = register_object__6TLobbyFl(sp[i]);
        }
    }
    {
        const s32 *sp = lbl_80475E24;
        volatile s32 *dp = ctrl->handler_a_ids;
        for (i = 0; i < 2; i++) {
            dp[i] = dispatch_shared_handler_a__6TLobbyFl(sp[i]);
        }
    }
    {
        volatile s32 *nb = ctrl->handler_a_ids;
        mn = (MdlNode *)nb[0];
        set_entry_value_clamped__18TObjEneMe3SinowZoaFlf(7, *(f32 *)((u8 *)mn + 0xC));
        set_entry_value_clamped__18TObjEneMe3SinowZoaFlf(4, *(f32 *)((u8 *)mn + 0x10));
    }
    zero_f = TObjEneMe3SinowZoa__data_805DF31C;
    w34 = (volatile f32 *)ctrl->f34;
    lbl_805D6ADC = 0;
    w34[0] = zero_f;
    w34[1] = zero_f;
    w34[2] = zero_f;
    res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
    mgr = *(u8 **)((u8 *)res + 0x42C);
    model = *(s32 *)(mgr + 8);
    mn = (MdlNode *)find_model_node__FUll((void *)model, 9);
    child = (MdlNode *)mn->node;
    ctrl->nodes[0] = (child != 0) ? ((*(s32 *)((u8 *)child + 4)) + 4) : 0;
    np = (volatile s32 *)ctrl->nodes;
    mn = (MdlNode *)find_model_node__FUll((void *)model, 0xD);
    child = (MdlNode *)mn->node;
    if (child != 0) {
        np[1] = (*(s32 *)((u8 *)child + 4)) + 4;
    } else {
        np[1] = 0;
    }
    mn = (MdlNode *)find_model_node__FUll((void *)model, 0x26);
    child = (MdlNode *)mn->node;
    if (child != 0) {
        np[2] = (*(s32 *)((u8 *)child + 4)) + 4;
    } else {
        np[2] = 0;
    }
    res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
    desc = (volatile s32 *)(init_base + 0xD8);
    idx = desc[0x15];
    mgr = *(u8 **)((u8 *)res + 0x430);
    sum = (volatile s32 *)(mgr + ((u32)idx << 3));
    mdl2 = sum[1];
    p = ::operator new(0x10);
    if (p != 0) {
        res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
        mgr = *(u8 **)((u8 *)res + 0x42C);
        p = init__11TBreakUpMdlFPviif(p, *(s32 *)(mgr + 8), mdl2,
                                      (f64)(u32)(*(s32 *)((u8 *)mdl2 + 4) - 1));
    }
    TObjEneMe3SinowZoa__data_805D6AE0 = (s32)p;
    res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
    mgr = *(u8 **)((u8 *)res + 0x42C);
    fa = (volatile s32 *)&lbl_80475FA8;
    pos2.w[0] = fa[0];
    pos2.w[1] = fa[1];
    pos2.w[2] = fa[2];
    pos2.w[3] = fa[3];
    fa = (volatile s32 *)&lbl_80475FB8;
    pos1.w[0] = fa[0];
    pos1.w[1] = fa[1];
    pos1.w[2] = fa[2];
    pos1.w[3] = fa[3];
    pos2.w[0] = *(s32 *)((u8 *)res + 0x430);
    pos1.w[0] = *(s32 *)((u8 *)res + 0x430);
    spawn_npc_enemy__6TLobbyFsllPvff(0x49, (s64)*(s32 *)(mgr + 8), (s64)*(s32 *)(mgr + 0xC),
                                     &pos1.w[0], TObjEneMe3SinowZoa__data_805DF2FC,
                                     TObjEneMe3SinowZoa__data_805DF31C);
    spawn_npc_enemy__6TLobbyFsllPvff(0x4A, (s64)*(s32 *)(mgr + 8), (s64)(u32)ctrl->alloc,
                                     &pos2.w[0], TObjEneMe3SinowZoa__data_805DF2FC,
                                     TObjEneMe3SinowZoa__data_805DF31C);
    res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
    mgr = *(u8 **)((u8 *)res + 0x42C);
    spawn_npc_enemy__6TLobbyFsllPvff(0x4B, (s64)*(s32 *)(mgr + 8), (s64)*(s32 *)(mgr + 0xC),
                                     &pos1.w[0], TObjEneMe3SinowZoa__data_805DF2FC,
                                     TObjEneMe3SinowZoa__data_805DF31C);
    res = (void *)TObjEneMe3SinowZoa__data_805D6AD8;
    mgr = *(u8 **)((u8 *)res + 0x42C);
    spawn_npc_enemy__6TLobbyFsllPvff(0x4C, (s64)*(s32 *)(mgr + 8), (s64)(u32)ctrl->alloc,
                                     &pos2.w[0], TObjEneMe3SinowZoa__data_805DF2FC,
                                     TObjEneMe3SinowZoa__data_805DF31C);
}

}
