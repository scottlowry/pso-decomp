import re
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f8"
D = REPO + "/tools/perm-tests/f8_TObjPlayer_801D4368"
src = open(REPO + "/src/pso/unk/text_801D40D4.cpp").read()
m = re.search(r"s32 TObjPlayer__sub_801D4368\(TObjPlayer \*arg0\) \{.*?\n\}", src, re.S)
body = m.group(0).replace("TObjPlayer *arg0", "void *arg0")
for a, b in [
    ("((TObjPlayer *)down)->get_owner_if_alive()", "get_owner_if_alive__10TObjPlayerFv(down)"),
    ("((TObjPlayer *)down_2)->get_owner_if_alive()", "get_owner_if_alive__10TObjPlayerFv(down_2)"),
    ("((TObjPlayer *)down_3)->get_owner_if_alive()", "get_owner_if_alive__10TObjPlayerFv(down_3)"),
    ("((TObjPlayer *)down_4)->get_owner_if_alive()", "get_owner_if_alive__10TObjPlayerFv(down_4)"),
    ("((TObjPlayer *)obj)->sort_by_key()", "sort_by_key__10TObjPlayerFv(obj)"),
    ("((TObjPlayer *)down_4)->set_field_1c((s32)rec_3[1])", "set_field_1c__10TObjPlayerFl(down_4, (s32)rec_3[1])"),
    ("NULL", "0"),
]:
    body = body.replace(a, b)
assert "TObjPlayer *)" not in body
head = open(D + "/base.c").read().split("s32 TObjPlayer__sub_801D4368")[0]
open(D + "/base.c", "w").write(head + body + "\n")
print("base.c re-rooted to r3 champ")
