---
title: PolicyLong: Towards On-Policy Context Extension
created: 2024-05-22
source: https://arxiv.org/abs/2604.07809
tags: [ai, machine-learning, LLM, context-extension, data-synthesis]
category: ai, machine-learning
---

# PolicyLong: Towards On-Policy Context Extension

The fundamental challenge in extending the [[lsrm-high-fidelity-object-centric-reconstruction-via-scaled-context-windows|context window]] of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) lies in the scarcity of high-quality, long-range dependency datasets. While recent research has successfully employed information-theoretic verification—selecting contexts that specifically reduce a model's predictive entropy—these methodologies typically rely on a single-pass, offline construction process. This creates a significant "off-policy gap," where the static screening landscape used to create training data fails to align with the model's evolving capabilities, leading to distribution drift during training.

## The PolicyLong Paradigm

[[policylong-towards-on-policy-context-extension|PolicyLong]] proposes a transition from static data construction to a dynamic, **on-policy** paradigm. The core innovation is the implementation of an iterative data screening process. Unlike previous approaches, PolicyLong re-executes the entire pipeline—including entropy computation, retrieval, and verification—using the current version of the model being trained. 

This iterative loop ensures that the training distribution tracks the model's developing capabilities, effectively generating an emergent **self-curriculum**. A critical feature of this method is that both positive training examples and "hard negative" contexts are harvested from the model's current entropy landscape. This simultaneous exposure allows the model to learn to exploit meaningful dependencies while learning to resist misleading or noisy long-range patterns.

## Experimental Performance

The effectiveness of PolicyLong has been validated through rigorous testing on various long-context benchmarks. Using [[qwen25-3b|Qwen2.5-3B]] as a base, the method demonstrated consistent superiority over predecessor methods such as [[entropylong|EntropyLong]] and [[nextlong|NExtLong]]. 

Key findings include:
* **Benchmark Success**: Significant performance gains were observed on [[ruler|RULER]], [[helmet|HELMET]], and [[longbench-v2|LongBench-v2]].
* **Scaling Efficiency**: The performance advantage of PolicyLong becomes more pronounced as the context length increases. For instance, a gain of +2.54 was recorded at the 128K context length on the RULER benchmark.

These results confirm that moving toward on-policy data evolution is a vital step in the advancement of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] techniques for long-context processing.