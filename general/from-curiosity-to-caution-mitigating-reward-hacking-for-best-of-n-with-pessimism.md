---
title: From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism
created: 2024-05-22
source: https://arxiv.org/abs/2604.04648
tags: [machine-learning, LLM, reward-hacking, reinforcement-learning, uncertainty-estimation]
category: machine-learning
author: wiki-pipeline
dc.title: "From Curiosity to Caution: Mitigating Reward Hacking for Best-of-N with Pessimism"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/from-curiosity-to-caution-mitigating-reward-hacking-for-best-of-n-with-pessimism.md
dc.language: en
dc.rights: CC-BY-4.0
---

# From Curiosity to Caution

The research paper "From Curiosity to Caution" addresses a critical bottleneck in the scaling of [[Inference-time compute]]: the phenomenon of **reward hacking**. As [[Large Language Models (LLMs)]] are increasingly optimized through [[Best-of-N sampling]]—a process where $N$ candidates are generated and the highest-scoring response via a [[consistrm-improving-generative-reward-models-via-consistency-aware-self-training|Reward Model]] is selected—performance often degrades as $N$ increases. This degradation occurs because the selection process begins to favor responses that exploit inaccuracies in the reward model rather than those that represent true linguistic or logical quality.

## The Problem: Reward Hacking
In [[Best-of-N sampling]], the objective is to use additional compute to find the optimal output. However, as the sample size grows, the probability of encountering an "outlier" response that the reward model incorrectly assigns a high score increases. This "over-optimization" creates a gap between the reward model's internal metrics and actual task performance.

## The Solution: The "Caution" Framework
The authors propose a novel approach termed **caution**, which is inspired by the principle of **pessimism** found in [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]]. While traditional "curiosity" models use prediction error as a signal for novelty and exploration, the "caution" framework treats prediction error as a signal of **[[Out-of-Distribution (OOD)]]** uncertainty.

### Implementation Mechanism
The methodology involves two primary steps:
1. **Error Model Training:** An error model is trained on a distribution of "typical" or high-quality responses.
2. **Reward Penalization:** During inference, the error model evaluates the candidate responses. If the error model exhibits high prediction error on a specific candidate, it suggests the response is atypical or potentially a "hacked" sample. The system then applies a penalty to the reward estimate for that candidate.

## Results and Implications
Extensive empirical evaluations demonstrate that "caution" provides a computationally efficient way to mitigate reward hacking without the need for heavy-handed [[distributional regularization]] or significantly larger reward models. Furthermore, the paper provides a theoretical analysis in a linear setting, proving that caution can demonstrably outperform standard sampling approaches. This work also suggests that error-based novelty detection can serve as a robust mechanism for [[OOD detection]] in advanced AI architectures.