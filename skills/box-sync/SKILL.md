# Skill: box-sync

## Current reality (as of 2026-04-18)

- **Hermes on W0 has no Box MCP configured** (`hermes mcp list` is empty)
- **rclone on W0 is installed but OAuth not completed** (interactive token)
- **Only the MacBook Claude session has Box MCP** (via toolbelt)

So we operate in **"pending-manifest" mode**:

1. W0 scripts append upload-intents to `/tmp/phgdh_box_pending.json`
2. When Jake's MacBook Claude session is active, Claude drains the manifest
   by calling Box MCP upload_file with the mapped folder IDs
3. Each successful upload is logged to `box_sync.log` (satisfies liveness)

## Enqueue format

```json
{"at": "...", "src": "/path/on/W0", "folder_id": "377423329269",
 "folder_label": "figures", "priority": "normal"}
```

One JSON per line in `/tmp/phgdh_box_pending.json`.

## Folder IDs (from BOX_FOLDERS.md)

| Label | ID | Used for |
|-------|----|----------|
| PHGDH (root) | 377424964160 | top-level |
| paper | 377423262935 | manuscript |
| slides | 377423558049 | decks |
| reports | 377423073347 | L1-L6 reports |
| logs | 377424191575 | daemon logs |
| data | 377424268363 | JSONL / CSV |
| figures | 377423329269 | PNG/SVG |
| references | 377424339814 | bibliography |

## Status reporter

`box_status.sh` writes `/tmp/phgdh_box_status.json` for dashboard:
- `macbook_last_seen` — timestamp of last MacBook Claude drain
- `pending_count` — lines in pending manifest
- `w0_rclone_configured` — bool (false until OAuth)
- `hermes_mcp_configured` — bool (false until `hermes mcp add box ...`)

## Upgrade path (to remove MacBook-only dependency)

1. Run `hermes mcp add box --command /path/to/box-mcp-server` on W0
2. Complete OAuth via device code flow (interactive once)
3. Switch enqueue script to call hermes directly (drop MacBook drain)
