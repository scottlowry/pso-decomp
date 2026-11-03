import re, glob, json, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
hits = []
for s in glob.glob(f"{REPO}/build/GPOE8P/asm/pso/**/*.s", recursive=True):
    txt = open(s).read()
    for m in re.finditer(r"^\.fn ([^,\n]+)[^\n]*\n(.*?)^\.endfn", txt, re.S | re.M):
        name, body = m.group(1), m.group(2)
        slots = []
        for l in body.splitlines():
            if "*/" not in l:
                continue
            ins = l.split("*/", 1)[1].strip()
            mm = re.match(r"stfd f\d+, (0x[0-9a-f]+)\(r1\)", ins)
            if mm:
                slots.append(int(mm.group(1), 16))
        conv = len(re.findall(r"fctiwz", body))
        if conv == 2 and len(slots) == 2 and slots[0] != slots[1]:
            hits.append((s.split("/asm/")[-1], name, [hex(x) for x in slots]))
print(f"corpus hits: {len(hits)}")
rep = json.load(open(f"{REPO}/build/GPOE8P/report.json"))
fm = {}
for u in rep["units"]:
    for f in u.get("functions") or []:
        fm[f["name"]] = f.get("fuzzy_match_percent")
for path, name, slots in hits:
    p = fm.get(name)
    src = os.system(f'grep -rl "{name}" {REPO}/src >/dev/null 2>&1') == 0
    print(f"{name}  slots={slots}  fuzzy={p}  src={'YES' if src else 'no'}  unit={path}")
