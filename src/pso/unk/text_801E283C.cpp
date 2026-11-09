#include "types.h"
#include "pso/unk/text_801E283C.h"
#include "pso/system/date.h"

struct Date_801E21A8 {
    u16 year;
    u8 mon;
    u8 mday;
    u8 hour;
    u8 min;
    u8 sec;
    u8 pad;
    u8 pad8[4];
};

extern "C" u8 fill_date_from_seconds(u32 seconds, Date_801E21A8 *date);
extern const s32 lbl_80449700[12];

extern "C" u8 fill_date_from_seconds(u32 seconds, Date_801E21A8 *date) {
    s32 daysBeforeMonth[12];
    s32 n;
    const s32 *src = lbl_80449700 - 1;
    s32 *dst = daysBeforeMonth - 1;

    for (n = 0; n < 6; n++) {
        dst[1] = src[1];
        dst[2] = src[2];
        dst += 2;
        src += 2;
    }

    u32 minutes = seconds / 60;
    u32 totalDays = seconds / 86400;
    u32 years4 = seconds / 31536000;
    u32 totalHours = seconds / 3600;
    u32 leapDays = (years4 + 1) / 4;
    u32 hoursFromMin = minutes / 60;

    date->sec = seconds % 60;
    u32 yearsInDays = totalDays / 365;
    date->min = minutes % 60;
    u32 dayInYear = totalDays % 365;
    date->hour = totalHours % 24;

    s32 dayOfYear;
    if (leapDays > dayInYear) {
        date->year = years4 + 1999;
        dayOfYear = dayInYear + (365 - leapDays);
        if (date->year % 4 == 0) {
            dayOfYear++;
        }
    } else {
        date->year = years4 + 2000;
        dayOfYear = dayInYear - leapDays;
    }

    s32 month;
    if (date->year % 4 == 0) {
        month = 1;
        if (dayOfYear >= daysBeforeMonth[1]) {
            for (month = 2; month < 12; month++) {
                if (dayOfYear < daysBeforeMonth[month] + 1) {
                    break;
                }
            }
        }
    } else {
        for (month = 1; month < 12; month++) {
            if (dayOfYear < daysBeforeMonth[month]) {
                break;
            }
        }
    }

    date->mon = month;
    date->mday = dayOfYear - daysBeforeMonth[month - 1] + 1;
    if (date->year % 4 == 0 && date->mon > 2) {
        date->mday--;
    }

    date->pad = calc_day_of_week(date->year, date->mon, date->mday);
    u8 dayInCycle = calc_day_in_cycle((s32 *)date);
    date->pad8[0] = dayInCycle;
    return dayInCycle;
}

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
