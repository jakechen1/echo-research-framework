---
title: "Cactus: Accelerating Auto-Regressive Decoding with Constrained Acceptance Speculative Sampling"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.04987"
tags: [ai, machine-learning, inference, optimization]
---

# Cactus: Accelerating Auto-Regressive Decoding

**Cactus**, or Constrained Acceptance Speculative Sampling, is a novel technique in [[machine-learning]] designed to optimize the decoding efficiency of [[Large Language Models]] (LLMs). By refining the way tokens are accepted during the inference process, Cactus seeks to bridge the gap between high-speed throughput and high-quality text generation.

## The Problem with Traditional Speculative Sampling

In standard [[Speculative Sampling]] (SpS), a smaller, faster "draft model" predicts a sequence of upcoming tokens, which are then verified by a larger, more accurate "verifier LLM." For the process to remain mathematically valid, the draft model's distribution must strictly match that of the verifier. While this ensures that the output quality remains unchanged, it is often overly restrictive; slight deviations in the distribution, such as those used in [[top-k sampling]] or [[temperature]] adjustment, would typically not harm the model's utility.

Previous attempts to improve this, such as Typical Acceptance Sampling (TAS), used entropy-based heuristics to accept more tokens. However, these methods often lead to significant distortions in the verifier's distribution, which can result in "hallucinations" or a degradation of the logical coherence of the output.

## The Cactus Solution

The authors of the Cactus paper propose a new methodology by framing speculative sampling as a [[constrained optimization]] problem. Rather than allowing for uncontrolled drift or enforcing an impossible-to-maintain exact match, Cactus introduces a mechanism that allows for a **controlled divergence** from the verifier's distribution.

Key features of the Cactus approach include:
* **Controlled Divergence:** It allows the draft model more flexibility in token selection while maintaining a strict mathematical bound on how much the distribution can deviate from the verifier.
* **Increased Acceptance Rates:** By optimizing the acceptance threshold, Cactus increases the number of tokens accepted per step, thereby accelerating [[inference]].
* **Distribution Preservation:** It prevents the structural distribution distortions seen in previous heuristic-based methods, ensuring the verifier's critical information is preserved.

## Conclusion

Empirical evaluations across various benchmarks confirm that Cactus significantly improves decoding throughput without the quality loss associated with prior methods. This makes it a vital development for the deployment of large-scale [[Artificial Intelligence]] in resource-constrained environments.

**Category:** ai, machine-learning