#include "types.h"
extern "C" {
int OSResetSystem(int, int, int);

__attribute__((naked)) void n2(u32* p) {
    OSResetSystem(2,0,0);
    __asm { blr }
}
__attribute__((noreturn)) void n3(u32* p);
void n3(u32* p) {
    OSResetSystem(2,0,0);
    __asm { blr }
}
}
