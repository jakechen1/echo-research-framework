---
title: Lost in Cultural Translation: Do LLMs Struggle with Math Across Cultural Contexts?
created: 2024-05-22
source: https://arxiv.org/abs/2503.18018
tags: [LLM, algorithmic-bias, mathematics, cultural-sensitivity]
category: ai
---

# Lost in Cultural Translation: Do LLMs Struggle with Math Across Cultural Contexts?

## Overview
Recent research (arXiv:2503.18018) investigates whether the [[Mathematical Reasoning]] capabilities of [[Large Language Models]] (LLMs) are influenced by cultural context. While mathematics is often viewed as a universal language, this study demonstrates that LLM performance is significantly sensitive to the cultural entities—such as names, foods, and locations—embedded within word problems.

## Methodology
The researchers tested 14 prominent models from major AI labs, including [[OpenAI]], [[Anthropic]], [[Google]], [[Meta]], and [[Mistral]]. To isolate cultural influence from mathematical complexity, the team created six culturally adapted variants of the [[GSM8K]] benchmark. These variants specifically integrated contexts from:
* Haiti
* Moldova
* Pakistan
* Solomon Islands
* Somalia
* Suriname

The study systematically replaced cultural markers in 1,198 questions while strictly preserving all numerical values and mathematical operations. This ensures that any drop in accuracy is a result of cultural unfamiliarity rather than changes in the underlying logic.

## Key Findings
The study found statistically significant performance reductions (p < 0.01) across the evaluated models. Accuracy drops ranged from a negligible 0.3% (Claude 3.5 Sonnet) to a substantial 5.9% (LLaMA 3.1-8B) when models encountered unfamiliar cultural contexts.

A quantitative error analysis of 18,887 instances revealed two primary failure modes:
* **Reasoning Errors:** 54.7% of failures were due to breakdowns in logical processing.
* **Calculation Errors:** 34.5% of failures were due to simple arithmetic mistakes.

Notably, the research observed that model performance correlates with [[Training Data]] exposure. For example, Mistral Saba outperformed larger models on Pakistan-adapted problems, suggesting that higher exposure to South Asian and Middle Eastern contexts during pre-training can mitigate cultural performance gaps.

## Implications
These findings highlight a significant form of [[Algorithmic Bias]] where mathematical "intelligence" is tethered to Western-centric or specific cultural datasets. To achieve robust, global [[Artificial Intelligence]], the industry must move toward more diverse and culturally inclusive [[Dataset]] curation to ensure performance remains stable across all global contexts.