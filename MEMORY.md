# Memory

## Wiki System
- Personal wiki at /Users/jakeclaw/wiki/ — 1550+ pages across 7 categories (ai, machine-learning, neuroscience, drug-discovery, biology, technology, other)
- Wiki builder (Hermes) generates pages from seed topics using Gemma 4 on L0
- Use `wiki-builder` skill to start/stop/check builds
- Dashboard at http://192.168.68.201:3002 shows live build progress
- Wiki auto-pushes to GitHub hourly (echo-research-framework repo)

## Active Projects
- **NIH Sex Hormones** (running): Sex hormone biology, HPG axis, estrogen/progesterone/testosterone pathways — depth 3, 20 pages/level
- **PHGDH & Alzheimers** (completed): 29 pages on PHGDH role in Alzheimer disease
- **RSS Pipeline** (completed): 1500+ pages from RSS feeds (arXiv, HN, PubMed)

## Jake Preferences
- Prefers Qwen 3.5 for fast queries, Gemma 4 for research/wiki
- Paper project is a priority
- Timezone: America/Chicago

## Infrastructure
- L0 (192.168.68.200): M4 Pro 24GB, Ollama inference, daily reboot 4 AM
- W0 (192.168.68.201): M4 16GB, all services
- NAS (192.168.68.128): Synology, mounted at /Volumes/dataset-jakeclaw
- IPs are now DHCP-reserved (stable)
