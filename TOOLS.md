# TOOLS.md - Local Environment

## Infrastructure
- **L0** (inference): mac-l0 / 192.168.68.200 — M4 Pro 24GB, Ollama (Gemma 4 26B, Qwen 3.5 10B)
- **W0** (gateway): mac-w0 / 192.168.68.201 — M4 16GB, OpenClaw + Dashboard + Hermes
- **NAS**: Synology / 192.168.68.128 — mounted at /Volumes/dataset-jakeclaw
- **Dashboard**: http://192.168.68.201:3002 (Wiki tab shows live build progress)

## SSH
- L0: `ssh jakechen@192.168.68.200` (from W0)
- Deploy key: `~/.ssh/id_ed25519` → github.com:jakechen1/echo-research-framework (wiki repo)

## Wiki System (Hermes Integration)
- **Wiki**: /Users/jakeclaw/wiki/ (1550+ pages, 7 categories)
- **Builder**: `~/.hermes-venv/bin/python ~/.hermes/scripts/wiki_builder.py`
  - start "<topic>" --depth N --pages-per-level N
  - status / stop / resume
- **Builder log**: ~/.hermes/logs/wiki-builder.log
- **Builder state**: ~/.hermes/wiki-builder-state.json
- **Projects**: ~/.hermes/wiki-projects.json
- **Scanner**: ~/wiki-scanner.js (run with node, outputs JSON)
- Pages go to: /Users/jakeclaw/wiki/topics/<category>/<slug>.md

## GitHub
- Wiki repo: github.com/jakechen1/echo-research-framework (SSH push via deploy key)
- Dashboard repo: github.com/jakechen1/local-llm-installation
- Auto-push: hourly via com.jakeclaw.git-autopush LaunchDaemon
- gh CLI: installed but NOT authenticated (needs `gh auth login` with PAT)

## Box
- JakeClaw folder: My Projects > Current > JakeClaw
- Reports auto-sync: ~/reports/ → Box (hourly)
- box CLI: NOT installed (needs `npm i -g @box/cli` + OAuth)
- Alternative: use dashboard Box MCP tools or save to ~/reports/

## LaunchDaemons
- com.openclaw.dashboard — Dashboard on :3002
- com.openclaw.jakeclaw — OpenClaw gateway (Echo)
- com.openclaw.claireclaw — Claire gateway
- com.jakeclaw.nas-mount — Synology auto-mount
- com.jakeclaw.git-autopush — Wiki hourly push
- com.jakeclaw.l0-keepalive — L0 health monitor
- com.jakeclaw.openclaw-watchdog — Service watchdog

## Preferred Model
- Qwen 3.5 for fast queries, Gemma 4 for detailed wiki/research tasks
