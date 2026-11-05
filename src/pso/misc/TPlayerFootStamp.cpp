#include "pso/TPlayerFootStamp.h"

TPlayerFootStamp::~TPlayerFootStamp() {}

#include "types.h"
#include "pso/system/vector.h"
#include "pso/ui/TAdSinglePlyChrSelectGC.h"

struct FS_802AF9C0 {
    u32 m_00;
    u8 pad04[0x14];
    void *m_18;
    u8 pad1c[0x0c];
    f32 m_28; f32 m_2c; u32 m_30;
    u8 pad34[0x0c];
    f32 m_40; f32 m_44; u32 m_48;
    u8 pad4c[0x0c];
    f32 m_58; f32 m_5c; u32 m_60;
    u8 pad64[0x0c];
    f32 m_70; f32 m_74; u32 m_78;
    f32 m_7c; f32 m_80; f32 m_84;
    f32 m_88[12];
    u32 m_b8;
    s16 m_bc;
    u8 padbe[2];
    u32 m_c0;
};

struct Pl_802AF9C0 { u8 pad[0xd48]; f32 m_d48; };
struct V3_802AF9C0 { f32 x, y, z; };
struct Plane_802AF9C0 { V3_802AF9C0 point; V3_802AF9C0 normal; };
struct Ground_802AF9C0 { u32 m_00; Plane_802AF9C0 *m_04; };

extern "C" {

s32 release_texture_list(void*);
void *__ct__16TPlayerFootStampFv(void *, void *, void *);
void *__nw__7TObjectFUl(int);

void __ct__7TObjectFP7TObject(void *, void *);
s32 get_current_floor_area__Fv(void);
u16 get_entity_id(void *);
s32 get_class_index__10TObjPlayerFv(void *);
void *get_hit_data__14TBoss4DarkFalzFv(void);
void *get_position_ptr__10TObjPlayerFv(void *);
void queue_destruction__7TObjectFv(void *);
Ground_802AF9C0 *csnVecterUnder(void *, s32);
f32 cos_table_lookup(s32);
f32 sin_table_lookup(s32);
s32 rand();
s32 push_matrix();
s32 set_matrix_identity(int);
s32 rotate_matrix_y(int, int);
s32 rotate_matrix_z(int, int);
s32 fn_803D8DE0(int, void *, void *, int);
s32 pop_matrix();
extern s32 tl_07;
extern s32 lbl_805D3E88;
extern const f32 lbl_805DE1FC;
extern const f32 lbl_805DE200;
extern const f32 lbl_805DE204;
extern const f32 lbl_805DE208;
extern const f32 lbl_805DE20C;
extern const f32 lbl_805DE210;
extern const f32 lbl_804707F8[36];
extern const f32 lbl_80470888[24];
extern void *__vt__16TPlayerFootStamp[];
}

void direction_to_rotation_yx(u8 *arg0, s32 *arg1, s32 *arg2);

#pragma push
#pragma fp_contract on
void *__ct__16TPlayerFootStampFv(void *self, void *player, void *arg1) {
    FS_802AF9C0 *fs;
    Pl_802AF9C0 *pl;
    Ground_802AF9C0 *ground;
    void *hit;
    f32 basis[6];
    s32 v0c;
    s32 pitch;
    s16 ang;
    f32 d;
    f32 s;
    f32 r0;
    f32 p0, p1, p2;
    f32 q0, q1, q2;
    f32 n0, n1, n2;
    f32 nb0, nb1, nb2;
    f32 fx;
    f32 fy;
    f32 fz;

    fs = (FS_802AF9C0 *)self;
    pl = (Pl_802AF9C0 *)player;
    __ct__7TObjectFP7TObject(self, (void *)tl_07);
    fs->m_18 = __vt__16TPlayerFootStamp;
    fs->m_00 = lbl_805D3E88;
    switch (get_current_floor_area__Fv()) {
    case 0x1b:
        fs->m_b8 = 0xff402a20;
        break;
    case 0x1c:
        fs->m_b8 = 0xff001923;
        break;
    case 0x1d:
        fs->m_b8 = 0xff050300;
        break;
    default:
        fs->m_b8 = 0xff282828;
        break;
    }
    fs->m_bc = (s16)(s32)arg1;
    if (get_entity_id(player) >= 4) {
        queue_destruction__7TObjectFv(self);
        return self;
    }
    switch ((s8)get_class_index__10TObjPlayerFv(player)) {
    case 0:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[2];
        s = lbl_80470888[3] * d + lbl_805DE1FC;
        fx = lbl_804707F8[3] * s;
        fy = lbl_804707F8[4] * s;
        fz = lbl_804707F8[5] * s;
        break;
    case 1:
        ((TPlayerFootStamp *)self)->sub_802B0204(1);
        d = pl->m_d48 - lbl_80470888[4];
        s = lbl_80470888[5] * d + lbl_805DE1FC;
        fx = lbl_804707F8[6] * s;
        fy = lbl_804707F8[7] * s;
        fz = lbl_804707F8[8] * s;
        break;
    case 2:
        ((TPlayerFootStamp *)self)->sub_802B0204(1);
        d = pl->m_d48 - lbl_80470888[6];
        s = lbl_80470888[7] * d + lbl_805DE1FC;
        fx = lbl_804707F8[9] * s;
        fy = lbl_804707F8[10] * s;
        fz = lbl_804707F8[11] * s;
        break;
    case 3:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[8];
        s = lbl_80470888[9] * d + lbl_805DE1FC;
        fx = lbl_804707F8[12] * s;
        fy = lbl_804707F8[13] * s;
        fz = lbl_804707F8[14] * s;
        break;
    case 4:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[10];
        s = lbl_80470888[11] * d + lbl_805DE1FC;
        fx = lbl_804707F8[15] * s;
        fy = lbl_804707F8[16] * s;
        fz = lbl_804707F8[17] * s;
        break;
    case 5:
        ((TPlayerFootStamp *)self)->sub_802B0204(1);
        d = pl->m_d48 - lbl_80470888[12];
        s = lbl_80470888[13] * d + lbl_805DE1FC;
        fx = lbl_804707F8[18] * s;
        fy = lbl_804707F8[19] * s;
        fz = lbl_804707F8[20] * s;
        break;
    case 6:
        ((TPlayerFootStamp *)self)->sub_802B0204(1);
        d = pl->m_d48 - lbl_80470888[14];
        s = lbl_80470888[15] * d + lbl_805DE1FC;
        fx = lbl_804707F8[21] * s;
        fy = lbl_804707F8[22] * s;
        fz = lbl_804707F8[23] * s;
        break;
    case 7:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[16];
        s = lbl_80470888[17] * d + lbl_805DE1FC;
        fx = lbl_804707F8[24] * s;
        fy = lbl_804707F8[25] * s;
        fz = lbl_804707F8[26] * s;
        break;
    case 8:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[18];
        s = lbl_80470888[19] * d + lbl_805DE1FC;
        fx = lbl_804707F8[27] * s;
        fy = lbl_804707F8[28] * s;
        fz = lbl_804707F8[29] * s;
        break;
    case 9:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[20];
        s = lbl_80470888[21] * d + lbl_805DE1FC;
        fx = lbl_804707F8[30] * s;
        fy = lbl_804707F8[31] * s;
        fz = lbl_804707F8[32] * s;
        break;
    case 10:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[22];
        s = lbl_80470888[23] * d + lbl_805DE1FC;
        fx = lbl_804707F8[33] * s;
        fy = lbl_804707F8[34] * s;
        fz = lbl_804707F8[35] * s;
        break;
    case 11:
    default:
        ((TPlayerFootStamp *)self)->sub_802B0204(0);
        d = pl->m_d48 - lbl_80470888[0];
        s = lbl_80470888[1] * d + lbl_805DE1FC;
        fx = lbl_804707F8[0] * s;
        fy = lbl_804707F8[1] * s;
        fz = lbl_804707F8[2] * s;
        break;
    }
    fs->m_28 = lbl_805DE200;
    fs->m_2c = lbl_805DE200;
    fs->m_30 = fs->m_b8;
    fs->m_40 = lbl_805DE200;
    fs->m_44 = lbl_805DE1FC;
    fs->m_48 = fs->m_b8;
    fs->m_58 = lbl_805DE1FC;
    fs->m_5c = lbl_805DE200;
    fs->m_60 = fs->m_b8;
    fs->m_70 = lbl_805DE1FC;
    fs->m_74 = lbl_805DE1FC;
    fs->m_78 = fs->m_b8;
    hit = get_hit_data__14TBoss4DarkFalzFv();
    VecCopy((Vec *)&fs->m_7c, (const Vec *)get_position_ptr__10TObjPlayerFv(player));
    fs->m_80 += lbl_805DE204;
    ground = csnVecterUnder(&fs->m_7c, 0x16EF);
    if (ground == NULL) {
        queue_destruction__7TObjectFv(self);
        return self;
    }
    ang = (s16)*(u32 *)((u8 *)hit + 4);
    VecCopy((Vec *)&fs->m_7c, (const Vec *)&ground->m_04->point);
    r0 = (f32)rand();
    fs->m_80 += lbl_805DE208 * (lbl_805DE20C * r0) + lbl_805DE208;
    if (fs->m_bc != 0) {
        if (fs->m_bc == 1) {
            ang = (s16)(ang + 1);
        } else {
            queue_destruction__7TObjectFv(self);
            return self;
        }
    }
    fs->m_7c = fz * cos_table_lookup(ang) + fs->m_7c;
    fs->m_84 = fs->m_84 - fz * sin_table_lookup(ang);
    basis[0] = lbl_805DE200;
    basis[1] = lbl_805DE200;
    basis[2] = lbl_805DE1FC;
    basis[3] = lbl_805DE200;
    basis[4] = lbl_805DE1FC;
    basis[5] = lbl_805DE200;
    direction_to_rotation_yx((u8 *)&ground->m_04->normal, &v0c, &pitch);
    if (pitch < 0x2000 || pitch > 0x6000) {
        queue_destruction__7TObjectFv(self);
        return self;
    }
    push_matrix();
    set_matrix_identity(0);
    rotate_matrix_y(0, *(s32 *)((u8 *)hit + 4));
    rotate_matrix_z(0, pitch);
    fn_803D8DE0(0, basis, basis, 2);
    pop_matrix();
    fy = fy * lbl_805DE210;
    fx = fx * lbl_805DE210;
    q0 = basis[3] * fy;
    q1 = basis[4] * fy;
    p1 = basis[1] * fx;
    fs->m_88[0] = basis[0] * fx + q0;
    q2 = basis[5] * fy;
    p2 = basis[2] * fx;
    p0 = basis[0] * fx;
    fs->m_88[1] = q1 + p1;
    fs->m_88[2] = q2 + p2;
    fs->m_88[3] = q0 - p0;
    nb0 = -basis[3];
    n0 = nb0 * fy;
    fs->m_88[4] = q1 - p1;
    nb1 = -basis[4];
    n1 = nb1 * fy;
    fs->m_88[5] = q2 - p2;
    nb2 = -basis[5];
    n2 = nb2 * fy;
    fs->m_88[6] = n0 + p0;
    fs->m_88[7] = n1 + p1;
    fs->m_88[8] = n2 + p2;
    fs->m_88[9] = n0 - p0;
    fs->m_88[10] = n1 - p1;
    fs->m_88[11] = n2 - p2;
    fs->m_c0 = 0x96;
    return self;
}
#pragma pop

extern "C" {

void *TPlayerFootStamp::create(void *arg0, void *arg1) {
    void *o;
    o = __nw__7TObjectFUl(0xC4);
    if (o != NULL) {
        o = __ct__16TPlayerFootStampFv(o, arg0, arg1);
    }
    return o;
}

extern u32 player_footstamp_texture_gvm_handle;

void TPlayerFootStamp::free_instance() {
    if ((u32) player_footstamp_texture_gvm_handle != 0U) {
        release_texture_list((void*)player_footstamp_texture_gvm_handle);
        TAdSinglePlyChrSelectGC::safe_free(player_footstamp_texture_gvm_handle);
        player_footstamp_texture_gvm_handle = 0U;
    }
}

}
