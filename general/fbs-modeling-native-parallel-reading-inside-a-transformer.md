---
title: "FBS: Modeling Native Parallel Reading inside a Transformer"
created: 2024-05-22
source: https://arxiv.org/abs/2601.21708
tags: [Transformer, Efficient Inference, Neural Architecture, Cognitive Modeling]
category: [ai, machine-learning, neuroscience, technology]
author: wiki-pipeline
dc.title: "FBS: Modeling Native Parallel Reading inside a Transformer"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/fbs-modeling-native-parallel-reading-inside-a-transformer.md
dc.language: en
dc.rights: CC-BY-4.0
---

# FBS: Modeling Native Parallel Reading inside a Transformer

The **Fovea-Block-Skip Transformer (FBS)** is a novel neural architecture designed to transcend the limitations of standard [[Autoregressive Inference]] in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). While traditional Transformers rely on a strictly token-by-token processing pipeline, FBS introduces mechanisms that mimic human-like reading behaviors, such as [[Skimming]] and structure-aware [[web-retrieval-aware-chunking-w-rac-for-efficient-and-cost-effective-retrieval-au|Chunking]].

## The Problem: Computational Bottlenecks in Autoregression
Current LLM inference is heavily dominated by sequential processing, which misses fundamental human-reading ingredients: content-adaptive foresight, chunk-structure-aware compute allocation, and the ability to perform training-test consistency for previewing text. Because existing acceleration methods largely focus on patching the existing pipeline rather than redesigning the core logic, they struggle to balance high-quality output with computational efficiency.

## The FBS Architecture
The FBS framework injects a causal, trainable loop into the standard [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] architecture through three complementary modules that draw inspiration from [[Cognitive Science]]:

1.  **Parafovea-Attention Window (PAW):** Mimicking the peripheral vision used in human reading, this module provides the model with "content-adaptive foresight," allowing it to look ahead within a controlled window.
2.  **Chunk-Head (CH):** This module enables the model to allocate compute based on the structural importance of text segments, allowing for more intelligent processing of grouped information.
3.  **Skip-Gate (SG):** This component facilitates the "skimming" process by allowing the model to bypass less critical tokens, optimizing throughput without sacrificing essential context.

## Results and Implications
Experimental evaluations across diverse benchmarks demonstrate that FBS improves the **quality-efficiency trade-off** significantly. Importantly, these architectural advancements are achieved without increasing the total number of parameters. By integrating principles from [[Neuroscience]] into [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]], FBS represents a step toward more efficient, biologically-inspired [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] that can process information with the fluidity of a human reader.