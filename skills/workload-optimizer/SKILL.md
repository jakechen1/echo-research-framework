# Skill: workload-optimizer

Self-evolving workload autoscaler. Reads AGE scores + live utilization +
queue depth, then places the next chunk of work where it does the most
good. Goal: drive **E → 9** (utilization) and **A → 9** (output) in
balanced fashion, without flapping.

## Decision matrix (every 15 min)

| Signal                              | Action                                 |
|-------------------------------------|----------------------------------------|
| E < 4 and local headroom ≥ 30 %     | Spawn **local expansion job** (L0 or W0) |
| E ≥ 4 **and** A < 4 (busy, slow)    | **Offload to Cheaha** — throughput problem |
| E ≥ 7 and A ≥ 7                      | No-op — healthy                        |
| E ≥ 9 sustained 2 ticks              | Backoff: pause next expansion          |
| Any job running > 2 h without progress | Kill + mark HUMAN_REQUIRED            |

**Signals used**
- `project-state/age_scores/<task>-iterN.json` — latest A/G/E
- `project-state/utilization.jsonl` — last 5 min mean of L0 GPU + W0 CPU
- `ps aux` + `squeue -u jakechen` — live concurrency
- `resolver_actions.jsonl` — avoid thrashing recently-failed playbooks

## Action registry

### Local-expansion actions (increase E)

| id | Host | Cost | Helps |
|----|------|------|-------|
| `L0_wiki_interlink_batch` | L0 GPU | 5-10 min | wiki interlinking, A↑ |
| `L0_smiles_curation`      | L0 GPU | 15 min  | clean CheMBL SMILES, A↑ |
| `W0_scaffold_cluster`     | W0 CPU | 2 min   | Task 2.4 prep, A↑ |
| `W0_tanimoto_matrix`      | W0 CPU | 3 min   | novelty scoring, A↑ |
| `W0_qed_lipinski_filter`  | W0 CPU | 1 min   | synthesis filter, A↑ |
| `W0_pubmed_sweep_topic`   | W0 CPU | 2 min   | Aim 3 expansion |
| `W0_more_pdbs`            | W0 CPU | 1 min   | Aim 3 structures |

### Cheaha-offload actions (when A low but E high)

| id | Where | Cost |
|----|-------|------|
| `cheaha_vina_top20`      | Cheaha express | ~20 min |
| `cheaha_vina_top500`     | Cheaha short   | ~4 h    |
| `cheaha_md_rescore_top10`| Cheaha gpu     | ~2 h    |

## Self-evolution (planned)

- `workload_policy.json` tracks (action_id → recent AGE delta)
- Actions with positive AGE delta get weighted-higher next tick
- Actions with negative delta cooldown 1 h
- TODO: UCB1 bandit over action registry

## Concurrency limits

- Max **3 concurrent local expansion jobs** (W0 + L0)
- Max **1 Cheaha submission per 15-min tick**
- Any action in cooldown < 30 min is skipped
- Kill-switch: `/tmp/phgdh_optimizer_pause` file halts all auto-dispatch

## State files

- `project-state/workload_actions.jsonl` — audit trail per dispatch
- `project-state/workload_policy.json`   — per-action cooldowns + weights
- `/tmp/phgdh_optimizer_status.json`     — current decision for dashboard
