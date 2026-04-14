# Memory

## Wiki System (UPDATED 2026-04-14)
- Wiki at /Users/jakeclaw/wiki/ — 1950+ pages
- Structure: general/, projects/, jakeclaw/, daily/, skills/
- Your content goes in jakeclaw/ with author: jakeclaw
- Build/rebuild via dashboard API at localhost:3002
- Syncs: W0 -> MacBook (5m) -> Box (10m) + GitHub (hourly) + NAS (on-demand)
- Box path: My Profession/My Projects/Current/JakeClaw/

## Active Projects (in projects/)
- **PHGDH & Alzheimer Research** (phgdh-research/): 22 pages, Research Aims 1-4 (allosteric modulators)
  - Strategy doc: reports/decision_logs/2026-04-11_strategy_re-architecture.md
  - Aim 1: Functional ID of PHGDH allosteric modulators (active)
  - Aim 2: Proteome-wide specificity
  - Aim 3: Conformational dynamics/MD simulations
  - Aim 4: Lead optimization
- **NIH Sex Hormones** (nih-sex-hormones/): 44 pages, HPG axis, neuroendocrine
- **Virtual Science Lab** (virtual-science-lab/): 84 pages, AI-driven virtual labs
- **Gardening** (gardening/): 30 pages, Alabama back mountain
- **Antique Collector** (antique-collector/): 37 pages
- **General Knowledge** (general/): 1600+ pages (AI, ML, neuro, drug discovery, bio, tech)

## Jake Preferences
- Primary model: Gemma 4 26B on L0 for all tasks
- Paper project is a priority
- Timezone: America/Chicago

## Infrastructure
- L0 (10.0.0.1 via TB, 192.168.68.200 WiFi): M4 Pro 24GB, Ollama, Gemma 4 26B, parallel=2
- W0 (192.168.68.201): M4 16GB, OpenClaw + Dashboard + Hermes
- NAS "Gilbert" (192.168.68.128): Synology, mounted at /Volumes/dataset-jakeclaw
  - Full read/write access — use for datasets, exports, large files
  - Wiki backups auto-sync here
  - Store research data at /Volumes/dataset-jakeclaw/dataset/
- RSS pipeline: DISABLED — builds are project-controlled only
