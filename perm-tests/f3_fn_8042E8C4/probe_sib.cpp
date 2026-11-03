#include "types.h"
extern "C" {
void g(void);
void h(void);

void sA(void) { g(); }
void sB(u32* p) { ((void(*)(void))p[56])(); }
int  sC(u32* p) { ((int(*)(void))p[56])(); return 0; }
}
