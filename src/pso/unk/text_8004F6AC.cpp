#include "types.h"
#include "pso/system/vector.h"
#include "pso/misc/CameraHelpers.h"
#include "pso/misc/TCameraCtrl.h"
#include "pso/unk/text_8004AA04.h"

#pragma readonly_strings on

// One model of the Dark Falz death scene: its model, texture list and motion.
struct Part_8004F6AC {
    s32 model;
    s32 texlist;
    s32 motion;
};

typedef struct Obj_8004F6AC {
    s32 name;
    u8 pad04[0x14];
    u8 *vt;
    u8 pad1C[0x90 - 0x1C];
    ModelNodeTables f90;
    s32 fa4[2];
    Part_8004F6AC parts1[2];
    Part_8004F6AC parts2[3];
    Vec pos;
    s32 angle;
    s32 timer;
    f32 frame;
    s32 node_list;
    Vec emitter_positions[2];
} Obj_8004F6AC;

typedef char Obj_8004F6AC_size[sizeof(Obj_8004F6AC) == 0x11C ? 1 : -1];

extern "C" {

void *TObjDFDemo4__ct(void *arg0, void *parent, const Vec *pos, s32 angle);
s32 __ct__8TObjBaseFP7TObject(void *, void *);
s32 get_instance_count__9TBoss4UroFv(void);
s32 get_bml_model(s32, s32);
s32 get_bml_motion(s32, s32);
s32 TObjFish__sub_8001EDB0(s32, s32);
s32 TObjFish__sub_800E3124(void *, s32);
s32 activate_camera_mode(s32);
void *__dt__11TObjDFDemo4Fv(void *, s16);
void run_task__11TObjDFDemo4Fv(void);
void render__11TObjDFDemo4Fv(void);
extern "C" void vfunc_6__8TObjBaseFPsl();
extern "C" void get_name__8TObjBaseFv();
extern "C" void get_center__8TObjBaseFv();
extern "C" void apply_object_set_data__8TObjBaseFPv();
extern "C" void classify_actor_view_detail__8TObjFfff();
extern "C" void render_shadows__7TObjectFv();
extern "C" void reset_motion_fields__8TObjBaseFv();
extern "C" void update_object_view_visibility__8TObjBaseFff();
extern const ModelNodeSpec lbl_804373C4[2];
extern const CameraPlayback lbl_804373DC;
extern const CameraAngles lbl_804373E8;
extern const float lbl_805D8A04;
extern s32 boss4_zanzo_bml_index_table[];
extern s32 lbl_80486FB0[3];

// The body motion ids for the two model groups; the vtable below is the tail
// of the same data blob.
s32 lbl_80485720[5] = {0x12, 0x11, 0x20, 0x21, 0x22};

// TObjFish node table for the emitter positions, padded to the vtable.
s32 lbl_80485734[12] = {0x34, 0, 0, 0, 0x35, 0, 0, 0, -1, 0, 0, 0};

void *__vt__11TObjDFDemo4[13] = {
    (void *)0x0, (void *)0x0, (void *)&__dt__11TObjDFDemo4Fv, (void *)&run_task__11TObjDFDemo4Fv,
    (void *)&render__11TObjDFDemo4Fv, (void *)&render_shadows__7TObjectFv, (void *)&vfunc_6__8TObjBaseFPsl,
    (void *)&apply_object_set_data__8TObjBaseFPv,
    (void *)&reset_motion_fields__8TObjBaseFv, (void *)&get_center__8TObjBaseFv,
    (void *)&update_object_view_visibility__8TObjBaseFff, (void *)&classify_actor_view_detail__8TObjFfff,
    (void *)&get_name__8TObjBaseFv,
};

const char *lbl_805D2798 = "TObjDFDemo4";

#pragma push
#pragma opt_common_subs off
#pragma opt_propagation off
#define self ((Obj_8004F6AC *)arg0)
void *TObjDFDemo4__ct(void *arg0, void *parent, const Vec *pos, s32 angle) {
    s32 *blob = lbl_80485720;
    s32 k;
    s32 res;
    s32 i;

    __ct__8TObjBaseFP7TObject(self, parent);
    // The vtable is the tail of this file's data blob.
    self->vt = (u8 *)&blob[17];
    self->name = (s32)lbl_805D2798;
    VecCopy(&self->pos, pos);
    self->angle = angle;
    res = get_instance_count__9TBoss4UroFv();
    for (i = 0; i < 2; i++) {
        s32 t = boss4_zanzo_bml_index_table[i];
        k = t;
        ((s32 *)self)[i * 3 + 0x2b] = get_bml_model(res, t);
        ((s32 *)self)[i * 3 + 0x2c] = TObjFish__sub_8001EDB0(res, k);
        ((s32 *)self)[i * 3 + 0x2d] = get_bml_motion(res, lbl_80485720[i]);
    }
    {
        // The second model group's motions start two ids into the table.
        s32 *motions = &blob[2];
        for (i = 0; i < 3; i++) {
            s32 t = lbl_80486FB0[i];
            k = t;
            ((s32 *)self)[i * 3 + 0x31] = get_bml_model(res, t);
            ((s32 *)self)[i * 3 + 0x32] = TObjFish__sub_8001EDB0(res, k);
            ((s32 *)self)[i * 3 + 0x33] = get_bml_motion(res, motions[i]);
        }
    }
    self->frame = lbl_805D8A04;
    init_model_node_tables(&self->f90, lbl_804373C4, 2);
    for (s32 j = 0; j < 2; j++) {
        self->fa4[j] = 0;
    }
    activate_camera_mode(5);
    {
        CameraPlayback playback = lbl_804373DC;
        CameraAngles angles = lbl_804373E8;
        angles.yaw = self->angle;
        set_scripted_camera_pose(&self->pos, &self->pos, &angles);
        ((TCameraCtrl *)&playback)->cache_target_and_forward(0x416C);
    }
    self->node_list = TObjFish__sub_800E3124(&blob[5], (s32)self->emitter_positions);
    self->timer = 0;
    return self;
}
#undef self
#pragma pop

// Defined after the constructor: they follow the constructor's string pool in .rodata.
const ModelNodeSpec lbl_804373C4[2] = {
    {0xC, 0x4A, 1}, {0xE, 0x4A, 1},
};

const CameraPlayback lbl_804373DC = {0, 3, 0, 0.0f, 0.5f};

const CameraAngles lbl_804373E8 = {0, 0, 0};

}
