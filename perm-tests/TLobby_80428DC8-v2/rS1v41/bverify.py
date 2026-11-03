import re, subprocess, sys
SYM = "TLobby__sub_80428DC8"

def words(obj, dr=False):
    a = ["/opt/homebrew/bin/powerpc-eabi-objdump", "-d"] + (["-r"] if dr else []) + [obj]
    txt = subprocess.run(a, capture_output=True, text=True).stdout
    lines = txt.splitlines()
    try:
        i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    except StopIteration:
        return None
    out = []
    for l in lines[i+1:]:
        if l.startswith(SYM) or "<" in l and ">" in l and ":" in l and not l[0].isspace():
            break
        m = re.match(r"\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} ){2,8})", l)
        if m:
            out.append(m.group(1).replace(" ", "").rstrip())
        if re.search(r"\bblr\b", l):
            break
    return out

base = words(sys.argv[1])
repo = words(sys.argv[2])
print("base n=", len(base) if base else None, " repo n=", len(repo) if repo else None)
if not base or not repo:
    sys.exit("extract fail")
n = min(len(base), len(repo))
diff = [k for k in range(n) if base[k] != repo[k]]
print("first diffs:", diff[:5])
for k in diff[:3]:
    print(k, base[k], repo[k])
if not diff and len(base) == len(repo):
    print("BYTES-IDENTICAL")
    sys.exit(0)
sys.exit(1)
