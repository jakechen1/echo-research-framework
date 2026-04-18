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

| Letter | Criterion | Question |
|--------|-----------|----------|
| A | **Accuracy** | Did outputs correctly represent reality? (computational accuracy vs ground truth or literature benchmarks) |
| G | **Generalizability** | Will the finding transfer beyond this instance? (other targets, datasets, conditions) |
| E | **Efficiency** | Did resource use (time, compute, tokens) match the value produced? |

Scoring: 1-9, 1 = best.

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
