#!/usr/bin/env python3.14
"""Round 2 of the fold-neighbor battery: associativity/cast/temp spellings
near the v12 frontier state."""
import gen_variants as G  # reuse HEAD/CHAMP_FOOT machinery

V = {
 "v41_lassoc": "    entry = entry * 10 + ch - '0';",
 "v42_rassoc": "    entry = entry + (ch - '0') * 10;",   # WRONG semantics — skip? keep as state probe only if size ok
 "v43_swapmul": "    entry = 10 * entry + (ch - '0');",
 "v44_subfirst": "    entry = entry * 10 - '0' + ch;",
 "v45_lits": "    entry = entry * 10 + (ch - 48);",
 "v46_noparen": "    entry = (entry * 10 + ch) - '0';",
 "v47_s16cast": "    entry = (s16)(entry * 10) + (s16)(ch - '0');",
 "v48_u16cast": "    entry = (s16)(entry * 10 + (u16)(ch - '0'));",
 "v49_twoexpr": "    ch = ch - '0';\n      entry = entry * 10 + ch;",
 "v50_u8sub": "    entry = entry * 10 + (u8)(ch - '0');",
}
BASE = """    n = *num_cnt;
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

import os, subprocess
rows = []
for name, stmt in sorted(V.items()):
    body = BASE % stmt
    src = G.HEAD + G.CHAMP_FOOT % body
    rc, o, err = G.compile_variant(name, src)
    if rc != 0:
        print(f"{name:14} COMPILE_FAIL {err.strip().splitlines()[-1] if err else ''}"); continue
    sz = G.fn_size(o)
    sc = G.score_offline(o)
    fp = G.fingerprint(G.disasm(o))
    print(f"{name:14} sz={sz} raw={('%.5f'%sc) if sc else None} {fp}")
