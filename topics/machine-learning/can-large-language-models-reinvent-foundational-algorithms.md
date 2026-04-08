title: Can Large Language Models Reinvent Foundational Algorithms?
created: 2024-05-22
source: https://arxiv.org/abs/2604.05716
tags: [LLM, Unlearning, Reinforcement Learning, Algorithms, AI Research]
category: ai

# Can Large Language Models Reinvent Foundational Algorithms?

The ability of [[Large Language Models]] (LLMs) to move beyond simple pattern recognition toward true foundational innovation remains a central question in [[Artificial Intelligence]] research. This article examines whether LLMs possess the capacity to rediscover fundamental [[Computer Science]] algorithms after having that knowledge intentionally removed from their training parameters.

## The Unlearn-and-Reinvent Pipeline

To test the limits of algorithmic reinvention, researchers developed the **Unlearn-and-Reinvent** pipeline. This methodology employs a GRPO-based, on-policy [[Machine Learning]] unlearning technique. The process involves two distinct phases:

1.  **Unlearning:** Specific foundational algorithms, such as [[Dijkstra's Algorithm]] or [[Euclid's Algorithm]], are stripped from the LLM's pretrained knowledge base using targeted unlearning methods.
2.  **Reinvention:** The "cleansed" model is placed in a controlled environment to determine if it can reconstruct the logic of the algorithm through autonomous reasoning.

## Experimental Results

The study evaluated three strong open-weight models across varying levels of assistance (hints). The most notable results were observed in the **Qwen3-4B-Thinking-2507** model:

*   **Zero Hints:** The model successfully reinvented