---
title: Weakly Supervised Distillation of Hallucination Signals into Transformer Representations
created: 2024-05-24
source: https://arxiv.org/abs/2604.06277
tags: [hallucination, LLM, transformer, weak-supervision, probing, machine-learning]
category: ai, machine-learning
---

# Weakly Supervised Distillation of Hallucination Signals into Transformer Representations

The paper **"Weakly Supervised Distillation of Hallucination Signals into Transformer Representations"** addresses one of the most significant challenges in [[Artificial Intelligence]]: the detection of [[Hallucination]] in [[Large Language Models (LLMs)]]. 

### The Problem: External Verification Bottlenecks
Currently, detecting hallucinations during [[Inference]] typically requires external verification methods. These include using [[Retrieval-Augmented Generation (RAG)]], secondary "judge" models, or external gold-standard datasets. While effective, these methods introduce significant computational overhead and require access to external knowledge at the time of generation.

### Proposed Solution: Internalized Detection
The authors propose a method to shift the burden of detection from inference-time verification to training-time distillation. The core hypothesis is that the signals indicating a hallucination are already present within the model's internal [[Transformer]] representations (hidden states) and can be "unlocked" via training.

### Methodology: Weak Supervision Framework
To avoid the prohibitive cost of human annotation, the researchers implemented a [[Weak Supervision]] framework. This framework labels generated responses as "grounded" or "hallucinated" using three complementary automated signals:
1. **Substring matching** against a reference.
2. **Sentence embedding similarity** analysis.
3. An **LLM as a judge** verdict.

Using this approach, a dataset of 15,000 samples was constructed from [[SQuAD v2]], mapping the per-layer hidden states of [[LLaMA-2-7B]] to these automated hallucination labels.

### Probing Architectures and Results
The study trained five distinct probing classifiers, ranging from simple [[Machine Learning]] architectures to complex structures:
* **ProbeMLP (M0)**
* **LayerWiseMLP (M1)**
* **CrossLayerTransformer (M2)**
* **HierarchicalTransformer (M3)**
* **CrossLayerAttentionTransformerV2 (M4)**

The results confirmed that hallucination signals can be successfully distilled into the model's activations. The **M2** and **M3** architectures (Transformer-based probes) achieved the highest AUC and F1 scores. 

### Practical Implications
A key finding of the research is the efficiency of the approach. The additional [[Inference Latency]] introduced by these probes is negligible, ranging from only **0.15 to 6.66 ms**. This suggests that hallucination detection can be integrated into production-level [[Software Engineering]] workflows for LLMs without significantly impacting throughput.