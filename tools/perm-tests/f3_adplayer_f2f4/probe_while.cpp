// rosetta probe: self-contained v3b while-form body of TAdPlayerLoadGC__sub_803F2F1C
// (card-adplayer-f2f4 visit-3) — {r27<->r28} ring fingerprint across GC versions.
typedef signed int s32;
typedef unsigned char u8;
typedef unsigned int u32;

struct CardInfo_803F31D8 { s32 state; s32 f4; u32 sector_size; };
typedef struct Slot_803F3478 {
    s32 f0;
    char name[0x20];
    char name2[0x20];
    s32 f44;
    s32 f48;
    s32 f4C;
    s32 f50;
    s32 f54;
    s32 f58;
    s32 f5C;
    s32 f60;
    u8 f64;
    u8 pad65[3];
} Slot_803F3478;
typedef Slot_803F3478 Slot_803F1CC4, Slot_803F1E90, Slot_803F2058;

class TAdPlayerLoadGC {
public:
    static s32 update_card_rename(s32);
    static s32 update_card_delete(s32);
    static s32 step_set_attributes(s32);
};

extern "C" {
extern s32 lbl_805D7940;
extern u8 lbl_805D7944;
extern void (*lbl_805D7948)(s32, s32, s32);
extern void (*lbl_805D794C)(s32, s32, s32);
u8 lbl_805A28C0[0x20];
s32 memset(void *, int, int);
s32 CARDProbeEx(s32, s32 *, s32 *);
s32 OSDisableInterrupts(void);
void OSRestoreInterrupts(s32);
s32 TAdPlayerLoadGC__sub_803F1908(s32);
s32 TAdPlayerLoadGC__sub_803F2240(s32);
s32 TAdPlayerLoadGC__sub_803F2610(s32);
s32 TAdPlayerLoadGC__sub_803F282C(s32);
s32 TAdPlayerLoadGC__sub_803F2A4C(s32);
s32 TAdPlayerLoadGC__sub_803F2D20(s32);

#pragma push
#pragma opt_propagation off
s32 TAdPlayerLoadGC__sub_803F2F1C(void) {
    u8 *base;
    s32 off2;
    u8 *p;
    CardInfo_803F31D8 *ci;
    s32 *py;
    s32 *px;
        s32 stv;
    s32 memCardSize;
    s32 errorBits;
    s32 stat;
    s32 level;
    s32 card_channel;
    s32 off;

    base = lbl_805A28C0;
    if (lbl_805D7940 < 1) {
        return -1;
    }
    if (lbl_805D7944 != 0) {
        return 0;
    }
    lbl_805D7944++;
    card_channel = 0;
    off = 0;
    while (card_channel < 2) {
        stat = CARDProbeEx(card_channel, &memCardSize, &errorBits);
        switch (stat) {
        case -128:
        default:
            p = base + off;
            p = p + 0x3610;
            if (stat != *(s32 *)p) {
                *(s32 *)p = stat;
                *(s32 *)(p + 4) = 0;
                *(s32 *)(p + 8) = 0;
            }
            break;
        case -3:
            p = base + off;
            p = p + 0x3610;
            if (stat != *(s32 *)p) {
                if (*(s32 *)p == 0) {
                    memCardSize = *(s32 *)(p + 4);
                    errorBits = *(s32 *)(p + 8);
                    *(s32 *)p = stat;
                    *(s32 *)(p + 4) = 0;
                    *(s32 *)(p + 8) = 0;
                    if (lbl_805D794C != 0) {
                        level = OSDisableInterrupts();
                        lbl_805D794C(card_channel, memCardSize, errorBits);
                        OSRestoreInterrupts(level);
                    }
                }
                *(s32 *)p = stat;
                *(s32 *)(p + 4) = 0;
                *(s32 *)(p + 8) = 0;
            }
            break;
        case -2:
            p = base + off;
            p = p + 0x3610;
            if (stat != *(s32 *)p) {
                *(s32 *)p = stat;
                *(s32 *)(p + 4) = 0;
                *(s32 *)(p + 8) = 0;
            }
            break;
        case -1:
            break;
        case 0:
            p = base + off;
            p = p + 0x3610;
            ci = (CardInfo_803F31D8 *)p;
            if (stat != ci->state) {
                ci->state = stat;
                py = (s32 *)(p + 8);
                px = (s32 *)(p + 4);
                ci->f4 = memCardSize;
                ci->sector_size = errorBits;
                if (lbl_805D7948 != 0) {
                    level = OSDisableInterrupts();
                    lbl_805D7948(card_channel, *px, *py);
                    OSRestoreInterrupts(level);
                }
            }
            break;
        }
        card_channel++;
        off += 0xC;
    }
    card_channel = 0;
    off2 = 0;
    while (card_channel < 2) {
        p = base + off2;
        stv = *(s32 *)(p + 0x64);
        p = p + 0x20;
        switch (stv) {
        case 0:
            break;
        case 1:
            TAdPlayerLoadGC__sub_803F2D20(card_channel);
            break;
        case 2:
            TAdPlayerLoadGC__sub_803F2A4C(((Slot_803F3478 *)p)->f54);
            break;
        case 3:
            TAdPlayerLoadGC__sub_803F282C(((Slot_803F3478 *)p)->f54);
            break;
        case 5:
            TAdPlayerLoadGC__sub_803F2240(((Slot_803F3478 *)p)->f54);
            break;
        case 4:
            TAdPlayerLoadGC__sub_803F2610(((Slot_803F3478 *)p)->f54);
            break;
        case 6:
            TAdPlayerLoadGC::update_card_rename(card_channel);
            break;
        case 7:
            TAdPlayerLoadGC::update_card_delete(card_channel);
            break;
        case 8:
            TAdPlayerLoadGC::step_set_attributes(card_channel);
            break;
        case 9:
            TAdPlayerLoadGC__sub_803F1908(card_channel);
            break;
        }
        card_channel++;
        off2 += 0x68;
    }
    lbl_805D7944--;
    return 0;
}
#pragma pop
}
