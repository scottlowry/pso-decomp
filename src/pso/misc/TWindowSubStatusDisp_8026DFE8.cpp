#include "types.h"
#include "pso/misc/TWindowBase.h"
#include "pso/misc/TWindowSubStatusDisp_802671F0.h"
#include "pso/misc/TWindowMenuIconLine.h"
#include "pso/misc/TUnk_804D0948.h"
#include "pso/misc/TWindowSubStatusDisp.h"
#include "pso/misc/TWindowChatSymbol_802486A8.h"

struct RecoveredGlobal_8026E110_lbl_804D0948 {
    s32 value;
    u8 remaining[0x1C];
};

struct RecoveredGlobal_8026E168_lbl_804D0948 {
    s32 value;
    u8 remaining[0x1C];
};

struct Msg_8026E1D4 {
    u16 flags;
    u8 pad2[0x10 - 2];
    f32 width;
    f32 height;
};

struct Stack_8026E1D4 {
    f32 spC;
    f32 sp10;
    f32 sp14;
    f32 sp18;
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
s32 get_array_entry__11TWindowBaseFi(void *, s16);
s32 get_message_10__20TWindowSubStatusDispFl(s32);
void fn_80266BD0(s32 index, u8 *first, u8 *second, s32 player);
s32 get_entry_ptr__20TWindowSubStatusDispFi(s32);
void set_text_entry_string__FPUcUll(u8 *, u32, s32);
void set_sprite_uv_from_pixels__FPUcff(u8 *, f32, f32);
s32 fn_80076BC4(s32 *);
void measure_message_text_width(Msg_8026E1D4 *, f32);
f32 round_away_from_zero__20TWindowSubStatusDispFf(f32);
s32 create_quest_message_window_at__Fll(s32, s32);
void dispatch_message_window_text__FPvii(void *, s32, s32);
s32 *get_shared_text_buffer(void);
void update_state__9TWindowDDFv(s32 *, s32, u16);
void refresh_status_display__9TWindowDDFv(void *);
s32 open_symbol_chat__11TWindowChatFPl(s32 *);
s32 get_symbol_chat_data__20TWindowSubSymbolChatFv();
void *set_selection__28TWindowSubSymbolChatPartsSetFUl(void *, u32);
void *__nw__7TObjectFUl(int);
extern const u8 lbl_805DD34C[4];
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
#pragma opt_common_subs off
void TWindowSubStatusDisp__sub_8026E1D4(TWindowSubStatusDisp *self, s32 index, s32 *chat_shortcut) {
    s32 e0;
    s32 e2;
    s32 e3;
    s32 e4;
    s32 e6;
    s32 e7;
    s32 e8;
    s32 e10;
    s32 mode;
    u8 sp9;
    u8 sp8;
    Stack_8026E1D4 stack;
    f32 *pt;
    s32 v;
    void *w;

    e0 = get_array_entry__11TWindowBaseFi(self, 0);
    e2 = get_array_entry__11TWindowBaseFi(self, 2);
    e3 = get_array_entry__11TWindowBaseFi(self, 3);
    e4 = get_array_entry__11TWindowBaseFi(self, 4);
    e6 = get_array_entry__11TWindowBaseFi(self, 6);
    e7 = get_array_entry__11TWindowBaseFi(self, 7);
    e8 = get_array_entry__11TWindowBaseFi(self, 8);
    e10 = get_array_entry__11TWindowBaseFi(self, 10);
    mode = *chat_shortcut;
    set_text_entry_string__FPUcUll((u8 *)e0, (u32)get_message_10__20TWindowSubStatusDispFl(0xc4), 0);
    fn_80266BD0(index, &sp9, &sp8, self->m_20);
    if (sp9 != 0x33) {
        pt = (f32 *)get_entry_ptr__20TWindowSubStatusDispFi(sp9);
        ((Msg_8026E1D4 *)e2)->flags &= ~2;
        set_sprite_uv_from_pixels__FPUcff((u8 *)e2, pt[0], pt[1]);
    } else {
        ((Msg_8026E1D4 *)e2)->flags |= 2;
    }
    pt = (f32 *)get_entry_ptr__20TWindowSubStatusDispFi(sp8);
    set_sprite_uv_from_pixels__FPUcff((u8 *)e3, pt[0], pt[1]);
    set_text_entry_string__FPUcUll((u8 *)e4, (u32)get_message_10__20TWindowSubStatusDispFl(0xc5), 0);
    set_text_entry_string__FPUcUll((u8 *)e7, (u32)get_message_10__20TWindowSubStatusDispFl(mode + 0xc0), 0);
    pt = (f32 *)get_entry_ptr__20TWindowSubStatusDispFi(lbl_805DD34C[mode - 1]);
    set_sprite_uv_from_pixels__FPUcff((u8 *)e6, pt[0], pt[1]);
    stack.sp14 = lbl_805DD350;
    stack.sp18 = lbl_805DD354;
    set_text_entry_string__FPUcUll((u8 *)e8, (u32)get_message_10__20TWindowSubStatusDispFl(0x35), 0);
    switch (mode) {
    case 0:
        break;
    case 1:
        v = fn_80076BC4(chat_shortcut + 1);
        set_text_entry_string__FPUcUll((u8 *)e10, (u32)v, 0);
        measure_message_text_width((Msg_8026E1D4 *)e10, lbl_805DD358);
        ((Msg_8026E1D4 *)e10)->flags |= 2;
        stack.spC = lbl_805DD35C + (lbl_805DD360 + ((Msg_8026E1D4 *)e10)->width);
        stack.sp10 = lbl_805DD364 + (lbl_805DD368 + ((Msg_8026E1D4 *)e10)->height);
        stack.sp14 = round_away_from_zero__20TWindowSubStatusDispFf(stack.sp14 - lbl_805DD36C * stack.spC);
        stack.sp18 = round_away_from_zero__20TWindowSubStatusDispFf(stack.sp18 - lbl_805DD36C * stack.sp10);
        w = (void *)create_quest_message_window_at__Fll((s32)&stack.sp14, (s32)&stack.spC);
        self->m_64 = (u32)w;
        dispatch_message_window_text__FPvii((void *)self->m_64, v, 0x402);
        ((TWindowBase *)self->m_64)->set_depth(lbl_805DD370);
        break;
    case 2:
        update_state__9TWindowDDFv(chat_shortcut + 1, (s32)get_shared_text_buffer(), (u16)local_client_id);
        set_text_entry_string__FPUcUll((u8 *)e10, (u32)get_shared_text_buffer(), 0);
        refresh_status_display__9TWindowDDFv((void *)e10);
        ((Msg_8026E1D4 *)e10)->flags |= 2;
        stack.spC = lbl_805DD35C + (lbl_805DD360 + ((Msg_8026E1D4 *)e10)->width);
        stack.sp10 = lbl_805DD364 + (lbl_805DD368 + ((Msg_8026E1D4 *)e10)->height);
        stack.sp14 = round_away_from_zero__20TWindowSubStatusDispFf(stack.sp14 - lbl_805DD36C * stack.spC);
        stack.sp18 = round_away_from_zero__20TWindowSubStatusDispFf(stack.sp18 - lbl_805DD36C * stack.sp10);
        w = (void *)create_quest_message_window_at__Fll((s32)&stack.sp14, (s32)&stack.spC);
        self->m_64 = (u32)w;
        dispatch_message_window_text__FPvii((void *)self->m_64, (s32)get_shared_text_buffer(), 2);
        ((TWindowBase *)self->m_64)->set_depth(lbl_805DD370);
        break;
    case 3:
        v = open_symbol_chat__11TWindowChatFPl(chat_shortcut + 1);
        set_text_entry_string__FPUcUll((u8 *)e10, (u32)get_symbol_chat_data__20TWindowSubSymbolChatFv(), 0);
        stack.sp14 = stack.sp14 - lbl_805DD36C * lbl_805DD374;
        stack.spC = lbl_805DD374;
        stack.sp18 = stack.sp18 - lbl_805DD36C * lbl_805DD378;
        stack.sp10 = lbl_805DD378;
        w = __nw__7TObjectFUl(0x68);
        if (w != 0) {
            w = (void *)TWindowChatSymbol__ct((TWindowChatSymbol *)w, (s32)&stack.sp14, (s32)&stack.spC);
        }
        self->m_68 = (u32)w;
        set_selection__28TWindowSubSymbolChatPartsSetFUl((void *)self->m_68, (u32)v);
        ((TWindowBase *)self->m_68)->set_depth(lbl_805DD370);
        break;
    }
}
#pragma pop

}
