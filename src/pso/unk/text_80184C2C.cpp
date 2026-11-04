#include "types.h"
#include "pso/unk/text_800F5BC0.h"
#include "pso/unk/text_80184C2C.h"
#include "pso/misc/TLobby.h"
#include "pso/npc/TObjNpcEnemy.h"
#include "pso/object/TObjLaboMapWarp.h"

struct Obj_80185160 { u8 pad[0x8C]; s32 dest; };

extern int lbl_8050DC20[];
extern s32 lobby_event_theme_id_table[];
extern s32 TLobby__event_theme_id;
extern u8 lbl_804B5E80[];
extern "C" {
void debug_printf_at(s32 id, const char *fmt, ...);
s32 get_main_phase(void);
u8* load_resource_from_descriptor(void *, s32, void *, s32, s32, s32);
u8* __nw__FUl(u32);
extern const char lbl_804449C0[];
extern const char lbl_804449D0[];
extern const char lbl_804449E0[];
extern const char lbl_804449F0[];
extern const char lbl_80444A00[];
extern const char lbl_80444A10[];
extern const char *labo_map_warp_dest_name_table_b[];
void TLobby__sub_8001FE7C(void *, s32);
extern int city_season_easter_egg_model_table[];
extern int city_season_xmas_model_table[];
extern void *lbl_805D5B34;
extern void *lbl_805D5B38;
extern s32 lbl_805D5B3C;
extern s32 lbl_805D5B40;
extern s32 lbl_805D5B44;
extern void *lbl_805D5B48;

int TLobby__sub_80184C2C(int a0) {  return city_season_xmas_model_table[a0]; }
}

int get_season_model_resource(int a0) {  return city_season_easter_egg_model_table[a0]; }

extern s32 lbl_805D5B30;

u8 TLobby__sub_80184C54(void) {
    return (u8) (lbl_805D5B30 != -1);
}

int TLobby__sub_80184C6C(int a0) {  return lbl_8050DC20[a0]; }

void TLobby__sub_80184C80(void *p) {
    s32 i;
    TLobby::clear_global_array(p);
    for (i = 0; i < 6; i++) {
        if (TLobby__event_theme_id == lobby_event_theme_id_table[i]) {
            lbl_8050DC20[i] = 1;
            return;
        }
    }
}

void TLobby__sub_80184CE0(void* p) { TLobby::clear_global_array(p); }
void TLobby::clear_global_array(void* _w0) {
    s32 i;
    for (i = 0; i < 6; i++) {
        ((s32 *)&lbl_8050DC20)[i] = 0;
    }
}

void TLobby::free_buffers() {
    s32 i;
    if (lbl_805D5B48 != NULL) {
        destroy_buffer_pair(lbl_805D5B48, 1);
        lbl_805D5B48 = NULL;
    }
    if (lbl_805D5B38 != NULL) {
        TLobby__sub_8001FE7C(lbl_805D5B38, 1);
        lbl_805D5B38 = NULL;
    }
    lbl_805D5B44 = 0;
    lbl_805D5B3C = 0;
    lbl_805D5B40 = 0;
    if (lbl_805D5B34 != NULL) {
        destroy_buffer_pair(lbl_805D5B34, 1);
        lbl_805D5B34 = NULL;
    }
    for (i = 5; i >= 0; i--) {
        if ((u32)city_season_easter_egg_model_table[i] != 0) {
            TLobby__sub_8001FE7C((void *)city_season_easter_egg_model_table[i], 1);
        }
        city_season_easter_egg_model_table[i] = 0;
        city_season_xmas_model_table[i] = 0;
    }
}

#pragma push
#pragma opt_common_subs off
void TLobby__sub_80184DF4(void) {
    u8* base;
    s32 phase;
    s32 i;
    s32 res;
    s32 off;
    s32 cnt;
    s32 e2;
    s32 t;
    s32 res2;
    s32 ix;
    s32 w;
    s32* p;
    s32* p1;

    base = lbl_804B5E80;
    TLobby::clear_global_array(base);
    phase = get_main_phase();
    if (phase == 15) {
        TLobby__sub_80184C80((void*)phase);
    } else {
        TLobby__sub_80184CE0((void*)phase);
    }
    lbl_805D5B30 = -1;
    for (i = 0; i < 6; i++) {
        if (TLobby__sub_80184C6C(i) != 0) {
            lbl_805D5B30 = i;
            break;
        }
    }
    if (lbl_805D5B30 != -1) {
        for (i = 0; i < 6; i++) {
            city_season_easter_egg_model_table[i] = 0;
            city_season_xmas_model_table[i] = 0;
        }
        res = (s32)__nw__FUl(0x440);
        if (res != 0) {
            res = (s32)load_resource_from_descriptor((void*)res, 1,
                    *(void**)(base + 0x15c + lbl_805D5B30 * 4), 0, 0, 0);
        }
        ix = lbl_805D5B30;
        city_season_easter_egg_model_table[ix] = res;
        off = 0;
        cnt = *(s32*)(res + 0x434);
        for (i = 0; i < cnt; i++) {
            e2 = *(s32*)(res + 0x42c);
            if (*(s32*)(e2 + off + 0xc) != 0) {
                e2 = e2 + off;
                city_season_xmas_model_table[ix] = *(s32*)(e2 + 0xc);
                break;
            }
            off += 0x10;
        }
        if (lbl_805D5B30 == 0) {
            e2 = *(s32*)(*(s32*)(res + 0x42c) + 0x18);
            t = (s32)__nw__FUl(0x14);
            if (t != 0) {
                t = (s32)((TLobby*)t)->alloc_tables(e2, 3);
            }
            lbl_805D5B34 = (void*)t;
            p = (s32*)(e2 + 0x2c);
            p = (s32*)*p;
            p = (s32*)p[1];
            p = (s32*)p[1];
            w = *(s16*)(p + 3);
            w = w & 0xFFF7FFFF;
            *(s16*)(p + 3) = w;
        } else if (lbl_805D5B30 == 4) {
            e2 = *(s32*)(*(s32*)(res + 0x42c) + 0x18);
            t = (s32)__nw__FUl(0x14);
            if (t != 0) {
                t = (s32)((TLobby*)t)->alloc_tables(e2, 0);
            }
            lbl_805D5B34 = (void*)t;
            p = (s32*)(e2 + 0x2c);
            p = (s32*)*p;
            p = (s32*)p[1];
            p = (s32*)p[1];
            w = *(s16*)(p + 3);
            w = w & 0xFFF7FFFF;
            *(s16*)(p + 3) = w;
        } else {
            lbl_805D5B34 = 0;
        }
    }
    if (lbl_805D5B30 == 2) {
        res2 = (s32)__nw__FUl(0x440);
        if (res2 != 0) {
            res2 = (s32)load_resource_from_descriptor((void*)res2, 1, base + 0x130, 0, 0, 0);
        }
        p1 = (s32*)*(s32*)(res2 + 0x42c);
        base = (u8*)res2;
        lbl_805D5B3C = p1[2];
        lbl_805D5B40 = *(s32*)(*(s32*)(res2 + 0x42c) + 0x18);
    } else if (lbl_805D5B30 == 4) {
        res2 = (s32)__nw__FUl(0x440);
        if (res2 != 0) {
            res2 = (s32)load_resource_from_descriptor((void*)res2, 1, base + 0x14c, 0, 0, 0);
        }
        p1 = (s32*)*(s32*)(res2 + 0x42c);
        base = (u8*)res2;
        lbl_805D5B3C = p1[2];
        lbl_805D5B40 = *(s32*)(*(s32*)(res2 + 0x42c) + 0x18);
    } else {
        res2 = (s32)__nw__FUl(0x440);
        if (res2 != 0) {
            res2 = (s32)load_resource_from_descriptor((void*)res2, 1, base + 0x114, 0, 0, 0);
        }
        p1 = (s32*)*(s32*)(res2 + 0x42c);
        base = (u8*)res2;
        lbl_805D5B3C = p1[2];
        lbl_805D5B40 = *(s32*)(*(s32*)(res2 + 0x42c) + 0x18);
    }
    t = (s32)__nw__FUl(0x14);
    if (t != 0) {
        t = (s32)((TLobby*)t)->alloc_tables(lbl_805D5B3C, 2);
    }
    lbl_805D5B48 = (void*)t;
    off = 0;
    p = (s32*)lbl_805D5B3C;
    p = (s32*)p[1];
    p = (s32*)p[1];
    w = *(s16*)(p + 3);
    w = w & 0xFFFBFFFF;
    *(s16*)(p + 3) = w;
    lbl_805D5B38 = base;
    cnt = *(s32*)(base + 0x434);
    for (i = 0; i < cnt; i++) {
        e2 = *(s32*)(base + 0x42c);
        if (*(s32*)(e2 + off + 0xc) != 0) {
            e2 = e2 + off;
            lbl_805D5B44 = *(s32*)(e2 + 0xc);
            break;
        }
        off += 0x10;
    }
}
#pragma pop

void TObjLaboMapWarp::slot4C() {
    Obj_80185160 *self = (Obj_80185160 *)this;
    ((TObjLaboMapWarp *)self)->clamp_index();
    TObjNpcEnemy::set_global_count(0xFF00FF);
    debug_printf_at(0x13001C, lbl_804449C0);
    debug_printf_at(0x13001D, lbl_804449D0);
    debug_printf_at(0x13001E, lbl_804449E0);
    debug_printf_at(0x130020, lbl_804449F0);
    debug_printf_at(0x130021, lbl_80444A00);
    debug_printf_at(0x130022, lbl_80444A10, labo_map_warp_dest_name_table_b[this->set_params[2]]);
    TObjNpcEnemy::set_global_count(0xF0F0F0FF);
}
