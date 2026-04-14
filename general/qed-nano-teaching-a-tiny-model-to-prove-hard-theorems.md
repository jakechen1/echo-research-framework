---
title: QED-Nano: Teaching a Tiny Model to Prove Hard Theorems
created: 2024-05-22
source: https://arxiv.org/abs/2604.04898
tags: [LLM, Mathematical Reasoning, Reinforcement Learning, Open Science]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "QED-Nano: Teaching a Tiny Model to Prove Hard Theorems"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/qed-nano-teaching-a-tiny-model-to-prove-hard-theorems.md
dc.language: en
dc.rights: CC-BY-4.0
---

# QED-Nano: Teaching a Tiny Model to Prove Hard Theorems

The **QED-Nano** project introduces a highly efficient 4-billion parameter model specifically engineered for performing advanced [[do-mllms-really-understand-space-a-mathematical-reasoning-evaluation|Mathematical Reasoning]] at the level of the International Mathematical Olympiad (IMO). While large-scale proprietary [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models have recently demonstrated "gold-level" capabilities in mathematics, their immense computational requirements and opaque training methodologies limit reproducibility and study within the [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] community.

### Training Methodology

The developers of QED-Nano implemented a specialized three-stage training pipeline designed to maximize the reasoning potential of a small-scale architecture:

1.  **Supervised Fine-Tuning (SFT):** The model was first trained to adopt high-quality proof-writing styles by distilling knowledge from the larger [[DeepSeek-Math-V2]] model.
2.  **Reinforcement Learning (RL) with Rubric Rewards:** This stage utilized reward functions based on specific mathematical rubrics to refine accuracy and logical consistency through [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]].
3.  **Reasoning Cache Expansion:** The final stage introduced an iterative "summarize-and-refine" cycle. This process allows the model to decompose complex, multi-step proofs into manageable segments, significantly enhancing performance during [[epistemic-blinding-an-inference-time-protocol-for-auditing-prior-contamination-i|Inference]].

### Performance and Impact

QED-Nano demonstrates remarkable efficiency, outperforming much larger open-source models such as [[Nomos-1]] and [[GPT-OSS-120B]]. Most notably, it approaches the mathematical proof-generation capabilities of leading proprietary systems like [[Gemini 3 Pro]], but at a significantly reduced computational and [[Inference Cost]].

### Open Research Contributions

To foster advancements in [[Open Science]] and mathematical [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Network]] research, the developers have released the complete QED-Nano pipeline. This includes:

*   **Models:** QED-Nano and QED-Nano-SFT.
*   **Datasets:** The FineProofs-SFT and FineProofs-RL datasets.
*   **Codebase:** Comprehensive training and evaluation frameworks for evaluating mathematical logic in small-scale models.