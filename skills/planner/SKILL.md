# Skill: planner

Called when task_advancer stalls on missing executor. The Planner's job:

1. Read the task definition (BACKLOG.md entry + CURRENT_GOAL.md if current)
2. Generate a Bash executor stub at `/Users/jakeclaw/workers/bin/task_<X_Y>_<stage>.sh`
3. Register it in `project-state/task_executors/registry.json`
4. Notify user with the stub path asking for review before activation

The Planner does NOT auto-activate the stub. User reviews, edits, and
removes a `.pending` marker to activate. This prevents the Planner from
generating vacuous stubs that pretend to work.

## Invocation

```
python3 skills/planner/scripts/plan_task.py --task "Task 4.4" --stage E
```

Output:
- `/Users/jakeclaw/workers/bin/task_4_4_E.sh.pending` — stub with TODO comments
- Registry updated (but executor points to `.sh.pending` so advancer still stalls)
- Telegram 📝 "Planner drafted task_4_4_E.sh.pending — review + rename to .sh to activate"
