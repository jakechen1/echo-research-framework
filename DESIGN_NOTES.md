---
title: "Design intent notes"
updated: 2026-04-18
---

# Design intent notes

Short reminders of *why* we built things, so future-you and future-agents
don't rebuild them differently.

## Hermes's higher purpose: close the data↔knowledge loop

Hermes is NOT just a "build a wiki from a seed topic" tool. Its mature
role is the **research synthesis engine that closes the loop between
project data and project knowledge**:

```
  scavenger → raw data (ChEMBL JSONL)
      ↓
  phgdh_enrichment daemon (G-012, pending)
      ↓
  ranks new entities → emits seeds for Hermes
      ↓
  Hermes generates/updates wiki pages, grounded by source_validator
      ↓
  pages are wikilinked (molecule ↔ target ↔ pathway ↔ disease ↔ paper)
      ↓
  back-links update phgdh-scavenger summary page
      ↓
  next day's scavenger finds novel molecules → loop continues
```

After N weeks, the wiki becomes a living, data-driven knowledge graph
specific to this project — every CHEMBL ID, every target, every pathway
has a grounded page that links to real literature.

**Why this sequencing matters.** Do NOT build the enrichment loop before
G-001..G-005 produce real "interesting entity" signals (pChEMBL tails,
top-20 inhibitors, PDB binding sites). Enrichment on a cold wiki yields
generic text. Enrichment on curated signals yields genuine knowledge.

## jakeclaw (Gemma 4 26B) vs qwenclaw (Qwen 3.5 9B): deliberate asymmetry

Gemma 4 has the better general reasoning (26B > 9B); Qwen 3.5 has the
better tool-call discipline (family was trained for it). We pair them so
each does what it's best at:

- Gemma = thinking, writing, interpreting literature
- Qwen = picking goals, routing commands, auditing outputs

DO NOT swap these without checking the context-window and benchmarks.

## Local-first, paid sparingly

Claude (Opus / Claude Code) is a consultant, not an employee. If you
catch yourself using Claude for routine work, ask: can a local agent
(jakeclaw / qwenclaw / Hermes) do this? Usually yes.

## Kill switch is for you, not the agents

`STOP-CHROME-CLAUDE` in chat halts all agents. They cannot disable it.
This is the escape hatch and stays inviolable.
