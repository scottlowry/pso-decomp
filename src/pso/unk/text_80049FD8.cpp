#include "pso/unk/text_80049FD8.h"

#include "pso/boss/TBoss3Volopt.h"
#include "pso/object/TObjVoloptPillar.h"
#include "pso/system/BmlResource.h"

extern "C" {
s32 __nw__7TObjectFUl(s32);
extern u8 *tl_05;
}

// The three debris chips a Vol Opt pillar bursts into when its pre-crash
// timer expires: the shared chip template, moved to the pillar's current
// position and tagged with the boss03 model/texture entry 0xE.
// opt_propagation off: stops the two models-pointer loads from being
// copy-propagated ahead of the template-copy block (fixes the f2/f0
// position-store role pair; scheduler hoist itself is spelling-invariant).
#pragma push
#pragma opt_propagation off
void fn_80049FD8(TObjVoloptPillar *pillar) {
    BmlModelEntry *models = boss3_volopt_resources->models;
    TObjChipParams params = volopt_pillar_chip_params;
    f32 z = pillar->position.z;
    f32 y = pillar->position.y;
    f32 x = pillar->position.x;
    s32 textures = models[0xE].m_c;
    s32 model = models[0xE].model;
    params.pos[0] = x;
    params.pos[1] = y;
    params.pos[2] = z;
    params.model = model;
    params.textures = textures;
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            __ct__8TObjChipFP7TObjectP14TObjChipParams(o, tl_05, (u8 *)&params);
        }
    }
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            __ct__8TObjChipFP7TObjectP14TObjChipParams(o, tl_05, (u8 *)&params);
        }
    }
    {
        u8 *o = (u8 *)__nw__7TObjectFUl(0x234);
        if (o != NULL) {
            __ct__8TObjChipFP7TObjectP14TObjChipParams(o, tl_05, (u8 *)&params);
        }
    }
}
#pragma pop
