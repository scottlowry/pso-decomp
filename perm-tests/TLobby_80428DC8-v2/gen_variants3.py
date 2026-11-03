#!/usr/bin/env python3.14
"""Third battery: within the v44 frontier basin, hunt the mul-in-place + ch-in-r0 flip."""
import gen_variants as G

FOLD = "entry = entry * 10 - '0' + ch;"
T = """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      %s
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;"""
T2 = """    n = *num_cnt;
    entry = 0;
    i = 0;
    while ((ch = text[i]) != 0)
    {
      %s
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;"""
T3 = """    i = 0;
    n = *num_cnt;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      %s
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;"""

V = {
 "w00_v44_3stmt": (T, "entry = entry * 10;\n      entry = entry - '0';\n      entry = entry + ch;"),
 "w01_v44_comm":  (T, "entry = ch + (entry * 10 - '0');"),
 "w02_v44_neg":   (T, "entry = entry * 10 - ('0' - ch);"),
 "w03_v44_lit":   (T, "entry = entry * 10 - 48 + ch;"),
 "w04_v44_paren": (T, "entry = (entry * 10 - '0') + ch;"),
 "w05_v44_comm2": (T, "entry = ch + entry * 10 - '0';"),
 "w06_v44_i2":    (T2, FOLD),
 "w07_v44_i3":    (T3, FOLD),
 "w08_v12_i2":    (T2, "entry = entry * 10 + (ch - '0');"),
 "w09_v12_i3":    (T3, "entry = entry * 10 + (ch - '0');"),
 "w10_v44_dbl":   (T.replace("while ((ch = text[i]) != 0)", "while (text[i] != 0)").replace(
                    "%s\n      i++;", "ch = text[i];\n      %s\n      i++;"), FOLD),
 "w11_v44_nfirst":(T, "entry = entry * 10 + ch - 48;"),  # = v41 tree, re-check in this scan
 "w12_mul2":      (T, "entry = entry + entry * 9 - '0' + ch;"),  # WRONG val (acc+9acc=10acc OK? entry+entry*9 == entry*10 yes) assoc probe
}
for name, (tmpl, stmt) in sorted(V.items()):
    body = tmpl % stmt
    src = G.HEAD + G.CHAMP_FOOT % body
    rc, o, err = G.compile_variant(name, src)
    if rc != 0:
        print(f"{name:16} COMPILE_FAIL"); continue
    print(f"{name:16} sz={G.fn_size(o)} raw={('%.5f'%G.score_offline(o))} {G.fingerprint(G.disasm(o))}")
