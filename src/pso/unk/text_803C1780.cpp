#include "types.h"
#include "pso/unk/text_803C1780.h"
#include "pso/misc/TLobby.h"

typedef void (*RecoveredCallback_1268626c296b)(void *);
struct Obj_803C1A24 { u8 pad[0xAC]; void *fac; };

extern RecoveredCallback_1268626c296b lbl_805D7514;
extern s32 (*lbl_805D7510)();

extern "C" {
int memcmp(const void *, const void *, unsigned long);
extern void *lbl_805D4650;
extern void *lbl_805D4654;
}

s32 TLobby__sub_803C1780(u8 *arg0, s32 arg1, s16 *arg2, u8 *arg3, u8 *arg4,
                         u8 *arg5, u8 *arg6, u8 *arg7, s32 *arg8, s32 *arg9,
                         s16 *arg10) {
    s32 i;
    for (i = 0; i < arg1; i++) {
        if (memcmp(arg0 + i, lbl_805D4650, 4) == 0) {
            break;
        }
    }
    if (i == arg1) {
        return -1;
    }
    if ((i % 4) != 0) {
        return -1;
    }
    u8 *hdr = arg0 + i;
    u16 tv = *(const u16 *)(hdr + 8);
    if ((s16)((tv >> 8) | ((tv & 0xFF) << 8)) > 1) {
        return -1;
    }
    for (i = 0; i < arg1; i++) {
        if (memcmp(arg0 + i, lbl_805D4654, 4) == 0) {
            break;
        }
    }
    if (i == arg1) {
        return -1;
    }
    u32 v = *(const u32 *)(arg0 + i + 4);
    s32 x = (s32)(((v >> 24) & 0xFF) | ((v >> 8) & 0xFF00) | ((v << 8) & 0xFF0000) |
                  ((v << 24) & 0xFF000000));
    *arg2 = (s16)(i + 8);
    *arg3 = -1;
    u32 w = *(const u32 *)(hdr + 0xc);
    *(u32 *)(arg7 + x) = ((w >> 24) & 0xFF) | ((w >> 8) & 0xFF00) |
                         ((w << 8) & 0xFF0000) | ((w << 24) & 0xFF000000);
    u16 t6 = *(const u16 *)(hdr + 0xa);
    *arg6 = (u8)((t6 >> 8) | ((t6 & 0xFF) << 8));
    u16 t4 = *(const u16 *)(hdr + 0x16);
    *arg4 = (u8)((t4 >> 8) | ((t4 & 0xFF) << 8));
    u16 t5 = *(const u16 *)(hdr + 0x14);
    *arg5 = (u8)((t5 >> 8) | ((t5 & 0xFF) << 8));
    *arg8 = x / (s8)*arg5;
    *arg9 = 1;
    if ((s8)*arg4 == 16) {
        *arg10 = 0;
    } else if ((s8)*arg4 == 8) {
        *arg10 = 1;
    } else if ((s8)*arg4 == 4) {
        *arg5 = (u8)((s8)*arg6 * 2);
        *arg9 = 4;
        *arg8 = (x / 2) / (s8)*arg6;
        *arg4 = 16;
        *arg10 = 2;
    }
    if ((s8)*arg4 == 0) {
        return -1;
    }
    if ((s8)*arg5 == 0) {
        return -1;
    }
    if ((s8)*arg6 <= 0) {
        return -1;
    }
    if ((s8)*arg6 > 2) {
        return -1;
    }
    return (*(u32 *)arg7 == 0) ? -1 : 0;
}

void TLobby__sub_803C19D8(void) {
    lbl_805D7510();
}
void TLobby__sub_803C1A00(u8 *arg0, s32 arg1) {
    *(s32 *)((s8 *)arg0 + 0xB0) = arg1;
    *(u32 *)((s8 *)arg0 + 0xB4) = (u32) (arg1 / 96);
}
void TLobby::invoke_notify_callback() {
    Obj_803C1A24 *arg0 = (Obj_803C1A24 *)this;
    if (arg0->fac != 0) {
        lbl_805D7514(arg0->fac);
    }
}
