---
title: Beyond Surface Judgments: Human-Grounded Risk Evaluation of LLM-Generated Disinformation
created: 2024-05-22
source: https://arxiv.org/abs/2604.06820
tags: [LLM, disinformation, AI evaluation, human-alignment, proxy-validity]
category: ai
author: wiki-pipeline
dc.title: "Beyond Surface Judgments: Human-Grounded Risk Evaluation of LLM-Generated Disinformation"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/beyond-surface-judgments-human-grounded-risk-evaluation-of-llm-generated-disinfo.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Beyond Surface Judgments: Human-Grounded Risk Evaluation of LLM-Generated Disinformation

The rapid advancement of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) has enabled the production of persuasive, large-scale narratives, significantly increasing the potential for automated [[disinformation]] campaigns. A critical challenge in [[iatrobench-pre-registered-evidence-of-iatrogenic-harm-from-ai-safety-measures|AI safety]] is assessing the risk of this content—specifically, understanding how human readers receive and react to such narratives. Due to the high cost of human-in-the-loop evaluation, researchers and developers are increasingly using "LLM judges" as a low-cost substitute to simulate human judgment.

This paper investigates the validity of this approach by treating the use of automated evaluators as a [[proxy-validity]] problem. The researchers audited eight frontier LLM judges against 2,043 paired human ratings derived from 290 aligned articles to determine how closely machine-based scoring tracks actual human responses.

### Key Findings

The study reveals a persistent and significant gap between human perception and LLM-based evaluation:

* **Divergent Textual Signals:** LLM judges rely on different linguistic features than humans. While humans may be swayed by the emotional impact of a narrative, judges tend to prioritize [[logic|logical rigor]] and are more likely to penalize "emotional intensity."
* **Systematic Harshness:** Compared to human readers, LLM judges act as much harsher critics, often failing to recover the item-level rankings established by human participants.
* **The Illusion of Consensus:** One of the most critical findings is that LLM judges demonstrate much higher agreement with each other than they do with human readers. This suggests that high internal agreement within a group of AI models is not evidence of their validity as a proxy for human behavior.

### Implications

These results suggest that relying on LLM judges to moderate or assess the risk of disinformation could lead to a significant failure in identifying truly impactful content. If the metrics used to evaluate "harmful" content are fundamentally decoupled from human psychological responses, the industry may develop a false sense of security, leaving human populations vulnerable to disinformation that passes AI scrutiny but succeeds in persuading human audiences.