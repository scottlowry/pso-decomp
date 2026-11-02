#include "types.h"
#include "pso/item/TItemEffPG_8034FE28.h"
#include "pso/item/TUnk_804F0C08.h"
#include "pso/player/TObjPlayer.h"
#include "pso/player/TObjChara.h"

extern "C" {

void TItemEffPG__ct(void *);
void *__nw__7TObjectFUl(int);
void *get_player_by_client_id(s32 i);

extern s32 lbl_804F0C08[];

void *TUnk_804F0C08::initialize(void *arg1, void *arg2, void *arg3) {
    TItemEffPG__ct(this);
    *(s32 **)((s8 *)this + 0x18) = lbl_804F0C08;
    *(void * *)&this->unk_D4 = arg3;
    return this;
}

s32 TItemEffPG::vfunc_7() {
    void *player = get_player_by_client_id(this->m_a8);
    if (player == NULL) {
        return 0;
    }
    if ((f32) ((TObjPlayer *)player)->get_photon_blast_charge() < *(f32 *)&this->unk_CC) {
        return 0;
    }
    ((TObjChara *)player)->vfunc_76();
    return 1;
}

void create__10TItemEffPGFPvPvPv(void *arg0, void *parent, void *item) {
    void *o;
    o = __nw__7TObjectFUl(0xD8);
    if (o != NULL) {
        ((TUnk_804F0C08 *)o)->initialize(arg0, parent, item);
    }
}

}
