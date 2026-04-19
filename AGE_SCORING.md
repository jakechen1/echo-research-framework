# AGE Scoring — Refined v2 (2026-04-18 evening)

**A.G.E.** — reverse-NIH 1-9 per PLEASER iteration. **9 = exceptional, 5 = par, 1 = failing.**

## A — Achievement (completion × quality-vs-SOTA)

Two sub-signals:

1. **Completion** = fraction of `done criteria` in `CURRENT_GOAL.md` / `iteration_state` that are objectively satisfied (artifact exists, size-bound met, sha in git log, etc.)
2. **Quality vs baseline/SOTA** = number of comparator categories where our
   output beats a documented benchmark (from `project-state/benchmarks.json`).

| Score | Meaning | Condition |
|------:|---------|-----------|
| 9 | **SOTA across ALL categories** | 100% complete + beats benchmark in every category |
| 8 | SOTA in **≥75 %** of categories | 100% complete + strong majority |
| 7 | SOTA in **≥50 %** of categories | 100% complete + clear majority |
| 6 | SOTA in **≥25 %** of categories | 100% complete + at least some wins |
| 5 | **100 % complete, par with baseline** | all criteria met, quality = benchmark |
| 4 | 75–99 % complete OR below par | sub-par, near miss |
| 3 | 50–74 % complete | partial |
| 2 | 25–49 % complete | mostly missing |
| 1 | < 25 % complete | failing |

Sub-par quality (met tasks but output below baseline) caps at 4.

## G — Growth (skill/code/docs delta vs 7-day baseline)

Unchanged from v1. ±10/20/33/50 % buckets around 5; ±5 % margin is 5.

## E — Effort (utilization vs absolute thresholds)

Anchors exactly as specified:

| Score | Utilization % |
|------:|---------------|
| 1 | **5 %** |
| 2 | **10 %** |
| 3 | **20 %** |
| 4 | **33 %** |
| 5 | **50 %** |
| 6 | **67 %** |
| 7 | **80 %** |
| 8 | **90 %** |
| 9 | **95 %** |

Score = largest anchor not exceeding the measured utilization.
`utilization = (W0 CPU % + L0 GPU %) / 2`.

## Benchmarks file

`project-state/benchmarks.json` declares comparators per task:

```json
{
  "Task 2.2": {
    "categories": ["potency_range", "chemical_diversity", "assay_types"],
    "baseline": {
      "potency_range": "pChEMBL 6-9 (ChEMBL public snapshot 2024)",
      "chemical_diversity": "≥10 scaffolds per 20 molecules",
      "assay_types": "cover IC50 + Ki + EC50"
    }
  },
  "Task 4.1": {
    "categories": ["dock_quality", "pocket_selection", "reproducibility"],
    "baseline": {
      "dock_quality": "≤ -7.0 kcal/mol for known K4T-class",
      "pocket_selection": "K4T-centered box from 6RIH",
      "reproducibility": "public receptor + deterministic seed"
    }
  }
}
```

Each task lists the categories it will be scored against. At A-stage, the
agent sets `sota_wins: [category, ...]` in the task's assessment and
`age_score.py` computes A accordingly.


## v3 update — Cheaha-aware Effort (2026-04-19)

E previously averaged only `(W0 CPU + L0 GPU) / 2`. This was blind to
Cheaha — a 95 % Cheaha array with idle local scored E = 1. Fixed:

```
effective_util = max(w0_cpu_pct, l0_gpu_pct, cheaha_rwi_pct)
score = bucket_utilization(effective_util)
```

where `cheaha_rwi_pct` is **Remote Workload Intensity** computed by
`skills/cheaha-telemetry`:

```
RWI = sum(CPUTimeRAW) / sum(ReqCPUS × Timelimit)   # over last 48 h of our jobs
```

Rationale: RWI = 1 means we fully used every second of CPU we requested
from Slurm. Values <1 mean under-packed jobs (requesting more than consumed).
Capped at 100 % at the sampler level.

`utilization.jsonl` records now carry a 4th field `cheaha_rwi_pct`.
`age_score.score_effort()` picks the max across all three tiers.
