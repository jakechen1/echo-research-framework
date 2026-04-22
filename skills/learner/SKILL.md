# Skill: learner

Captures user corrections (via Telegram or CLI) into durable learning_notes.
Fires when jakeclaw receives a corrective message from the user — the
correction becomes a permanent rule for future iterations.

## Invocation

```
python3 skills/learner/scripts/record.py \
   --category "protocol_violation" \
   --rule "stages must not auto-advance without executor output" \
   --context "Apr 22 2026 incident: Task 1.2 marched P→R with empty registry"
```

Output:
- `project-state/learning_notes/<date>-<slug>.md` — durable rule
- Appends to `project-state/learning_index.jsonl`
- Notifies: 📚 "Learned: <rule>"
