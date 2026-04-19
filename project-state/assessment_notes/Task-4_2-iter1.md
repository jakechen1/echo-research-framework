# Assessment — Task 4.2 iter 1
*2026-04-19T04:41:11+00:00*

## Scores vs target

| Axis | Actual | Target | Diagnosis |
|------|-------:|-------:|-----------|
| A | 1 | 7+ | completion=0.0%, SOTA=0.0 |
| G | 7 | — | delta_pct=8011600.0 |
| E | 2 | 6+ | combined=14.09% |

## Recommendation: **RETRY** — A=1, try: rerun_with_logging

## Alternatives (ranked)

1. **`rerun_with_logging`** (cost 1) — Re-run failing step with set -x + tee logs; fix DoD item
2. **`relax_DoD`** (cost 1) — Lower size-bound or dedup more aggressively; iter 1.x
3. **`parallelize`** (cost 1) — Fan-out N sibling jobs (respect parallelism guidance)

## Benchmark comparator categories

- ⚪ `ligands_docked` — baseline: 20 / 20
- ⚪ `novel_scaffolds` — baseline: ≥3 distinct Murcko in top-10 by ΔG
- ⚪ `score_correlation` — baseline: Spearman(ΔG, pChEMBL) < -0.3
- ⚪ `ranked_output` — baseline: CSV + scatter PNG + wiki page
