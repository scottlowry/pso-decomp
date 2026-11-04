#include "types.h"
#include "pso/player/TObjChara.h"
#include "pso/misc/TLobby.h"
#include "pso/item/TItemData.h"
#include "pso/player/TObjPlayer.h"
#include "pso/map/FloorArea.h"
#include "pso/unk/text_8011A780.h"

struct Blk_8010542C { u32 w[4]; };
struct Item_8010542C { u32 a; Blk_8010542C b; };
struct Entry_8010567C { u16 a; u16 b; };

struct Pkt_8010567C {
    u8 hdr[4];
    u8 f4;
    u8 f5;
    s16 f6;
    f32 x;
    f32 z;
    s16 f10;
    s16 f12;
    u8 f14;
    f32 f18;
    s32 f1c;
    s32 f20;
    s32 f24;
};

struct Obj_8010567C {
    u8 pad[0x28];
    s16 f28;
    u8 pad2a[2];
    s16 f2c;
    u8 pad2e[0x38 - 0x2E];
    f32 x;
    f32 y;
    f32 z;
    u8 pad44[0x70 - 0x44];
    f32 f70;
    u8 pad74[0x84 - 0x74];
    s32 f84;
    s32 f88;
    s32 f8c;
};


struct Rec_80105538 { s32 a; u16 b; u16 b2; s32 c; };

struct Pkt_80105538 {
    u8 hdr[4];
    s8 f4;
    s8 f5;
    s16 f6;
    f32 x;
    f32 z;
    s16 f10;
    u8 f12[2];
    s8 f14;
};

struct Vec_80105538 { f32 x, y, z; };

struct Obj_80105538 {
    u8 pad[0x28];
    s16 f28;
    u8 pad2a[2];
    s16 f2c;
    u8 pad2e[0x38 - 0x2E];
    f32 x;
    f32 y;
    f32 z;
    u8 pad44[0x370 - 0x44];
    s32 f370;
};

extern "C" {
typedef s32 (*Fn_8010542C)(void *);
extern Fn_8010542C item_create_fn_table[];
struct In_801054E0 { u8 pad0; u8 idx; };
typedef s32 (*Fn_801054E0)(In_801054E0 *);
struct E_801054E0 { Fn_801054E0 fn; };
extern E_801054E0 item_pro_create_fn_table[];
s32 TLobby__sub_801054E0(In_801054E0 *arg0);
void *get_player_by_client_id(s32);
s32 get_current_floor(void);
s32 TObjPlayer__sub_80104840(s32);
extern s32 TLobby__designated_client_id;
extern Entry_8010567C *quest_object_entries;
extern s32 local_client_id;
int check_class_equip_permission(TObjPlayer *player, s32 perm);
s32 *csnVecterUnder(s32 origin, s32 mask);
s32 is_valid_drop_floor();
}
void *build_6x06_send_guild_card(void *arg0);
extern Rec_80105538 *TLobby__data_805D6144;
extern const f32 lbl_805DAAB4;
extern "C" {
void send_6x60_standard_drop_item_request(Obj_80105538 *self);
int roll_weapon_special_channel15(void* p);
int roll_weapon_special_for_stars(void*);

struct VBase_18_80105218 { char pad[0x18]; };

struct VObj_18_80105218 : VBase_18_80105218 {
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

struct ReqStats_80104FCC {
    s16 atp;
    s16 pad2;
    s16 mst;
    s16 ata;
    u8 pad8[0x10];
};

extern "C" {
s32 obj_isState3_324__9TObjCharaFv(void *);
s32 is_script_controlled__10TObjPlayerFv(void *);
int is_quest_active(void);
s32 query_flag__13TItemMenuCtrlFl(s32);
void *lookup_item_pmt_record(u8 *);
u8 get_technique_learn_limit(u8, u8);
int clear_fields__20TWindowSubStatusDispFv(void *);
s32 build_player_equipment_requirement_stats(s32, ReqStats_80104FCC *);
}

#pragma push
#pragma opt_propagation off
s32 check_equip_requirements(void *player, void *item, s32 *requirement) {
    TObjPlayer *p = (TObjPlayer *)player;
    u8 *rec;
    u8 *rec2;
    s32 acc;
    u32 code;
    s32 t;
    u32 lim;
    s32 k;
    ReqStats_80104FCC st;

    if (p == 0 || item == 0) {
        if (requirement != 0) {
            *requirement |= 0x20;
        }
        return 0;
    }
    if (obj_isState3_324__9TObjCharaFv(p) != 0 ||
        is_script_controlled__10TObjPlayerFv(p) != 0) {
        if (requirement != 0) {
            *requirement = 0;
        }
        return 1;
    }
    if (is_quest_active() != 0) {
        t = *(u8 *)item;
        code = 0;
        switch (t) {
        case 0:
            code = 1;
            break;
        case 1:
            t = *(u8 *)((s8 *)item + 1);
            switch (t) {
            case 1:
                code = 2;
                break;
            case 2:
                code = 3;
                break;
            case 3:
                code = 4;
                break;
            default:
                break;
            }
            break;
        case 2:
            code = 5;
            break;
        default:
            break;
        }
        if (code != 0 && query_flag__13TItemMenuCtrlFl(code) == 1) {
            return 0;
        }
    }
    t = *(u8 *)item;
    acc = 0;
    switch (t) {
    case 0:
        rec = (u8 *)lookup_item_pmt_record((u8 *)item);
        if (rec != 0) {
            if (check_class_equip_permission(p, (s16)*(u16 *)((s8 *)rec + 8)) == 0) {
                acc |= 1;
            }
            clear_fields__20TWindowSubStatusDispFv(&st);
            build_player_equipment_requirement_stats((s32)p, &st);
            if (st.atp < (s32)*(u16 *)((s8 *)rec + 0xE)) {
                acc |= 2;
            }
            if (st.ata < (s32)*(u16 *)((s8 *)rec + 0x12)) {
                acc |= 4;
            }
            if (st.mst < (s32)*(u16 *)((s8 *)rec + 0x10)) {
                acc |= 8;
            }
        } else {
            acc |= 0x20;
        }
        break;
    case 1:
        if (*(u8 *)((s8 *)item + 1) != 3) {
            rec = (u8 *)lookup_item_pmt_record((u8 *)item);
            if (rec != 0) {
                if (check_class_equip_permission(p, (s16)*(u16 *)((s8 *)rec + 0xE)) == 0) {
                    acc |= 1;
                }
                if (((VObj_18_80105218 *)p)->m14() < (s32)*(u8 *)((s8 *)rec + 0x10)) {
                    acc |= 0x10;
                }
            } else {
                acc |= 0x20;
            }
        } else {
            if (check_class_equip_permission(p, 0xD7) != 0) {
                rec2 = (u8 *)lookup_item_pmt_record((u8 *)item);
                if (rec2 != 0) {
                    k = *(s16 *)((s8 *)rec2 + 8);
                    switch (k) {
                    case 1:
                    case 5:
                    case 16:
                    case 18:
                    case 21:
                        acc |= 1;
                        break;
                    default:
                        break;
                    }
                } else {
                    acc |= 0x20;
                }
            }
        }
        break;
    case 2:
        rec = (u8 *)lookup_item_pmt_record((u8 *)item);
        if (rec != 0) {
            if (check_class_equip_permission(p, (s16)*(u16 *)((s8 *)rec + 0x14)) == 0) {
                acc |= 1;
            }
        } else {
            acc |= 0x20;
        }
        break;
    case 3:
        t = *(u8 *)((s8 *)item + 1);
        switch (t) {
        case 2:
            {
                u8 ib = ((u8 *)item)[4], pb = ((u8 *)p)[0x88D];
                lim = get_technique_learn_limit(pb, ib);
            }
            if (lim == 0xFF || lim < *(u8 *)((s8 *)item + 2)) {
                acc |= 1;
            }
            break;
        case 8:
            if (check_class_equip_permission(p, 0xD7) != 0) {
                acc |= 1;
            }
            break;
        default:
            break;
        }
        break;
    case 4:
        if ((s32)*(u32 *)((s8 *)item + 0x10) > 999999) {
            acc |= 0x20;
        }
        break;
    default:
        break;
    }
    if (requirement != 0) {
        *requirement = acc;
    }
    if (acc == 0) {
        return 1;
    }
    return 0;
}
#pragma pop

int check_class_equip_permission(TObjPlayer *player, s32 perm) {
    s32 t = player->class_flags;
    if (t & CLASS_FLAG_HUNTER) {
        if (!(perm & 1)) return 0;
    } else if (t & CLASS_FLAG_RANGER) {
        if (!(perm & 2)) return 0;
    } else if (!(perm & 4)) {
        return 0;
    }
    if (t & CLASS_FLAG_ANDROID) {
        if (!(perm & 0x10)) return 0;
    } else if (t & CLASS_FLAG_NEWMAN) {
        if (!(perm & 0x20)) return 0;
    } else if (t & CLASS_FLAG_HUMAN) {
        if (!(perm & 8)) return 0;
    }
    if (t & CLASS_FLAG_MALE) {
        if (!(perm & 0x40)) return 0;
    } else if (t & CLASS_FLAG_FEMALE) {
        if (!(perm & 0x80)) return 0;
    }
    return 1;
}

int roll_weapon_special_channel15(void* p) { return roll_weapon_special_for_stars(p); }
}

TItem *construct_item(TItemData *data) {
    Item_8010542C *src = (Item_8010542C *)data;
    Fn_8010542C fn;
    if (src != 0) {
        Item_8010542C item = *src;
        ((TItemData *)&item)->decode_from_network();
        if (((TItemData *)(&item))->isValidGroundDrop() != 0) {
            if (*(u8 *)src < 5) {
                fn = item_create_fn_table[*(u8 *)src];
                if (fn != 0) {
                    observe_item_id(item.b.w[2]);
                    return (TItem *)fn(&item);
                }
            }
        }
    }
    return 0;
}

extern "C" {

s32 TLobby__sub_801054E0(In_801054E0 *arg0) {
    if (arg0 != 0) {
        if (arg0->idx < 4) {
            if (item_pro_create_fn_table[arg0->idx].fn != 0) {
                return item_pro_create_fn_table[arg0->idx].fn(arg0);
            }
        }
    }
    return 0;
}

void send_6x60_standard_drop_item_request(Obj_80105538 *self) {
    void *p1;
    void *p2;
    if (self != 0) {
        p1 = get_player_by_client_id(TLobby__designated_client_id);
        p2 = get_player_by_client_id(local_client_id);
        if (p1 != 0 && p2 != 0) {
            get_current_floor();
            if (is_valid_drop_floor() != 0 &&
                (((TObjPlayer *)p1)->get_floor() != ((TObjPlayer *)p2)->get_floor() ||
                 TLobby__designated_client_id == local_client_id)) {
                if (self->f2c != -1) {
                    Rec_80105538 e = TLobby__data_805D6144[self->f2c];
                    if (e.b != 0xFFFF) {
                        Pkt_80105538 pkt;
                        build_6x06_send_guild_card(&pkt);
                        pkt.f4 = get_current_floor();
                        pkt.f5 = self->f370;
                        pkt.f6 = self->f2c;
                        pkt.x = self->x;
                        pkt.z = self->z;
                        pkt.f10 = self->f28;
                        pkt.f14 = get_current_floor_area();
                        Vec_80105538 v;
                        v.x = pkt.x;
                        v.y = lbl_805DAAB4;
                        v.z = pkt.z;
                        if (csnVecterUnder((s32)&v, 1) != 0) {
                            ((TLobby *)(&pkt))->dispatch_packet_wrapper();
                        }
                    }
                }
            }
        }
    }
}

void TObjChara::request_box_item_drop(void *unused, s16 arg2) {
    Obj_8010567C *self = (Obj_8010567C *)this;
    void *p1;
    void *p2;
    if (self != 0) {
        p1 = get_player_by_client_id(TLobby__designated_client_id);
        p2 = get_player_by_client_id(local_client_id);
        if (p1 != 0 && p2 != 0 && TObjPlayer__sub_80104840(get_current_floor_area()) != AREA_PIONEER2_EP1 &&
            (((TObjPlayer *)p1)->get_floor() != ((TObjPlayer *)p2)->get_floor() ||
             TLobby__designated_client_id == local_client_id)) {
            if (self->f2c != -1) {
                Entry_8010567C e = quest_object_entries[self->f2c];
                if (e.b != 0xFFFF) {
                    Pkt_8010567C pkt;
                    ((TLobby *)(&pkt))->build_6x06_guild_card_packet();
                    pkt.f4 = get_current_floor();
                    pkt.f5 = 0x30;
                    pkt.x = self->x;
                    pkt.z = self->z;
                    pkt.f10 = self->f28;
                    pkt.f12 = arg2;
                    pkt.f6 = self->f2c;
                    pkt.f14 = get_current_floor_area();
                    pkt.f18 = self->f70;
                    pkt.f1c = this->set_params[0];
                    pkt.f20 = self->f88;
                    pkt.f24 = this->set_params[2];
                    ((TLobby *)(&pkt))->process_and_dispatch_packet();
                }
            }
        }
    }
}
}
