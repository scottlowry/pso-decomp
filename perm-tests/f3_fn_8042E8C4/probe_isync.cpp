#include "types.h"
extern "C" void probe_a(void* p) {
    __isync();
    ((void(*)(void))((u32*)p)[0])();
}
extern "C" int probe_b(void) {
    __isync();
    return 7;
}
