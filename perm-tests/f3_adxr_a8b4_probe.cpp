// f3_adxr_a8b4 rosetta probe: self-contained TU, era body transcribe, version sweep
typedef signed char s8;
typedef unsigned char u8;
typedef signed short s16;
typedef unsigned short u16;
typedef signed int s32;
typedef unsigned int u32;

struct Strm;
struct StrmVt {
    void *pad[6];
    void (*read)(Strm *, s32, s32, void *);
    void (*release)(Strm *, s32, void *);
    void (*submit)(Strm *, s32, void *);
    s32 (*avail)(Strm *, s32);
};
struct Strm { StrmVt *vt; };
struct Pair { u32 a, b; };
struct Lsc;
struct Ab {
    u8 f0;
    s8 state;
    u8 f2;
    s8 n;
    s32 f4;
    void *f8;
    s32 fc;
    u8 pad10[8];
    Strm *f18[8];
    s32 f38;
    s16 f3c;
    s16 f3e;
    s16 f40;
    s16 f42;
    s16 f44;
    s16 pad46;
    s32 f48;
    s32 pad4c;
    s32 f50;
    u8 pad54[0xC];
    s16 f60;
    u8 pad62[0xE];
    s8 f70;
    u8 f71;
    s8 f72;
    u8 pad73[0x21];
    void *f94;
    s8 f98;
    u8 pad99[3];
    s32 f9c;
    s32 fa0;
};
struct Sb { u8 x; s8 f1; u8 pad[0x100]; };

extern "C" {
s32 query_available_size__6TLobbyFv(int);
s32 send_with_offset4__6TLobbyFv(int);
s32 TLobby__sub_803CC030(int, int);
s32 dispatch_packet__6TLobbyFv(int, int);
s32 notify_field_4_alt__6TLobbyFv(int);
s32 TLobby__sub_803C07E8(int);
s32 TLobby__sub_803CBFF0(int);
s32 TLobby__sub_803C9740(u8 *);
s32 TLobby__sub_803C8B2C(u8 *);
void TLobby__sub_803CAB38(Sb *);
s32 lsc_get_state(Lsc *);
s32 memset(void *, int, int);
extern s32 lbl_805D7540;
extern s32 lbl_805D7578;
extern s32 lbl_805D757C;
extern s32 lbl_805D7580;
}

void TLobby__sub_803CA8B4(Ab *arg0) {
    s32 TLobby__sub_803C8B2C(u8 *);
    if (arg0->state == 3) {
        if (TLobby__sub_803C07E8(arg0->f4) == 3) {
            s32 n = send_with_offset4__6TLobbyFv(arg0->f4), i;
            lbl_805D7580 = n;
            for (i = 0; i < n; i++) {
                s32 v = arg0->f18[i]->vt->avail(arg0->f18[i], 1);
                lbl_805D757C = v;
                if (v >= 0x40) {
                    break;
                }
            }
            if (i == n) {
                dispatch_packet__6TLobbyFv(arg0->fc, 0);
                arg0->state = 4;
            }
        }
    } else if (arg0->state == 1) {
        TLobby__sub_803CAB38((Sb *)arg0);
    } else if (arg0->state == 2) {
        s32 fcv = arg0->fc;
        s32 f4v = arg0->f4;
        s32 avail = query_available_size__6TLobbyFv(fcv);
        s32 pos = TLobby__sub_803CBFF0(fcv);
        if (avail >= arg0->f48 * 2 || pos <= notify_field_4_alt__6TLobbyFv(f4v) ||
            TLobby__sub_803C07E8(arg0->f4) == 3) {
            if (arg0->f70 == 0) {
                if (arg0->f72 == 0) {
                    TLobby__sub_803CC030(fcv, 1);
                    arg0->f9c = 0;
                    arg0->fa0 = lbl_805D7540;
                }
                arg0->state = 3;
            }
            arg0->f71 = 1;
        }
        if (TLobby__sub_803C07E8(arg0->f4) == 3) {
            s32 cnt = TLobby__sub_803C9740((u8 *)arg0), size;
            size = arg0->f48 * cnt * 2;
            for (s32 i = 0; i < cnt; i++) {
                Pair pr;
                Strm *e = arg0->f18[i];
                e->vt->read(e, 0, size, &pr);
                memset((void *)pr.a, 0, pr.b);
                e->vt->submit(e, 1, &pr);
            }
        }
    } else if (arg0->state == 4) {
        lbl_805D7578 = query_available_size__6TLobbyFv(arg0->fc);
        if (query_available_size__6TLobbyFv(arg0->fc) <= 0) {
            TLobby__sub_803CC030(arg0->fc, 0);
            arg0->state = 5;
        }
    }
    if (arg0->f8 != 0) {
        if (TLobby__sub_803C8B2C((u8 *)arg0->f8) == 4) {
            arg0->f60 = -1;
            arg0->state = 6;
        }
    }
    if (arg0->f94 != 0) {
        if (lsc_get_state((Lsc *)arg0->f94) == 3) {
            arg0->f60 = -1;
            arg0->state = 6;
        }
    }
}
