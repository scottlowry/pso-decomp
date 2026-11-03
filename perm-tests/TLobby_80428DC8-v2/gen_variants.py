#!/usr/bin/env python3.14
"""Rotation-state enumeration for TLobby__sub_80428DC8 visit-2.
Generate size-preserving-class topology variants of the champ block-2,
compile each via kit compile.sh (offline, zero repo builds), fingerprint
the r3/r4/r6/r7 home state of the loop pool, cluster distinct states.
"""
import re, subprocess, os, sys, json

KIT = os.path.dirname(os.path.abspath(__file__))
HEAD = open(f"{KIT}/base.c").read().split("void TLobby__sub_80428DC8")[0]
CHAMP_FOOT = """void TLobby__sub_80428DC8(s16 entry, s16 slot, u8 *text, s16 *cnt, s16 *num_cnt)
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
%s
  }
}
"""

BODY = {  # block-2 interior (the loop-state region) per variant
 "v00_champ": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v01_n_e_i": """    n = *num_cnt;
    entry = 0;
    i = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v02_i_n_e": """    i = 0;
    n = *num_cnt;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v03_i_e_n": """    i = 0;
    entry = 0;
    n = *num_cnt;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v04_e_n_i": """    entry = 0;
    n = *num_cnt;
    i = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v05_e_i_n": """    entry = 0;
    i = 0;
    n = *num_cnt;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v06_comm": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = entry + ch;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v07_incr_head": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      i++;
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v08_forform": """    n = *num_cnt;
    entry = 0;
    for (i = 0; (ch = text[i]) != 0; i++)
    {
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v09_dblread": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while (text[i] != 0)
    {
      ch = text[i];
      entry = entry * 10;
      entry = ch + entry;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v10_fold_muladd": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10 + ch;
      entry = entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v11_fold_addsub": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10;
      entry = ch + entry - '0';
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v12_fullfold": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = entry * 10 + (ch - '0');
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
 "v13_fullfold_comm": """    n = *num_cnt;
    i = 0;
    entry = 0;
    while ((ch = text[i]) != 0)
    {
      entry = (ch - '0') + entry * 10;
      i++;
    }

    lobby_net_session_state.ints[n] = entry;
    lobby_net_session_state.fields[slot] = (u8 *) (&lobby_net_session_state.ints[n]);
    *num_cnt = n + 1;""",
}

# decl-order variants: same champ body, rotate local decl order
DECL_PERMS = {
 "v20_d_n_c_i":  "  s16 n;\n  s16 c;\n  char *dest;\n  s16 i;\n  u8 ch;\n",
 "v21_d_i_n_c":  "  s16 i;\n  s16 n;\n  s16 c;\n  char *dest;\n  u8 ch;\n",
 "v22_c_i_n_d":  "  s16 c;\n  s16 i;\n  s16 n;\n  char *dest;\n  u8 ch;\n",
 "v23_i_n_d_c":  "  s16 i;\n  s16 n;\n  char *dest;\n  s16 c;\n  u8 ch;\n",
}

SYM = "TLobby__sub_80428DC8"

def compile_variant(name, src):
    c = f"{KIT}/gen_{name}.c"
    open(c, "w").write(src)
    o = f"{KIT}/gen_{name}.o"
    r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o],
                       capture_output=True, text=True, cwd=KIT)
    return r.returncode, o, r.stderr

def fn_size(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for l in out.splitlines():
        p = l.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

INSN_RE = re.compile(r"^\s+[0-9a-f]+:\s+(?:[0-9a-f]{2} )+\s+([a-z][a-z0-9.]*)\s*(.*)$")

def disasm(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    out = []
    inside = False
    for l in txt.splitlines():
        if f"<{SYM}>:" in l:
            inside = True; continue
        if inside:
            if l.strip().startswith("R_PPC") or not l.strip():
                continue
            m = INSN_RE.match(l)
            if m:
                out.append((m.group(1), m.group(2).split("#")[0].strip()))
            elif "blr" in l:
                break
    return out

def fingerprint(insns):
    """Extract loop-pool state: n-home, i-home, acc-home, mulli inplace, extsh src."""
    st = {}
    # region: from 'lha' reading (r30) to final 'sth r?,0x0(r30)'
    for i, (op, args) in enumerate(insns):
        if op == "lha" and "0x0(r30)" in args:
            st["n_home"] = args.split(",")[0].strip()
        if op == "mulli":
            d, s = [x.strip() for x in args.split(",")[:2]]
            st["acc_home"] = s
            st["acc_temp"] = d
            st["mulli_inplace"] = (d == s)
        if op == "subi":
            d, s = [x.strip() for x in args.split(",")[:2]]
            st["subi"] = f"{d}<-{s}"
        if op == "addi" and "0x1" in args:
            d, s = [x.strip() for x in args.split(",")[:2]]
            if d == s and "i_home" not in st:
                st["i_home"] = d
        if op == "extsh":
            parts = [x.strip() for x in args.split(",")]
            d, s = parts[0], parts[1]
            if s in ("r3", "r4", "r6", "r7") and d == "r0":
                st["extsh_src"] = s
        if op == "sthx":
            st["sthx_src"] = args.split(",")[0].strip()
    return st

def score_offline(obj):
    """raw objdiff single-symbol score vs target.o (calibrated route)."""
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run(["/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/tools/objdiff-cli",
                    "diff", "-1", f"{KIT}/target.o", "-2", obj, SYM,
                    "--format", "json", "-o", p],
                   capture_output=True, text=True,
                   cwd="/Users/scott/Hermes/pso-decomp/pso-decomp-f3")
    try:
        d = json.load(open(p))
    except Exception:
        return None
    finally:
        os.unlink(p)
    for side in ("left", "right"):
        for s in d.get(side, {}).get("symbols", []):
            if isinstance(s, dict) and SYM in str(s.get("name", "")):
                mp = s.get("match_percent")
                if mp is not None:
                    return float(mp)
    return None

results = {}

def run_battery():
    for name, body in BODY.items():
        src = HEAD + CHAMP_FOOT % body
        rc, o, err = compile_variant(name, src)
        results[name] = (rc, o)
    for name, decls in DECL_PERMS.items():
        champ_body_block = CHAMP_FOOT % BODY["v00_champ"]
        src = HEAD + champ_body_block.replace(
            "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n", decls)
        rc, o, err = compile_variant(name, src)
        results[name] = (rc, o)
    print(f"{'variant':16} {'rc':3} {'size':5} {'score':9} fingerprint")
    for name, (rc, o) in sorted(results.items()):
        if rc != 0:
            print(f"{name:16} FAIL")
            continue
        sz = fn_size(o)
        sc = score_offline(o)
        fp = fingerprint(disasm(o))
        print(f"{name:16} {rc:3} {str(sz):5} {('%.5f' % sc) if sc else 'None':9} {fp}")

if __name__ == "__main__":
    run_battery()
