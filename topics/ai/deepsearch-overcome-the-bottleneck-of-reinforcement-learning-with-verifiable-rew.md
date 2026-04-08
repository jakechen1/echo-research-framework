---
title: "DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search"
created: 2024-05-22
source: https://arxiv.org/abs/2509.25454
tags: [reinforcement-learning, MCTS, large-language-models, algorithmic-efficiency]
category: ai
---

# DeepSearch

DeepSearch is a specialized framework designed to address the "training plateau" phenomenon observed in [[Reinforcement Learning with Verifiable Rewards]] (RLVR). As [[Large Language Models]] are developed for complex reasoning, researchers often encounter a bottleneck where increased computational investment fails to yield significant performance gains. This is largely due to sparse exploration patterns in current RLVR practices, where models rely on limited rollouts that miss critical reasoning paths.

## The Innovation: Training-Time Search

Unlike traditional methodologies that utilize [[Monte Carlo Tree Search]] (MCTS) only during the inference stage, DeepSearch integrates structured search directly into the training loop. By embedding search capabilities during the optimization process, the framework enables systematic exploration and more precise [[Credit Assignment]] across individual reasoning steps. This approach ensures a more comprehensive coverage of the solution space than standard gradient-based or rollout-based updates.

## Key Technical Contributions

The DeepSearch architecture introduces three fundamental components to optimize training efficiency and efficacy:

1.  **Global Frontier Selection Strategy:** A method to prioritize the most promising nodes within the search tree, focusing computational resources on high-potential reasoning branches.
2.  **Entropy-based Guidance:** A selection mechanism that utilizes entropy to identify confident paths, providing high-quality supervision for the model.
3.  **Adaptive Replay Buffer Training:** An efficient training loop featuring solution caching, which optimizes the use of previously explored successful paths.

## Experimental Results

The effectiveness of DeepSearch has been validated on rigorous [[Mathematical Reasoning]] benchmarks. The framework achieved a state-of-the-art average accuracy of 62.9