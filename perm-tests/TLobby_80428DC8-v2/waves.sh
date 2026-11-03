#!/bin/bash
# Wave runner: rotation-state seeded rounds, 2 at a time, then --stack-diffs variants.
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2
{
  bash "$K/run_round.sh" rS3v44 1500 &
  P1=$!
  bash "$K/run_round.sh" rS3w04 1500 &
  P2=$!
  wait $P1; wait $P2
  echo "=== WAVE1-DONE"
  bash "$K/run_round.sh" rS2v10 1200 &
  P3=$!
  bash "$K/run_round.sh" rS1v41 1200 &
  P4=$!
  wait $P3; wait $P4
  echo "=== WAVE2-DONE"
  bash "$K/run_round.sh" rS3v44_stack 600 --stack-diffs &
  P5=$!
  bash "$K/run_round.sh" rS2v10_stack 600 --stack-diffs &
  P6=$!
  wait $P5; wait $P6
  echo "=== ALL-WAVES-DONE"
} 2>&1 | tee "$K/waves.log"
