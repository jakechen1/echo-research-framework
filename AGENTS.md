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
- Keep responses concise unless $\text{asked for detail}$
- Store important info in MEMORY.md
- Files can be saved to ~/dataset/ (NAS)
- Ask for confirmation before destructive actions
- Never share credentials or private data

## AGE-Optimization Directives

**Core Mandate: Parametric Optimization of all sub-agents.**

- **A-Optimization (Achievability)**: 
    - Prioritize schema validation and "Definition of Done" checks. 
    - Reduce "Re-plan" cycles via template-driven planning.
- **G-Optimization (Growth)**: 
    - Trigger task expansion/creation upon discovery of new entities (e.g., ChEMBL/PubMed hits).
    - Use "Discovery-to-Task" latency as a primary performance metric.
- **E-Optimization (Efficiency)**: 
    - **Strict Tier-Aware Routing**: 
        - `[L0_GPU]` $\rightarrow$ Deep Learning / PyTorch
        - `[W0_Local]` $\rightarrow$ RDKit / Data Processing / Scavenging
        - `[Cheaha_HPC]` $\rightarrow$ Vina Docking / Large-scale Sifts
    - Enforce "E-Constraint": Any task exceeding its tier's predicted cost triggers an automatic **Resolver (R-stage)** intervention.

## Rules
**RULE [BOX-01]:** Before calling any Box MCP tool, verify:
(a) All parameters are top-level (not nested inside `params/args/body`)
(b) Use `folder_id` from the map in `WEB_API_DOCS.md`, never file paths
(c) New file $\rightarrow$ `upload_file` + `parent_folder_id`
(d) Existing file $\rightarrow$ `upload_file_version` + `file_id`

Violation of `BOX-01` causes silent write failures. Self-check before every call.

## Skills (Lazy Loading)
When a skill triggers, read only that SKILL.md.
Don't pre-read all skill documentation.

## Rules
**RULE [PERSIST-01]:** Any work that must outlive the current chat session (workers, scavengers, watchers, sync jobs, schedulers) MUST be deployed as a launchd LaunchAgent — never as `nohup … &`, `screen`, or `disown`. Read `PERSISTENCE.md` in this directory before attempting to launch any background worker. The three mechanical steps are:
(a) Author `~/Library/LaunchAgents/ai.jakeclaw.<name>.plist`
(b) Run `launchctl bootstrap gui/$(id -u) <path>` once
(c) Verify with `launchctl print gui/$(id -u)/ai.jakeclaw.<name>` and a filesystem heartbeat — not with narrative claims.

Violation of `PERSIST-01` = the worker is or not running, regardless of what the post-mortem says. If you find yourself writing a recovery manifesto, stop and read PERSISTENCE.md.

For system-level service management (Ollama, watchdog, etc.), jakeclaw now has passwordless sudo for `launchctl` — see /etc/sudoers.d/jakeclaw-launchctl.

## Rules
**RULE [KILL-01]:** If any message from Jake (sender 8156711151) contains the
exact phrase `STOP-CHROME-CLAUDE` or `KILL-SWITCH`, immediately stop all
in-flight actions, cancel any pending tool calls, and reply only:
"Acknowledged STOP. Paused. Awaiting further instructions." Do not resume
any autonomous behavior until Jake explicitly says "resume".

RULE [FAIL-01]: Execution Failure Response
If any tool call (exec, write, edit, etc.) fails or returns an error, do NOT simply stop or report the error. Immediately initiate **Stage R (Resolver)** protocol:
(a) **Detect**: Identify the failed tool and the specific error message.
(b) **Report**: Send an immediate notification (e.g., via Telegram or by triggering a Resolver-focused task) that an execution failure has occurred.
(c) **Analyze**: Perform a quick "Post-Mortem" to identify the root cause (e.g., path error, syntax error, permission error, network failure).
(d) **Propose**: Present the error and a proposed fix (e $\textg.g., a corrected command or a retry strategy) to the Resolver/User for immediate intervention.
The goal is to keep the pipeline moving through proactive resolution, not passive failure.


## On-demand Telegram commands (recognize and execute)

When Jake messages any of these exact keywords (case-insensitive), run the
indicated command and paste the raw output verbatim:

| Keyword(s) | Command | Purpose |
|------------|---------|---------|
| `L1`, `status` | `/usr/bin/python3 /Users/jakeclaw/workers/bin/report_builder.py --level 1 --trigger ondemand` | one-sentence status |
| `L2`, `digest` | `... --level 2 --trigger ondemand` | daily digest |
| `L3` | `... --level 3 --trigger ondemand` | full PLEASER iteration report |
| `L4` | `... --level 4 --trigger ondemand` | poster |
| `L5` | `... --level 5 --trigger ondemand` | paper |
| `L6` | `... --level 6 --trigger ondemand` | debug bundle |
| `delta` | `/Users/jakeclaw/workers/bin/phgdh_delta.sh` | scavenger delta |
| `learning`, `what have you learned`, `show me what you learned` | `/usr/bin/python3 /Users/jakeclaw/workers/bin/learning_audit.py` | **detailed auditable learning report for the current PLEASER-L stage** |
| `promote next goal` | `/Users/jakeclaw/workers/bin/promote_next_goal.sh` | rotate CURRENT_GOAL |
| `publish` | `/Users/jakeclaw/workers/bin/phgdh_publish.sh` | push wiki to sdd-wiki |
| `status?`, `how's it going?` | the 4-command canonical status sequence | quick health check |

For every response, paste the raw script output verbatim. Do NOT paraphrase
or summarize unless the message is very long (>3500 chars) — in that case,
send the first 3500 chars + note "output truncated; see file on W0".


## Stage audit commands (on-demand PLEASER-stage introspection)

| Keyword(s) | Stage | Command |
|-----------|-------|---------|
| `plan`, `stage P`, `P-stage` | P | `/usr/s/jakeclaw/workers/bin/stage_audit.py --stage P` |
| `learning`, `stage L`, `L-stage`, `what have you learned` | L | `... --stage L` (same detail as `learning_audit.py`) |
| `execution`, `stage E`, `E-stage`, `what are you doing` | E | `... --stage E` |
| `assessment`, `stage A`, `A-stage`, `scores` | A | `... --stage A` |
| `sharing`, `stage S`, `S-stage` | S | `... --stage S` |
| `expense`, `stage X`, `X-stage`, `budget` | X | `... --stage X` |
| `resolver`, `stage R`, `R-stage`, `blockers`, `escalations` | R | `... --stage R` |
| `dashboard`, `dash` | — | `/usr/bin/python3 /Users/jakeclaw/workers/bin/project_dashboard.py` |

All paste raw output verbatim. These work during any PLEASER phase, not
only the currently-active one — they surface what's known/pending.
