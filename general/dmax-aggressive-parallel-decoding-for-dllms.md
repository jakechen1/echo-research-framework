---
title: DMax: Aggressive Parallel Decoding for dLLMs
created: 2024-05-22
source: https://arxiv.org/abs/2604.08302
tags: [diffusion-models, parallel-decoding, LLMs, efficiency]
category: ai
author: wiki-pipeline
dc.title: "DMax: Aggressive Parallel Decoding for dLLMs"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/dmax-aggressive-parallel-decoding-for-dllms.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DMax: Aggressive Parallel Decoding for dLLMs

DMax represents a significant advancement in the efficiency of [[$s^3$-stratified-scaling-search-for-test-time-in-diffusion-language-models|Diffusion Language Models]] (dLLMs). While traditional masked dLLMs often struggle with [[Error Accumulation]] during the decoding process, DMax introduces a new paradigm that enables highly aggressive [[dmax-aggressive-parallel-decoding-for-dllms|Parallel Decoding]] without sacrificing the quality of the generated text.

## Core Innovations

The fundamental shift in DMax is the movement away from the conventional binary mask-to-token transition. Instead, DMax reformulates the decoding process as a continuous, progressive [[Self-Refinement]] task, transitioning from mask embeddings to token embeddings.

### On-Policy Uniform Training
A key component of this architecture is [[On-Policy Uniform Training]]. This novel strategy provides a unified training framework for both masked and uniform dLLMs. By training the model to handle both masked inputs and its own potentially erroneous predictions, the system becomes significantly more robust. This allows the model to "self-correct" during the diffusion process, recovering clean tokens from corrupted intermediate states.

### Soft Parallel Decoding
DMax further optimizes performance through [[Soft Parallel Decoding]]. Within this framework, each intermediate decoding state is treated as an interpolation within the [[geometric-organization-of-cognitive-states-in-transformer-embedding-spaces|Embedding Space]] between the predicted token embedding and the mask embedding. This iterative approach allows for smoother transitions and more precise refinement of the sequences being generated.

## Performance and Benchmarks

Experimental results demonstrate that DMax significantly improves the Tokens Per Frame (TPF) metric—a measure of decoding speed—while maintaining high accuracy. When compared to the [[LLaDA-2.0-mini]] baseline, the improvements are notable:

* **GSM8K Benchmark:** TPF increased from 2.04 to 5.47.
* **MBPP Benchmark:** TPF increased from 2.71 to 5.86.

In terms of raw throughput, DMax achieves an average of 1,338 Tokens Per Second (TPS) on two [[NVIDIA H200 GPUs]] at a batch size of 1. This makes DMax a highly scalable solution for high-speed [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] inference tasks requiring complex reasoning and coding capabilities.