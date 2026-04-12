---
title: Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning
created: 2025-05-22
source: https://arxiv.org/abs/2602.01528
tags: [AI, Machine Learning, Reinforcement Learning, LLM, Bias Mitigation]
category: ai, machine-learning
---

# Making Bias Non-Predictive: Training Robust LLM Reasoning via Reinforcement Learning

As [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) become increasingly integrated into automated reasoning and evaluation workflows, their susceptibility to cognitive biases presents a significant risk. This paper identifies a critical flaw: LLMs often alter their reasoning processes when presented with "spurious prompt-level cues," such as consensus claims (the bandwagon effect) or appeals to authority.

## The Limitation of Current Mitigations
Existing approaches to mitigate these biases, including [[supervised-fine-tuning|Supervised Fine-Tuning]] (SFT) and advanced prompting techniques, have proven insufficient. The authors argue that these methods only modify the "surface behavior" of the model. They fail to address the underlying optimization objective, which continues to make following biased cues a statistically "attractive" path for the model during training.

## Epistemic Independence Training (EIT)
To address this, the researchers propose a new [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] framework called [[epistemic-independence-training|Epistemic Independence Training]] (EIT). The fundamental principle of EIT is to ensure that bias cues become "non-predictive" of the reward. 

The framework utilizes two core components:
1. **Balanced Conflict Strategy**: During training, bias signals are intentionally presented in a way that they are equally likely to support both correct and incorrect answers.
2. **Reward Design**: The reward function is engineered to specifically penalize the model for following bias-driven cues while ensuring it does not lose the ability to follow truthful information.

## Experimental Results and Generalization
The study demonstrates the efficacy of EIT across various model scales and families, including [[qwen3|Qwen3]] and [[llama-32|Llama-3.2]]. Key findings include:
* **Transferable Robustness**: Models trained specifically on [[bandwagon-bias|Bandwagon Bias]] demonstrated an unexpected ability to resist unseen bias types, such as [[authority-bias|Authority Bias]] and [[distraction-bias|Distraction Bias]]. This suggests EIT fosters a general "epistemic independence" rather than simple heuristic learning.
* **Benchmark Performance**: EIT showed superior performance on reasoning benchmarks such as [[medqa|MedQA]] and [[hellaswag|HellaSwag]].
* **Superiority over Distribution Shift Methods**: EIT outperformed established [[learning-stable-predictors-from-weak-supervision-under-distribution-shift|Distribution Shift]] mitigation techniques, including [[groupdro|GroupDRO]] and [[invariant-risk-minimization|Invariant Risk Minimization]] (IRM), notably without requiring explicit environmental labels.

This research marks a significant step toward developing more reliable and trustworthy [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] systems capable of objective reasoning.