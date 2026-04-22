---
category: protocol_violation
recorded: 2026-04-22T20:00:11+00:00
---

# Learning: PLEASER stages must never auto-advance when the stage executor is missing

## Context
Apr 22 2026 incident: Task 1.2 and Task 4.4 marched P→L→E→A→S→X→R within minutes because task_advancer silently auto-advanced on empty/broken registry entries. User observed vacuous stage transitions while zero scientific work was being performed. Fixed: task_advancer now STALLS on missing executor and invokes Planner to draft a .pending stub for user review.

## Enforcement
This rule should be checked during Assessor (A-stage) reviews and
enforced by relevant skill upgrades. Future iterations must not repeat
the pattern that triggered this correction.
