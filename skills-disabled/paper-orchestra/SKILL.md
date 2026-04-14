---
name: paper-orchestra
version: "1.0.0"
description: "Multi-agent paper writing pipeline inspired by Google's PaperOrchestra (Song et al., 2026). Transforms research ideas and experimental data into submission-ready LaTeX manuscripts with verified citations, generated figures, and iterative peer-review refinement."
metadata:
  openclaw:
    emoji: "📝"
    requires:
      bins: ["python3", "curl", "pdflatex"]
    install: []
---

# Paper Orchestra — AI Research Paper Writing

Transform research ideas and experimental data into submission-ready LaTeX manuscripts. Based on Google's PaperOrchestra framework (Song et al., 2026), adapted for local execution with Ollama (Gemma 4 / Qwen 3.5).

## When to Use
- "Write a paper about X" / "Draft a manuscript on X"
- "Turn my research into a paper"
- "Help me write the related work / introduction / methods section"
- "Create a submission-ready manuscript"
- "Write up these experimental results"
- User provides an idea + experimental data and wants a paper

## Architecture: 5-Stage Pipeline

Following PaperOrchestra's proven multi-agent decomposition. Each stage produces artifacts that feed into the next. Steps 2 and 3 can run in parallel.

```
Input Materials          Step 1          Steps 2+3 (parallel)      Step 4          Step 5
                       ┌─────────┐    ┌──────────────────┐    ┌───────────┐    ┌───────────┐
Idea Summary (I) ──┐   │ Outline │    │ Plotting Agent   │    │ Section   │    │ Content   │
Exp. Log (E) ──────┼──►│ Agent   │──┬►│ (figures/plots)  │──┬►│ Writing   │──►│ Refinement│──► Final
LaTeX Template (T)─┤   │         │  │ │                  │  │ │ Agent     │    │ Agent     │    Paper
Guidelines (G) ────┘   └─────────┘  │ ├──────────────────┤  │ └───────────┘    └───────────┘
                                    │ │ Lit Review Agent  │  │
                                    └►│ (citations/refs)  │──┘
                                      └──────────────────┘
```

### Step 1: Outline Agent — Structure Planning

Generate a JSON outline from the user's idea and experimental data:

```
Given the research idea and experimental results, create:
(a) Visualization plan: what plots/diagrams to generate, data sources, figure types
(b) Literature search strategy: macro-level context + micro-level methodology keywords
(c) Section-level writing plan: content bullets for each section, citation hints
```

**Prompt the LLM:**
```
You are a senior research advisor planning a paper manuscript.

IDEA: <user's idea summary>
EXPERIMENTAL RESULTS: <user's data/logs>
TARGET VENUE: <conference/journal>

Create a detailed paper outline as JSON:
{
  "title": "proposed paper title",
  "sections": [
    {"name": "Introduction", "bullets": ["...", "..."], "citations_needed": ["topic1", "topic2"]},
    {"name": "Related Work", "subsections": ["area1", "area2"], "search_terms": ["..."]},
    {"name": "Method", "bullets": ["...", "..."]},
    {"name": "Experiments", "tables": ["..."], "figures": ["..."]},
    {"name": "Conclusion", "bullets": ["..."]}
  ],
  "figures_to_generate": [
    {"type": "conceptual_diagram", "description": "system architecture"},
    {"type": "bar_chart", "data_source": "table 1", "description": "accuracy comparison"}
  ],
  "lit_search_strategy": {
    "macro_context": ["broad field terms"],
    "micro_methods": ["specific technique terms"],
    "baselines": ["competing method names"]
  }
}
```

Save to: `~/research/<paper-slug>/outline.json`

### Step 2: Plotting Agent — Figure Generation (parallel with Step 3)

Generate figures using Python matplotlib/seaborn:

```python
# For data plots: generate Python code, execute, save PNG
import matplotlib.pyplot as plt
import numpy as np

# Extract data from experimental log
data = {...}  # parsed from user's data

plt.figure(figsize=(8, 5))
# ... plot code ...
plt.savefig('figures/fig1_results.png', dpi=300, bbox_inches='tight')
```

For conceptual diagrams: generate TikZ or describe for manual creation.

Save figures to: `~/research/<paper-slug>/figures/`

### Step 3: Literature Review Agent — Citation Discovery (parallel with Step 2)

**This is the most critical stage.** Following PaperOrchestra's API-grounded citation approach:

1. **Search** using terms from the outline's lit_search_strategy
2. **Validate** every paper via Semantic Scholar API (get S2 ID, verify existence)
3. **Fetch abstracts** for relevant papers
4. **Build BibTeX** file with verified entries only
5. **Draft Introduction and Related Work** sections using validated citations

```bash
# Search PubMed
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&sort=relevance&term=<QUERY>"

# Validate on Semantic Scholar (get canonical metadata)
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=<TITLE>&limit=1&fields=title,authors,year,externalIds,abstract,venue"

# Build BibTeX entry from validated metadata
```

**Output:**
- `~/research/<paper-slug>/references.bib` — verified BibTeX
- `~/research/<paper-slug>/related_work.tex` — drafted Introduction + Related Work

### Step 4: Section Writing Agent — Full Manuscript Draft

Assemble the complete LaTeX manuscript:

1. Use the outline (Step 1) as the structural guide
2. Integrate figures from Step 2 with proper `\includegraphics` and captions
3. Include the BibTeX from Step 3 with `\cite{}` commands
4. Extract data tables from experimental log into LaTeX `tabular` environments
5. Write Abstract, Method, Experiments, Discussion, Conclusion sections

**Prompt pattern for each section:**
```
You are writing the [SECTION] of a research paper.

PAPER OUTLINE: <from step 1>
RELATED WORK: <from step 3>
EXPERIMENTAL DATA: <from user input>
AVAILABLE FIGURES: <from step 2>
CITATION BANK: <BibTeX entries from step 3>

Write the [SECTION] in LaTeX. Requirements:
- Use \cite{} for all claims from prior work
- Reference figures with \ref{fig:...}
- Reference tables with \ref{tab:...}
- Be specific and technical
- Use the venue's style conventions
```

Save to: `~/research/<paper-slug>/manuscript.tex`

### Step 5: Content Refinement Agent — Iterative Review

Simulate peer review and iteratively improve:

1. **Review prompt:** Act as a reviewer for [VENUE]. Score this manuscript on: originality, quality, clarity, significance, soundness, presentation (1-4 each). List specific weaknesses.

2. **Revision prompt:** Given these reviewer comments, revise the manuscript. Address each weakness specifically.

3. **Accept/reject:** If overall score improves or ties with non-negative sub-axis changes, keep revision. Otherwise revert.

4. **Iterate** up to 3 rounds (diminishing returns after that).

Save to: `~/research/<paper-slug>/manuscript_v{N}.tex`

## File Organization

```
~/research/<paper-slug>/
  plan.json          # Step 1 outline
  outline.json       # Detailed section outline
  citations.json     # Validated citations
  references.bib     # BibTeX file
  related_work.tex   # Intro + Related Work draft
  figures/           # Generated plots and diagrams
  manuscript.tex     # Full LaTeX manuscript
  manuscript_v2.tex  # After refinement round 1
  manuscript_v3.tex  # After refinement round 2
  manuscript.pdf     # Compiled PDF (if pdflatex available)

~/reports/<date>-paper-<slug>.md  # Summary for Box sync
```

## Compilation

```bash
# Compile LaTeX to PDF (if pdflatex available on W0)
cd ~/research/<paper-slug>
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

If `pdflatex` is not available, save the `.tex` and `.bib` files — the user can compile locally or on Overleaf.

## Integration Points

- **Wiki builder:** After paper is drafted, generate wiki pages from the research (use `wiki-builder` skill)
- **Box sync:** Save summary report to `~/reports/` for automatic Box upload
- **GitHub:** Push manuscript to a repo branch for version control
- **Obsidian:** Research notes and outlines viewable in the wiki vault

## Important Rules

1. **NEVER fabricate citations.** Every `\cite{}` must reference a validated BibTeX entry.
2. **API-grounded only.** All references validated via PubMed or Semantic Scholar.
3. **Save incrementally.** Save after each stage so work isn't lost.
4. **Rate limit APIs.** 1s between PubMed calls, 2s between Semantic Scholar.
5. **Be honest.** If the experimental data doesn't support a claim, say so.
6. **Follow venue guidelines.** Respect page limits, formatting, and style requirements.
7. **LaTeX best practices.** Use proper float placement, cross-references, and bibliography management.
