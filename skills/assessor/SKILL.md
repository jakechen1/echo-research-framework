# Skill: assessor

Runs at PLEASER A-stage (Assessment). Reads the current task's AGE score,
artifacts, benchmarks.json, and writes an improvement plan for the
iteration close / next iteration.

## What it evaluates

1. **Completion checklist** — which DoD items are met/missing?
2. **Benchmark categories** — which have we declared wins for? missed?
3. **AGE score components** — A/G/E vs target band per
   OPTIMIZATION_GUIDELINES.md
4. **Resource usage** — wall-time vs budget, concurrency actually used
5. **Per-axis improvement candidates** — ranked by expected ΔA/ΔX

## Output

`project-state/assessment_notes/<task_slug>-iter<N>.md` — markdown
plan with:
- summary table (target vs actual per axis)
- list of alternatives (ranked) with code-hint per alternative
- recommendation: `ACCEPT` (close iteration), `RETRY` (try alt #1),
  or `ESCALATE` (no good alt, human in loop)

Also appends to `project-state/assessment_history.jsonl` for trend tracking.

## Invocation

- Automatic: called from advance_stage.sh when entering stage A
- On-demand: `python3 skills/assessor/scripts/assessor.py --task "Task X.Y" --iteration N`

## Rules

- Rule-based first (reliable), LLM-assisted second (for writing prose)
- Never runs remediation itself — that's retry-alternatives
- Never advances stage; writes the plan only
- Limits to 3 alternatives (matches retry budget)
