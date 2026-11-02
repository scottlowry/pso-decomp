# text_801A3BB8 (fn_801A3BB8) — FALSE-DISPATCH + synthesis proof + FORCEACTIVE trap

**Status at base 535b1afc: DONE.** Report (fresh, restore build): `fuzzy 100.0, code 60/60,
data 1068/1068, complete True`. Unit is linked; manual extern-C spelling (upstream
`add text_801A3BB8 data to source`, 76151fea) pairs the fn row by name. Dispatch #2 was cut
from the pre-screen file; sinit_mine_screen.py confirms DONE.

## Synthesis decode (probe v1, 1 build-free compile)

`tools/perm-tests/text_801A3BB8_sinit/text_801A3BB8.cpp`:

```cpp
#include "types.h"
class TPlyCharData {
public:
    TPlyCharData();      // -> __ct__12TPlyCharDataFv (era row 2835 @0x8007214C)
    ~TPlyCharData();     // -> __dt__12TPlyCharDataFv (era row 2825 @0x80071DFC)
    u8 d[0x41C];         // sizeof == era object size
};
TPlyCharData TPlyCharData__global_character_data;
```

MWCC synthesizes NATIVELY (gate-exact, first try):
- `__sinit_text_801A3BB8_cpp` local, gnm size **0x3c** == symbols.txt `size:0x3C`.
- 15-word body: RAW-WORD 15/15 EQUAL AT LINK — 7/15 positional byte-exact + 8/15
  resolve-at-link class (4x ADDR16 HA/LO, 2x REL24, +2 HA/LO pair on the reg blob), every
  one recomputed from era addresses and word-matched (`v1_wd_proof.txt`; content multiset
  15/15, positional LCS 15/15 — ZERO order residue, cleaner than 69C).
- .bss fragment order exact: [@1 reg 0xC @+0][obj 0x41C @+C] == era DDE0/DDEC.
- .ctors word auto-emitted (R_PPC_ADDR32 -> __sinit). No manual `__declspec(section
  ".ctors")` ref line needed — visit-1 doctrine confirmed.
- All 5 refs = era rows verbatim, bl displacements measured vs disasm (`__register_global_object`
  bl 48 1F 2A 55 @0x801A3BE0 -> 0x80396634 == row 25524 ✓).
- 8B `.mwcats.text` rides the .o (A41C/67F4 family artifact).

## WHY THE SWAP CANNOT LAND ON TODAY'S CONFIG (fleet-relevant trap)

Config `psov3/config.yml` force_active list line ~4541 contains `fn_801A3BB8`.
FORCEACTIVE matches by NAME. Synthesis renames the only global fn to local
`__sinit_text_801A3BB8_cpp` -> linker warns `FORCEACTIVE symbol 'fn_801A3BB8' is either
not a global symbol or doesn't exist. Ignored.` -> dead-strip eats 0x40 bytes of UNRELATED
era text (`__close_console` tail 0x8039637C-3AC + mslsupp head 3AC-3BC; whole image shifts
-64; bl re-targets propagate from 0x8000F770 on) -> `build.sha1` DOL verify FAILS
(ninja rc=1, receipts b_swap.log/dol diff; good_head.dol saved).

**Lesson for the whole sinit family:** a synthesis swap is only safe for units that are NOT
in linked_units/force_active, or must be paired with the config ASK
(rename row 11426 `fn_801A3BB8` -> `__sinit_text_801A3BB8_cpp` scope:local +
re-sync force_active + link_units state in the same commit — config is integrator-side).
69C/67F4 "hold unlinked" resolves this automatically; a LINKED 100% unit must stay manual
until the rename lands. Also: era reg-blob row 45849 `TPlyCharData__global_destructor_registration`
maps to compiler-anon `@1` (jumptable `@NNN` lore class — not nameable from source).

## Verdict

NO repo src change (manual spelling holds 100.0; synthesis swap = DOL break on current
config). Kit parked here; ASK (report-only naming doctrine applies; config edit NOT attempted):
when renaming fn_801A3BB8 -> __sinit_text_801A3BB8_cpp scope:local (precedents 2174/2256/
14846/22209/23145 + 69C row 23312), resync force_active and the swap can land gate-exact
zero-residue at 100% pairing (single-fn unit pairs by position pre-rename too, per swap
report.json: fn row rendered 100% under the synth .o — the only hard break was the
force_active dead-strip cascade, bytes, not pairing).
