extern "C" void ff(int);
extern "C" void s_0(short a) { ff(a == 2); }
extern "C" void s_1(short a) { ff((a == 2) + 0); }
extern "C" void s_2(short a) { ff((a == 2) | 0); }
extern "C" void s_3(short a) { ff((a == 2) ^ 0); }
extern "C" void s_4(short a) { ff((a == 2) * 1); }
extern "C" void s_5(short a) { ff((a == 2) - 0); }
extern "C" void s_6(short a) { ff((a == 2) ? 1 : 0); }
extern "C" void s_7(short a) { ff(!(a != 2)); }
extern "C" void s_8(short a) { ff((int)(a == 2)); }
extern "C" void s_9(short a) { ff((a == 2) & 1); }
extern "C" void s_10(unsigned a) { ff(a == 2u); }
extern "C" void s_11(int a) { ff(a == 2); }
extern "C" void s_12(short a) { ff(2 == a); }
extern "C" void s_13(short a) { int x; x = (a == 2); ff(x); }
extern "C" void s_14(short a) { ff((int)(a - 2 == 0)); }
extern "C" void s_15(short a) { ff((a == 2) << 0); }
enum E2 { E2_TWO = 2 };
extern "C" void s_16(short a) { ff((int)(a == (short)E2_TWO)); }
extern "C" void s_17(short a) { ff((unsigned)(a == 2)); }
extern "C" void s_18(short a) { ff((a == 2) != 0); }
extern "C" void s_19(short a) { ff(0 + (a == 2)); }
