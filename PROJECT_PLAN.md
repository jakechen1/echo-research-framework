# PHGDH Autonomous Drug-Discovery Project — Plan v2

*Last reorganized: 2026-04-18. Project target: novel allosteric/RBD-site
PHGDH modulators for neurodegeneration (Alzheimer's focus).*

## 1. Architecture (3 tiers)

| Tier | Role | Substrate |
|------|------|-----------|
| 0 | OS-level daemons (no LLM) | LaunchDaemons + cron + `scheduler_loop.sh` |
| 1 | Autonomous agents | jakeclaw (Gemma 4 26B @ L0), qwenclaw (Qwen 3.5 @ W0), Hermes |
| 2 | Human consultant | Claude — design + unstick only, minimize cost |

**Hosts:** L0 = `192.168.68.200` (inference). W0 = `192.168.68.201` (agents, dashboard, scheduler). Cheaha = UAB HPC via SSH alias `cheaha` (user=jakechen).

## 2. 5 Aims

| Aim | Title | Status | Completed tasks |
|-----|-------|--------|-----------------|
| **1** | Automated data pipeline + enrichment | 🟡 in progress | 1.1 |
| **2** | Computational analysis of PHGDH inhibitors | ✅ complete | 2.1, 2.2, 2.3 |
| **3** | Literature synthesis & knowledge graph | 🟡 in progress | 3.1 |
| **4** | Structure-based virtual screening on Cheaha | 🟡 active | 4.1 |
| **5** | Scientific deliverables (paper, slides, wiki) | ⚪ pending | — |
| **∞** | **Infrastructure** (cross-cutting) | ✅ complete | liveness, notifier, AGE, resilience, auto-resolver, plan-sync |

## 3. PLEASER iteration loop (per task)

7 stages, single-char codes: **P** L E A S **X** R (X = eXpense; see `STAGE_CODES.md`).
One active task at a time. AGE scored 1–9 reverse-NIH. Stage-timeout thresholds enforced by liveness → auto-resolver.

## 4. Infrastructure skills built (2026-04-18)

| Skill | Purpose |
|-------|---------|
| `liveness-audit` | 10-channel health monitor every 5 min |
| `age-scoring` | Accuracy + Growth + Expense per iteration vs 7-day baseline |
| `notifier` | Telegram alerts on milestones (dedup + rate-limit + queue) |
| `resilience` | Atomic writes, retry queues, hourly checkpoint, boot recovery, scheduler_loop |
| `auto-resolver` | Self-healing: per-channel playbook + 4-step escalation ladder |
| `plan-sync` | **(new)** Auto-updates BACKLOG completion status from COMPLETED + artifacts |

## 5. Data assets (on W0 `~/.openclaw/workspace/data/`)

- `aim2_top20_inhibitors.csv` — 20 rows, pv ≥ 7, ranked
- `aim2_pdb_binding_sites.json` — 5 Å residue shells per PDB ligand
- `aim3_structures/` — 4NJN, 6RIH, 6PLF, 7S3R, 2G76 (PDB files)
- `aim3_pubmed_phgdh_allosteric.json` — 29 papers 2024–2026
- `aim4_smiles/smiles_potency_sorted.tsv` — 1011 molecules
- `aim4_docking_results/` — Vina dock poses (currently 1; scaling to 20)

## 6. Key decisions & conventions

- **Publish gate:** PUBLISH-01 — Jake triggers publish, daemons never push
- **Stage codes:** never rename `X` (eXpense)
- **Scheduling:** macOS SSH can't install LaunchAgents/cron → scheduler_loop nohup with 3 resurrection paths
- **IPs:** L0=.200, W0=.201 (NOT .133/.134)
- **Cheaha:** SSH alias `cheaha` as user `jakechen`, key `id_ed25519`, no VPN for login node

## 7. Next 48 h

1. Task 4.2 — scale Vina to top-20 inhibitors × 6RIH K4T pocket
2. Task 1.2 — Hermes data→knowledge enrichment loop
3. Task 5.2 — Repo README + pipeline diagram
4. Move L2 report cron 17:00 → 23:00 (needs user-terminal sudo)
5. User-gated publish of 3 wiki drafts + 20 concept-hub stubs

## 8. Automatic plan maintenance

Starting 2026-04-18, `plan-sync` runs:
- **Every hour** via scheduler_loop — scans COMPLETED.md + artifact files,
  auto-updates BACKLOG.md task statuses (pending → DONE when evidence found)
- **At every R-stage exit** — post_r_watchdog calls plan-sync before promoting
- Writes `project-state/PLAN_STATUS.md` — a one-page human-readable dashboard
- Telegram 📋 notice when any status flip occurs

No more stale plans.
