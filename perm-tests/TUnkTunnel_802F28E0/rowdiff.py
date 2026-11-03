import json, sys, itertools
d = json.load(open(sys.argv[1]))
def sym(side):
    for s in d[side]["symbols"]:
        if isinstance(s, dict) and "run_task" in str(s.get("name", "")):
            return s
o, n = sym("left"), sym("right")
rows_o = o.get("instructions", [])
rows_n = n.get("instructions", [])

def fmt(r):
    if r is None:
        return "<none>"
    i = r.get("instruction")
    if not i:
        return f"<{r.get('kind', '?')}: {str(r)[:30]}>"
    return str(i.get("formatted") or i.get("text") or i)[:46]

print("orig rows:", len(rows_o), "ours rows:", len(rows_n))
diff = 0
for a, b in itertools.zip_longest(rows_o, rows_n):
    fa, fb = fmt(a), fmt(b)
    if fa != fb:
        diff += 1
        ka = (a or {}).get("kind", "?")
        print(f"O: {fa:48} N: {fb:48} kind={ka}")
print("diff rows:", diff)
