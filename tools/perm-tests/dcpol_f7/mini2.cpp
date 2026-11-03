extern "C" void gg(unsigned char);
extern "C" void other(void);
extern "C" void p_bool(bool large) { other(); if (large) { gg(12); } else { gg(8); } }
extern "C" void p_int(int large) { other(); if (large) { gg(12); } else { gg(8); } }
extern "C" void p_tern(bool large) { other(); gg(large ? 12 : 8); }
extern "C" void p_inttern(int large) { other(); gg(large ? 12 : 8); }
extern "C" void p_nezero(bool large) { other(); gg(large != 0 ? 12 : 8); }
extern "C" void p_u8(unsigned char large) { other(); gg(large ? 12 : 8); }
extern "C" void p_boolassign(bool large) { int x; x = large; other(); gg(x ? 12 : 8); }
