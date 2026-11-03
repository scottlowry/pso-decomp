#!/bin/bash
# setup_v3_rounds.sh — stage rotation-state seed kits for visit-3 perm rounds
set -u
KIT=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TRaderMapCore_801FA6CC
PERM=$KIT/perm
cd "$KIT" || exit 1

# 1) archive visit-1/2 harvests (already ranked under calibrated harness)
for d in "$PERM"/output-*; do
  [ -d "$d" ] || continue
  base=$(basename "$d")
  mv "$d" "$PERM/v12-$base"
done

# 2) seed dirs
for pair in "s15:q15_useflip" "s16:q16_m19c_above" "s09:q09_above_begin"; do
  tag=${pair%%:*}; f=${pair##*:}
  D=$KIT/perm_$tag
  mkdir -p "$D"
  cp "$PERM/target.o" "$PERM/target.s" "$PERM/compile.sh" "$PERM/settings.toml" "$PERM/harvest_rank.py" "$D/"
  cp "$KIT/$f.c" "$D/base.c"
  # seed compile sanity (must build; intentionally NOT champ-identical)
  ( cd "$D" && bash compile.sh base.c -o base_direct.o >/dev/null 2>&1 \
      && echo "$tag: seed compile OK" || echo "$tag: SEED COMPILE FAIL" )
done

# 3) round runner template (cd into dir: fork writes output-*/ into CWD)
cat > "$KIT/run_round_v3.sh" <<'RS'
#!/bin/bash
# usage: run_round_v3.sh <permdir> <cap> <jobs> <log>
D=$1; CAP=$2; J=$3; LOG=$4
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TRaderMapCore_801FA6CC
cd "$K/$D" || exit 1
PATH="/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/binutils:$PATH" \
  /usr/bin/timeout "$CAP" /Users/scott/Hermes/tools/decomp-permuter/.venv/bin/python \
  /Users/scott/Hermes/tools/decomp-permuter/permuter.py . \
  --better-only --stop-on-zero --stack-diffs -j "$J" > "$LOG" 2>&1
echo "exit=$? cap=${CAP}s jobs=${J}" >> "$LOG"
RS
chmod +x "$KIT/run_round_v3.sh"
echo setup-done
