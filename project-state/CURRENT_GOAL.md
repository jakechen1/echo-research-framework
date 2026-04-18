# Current Sub-Goal

**ID:** G-001
**Started:** 2026-04-18
**Owner:** jakeclaw (executor) / qwenclaw (PM, once online) / jakechen (human)
**Deadline:** within 1 day
**Status:** open

## Goal
Verify the PHGDH scavenger ran successfully (scheduled 02:00 daily) and sanity-check
the output file for today.

## Definition of done
- [ ] `/Users/jakeclaw/workers/data/phgdh/2026-04-18.jsonl` exists
- [ ] File is ≥ 1 MB (typical scavenge ≈ 3.5 MB, 2600+ rows)
- [ ] First row parses as valid JSON with fields: `molecule_chembl_id`,
      `canonical_smiles`, `standard_type`, `pchembl_value`
- [ ] Heartbeat `/Users/jakeclaw/workers/heartbeats/phgdh_scavenger.ts`
      is within the last 24 h
- [ ] Today's DAILY_LOG entry mentions row count + file size

## Commands jakeclaw should run
```bash
ls -la /Users/jakeclaw/workers/data/phgdh/2026-04-18.jsonl
wc -l /Users/jakeclaw/workers/data/phgdh/2026-04-18.jsonl
head -1 /Users/jakeclaw/workers/data/phgdh/2026-04-18.jsonl | python3 -m json.tool | head -12
stat -f '%Sm' /Users/jakeclaw/workers/heartbeats/phgdh_scavenger.ts
```

## Notes
This is the smallest first goal — validates Tier 0 daemon, Tier 1 state update,
and the new auto-compactor in one shot. On success, pick next from BACKLOG.md.
