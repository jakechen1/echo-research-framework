# Cheaha partitions — full reference

Source: https://docs.rc.uab.edu/cheaha/hardware/ (as of April 2026)

## CPU Intel (52 nodes, 48 cores, 754 GB)
- `express`  — 2h — QoS: 264 cores/person
- `short`    — 12h — 44 nodes/person
- `medium`   — 50h — 44 nodes/person
- `long`     — 150h — 5 nodes/person

## CPU AMD (34 nodes, 128 cores, 504 GB)
- `amd-hdr100` — 150h — high core count per node

## Large memory
- `largemem`      — 50h — 13 nodes, 24 cores, 755 GB
- `largemem-long` — 150h — 5 nodes, 24 cores, 755 GB

## GPU — Pascal (P100, 16 GB VRAM, CC 6.0)
- `pascalnodes`        — 12h — 18 nodes, 4x P100, 28 cores, 252 GB
- `pascalnodes-medium` — 48h — 7 nodes, same spec

## GPU — Ampere (A100 80GB, CC 8.0)
- `amperenodes`        — 12h — 20 nodes, 2x A100, 32 cores, 189 GB
- `amperenodes-medium` — 48h — 20 nodes, same spec

## Choosing a partition — decision tree
1. Needs GPU? → A100 for big models (LLM inference, modern training), P100 for small models
2. Memory > 500 GB? → `largemem`
3. CPU only, >24h? → `medium` (≤50h) or `long` (≤150h)
4. Quick smoke test? → `express` (fast queue turnaround)
