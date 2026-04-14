---
title: DP-OPD: Differentially Private On-Policy Distillation for Language Models
created: 2024-05-23
source: https://arxiv.org/abs/2604.04461
tags: [differential privacy, machine learning, large language models, knowledge distillation]
category: ai
author: wiki-pipeline
dc.title: "DP-OPD: Differentially Private On-Policy Distillation for Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/dp-opd-differentially-private-on-policy-distillation-for-language-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DP-OPD: Differentially Private On-Policy Distillation for Language Models

**DP-OPD** (Differentially Private On-Policy Distillation) is a novel framework designed to address the fundamental tension between maintaining formal [[adaptive-differential-privacy-for-federated-medical-image-segmentation-across-di|Differential Privacy]] guarantees and preserving the utility of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) during the process of [[enec-a-lossless-ai-model-compression-method-enabling-fast-inference-on-ascend-np|Model Compression]].

## Background and Problem Statement

As LLMs are increasingly fine-tuned on proprietary and sensitive datasets, ensuring privacy is critical. The standard approach, [[DP-SGD]] (Differentially Private Stochastic Gradient Descent), provides robust record-level protection. However, in the context of [[Autoregressive generation]], the noise introduced by DP-SGD often leads to significant utility degradation. This is particularly problematic due to "exposure bias," where optimization noise compounds over long sequence rollouts.

Historically, researchers used two main approaches to private distillation:
1. **Dual DP-Training**: Applying DP-SGD to both the teacher and student models, which is computationally expensive and further degrades utility.
2. **Synthesis-based Distillation**: Using a DP-trained teacher to generate synthetic text, which requires a complex, multi-stage offline pipeline.

## The DP-OPD Approach

DP-OP1 introduces a synthesis-free framework that streamlines the distillation process into a single training loop. The core innovation lies in its **on-policy** nature: instead of relying on external synthetic datasets, the framework applies [[adaptive-differential-privacy-for-federated-medical-image-segmentation-across-di|Differential Privacy]] solely to the student model while utilizing a frozen teacher model to provide dense, token-level targets.

In DP-OPD, the student model generates its own trajectories (on-policy). The frozen teacher then provides feedback on these student-generated tokens through a process of [[Private Generalized Knowledge Distillation]]. This prevents the need for expensive teacher training or offline data generation.

## Results and Impact

Experimental evaluations demonstrate that DP-OPD significantly outperforms existing methods under strict privacy budgets (e.g., $\varepsilon=2.0$). Specifically, it shows marked improvements in **perplexity** compared to both DP fine-tuning and off-policy DP distillation.

Key performance benchmarks include:
* **Yelp dataset**: Perplexity improved from 44.15 to 41.68.
* **BigPatent dataset**: Perplexity improved from 32.43 to 30.63.

By collapsing private compression into a single DP student-training loop, DP-OPD offers a highly efficient and scalable solution for deploying private, high-performance language models in sensitive domains.