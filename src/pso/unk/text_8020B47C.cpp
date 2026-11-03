#include "types.h"
#include "pso/system/byteswap.h"

struct Dst_8020B47C { s16 f0; s16 f2; s32 f4; };

extern "C" {
void bswap_4_words__6TLobbyFv(void *self);
extern u32 TLobby__floor_enemy_group_table[];
void TLobby__sub_8020B47C(void *self);
}

void TLobby__sub_8020B47C(void *self) {
    s16 t1, t2;
    u8 *cur;
    s32 off;
    u32 a;
    s32 i1, i2;
    s32 n1, n2;
    s32 j1, j2;
    u8 *base1, *base2;
    Dst_8020B47C *d1, *d2;

    bswap_4_words__6TLobbyFv(self);

    a = *(u32 *)((u8 *)self + 0x0);
    base1 = (u8 *)TLobby__floor_enemy_group_table;
    i1 = 0;
    cur = (u8 *)self + a;
    off = 0;
    for (; i1 < 18; i1++, off += 0x18) {
        u8 *p = base1 + off;
        n1 = *(s32 *)(p + 0x0);
        if (n1 > 0) {
            d1 = *(Dst_8020B47C **)(p + 0x10);
            j1 = 0;
            while (j1 < n1) {
                t1 = *(s16 *)cur;
                bswap_16((u16 *)&t1);
                cur += 2;
                j1++;
                d1->f2 = t1;
                d1++;
            }
        }
    }

    a = *(u32 *)((u8 *)self + 0x8);
    base2 = (u8 *)TLobby__floor_enemy_group_table;
    i2 = 0;
    cur = (u8 *)self + a;
    off = 0;
    for (; i2 < 18; i2++, off += 0x18) {
        u8 *p = base2 + off;
        n2 = *(s32 *)(p + 0x4);
        if (n2 > 0) {
            d2 = *(Dst_8020B47C **)(p + 0x14);
            j2 = 0;
            while (j2 < n2) {
                t2 = *(s16 *)cur;
                bswap_16((u16 *)&t2);
                cur += 2;
                j2++;
                d2->f2 = t2;
                d2++;
            }
        }
    }
}
