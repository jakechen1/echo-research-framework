---
title: Discrete Flow Matching Policy Optimization (DoMinO)
created: 2024-05-23
source: https://arxiv.org/abs/2604.06491
tags: [reinforcement-learning, flow-matching, generative-models, dna-design, policy-optimization]
category: machine-learning
---

# Discrete Flow Matching Policy Optimization (DoMinO)

The **Discrete Flow Matching Policy Optimization (DoMinO)** is a newly introduced unified framework designed for the [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) fine-tuning of [[discrete-flow-matching-policy-optimization|Discrete Flow Matching]] (DFM) models. As generative modeling for discrete sequences becomes increasingly important in fields such as [[bioinformatics|Bioinformatics]] and [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]], DoMinO provides a method to steer these models toward specific rewards while maintaining the integrity of the learned distribution.

## Methodology

The fundamental innovation of DoMinO is the conceptualization of the DFM sampling procedure as a multi-step [[markov-decision-process|Markov Decision Process]] (MDP). By viewing the sampling trajectory through this lens, the authors provide a transparent reformulation of reward maximization into a robust RL objective. 

Key technical features include:
* **Sampler Preservation:** Unlike many prior methods, DoMinO preserves the original DFM samplers, ensuring compatibility with existing architectures.
* **Unbiased Objectives:** The framework avoids the use of biased auxiliary estimators and the likelihood surrogates that are frequently observed in previous RL fine-tuning approaches.
* **Regularization against Policy Collapse:** To prevent the model from overfitting to rewards (a phenomenon known as policy collapse), the framework introduces new **total-variation regularizers**. These regularizers ensure that the fine-tuned distribution remains mathematically close to the original pre-trained distribution, preserving the "naturalness" of the output.

## Theoretical and Experimental Results

The authors establish rigorous theoretical foundations for the framework, providing an upper bound on the discretization error of DoMinO and establishing tractable upper bounds for the proposed regularizers.

In practical applications, DoMinO was evaluated on the complex task of **regulatory DNA sequence design**. The goal in this domain is to generate sequences with high predicted enhancer activity. Experimental results demonstrate that DoMinO achieves significantly stronger predicted enhancer activity and superior sequence naturalness compared to previous state-of-the-art reward-driven baselines. The integration of regularization specifically improved the alignment with natural sequence distributions while maintaining high functional performance, establishing DoMinO as a robust framework for controllable discrete sequence generation.