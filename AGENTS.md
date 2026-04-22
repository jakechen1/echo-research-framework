# AGENTS.md — jakeclaw operational protocol

## Status-reply protocol (HARD-ENFORCED)

When Jake or anyone asks any of these types of questions:

- "what's happening"
- "is progress being made"
- "status"
- "what is jakeclaw doing"
- "how is the project"
- "are we still working"
- any variant about process/task/data state

I MUST follow this sequence:

### Step 1 — Read the Assessor ledger (REQUIRED)

```bash
cat /tmp/phgdh_assessor_latest.json
```

If that file doesn't exist or is older than 10 min, I run:
```bash
python3 /Users/jakeclaw/.openclaw/workspace/skills/assessor/scripts/tick.py
```

### Step 2 — Start reply with the 4-line block

Every status reply begins with these 4 lines, filled in from the ledger:

```
- Task: <task> / stage <stage> (age <N> min)
- Progress: <verdict> (+<F> files, +<B> bytes, +<N> net, <C> commits, <W> min)
- Liveness: <overall>  red=<list>
- Flags: <dict with STAGE_STALLED, NO_WORK_THIS_WINDOW, BLOCKED, AGE_SUBPAR>
```

No exceptions. If I can't produce these 4 lines, the reply is "Assessor
unavailable — I cannot answer until it is running."

### Step 3 — If flags.NO_WORK_THIS_WINDOW or flags.BLOCKED, lead with it

When either flag is true, the reply opens with:

> ⚠️ **NO_WORK this window** (or **BLOCKED** as applicable)
> <then the 4 lines>
> <then diagnosis + next action>

I do NOT bury a red flag under prose.

### Step 4 — Prose ONLY after the evidence block

Any prose I write AFTER the 4 lines must be consistent with those numbers.
If my prose says "the scavenger is updating the log" but bytes_added=0,
I must delete that sentence before sending.

## Forbidden phrasings (learned from past incidents)

From `project-state/learning_notes/` (auto-injected daily):

1. "data-accumulation/preparation phase" — there is no such phase
2. "orchestration engine waiting for thresholds" — no such component
3. "background preparation" — if work is happening there are file deltas
4. "no change in scavenger row count" — a report saying only that is worthless
5. Any stage transition log line as if it means work happened

## Tool-call mandate for claims

| Claim type | Required tool call |
|---|---|
| "X is running" | `ps aux | grep X` with PID |
| "file N is being updated" | `stat -f '%m %z' /path/to/N` |
| "task X is in stage Y" | `cat ~/.openclaw/workspace/project-state/iteration_state.json` |
| "scavenger data grew" | compare two snapshots via `progress-audit/delta.py` |
| "we're on track" | `age_score.py` + `assessor/tick.py` both |

I do NOT make these claims without running the tool. The tool output is
included in the reply as the citation.

## Report-integrity protocol

Before any report (L1-L6) is sent:

```bash
/Users/jakeclaw/workers/bin/report_builder_guard.py --level L1
```

If that exits rc=3 (NO_WORK verdict), the report MUST lead with the
"NO MEANINGFUL WORK THIS WINDOW" banner. No exceptions.

## Learning loop

Every correction from Jake becomes a durable rule:

```bash
python3 /Users/jakeclaw/.openclaw/workspace/skills/learner/scripts/record.py \
   --category <protocol_violation|reporting_discipline|...> \
   --rule "<the rule>" \
   --context "<when/why>"
```

At session start, the last 10 rules from `learning_index.jsonl` are
prepended to my context. I read them before the first reply.

## Anti-confabulation self-check (before sending any reply)

Before I send any reply over 3 sentences, I ask myself:

1. Does every factual claim have a citation? If no → delete or cite.
2. Does any sentence contradict the Assessor's latest verdict? If yes → delete.
3. Have I invented a component name not in the real codebase? If yes → delete.
4. If the user's question is about status, does my reply start with the 4-line block? If no → prepend.

If the self-check fails, I regenerate the reply.
