---
issue_id: ISSUE-20260427-001
title: "Task 4.4 iter 2 — LSTM ChEMBL pretrain on Cheaha"
opened_at: 2026-04-27T06:00:00Z
opened_by: jakechen
priority: high
age_bumps: 0
last_bumped_at: 2026-04-27T06:00:00Z
status: open
owner: executor
related_task: "Task 4.4"
---

# Task 4.4 iter 2 — LSTM ChEMBL pretrain on Cheaha

**ID:** `ISSUE-20260427-001`  ·  **Priority:** high  ·  **Owner:** executor  ·  **Status:** open
**Related task:** Task 4.4  ·  **Iteration:** 2  ·  **Compute target:** Cheaha (NOT L0)

## Problem statement
Iter 1 produced PHGDH potency-bucket SMILES files only. The actual LSTM pretrain (Fan Li 2026 CLM) was deferred. Iter 2 retargets pretrain from L0 M4 Pro to Cheaha A100 (better fit, frees L0). Three sbatch jobs in sequence (setup -> smoke -> full) driven by an idempotent state-machine executor.

## Plan
See `project-state/learning_notes/Task-4.4-iter2.md`.

## Executor
`/Users/jakeclaw/workers/bin/task_4_4_lstm_cheaha.sh` (registered for Task 4.4 stage E)
State file: `project-state/aim4_clm_state.json`
Convenience entry: `/Users/jakeclaw/workers/bin/start_lstm_chembl_training.sh`

## Attempts tried (chronological — append, never edit)

| When (UTC) | Actor | Approach | Outcome | Evidence |
|---|---|---|---|---|
| 2026-04-27T06:36:29Z | start_lstm_chembl_training | red | Job 38296587 failed on Cheaha during setup stage (rsync / sbatch error) | - |
| 2026-04-27T06:36:10Z | submit_setup | yellow | Submitted Cheaha setup job 38296589 (express, env build + ChEMBL extract) | - |
| 2026-04-27T06:35:59Z | setup_failed | red | Setup job 38296587 -> FAILED; see ~/jobs/aim4_clm/logs/clm_setup_38296587.err on cheaha | - |
| 2026-04-27T06:26:14Z | submit_setup | yellow | Submitted Cheaha setup job 38296587 (express, env build + ChEMBL extract) | - |
| 2026-04-27T06:25:01Z | submit_setup | red | sbatch returned no jobid | - |
| 2026-04-27T06:00:00Z | jakechen+claude | Wrote iter 2 plan, executor, sbatch chain, registry patch | yellow | files committed; no submission yet |

