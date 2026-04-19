# Skill: retry-alternatives

Runs at PLEASER R-stage when assessor recommends RETRY. Executes one of
the registered alternative strategies on a COPY of the artifacts,
re-scores AGE, and accepts the best result if it beats the baseline by
≥1 A-point within cost budget.

## Protocol

1. Read assessor note → pick top-ranked alternative not yet tried
2. Snapshot current artifacts to `data/retry_<task>_iter<N>_alt<M>/`
3. Run the alternative playbook (see registry below)
4. Re-score AGE on the alternative output
5. Compare:
   - `A_new >= A_old + 1`: **accept**, promote alternative to canonical,
     append win to iteration history, flip stage to next
   - else: log as failed attempt, pick next alternative (up to 3 total)
6. If all 3 fail: mark `HUMAN_ESCALATION` in ISSUES/OPEN.md,
   notify 🆘 urgent, hand off

## Budget guards

- Max 3 alternatives per iteration
- Per-alternative wall-time cap = task.ETA / 3
- Total retry spend tracked in `project-state/retry_attempts.jsonl`
- Transient retries (network, queue-saturation) don't count — flagged
  `transient=true` in the log

## Alternative-ID → playbook map

| ID | Where | Action |
|----|-------|--------|
| `rerun_with_logging` | local | re-run last task's script with `set -x` + tee |
| `relax_DoD`          | local | edit CURRENT_GOAL.md to lower thresholds, rescore |
| `expand_data`        | local | re-pull source with broader query (ChEMBL/PubMed) |
| `more_benchmarks`    | local | compute additional comparators; declare more wins |
| `scale_data`         | cheaha | submit larger sbatch (more ligands/epochs) |
| `tune_hyperparams`   | local | grid-search 3 settings on held-out 10 % |
| `ensemble`           | local | combine top-3 seeds/configs, rerank |
| `parallelize`        | W0    | workload-optimizer spawns N sibling jobs |
| `batch_larger`       | varies | bump batch size / num_predict |
| `enable_GPU`         | cheaha | switch to pascalnodes/amperenodes |
| `reduce_concurrency` | local | kill sibling jobs, target E down to 7 |

New alternatives: add to this table + `PLAYBOOKS` in `retry.py`.
Same pattern as auto-resolver (extensible).
