---
title: "IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.05157"
tags: [ai, machine-learning, technology, autonomous-agents, reward-models]
category: [ai, machine-learning, technology]
---

# IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents

**IntentScore** is a novel "plan-aware" [[consistrm-improving-generative-reward-models-via-consistency-aware-self-training|Reward Model]] designed to solve the problem of cascading errors in [[computer-use-agents-cuas|Computer-Use Agents (CUAs)]]. As [[large-language-models-llms|Large Language Models (LLMs)]] are increasingly deployed to execute [[gui-operations|GUI Operations]] within desktop environments, they face a significant limitation: they often generate actions without a mechanism to evaluate the quality or correctness of those actions. This lack of self-correction leads to irreversible mistakes that propagate through subsequent execution steps, ultimately causing task failure.

### Architecture and Methodology

IntentScore addresses this by introducing an architecture that embeds the agent's planning intent directly into the action encoder. This allows the model to distinguish between candidate actions that might look identical in terms of GUI state but differ based on their underlying rationales. 

The model was trained using 398,000 offline GUI interaction steps spanning three different operating systems. The training process utilizes two complementary objectives to ensure high-fidelity evaluation:
1. **Contrastive Alignment:** This objective ensures that the proposed action is relevant to the current environmental state.
2. **Margin Ranking:** This objective focuses on the precision of action correctness, helping the model rank better actions higher than suboptimal ones.

### Performance and Generalization

The effectiveness of IntentScore was validated through rigorous testing, achieving a **97.5% pairwise discrimination accuracy** on held-out evaluation sets. 

One of the most significant findings of the research is the model's superior generalization capabilities. When deployed as a re-ranker for [[agent-s3|Agent S3]] on the [[osworld|OSWorld]] benchmark—an environment and task distribution entirely unseen during the training phase—IntentScore demonstrated a **6.9 percentage point increase** in the task success rate. This indicates that reward estimation learned from heterogeneous offline trajectories is highly effective for scaling [[claw-eval-toward-trustworthy-evaluation-of-autonomous-agents|Autonomous Agents]] to new, complex environments.

### Related Topics
[[large-language-models-llms|Large Language Models (LLMs)]]
[[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
[[claw-eval-toward-trustworthy-evaluation-of-autonomous-agents|Autonomous Agents]]
[[gui-operations|GUI Operations]]
[[consistrm-improving-generative-reward-models-via-consistency-aware-self-training|Reward Models]]
[[osworld|OSWorld]]