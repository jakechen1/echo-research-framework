# Boot context for jakeclaw (auto-updated by refresh_boot_md.sh)

**CRITICAL: When asked any status-type question, you MUST use these
Assessor numbers VERBATIM. Do NOT paraphrase, do NOT invent channels,
do NOT add fabricated disclaimers about "truncated buffer".**

## Latest Assessor snapshot (updated 2026-04-22T21:51:36Z)

```
⚠️ BLOCKED (stalls pending)
⚠️ AGE_SUBPAR
- Task: Task 1.3 / stage P (age None min)
- Progress: PROGRESS (+1 files, +264 bytes, +1,258,021 net, 0 commits, 1 min window)
- Liveness: red  red=['wiki_interlink', 'cheaha_queue', 'box_sync']
- Flags: {'STAGE_STALLED': False, 'NO_WORK_THIS_WINDOW': False, 'BLOCKED': True, 'AGE_SUBPAR': True}
```

## Integrity directive

Every status reply begins with the block above, copied EXACTLY. If a field
looks odd (e.g. a channel name you don't recognize), quote it exactly as
shown — the Assessor is the source of truth, not your memory.

If numbers seem stale (>10 min old from timestamp above), say
"Assessor snapshot is >10 min old; running fresh tick now" and call
`bash /Users/jakeclaw/workers/bin/read_assessor.sh` via the shell tool.

NEVER output text resembling Assessor output without actually running the
tool. The real tool output goes into tool_result; if you emit it as plain
text, you are hallucinating.
