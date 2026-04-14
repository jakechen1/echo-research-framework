---
title: Bit-by-Bit: Progressive QAT Strategy with Outlier Channel Splitting for Stable Low-Bit LLMs
created: 2024-05-22
source: https://arxiv.org/abs/2604.07888
tags: [ai, machine-learning, quantization, llm, optimization]
category: machine-learning
author: wiki-pipeline
dc.title: "Bit-by-Bit: Progressive QAT Strategy with Outlier Channel Splitting for Stable Low-Bit LLMs"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/bit-by-bit-progressive-qat-strategy-with-outlier-channel-splitting-for-stable-lo.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Bit-by-Bit: Progressive QAT Strategy with Outlier Channel Splitting for Stable Low-Bit LLMs

The paper **Bit-by-Bit** introduces a novel framework for [[Quantization-Aware Training]] (QAT) designed to solve the fundamental stability and convergence issues associated with training [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) at ultra-low precision. Traditional low-bit quantization often suffers from significant error accumulation and high training costs, largely driven by quantization noise originating from heavy-tailed outlier channels in the model layers.

## Core Methodology

The Bit-by-Bit framework utilizes a three-pronged strategy to mitigate these challenges:

1. **Block-wise Progressive Training**: Rather than attempting to train at ultra-low precision immediately, the framework reduces precision stage-by-stage. This gradual reduction ensures a stable initialization process, preventing the divergence common in direct low-bit optimization.
2. **Nested Quantization Grids**: The authors implement a nested structure of integer quantization grids. This enables a "train once, deploy any precision" paradigm, allowing a single trained model to support multiple bit-widths without the need for additional retraining cycles.
3. **