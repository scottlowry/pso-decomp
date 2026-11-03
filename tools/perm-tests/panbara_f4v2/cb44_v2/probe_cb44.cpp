// shape probe for CB44 residual classes: p-merge into trip-counter home + (s16)test clamp form
typedef unsigned char u8;
typedef unsigned int u32;
typedef unsigned short u16;
typedef signed int s32;
typedef signed short s16;
#define NULL 0

typedef struct NetPacket { u8 x[0x20]; } NetPacket;

s32 ext_cfe8(u8 type, u8 code, u32 src, u32 dst, NetPacket *pkt);
void *NetMemcpy(void *d, const void *s, u32 n);
NetPacket *alloc_entry(void);
void release_entry(NetPacket *p);

s32 probe_cb44(u8 *arg0, u32 arg1, u32 arg2) {
    s32 refbox[3];
    u8 hdr[8];
    u8 *p;
    NetPacket *pkt;
    s32 r;
    u32 i;

    p = arg0 + 0x18;
    (void)refbox;
    (void)hdr;
    if (*(s32 *)(p - 0x14) != 0) {
        return -1;
    }
    switch (arg1 & 0xff) {
    case 8:
        pkt = alloc_entry();
        if (pkt == NULL) {
            return -0x101;
        }
        i = 0;
        pkt->x[4] = arg0[4];
        for (; i < 3; i++) {
            pkt->x[0xc + i * 2] = p[i];
            NetMemcpy(&pkt->x[0x10 + i * 2], p + 4, 8);
        }
        r = ext_cfe8(0, 0, arg2, arg1, pkt);
        if ((s16)r < 0) {
            release_entry(pkt);
            return r;
        }
        release_entry(pkt);
        return 0;
    default:
        return (s32)(p[0]);
    }
}
