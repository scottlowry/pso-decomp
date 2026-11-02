// Probe V1: file-scope-static synthesis spelling for fn_801A3BB8.
// Goal: MWCC natively emits __sinit_text_801A3BB8_cpp (ctor+register wrapper,
// 15 words), auto .ctors entry, and the two .bss blobs (registration 0xC +
// object 0x41C) in era order DDE0(reg) -> DDEC(obj).
#include "types.h"

class TPlyCharData {
public:
    TPlyCharData();
    ~TPlyCharData();
    u8 d[0x41C];
};

TPlyCharData TPlyCharData__global_character_data;
