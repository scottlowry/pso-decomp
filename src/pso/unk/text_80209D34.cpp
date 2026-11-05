#include "types.h"
#include "pso/misc/TLobby.h"
#include "pso/misc/TLobby_80207644.h"
#include "pso/misc/TLobby_80209BD8.h"
#include "pso/misc/TLobby_8020A568.h"
#include <string.h>

struct Hdr_80209D34 { u32 a, b, count, d; };

struct Ent_80209D34 {
    u32 w0;
    s16 a;
    s16 b;
    s16 c;
    s16 d;
    s16 e;
    s16 f;
    u8 g;
    u8 h;
    s16 i;
    u32 j;
};

extern "C" {
extern u32 lbl_805D60A8;
extern s32 lbl_805D60B4;
extern s32 lbl_805D60BC;
extern s32 lbl_805D60C0;
extern s32 lbl_805D60C4;
extern s32 lbl_805D60C8;
extern s32 lbl_805D60CC;

s16 clamp_min_drop__6TLobbyFUl(s32, s32);
void TLobby__sub_802097B0(s16);
void *alloc_heap_slot__6TLobbyFll(s32, s32);
void append_swapped_u32__6TLobbyFPl(s32 *);
void move_data__6TLobbyFPCvUl(void *, void *, void *);
void reserve_enemy_set_actor_ids(void *, s32, s32);
void init_floor_enemy_count__6TLobbyFlPUcUl(s32, void *, s32);

void TLobby__sub_80209D34(TLobby *lobby) {
    Hdr_80209D34 hdr;
    Ent_80209D34 ent;
    u8 *walk;
    u32 *src;
    s32 r29;
    s32 off;
    s32 picked;
    s32 i;
    s32 cnt;
    s32 cnt2;
    s32 d26;
    s32 r27;
    u8 flag;
    s32 swp;
    u32 desc[3];
    u8 *heap;
    s32 n;
    s32 pad;

    src = (u32 *)lbl_805D60A8;
    hdr.a = src[0];
    hdr.b = src[1];
    hdr.count = src[2];
    hdr.d = src[3];
    ((TLobby *)&hdr)->swap_endian_header();

    walk = (u8 *)lbl_805D60A8 + hdr.b;
    r29 = lbl_805D60CC - (hdr.count * 0x18 + 0x10);
    memset((void *)lbl_805D60B4, 0, 0x9000);
    memset((void *)lbl_805D60BC, 0, 0x1400);
    lbl_805D60C0 = 0;
    memset((void *)lbl_805D60C4, 0, 0x1000);
    off = 0;
    picked = 0;
    lbl_805D60C8 = 0;
    for (i = 0; i < hdr.count; i++) {
        TLobby__sub_8020A618(&ent, walk);
        ((TLobby *)&ent)->bswap();
        cnt = clamp_min_drop__6TLobbyFUl(1, ent.i + 1);
        r27 = ent.d;
        d26 = (s16)ent.w0;
        while (cnt-- > 0) {
            cnt2 = clamp_min_drop__6TLobbyFUl(ent.g, ent.h + 1);
            TLobby__sub_802097B0(ent.c);
            while (cnt2-- > 0) {
                if (pick_random_slot__6TLobbyFPv((s16 *)(lbl_805D60B4 + off)) == 0) {
                    picked++;
                    *(s16 *)(lbl_805D60B4 + off + 0xE) = r27;
                    off += 0x48;
                    *(s16 *)(lbl_805D60B4 + off + 0xC) = ent.c;
                }
            }
            if (cnt > 0) {
                n = lbl_805D60C0;
                *(s32 *)((u8 *)&lbl_805D60BC + n * 0x14) = d26;
                *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 4) = ent.a;
                *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 6) = ent.b;
                *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 8) = ent.c;
                *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 0xA) = r27;
                cnt2 = clamp_min_drop__6TLobbyFUl(ent.e, ent.f + 1);
                n = lbl_805D60C0;
                *(s32 *)((u8 *)&lbl_805D60BC + n * 0x14 + 0xC) = cnt2;
                desc[0] = 0xC;
                d26 = (s16)(ent.w0 + cnt2 + 10000);
                ((TLobby *)&flag)->append_entity_entry();
                swp = (u16)d26;
                append_swapped_u32__6TLobbyFPl(&swp);
                desc[0] = 1;
                ((TLobby *)&flag)->append_entity_entry();
                r27++;
                lbl_805D60C0 = lbl_805D60C0 + 1;
            }
        }
        TLobby__sub_8020A618(&ent, walk);
        ((TLobby *)&ent)->bswap();
        n = lbl_805D60C0;
        *(s32 *)((u8 *)&lbl_805D60BC + n * 0x14) = d26;
        *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 4) = ent.a;
        *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 6) = ent.b;
        *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 8) = ent.c;
        *(s16 *)((u8 *)&lbl_805D60BC + n * 0x14 + 0xA) = r27;
        cnt2 = clamp_min_drop__6TLobbyFUl(ent.e, ent.f + 1);
        n = lbl_805D60C0;
        *(s32 *)((u8 *)&lbl_805D60BC + n * 0x14 + 0xC) = cnt2;
        n = lbl_805D60C0;
        *(u32 *)((u8 *)&lbl_805D60BC + n * 0x14 + 0x10) = ent.j;
        walk += 0x18;
        lbl_805D60C0 = lbl_805D60C0 + 1;
    }
    if (picked > 0) {
        n = get_floor_area((s32)lobby);
        reserve_enemy_set_actor_ids((void *)lbl_805D60B4, picked, n);
        init_floor_enemy_count__6TLobbyFlPUcUl((s32)lobby, (void *)lbl_805D60B4, picked * 0x48);
    }
    n = lbl_805D60C0;
    if (n > 0) {
        pad = (lbl_805D60C8 + 3) & ~3;
        heap = (u8 *)alloc_heap_slot__6TLobbyFll((s32)lobby, n * 0x14 + r29 + pad + 0x10);
        if (heap != 0) {
            desc[0] = n * 0x14 + 0x10;
            desc[1] = 0x10;
            desc[2] = n;
            move_data__6TLobbyFPCvUl(heap, desc, (void *)0x10);
            heap += 0x10;
            n = lbl_805D60C0;
            if (n > 0) {
                move_data__6TLobbyFPCvUl(heap, (void *)lbl_805D60BC, (void *)(n * 0x14));
            }
            if (r29 > 0) {
                heap += n * 0x14;
                move_data__6TLobbyFPCvUl(heap, (void *)(lbl_805D60A8 + hdr.a), (void *)r29);
            }
            if (pad > 0) {
                move_data__6TLobbyFPCvUl(heap + r29, (void *)lbl_805D60C4, (void *)pad);
            }
        }
    }
}
}
