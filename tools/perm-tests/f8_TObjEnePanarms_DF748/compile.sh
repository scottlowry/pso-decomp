#!/bin/bash
# df748 kit compile.sh — exact ninja mwcc line, candidate wrapped extern "C", OUT default = src.o
IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="${3:-${IN%.c}.o}"
case "$OUT" in /*) ;; *) OUT="$(pwd)/$OUT";; esac
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f8
TMP="$OUT.src.cpp"
printf 'extern "C" {\n' > "$TMP"; cat "$IN" >> "$TMP"; printf '}\n' >> "$TMP"
LINE=$(head -1 /Users/scott/.hermes/profiles/pso-decomp/cache/scratch/df748_cc.txt)
CMD=$(python3 - "$LINE" "$TMP" "$OUT" <<'PY'
import sys, shlex
args = shlex.split(sys.argv[1])
i = args.index('-c'); args[i+1] = sys.argv[2]
j = args.index('-o'); args[j+1] = sys.argv[3]
print(shlex.join(args))
PY
)
cd "$REPO" || exit 1
eval "$CMD"
RC=${PIPESTATUS[0]}
rm -f "$TMP" "$OUT.d"
exit $RC
