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

## Recent Optimizations & Diagnostics (2026-04-14)
- **Network Latency Found:** Critical performance gap identified between Thunderbolt (0.55ms) and WiFi (115.92ms) for W0 $\leftrightarrow$ L0 communication.
- **Optimization Plan:**
    1. **Switch to Thunderbolt:** Update W0 Gateway to use `10.0.0.1` instead of WiFi IP.
    2. **Model Tiering:** Use lightweight models (e.g., 2B/7B) for routine tasks and Gemma 4 26B for heavy reasoning.
    3. **Context Management:** Periodically trigger "fresh sessions" to flush KV cache.
- **Established Reset Protocol:** When asked to "reset" or "start fresh," Echo will summarize vital info to `MEMORY.md` and conclude the current session.
