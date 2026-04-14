# Web API & Tool Usage Golden Rules

## Universal Tool Rule
**All tool parameters must be top-level.** Never wrap arguments inside a `params: {}` or `args: {}` object.

## Box MCP Integration Rules
- **No Path Strings:** Never use `path` or `folder_path` for Box operations. Use `folder_id` (numeric strings).
- **Use IDs, Not Paths:** Refer to `schema/BOX_SKILL.md` for the mapping of human-readable folders to `folder_id`.
- **Upload Strategy:**
    - New file $\rightarrow$ `upload_file` + `parent_folder_id`.
    - Existing file $\rightarrow$ `upload_file_version` + `file_id`.
- **No Parameter Nesting:** All parameters for Box tools must be flat, top-level arguments.

### Error Diagnosis
| Error Message | Root Cause | Fix |
| :--- | :--- | :--- |
| `params.path is undefined` | Wrapping args in `params` | Flatten the arguments. |
| `folder_id not found` | Using a path instead of an ID | Use the numeric ID from the map. |
