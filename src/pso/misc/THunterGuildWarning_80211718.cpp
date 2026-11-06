#include "types.h"
#include "pso/misc/TWindowBase.h"
#include "pso/misc/TWindowSubComCard_80244774.h"
#include "pso/THunterGuildWarning.h"
struct Obj_802119CC { u8 pad[0x24]; s32 a[4]; };

struct S_80211718 { u8 pad[0x1c]; s32 state; u8 pad20[4]; u32 w[4]; };

struct Pos2_80211774 { f32 x; f32 y; };
struct Coord2_80211774 { s32 x; s32 y; };

extern "C" {
void THunterGuildWarning__sub_802119CC(Obj_802119CC *self);
int get_instance__11TCameraCtrlFv(void);
s32 get_nth_view_player_id__11TCameraCtrlFl(s32);
u32 get_player_by_client_id(s32);
s32 get_window_layout_position(s32);
void *create_message_window__6TLobbyFllUls(s32, void *, s32, s32);
s32 send_and_handle__6TLobbyFii(u32, s32, s32);
void set_position_xy__13TUnk_804CDFE8Fff(u32, f32, f32);
s32 TQuestVmDownLoadServer__sub_8006EF6C(s32);
s32 get_game_play_mode();
extern const u32 lbl_8044BC7C[];
extern const u32 lbl_8044BC84[];
extern const f32 lbl_805DC640;

void THunterGuildWarning::close_windows() {
    S_80211718 *self = (S_80211718 *)this;
    s32 i = 0;
    do {
        if (self->w[i] != 0) {
            ((TWindowBase *)(self->w[i]))->close();
            self->w[i] = 0;
        }
        i++;
    } while (i < 4);
}

void THunterGuildWarning__sub_80211774(void *selfv) {
    S_80211718 *self = (S_80211718 *)selfv;
    Coord2_80211774 pair;
    pair.x = lbl_8044BC7C[0];
    pair.y = lbl_8044BC7C[1];
    Pos2_80211774 pos = *(const Pos2_80211774 *)lbl_8044BC84;
    if (get_instance__11TCameraCtrlFv() > 2) {
        pos.x = lbl_805DC640;
        pos.y = lbl_805DC640;
    }
    switch (self->state) {
    case 0: {
        s32 raw = get_nth_view_player_id__11TCameraCtrlFl(0);
        u16 id = (u16)raw;
        if (((!self) && (!self)) && (!self)) {
        }
        if (!self) {
        }
        if (get_player_by_client_id(id) != 0) {
            self->w[(u16)raw] = (u32)create_message_window__6TLobbyFllUls(get_window_layout_position(0x31), &pair, 1, id);
        }
        if (self->w[(u16)raw] == 0) {
            break;
        }
        send_and_handle__6TLobbyFii(self->w[(u16)raw], TQuestVmDownLoadServer__sub_8006EF6C(0x63), 0x81);
        set_position_xy__13TUnk_804CDFE8Fff(self->w[(u16)raw], pos.x, pos.y);
        break;
    }
    case 1: {
        s32 raw = get_nth_view_player_id__11TCameraCtrlFl(0);
        u16 id = (u16)raw;
        if (((!self) && (!self)) && (!self)) {
        }
        if (get_player_by_client_id(id) != 0) {
            self->w[(u16)raw] = (u32)create_message_window__6TLobbyFllUls(get_window_layout_position(0x31), &pair, 1, id);
        }
        if (self->w[(u16)raw] == 0) {
            break;
        }
        send_and_handle__6TLobbyFii(self->w[(u16)raw], TQuestVmDownLoadServer__sub_8006EF6C(0x68), 0x81);
        set_position_xy__13TUnk_804CDFE8Fff(self->w[(u16)raw], pos.x, pos.y);
        break;
    }
    case 2: {
        s32 msg = 0x64;
        if (get_game_play_mode() == 2) {
            msg = 0x6a;
        }
        s32 raw = get_nth_view_player_id__11TCameraCtrlFl(0);
        s32 vm = (0, msg);
        s32 i;
        for (i = 0; i < 4; i++) {
            if ((u16)(raw & 0xFFFFFFFFFFFFFFFFu) == i) {
                continue;
            }
            if (get_player_by_client_id(i) != 0) {
                self->w[i] = (u32)create_message_window__6TLobbyFllUls(get_window_layout_position(0x31), &pair, 1, i);
            }
            if (self->w[i] == 0) {
                continue;
            }
            send_and_handle__6TLobbyFii(self->w[i], TQuestVmDownLoadServer__sub_8006EF6C(vm & 0xFFFFFFFFu), 0x81);
            set_position_xy__13TUnk_804CDFE8Fff(self->w[i], pos.x, pos.y);
        }
        break;
    }
    }
}

void THunterGuildWarning__sub_802119CC(Obj_802119CC *self) {
    s32 i;
    for (i = 0; i < 4; i++) self->a[i] = 0;
}

}
