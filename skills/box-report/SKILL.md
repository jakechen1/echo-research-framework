# Box Report Generator

Generate structured reports and save them for Box sync.

## When to Use
- User asks to create a report, summary, or status update
- User mentions Box, cloud storage, or sharing
- Periodic status updates needed

## How It Works
1. Generate the report content in markdown
2. Save to ~/reports/ with date-stamped filename
3. Reports are automatically synced to Box every hour

## Report Format
Save reports as markdown files:
- Filename: YYYY-MM-DD-{topic}.md  
- Location: ~/reports/
- Include YAML frontmatter with title, date, tags

## Example
When asked "create a weekly research summary":
1. Gather data from memory, wiki, and recent activity
2. Write a structured markdown report
3. Save to ~/reports/2026-04-11-weekly-research-summary.md
4. Tell user it will sync to Box within the hour

## Available Commands
- save_report(filename, content) - saves to ~/reports/
- The sync daemon handles Box upload automatically
