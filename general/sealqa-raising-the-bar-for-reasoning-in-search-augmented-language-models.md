---
title: "SealQA: Raising the __Bar__ for Reasoning in Search-Augmented Language Models"
created: 2025-05-23
source: "https://arxiv.org/abs/2506.01062"
tags: [Benchmark, LLM, Search-Augmented Generation, Reasoning, AI Evaluation]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "SealQA: Raising the __Bar__ for Reasoning in Search-Augmented Language Models"
dc.creator: wiki-pipeline
dc.date: 2025-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/sealqa-raising-the-bar-for-reasoning-in-search-augmented-language-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models

**SealQA** is a novel [[evgeoqa-benchmarking-llms-on-dynamic-multi-objective-geo-spatial-exploration|Benchmark]] designed to evaluate the capabilities of [[sealqa-raising-the-bar-for-reasoning-in-search-augmented-language-models|Search-Augmented Language Models]] (SALMs) when faced with complex, real-world retrieval challenges. Unlike standard evaluations, SealQA focuses on "fact-seeking" questions where the retrieved web search results are intentionally difficult, containing conflicting, noisy, or unhelpful information.

## Benchmark Flavors

The SealQA framework is categorized into three specialized configurations to test different dimensions of model intelligence:

1.  **Seal-0**: The primary evaluation tier, which targets extremely challenging questions where current top-tier [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs), such as GPT-4.1, often approach near-zero accuracy.
2.  **Seal-Hard**: A subset specifically designed to assess rigorous factual accuracy and sophisticated reasoning capabilities.
3.  **LongSeal**: An extension of the benchmark that evaluates [[$pi^2$-structure-originated-reasoning-data-improves-long-context-reasoning-abili|Long-context reasoning]] within "needle-in-a-haystack" scenarios. This tests a model's ability to navigate multi-document environments and extract relevant data from massive datasets.

## Key Findings

The introduction of SealQA has revealed critical limitations in contemporary [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] performance:

*   **Frontier Model Vulnerability**: Even advanced agentic models demonstrate poor performance. For instance, models like **o3** and **o4-mini** achieved accuracies of only 17.1% and 6.3%, respectively, on the Seal-0 tier.
*   **Sensitivity to Noise**: Highly advanced reasoning models, including **DeepSeek-R1-671B** and **o3-mini**, are notably susceptible to errors introduced by noisy search results.
*   **Limits of Test-Time Compute**: The researchers found that increasing [[test-time compute]] does not provide a consistent or reliable path to improved accuracy; performance often plateaus or even declines during extended reasoning attempts.
*   **Retrieval Failures**: In the LongSeal setting, while models are increasingly resistant to the "lost-in-the-middle" phenomenon