#!/opt/homebrew/bin/python3.14
"""gen_probes_v3.py — build slwi/add def-site probe variants from base.c (champ mirror).
Each probe: a labeled edit around `f32 *tbl = lbl_804C87B4[mode];` (filler/comma/position/temp)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = open(f"{HERE}/base.c").read()
TBL = "    f32 *tbl = lbl_804C87B4[mode];\n"
assert BASE.count(TBL) == 1

def sub(old, new, s=None):
    s = s if s is not None else BASE
    assert s.count(old) == 1, f"anchor not unique: {old[:50]!r}"
    return s.replace(old, new)

P = {}
# control
P["q00_ctrl"] = BASE
# second dead self-assign fillers around def site (existing champ filler = m_19c after uses)
P["q01_fill_unk18_before"] = sub(TBL, "    state.unk18 = state.unk18;\n" + TBL)
P["q02_fill_unk18_after"] = sub(TBL, TBL + "    state.unk18 = state.unk18;\n")
P["q03_fill_newvar_before"] = sub(TBL, "    new_var = new_var;\n" + TBL)
P["q04_fill_color_before"] = sub(TBL, "    color = color;\n" + TBL)
P["q05_fill_mode_before"] = sub(TBL, "    mode = mode;\n" + TBL)
# comma-def (D80 precedent: tbl = (0, &sym))
P["q06_comma_arr"] = sub(TBL, "    f32 *tbl = (0, lbl_804C87B4)[mode];\n")
P["q07_comma_idx"] = sub(TBL, "    f32 *tbl = lbl_804C87B4[(0, mode)];\n")
P["q08_comma_full"] = sub(TBL, "    f32 *tbl = (0, lbl_804C87B4[mode]);\n")
# position rotation of def site
P["q09_above_begin"] = sub("    begin_effect_render__13TParticleCtrlFv();\n" + TBL,
                           TBL + "    begin_effect_render__13TParticleCtrlFv();\n")
P["q10_above_color"] = sub("    color = -1;\n    begin_effect_render__13TParticleCtrlFv();\n" + TBL,
                           TBL + "    color = -1;\n    begin_effect_render__13TParticleCtrlFv();\n")
P["q11_above_stor"] = BASE.replace(TBL, "").replace("    state.rot = 0;\n", TBL + "    state.rot = 0;\n")
# named temp / split decl / inline
P["q12_named_idx"] = sub(TBL, "    s32 mi = mode;\n    f32 *tbl = lbl_804C87B4[mi];\n")
P["q13_decltop_defer"] = sub("    u32 new_var;\n", "    u32 new_var;\n    f32 *tbl;\n").replace(TBL, "    tbl = lbl_804C87B4[mode];\n")
P["q14_inline"] = BASE.replace(TBL, "").replace("state.x = tbl[2]", "state.x = lbl_804C87B4[mode][2]").replace("state.y = tbl[3]", "state.y = lbl_804C87B4[mode][3]").replace("state.x = tbl[0]", "state.x = lbl_804C87B4[mode][0]").replace("state.y = tbl[1]", "state.y = lbl_804C87B4[mode][1]")
# consumer order flip on tbl uses
P["q15_useflip"] = sub("    state.x = tbl[2] + (f32)lbl_804C87E4[1].x;\n    state.y = tbl[3] + (f32)lbl_804C87E4[1].y;\n",
                       "    state.y = tbl[3] + (f32)lbl_804C87E4[1].y;\n    state.x = tbl[2] + (f32)lbl_804C87E4[1].x;\n")
# filler BEFORE begin (m_19c moved above tbl def)
_tmp = sub(TBL + "    state.x = tbl[2]", TBL + "    self->m_19c = self->m_19c;\n    state.x = tbl[2]")
P["q16_m19c_above"] = _tmp.replace(
    "    self->m_19c = self->m_19c;\n    set_default_alpha_blend__Fv();",
    "    set_default_alpha_blend__Fv();")
# double filler sandwich
P["q17_sandwich"] = sub(TBL, "    new_var = new_var;\n" + TBL + "    color = color;\n")


# v3b: second dead self-assign fillers of the SAME family as the champ winner,
# placed directly at the slwi/add def seam (above and below TBL), using f32 member
P["q18_fill_m174_before"] = sub(TBL, "    self->m_174 = self->m_174;\n" + TBL)
P["q19_fill_m174_after"] = sub(TBL, TBL + "    self->m_174 = self->m_174;\n")
P["q20_fill_a_before"] = sub(TBL, "    a = a;\n" + TBL)
P["q21_fill_b_after"] = sub(TBL, TBL + "    b = b;\n")

for name, src in P.items():
    if src == BASE and name != "q00_ctrl":
        print(f"{name}: NO-OP edit, skipped"); continue
    open(f"{HERE}/../{name}.c", "w").write(src)
    print(name, "written")
