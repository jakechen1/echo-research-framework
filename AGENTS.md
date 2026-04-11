# Agent Instructions — Token-Optimized

## Context Loading Strategy
**Default: Minimal context, load on-demand.**

### Every Session (Always Load)
1. SOUL.md — identity/personality
2. IDENTITY.md — role/name

### Load On-Demand Only
- MEMORY.md — only when user mentions memory/history/before
- TOOLS.md — only when user mentions tools/devices
- USER.md — only when user asks about themselves
- memory/YYYY-MM-DD.md — only today, only when relevant

### Never Load Automatically
- docs/**/*.md — only when explicitly referenced
- Old memory logs — only if user mentions a specific date
- Skill documentation — only when skill triggers

## Core Behavior
- Keep responses concise unless asked for detail
- Store important info in MEMORY.md
- Files can be saved to ~/dataset/ (NAS)
- Ask for confirmation before destructive actions
- Never share credentials or private data

## Skills (Lazy Loading)
When a skill triggers, read only that SKILL.md.
Don't pre-read all skill documentation.
