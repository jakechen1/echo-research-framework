---
title: Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation
created: 2024-05-23
source: https://arxiv.org/abs/2604.04894
tags: [RLVR, LLM, Reinforcement Learning, AsymGRPO, Entropy]
category: ai, machine-learning
---

# Rethinking Exploration in RLVR: From Entropy Regularization to Refinement via Bidirectional Entropy Modulation

The research addresses a critical bottleneck in [[reinforcement-learning-with-verifiable-rewards-rlvr|Reinforcement Learning with Verifiable Rewards (RLVR)]]: the phenomenon of "restricted exploration." When training [[large-language-models-llms|Large Language Models (LLMs)]] for reasoning tasks, the policy often converges prematurely to a narrow set of solutions, preventing the model from discovering complex or creative reasoning paths.

While [[rethinking-exploration-in-rlvr-from-entropy-regularization-to-refinement-via-bid|Entropy Regularization]] is the industry standard for encouraging diversity during training