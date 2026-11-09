#include "types.h"
#include "pso/unk/text_801E283C.h"
#include "pso/system/date.h"

struct Date_801E21A8 { u16 year; u8 mon; u8 mday; u8 hour; u8 min; u8 sec; u8 pad; u8 pad8[4]; };
struct Tbl_801E283C { s32 v[12]; };
extern "C" u8 fill_date_from_seconds(u32 seconds, Date_801E21A8 *out);
extern const Tbl_801E283C lbl_80449700[];

#pragma inline_depth(1)
#pragma auto_inline off
#pragma dont_inline off

#pragma push
#pragma opt_propagation off

static inline int inline_fn(u32 arg0, s32 arg1, s32 arg2)
{
  return (arg0 / arg1) * arg2;
}

u8 fill_date_from_seconds(u32 seconds, Date_801E21A8 *out)
{
  unsigned int new_var;
  int new_var3;
  s32 tbl[12];
  Date_801E21A8 *new_var2;
  s32 sixty;
  *((Tbl_801E283C *) tbl) = lbl_80449700[0];
  sixty = 60;
  u32 minutes = seconds / sixty;
  u32 hours = seconds / 3600;
  u32 days = seconds / 86400;
  u32 years = seconds / 31536000;
  out->sec = seconds - (minutes * sixty);
  new_var = (hours / 24) * 24;
  u32 leapc = (years + 1) >> 2;
  out->min = minutes - inline_fn(minutes, sixty, sixty);
  new_var3 = days / 365;
  out->hour = hours - new_var;
  u32 yrs_365 = new_var3;
  u32 rem = days - (yrs_365 * 365);
  u32 doy;
  if (leapc <= rem)
  {
    out->year = years + 2000;
    doy = rem - leapc;
  }
  else
  {
    doy = rem + (365 - leapc);
    out->year = years + 1999;
    if ((out->year % 4) == 0)
    {
      doy += 1;
    }
  }
  u32 month = 1;
  if ((out->year % 4) == 0)
  {
    if (doy >= ((u32) tbl[1]))
    {
      for (month = 2; month < 12; month++)
      {
        new_var = (u32) tbl[month];
        if (doy < (new_var + 1))
        {
          break;
        }
      }

    }
  }
  else
  {
    for (month = 1; month < 12; month++)
    {
      if (doy < ((u32) tbl[month]))
      {
        break;
      }
    }

  }
  u32 prev = (u32) tbl[month - 1];
  out->mon = (u8) month;
  new_var2 = out;
  out->mday = (u8) ((doy - prev) + 1);
  if ((out->year % 4) == 0)
  {
    if (out->mon > 2)
    {
      if (years || tbl)
      {
        out->mday = out->mday - 1;
      }
      else
      {
        out->mday = out->mday - 1;
      }
    }
  }
  out->pad = calc_day_of_week(out->year, out->mon, out->mday);
  out->pad8[0] = calc_day_in_cycle((s32 *) new_var2);
}

#pragma pop

u8 calc_day_in_cycle(s32 *date) {
    u32 sp8;
    u32 var_r4;
    DateToSeconds((DateStamp *)date, (int *)&sp8);
    if (sp8 >= 0x5CB417D1U) {
        var_r4 = sp8 - 0x5CB417D1U;
        var_r4 = var_r4 % 0x26EE7FU;
    } else {
        var_r4 = 0x5CB417D1U - sp8;
        var_r4 = var_r4 % 0x26EE7FU;
        var_r4 = 0x26EE7FU - var_r4;
    }
    return (u8) (var_r4 / 86400U);
}

u8 calc_day_of_week(u16 year, u8 month, u8 day) {
    if (month <= 2) {
        year--;
        month += 12;
    }
    return (year + (year >> 2) - 15 + (13 * month + 8) / 5 + day) % 7;
}
