---
title: Self-Preference Bias in Rubric-Based Evaluation of Large Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.06996
tags: [ai, machine-learning, bias, evaluation-metrics]
author: wiki-pipeline
dc.title: "Self-Preference Bias in Rubric-Based Evaluation of Large Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/self-preference-bias-in-rubric-based-evaluation-of-large-language-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Self-Preference Bias in Rubric-Based Evaluation of Large Language Models

The rise of the [[beyond-llm-as-a-judge-deterministic-metrics-for-multilingual-generative-text-eva|LLM-as-a-judge]] paradigm has established a new standard for evaluating [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]]. However, this approach is susceptible to **Self-Preference Bias (SPB)**, a phenomenon where judging models exhibit a tendency to favor outputs produced by themselves or their model families. This research focuses on a specific, emerging subset of evaluation: **rubric-based evaluation**, where judges issue binary (pass/fail) verdicts on individual criteria rather than providing holistic scores.

### Key Research Findings

The study demonstrates that SPB is not merely a byproduct of subjective interpretation but persists even in highly controlled environments:

*   **Persistence in Objective Settings:** Using **IFEval**—a benchmark featuring programmatically verifiable rubrics—the researchers found that SPB remains significant even when evaluation criteria are entirely objective. In scenarios where the generator failed to meet a specific requirement, the judge was up to 50% more likely to incorrectly mark the output as "satisfied" if the output originated from its own model family.
*   **Impact on Subjective Benchmarks:** On **HealthBench**, a medical chat benchmark utilizing subjective rubrics, SPB was