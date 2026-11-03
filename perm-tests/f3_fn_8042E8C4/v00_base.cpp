#include "types.h"

extern "C" {

void* memmove(void*, void*, u32);
void* memset(void*, s32, u32);
void DCStoreRange(void*, u32);
void ICInvalidateRange(void*, u32);
int OSResetSystem(int, int, int);

void fn_8042E8C4(u32* arg)
{
    u32 size = arg[0x108 / 4];
    u32 base = arg[0x104 / 4];
    u32 len = (size + 0x132) & ~31u;

    memmove((void*)0x80003100u, arg, len);
    DCStoreRange((void*)0x80003100u, len);
    OSResetSystem(2, 0, 0);

    memset((void*)*(u32*)(base + 0xd8), 0, *(u32*)(base + 0xdc));
    DCStoreRange((void*)*(u32*)(base + 0xd8), *(u32*)(base + 0xdc));

    u32 i = 0;
    u32 off = 0;
    u32 prev = 0;
    do {
        u32 t = *(u32*)(base + off);
        u32 dst = *(u32*)(base + off + 0x48);
        u32 n = *(u32*)(base + off + 0x90);
        if (t == prev) {
            break;
        }
        memmove((void*)dst, (void*)(base + t), n);
        DCStoreRange((void*)dst, n);
        ICInvalidateRange((void*)dst, n);
        i += 1;
        off += 4;
    } while (i < 7);

    i = 0;
    off = 0;
    prev = 0;
    do {
        u32 t = *(u32*)(base + off + 0x1c);
        u32 dst = *(u32*)(base + off + 0x64);
        u32 n = *(u32*)(base + off + 0xac);
        if (t == prev) {
            break;
        }
        memmove((void*)dst, (void*)(base + t), n);
        DCStoreRange((void*)dst, n);
        i += 1;
        off += 4;
    } while (i < 11);

    __asm {
        lwz r0, 0xE0(r26)
        isync
        mtlr r0
        blr
    }
}

}
