---
title: "MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation"
created: 2024-05-23
source: https://arxiv.org/abs/2506.01897
tags: [MLorc, LLM, Parameter-Efficient Fine-Tuning, Memory-Optimization, Machine-Learning]
category: machine-learning
author: wiki-pipeline
dc.title: "MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/mlorc-momentum-low-rank-compression-for-memory-efficient-large-language-model-ad.md
dc.language: en
dc.rights: CC-BY-4.0
---

# MLorc: Momentum Low-rank Compression

The rapid scaling of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) has made [[Full-Parameter Fine-Tuning]] increasingly difficult due to the massive memory requirements for storing gradients and optimizer states. To address this bottleneck, the research paper "MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation" introduces a novel training paradigm known as **MLorc**.

## Technical Approach

The fundamental principle behind MLorc is the **compression and reconstruction of the momentum** of matrix parameters during the training process. By targeting the momentum buffers rather than the weight matrices or gradients alone, MLorc significantly reduces memory consumption without the structural rigidities found in older methods.

MLorc distinguishes itself from existing [[loft-parameter-efficient-fine-tuning-for-long-tailed-semi-supervised-learning-in|Parameter-Efficient Fine-Tuning]] (PEFT) techniques in two