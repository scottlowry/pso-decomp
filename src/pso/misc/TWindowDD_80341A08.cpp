#include "types.h"
#include "pso/misc/TWindowDD_WS_Word.h"
#include "pso/misc/TWindowDD_803488A8.h"
#include "pso/misc/TWindowSubStatusDisp_8025A9B4.h"
#include "pso/misc/TWindowDD_80341A08.h"
#include "pso/misc/TWindowBase.h"

#include "pso/misc/TWindowDD.h"
#include "pso/misc/TWindowHelpItem.h"
#include "pso/misc/TWindowKeyBoardSoft.h"
#include "pso/misc/TUnk_804CFA28.h"

extern "C" {
int refresh_status_display__9TWindowDDFv(void *);
void TWindowDD__sub_80341674(TWindowDD_WS_Word *, u8 *);
void draw_visible_window_entries(TWindowDD_WS_Word *, TWindowDDWordEntryList *, TWindowKeyBoardSoft *);
extern const s32 TWindowDD__data_805DFC14;
extern const s32 lbl_805DFC18;
extern const f32 lbl_805DFCA0;
}

void TWindowDD_WS_Word::render() {
    TWindowDD_WS_Word *self = this;
    TWindowKeyBoardSoft *entry;
    TUnk_804CFA28 *item;
    s32 idx;
    s32 i;
    s32 j;
    entry = (TWindowKeyBoardSoft *)TWindowDD::draw_default_entry((s32)self);
    self->calc_inner_rect((u8 *)entry);
    TWindowDD__sub_80341674(self, (u8 *)entry);
    if (self->m_8c != 0) {
        self->m_8c = 0;
        idx = self->m_68 - self->m_6c;
        for (i = 0; i < self->m_7c; i++, idx++) {
            item = (TUnk_804CFA28 *)self->get_array_entry(i);
            set_text_entry_string((u8 *)item, TWindowDD__sub_80348B70(((s16 *)self->m_80)[idx]), 0xC0);
            item->y = (f32)(i * 20);
            refresh_status_display__9TWindowDDFv(item);
            ((TWindowHelpItem *)item)->reset_float_field();
            item->color = TWindowDD__data_805DFC14;
        }
        if (self->sub_80342254() != 0) {
            for (j = 0; j < self->m_7c; j++) {
                item = (TUnk_804CFA28 *)self->get_array_entry(j);
                if (j == self->m_6c) {
                    item->color = lbl_805DFC18;
                }
            }
        }
    }
    entry->inner_y += lbl_805DFCA0;
    draw_visible_window_entries(self, &self->entries, entry);
}

struct E_80341674 { f32 v[12]; };

extern "C" {
void reset_entries__9TWindowDDFf(void *, s32);
void copy_point_table__9TWindowDDFl(void *, s32);
f32 TWindowDD__sub_80348AD4(f32, f32);
void TWindowDD__sub_80348A2C(void *, void *);
f32 fn_803D6308(f32, f32, f32);
extern u32 lbl_805D63F0;
extern const f32 lbl_805DFCA4;
extern const f32 lbl_805DFCAC;
extern const f32 TWindowDD__data_805DFB18;
extern const f32 TWindowDD__data_805DFB20;
extern const float TWindowDD__data_805DFCA8;
extern const f32 lbl_805DFB40;
extern const f32 lbl_805DFB44;
extern const double TWindowDD__data_80478610;
}

void TWindowDD__sub_80341674(TWindowDD_WS_Word *selfv, u8 *entry) {
    u8 *self = (u8 *)selfv;
    E_80341674 q[4];
    f32 *pd;
    s32 p0;
    s32 p1;
    s32 p2;
    s32 count;
    f32 depth;
    f32 width;
    f32 neg;
    f32 f2v;
    f32 lo;
    f32 hi;
    f32 cornerA;
    f32 cornerB;
    f32 c;
    f32 norm;
    f32 t;
    f32 d24;
    f32 z;
    s32 n;
    s32 i;
    s32 k4;
    s32 k;
    p0 = *(s32 *)lbl_805D63F0;
    p1 = *(s32 *)(p0 + 0x20);
    p2 = *(s32 *)(p1 + 0xC);
    count = *(s32 *)p2;
    if (*(s32 *)(entry + 0x30) < 0) {
        return;
    }
    depth = lbl_805DFCA4 * *(f32 *)(self + 0x4c) + *(f32 *)(self + 0x44);
    TWindowDD__sub_80348AD4(*(f32 *)(self + 0x54), TWindowDD__data_805DFCA8);
    reset_entries__9TWindowDDFf(q, -1);
    copy_point_table__9TWindowDDFl(q, *(s32 *)(self + 0x64));
    TWindowDD__sub_80348A2C(entry, q);
    neg = -(lbl_805DFCA4 * *(f32 *)(self + 0x4c));
    f2v = neg + TWindowDD__data_805DFB20;
    width = *(f32 *)(entry + 0x2c);
    n = *(s32 *)(self + 0x78);
    cornerA = neg * width + depth;
    cornerB = f2v * width + depth;
    if (*(s32 *)(self + 0x64) == 0) {
        c = lbl_805DFB40;
    } else {
        c = lbl_805DFB44;
    }
    lo = c * TWindowDD__data_805DFB18;
    hi = (c + TWindowDD__data_805DFB20) * TWindowDD__data_805DFB18;
    t = fn_803D6308(-(*(f32 *)(self + 0x88)) / TWindowDD__data_805DFB20, TWindowDD__data_805DFB18, lbl_805DFCA4);
    norm = TWindowDD__data_805DFB20 * t;
    if (TWindowDD__data_805DFCA8 != norm) {
        n = *(s32 *)(self + 0x78) - 1;
        if (norm < TWindowDD__data_805DFCA8) {
            t = norm + TWindowDD__data_805DFB20;
        } else {
            t = norm;
            norm = norm - TWindowDD__data_805DFB20;
        }
        d24 = t * width + cornerA;
        z = hi - t * TWindowDD__data_805DFB18;
        for (k = 0; k < 4; k++) {
            pd = q[k].v;
            pd[1] = cornerA;
            pd[4] = z;
            pd[7] = d24;
            pd[10] = hi;
        }
        ((TWindowDD *)q)->draw_transformed_primitive((void *)8, (void *)count, (void *)1);
        cornerA = d24;
    }
    if (n > 0) {
        d24 = TWindowDD__data_805DFB20 * width;
        for (k = 0; k < 4; k++) {
            pd = q[k].v;
            pd[4] = lo;
            pd[10] = hi;
        }
        i = 0;
        k4 = 4;
        while (i < n) {
            cornerB = cornerA + d24;
            for (k = 0; k < k4; k++) {
                pd = q[k].v;
                pd[1] = cornerA;
                pd[7] = cornerB;
            }
            ((TWindowDD *)q)->draw_transformed_primitive((void *)8, (void *)count, (void *)1);
            cornerA = cornerB;
            i = i + 1;
        }
    }
    if (TWindowDD__data_805DFCA8 != norm) {
        t = lbl_805DFCA4 * *(f32 *)(self + 0x4c);
        z = lo - norm * TWindowDD__data_805DFB18;
        t = t * width + depth;
        for (k = 0; k < 4; k++) {
            pd = q[k].v;
            pd[1] = cornerB;
            pd[4] = lo;
            pd[7] = t;
            pd[10] = z;
        }
        ((TWindowDD *)q)->draw_transformed_primitive((void *)8, (void *)count, (void *)1);
    }
    if (selfv->m_74 > 0) {
        if (selfv->sub_80342254() != 0) {
            TWindowDD__sub_80348AD4(*(f32 *)(self + 0x54), lbl_805DFCAC);
            reset_entries__9TWindowDDFf(q, -1);
            copy_point_table__9TWindowDDFl(q, 1);
            TWindowDD__sub_80348A2C(entry, q);
            t = (f32) selfv->m_6c;
            neg = -(lbl_805DFCA4 * *(f32 *)(self + 0x4c));
            z = t * TWindowDD__data_805DFB20 + neg;
            t = z + TWindowDD__data_805DFB20;
            z = z * width + depth;
            t = t * width + depth;
            pd = (f32 *)q;
            for (k = 0; k < 4; k++) {
                pd[1] = z;
                pd += 6;
                pd[1] = t;
                pd += 6;
            }
            ((TWindowDD *)q)->draw_transformed_primitive((void *)8, (void *)count, (void *)1);
        }
    }
}

#define sub_80341AC0__17TWindowDD_WS_WordFv ((s32 (*)(void))sub_80341AC0__17TWindowDD_WS_WordFv)

s32 TWindowDD_WS_Word::can_scroll(s32 arg1) {
    s32 temp_r0;
    s32 temp_r3;
    s32 temp_r4;
    s32 temp_r5;

    if (sub_80341AC0__17TWindowDD_WS_WordFv() == 0) {
        return 0;
    }
    temp_r4 = *(s32 *)((s8 *)this + 0x78);
    temp_r5 = temp_r4 / 2;
    if (arg1 > 0) {
        temp_r0 = *(s32 *)((s8 *)this + 0x6C);
        if (temp_r0 < temp_r5) {
            return 0;
        }
        return (this->m_68 + (temp_r4 - temp_r0)) < this->m_74;
    }
    temp_r3 = *(s32 *)((s8 *)this + 0x6C);
    if (temp_r3 >= temp_r5) {
        return 0;
    }
    return ((u32) (this->m_68 - (temp_r3 + 1)) >> 0x1FU) ^ 1;
}

#undef sub_80341AC0__17TWindowDD_WS_WordFv

s32 TWindowDD_WS_Word::sub_80341AC0() {
    return this->m_74 > *(s32 *)((s8 *)((u8 *)this) + 0x78);
}

void TWindowDD__sub_80341AE0(u8 *arg0) {
    *(s32 *)((s8 *)arg0 + 0x60) = (s32) (*(s32 *)((s8 *)arg0 + 0x60) | 1);
    *(s32 *)((s8 *)arg0 + 0x8C) = 1;
}

void TWindowDD__sub_80341AF8(u8 *arg0) {
    *(s32 *)((s8 *)arg0 + 0x60) = (s32) (*(s32 *)((s8 *)arg0 + 0x60) & 0xFFFFFFFE);
    *(s32 *)((s8 *)arg0 + 0x8C) = 1;
}

#include "pso/misc/TWindowDD.h"
#include "pso/misc/TWindowSubComCard.h"
#include "pso/misc/TWindowSubStatusDisp.h"

#define sub_80341AC0__17TWindowDD_WS_WordFv ((s32 (*)(void *))sub_80341AC0__17TWindowDD_WS_WordFv)

struct RecoveredGlobal_80341F9C_TWindowDD__data_804EFC50 {
    s32 value;
    u8 remaining[0x3C];
};

struct Elem_80341FFC {
    s16 *data;
    s32 count;
};

struct Win_80341FFC {
    u8 pad[0x70];
    s32 x70;
    s32 count;
    s32 max;
    s32 shown;
    s16 *buf;
};

struct Entry_80341FFC {
    u8 pad[0xC];
    f32 y;
};

extern "C" {
s32 apply_both_choices__9TWindowDDFll(void *, int);
s32 sub_80342268__17TWindowDD_WS_WordFv();
extern const f32 TWindowDD__data_805DFB20;
extern const float TWindowDD__data_805DFCA8;
s32 init_window_layout_entries(void *, void *, int);
extern RecoveredGlobal_80341F9C_TWindowDD__data_804EFC50 TWindowDD__data_804EFC50;
void *mem_alloc(u32 size);
s32 get_array_entry__11TWindowBaseFi(void * a0, s32 a1);
Elem_80341FFC *get_element_ptr__9TWindowDDFl(s32);
void mem_free(void *);
s32 get_array_entry__11TWindowBaseFi(void * a0 = 0, s32 a1 = 0);
s32 get_field_20__17TWindowSubComCardFv(void);

void TWindowDD::set_mode_2() { this->m_80 = 2; }
void TWindowDD::reset_cursor() { this->m_80 = 0; }

#pragma push
#pragma fp_contract on
void TWindowDD::handle_scroll_input() {
    u8 *arg0 = (u8 *)this;
    s32 temp_r3_3;
    s32 temp_r3_4;
    s32 temp_r4;
    s32 temp_r4_2;
    s32 temp_r4_3;
    s32 temp_r5;
    s32 var_r30;
    s32 var_r30_2;
    if (sub_80342268__17TWindowDD_WS_WordFv() != 0) {
        if (apply_both_choices__9TWindowDDFll((u8 *)&this->m_7c, 0x20) != 0) {
            temp_r4 = *(s32 *)&this->m_84;
            if (temp_r4 < (s32) (*(s32 *)&this->m_90 - 1)) {
                switch (((TWindowDD_WS_Word *)arg0)->can_scroll(1)) {
                case 0:
                    *(s32 *)&this->m_88 = (s32) (*(s32 *)&this->m_88 + 1);
                    break;
                case 1:
                    *(f32 *)((s8 *)arg0 + 0x88) = (f32) (*(f32 *)((s8 *)arg0 + 0x88) + TWindowDD__data_805DFB20);
                    break;
                }
                add_scroll_offset(1);
            } else {
                add_scroll_offset((int)(-temp_r4));
                *(s32 *)&this->m_88 = 0;
                *(f32 *)((s8 *)arg0 + 0x88) = (f32) (*(const f32 *)&TWindowDD__data_805DFCA8);
            }
        } else if (apply_both_choices__9TWindowDDFll((u8 *)&this->m_7c, 0x10) != 0) {
            if ((s32) *(s32 *)&this->m_84 > 0) {
                switch (((TWindowDD_WS_Word *)arg0)->can_scroll(-1)) {
                case 0:
                    *(s32 *)&this->m_88 = (s32) (*(s32 *)&this->m_88 - 1);
                    break;
                case 1:
                    *(f32 *)((s8 *)arg0 + 0x88) = (f32) (*(f32 *)((s8 *)arg0 + 0x88) - TWindowDD__data_805DFB20);
                    break;
                }
                add_scroll_offset(-1);
            } else {
                *(s32 *)&this->m_88 = (s32) (*(s32 *)&this->m_98 - 1);
                add_scroll_offset((int)((*(s32 *)&this->m_90 - *(s32 *)&this->m_84) - 1));
                *(f32 *)((s8 *)arg0 + 0x88) = (f32) (TWindowDD__data_805DFB20 * (f32) -(*(s32 *)&this->m_84 - *(s32 *)&this->m_88));
            }
        } else if ((apply_both_choices__9TWindowDDFll((u8 *)&this->m_7c, 0x10000) != 0) && ((s32) *(s32 *)&this->m_84 < (s32) (*(s32 *)&this->m_90 - 1))) {
            if (sub_80341AC0__17TWindowDD_WS_WordFv(arg0) != 0) {
                temp_r4_2 = *(s32 *)&this->m_94;
                temp_r4_3 = temp_r4_2 - 1;
                temp_r5 = *(s32 *)&this->m_84 + (temp_r4_2 - (*(s32 *)&this->m_88 + 1));
                temp_r3_3 = *(s32 *)&this->m_90;
                var_r30 = temp_r4_3;
                if ((s32) (temp_r5 + temp_r4_3) >= temp_r3_3) {
                    var_r30 = (temp_r3_3 - temp_r5) - 1;
                }
                if (var_r30 <= 0) {
                    *(s32 *)&this->m_88 = temp_r4_3;
                    add_scroll_offset((int)((*(s32 *)&this->m_90 - 1) - *(s32 *)&this->m_84));
                } else {
                    add_scroll_offset(var_r30);
                    *(f32 *)((s8 *)arg0 + 0x88) = (f32) (((f32) var_r30 * TWindowDD__data_805DFB20) + *(f32 *)((s8 *)arg0 + 0x88));
                }
            } else {
                *(s32 *)&this->m_88 = (s32) (*(s32 *)&this->m_90 - 1);
                add_scroll_offset((int)((*(s32 *)&this->m_90 - 1) - *(s32 *)&this->m_84));
            }
        } else if ((apply_both_choices__9TWindowDDFll((u8 *)&this->m_7c, 0x20000) != 0) && ((s32) *(s32 *)&this->m_84 > 0)) {
            if (sub_80341AC0__17TWindowDD_WS_WordFv(arg0) != 0) {
                var_r30_2 = *(s32 *)&this->m_94 - 1;
                temp_r3_4 = *(s32 *)&this->m_84 - *(s32 *)&this->m_88;
                if ((temp_r3_4 - var_r30_2) < 0) {
                    var_r30_2 = temp_r3_4;
                }
                if (var_r30_2 <= 0) {
                    *(s32 *)&this->m_88 = 0;
                    add_scroll_offset((int)(-*(s32 *)&this->m_84));
                } else {
                    add_scroll_offset((int)(-var_r30_2));
                    *(f32 *)((s8 *)arg0 + 0x88) = (f32) -(((f32) var_r30_2 * TWindowDD__data_805DFB20) - *(f32 *)((s8 *)arg0 + 0x88));
                }
            } else {
                *(s32 *)&this->m_88 = 0;
                add_scroll_offset((int)(-*(s32 *)&this->m_84));
            }
        }
    }
    ((TWindowDD *)arg0)->initialize_subwindow();
    ((TWindowBase *)arg0)->update_fade();
    ((TWindowBase *)arg0)->update_window_entry_list(arg0 + 0x24);
}
#pragma pop

void TWindowDD::init_and_mark_field8C() { init_layout_entries(); load_element_list(); this->m_a8 = 1; }

void TWindowDD::free_child() {
    if (*(void **)((s8 *)this + 0x80) != NULL) {
        mem_free(*(void **)((s8 *)this + 0x80));
        this->m_9c = 0;
    }
    ((TWindowSubStatusDisp *)((char *)this + 36))->destroy_all_items();
    this->m_90 = 0;
    this->m_98 = 0;
}

void TWindowDD::init_child(void* a1) { free_child(); *(void**)((char*)this + 0x70) = a1; init_layout_entries(); load_element_list(); reset_fields(); this->m_a8 = 1; }

typedef char RecoveredGlobal_80341F9C_TWindowDD__data_804EFC50_size[sizeof(RecoveredGlobal_80341F9C_TWindowDD__data_804EFC50) == 0x40 ? 1 : -1];
void TWindowDD::init_layout_entries() {
    u8 *arg0 = (u8 *)this;
    *(s32 *)((s8 *)&TWindowDD__data_804EFC50.value + 4) = (s32) this->m_94;
    init_window_layout_entries(arg0 + 0x24, (void *)&TWindowDD__data_804EFC50.value, (int) (*(s16 *)((s8 *)arg0 + 0x20)));
}

void TWindowDD::reset_fields() { *(float*)((char*)this + 0x88) = TWindowDD__data_805DFCA8; *(float*)((char*)this + 0x84) = TWindowDD__data_805DFCA8; this->m_84 = 0; this->m_88 = 0; this->m_a8 = 1; }

extern s32 TWindowDD__data_805DFB50;

void TWindowDD::load_element_list() {
    Win_80341FFC *self = (Win_80341FFC *)this;
    Elem_80341FFC *e;
    s32 i;
    s32 n;
    Entry_80341FFC *ent;
    e = get_element_ptr__9TWindowDDFl(self->x70);
    if (e != NULL) {
        self->count = e->count;
        self->buf = (s16 *)mem_alloc(self->count * 2);
        for (i = 0; i < self->count; i++) {
            self->buf[i] = e->data[i];
        }
    } else {
        self->count = 0;
        self->buf = NULL;
    }
    n = self->count;
    if (self->max < n) {
        n = self->max;
    }
    self->shown = n;
    for (i = 0; i < self->shown; i++) {
        ent = (Entry_80341FFC *)get_array_entry__11TWindowBaseFi(self, i);
        set_text_entry_string((u8 *)ent, TWindowDD__sub_80348B70((s16)self->buf[i]), 0xC0);
        ent->y = i * 20;
        refresh_status_display__9TWindowDDFv(ent);
    }
}

void TWindowDD::set_pos_and_data(f32 farg0) {
    u8 *arg0 = (u8 *)this;
    *(f32 *)((s8 *)arg0 + 0x30) = farg0;
    *(s32 *)((s8 *)arg0 + 0x50) = (s32) TWindowDD__data_805DFB50;
}

s32 TWindowDD::get_field_0x74() { return this->m_90; }

s16 TWindowDD__sub_8034214C(u8 *arg0) {
    return (s16) *(s32 *)((s8 *)arg0 + 0x70);
}

int TWindowDD__sub_80342158(u8 *arg0) {
    u32 temp_r4;
    temp_r4 = *(u32 *)((s8 *)arg0 + 0x80);
    if (temp_r4 != 0U) {
        return *(s16 *)((s8 *)(temp_r4 + (*(s32 *)((s8 *)arg0 + 0x68) * 2)) + 0);
    }
    return 0x685;
}

s32 TWindowDD__sub_8034217C(u8 *arg0) {
    return *(s32 *)((s8 *)arg0 + 0x68) - *(s32 *)((s8 *)arg0 + 0x6C);
}

s32 TWindowDD::get_cursor_index() { return this->m_88; }
s32 TWindowDD::update_if_field28_set() {
    if ((u32) this->m_44 != 0U) {
        get_array_entry__11TWindowBaseFi(this, this->m_88);
        return get_field_20__17TWindowSubComCardFv();
    }
    return 0;
}

#pragma push
#pragma fp_contract on
void TWindowDD::get_cursor_pos(u8 *arg1) {
    u8 *arg0 = (u8 *)this;
    *(f32 *)((s8 *)arg1 + 0) = (f32) *(f32 *)((s8 *)arg0 + 0x40);
    *(f32 *)((s8 *)arg1 + 4) = (f32) (((f32) *(s32 *)((s8 *)arg0 + 0x6C) * TWindowDD__data_805DFB20) + *(f32 *)((s8 *)arg0 + 0x44));
}
#pragma pop

s32 TWindowDD::get_field_68() { return this->m_84; }
void TWindowDD::add_scroll_offset(int a1) { this->m_84 = (this->m_84 + a1); this->m_a8 = 1; TWindowDD::spawn_window(); }

}

#undef sub_80341AC0__17TWindowDD_WS_WordFv
