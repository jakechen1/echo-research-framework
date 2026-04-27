---
task: Task 4.4
iteration: 2
status: in-progress
compute: cheaha (amperenodes, 1x A100 80GB)
issue: ISSUE-20260427-001
---

# Task 4.4 — iteration 2

**LSTM CLM pretrain on Cheaha, replacing iter 1 data-prep stub.**

Iter 1 produced PHGDH potency buckets (`data/aim4_clm/bucket_pv{5..9}.smi`).
Iter 2 trains the upstream pretrain LSTM that iter 3 will fine-tune.

## Pipeline (state machine)

```
P (this) -> L (lit check) -> E.1 setup -> E.2 smoke -> E.3 full -> E.4 retrieve
                              express     express     amperenodes  rsync to W0
```

State at `project-state/aim4_clm_state.json`. Each invocation of
`task_4_4_lstm_cheaha.sh` advances one step (idempotent). PLEASXR
heartbeat at `workers/heartbeats/pleaser_E.ts`.

## How to start (jakeclaw)
> Start the LSTM ChEMBL training job

This invokes `start_lstm_chembl_training.sh` which calls the COO
executor wrapper. Subsequent advancer ticks (every 2 min) progress
the state machine without further user input.

## Outputs
- Checkpoint: `data/aim4_clm/runs/<jobid>/best.pt`
- Vocab: `data/aim4_clm/runs/<jobid>/vocab.json`
- Train log: `data/aim4_clm/runs/<jobid>/train.log`
- Loss curve: `data/aim4_clm/runs/<jobid>/loss.csv`

## See also
- Plan: `project-state/learning_notes/Task-4.4-iter2.md`
- Issue: `wiki/issues/ISSUE-20260427-001-task-4-4-iter-2-lstm-chembl-pretrain.md`
- Cheaha skill: `skills/cheaha-hpc/SKILL.md`
