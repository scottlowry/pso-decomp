#include "types.h"
#include "pso/misc/TWindowBase.h"
#include "pso/misc/TWindowSubStatusDisp_802671F0.h"
#include "pso/misc/TWindowMenuIconLine.h"
#include "pso/misc/TUnk_804D0948.h"
#include "pso/misc/TWindowSubStatusDisp.h"

struct RecoveredGlobal_8026E110_lbl_804D0948 {
    s32 value;
    u8 remaining[0x1C];
};

struct RecoveredGlobal_8026E168_lbl_804D0948 {
    s32 value;
    u8 remaining[0x1C];
};

extern "C" {
s32 get_draw_context__11TWindowBaseFPv();
s32 draw_visible_window_entries(void *, void *, int);
s32 draw_item_list_capacity(void *, int, int, int);
s32 draw_window_scrollbar(void *, int, void *);
s32 forward_render__20TWindowSubStatusDispFv(void *, int);
u8 * fn_80268384(void *, s32, s32, s16, s32);
s32 sub_8026DE94__13TUnk_804D0948Fv(void *, void *);
extern s32 item_list_window_vtable[];
extern s32 local_client_id;
u8 * get_window_layout_position(s32);
u8 *fn_802683F4(u8 *arg0, s32 arg1, s32 arg2, s32 arg3);
void __dl__7TObjectFPv(void *);
void * get_message_10__20TWindowSubStatusDispFl(s32);
u16 * get_array_entry__13TUnk_804CE018Fi(void *, s32);
s32 set_text_entry_string__FPUcUll(void *, void *, u32);
s32 fn_80266BD0(s32, u8 *, u8 *, s16);
void * get_entry_ptr__20TWindowSubStatusDispFi(s32);
s32 set_sprite_uv_from_pixels__FPUcff(void *, f32, f32);
s32 fn_80076BC4(s32);
s32 measure_message_text_width(void *, f32);
f32 round_away_from_zero__20TWindowSubStatusDispFf(f32);
s32 create_quest_message_window_at__Fll(s32, s32);
s32 dispatch_message_window_text__FPvii(void *, s32, s32);
s32 set_field_1c__6TLobbyFf(void *, f32);
void * get_shared_text_buffer(void);
s32 update_state__9TWindowDDFv(void *, void *, u32);
s32 refresh_status_display__9TWindowDDFv(void *);
s32 open_symbol_chat__11TWindowChatFPl(void *);
void * get_symbol_chat_data__20TWindowSubSymbolChatFv(s32);
void * __nw__7TObjectFUl(u32);
void * TWindowChatSymbol__ct(void *, void *, void *);
s32 set_selection__28TWindowSubSymbolChatPartsSetFUl(void *, u32);
extern u8 lbl_805DD34C[4];
extern const f32 lbl_805DD350;
extern const f32 lbl_805DD354;
extern const f32 lbl_805DD358;
extern const f32 lbl_805DD35C;
extern const f32 lbl_805DD360;
extern const f32 lbl_805DD364;
extern const f32 lbl_805DD368;
extern const f32 lbl_805DD36C;
extern const f32 lbl_805DD370;
extern const f32 lbl_805DD374;
extern const f32 lbl_805DD378;

#pragma push
#pragma fp_contract on
void TUnk_804D0948::render() {
    u8 *arg0 = (u8 *)this;
    s32 temp_r3;
    s32 n;
    void *p;
    temp_r3 = get_draw_context__11TWindowBaseFPv();
    ((TWindowBase *)arg0)->draw_window_frame((void *)temp_r3);
    draw_visible_window_entries(arg0, arg0 + 0x24, temp_r3);
    if (!(this->state_flags & 0x80)) {
        ((TWindowMenuIconLine *)arg0)->draw_selected_list_entry(temp_r3);
    }
    n = *(s32 *)&this->unk_88;
    if (n > 0) {
        draw_item_list_capacity(arg0, temp_r3, this->entry_count, n);
    }
    p = this->status_display;
    if (p != NULL) {
        forward_render__20TWindowSubStatusDispFv(p, temp_r3);
    }
    p = *(void * *)&this->unk_84;
    if (p != NULL) {
        draw_window_scrollbar(p, temp_r3, (u8 *)&this->m_68);
    }
}
#pragma pop

void TUnk_804D0948::run_task() { run_task__19TWindowMenuIconLineFv((u8 *)this); }

void *TWindowSubStatusDisp::deleting_dtor(s16 arg1) {
    if (this != NULL) {
        *(s32 **)((s8 *)this + 0x18) = item_list_window_vtable;
        destroy_item_list_resources(0);
        if (arg1 > 0) {
            __dl__7TObjectFPv(this);
        }
    }
    return this;
}
typedef char RecoveredGlobal_8026E110_lbl_804D0948_size[sizeof(RecoveredGlobal_8026E110_lbl_804D0948) == 0x20 ? 1 : -1];
u8 *TWindowSubStatusDisp::ct_helper(s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    fn_80268384(this, arg1, arg3, (s16) local_client_id, arg4);
    *(s32 **)((s8 *)((u8 *)this) + 0x18) = &(*(RecoveredGlobal_8026E110_lbl_804D0948 *)&item_list_window_vtable).value;
    sub_8026DE94__13TUnk_804D0948Fv(this, (void *)arg2);
    return ((u8 *)this);
}
typedef char RecoveredGlobal_8026E168_lbl_804D0948_size[sizeof(RecoveredGlobal_8026E168_lbl_804D0948) == 0x20 ? 1 : -1];
u8 *TWindowSubStatusDisp::construct_item_list(s32 arg1, s32 arg2, s16 arg3) {
    fn_802683F4((((u8 *)this)), (s32)(get_window_layout_position(0x26)), (arg2), (arg3));
    *(s32 **)((s8 *)((u8 *)this) + 0x18) = &(*(RecoveredGlobal_8026E168_lbl_804D0948 *)&item_list_window_vtable).value;
    sub_8026DE94__13TUnk_804D0948Fv(this, (void *)arg1);
    return ((u8 *)this);
}


#pragma push
#pragma fp_contract on
void TWindowSubStatusDisp__sub_8026E1D4(TWindowSubStatusDisp *self, s32 arg1, s32 *arg2) {
    f32 pos[2];
    f32 size[2];
    u8 a;
    s32 mode;
    u8 b;
    const u8 *tbl;
    u16 *e0;
    u16 *e2;
    u16 *e3;
    u16 *e4;
    u16 *e6;
    u16 *e7;
    u16 *e8;
    u16 *e10;
    void *p;
    void *q;
    void *o;
    s32 name;
    s32 chat;
    f32 g;
    f32 x0;
    f32 y0;
    e0 = get_array_entry__13TUnk_804CE018Fi(self, 0);
    e2 = get_array_entry__13TUnk_804CE018Fi(self, 2);
    e3 = get_array_entry__13TUnk_804CE018Fi(self, 3);
    e4 = get_array_entry__13TUnk_804CE018Fi(self, 4);
    e6 = get_array_entry__13TUnk_804CE018Fi(self, 6);
    e7 = get_array_entry__13TUnk_804CE018Fi(self, 7);
    e8 = get_array_entry__13TUnk_804CE018Fi(self, 8);
    e10 = get_array_entry__13TUnk_804CE018Fi(self, 10);
    mode = *arg2;
    set_text_entry_string__FPUcUll(e0, get_message_10__20TWindowSubStatusDispFl(0xc4), 0);
    fn_80266BD0(arg1, &a, &b, self->m_20);
    if (a != 0x33) {
        p = get_entry_ptr__20TWindowSubStatusDispFi(a);
        *e2 = (u16)(*e2 & 0xFFFFFFFD);
        set_sprite_uv_from_pixels__FPUcff(e2, *(f32 *)p, *(f32 *)((s8 *)p + 4));
    } else {
        *e2 = (u16)(*e2 | 2);
    }
    q = get_entry_ptr__20TWindowSubStatusDispFi(b);
    set_sprite_uv_from_pixels__FPUcff(e3, *(f32 *)q, *(f32 *)((s8 *)q + 4));
    set_text_entry_string__FPUcUll(e4, get_message_10__20TWindowSubStatusDispFl(0xc5), 0);
    set_text_entry_string__FPUcUll(e7, get_message_10__20TWindowSubStatusDispFl(mode + 0xc0), 0);
    tbl = lbl_805DD34C;
    o = get_entry_ptr__20TWindowSubStatusDispFi(tbl[mode - 1]);
    set_sprite_uv_from_pixels__FPUcff(e6, *(f32 *)o, *(f32 *)((s8 *)o + 4));
    pos[0] = lbl_805DD350;
    pos[1] = lbl_805DD354;
    q = get_message_10__20TWindowSubStatusDispFl(0x35);
    set_text_entry_string__FPUcUll(e8, q, 0);
    switch (mode) {
    case 0:
        break;
    case 1:
        name = fn_80076BC4((s32)(void *)(arg2 + 1));
        set_text_entry_string__FPUcUll(e10, (void *)name, 0);
        measure_message_text_width(e10, lbl_805DD358);
        *e10 = (u16)(*e10 | 2);
        size[0] = lbl_805DD35C + (lbl_805DD360 + *(f32 *)((s8 *)e10 + 0x10));
        size[1] = lbl_805DD364 + (lbl_805DD368 + *(f32 *)((s8 *)e10 + 0x14));
        pos[0] = round_away_from_zero__20TWindowSubStatusDispFf(pos[0] - lbl_805DD36C * size[0]);
        pos[1] = round_away_from_zero__20TWindowSubStatusDispFf(pos[1] - lbl_805DD36C * size[1]);
        self->m_64 = create_quest_message_window_at__Fll((s32)(void *)pos, (s32)(void *)size);
        dispatch_message_window_text__FPvii((void *)self->m_64, name, 0x402);
        set_field_1c__6TLobbyFf((void *)self->m_64, lbl_805DD370);
        break;
    case 2:
        update_state__9TWindowDDFv((void *)(arg2 + 1), get_shared_text_buffer(), (u32)(u16)local_client_id);
        set_text_entry_string__FPUcUll(e10, get_shared_text_buffer(), 0);
        refresh_status_display__9TWindowDDFv(e10);
        *e10 = (u16)(*e10 | 2);
        size[0] = lbl_805DD35C + (lbl_805DD360 + *(f32 *)((s8 *)e10 + 0x10));
        size[1] = lbl_805DD364 + (lbl_805DD368 + *(f32 *)((s8 *)e10 + 0x14));
        pos[0] = round_away_from_zero__20TWindowSubStatusDispFf(pos[0] - lbl_805DD36C * size[0]);
        pos[1] = round_away_from_zero__20TWindowSubStatusDispFf(pos[1] - lbl_805DD36C * size[1]);
        self->m_64 = create_quest_message_window_at__Fll((s32)(void *)pos, (s32)(void *)size);
        dispatch_message_window_text__FPvii((void *)self->m_64, (s32)(void *)get_shared_text_buffer(), 2);
        set_field_1c__6TLobbyFf((void *)self->m_64, lbl_805DD370);
        break;
    case 3:
        chat = open_symbol_chat__11TWindowChatFPl((void *)(arg2 + 1));
        set_text_entry_string__FPUcUll(e10, get_symbol_chat_data__20TWindowSubSymbolChatFv(chat), 0);
        g = lbl_805DD36C;
        x0 = pos[0] - lbl_805DD374 * g;
        size[0] = lbl_805DD374;
        pos[0] = x0;
        y0 = pos[1] - lbl_805DD378 * g;
        size[1] = lbl_805DD378;
        pos[1] = y0;
        o = __nw__7TObjectFUl(0x68);
        if (o != NULL) {
            o = TWindowChatSymbol__ct(o, pos, size);
        }
        self->m_68 = (u32)o;
        set_selection__28TWindowSubSymbolChatPartsSetFUl((void *)self->m_68, (u32)chat);
        set_field_1c__6TLobbyFf((void *)self->m_68, lbl_805DD370);
        break;
    }
}
#pragma pop

}
