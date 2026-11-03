#!/usr/bin/env python3
"""port_candidate.py — splice a permuter harvest's dispatch_chunk_polygon_list
definition (signature..closing brace, incl. head decls) into the repo file on the
current branch, verbatim. Usage: python3 port_candidate.py <output-dir>
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f7"
TU = os.path.join(REPO, "src/pso/unk/text_803E2D70.cpp")
FN = "dispatch_chunk_polygon_list"

def extract_fn(text):
    m = re.search(r"void\s+" + FN + r"\s*\([^)]*\)\s*\{", text)
    if not m:
        sys.exit("NO-SIG in candidate")
    start = m.start()
    i = m.end() - 1
    depth = 0
    while i < len(text):
        c = text[i]
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[start:i+1]
        i += 1
    sys.exit("UNBALANCED candidate")

def main():
    src = open(os.path.join(sys.argv[1], "source.c")).read()
    body = extract_fn(src)
    repo = open(TU).read()
    # regex per skill law: signature .. newline-closing brace, \s* tolerant
    pat = re.compile(r"void\s+" + FN + r"\s*\([^)]*\)\s*\{.*?\n\}", re.S)
    hits = list(pat.finditer(repo))
    # pick the DEFINITION (body contains a '{' after sig; decl ends with ';')
    defs = [h for h in hits if "{" in h.group(0)]
    if len(defs) != 1:
        sys.exit(f"DEF-AMBIGUOUS: {len(defs)}")
    out = repo[:defs[0].start()] + body + repo[defs[0].end():]
    open(TU, "w").write(out)
    print(f"PORTED {sys.argv[1]} -> {TU} ({len(body)} bytes fn-def)")

if __name__ == "__main__":
    main()
