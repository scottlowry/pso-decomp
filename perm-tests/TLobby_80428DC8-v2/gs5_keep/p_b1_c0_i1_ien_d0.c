typedef signed char s8;
typedef unsigned char u8;
typedef signed short s16;
typedef unsigned short u16;
typedef signed long s32;
typedef unsigned long u32;

struct ModemSessionState {
    char **subst;
    u8 pad04[4];
    char *strbuf;
    u8 pad0C[2];
    s16 strstride;
    u8 **fields;
    u8 pad14[4];
    s16 *ints;
    u8 pad1C[0xC];
    u8 *cmd;
    u8 *out;
    u8 *expect;
    u8 *window;
    u8 *rxbuf;
    u8 pad3C[0xA];
    s16 window_len;
    s16 rxlen;
    u8 pad4A[0x16];
};

typedef struct Ent_80480138 {
    u32 f0;
    s32 mode[4];
} Ent_80480138;

struct ModemSessionState lobby_net_session_state;
extern Ent_80480138 lbl_80480138[5];
char *NetCopyString(char *destination, const char *source);

void TLobby__sub_80428DC8(s16 entry, s16 slot, u8 *text, s16 *cnt, s16 *num_cnt)
{
  s16 c;
  s16 n;
  char *dest;
  s16 i;
  u8 ch;
  if (lbl_80480138[entry].mode[slot] == 0)
  {
    c = *cnt;
    dest = lobby_net_session_state.strbuf + (c * lobby_net_session_state.strstride);
    NetCopyString(dest, (char *) text);
    lobby_net_session_state.fields[slot] = (u8 *) dest;
    *cnt = c + 1;
  }
  if (lbl_80480138[entry].mode[slot] == 1)
  {
    i = 0;
    entry = 0;
    n = *num_cnt;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry += ch;
      entry -= '0';
      ++i;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;
  }
}
