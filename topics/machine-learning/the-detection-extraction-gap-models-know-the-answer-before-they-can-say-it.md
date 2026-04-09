---
title: "The Detection--Extraction Gap: Models Know the Answer Before They Can Say It"
created: 2024-05-23
source: https://arxiv.org/abs/2604.06613
tags: [[Large Language Models]], [[Chain-of-Thought]], [[Inference Optimization]], [[Machine Learning]]
category: ai, machine-learning
---

# The Detection--Extraction Gap

The **Detection--Extraction Gap** is a structural phenomenon identified in modern [[Large Language Models]] (LLMs) where the model's internal state and partial output sequences contain the correct answer long before the model completes its generation process. Research demonstrates that in various model configurations and benchmarks, between **52% and 88% of [[Chain-of-Thought]] (CoT) tokens** are generated after the answer is already recoverable from an early prefix of the sequence.

## The Phenomenon

The gap is defined by a breakdown between two linguistic capabilities:

1.  **Detection:** The ability to retrieve the correct answer from a partial prefix or the model's internal state.
2.  **Extraction:** The ability of prompt-conditioned decoding to successfully output that answer.

The study finds that while the answer is often present in the early stages of a trace (sometimes at just 10% of the total length), the model's forced extraction process fails in approximately 42% of these recoverable cases. This suggests that the subsequent "post-commitment" generation can lead to **post-commitment overwriting**, where the model generates tokens that contradict or obscure the previously determined correct answer.

## Technical Analysis and Solution

The researchers formalize this discrepancy using a **total-variation bound** to measure the shift between "free" continuation distributions (unconstrained generation) and "forced" continuation distributions (generation guided by specific prompts).

To mitigate this inefficiency, the paper proposes **[[Black-box Adaptive Early Exit]] (BAEE)**. This method utilizes free continuations to perform both detection and extraction simultaneously. By exiting the generation process as soon as the answer is detectable, BAEE achieves significant performance improvements:

*   **Efficiency:** Reduces serial generation by **70–78%**.
*   **Accuracy:** Increases accuracy by **1–5 percentage points** across all tested models.
*   **Thinking-Mode Optimization:** Specifically prevents the accuracy degradation caused by overwriting in advanced reasoning models.

A cost-optimized version of BAEE can achieve a reduction in generation cost of up to 73% while maintaining a median of only 9 API calls.

## Related Topics
* [[Transformer Architectures]]
* [[Inference Latency]]
* [[Algorithmic Efficiency]]
* [[Generative AI]]