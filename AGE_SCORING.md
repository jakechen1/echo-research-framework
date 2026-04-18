# AGE Scoring — Refined (2026-04-18)

**A.G.E.** is the reverse-NIH assessment axis for each PLEASER iteration close.
All three axes use the same 1–9 scale: **9 = exceptional, 5 = average (50th
percentile), 1 = failing**. This replaces the informal AGE used before
Apr 18 2026.

## Shared bucket scheme (reverse NIH)

| Score | Meaning                                | Percentile vs 7-day baseline |
|------:|----------------------------------------|------------------------------|
|   9   | exceptional — top 5 %                  | > 95th                      |
|   8   | excellent — top 10 %                   | 90–95th                     |
|   7   | very good — top 20 %                   | 80–90th                     |
|   6   | above average — top 33 %               | 67–80th                     |
|   5   | average (±5 % margin)                  | 45–55th                     |
|   4   | below average — bottom 33 %            | 33–45th                     |
|   3   | poor — bottom 20 %                     | 20–33th                     |
|   2   | very poor — bottom 10 %                | 10–20th                     |
|   1   | failing — bottom 5 %                   | < 10th                      |

The margin-of-error band (±5 %) guarantees a 5 for anything within ±5 %
of baseline — prevents noise from rewarding or penalising us unfairly.

## A — Achievement (output document quality + quantity)

Baseline = mean daily output over the **prior 7 days** of the same
iteration/task class.

Components (weighted equally):
1. **Document count** — new or modified files in: `~/wiki/**/*.md`,
   Box (via `BOX_FOLDERS.md` log), GitHub commits to `phgdh-scavenger` repo.
2. **Total length added** — sum of characters added to wiki/docs (not
   counting auto-generated templates).
3. **Curated link count** — `[[wikilink]]` count added **that resolve**
   to an existing page (broken links don't count).
4. **Artifact count** — figures (`.png`), data tables (`.tsv`, `.jsonl`),
   code files (`.py`, `.sh`).

Each component scored against baseline using the bucket scheme, then
averaged (arithmetic mean, rounded to nearest integer).

## G — Growth (skill evolution vs baseline)

Baseline = skill-surface snapshot from 7 days ago. Growth % =
`(current_skill_size − baseline_size) / baseline_size × 100`.

Skill surface is measured by:
- Total byte count of `skills/**/*.{md,py,sh}`
- Count of distinct skills (`skills/*/SKILL.md`)
- Count of new scripts under `workers/bin/`

| Growth % (positive) | Score |
|---------------------:|------:|
|  > 50 %              |   9   |
|  33–50 %             |   8   |
|  20–33 %             |   7   |
|  10–20 %             |   6   |
|   ~1 % (±5 % margin) |   5   |
| −10 to −5 %          |   4   |
| −20 to −10 %         |   3   |
| −33 to −20 %         |   2   |
| < −33 %              |   1   |

Negative growth ≈ skills shrinking (deletions, simplifications). Not
always bad, but scored as such — reviewer reads context.

## E — Effort (CPU + GPU utilisation vs 7-day baseline)

Baseline = mean CPU + GPU utilisation over the prior 7 days during
active work hours.

Measured by `utilization_sampler.py` every 60 s:
- **W0 CPU**: sum of `%CPU` for python/node/ollama/worker procs
  divided by core count, averaged over the iteration window.
- **L0 GPU**: powermetrics `GPU HW active residency` if available,
  else proxy = `1.0` when any Ollama model is loaded (running), `0.0`
  otherwise, averaged over the window.

| Average utilisation | Score | Meaning       |
|--------------------:|------:|---------------|
|  > 95 %             |   9   | exceptional   |
|  85–95 %            |   8   | excellent     |
|  67–85 %            |   7   | very good     |
|  50–67 %            |   6   | above average |
|  45–55 %            |   5   | average       |
|  33–45 %            |   4   | below average |
|  20–33 %            |   3   | poor          |
|  10–20 %            |   2   | very poor     |
|  <10 % (idle)       |   1   | failing       |

The 5-bucket is anchored at 50 % and fuzzy-bounded on both sides (the
45 %/55 % edges), matching the 1-% margin rule for G.

## Invocation

- On iteration close: `skills/age-scoring/scripts/age_score.py --task "Task X.Y"`
- Writes `project-state/age_scores/<task>-iter<N>.json`
- `report_builder.py --level L3` consumes it for the Assessment section
- Dashboard renders a rolling AGE heatmap on Project Status tab

## Baselines

Refreshed nightly at 03:00 by `baseline_refresh.sh`:
`project-state/age_baselines/{achievement,growth,effort}.json`.
