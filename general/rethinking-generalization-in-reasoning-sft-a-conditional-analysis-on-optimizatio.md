---
title: Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability
created: 2024-05-22
source: https://arxiv.org/abs/2604.06628
tags: [LLM, Supervised Fine-Tuning, Chain-of-Thought, Generalization, Machine Learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/rethinking-generalization-in-reasoning-sft-a-conditional-analysis-on-optimizatio.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Rethinking Generalization in Reasoning SFT

The paper *"Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability"* challenges the prevailing paradigm in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) post-training. Historically, a common narrative has suggested that [[Supervised Fine-Tuning]] (SFT) is primarily a mechanism for memorization, whereas [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) is the necessary driver for true [[a-canonical-generalization-of-obdd|Generalization]]. This research re-evaluates this distinction through the lens of reasoning SFT using long [[tool-mcot-tool-augmented-multimodal-chain-of-thought-for-content-safety-moderati|Chain-of-Thought]] (CoT) supervision.

## Key Findings

### The "Dip-and-Recovery" Pattern
The authors identify that failures in cross-domain generalization are often artifacts of under-optimization rather than inherent limitations of SFT. They observe a "dip-and-recovery" pattern, where cross-domain performance initially degrades during the early stages of training before eventually recovering and improving. This implies that evaluating models using short training checkpoints can lead to significant underestimations of a model's generative potential.

### Impact of Data and Model Capability
The study highlights that generalization is conditional upon two main pillars:

*   **Data Quality and Structure:** The use of verified, long-CoT traces provides consistent gains across different domains. Conversely, low-quality or poorly structured solutions negatively impact the model's ability to generalize.
*   **Base Model Capacity:** There is a clear divide in how models process SFT data based on their strength. Stronger models are capable of internalizing transferable procedural patterns—such as [[backtracking]]—even when trained on simple, "toy" arithmetic tasks. In contrast, weaker models tend to exhibit "surface verbosity," where they mimic the length and style of the training data without capturing the underlying logic.

### The Cost of Reasoning
Crucially, the research notes an asymmetric trade-off: while SFT can enhance complex reasoning capabilities, it may simultaneously lead to a degradation in [[iatrobench-pre-registered-evidence-of-iatrogenic-harm-from-ai-safety-measures|AI Safety]] and alignment. This shifts the research focus from whether SFT can generalize to understanding the specific conditions and costs associated with such a transition.

## Related Topics
* [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]]
* [[Transformer Architectures]]
* [[Artificial Intelligence Safety]]
*