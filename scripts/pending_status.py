#!/usr/bin/env python3
"""Return JSON counts of {total, new, changed, sample_files} for Publish."""
import hashlib, json, pathlib, sys

SOURCES = [
    ("PHGDH-Allosteric-RBD-Binder",
     pathlib.Path("/Users/jakeclaw/wiki/projects/PHGDH-Allosteric-RBD-Binder"),
     pathlib.Path("/Users/jakeclaw/sdd-wiki/content/PHGDH-Allosteric-RBD-Binder")),
    ("phgdh-research",
     pathlib.Path("/Users/jakeclaw/wiki/projects/phgdh-research"),
     pathlib.Path("/Users/jakeclaw/sdd-wiki/content/phgdh-research")),
]

def sha(f):
    h = hashlib.sha256()
    with f.open("rb") as fh:
        for c in iter(lambda: fh.read(65536), b""): h.update(c)
    return h.hexdigest()[:16]

total = new = changed = 0
samples = []
for label, local, remote in SOURCES:
    if not local.exists(): continue
    for f in sorted(local.rglob("*.md")):
        total += 1
        rel = f.relative_to(local)
        r = remote / rel
        if not r.exists():
            new += 1
            if len(samples) < 5:
                samples.append({"file": f"{label}/{rel}", "status": "new"})
        else:
            if sha(f) != sha(r):
                changed += 1
                if len(samples) < 5:
                    samples.append({"file": f"{label}/{rel}", "status": "changed"})

print(json.dumps({"total": total, "new": new, "changed": changed, "samples": samples}))
