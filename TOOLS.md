# TOOLS.md - Local Environment

## Infrastructure
- **L0** (inference): mac-l0 / 192.168.68.200 — M4 Pro 24GB, Ollama (Gemma 4 26B)
- **W0** (gateway): mac-w0 / 192.168.68.201 — M4 16GB, OpenClaw + Dashboard + Hermes
- **W0 Ollama**: port 11435, Qwen 3.5 (backup model, 5m idle timeout)
- **NAS**: Synology / DHCP (changes frequently) — mounted at /Volumes/dataset-jakeclaw
- **Dashboard**: http://192.168.68.201:3002

## SSH
- L0: `ssh jakechen@10.0.0.1` (Thunderbolt) or `ssh jakechen@192.168.68.200` (WiFi)
- Deploy key: `~/.ssh/id_ed25519`

## Wiki System

### Directory Structure (UPDATED 2026-04-14)
```
/Users/jakeclaw/wiki/
  general/              <- 1600+ pages (general knowledge)
  projects/             <- dashboard-created project branches
    gardening/
    phgdh-research/
    virtual-science-lab/
    antique-collector/
    nih-sex-hormones/
  jakeclaw/             <- YOUR pages (Echo/OpenClaw-created content goes HERE)
  daily/                <- daily notes
  skills/               <- OpenClaw skills
```

IMPORTANT: When you create wiki content, write to `jakeclaw/` subdirectory with `author: jakeclaw` and `dc.creator: jakeclaw` in the frontmatter.

### Wiki Builder
- Script: `~/.hermes-venv/bin/python ~/.hermes/scripts/wiki_builder.py`
- Build: `start "topic" --depth 2 --pages-per-level 15 --output-dir projects/foo`
- Rebuild: `start "topic" --rebuild --strategy fix-links --output-dir projects/foo`
- Other: `status` / `stop` / `resume`
- Build modes: seed (depth=1), direct (depth=2), full (depth=3)
- Rebuild strategies: fix-links, update-pages, add-links, add-pages, full

### Page Metadata (Dublin Core)
Every page must have this frontmatter:
```yaml
title: "Page Title"
created: 2026-04-14
category: machine-learning
author: jakeclaw
node_level: N0
dc.title: "Page Title"
dc.creator: jakeclaw
dc.date: 2026-04-14
dc.type: Text
dc.format: text/markdown
dc.language: en
dc.rights: CC-BY-4.0
```

## GitHub
- Wiki repo: github.com/jakechen1/echo-research-framework (SSH deploy key)
- Auto-push: hourly via com.jakeclaw.git-autopush LaunchDaemon
- Manual: `cd ~/wiki && git add -A && git commit -m "msg" && git push`
- Dashboard repo: github.com/jakechen1/local-llm-installation
- gh CLI: installed, authenticated as jakechen1

## Box (Cloud Storage)
- Syncs automatically: W0 wiki -> MacBook wiki-vault -> Box
- Box path: Box/OpenClaw-LLM-Infrastructure/wiki/
- You do NOT need to push to Box — it syncs every 10 minutes automatically

## Obsidian
- Vault: wiki-vault on MacBook at ~/wiki-vault/
- Synced from W0 every 5 minutes

## Dashboard API (control builds from code)
Base: http://localhost:3002

List projects: POST /api/wiki-projects  {"action": "list"}
Create: POST /api/wiki-projects  {"action": "create", "name": "X", "prompt": "topic", "depth": 2, "pagesPerLevel": 15, "autoRun": true}
Run: POST /api/wiki-projects  {"action": "run", "id": "proj_xxx", "buildMode": "direct"}
Rebuild: POST /api/wiki-projects  {"action": "run", "id": "proj_xxx", "rebuildStrategy": "add-pages"}
Schedule: POST /api/wiki-projects  {"action": "update", "id": "proj_xxx", "schedule": "daily"}
Stop: POST /api/wiki-projects  {"action": "stop", "id": "proj_xxx"}
Schedule options: off, daily (update-pages), weekly (update-pages), monthly (full rebuild)

## NAS Backup
- NAS mounted at: /Volumes/dataset-jakeclaw/ (SMB, auto-mounted by launchd)
- NAS IP: 192.168.68.128 (DHCP — may change, mount script handles WOL + retry)
- Backup script: `/usr/local/bin/wiki-backup.sh`
- What it backs up:
  - Wiki → /Volumes/dataset-jakeclaw/wiki/ (latest mirror)
  - Wiki snapshots → /Volumes/dataset-jakeclaw/wiki-snapshots/YYYY-MM-DD_HHMM/ (last 7 kept)
  - OpenClaw workspace → /Volumes/dataset-jakeclaw/openclaw-backup/
  - Hermes config → /Volumes/dataset-jakeclaw/hermes-backup/
- Manual backup: `bash /usr/local/bin/wiki-backup.sh`
- API backup: POST /api/wiki-backup (from dashboard)
- The wiki directory lives on W0 local SSD — NOT on NAS. NAS is backup-only.

## Storage Sync Chain
```
W0 local SSD (/Users/jakeclaw/wiki/)
  → rsync 5m → MacBook ~/wiki-vault/
    → rsync 10m → Box cloud (Box/OpenClaw-LLM-Infrastructure/wiki/)
  → backup script → NAS /Volumes/dataset-jakeclaw/wiki/ + snapshots
  → git auto-push hourly → GitHub
```

## System Health
- Watchdog: com.jakeclaw.system-health (every 5m, auto-restarts all services)
- RSS pipeline is DISABLED — builds are project-controlled only
- All services auto-recover from power outages via launchd
