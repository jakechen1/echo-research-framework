# Box folder IDs for PHGDH project

All paths live under: My Projects > Current > JakeClaw > PHGDH

| Folder | ID | URL | Purpose |
|---|---|---|---|
| PHGDH (root) | 377424964160 | https://uab.app.box.com/folder/377424964160 | project root |
| paper | 377423262935 | https://uab.app.box.com/folder/377423262935 | manuscript draft (intro / methods / results / discussion) |
| slides | 377423558049 | https://uab.app.box.com/folder/377423558049 | PPT/key deck of findings |
| reports | 377423073347 | https://uab.app.box.com/folder/377423073347 | daily + weekly summaries |
| logs | 377424191575 | https://uab.app.box.com/folder/377424191575 | raw session/daemon logs rolled up |
| data | 377424268363 | https://uab.app.box.com/folder/377424268363 | exported JSONL / figures' source data |
| figures | 377423329269 | https://uab.app.box.com/folder/377423329269 | PNG/SVG figures for paper + slides |
| references | 377424339814 | https://uab.app.box.com/folder/377424339814 | bibliography, downloaded PDFs |

Programmatic upload: use Box MCP `upload_file` with `parent_folder_id` = the
corresponding ID above. NEVER hard-code paths — always reference by ID.

## Old contents needing manual cleanup
Parent folder `JakeClaw` (ID 375865153759) has 12 pre-existing subfolders
(.clawhub, .openclaw, daily, general, jakeclaw, memory, projects, reports,
research, schema, skills, skills-available) and 8 markdown files. These are
historical jakeclaw workspace backups. The Box MCP in use does not expose
move/delete, so cleanup must happen via Box web UI:

1. Go to https://uab.app.box.com/folder/375865153759
2. Select all items EXCEPT the new "PHGDH" folder
3. Right-click → Move to → pick an archive location (or Trash)
