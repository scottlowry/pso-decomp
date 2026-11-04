
typedef signed char s8;
typedef unsigned char u8;
typedef signed short s16;
typedef unsigned short u16;
typedef signed long s32;
typedef unsigned long u32;
typedef signed long long s64;
typedef unsigned long long u64;
typedef float f32;
typedef double f64;
extern s32 is_item_valid__9TItemListFl(void *);
extern u8 *__nw__FUl(u32);
extern u8 *TObjPlayer__sub_801D46D4(u8 *, s32);
extern u8 *TObjPlayer__sub_801D4678(u8 *, s16);
extern void TObjPlayer__sub_801D45B0(s32 *, s32);
extern s32 get_owner_if_alive__10TObjPlayerFv(void *);
extern void sort_by_key__10TObjPlayerFv(void *);
extern void set_field_1c__10TObjPlayerFl(void *, s32);
s32 TObjPlayer__sub_801D4368(void *arg0)
{
  u8 *obj;
  void *down;
  s32 cnt_2;
  u32 *rec;
  void *down_2;
  s32 owner;
  u32 *rec_2;
  void *down_3;
  s32 cnt_3;
  s32 cnt;
  u32 *rec_3;
  void *down_4;
  if ((*((void **) (((s8 *) arg0) + 0x1c4))) == 0)
  {
    return 0;
  }
  if (is_item_valid__9TItemListFl(*((void **) (((s8 *) arg0) + 0x1c4))) == 0)
  {
    return 0;
  }
  if (((*((s16 *) (((s8 *) arg0) + 0x1c))) > 0x1e) || ((*((s16 *) (((s8 *) arg0) + 0x1c))) < 1))
  {
    return 0;
  }
  obj = __nw__FUl(8);
  if (obj != 0)
  {
    obj = TObjPlayer__sub_801D46D4(obj, *((s16 *) (((s8 *) arg0) + 0x1c)));
  }
  if (obj == 0)
  {
    return 0;
  }
  if ((*((u32 *) (obj + 4))) == 0)
  {
    TObjPlayer__sub_801D4678(obj, 1);
    return 0;
  }
  cnt = 0;
  down = *((void **) (((s8 *) (*((s32 *) (((s8 *) arg0) + 0x1c4)))) + 0x14));
  while (down != 0)
  {
    if ((is_item_valid__9TItemListFl(down) != 0) && (get_owner_if_alive__10TObjPlayerFv(down) != 0U))
    {
      cnt++;
    }
    down = *((void **) (((s8 *) down) + 0xC));
  }

  if (cnt != (*((s16 *) (((s8 *) arg0) + 0x1c))))
  {
    TObjPlayer__sub_801D4678(obj, 1);
    return 0;
  }
  cnt_2 = 0;
  rec = (u32 *) (*((s32 *) (obj + 4)));
  down_2 = *((void **) (((s8 *) (*((s32 *) (((s8 *) arg0) + 0x1c4)))) + 0x14));
  while (down_2 != 0)
  {
    if ((is_item_valid__9TItemListFl(down_2) != 0) && ((owner = get_owner_if_alive__10TObjPlayerFv(down_2)) != 0U))
    {
      rec[1] = owner;
      TObjPlayer__sub_801D45B0((s32 *) rec, owner);
      if (!down_4)
      {
      }
      rec = (u32 *) (((s8 *) rec) + 8);
      cnt_2++;
    }
    down_2 = *((void **) (((s8 *) down_2) + 0xC));
  }

  sort_by_key__10TObjPlayerFv(obj);
  cnt_3 = 0;
  rec_2 = (u32 *) (*((s32 *) (obj + 4)));
  down_3 = *((void **) (((s8 *) (*((s32 *) (((s8 *) arg0) + 0x1c4)))) + 0x14));
  while (down_3 != 0)
  {
    if (((is_item_valid__9TItemListFl(down_3) != 0) && (get_owner_if_alive__10TObjPlayerFv(down_3) != 0U)) && (rec_2[1] != 0))
    {
      rec_2 = (u32 *) (((s8 *) rec_2) + 8);
      cnt_3++;
    }
    down_3 = *((void **) (((s8 *) down_3) + 0xC));
  }

  if (cnt_2 != cnt_3)
  {
    TObjPlayer__sub_801D4678(obj, 1);
    return 0;
  }
  rec_3 = (u32 *) (*((s32 *) (obj + 4)));
  down_4 = *((void **) (((s8 *) (*((s32 *) (((s8 *) arg0) + 0x1c4)))) + 0x14));
  while (down_4 != 0)
  {
    if ((is_item_valid__9TItemListFl(down_4) != 0) && (get_owner_if_alive__10TObjPlayerFv(down_4) != 0U))
    {
      if (rec_3[1] != 0)
      {
        set_field_1c__10TObjPlayerFl(down_4, (s32) rec_3[1]);
        rec_3 = (u32 *) (((s8 *) rec_3) + 8);
      }
    }
    down_4 = *((void **) (((s8 *) down_4) + 0xC));
  }

  TObjPlayer__sub_801D4678(obj, 1);
  return 1;
}
