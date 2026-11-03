#include "types.h"

struct Hdr_803E34B0 { u8 *dst; u8 *src; s32 count; };

typedef struct Vtx_803E36C4 { f32 x, y, z, nx, ny, nz; u32 pad[2]; } Vtx_803E36C4;

struct SrcVtx_803E3390 { f32 x, y, z, nx, ny, nz; };

extern "C" void transform_chunk_vertices_pos_normal(Hdr_803E34B0 *job, s32 matrix) {
    f32 (*m)[3] = (f32 (*)[3])matrix;
    SrcVtx_803E3390 *src = (SrcVtx_803E3390 *)job->src;
    Vtx_803E36C4 *dst = (Vtx_803E36C4 *)job->dst;
    s32 n = job->count;
    while (n-- > 0) {
        f32 vx = src->x;
        f32 vy = src->y;
        f32 vz = src->z;
        f32 ax = src->nx;
        f32 ay = src->ny;
        f32 az = src->nz;
        dst->x = m[3][0] + vx * m[0][0] + vy * m[1][0] + vz * m[2][0];
        dst->y = m[3][1] + vx * m[0][1] + vy * m[1][1] + vz * m[2][1];
        dst->z = m[3][2] + vx * m[0][2] + vy * m[1][2] + vz * m[2][2];
        dst->nx = ax * m[0][0] + ay * m[1][0] + az * m[2][0];
        dst->ny = ax * m[0][1] + ay * m[1][1] + az * m[2][1];
        dst->nz = ax * m[0][2] + ay * m[1][2] + az * m[2][2];
        src++;
        dst++;
    }
}
