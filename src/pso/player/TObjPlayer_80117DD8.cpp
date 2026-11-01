#include "types.h"
#include "pso/item/TItem.h"
#include "pso/player/TObjPlayer.h"
#include "pso/item/TItemData.h"
#include "pso/item/TItemProShield.h"

struct Pl_80117F14 { u8 pad0[0x38]; f32 pos[3]; };

extern "C" {
f32 horizontal_distance_squared(void *, void *);
void *get_player_by_client_id(s32 i);
extern const f64 lbl_8043E650[];

extern const f64 lbl_8043E648[];

s32 TObjPlayer__sub_80117E50(u16 idx) {
    s32 key;
    Pl_80117F14 *me;
    s32 mask;
    s32 result;
    u16 i;
    Pl_80117F14 *other;

    result = 0;
    me = (Pl_80117F14 *)get_player_by_client_id(idx);
    if (me != NULL) {
        mask = (*(u32 *)((u8 *)me + 0x890) & 1) + 1;
        key = ((TObjPlayer *)me)->get_field_3e4();
        for (i = 0; i != 4; i++) {
            if (i != idx) {
                other = (Pl_80117F14 *)get_player_by_client_id(i);
                if (other != NULL && (*(u32 *)((u8 *)other + 0x890) & mask) != 0 &&
                    ((TObjPlayer *)other)->get_field_3e4() == key &&
                    horizontal_distance_squared(me->pos, other->pos) < lbl_8043E648[0]) {
                    result = 1;
                    break;
                }
            }
        }
    }
    return result;
}
s32 TObjPlayer::count_nearby_players_with_shield(u16 idx, u8 *item) {
    s32 key;
    Pl_80117F14 *me;
    s32 count;
    u16 i;
    Pl_80117F14 *other;
    void *it;
    count = 0;
    me = (Pl_80117F14 *)get_player_by_client_id(idx);
    if (me != NULL && item != NULL) {
        key = ((TObjPlayer *)me)->get_field_3e4();
        for (i = 0; i != 4; i++) {
            if (i != idx) {
                other = (Pl_80117F14 *)get_player_by_client_id(i);
                if (other != NULL && key == ((TObjPlayer *)other)->get_field_3e4() &&
                    horizontal_distance_squared(me->pos, other->pos) < lbl_8043E650[0] &&
                    (it = (void *)((TItemData *)other)->test_flag3()) != NULL &&
                    item[2] == ((TItem *)it)->get_item_index()) {
                    count++;
                }
            }
        }
    }
    return count;
}

}
