---
title: Offline RL for Adaptive Policy Retrieval in Prior Authorization
created: 2024-05-23
source: https://arxiv.org/abs/2604.05125
tags: [offline reinforcement learning, retrieval-augmented generation, prior authorization, MDP, DPO]
category: machine-learning
---

# Offline RL for Adaptive Policy Retrieval in Prior Authorization

The paper "Offline RL for Adaptive Policy Retrieval in Continuous Policy Interpretation" addresses the inherent inefficiencies in traditional [[retrieval-augmented-generation-rag|Retrieval-Augmented Generation (RAG)]] systems used in [[offline-rl-for-adaptive-policy-retrieval-in-prior-authorization|Prior Authorization]] (PA). Standard retrieval models often utilize a static top-$K$ strategy, which retrieves a fixed number of document sections. This approach is prone to either missing critical information or gathering excessive, irrelevant data, leading to sub-optimal decision-making.

## Methodology

The researchers propose a paradigm shift by modeling the retrieval process as a [[markov-decision-process-mdp|Markov Decision Process (MDP)]]. Instead of a single-step retrieval, an autonomous agent is trained to perform adaptive retrieval. The agent interacts with a candidate set of policy chunks, iteratively deciding whether to select an additional chunk or to stop and issue a final decision. 

The training utilizes an [[epistemic-robust-offline-reinforcement-learning|Offline Reinforcement Learning]] framework, where the reward function is designed to balance two competing objectives:
1. **Decision Correctness**: Ensuring the final authorization decision is accurate.
2. **Retrieval Cost**: Minimizing the number of steps (computational/latency cost) taken during retrieval.

## Experimental Results

The study evaluates several algorithms using trajectories generated from synthetic PA requests based on [[cms-coverage-data|CMS coverage data]]. The researchers compared [[conservative-q-learning-cql|Conservative Q-Learning (CQL)]], [[implicit-q-learning-iql|Implicit Q-Learning (IQL)]], and [[direct-preference-optimization-dpo|Direct Preference Optimization (DPO)]] against a [[behavioral-cloning-bc|Behavioral Cloning (BC)]] baseline.

Key findings include:
* **Accuracy**: [[conservative-q-learning-cql|Conservative Q-Learning (CQL)]] achieved 92% decision accuracy, a significant improvement over traditional fixed-$K$ baselines.
* **Efficiency**: [[implicit-q-learning-iql|Implicit Q-Learning (IQL)]] maintained high accuracy while reducing retrieval steps by 44%.
* **Optimization**: [[direct-preference-optimization-dpo|Direct Preference Optimization (DPO)]] emerged as the most efficient "selective-accurate" model. It matched the 92% accuracy of CQL but required 47% fewer retrieval steps (10.6 vs 20.0).

The study concludes that [[preference-based-learning|Preference-based Learning]] is necessary to move beyond simple imitation and achieve a state of optimal efficiency on the [[pareto-frontier|Pareto frontier]], particularly when managing the trade-off between information density and retrieval latency.