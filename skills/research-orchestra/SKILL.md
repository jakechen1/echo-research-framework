---
name: research-orchestra
version: "1.0.0"
description: "Autonomous multi-stage research pipeline inspired by PaperOrchestra (Google, 2026). Conducts literature discovery, citation validation, data analysis, and synthesis. Produces structured research reports with verified PubMed/Semantic Scholar citations."
metadata:
  openclaw:
    emoji: "🔬"
    requires:
      bins: ["python3", "curl"]
    install: []
---

# Research Orchestra Skill

Conduct rigorous, citation-grounded research autonomously. Inspired by PaperOrchestra's multi-agent architecture (Song et al., Google, 2026), adapted for local LLM execution via Ollama on L0.

## When to Use
- "Research X for me" / "Find papers about X"
- "What does the literature say about X?"
- "Do a deep dive on X with real citations"
- "Prepare a literature review on X"
- "Summarize recent findings on X"
- Any request for evidence-based analysis with verified sources

## Architecture (3-Stage Pipeline)

Unlike single-shot LLM responses, this skill decomposes research into specialized stages that run sequentially, each building on the previous output. This mirrors PaperOrchestra's agent separation principle.

### Stage 1: Outline Agent — Research Planning
Given a research question, generate a structured research plan:

1. Parse the research question into 3-5 specific sub-questions
2. Identify key search terms for each sub-question
3. Determine which databases to search (PubMed, Semantic Scholar, arXiv)
4. Define the scope: time range, field, inclusion/exclusion criteria

**Output:** JSON research plan with sub-questions, search terms, and scope.

```bash
# Save research plan
cat > ~/research/<topic-slug>/plan.json << 'EOF'
{
  "topic": "<research question>",
  "sub_questions": ["...", "..."],
  "search_terms": {"pubmed": ["..."], "semantic_scholar": ["..."]},
  "scope": {"years": "2020-2026", "fields": ["..."]},
  "created": "YYYY-MM-DD"
}
EOF
```

### Stage 2: Literature Review Agent — Discovery & Validation
Execute the search plan using real APIs. **Never fabricate citations.**

#### PubMed Search (free, no API key needed)
```bash
# Search PubMed E-utilities
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=10&sort=relevance&term=<ENCODED_QUERY>"

# Get paper details
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=<PMID1>,<PMID2>"

# Get abstract
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=<PMID>"
```

#### Semantic Scholar API (free, rate-limited)
```bash
# Search papers
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=<QUERY>&limit=10&fields=title,authors,year,abstract,url,citationCount,externalIds"

# Get paper details by Semantic Scholar ID
curl -s "https://api.semanticscholar.org/graph/v1/paper/<S2_ID>?fields=title,abstract,authors,year,references,citations"
```

#### Citation Validation (Critical — PaperOrchestra's key innovation)
Every citation MUST be validated:
1. Search by title/author on Semantic Scholar
2. Verify the paper exists and matches
3. Extract the DOI or PubMed ID
4. Build a verified citation entry with real URL

**Output:** Save validated citations to `~/research/<topic>/citations.json`:
```json
[
  {
    "title": "...",
    "authors": "First Author et al.",
    "year": 2024,
    "journal": "...",
    "pmid": "12345678",
    "doi": "10.1234/...",
    "url": "https://pubmed.ncbi.nlm.nih.gov/12345678/",
    "abstract": "...",
    "relevance": "Directly supports sub-question 1"
  }
]
```

### Stage 3: Synthesis Agent — Analysis & Report
Synthesize findings into a structured research report:

1. Group papers by sub-question/theme
2. Identify consensus findings, contradictions, and gaps
3. Write a narrative synthesis (not just a list of papers)
4. Include a "Key Findings" summary
5. Flag limitations and future directions

**Output:** Save report to `~/research/<topic>/report.md` AND `~/reports/<date>-<topic>.md` (for Box sync).

## Report Template

```markdown
---
title: "Research Report: <Topic>"
date: YYYY-MM-DD
type: research-report
citations: <count>
---

# <Research Question>

## Key Findings
- Finding 1 (Author et al., Year)
- Finding 2 (Author et al., Year)

## Background
<Context and significance>

## Literature Analysis

### <Sub-question 1>
<Narrative synthesis with inline citations>

### <Sub-question 2>
<Narrative synthesis with inline citations>

## Discussion
<Synthesis across sub-questions, contradictions, gaps>

## Future Directions
<Open questions, emerging areas>

## References
1. Author et al., Year. Title. Journal. https://doi.org/...
2. ...
```

## Integration with Wiki Builder

After completing research, optionally generate wiki pages:
```bash
# Use wiki-builder skill to create wiki pages from research findings
HOME=/Users/jakeclaw /Users/jakeclaw/.hermes-venv/bin/python \
  /Users/jakeclaw/.hermes/scripts/wiki_builder.py start \
  "<research topic summary>" --depth 2 --pages-per-level 15
```

## Important Rules

1. **NEVER fabricate citations.** Every reference must be validated via PubMed or Semantic Scholar API.
2. **Always show your work.** Save intermediate outputs (plan, citations, report) to ~/research/<topic>/.
3. **Rate limit API calls.** Wait 1s between PubMed calls, 2s between Semantic Scholar calls.
4. **Prefer recent work.** Default to papers from the last 5 years unless historical context is needed.
5. **Be honest about limitations.** If search results are sparse, say so. Don't pad with irrelevant papers.
6. **Save reports to ~/reports/ for Box sync.** Reports automatically sync to Box hourly.
