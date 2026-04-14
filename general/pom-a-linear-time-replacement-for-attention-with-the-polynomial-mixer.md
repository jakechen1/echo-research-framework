---
title: "PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.06129"
tags: [machine-learning, transformers, polynomial-mixer, attention-mechanisms, computational-efficiency]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/pom-a-linear-time-replacement-for-attention-with-the-polynomial-mixer.md
dc.language: en
dc.rights: CC-BY-4.0
---

# PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer

The **Polynomial Mixer (PoM)** is a novel token mixing mechanism designed to serve as a highly efficient, drop-in replacement for the standard [[Self-Attention]] mechanism used in [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] architectures. Developed to address the inherent computational bottlenecks associated with quadratic complexity, PoM introduces a method that operates with **linear complexity**, making it particularly effective for processing extremely long sequences.

### Mechanism and Theory
The core innovation of PoM lies in its approach to token aggregation. Instead of the intensive pairwise comparisons characteristic of traditional attention, PoM utilizes a learned [[Polynomial Function]] to aggregate input tokens into a compact, global representation. Individual tokens then retrieve contextual information from this compressed state.

Crucially, the research proves that PoM satisfies the **contextual mapping property**. This theoretical foundation is vital because it ensures that models utilizing PoM retain the capability of being [[Universal Sequence-to-Sequence Approximators]], preserving the fundamental expressive power and mathematical utility of the original [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] models.

### Experimental Validation
The efficacy of PoM has been validated across five diverse computational domains, demonstrating its versatility:
* [[a-severity-based-curriculum-learning-strategy-for-arabic-medical-text-generation|Text Generation]]
* [[deco-frequency-decoupled-pixel-diffusion-for-end-to-end-image-generation|Image Generation]]
* [[Handwritten Text Recognition]]
* [[3D Modeling]]
* [[assessing-the-added-value-of-onboard-earth-observation-processing-with-the-iride|Earth Observation]]

In these benchmarks, PoM demonstrates performance parity with traditional [[Attention-Based Models]] while delivering significant reductions in computational overhead. This efficiency gain is most pronounced when handling long-range dependencies and high-resolution inputs, where the [[Quadratic Complexity]] of standard attention typically becomes a prohibitive barrier to scaling.

### Resources
* **Original Paper:** [arXiv:2604.06129](https://arxiv.org/abs/2604.06129)
* **Source Code:** [GitHub - davidpicard/pom](https://github.com/davidpicard/pom)