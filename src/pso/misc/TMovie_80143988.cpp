#include "types.h"

extern "C" {

extern void *movie_current_frame_buffer;
extern u32 lbl_805D56A4;
extern u32 lbl_805D56A8;


void pack_movie_frame(u32 *hdr) {
    u32 w = lbl_805D56A4;
    u32 h = lbl_805D56A8;
    u32 *p = (u32 *)hdr[0];
    u32 m0 = 0x280 - w;
    u32 mh = 0x1E0 - h;
    u32 *a = (u32 *)hdr[1];
    u32 m1 = mh * 0x280;
    u32 *b = (u32 *)hdr[2];
    u8 *db = (u8 *)movie_current_frame_buffer;
    m0 = m0 & 0x7FFFFFFC;
    u32 xlen = hdr[4];
    u32 wh1 = w >> 1;
    u32 xs = hdr[3];
    db = db + m0;
    u32 wq = m1 >> 2;
    u32 s5h = 0x280 - wh1;
    db = db + wq;
    u32 wq3 = w >> 3;
    u32 xw = xs >> 2;
    u32 wq2 = w >> 2;
    u32 s3h = (xlen >> 2) - wq3;
    u32 sh1 = (xs >> 1) & 0x3FFFFFFE;
    u32 s4h = wq2 - sh1;
    u32 *d2 = (u32 *)(db + 0x4FC);
    u32 plimm = h * 0x500;
    p = p - 1;
    d2 = d2 - 1;
    u32 *d = (u32 *)(db - 4);
    u32 *x = p + xw;
    x = x - 1;
    a = a - 1;
    u32 *plim = (u32 *)(db + plimm - 4);
    b = b - 1;
    u32 in6 = (w << 1) & 0x7FFFFFFC;
    u32 s5 = s5h << 2;
    u32 s4 = s4h << 2;
    u32 s3 = s3h << 2;

    while ((u32)d < (u32)plim) {
        u32 *stop = (u32 *)((u8 *)d + in6);
        while ((u32)d < (u32)stop) {
            __dcbt(0, (s32)p);
            u32 a1 = a[1];
            u32 b1 = b[1];
            u32 p1 = p[1];
            u32 x1 = x[1];
            u32 u = ((a1 >> 8) & 0xFF00) | ((b1 << 8) & 0xFF000000) | (p1 & 0xFF000000) |
                    ((p1 & 0xFF) << 8);
            d[1] = u;
            d2[1] = (u & 0x00FF00FF) | (x1 & 0xFF000000) | ((x1 & 0xFF) << 8);
            u32 p2 = p[2];
            u32 x2 = x[2];
            x = x + 2;
            u = (a1 & 0xFF00) | ((b1 << 16) & 0xFF) | ((p2 >> 16) & 0xFF000000) | ((p2 >> 8) & 0xFF00);
            d[2] = u;
            d2[2] = (u & 0x00FF00FF) | ((x2 >> 16) & 0xFF000000) | ((x2 >> 8) & 0xFF00);
            u = ((a1 >> 8) & 0xFF00) | ((b1 >> 16) & 0xFF) | (p2 & 0xFF000000) | ((p2 & 0xFF) << 8);
            d[3] = u;
            d2[3] = (u & 0x00FF00FF) | (x2 & 0xFF000000) | ((x2 & 0xFF) << 8);
            u = ((a1 & 0xFFFFFF00) << 16) | (b1 & 0xFF) | ((p2 >> 16) & 0xFF000000) | ((p2 >> 8) & 0xFF00);
            d[4] = u;
            d2[4] = (u & 0x00FF00FF) | ((x2 >> 16) & 0xFF000000) | ((x2 >> 8) & 0xFF00);
            __dcbt(0, (s32)x);
            u32 a2 = a[2];
            a = a + 2;
            u32 b2 = b[2];
            b = b + 2;
            u32 p3 = p[3];
            u32 x3 = x[1];
            u32 v = ((a2 >> 8) & 0xFF00) | ((b2 << 8) & 0xFF000000) | (p3 & 0xFF000000) |
                    ((p3 & 0xFF) << 8);
            d[5] = v;
            d2[5] = (v & 0x00FF00FF) | (x3 & 0xFF000000) | ((x3 & 0xFF) << 8);
            u32 p4 = p[4];
            u32 x4 = x[2];
            x = x + 2;
            v = (a2 & 0xFF00) | ((b2 << 16) & 0xFF) | ((p4 >> 16) & 0xFF000000) | ((p4 >> 8) & 0xFF00);
            d[6] = v;
            d2[6] = (v & 0x00FF00FF) | ((x4 >> 16) & 0xFF000000) | ((x4 >> 8) & 0xFF00);
            v = ((a2 >> 8) & 0xFF00) | ((b2 >> 16) & 0xFF) | (p4 & 0xFF000000) | ((p4 & 0xFF) << 8);
            d[7] = v;
            d2[7] = (v & 0x00FF00FF) | (x4 & 0xFF000000) | ((x4 & 0xFF) << 8);
            v = ((a2 & 0xFFFFFF00) << 16) | (b2 & 0xFF) | ((p4 >> 16) & 0xFF000000) | ((p4 >> 8) & 0xFF00);
            d[8] = v;
            d2[8] = (v & 0x00FF00FF) | ((x4 >> 16) & 0xFF000000) | ((x4 >> 8) & 0xFF00);
            d = d + 8;
            d2 = d2 + 8;
        }
        d = (u32 *)((u8 *)d + s5);
        d2 = (u32 *)((u8 *)d2 + s5);
        p = (u32 *)((u8 *)p + s4);
        x = (u32 *)((u8 *)x + s4);
        a = (u32 *)((u8 *)a + s3);
        b = (u32 *)((u8 *)b + s3);
    }
}

}
