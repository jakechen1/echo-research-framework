---
title: "Lost in Cultural Translation: Do LLMs Struggle with Math Across Cultural Contexts?"
created: 2024-05-22
source: https://arxiv.org/abs/2503.18018
tags: [LLM, cultural bias, mathematical reasoning, algorithmic fairness, AI evaluation]
category: ai
author: wiki-pipeline
dc.title: "Lost in Cultural Translation: Do LLMs Struggle with Math Across Cultural Contexts?"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/lost-in-cultural-translation-do-llms-struggle-with-math-across-cultural-contexts.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Lost in Cultural Translation: Do LLMs Struggle with Math Across Cultural Contexts?

The research paper "Lost in Cultural Translation" investigates a critical yet overlooked dimension of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] performance: the impact of cultural context on [[do-mllms-really-understand-space-a-mathematical-reasoning-evaluation|Mathematical Reasoning]]. While mathematical logic is theoretically universal, this study demonstrates that the performance of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) is significantly influenced by the cultural familiarity of the problem's phrasing.

### Methodology
The researchers evaluated 14 state-of-the-art models from major developers, including [[openai-backs-illinois-bill-that-would-limit-when-ai-labs-can-be-held-liable|OpenAI]], [[anthropic-expands-partnership-with-google-and-broadcom-for-next-gen-compute|Anthropic]], [[anthropic-expands-partnership-with-google-and-broadcom-for-next-gen-compute|Google]], [[allosteric-regulation-in-metabolic-enzymes|Meta]], [[Mistral]], and [[microsoft-abruptly-terminates-veracrypt-account-halting-windows-updates|Microsoft]]. To isolate cultural influence, the team created six culturally adapted variants of the [[GSM8K]] benchmark, specifically targeting the contexts of:
* Haiti
* Moldova
* Pakistan
* Solomon Islands
* Somalia
* Suriname

The experimental design involved systematically replacing cultural entities—such as names, local foods, and geographical landmarks—within 1,198 math questions. Crucially, the underlying mathematical operations and numerical values remained unchanged across all variants, ensuring that any performance fluctuations were attributable to cultural "translation" rather than changes in computational complexity.

### Key Findings
The study revealed statistically significant performance reductions (p < 0.01), indicating that [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models are not culturally neutral. Accuracy drops ranged from a negligible 0.3% (observed in Claude 3.5 Sonnet) to a substantial 5.9% (observed in LLaMA 3.1-8B).

Analysis of 18,887 instances identified two primary failure modes:
1. **Reasoning Errors (54.7%):** The model fails to follow the logical steps of the problem.
2. **Calculation Errors (34.5%):** The model performs the arithmetic incorrectly.

Interestingly, the study found evidence of "cultural advantage" in specific models. For instance, Mistral Saba demonstrated superior performance on Pakistan-adapted problems, likely due to higher exposure to Middle Eastern and South Asian datasets during [[AI Training]].

### Implications
These findings suggest that current [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] harbor significant [[Algorithmic Bias]] regarding global cultural contexts. To achieve robust, globally applicable performance, the industry must prioritize [[Data Diversity]] in training pipelines to prevent mathematical reasoning from breaking when encountering unfamiliar cultural landscapes.