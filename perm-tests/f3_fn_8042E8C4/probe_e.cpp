#include "types.h"
extern "C" {
int OSResetSystem(int, int, int);
void e1(u32 b) {
    OSResetSystem(2,0,0);
    __asm { lwz r0, 0xE0(r26) }
    __asm { isync }
    __asm { mtlr r0 }
    for (;;) { }
}
void e2(u32* p) {
    OSResetSystem(2,0,0);
    __asm { lwz r0, 0xE0(r26) }
    __asm { isync }
    __asm { blr }
}
}
