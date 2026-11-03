#include "types.h"
#include "pso/item/TItem.h"
#include "pso/misc/TWindowSubEquip.h"
#include "pso/misc/TWindowSubStatusDisp.h"
#include "pso/player/TObjPlayer.h"

struct ItemData_80279178 {
    u8 b[0x14];
};

extern "C" {

void *get_player_by_client_id(s32 i);
s32 get_class_weapon_icon_index(void *self, u8 *p);
s32 get_slot_value__10TObjPlayerFPvi(s32 *arg0, s32 arg1);

s32 init_status_entry__20TWindowSubStatusDispFPvcUii(void *, u8, s32, s32);
void *get_array_entry__11TWindowBaseFi(void *, s16);

extern const f32 lbl_805DD620;

void TObjPlayer::add_status_line(u8 arg1, u32 arg2, s32 arg3) {
    void *temp_r31;

    temp_r31 = get_array_entry__11TWindowBaseFi(this, *(s16 *)((s8 *)this + 0x72));
    if (arg2 == 0U) {
        init_status_entry__20TWindowSubStatusDispFPvcUii(temp_r31, arg1, 0, arg3);
        *(f32 *)((s8 *)temp_r31 + 8) = (f32) (*(f32 *)((s8 *)temp_r31 + 8) + lbl_805DD620);
        ((TWindowSubStatusDisp *)temp_r31)->m_2c = 0xFFAAAAAA;
    } else {
        ((TWindowSubStatusDisp *)temp_r31)->init_item_row((void *)arg2, (s32)arg3);
    }
    if (arg1 == 4) {
        *(f32 *)((s8 *)temp_r31 + 8) = (f32) (*(f32 *)((s8 *)temp_r31 + 8) + lbl_805DD620);
    }
    *(s16 *)((s8 *)this + 0x72) = (s16) (*(s16 *)((s8 *)this + 0x72) + 1);
}

void TWindowSubEquip::build_equipment_list() {
    ItemData_80279178 d;
    s32 player;
    s32 icon;
    s32 item;
    s32 count;
    s32 i;

    player = (s32)get_player_by_client_id((s32)*(s16 *)((s8 *)this + 0x20));
    if (player != 0) {
        icon = get_class_weapon_icon_index(this, (u8 *)player);
        ((TObjPlayer *)this)->add_status_line(icon, get_slot_value__10TObjPlayerFPvi((s32 *)(player + 0xD04), 6), 6);
        item = get_slot_value__10TObjPlayerFPvi((s32 *)(player + 0xD04), 2);
        ((TObjPlayer *)this)->add_status_line(0xb, item, 2);
        if (item != 0) {
            ((TItem *)item)->copy_to_item_data((TItemData *)&d);
            count = (s8)d.b[13];
            for (i = 0; i < count; i++) {
                ((TObjPlayer *)this)->add_status_line(4, get_slot_value__10TObjPlayerFPvi((s32 *)(player + 0xD04), i + 9), i + 9);
            }
        }
        ((TObjPlayer *)this)->add_status_line(0xa, get_slot_value__10TObjPlayerFPvi((s32 *)(player + 0xD04), 3), 3);
        ((TObjPlayer *)this)->add_status_line(3, get_slot_value__10TObjPlayerFPvi((s32 *)(player + 0xD04), 1), 1);
    }
}

}
