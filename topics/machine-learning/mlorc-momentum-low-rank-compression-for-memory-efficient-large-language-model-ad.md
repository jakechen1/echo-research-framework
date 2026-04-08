---
title: "MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation"
created: 2024-05-23
source: https://arxiv.org/abs/2506.01897
tags: [MLorc, LLM, Parameter-Efficient Fine-Tuning, Memory-Optimization, Machine-Learning]
category: machine-learning
---

# MLorc: Momentum Low-rank Compression

The rapid scaling of [[Large Language Models]] (LLMs) has made [[Full-Parameter Fine-Tuning]] increasingly difficult due to the massive memory requirements for storing gradients and optimizer states. To address this bottleneck, the research paper "MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation" introduces a novel training paradigm known as **MLorc**.

## Technical Approach

The fundamental principle behind MLorc is the **compression and reconstruction of the momentum** of matrix parameters during the training process. By targeting the momentum buffers rather than the weight matrices or gradients alone, MLorc significantly reduces memory consumption without the structural rigidities found in older methods.

MLorc distinguishes itself from existing [[Parameter-Efficient Fine-Tuning]] (PEFT) techniques in two