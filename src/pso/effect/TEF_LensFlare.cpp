#include "types.h"
#include "pso/effect/TEF_LensFlare.h"
#include "pso/effect/TEF_PvrWave.h"
#include "pso/effect/TEF_LensFlare.h"

#include "pso/TMainTask.h"
#include "pso/TParticleCtrl.h"
#include "pso/math/MatrixVector.h"
#include "pso/misc/TWindowSubStatusDisp.h"
#include "pso/misc/TWindowSubStatusDisp_803DEE6C.h"
#include "pso/object/TObjFish.h"
#include "pso/render/render_util.h"
#include "pso/system/MatrixOps.h"
#include "pso/system/MatrixStack.h"
#include "pso/system/vector.h"
#include "pso/unk/text_803D853C.h"
#include "pso/unk/text_803D8F74.h"
#include "pso/unk/text_803D96A8.h"

struct Base_8008194C_80081278 { char pad[0x50]; };
struct VObj_8008194C_80081278 : Base_8008194C_80081278 {
    virtual void m0();
    virtual void m1();
};

struct RecoveredGlobal_800818D8_lbl_8048E040 {
    s32 value;
    u8 remaining[0xEC];
};

struct RecoveredGlobal_800818D8_lbl_8048E130 {
    s32 value;
    u8 remaining[0x34];
};

struct FlareVec { f32 x, y, z; };
struct FlareScreenPt { f32 x, y; };
struct FlareQuad { f32 x0, y0, x1, y1, r, g, b, a; };
struct FlareItem {
    FlareVec pos;
    f32 f0c;
    f32 f10;
    f32 f14;
    f32 sx;
    f32 sy;
    u32 color;
    u8 b0;
    u16 h0;
};
struct FlareElement {
    s32 def_index;
    f32 offset;
    f32 size;
    f32 alpha;
    f32 color_mul;
    f32 pad14;
};
struct FlareDefLayer {
    u32 flags;
    void *texlist;
    s32 texture;
    s32 uv_count;
    f32 (*uvs)[4];
    f32 width;
    f32 height;
    u32 color;
    s32 texlist_index;
    s32 sprite_type;
};
struct FlareDefSet { FlareDefLayer layers[9]; };

extern "C" {
extern FlareDefLayer lbl_804C5820[];
extern FlareVec lbl_80438E40;
extern u8 *camera_ctrl_instance;
void normalize_vector(FlareVec *vector);
s32 __ct__8TObjBaseFP7TObject(void *, void *);
extern RecoveredGlobal_800818D8_lbl_8048E040 lens_flare_reflected_element_descriptors;
extern s32 __vt__13TEF_LensFlare[];
extern s32 TEF_LensFlare__class_name;
u8 *TEF_LensFlare__ct(u8 *arg0, s32 arg1, s32 arg2);
void *__dt__13TEF_LensFlareFv(void *arg0, s16 arg1);
void __dl__7TObjectFPv(void *);

}
TEF_LensFlare::~TEF_LensFlare() {

}
extern "C" {

typedef char RecoveredGlobal_800818D8_lbl_8048E040_size[sizeof(RecoveredGlobal_800818D8_lbl_8048E040) == 0xF0 ? 1 : -1];
typedef char RecoveredGlobal_800818D8_lbl_8048E130_size[sizeof(RecoveredGlobal_800818D8_lbl_8048E130) == 0x38 ? 1 : -1];
u8 *TEF_LensFlare__ct(u8 *ef_lens_flare, s32 parent, s32 arg2) {
    __ct__8TObjBaseFP7TObject((void *)ef_lens_flare, (void *)parent);
    *(s32 **)((s8 *)ef_lens_flare + 0x18) = &(*(RecoveredGlobal_800818D8_lbl_8048E130 *)&__vt__13TEF_LensFlare).value;
    *(s32 *)((s8 *)ef_lens_flare + 0) = (s32) TEF_LensFlare__class_name;
    ((TEF_LensFlare *)(ef_lens_flare))->apply_object_set_data((void *)arg2);
    *(s32 **)((s8 *)ef_lens_flare + 0x90) = &lens_flare_reflected_element_descriptors.value;
    return ef_lens_flare;
}

void TEF_LensFlare::run_task() {  }
void TEF_PvrWave::render() {  }

void TEF_PvrWave::run_task() {
    struct VObj_8008194C_80081278 *o = (struct VObj_8008194C_80081278 *)*(void **)((s8 *)this + 0x1C);
    o->m1();
}

#pragma push
#pragma fp_contract on
void TEF_LensFlare::render() {
    FlareItem item;
    FlareQuad glow;
    FlareQuad halo;
    FlareQuad refl;
    FlareVec view;
    FlareVec rotated;
    FlareVec dir;
    FlareVec point;
    FlareScreenPt scr;
    u8 glow_color[4];
    u8 halo_color[4];
    u8 refl_color[4];
    s8 *self = (s8 *)this;
    FlareItem *pi = &item;
    u8 *cam;
    FlareElement *element;
    FlareDefSet *set;
    FlareDefLayer *layer;
    f32 dot;
    f32 dist_sq;
    f32 glow_sq;
    f32 halo_alpha;
    f32 halo_sq;
    f32 halo_cube;
    f32 refl_alpha;
    f32 refl_base;
    f32 refl_scale;
    f32 center_dx;
    f32 center_dy;
    f32 half_w;
    f32 half_h;
    f32 scale;
    s32 i;

    if (TMainTask::get_render_pass() == 0) {
        return;
    }
    cam = camera_ctrl_instance;
    if (cam == NULL) {
        return;
    }
    item.color = 0;
    item.pos.x = 0.0f;
    item.pos.y = 0.0f;
    item.pos.z = 0.0f;
    item.f0c = 0.0f;
    item.f10 = 0.0f;
    item.f14 = 0.0f;
    item.sx = 0.0f;
    item.sy = 0.0f;
    item.b0 = 0;
    item.h0 = 0;
    set_additive_blend();
    if (*(f32 *)(self + 0x68) >= 0.0f) {
        scale = 10.0f * *(f32 *)(self + 0x68);
        if (is_player_near(scale * scale) != 0) {
            return;
        }
    }
    TParticleCtrl::begin_effect_render();
    cam = camera_ctrl_instance;
    view.x = *(f32 *)(self + 0x38) - *(f32 *)(cam + 0x178);
    view.y = *(f32 *)(self + 0x3C) - *(f32 *)(cam + 0x17C);
    view.z = *(f32 *)(self + 0x40) - *(f32 *)(cam + 0x180);
    dist_sq = vec_squared_length((const Vec *)&view);
    if (0.0f != dist_sq) {
        normalize_vector(&view);
    }
    push_matrix_from(identity_matrix);
    *(u32 *)&dir.x = *(const u32 *)&lbl_80438E40;
    *(u32 *)&dir.y = ((const u32 *)&lbl_80438E40)[1];
    *(u32 *)&dir.z = ((const u32 *)&lbl_80438E40)[2];
    cam = camera_ctrl_instance;
    rotate_matrix_y(0, *(s32 *)(cam + 0x194));
    cam = camera_ctrl_instance;
    rotate_matrix_x(0, *(s32 *)(cam + 0x190));
    rotate_vector_by_matrix(0, (const Vec *)&dir, (Vec *)&rotated);
    pop_matrix();
    dot = vec3_dot((const Vec *)&rotated, (const Vec *)&view);
    if (dot > 0.0f) {
        set_depth_buffer_settings_1();
        project_world_to_screen(0, (const Vec *)(self + 0x38), &scr.x);
        if (dot > 0.99f) {
            glow_sq = 50.0f * (dot - 0.98f);
            glow_sq = glow_sq * glow_sq;
            glow_color[1] = 0xff;
            glow_color[2] = 0xff;
            glow_color[3] = 0xff;
            glow_color[0] = (s32)(255.0f * (0.9f * glow_sq));
            point.x = scr.x;
            point.y = scr.y;
            point.z = 0.0f;
            item.color = *(u32 *)glow_color;
            VecCopy((Vec *)&pi->pos, (const Vec *)&point);
            item.sy = item.sx = 20.0f * glow_sq;
            begin_screen_draw(1);
            TObjFish::set_global_param((s32)lbl_804C5820[15].texlist);
            set_draw_texture_and_color(lbl_804C5820[15].texture, -1);
            half_w = lbl_804C5820[15].width * (2.0f * item.sx);
            half_h = lbl_804C5820[15].height * (2.0f * item.sy);
            glow.r = 0.0f;
            glow.x0 = point.x - half_w;
            glow.g = 0.0f;
            glow.x1 = point.x + half_w;
            glow.b = 1.0f;
            glow.y0 = point.y - half_h;
            glow.a = 1.0f;
            glow.y1 = point.y + half_h;
            set_constant_material_color(item.color);
            draw_textured_quad_at_depth((f32 *)&glow, 0.5f);
            TWindowSubStatusDisp::get_player();
        }
        if (dot > 0.6f) {
            halo_alpha = 3.0f * (dot - 0.6f);
        } else {
            halo_alpha = 0.0f;
        }
        halo_sq = halo_alpha * halo_alpha;
        halo_cube = halo_alpha * halo_sq;
        halo_alpha = halo_alpha * halo_cube;
        halo_color[0] = 0xff;
        halo_color[1] = 0xff;
        halo_color[2] = 0xff;
        halo_color[3] = 0xff;
        center_dx = 320.0f - scr.x;
        center_dy = 240.0f - scr.y;
        point.x = scr.x;
        point.y = scr.y;
        point.z = 0.0f;
        item.color = *(u32 *)halo_color;
        VecCopy((Vec *)&pi->pos, (const Vec *)&point);
        item.sy = item.sx = 1.0f;
        begin_screen_draw(1);
        TObjFish::set_global_param((s32)lbl_804C5820[9].texlist);
        set_draw_texture_and_color(lbl_804C5820[9].texture, -1);
        half_w = lbl_804C5820[9].width * (2.0f * item.sx);
        half_h = lbl_804C5820[9].height * (2.0f * item.sy);
        halo.r = 0.0f;
        halo.x0 = point.x - half_w;
        halo.g = 0.0f;
        halo.x1 = point.x + half_w;
        halo.b = 1.0f;
        halo.y0 = point.y - half_h;
        halo.a = 1.0f;
        halo.y1 = point.y + half_h;
        set_constant_material_color(item.color);
        draw_textured_quad_at_depth((f32 *)&halo, 0.5f);
        TWindowSubStatusDisp::get_player();
        element = (FlareElement *)*(void **)(self + 0x90);
        refl_alpha = 1.0f - halo_alpha;
        set = (FlareDefSet *)lbl_804C5820;
        refl_base = 1.0f;
        for (i = 0; i < 9; i++, element++) {
            refl_scale = element->size * (refl_base - refl_alpha * element->alpha);
            if (refl_scale < 0.0f) {
                refl_scale = 0.0f;
            }
            refl_color[1] = 0xff;
            refl_color[2] = 0xff;
            refl_color[3] = 0xff;
            refl_color[0] = (s32)(255.0f * (halo_alpha * element->color_mul));
            item.color = *(u32 *)refl_color;
            point.x = center_dx * element->offset + scr.x;
            point.y = center_dy * element->offset + scr.y;
            point.z = 0.0f;
            VecCopy((Vec *)&pi->pos, (const Vec *)&point);
            item.sx = refl_scale;
            item.sy = (f32)(f64)refl_scale;
            begin_screen_draw(1);
            layer = &set->layers[element->def_index + 9];
            TObjFish::set_global_param((s32)set->layers[element->def_index + 9].texlist);
            set_draw_texture_and_color(set->layers[element->def_index + 9].texture, -1);
            half_w = layer->width * (2.0f * item.sx);
            half_h = layer->height * (2.0f * item.sy);
            refl.r = 0.0f;
            refl.x0 = point.x - half_w;
            refl.g = 0.0f;
            refl.x1 = point.x + half_w;
            refl.b = 1.0f;
            refl.y0 = point.y - half_h;
            refl.a = 1.0f;
            refl.y1 = point.y + half_h;
            set_constant_material_color(item.color);
            draw_textured_quad_at_depth((f32 *)&refl, 0.5f);
            TWindowSubStatusDisp::get_player();
        }
        restore_saved_depth_alpha_state();
    }
    TParticleCtrl::end_effect_render();
}
#pragma pop

}
