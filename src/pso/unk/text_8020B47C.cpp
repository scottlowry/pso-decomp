#include "types.h"
#include "pso/system/byteswap.h"

struct Dst_8020B47C { s16 f0; s16 f2; s32 f4; };
struct Row_8020B47C { s32 f0; s32 f4; u8 pad8[8]; Dst_8020B47C *f10; Dst_8020B47C *f14; };

extern "C" {
void bswap_4_words__6TLobbyFv(void *self);
extern Row_8020B47C TLobby__floor_enemy_group_table[];
void TLobby__sub_8020B47C(void *self);
}

void TLobby__sub_8020B47C(void *self)
{
  s16 t1;
  s16 t2;
  u8 *cur;
  s32 i1;
  s32 n1;
  u32 a;
  s32 n2;
  s32 j1;
  s32 i2;
  s32 j2;
  Dst_8020B47C *new_var[2];
  bswap_4_words__6TLobbyFv(self);
  a = *((u32 *) (((u8 *) self) + 0x0));
  cur = ((u8 *) self) + a;
  for (i1 = 0; i1 < 18; i1++)
  {
    Row_8020B47C *row = &TLobby__floor_enemy_group_table[i1];
    n1 = row->f0;
    if (n1 > 0)
    {
      new_var[1] = row->f10;
      j1 = 0;
      while (j1 < n1)
      {
        t1 = *((s16 *) cur);
        bswap_16((u16 *) (&t1));
        cur += 2;
        j1++;
        new_var[1]->f2 = t1;
        new_var[1]++;
      }

    }
  }

  a = *((u32 *) (((u8 *) self) + 0x8));
  cur = ((u8 *) self) + a;
  for (i2 = 0; i2 < 18; i2++)
  {
    Row_8020B47C *row = &TLobby__floor_enemy_group_table[i2];
    n2 = row->f4;
    if (n2 > 0)
    {
      new_var[0] = row->f14;
      j2 = 0;
      while (j2 < n2)
      {
        t2 = *((s16 *) cur);
        bswap_16((u16 *) (&t2));
        cur += 2;
        j2++;
        new_var[0]->f2 = t2;
        new_var[0]++;
      }

    }
  }

}
