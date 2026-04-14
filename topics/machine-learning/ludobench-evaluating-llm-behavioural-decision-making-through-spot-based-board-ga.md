---
title: LUDOBENCH: Evaluating LLM Behavioural Decision-Making Through Spot-Based Board Game Scenarios in Ludo
created: 2024-05-24
source: https://arxiv.org/abs/2604.05681
tags: [LLM, Benchmarking, Strategic Reasoning, Game Theory, Stochastic Games]
category: ai, machine-learning
---

# LUDOBENCH: Evaluating LLM Behavioural Decision-Making Through Spot-Based Board Game Scenarios in Ludo

LudoBench is a novel benchmarking framework designed to evaluate the [[strategic-reasoning|Strategic Reasoning]] capabilities of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) within the context of Ludo—a stochastic, multi-agent board game. Unlike traditional benchmarks that focus on linguistic proficiency, LudoBench assesses how models navigate complex game mechanics, such as piece capture, safe-square navigation, and progress toward a home path.

## Methodology

The framework comprises 480 handcrafted "spot scenarios" organized into 12 distinct decision categories, each isolating a specific strategic choice. To evaluate the models, the researchers contributed a fully functional 4-player Ludo simulator capable of supporting various agent types, including Random, Heuristic, and [[game-theory|Game Theory]] agents. A key component of the benchmark is the implementation of an **Expectiminimax search** agent, which provides a principled strategic ceiling via depth-limited lookahead, serving as the gold standard for comparison.

## Key Findings and Behavioral Archetypes

The study evaluated six models across four model families, uncovering significant gaps between [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] behavior and optimal strategic play. The researchers found that models align with the game-theory baseline only 40-46% of the time. Specifically, the models exhibited two distinct behavioral archetypes:

*   **Finishers:** These models focus on completing pieces but neglect broader board development.
*   **Builders:** These models prioritize developing their position but neglect the final progression of pieces.

Crucially, neither archetype captures the full spectrum of the optimal strategy. Furthermore, the study identified a major vulnerability in [[optimizing-llm-prompt-engineering-with-dspy-based-declarative-learning|Prompt Engineering]]: **prompt-sensitivity**. When presented with "grudge framing"—where identical board states are described using historical context of conflict—the models displayed measurable shifts in decision-making.

## Significance

LudoBench provides a lightweight and interpretable framework for studying [[before-we-trust-them-decision-making-failures-in-navigation-of-foundation-models|Decision-Making]] under [[stochastic-processes|Stochastic Processes]] and uncertainty. It serves as a vital tool for researchers investigating the limits of [[strategic-persuasion-with-trait-conditioned-multi-agent-systems-for-iterative-le|Multi-Agent Systems]] and the robustness of LLMs in environments requiring long-term planning and adaptation to random variables.

The dataset and simulation code are available for further research in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]].