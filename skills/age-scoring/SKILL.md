# Skill: age-scoring

Computes Accuracy/Generalizability/Effort scores (1–9 reverse-NIH) against
rolling 7-day baseline. Used by Assessment (A) stage of every PLEASER
iteration. Spec: `AGE_SCORING.md` at workspace root.

## Scripts
- `scripts/utilization_sampler.py` — every 60 s, samples W0 CPU% and L0 GPU
  residency via powermetrics/ioreg fallback + Ollama `/api/ps`. Writes
  `project-state/utilization.jsonl`.
- `scripts/baseline_refresh.sh` — nightly at 03:00. Rebuilds
  `project-state/age_baselines/{achievement,growth,effort}.json` from the
  last 7 days of telemetry + git log + skill tree.
- `scripts/age_score.py` — computes A, G, E for a given task window.
  Writes `project-state/age_scores/<task>-iter<N>.json`.

## Invocation

```
# At iteration close (called by report_builder.py --level L3):
python3 skills/age-scoring/scripts/age_score.py \
    --task "Task 2.1" --iteration 1 \
    --window-start 2026-04-18T10:00 --window-end 2026-04-18T12:00

# Nightly baseline refresh (cron):
bash skills/age-scoring/scripts/baseline_refresh.sh

# Sampler (every 60 s via LaunchAgent):
python3 skills/age-scoring/scripts/utilization_sampler.py
```

## Dependencies
- `/Users/jakeclaw/.hermes-venv/bin/python` (requests)
- SSH to L0 (192.168.68.200) as jakechen for powermetrics (optional; if
  unavailable, falls back to Ollama `/api/ps` proxy)
- Read access to `~/wiki/`, `~/phgdh-scavenger/`, skill tree
