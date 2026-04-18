---
title: "Project Taxonomy & PLEASER Framework"
version: 1.0
date: 2026-04-18
authors: [jakechen]
status: canonical
---

# Project Taxonomy & PLEASER Framework

All agent outputs (PLAN, backlog entries, daily logs, reports) MUST use
this nomenclature. Agents that deviate silently are out-of-spec.

## 1. Nomenclature

### Aims (top-level; up to 4)
Written **Aim 1**, **Aim 2**, …, **Aim 4**.
Each aim is a distinct research direction with its own hypothesis or
engineering target. Every report (L1-L5) references at least one aim.

### Tasks (per aim)
Written **Task X.Y** where X is the aim number and Y is the task number
within that aim.
*Examples: Task 1.1, Task 1.2, Task 2.5.*
Tasks are the unit of PLEASER iteration.

### Subtasks (per task, if decomposition aids planning)
Written **Task X.Y.a**, **Task X.Y.b**, ..
*Examples: Task 2.5.a "filter by docking score", Task 2.5.b "cluster by
scaffold", Task 2.5.c "re-score top 50 with MD".*

### Legacy ID compatibility
The existing G-NNN goal IDs map onto the new taxonomy. Each G-NNN entry
in BACKLOG now carries its Aim + Task code. We keep G-NNN as a stable
identifier for historical traceability; Task codes are the canonical
organizational reference.

## 2. PLEASER — iteration format (7 phases)

Each PLEASER-ONE iteration covers ONE task (Task X.Y) and produces a
structured L3 report with these seven sections:

| # | Letter | Phase | What goes here |
|---|--------|-------|----------------|
| 1 | **P** | **Plan** | Task text, hypothesis or prediction, expected artifacts, success criteria (specific, measurable) |
| 2 | **L** | **Learning** | Prior art + context: relevant wiki pages, recent literature, prior PLEASER iterations. Short bibliography in `[[wikilink]]` form. |
| 3 | **E** | **Execution** | What was actually done. Commands run, who ran them (jakeclaw / qwenclaw / Hermes / cheaha), when. Raw log pointer. |
| 4 | **A** | **Assessment** | NIH-style scores (1-9, 1=best) for Significance, Innovation, Approach + AGE scores (Accuracy, Generalizability, Efficiency) |
| 5 | **S** | **Sharing** | What got published where (Wiki, Box, Telegram, GitHub). Discussion notes from Jake / co-supervisor / collaborators. |
| 6 | **E** | **Expense** | Resource accounting: wall-clock hours, GPU-hours (L0 / Cheaha), Claude API $ spent, tokens used, Telegram msg count. Compare against the planned budget from Phase 1 (Plan). Flag overruns. |
| 7 | **R** | **Resolver** | Escalations invoked (Claude co-supervisor, human expert) + resolutions captured. Any scientific-direction shifts noted here with dated justification. |

**Expense section format:**

```
| Resource      | Planned | Actual | Note                                    |
|---------------|---------|--------|-----------------------------------------|
| Wall-clock    | 1 d     | 0.8 d  | faster than expected                    |
| L0 GPU-hours  | 0.5     | 0.3    | Gemma 4 only touched for a few queries  |
| Cheaha SU     | 0       | 0      | no HPC use this task                    |
| Claude API $  | 0       | 0      | no paid Claude call                     |
| Telegram msgs | 4       | 3      | 1 under (compactor skipped one)         |
```

Under-budget tasks are as noteworthy as over-budget ones — surface both
so Jake can tune planning.

**Artifact references** (commit SHAs, file paths, figure hashes, DOIs)
stay in the Execution section where they are produced — they are part of
"what was done", not a separate accounting category.

## 3. NIH scoring (applies to Assessment phase)

1-9 scale, **1 = exceptional, 9 = poor**. Give score + one-line reason.

| Criterion | Question |
|-----------|----------|
| Significance | Does this task advance an important problem? |
| Innovation | Is the approach novel, or standard? |
| Approach | Is the method sound and feasible? |
| Investigator | Does the team have capacity? (usually 1-2 for local team) |
| Environment | Infrastructure adequate? (score L0/W0/Cheaha) |

**Composite Overall Impact** = weighted mean, usually the user reports it.

## 4. AGE scoring (applies to Assessment phase)

**IMPORTANT:** AGE uses the **REVERSE of the NIH scale** — higher is better.

| Letter | Criterion | Question |
|--------|-----------|----------|
| A | **Accuracy** | Did outputs correctly represent reality? (computational accuracy vs ground truth or literature benchmarks) |
| G | **Generalizability** | Will the finding transfer beyond this instance? (other targets, datasets, conditions) |
| E | **Efficiency** | Did resource use (time, compute, tokens) match the value produced? |

### AGE rubric (1-9, 9 = best)

| Score | Percentile | Interpretation |
|-------|-----------|----------------|
| **9** | top 5% | Exceptional. Outstanding in every respect. |
| **8** | top 10% | Excellent. Notably strong. |
| **7** | top 20% | Very good. Clearly above average. |
| **6** | top 33% | Good. Above average. |
| **5** | 50% (median) | **Satisfactory.** Meets expectations, no more no less. |
| **4** | bottom 33% | Below average. Noticeable weakness. |
| **3** | bottom 20% | Poor. Significant weakness. |
| **2** | bottom 10% | Very poor. Fundamental weakness. |
| **1** | bottom 5% | Unacceptable. Fails in every respect. |

Compare to the NIH rubric (§3) which runs the opposite direction
(1 = exceptional, 9 = poor). Be careful to not mix scales when writing.

## 5. Iteration tracking (required for L3+)

Every PLEASER report at **L3 or above** MUST include:

- **Task code** (e.g., `Task 2.1`)
- **Iteration number** (how many PLEASER cycles on this Task)
- **Current PLEASER stage** (which of the 7 phases the iteration is in)

These are tracked in `project-state/iteration_state.json`:
```
{
  "task": "Task 2.1",
  "iteration": 1,
  "stage": "E",
  "started": "2026-04-18T10:00",
  "history": [{"stage":"P","at":"..."},{"stage":"L","at":"..."}]
}
```

`promote_next_goal.sh` resets iteration to 1 when the Task changes.
Reopening an already-completed Task (e.g., revisiting with new data)
increments iteration to 2, 3, ...

## 6. Artifact audit requirement

When any report references a file / wiki page / commit / Box doc, the
reference MUST include an **audited timestamp**:

- File path OR URL
- Last-modified timestamp (from actual `stat` / API call, not claimed)
- Size or length
- SHA-256 hash (for files) OR commit SHA (for git) OR page revision (for wiki)

Format inside a report:
```
[[Master-Blueprint]]  (sdd-wiki v4, file content/PHGDH-Allosteric-RBD-Binder/Master-Blueprint.md, 
                       mtime 2026-04-18T09:57Z, 1,240 bytes, sha-256 ab34…)
```

The `report_builder.py` helper `audit_artifact(path_or_url)` returns
this metadata dict. Agents must not fabricate timestamps — if the
artifact does not exist at audit time, the report states "NOT FOUND
at audit time" and escalates to Resolver.

## 6.5 Learning audit (on-demand)

Ask any time: "learning" or "what have you learned" or
"show me what you learned" (via Telegram to jakeclaw).

Returns a structured markdown report with:
- **Context:** Aim, Task code, iteration number, current PLEASER stage
- **Overall learning goal** — mapped from the active Aim
- **Current learning focus** — the Task's goal text
- **Sources consulted** — wiki pages that match Task keywords, audited
  (size, mtime, SHA-256)
- **Hermes activity** — last 48h of wiki-builder runs with full log lines
- **Prior PLEASER iterations** — Learning-phase snippets from previous L3
  reports on this Task (with audit metadata)
- **Gaps** — explicit list of open questions

Generated by `/Users/jakeclaw/workers/bin/learning_audit.py`. Every
artifact referenced is verified by filesystem `stat` at audit time —
missing artifacts flagged explicitly, never fabricated.

## 7. Report-request conventions (all levels, any time)

Reports may be requested at any level, at any time, by anyone:

| Trigger | Channel | Generates |
|---------|---------|-----------|
| `L1`, `status` on Telegram | Telegram | L1 now |
| `L2`, `digest` | Telegram | L2 now |
| `L3` | Wiki + Telegram | L3 for current Task |
| `L4` | Wiki | L4 poster |
| `L5` | Box | L5 paper draft |
| `L6` | GitHub | L6 debug bundle |
| `report N` | as above | generic form |

Requests for reports that depend on artifacts not yet present (e.g., L4
poster requiring figures that haven't been produced) MUST be generated
anyway — with explicit "pending Task X.Y" placeholders instead of
fabricated content.

## 5. Resolver — when to escalate

Invoke a Resolver when:
- **Scientific direction shift** — results contradict hypothesis or reveal a better target
- **Ambiguous findings** that could mean 2+ things
- **Engineering block** where 3+ iteration attempts have failed
- **Cross-domain question** needing expertise outside the local team

Resolvers (in order of cost):
1. **Claude (co-supervisor)** — via Jake, for strategic or architectural calls
2. **Human expert** — lab collaborator, Cheaha RC team, subject-matter specialist
3. **Literature deep-dive** — Hermes commissioned wiki-growth on the specific question

Every resolver escalation MUST produce a written resolution (one
paragraph minimum) committed to the iteration's Resolver section.
Ignored escalations are tracked as Open Issues.

## 6. How this interacts with COMMUNICATION_LEVELS.md

- **L1 (Telegram, 3×/day)**: names the current Task X.Y + one-line delta
- **L2 (Telegram, 17:00 daily)**: progress across active aims (up to 4),
  pointing at which tasks moved
- **L3 (Wiki + Telegram, each iteration)**: full PLEASER report for the
  just-closed Task X.Y
- **L4 (Wiki, on demand)**: poster format — typically pulls figures from
  closed L3 iterations to tell a multi-task story
- **L5 (Box, on demand)**: paper-level — stitches L3/L4 into a single
  reproducible narrative with proper methods
- **L6 (GitHub, on demand)**: debug / reproducibility bundle


## 8. Project Dashboard (Wiki-published, regenerated daily)

Two-table dashboard at **`/Project-Dashboard`** on the public wiki.

### Table 1 — PLEASER × Iterations
- **Rows:** P, L, E, A, S, X, R (7 PLEASER stages)
- **Columns:** each iteration (e.g., "Iter 1 (Task 2.1)", "Iter 2 (Task 2.2)")
- **Cells:** AGE triple score `A.G.E` (e.g., `7.6.5`) on reverse-NIH scale
- **Cell color** by min(A,G,E): green ≥5, yellow =4, red ≤3
- **Cell link:** opens the L3 report for that iteration

### Table 2 — Aim → Task → Subtask progress
- **Rows:** Aim (H3) → Task (indented) → Subtask (doubly indented)
- **Columns:** Status, % complete, Achievement (reverse-NIH, color-coded)
- **Parallelism:** tasks may run in parallel, local (W0/L0) or remote (Cheaha)

### Color policy
| Color | Achievement | Meaning |
|-------|-------------|---------|
| 🟢 Green | ≥ 5 | Satisfactory or better; problems resolved with progress |
| 🟡 Yellow | = 4 | Some problem; recoverable without human intervention |
| 🔴 Red | ≤ 3 | Major challenge; human decision requested; time/cost at risk |

Boundary case: Achievement = 4 with a known blocker → Yellow; Achievement
= 4 with unknown causal path → Red.

### Regeneration cadence
- Daily via `ai.jakeclaw.daily_wiki_publish` at 17:05 (pushed to sdd-wiki)
- On-demand via `dashboard` Telegram keyword → jakeclaw runs
  `project_dashboard.py` and pastes the rendered markdown
- Initial seed: dashboard exists from project start even with sparse data;
  missing cells render as "—" rather than absent rows

### Source of truth
`project-state/iteration_state.json` drives "current stage";
`project-state/reports/L3/*.md` drives AGE scores via regex extraction
of "Accuracy=N / Generalizability=N / Efficiency=N" lines.
Backlog + Completed + CurrentGoal files drive Table 2.


<!-- LIVENESS-RESOLVER -->
## Resolver phase — liveness check (Apr 18 2026)

At the start of every Resolver (R) phase, qwenclaw MUST:

1. Invoke `skills/liveness-audit/scripts/liveness.sh --resolver`
2. Read `project-state/liveness.json` — if `overall == "red"`:
   - List red channels in the R-phase note in `iteration_state.json`
   - Escalate via `project-state/ISSUES/OPEN.md` (already appended by the skill)
   - Force L1 report within 5 min with `report_builder.py --level L1 --urgent`
3. Only advance to next-task promotion when `overall == "green"` OR the user
   explicitly unblocks via the dashboard "Unstick" button.

Dashboard surfaces a **Liveness** card on Project Status tab with:
- 10 per-channel traffic-lights (green / red / unknown)
- Age-of-last-change per channel
- Overall status badge
- Last 24 h trend (from `liveness_history.jsonl`)
