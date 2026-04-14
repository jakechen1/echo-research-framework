---
title: Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency
created: 2024-05-22
source: https://arxiv.org/abs/2601.05905
tags: [LLM, Robustness, Truthfulness, Machine Learning, AI]
category: ai, machine-learning, technology
---

# Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency

As [[large-language-models-llms|Large Language Models (LLMs)]] are increasingly integrated into critical real-world decision-making processes, the benchmark for success is shifting. While accuracy is a primary concern, the broader requirement for reliable deployment is the ability to maintain truthful beliefs under [[contextual-perturbations|Contextual Perturbations]].

## The Limitation of Point-wise Evaluation

Current methodologies for evaluating LLM reliability often rely on point-wise confidence metrics, such as [[scientific-graphics-program-synthesis-via-dual-self-consistency-reinforcement-le|Self-Consistency]]. While effective at measuring internal agreement on a specific prompt, these metrics can mask "brittle" beliefs. A model may exhibit perfect consistency on a single data point, yet its underlying factual accuracy can rapidly collapse when faced with minor linguistic or structural changes to the input. This phenomenon creates an "illusion of confidence," where the model appears stable despite lacking a robust knowledge foundation.

## Introducing Neighbor-Consistency Belief (NCB)

To address the lack of structural evaluation, the researchers propose [[neighbor-consistency-belief-ncb|Neighbor-Consistency Belief (NCB)]]. Rather than looking at a single response, NCB serves as a structural measure of belief robustness. It assesses the coherence of a model's responses across a "conceptual neighborhood"—a cluster of related prompts that vary slightly in phrasing or context. 

To benchmark this metric, the study introduces a new cognitive stress-testing protocol. This protocol subjects model outputs to intentional contextual interference, allowing researchers to quantify how much "pressure" a belief can withstand before it degrades. The findings indicate that data segments identified with high NCB scores are significantly more resistant to interference.

## Structure-Aware Training (SAT)

The paper concludes by presenting [[structure-aware-training-sat|Structure-Aware Training (SAT)]], an optimization framework designed to minimize knowledge brittleness. SAT focuses on cultivating context-invariant belief structures, training the model to maintain consistency across the conceptual neighborhood. Experimental results demonstrate that implementing SAT can reduce the