#include "types.h"
extern "C" {
int OSResetSystem(int, int, int);

void tC(u32 base) {
    OSResetSystem(2,0,0);
    __asm("lwz r0, 0xE0(r26)");
    __asm("isync");
    __asm("mtlr r0");
    __asm("blr");
}
}
