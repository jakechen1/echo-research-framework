# Publish Queue — pending your approval (PUBLISH-01)

Review each draft. To approve, send on Telegram or reply here:
- **"publish literature"** → publishes 29-paper sweep
- **"publish top20"** → publishes Task 2.2 top-20 inhibitors
- **"publish binding-sites"** → publishes Task 2.3 PDB binding sites
- **"publish stubs"** → publishes 20 Gemma-generated concept hubs
- **"publish all"** → all four bundles above

Each publish runs `phgdh_publish.sh` scoped to the selected bundle and pushes
to `aimed-lab/sdd-wiki` → Quartz rebuilds → live on public site.

## Ready drafts

| Draft | Lines | Links | Target path in sdd-wiki |
|-------|------:|------:|-------------------------|
| wiki_drafts/phgdh-allosteric-literature-2024-2026.md | 188 | 4 | content/phgdh-research/phgdh-allosteric-literature-2024-2026.md |
| wiki_drafts/top20-phgdh-inhibitors.md | ~50 | 5 | content/PHGDH-Allosteric-RBD-Binder/Top20-Inhibitors.md |
| wiki_drafts/phgdh-pdb-binding-sites.md | ~40 | 2 | content/phgdh-research/phgdh-pdb-binding-sites.md |
| wiki/_generated_hubs/*.md (20 files) | varied | varied | content/*.md (concept hubs) |

## Audit guarantees before publish

- `plan-sync` marks Task 3.4 as DONE only when the files land in `aimed-lab/sdd-wiki` HEAD
- `phgdh_publish.sh` uses rsync WITHOUT --delete for the PHGDH-Allosteric-RBD-Binder dir (human-curated safety)
- Quartz frontmatter validated: every draft has `tier: public` AND `status: published`
- Broken wikilinks scanned; publish aborts if any target doesn't resolve
