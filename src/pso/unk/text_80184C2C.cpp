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
extern "C" {
void debug_printf_at(s32 id, const char *fmt, ...);
extern const char lbl_804449C0[];
extern const char lbl_804449D0[];
extern const char lbl_804449E0[];
extern const char lbl_804449F0[];
extern const char lbl_80444A00[];
extern const char lbl_80444A10[];
extern const char *labo_map_warp_dest_name_table_b[];
void TLobby__sub_8001FE7C(void *, s32);
s32 get_main_phase(void);
void *load_resource_from_descriptor(void *, s32, void *, s32, s32, s32);
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
extern u8 lbl_804B5E80[];
void *operator new(size_t size);

struct ModelEnt_80184DF4 { s32 f0; s32 f4; s32 f8; s32 fc; };
struct ResBlock_80184DF4 { u8 pad0[0x42C]; ModelEnt_80184DF4 *models; s32 pad430; s32 model_count; };

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

extern "C" void TLobby__sub_80184DF4(void) {
    ResBlock_80184DF4 *res;
    ModelEnt_80184DF4 *me;
    TLobby *tbl;
    s16 *flags;
    s32 i;
    s32 m1;
    void *n;
    u8 *base;

    base = lbl_804B5E80;
    TLobby::clear_global_array(base);
    if (get_main_phase() == 0xf) {
        TLobby__sub_80184C80(base);
    } else {
        TLobby__sub_80184CE0(base);
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
        res = (ResBlock_80184DF4 *)::operator new(0x440);
        if (res != NULL) {
            res = (ResBlock_80184DF4 *)load_resource_from_descriptor(res, 1,
                    (void *)*(s32 *)(base + 0x15c + lbl_805D5B30 * 4), 0, 0, 0);
        }
        city_season_easter_egg_model_table[lbl_805D5B30] = (s32)res;
        for (i = 0; i < res->model_count; i++) {
            if (*(s32 *)((s8 *)res->models + i * 16 + 12) == 0) {
                continue;
            }
            me = (ModelEnt_80184DF4 *)((s8 *)res->models + i * 16);
            city_season_xmas_model_table[lbl_805D5B30] = me->fc;
            break;
        }
        if (lbl_805D5B30 == 0) {
            m1 = res->models[1].f8;
            tbl = (TLobby *)::operator new(0x14);
            n = tbl;
            if (tbl != NULL) {
                n = tbl->alloc_tables(m1, 3);
            }
            lbl_805D5B34 = n;
            flags = (s16 *)(*(s32 *)(*(s32 *)(*(s32 *)(m1 + 0x2c) + 4) + 4) + 0xc);
            *flags &= (s16)~0x1000;
        } else if (lbl_805D5B30 == 4) {
            m1 = res->models[1].f8;
            tbl = (TLobby *)::operator new(0x14);
            n = tbl;
            if (tbl != NULL) {
                n = tbl->alloc_tables(m1, 0);
            }
            lbl_805D5B34 = n;
            flags = (s16 *)(*(s32 *)(*(s32 *)(*(s32 *)(m1 + 0x2c) + 4) + 4) + 0xc);
            *flags &= (s16)~0x1000;
        } else {
            lbl_805D5B34 = 0;
        }
    }
    if (lbl_805D5B30 == 2) {
        res = (ResBlock_80184DF4 *)::operator new(0x440);
        if (res != NULL) {
            res = (ResBlock_80184DF4 *)load_resource_from_descriptor(res, 1,
                    (void *)(base + 0x130), 0, 0, 0);
        }
        lbl_805D5B3C = res->models[0].f8;
        lbl_805D5B40 = res->models[1].f8;
    } else if (lbl_805D5B30 == 4) {
        res = (ResBlock_80184DF4 *)::operator new(0x440);
        if (res != NULL) {
            res = (ResBlock_80184DF4 *)load_resource_from_descriptor(res, 1,
                    (void *)(base + 0x14c), 0, 0, 0);
        }
        lbl_805D5B3C = res->models[0].f8;
        lbl_805D5B40 = res->models[1].f8;
    } else {
        res = (ResBlock_80184DF4 *)::operator new(0x440);
        if (res != NULL) {
            res = (ResBlock_80184DF4 *)load_resource_from_descriptor(res, 1,
                    (void *)(base + 0x114), 0, 0, 0);
        }
        lbl_805D5B3C = res->models[0].f8;
        lbl_805D5B40 = res->models[1].f8;
    }
    tbl = (TLobby *)::operator new(0x14);
    n = tbl;
    if (tbl != NULL) {
        n = tbl->alloc_tables(lbl_805D5B3C, 2);
    }
    lbl_805D5B48 = n;
    i = 0;
    flags = (s16 *)(*(s32 *)(*(s32 *)(lbl_805D5B3C + 4) + 4) + 0xc);
    *flags &= (s16)~0x2000;
    lbl_805D5B38 = res;
    for (; i < res->model_count; i++) {
        if (*(s32 *)((s8 *)res->models + i * 16 + 12) == 0) {
            continue;
        }
        me = (ModelEnt_80184DF4 *)((s8 *)res->models + i * 16);
        lbl_805D5B44 = me->fc;
        break;
    }
}

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
