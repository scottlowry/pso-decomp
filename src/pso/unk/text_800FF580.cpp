#include "types.h"
#include "pso/system/vector.h"
#include "pso/TObjEZRopeBase.h"
#include "pso/misc/TQuestVmDownLoadServer.h"
struct Vec_800FF8CC {
    f32 x, y, z;
};

struct Src_800FF8CC {
    s8 count;
    u8 pad[3];
    Vec_800FF8CC rot;
    u8 pad2[8];
};

struct Pos_800FF8CC {
    u32 f0;
    Vec_800FF8CC v;
};

struct Self_800FF8CC {
    u8 pad[0x1C];
    s32 num;
    Src_800FF8CC *src;
    Pos_800FF8CC *pos;
    s32 arg;
    Vec_800FF8CC *out;
};

struct Vec_800FF8CC;
struct Vec_800FF788 { f32 x, y, z; };

struct Seg_800FF788 { s8 n; u8 pad1[3]; Vec_800FF788 dir; u8 pad10[8]; };

struct Src_800FF788 { s32 a; Vec_800FF788 v; };

struct Obj_800FF788 {
    u8 pad0[0x20];
    Seg_800FF788 *segs;
    Src_800FF788 *srcs;
    u32 flag;
    Vec_800FF788 *out;
};

struct Node_800FF580 {
    f32 f0;
    Vec_800FF8CC pos;
};

extern "C" {
void vec3_add_to(Vec_800FF8CC *, Vec_800FF8CC *);
void fn_800FF580(void *, void *, f32);
f32 vector_length(void *);
void subtract_vector(void *, void *);
void normalize_vector(void *);
f32 xyz_distance(void *, void *);
extern const f32 lbl_805DAA58;
extern const f32 lbl_805DAA5C;
extern const f32 lbl_805DAA64;

void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt_arg;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base;
    f32 zero;
    f32 best;
    f32 best_thr;
    f32 thr;
    f32 dist;
    f32 margin;
    s32 iters;
    lw[0] = pw[0];
    lw[1] = pw[1];
    lw[2] = pw[2];
    iters = 16;
    base = lbl_805DAA64 * arg3;
    zero = lbl_805DAA58;
    for (;;) {
        best = lbl_805DAA58;
        node = (Node_800FF580 *)((TObjEZRopeBase *)obj_arg)->m_28;
        while (node->f0 >= zero) {
            thr = base + node->f0;
            dist = xyz_distance(&local, &node->pos);
            if (dist < thr) {
                margin = thr - dist;
                if (margin > best) {
                    best = margin;
                    best_thr = thr;
                    VecCopy((Vec *)&npos, (const Vec *)&node->pos);
                }
            }
            node++;
        }
        if (!(iters > 0 && zero != best)) {
            VecCopy((Vec *)pt, (const Vec *)&local);
            return;
        }
        subtract_vector(&local, &npos);
        if (zero == vector_length(&local)) {
            local.x = zero;
            local.y = lbl_805DAA5C;
            local.z = zero;
        } else {
            normalize_vector(&local);
        }
        local.x *= best_thr;
        local.y *= best_thr;
        local.z *= best_thr;
        vec3_add_to(&local, &npos);
        subtract_vector(&local, pt - 1);
        if (zero == vector_length(&local)) {
            local.x = zero;
            local.y = lbl_805DAA5C;
            local.z = zero;
        } else {
            normalize_vector(&local);
        }
        local.x *= arg3;
        local.y *= arg3;
        local.z *= arg3;
        vec3_add_to(&local, pt - 1);
        iters--;
    }
}

void TObjEZRopeBase::sub_800FF788(void *mtx) {
    Seg_800FF788 *seg;
    Src_800FF788 *src;
    Vec_800FF788 *p;
    s32 n;
    f32 zero;
    f32 len;
    zero = lbl_805DAA58;
    seg = ((Obj_800FF788 *)this)->segs;
    src = ((Obj_800FF788 *)this)->srcs;
    p = ((Obj_800FF788 *)this)->out;
    while (seg->n >= 2) {
        len = vector_length(&seg->dir);
        VecCopy((Vec *)((Vec_800FF8CC *)p), (const Vec *)((Vec_800FF8CC *)&src->v));
        p++;
        n = seg->n - 1;
        while (n > 0) {
            vec3_add_to((Vec_800FF8CC *)p, (Vec_800FF8CC *)mtx);
            subtract_vector(p, p - 1);
            if (zero == vector_length(p)) {
                p->x = zero;
                p->y = lbl_805DAA5C;
                p->z = zero;
            } else {
                normalize_vector(p);
            }
            p->x *= len;
            p->y *= len;
            p->z *= len;
            vec3_add_to((Vec_800FF8CC *)p, (Vec_800FF8CC *)(p - 1));
            if (((Obj_800FF788 *)this)->flag != 0) {
                fn_800FF580(((Obj_800FF788 *)this), p, len);
            }
            n--;
            p++;
        }
        seg++;
        src++;
    }
}

void TObjEZRopeBase::sub_800FF8CC(void *src_arg, void *pos_arg, s32 arg) {
    Src_800FF8CC *src = (Src_800FF8CC *)src_arg;
    Pos_800FF8CC *pos = (Pos_800FF8CC *)pos_arg;
    s32 total;
    Src_800FF8CC *s;
    Pos_800FF8CC *p;
    Vec_800FF8CC *out;
    s32 n;
    total = 0;
    ((Self_800FF8CC *)this)->src = src;
    ((Self_800FF8CC *)this)->pos = pos;
    ((Self_800FF8CC *)this)->arg = arg;
    ((Self_800FF8CC *)this)->num = 0;
    for (s = src; s->count >= 2; s++) {
        total += s->count;
        ((Self_800FF8CC *)this)->num++;
    }
    ((Self_800FF8CC *)this)->out = (Vec_800FF8CC *)TQuestVmDownLoadServer::alloc(total * 0xC);
    s = ((Self_800FF8CC *)this)->src;
    p = ((Self_800FF8CC *)this)->pos;
    out = ((Self_800FF8CC *)this)->out;
    for (; s->count >= 2; s++, p++) {
        Vec_800FF8CC v = p->v;
        for (n = s->count; n > 0; n--, out++) {
            VecCopy((Vec *)out, (const Vec *)&v);
            vec3_add_to(&v, &s->rot);
        }
    }
}

}
