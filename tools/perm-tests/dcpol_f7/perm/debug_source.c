
typedef signed char s8;
typedef unsigned char u8;
typedef signed short s16;
typedef unsigned short u16;
typedef signed long s32;
typedef unsigned long u32;
typedef signed long long s64;
typedef unsigned long long u64;
typedef float f32;
typedef double f64;
typedef int permbool;
typedef struct Vtx_803E352C
{
  f32 x;
  f32 y;
  f32 z;
  f32 nx;
  f32 ny;
  f32 nz;
  u32 pad[2];
} Vtx_803E352C;
typedef struct Vtx_803E36C4
{
  f32 x;
  f32 y;
  f32 z;
  f32 nx;
  f32 ny;
  f32 nz;
  u32 pad[2];
} Vtx_803E36C4;
typedef struct Vtx_803E46FC
{
  f32 x;
  f32 y;
  f32 z;
  f32 nx;
  f32 ny;
  f32 nz;
  u32 pad[2];
} Vtx_803E46FC;
typedef struct Vtx_803E47E0
{
  f32 x;
  f32 y;
  f32 z;
  f32 nx;
  f32 ny;
  f32 nz;
  u32 pad[2];
} Vtx_803E47E0;
extern s16 *chunk_polygon_list_cache[];
extern s32 lbl_805D7798;
extern s32 chunk_polygon_flags_and_mask;
extern s32 chunk_polygon_flags_or_mask;
extern s32 chunk_previous_strip_flags;
extern u32 chunk_strip_dirty_flags;
extern s32 model_render_flags;
extern u32 chunk_has_vertex_colors;
void set_chunk_blend__FUl(u32 x);
void apply_chunk_texture_command__Fll(s32 arg0, s32 arg1);
void setup_chunk_tev_stages__Fv(void);
void set_strip_lighting_chan_ctrl__FUl(u32 flags);
void set_chunk_blend_depth_mode__Fll(s32 arg0, s32 arg1);
s32 GXSetTexCoordGen2(s32, s32, s32, s32, s32, s32);
void draw_chunk_color_tex_strips(s16 *, void *, u32, permbool);
void draw_chunk_textured_strips(s16 *list, Vtx_803E352C *verts, u32 info, s32 large);
void submit_chunk_material_color__FUcPs(s32, s16 *);
void setup_tev_passclr__10TObjPlayerFv(void);
void draw_strip_pos_normal__10TObjPlayerFPvPvUi(s16 *list, Vtx_803E46FC *verts, u32 info);
void draw_strip_list_pos_nrm__10TObjPlayerFPvPvUi(s16 *list, Vtx_803E36C4 *verts, u32 info);
void draw_triangle_strips__10TObjPlayerFPvPvUi(s16 *list, Vtx_803E47E0 *verts, u32 info);
#pragma push
#pragma scheduling off
#pragma use_lmw_stmw off
void dispatch_chunk_polygon_list(s16 *list, s32 buffer)
{
  s32 cmd;
  u32 count;
  s32 info;
  s16 op;
  s16 slot;
  u32 changed;
  s16 t;
  while ((cmd = *(list++)) != 0xFF)
  {
    op = cmd & 0xFF;
    if (op < 8)
    {
      switch (op)
      {
        case 1:
          set_chunk_blend__FUl(cmd);
          break;

        case 4:
          slot = (cmd >> 8) & 0xFF;
          chunk_polygon_list_cache[slot] = list;
          lbl_805D7798++;
          return;

        case 5:
          slot = (cmd >> 8) & 0xFF;
          dispatch_chunk_polygon_list(chunk_polygon_list_cache[slot], buffer);
          lbl_805D7798--;
          break;

      }

    }
    else
      if (op < 0x10)
    {
      apply_chunk_texture_command__Fll(cmd, *list);
      list++;
    }
    else
      if (op < 0x40)
    {
      op = *(list++);
      set_chunk_blend__FUl(cmd);
      submit_chunk_material_color__FUcPs(cmd, list);
      list += op;
    }
    else
    {
      count = *((u16 *) list);
      t = list[1];
      list += 2;
      info = t;
      if (((u32) (model_render_flags & 0x800)) != 0)
      {
        cmd = (s16) (cmd & chunk_polygon_flags_and_mask);
        cmd = (s16) (cmd | chunk_polygon_flags_or_mask);
      }
      cmd = (s16) (cmd >> 8);
      changed = cmd ^ chunk_previous_strip_flags;
      changed = changed | chunk_strip_dirty_flags;
      chunk_previous_strip_flags = cmd;
      chunk_strip_dirty_flags = 0;
      if ((changed & 1) != 0)
      {
        set_strip_lighting_chan_ctrl__FUl(cmd);
      }
      switch (op)
      {
        case 0x40:
          if ((cmd & 0x40) != 0)
        {
          set_chunk_blend_depth_mode__Fll(cmd, 1);
          setup_chunk_tev_stages__Fv();
          GXSetTexCoordGen2(0, 0, 1, 0x2A, 0, 0x7D);
          draw_strip_pos_normal__10TObjPlayerFPvPvUi(list, (Vtx_803E46FC *) buffer, info);
        }
        else
        {
          set_chunk_blend_depth_mode__Fll(cmd, 0);
          setup_tev_passclr__10TObjPlayerFv();
          draw_strip_list_pos_nrm__10TObjPlayerFPvPvUi(list, (Vtx_803E36C4 *) buffer, info);
        }
          break;

        case 0x41:

        case 0x42:
          set_chunk_blend_depth_mode__Fll(cmd, 1);
          if ((cmd & 0x40) != 0)
        {
          setup_chunk_tev_stages__Fv();
          GXSetTexCoordGen2(0, 0, 1, 0x2A, 0, 0x7D);
          draw_triangle_strips__10TObjPlayerFPvPvUi(list, (Vtx_803E47E0 *) buffer, info);
        }
        else
          if (chunk_has_vertex_colors != 0)
        {
          setup_chunk_tev_stages__Fv();
          GXSetTexCoordGen2(0, 1, 4, 0x3C, 0, 0x7D);
          draw_chunk_color_tex_strips(list, (void *) buffer, info, op == 0x42);
        }
        else
        {
          setup_chunk_tev_stages__Fv();
          GXSetTexCoordGen2(0, 1, 4, 0x3C, 0, 0x7D);
          draw_chunk_textured_strips(list, (Vtx_803E352C *) buffer, info, op == 0x42);
        }
          break;

      }

      list += count - 1;
    }
  }

}

#pragma pop
