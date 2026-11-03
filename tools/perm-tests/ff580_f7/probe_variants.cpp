#include "types.h"
#include "pso/system/vector.h"
#include "pso/TObjEZRopeBase.h"
#include "pso/misc/TQuestVmDownLoadServer.h"

struct Vec_800FF8CC {
    f32 x, y, z;
};

struct Node_800FF580 {
    f32 f0;
    Vec_800FF8CC pos;
};

extern "C" {
void vec3_add_to(Vec_800FF8CC *, Vec_800FF8CC *);
f32 vector_length(void *);
void subtract_vector(void *, void *);
void normalize_vector(void *);
f32 xyz_distance(void *, void *);
extern const f32 lbl_805DAA58;
extern const f32 lbl_805DAA5C;
extern const f32 lbl_805DAA64;

#ifndef VFORM
#define VFORM 0
#endif

#if VFORM == 0
// current committed state
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt_arg;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
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
        if (iters > 0 && zero != best) {
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
        } else {
            VecCopy((Vec *)pt, (const Vec *)&local);
            return;
        }
    }
}
#elif VFORM == 1
// top-order: iters/base/zero first; pw derived from pt
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
    s32 iters;
    iters = 16;
    base = lbl_805DAA64 * arg3;
    zero = lbl_805DAA58;
    lw[0] = pw[0];
    lw[1] = pw[1];
    lw[2] = pw[2];
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
        if (iters > 0 && zero != best) {
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
        } else {
            VecCopy((Vec *)pt, (const Vec *)&local);
            return;
        }
    }
}
#elif VFORM == 2
// guard V2: negated compound, else-returns, process falls through, loop back via continue? use for(;;) with early return body
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt_arg;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
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
#elif VFORM == 3
// guard V3: DeMorgan spelled ||, else form
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt_arg;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
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
        if (iters <= 0 || zero == best) {
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

#elif VFORM == 4
// guard V2: negated compound, else-returns, process falls through, loop back via continue? use for(;;) with early return body
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
    s32 iters;
    iters = 16;
    base = lbl_805DAA64 * arg3;
    zero = lbl_805DAA58;
    lw[0] = pw[0];
    lw[1] = pw[1];
    lw[2] = pw[2];
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
#elif VFORM == 5
// guard V2: negated compound, else-returns, process falls through, loop back via continue? use for(;;) with early return body
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    u32 *pw = (u32 *)pt;
    u32 *lw = (u32 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
    s32 iters;
    iters = 16;
    base = lbl_805DAA64 * arg3;
    zero = lbl_805DAA58;
    lw[0] = pw[0];
    lw[1] = pw[1];
    lw[2] = pw[2];
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
        if (iters <= 0 || zero == best) {
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
#elif VFORM == 6
// guard V2: negated compound, else-returns, process falls through, loop back via continue? use for(;;) with early return body
void fn_800FF580(void *obj_arg, void *pt_arg, f32 arg3) {
    Vec_800FF8CC *pt = (Vec_800FF8CC *)pt_arg;
    Vec_800FF8CC local;
    struct IV6 { u32 v[3]; };
    IV6 *pi = (IV6 *)pt;
    IV6 *li = (IV6 *)&local;
    Vec_800FF8CC npos;
    Node_800FF580 *node;
    f32 base, zero, best, best_thr, thr, dist, margin;
    s32 iters;
    li->v[0] = pi->v[0];
    li->v[1] = pi->v[1];
    li->v[2] = pi->v[2];
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
#endif
}
