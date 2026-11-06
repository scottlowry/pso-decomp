#include "types.h"
#include "pso/unk/TUnk_804C349C.h"
#include "pso/misc/TCameraCtrl.h"
#include "pso/misc/TFogCtrl.h"
#include "pso/misc/TLobby.h"

struct Rec_801AA17C {
    s32 kinds[4];
    s32 participants[4];
    s32 state;
};

struct Obj_801A9CB8 {
    u8 pad0[0x18];
    void *vt;
    u32 f1c;
    u32 f20;
    u32 f24;
    s32 count;
    u8 pad2c[0xc];
    s32 player;
    u16 id;
    s32 charge;
    s32 f44;
    s32 f48;
    s32 active;
    s32 entries50[4];
    u32 ids[4];
    s32 counts70[4];
    s32 types80[4];
    u16 holds90[4];
};

extern struct Rec_801AA17C photon_blast_sequence_table[];
extern "C" {
s32 get_photon_blast_chain(struct Rec_801AA17C *output, s32 player);
void __dt__7TObjectFv(void *, int);
s32 restore_player_cameras(void);
}
void reset_cameras_to_actor(void *actor, s32 arg1);
extern "C" {
void *get_player_by_client_id(s32);
void release_photon_blast_player_holds(u16 *p);
void __dl__7TObjectFPv(void *);
void TLobby__sub_8024AC20(s32);
extern u8 __vt__13TUnk_804C349C[];
extern s32 local_client_id;
extern s32 tl_07;
Obj_801A9CB8 *__dt__13TUnk_804C349CFv(Obj_801A9CB8 *self, s16 flag);
void __ct__7TObjectFP7TObject(void *, void *);
s32 get_photon_blast_charge__10TObjPlayerFv(void *);
s32 TObjPlayer__sub_80313114(void *);
s32 get_section_id__10TObjPlayerFv(void *);
void apply_photon_blast_action_hold__Flll(s32, s32, s32);
void send_neg30__6TLobbyFv(void);
void TObjPlayer__sub_8024ABDC(s32);
void VecCopy__FP3VecPC3Vec(void *, void *);
s32 play_sound_effect(s32, s32, s32, s32);
void clear_photon_blast_hits__Fv(void);
void clear_deferred_photon_blast_hits__Fv(void);
s32 get_entity_id(void *);
void *find_photon_blast_by_section_id__10TObjPlayerFl(s32, s32);
s32 get_entity_type__10TObjPlayerFv(void *);
s32 get_room__8TObjBaseFv(void *);
void freeze_players_for_photon_blast__FsPUs(s32, u16 *);

}
TUnk_804C349C::~TUnk_804C349C() {
    s32 i;
    s32 j;
    if (((Obj_801A9CB8 *)this)->active != 0) {
        TLobby::set_and_notify_default();
        release_photon_blast_player_holds((u16 *)((u8 *)this + 0x90));
        if (get_player_by_client_id(local_client_id) != NULL) {
            TLobby__sub_8024AC20(local_client_id);
            TCameraCtrl::release_photon_blast_camera();
            restore_player_cameras();
            reset_cameras_to_actor(get_player_by_client_id(local_client_id), 0);
        }
    } else {
        TFogCtrl::restore_fog_for_player(((Obj_801A9CB8 *)this)->id, 0);
    }
    if (((Obj_801A9CB8 *)this)->id != 0xFFFF && ((Obj_801A9CB8 *)this)->id < 4) {
        for (i = 0; i < 4; i++) {
            if (((Obj_801A9CB8 *)this)->ids[i] < 4) {
                for (j = 0; j < 4; j++) {
                    photon_blast_sequence_table[((Obj_801A9CB8 *)this)->ids[i]].kinds[j] = -1;
                    photon_blast_sequence_table[((Obj_801A9CB8 *)this)->ids[i]].participants[j] = 0xFFFF;
                }
                photon_blast_sequence_table[((Obj_801A9CB8 *)this)->ids[i]].state = 0;
            }
        }
    }
}
extern "C" {

Obj_801A9CB8 *TObjPlayer__sub_801A9E10(Obj_801A9CB8 *self, s32 client_id, u8 *records,
                                       u32 *ids_src, s32 flag, s32 cost) {
    s32 i;
    s32 j;
    s32 neg1;
    s32 player;
    s32 *obj;

    __ct__7TObjectFP7TObject(self, (void *)tl_07);
    self->vt = __vt__13TUnk_804C349C;
    self->id = (u16)client_id;
    self->f48 = cost;
    self->f44 = 0;
    self->active = flag;
    for (i = 0; i < 4; i++) {
        self->counts70[i] = ids_src[i] + 1;
        self->entries50[i] = -1;
        self->holds90[i] = 0xFFFF;
    }
    self->charge = 0;
    if (get_player_by_client_id(client_id) != 0) {
        self->charge = get_photon_blast_charge__10TObjPlayerFv(get_player_by_client_id(client_id));
    }
    for (i = 0; i < 4; i++) {
        self->ids[i] = 0xFFFF;
    }
    self->count = 4;
    for (i = 0; i < 4; i++) {
        if ((s16)TObjPlayer__sub_80313114(records) == -1) {
            self->count = i;
            break;
        }
        self->entries50[i] = (s16)TObjPlayer__sub_80313114(records);
        self->ids[i] = (u16)get_section_id__10TObjPlayerFv(records);
        records += 24;
    }
    self->player = (s32)get_player_by_client_id(client_id);
    apply_photon_blast_action_hold__Flll((s32)self, self->count * 150 + 100, client_id);
    if (self->active != 0) {
        send_neg30__6TLobbyFv();
        TObjPlayer__sub_8024ABDC(local_client_id);
        if (self->player != 0) {
            VecCopy__FP3VecPC3Vec(self->pad2c, (void *)(self->player + 0x38));
            play_sound_effect(0x40021927, (s32)self->pad2c, 0, 0);
        }
        clear_photon_blast_hits__Fv();
    } else {
        clear_deferred_photon_blast_hits__Fv();
        TFogCtrl::select_fog_for_viewport(self->id, 0x3e, 0);
    }
    for (i = 0; i < 4; i++) {
        if (self->ids[i] < 4) {
            if (photon_blast_sequence_table[self->ids[i]].state != 2) {
                for (j = 0; j < 4; j++) {
                    photon_blast_sequence_table[self->ids[i]].kinds[j] = self->entries50[j];
                    photon_blast_sequence_table[self->ids[i]].participants[j] = self->ids[j];
                }
            }
            photon_blast_sequence_table[self->ids[i]].state = 2;
        }
    }
    self->f1c = 0;
    self->f20 = 0;
    self->f24 = 0;
    neg1 = -1;
    for (i = 0; i < 4; i++) {
        self->types80[i] = neg1;
    }
    if (self->player != 0 && get_player_by_client_id(local_client_id) != 0 &&
        (obj = (s32 *)find_photon_blast_by_section_id__10TObjPlayerFl(
                    get_entity_id((void *)self->player), neg1)) != 0) {
        for (i = 0; i < 4; i++) {
            if ((u16)get_entity_type__10TObjPlayerFv(obj) != 0xFFFF &&
                (u16)get_entity_type__10TObjPlayerFv(obj) != (u16)self->id) {
                self->types80[i] = (u16)get_entity_type__10TObjPlayerFv(obj);
            }
            obj++;
        }
    }
    if (self->active != 0) {
        player = (s32)get_player_by_client_id(self->id);
        if (player != 0) {
            freeze_players_for_photon_blast__FsPUs(get_room__8TObjBaseFv((void *)player),
                                                   self->holds90);
        }
    }
    return self;
}

s32 get_photon_blast_chain(struct Rec_801AA17C *output, s32 player) {
    s32 i;
    if (photon_blast_sequence_table[player].state == 0) {
        return 0;
    }
    if (photon_blast_sequence_table[player].state == 2) {
        for (i = 0; i < 4; i++) {
            output->kinds[i] = photon_blast_sequence_table[player].kinds[i];
            output->participants[i] = photon_blast_sequence_table[player].participants[i];
        }
        return 2;
    }
    if (photon_blast_sequence_table[player].state == 1) {
        for (i = 0; i < 4; i++) {
            output->kinds[i] = photon_blast_sequence_table[player].kinds[i];
            output->participants[i] = photon_blast_sequence_table[player].participants[i];
        }
        return 1;
    }
    return 0;
}
}
