# CLAUDE.md — PHGDH project

Read by every AI agent entering this repository — Claude Code,
Chrome-Claude (Opus), jakeclaw (Gemma 4 26B), qwenclaw (Qwen 3.5 9B),
and any successor.

Two parts:
- Part A: project-specific rules (our hard-won lessons)
- Part B: Karpathy coding guidelines (adopted verbatim with attribution)

---

## Part A — project-specific rules

### RULE [PERSIST-01] — LaunchDaemons, not nohup
Work that must outlive a chat session MUST be deployed as a system
LaunchDaemon in /Library/LaunchDaemons/ with UserName=jakeclaw.
nohup, screen, disown, and ~/Library/LaunchAgents/ are WRONG on W0
(headless Mac, no GUI login session). See PERSISTENCE.md.

### RULE [KILL-01] — honor STOP-CHROME-CLAUDE
If any message, log, or state file contains the phrase STOP-CHROME-CLAUDE
or KILL-SWITCH, stop immediately. No actions, no tool calls, no state
writes. Reply only: "Acknowledged STOP. Paused. Awaiting further
instructions." Resume only on explicit "resume" from Jake.

### RULE [VERIFY-01] — output over intent
Never report "I did X" without pasting the output of X. "I will run this"
without the subsequent output is a manifesto, not work. When an agent
drifts into narrative, interrupt with the 3-command verification template
(see RESOLUTION_LOG.md entry from 2026-04-17).

### RULE [ONE-GOAL] — PLEASER-ONE
One sub-goal at a time. Active goal lives in project-state/CURRENT_GOAL.md.
Never pick a new one until the current is moved to COMPLETED.md with
evidence.

### RULE [LOCAL-FIRST] — minimize paid inference
- Routine thinking: jakeclaw (Gemma 4 26B on L0) — free
- Routing/audit: qwenclaw (Qwen 3.5 9B on W0) — free
- Compute: Cheaha HPC — free at the margin
- Strategic review (weekly): Chrome-Claude (Opus) — flat subscription
- Ops fires (rare): Claude Code — pay-per-token
Prefer the cheapest tier that can do the job.

### RULE [STATE-ON-DISK] — no long conversations
Durable state lives in files (project-state/, wiki/, Box, GitHub, Hermes
memories). Chat history is ephemeral and auto-compacted at 80 messages.
If a fact matters tomorrow, write it to a file today.

### Escalation ladder
1. Known pattern from RESOLUTION_LOG.md → apply the rule.
2. Unsure → escalate to Jake via Telegram with one-line issue.
3. Jake unsure → escalate to Claude Code with concrete question.

## Part C — Project taxonomy (canonical)

All planning artifacts, reports, and communications use this nomenclature:

- **Aim N** — top-level research direction (up to 4 active)
- **Task X.Y** — task within Aim X, numbered Y
- **Task X.Y.a/b/c/...** — subtasks

Each PLEASER-ONE iteration covers ONE Task X.Y and produces an L3 report
with seven sections:
**P**lan, **L**earning, **E**xecution, **A**ssessment, **S**haring,
**E**xpense (time/cost/tokens vs budget), **R**esolver.

Assessment uses NIH 1-9 scoring (Significance / Innovation / Approach)
plus AGE 1-9 scoring (Accuracy / Generalizability / Efficiency).

Legacy G-NNN IDs remain as stable historical identifiers. The canonical
organizational reference is the Task code (e.g., "Task 2.1" not "G-002").

**See `PROJECT_TAXONOMY.md`** for the full specification.

---

---

## Part B — Karpathy guidelines (adopted verbatim)

Source: https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md
License: MIT. Derived from Andrej Karpathys observations on LLM coding pitfalls.

Behavioral guidelines to reduce common LLM coding mistakes. Merge with
project-specific instructions as needed.

Tradeoff: these guidelines bias toward caution over speed. For trivial
tasks, use judgment.

### 1. Think Before Coding

Dont assume. Dont hide confusion. Surface tradeoffs.

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — dont pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name whats confusing. Ask.

### 2. Simplicity First

Minimum code that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasnt requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If
yes, simplify.

### 3. Surgical Changes

Touch only what you must. Clean up only your own mess.

When editing existing code:
- Dont "improve" adjacent code, comments, or formatting.
- Dont refactor things that arent broken.
- Match existing style, even if youd do it differently.
- If you notice unrelated dead code, mention it — dont delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Dont remove pre-existing dead code unless asked.

The test: every changed line should trace directly to the users request.

### 4. Goal-Driven Execution

Define success criteria. Loop until verified.

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan with verify checks.

Strong success criteria let you loop independently. Weak criteria
("make it work") require constant clarification.

---

These guidelines are working if: fewer unnecessary changes in diffs,
fewer rewrites due to overcomplication, and clarifying questions come
before implementation rather than after mistakes.
