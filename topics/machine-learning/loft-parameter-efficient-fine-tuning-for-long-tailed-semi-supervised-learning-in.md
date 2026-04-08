---
title: LoFT: Parameter-Efficient Fine-Tuning for Long-tailed Semi-Supervised Learning in Open-World Scenarios
created: 2024-05-22
source: https://arxiv.org/abs/2509.09926
tags: [AI, Machine Learning, Semi-Supervised Learning, Foundation Models, Open-World Learning]
category: machine-learning
---

# LoFT: Parameter-Efficient Fine-Tuning for Long-tailed Semi-Supervised Learning

**LoFT** (Long-tailed semi-supervised learning via parameter-efficient Fine-Tuning) is a specialized framework designed to address the critical challenges of [[Long-tailed semi-supervised learning (LTSSL)]]. LTSSL presents a dual difficulty: the severe scarcity of samples in "tail" classes and the presence of noise within [[Pseudo-labels]] generated during the learning process.

### The Problem with Training from Scratch
Most traditional LTSSL methodologies focus on training models from scratch. The authors argue that this approach is fundamentally flawed for long-tailed distributions, as it frequently leads to high [[Overfitting]] rates, excessive model overconfidence, and the propagation of low-quality, inaccurate pseudo-labels.

### The LoFT Approach
LoFT proposes a paradigm shift by moving away from scratch-based training toward the fine-tuning of [[Foundation Models]]. This transition is supported by two primary theoretical pillars:

1.  **Complexity Reduction**: The researchers theoretically demonstrate that employing a foundation model significantly reduces [[Hypothesis Complexity]]. This reduction tightens the [[Generalization Bound]] and effectively minimizes the [[Balanced Posterior Error (BPE)]].
2.  **Geometric Robustness**: The framework leverages the intrinsic "feature compactness" of foundation models. This compactness serves to compress the acceptance region for outliers, providing a geometric guarantee that increases the model's robustness against noisy data.

By utilizing [[Parameter-Efficient Fine-Tuning]] (PEFT), LoFT maintains the high-quality feature representations of the base model while adapting to the specific long-tailed distribution of the target task.

### Expansion to Open-World Scenarios
To address real-world complexities, the paper introduces **LoFT-OW** (LoFT under Open-World scenarios). In practical applications, unlabeled datasets often contain [[Out-of-Distribution (OOD)]] samples—data that does not belong to any of the predefined classes. LoFT-OW is specifically engineered to improve discriminative ability in these [[Open-World Scenarios]], preventing unknown classes from corrupting the learned representations of the known classes.

Experimental evaluations across various benchmarks indicate that LoFT and LoFT-OW achieve superior performance compared to existing state-of-the-art methods in [[Deep Learning]].