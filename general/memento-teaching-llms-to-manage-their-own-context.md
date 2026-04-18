---
title: "MEMENTO: Teaching LLMs to Manage Their $Own$ Context"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.09852"
tags: [llm, context-management, inference-optimization, deep-learning]
category: ai, machine-learning, technology
---

# MEMENTO: Teaching LLMs to Manage Their Own Context

**MEMENTO** is a novel framework designed to address the inefficiencies inherent in the long-form, unstructured reasoning processes of [[Large Language Models]] (LLMs). In traditional reasoning models, the lack of a mechanism to compress or organize intermediate computational states leads to ever-expanding context windows, increasing [[KV cache]] demands and computational overhead.

## Overview

The MEMENTO method introduces a structural paradigm shift by teaching models to segment their reasoning into discrete "blocks." Instead of processing a continuous, uncompressed stream of tokens, the model compresses each reasoning block into a **memento**—a dense, high-level state summary. The model then continues its reasoning by attending primarily to these mementos, effectively bypassing the need to process the full, raw history of the conversation.

## Implementation and Training

To train these models, the researchers introduced **OpenMementos**, a public dataset consisting of 228,000 reasoning traces. These traces, derived from [[OpenThoughts-v3]], were specifically segmented and annotated with intermediate summaries to facilitate [[Supervised Fine-Tuning]] (SFT). 

The efficacy of this two-stage SFT recipe has been demonstrated across several prominent model families, including [[Qwen3]], [[Phi-4]], and [[Olmo 3]], across scales ranging from 8B to 32B parameters.

## Key Results

The implementation of MEMENTO provides significant advantages in both efficiency and throughput:

*   **Memory Reduction:** The method achieves approximately a $2.5\times$ reduction in peak [[KV cache]] usage.
*   **Inference Speed:** By extending the [[vLLM]] inference engine to support the MEMENTO method, the researchers achieved a $1.75\times$ improvement in throughput.
*   **Performance Stability:** Despite the aggressive compression, models maintain high accuracy levels on complex benchmarks involving [[mathematics]], [[science]], and [[coding]].

## The Dual Information Stream

A significant technical insight from the study is the identification of a "dual information stream." The researchers discovered that information from each reasoning block is carried both by the explicit text of the memento and by the underlying [[KV states]], which retain implicit information from the original, uncompressed block. Experimental results showed that removing this latent KV-state channel led to a drastic 15-percentage-point drop in accuracy on the AIME24 benchmark, proving that textual summaries alone are insufficient for complex reasoning tasks.