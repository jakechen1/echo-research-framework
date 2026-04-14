---
title: "UniCreative: Unifying Long-form Logic and Short-form Sparkle via Reference-Free Reinforcement Learning"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.05517"
tags: [ai, machine-learning, reinforcement-learning, nlp, technology]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "UniCreative: Unifying Long-form Logic and Short-form Sparkle via Reference-Free Reinforcement Learning"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/unicreative-unifying-long-form-logic-and-short-form-sparkle-via-reference-free-r.md
dc.language: en
dc.rights: CC-BY-4.0
---

# UniCreative: Unifying Long-form Logic and Short-form Sparkle via Reference-Free Reinforcement Learning

The field of [[Natural Language Generation]] faces a persistent fundamental challenge: reconciling the need for global coherence in long-form narratives with the desire for local, spontaneous expression in short-form text. While long-context generation requires explicit macroscopic planning to maintain narrative flow, short-form creativity often thrives on constraint-free, spontaneous expression.

## The UniCreative Framework

To address this tension, researchers have proposed **UniCreative**, a unified, reference-free [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] framework. Transitioning away from traditional alignment paradigms that rely on expensive [[Supervised Fine-Tuning]] (SFT) and static reward signals, UniCreative bypasses the need for high-quality supervised datasets and ground-truth references.

The framework introduces two primary architectural innovations:

*   **AC-GenRM (Adaptive Constraint-aware Reward Model):** This model dynamically synthesizes query-specific criteria to provide fine-grained preference judgments. It adapts its evaluative focus based on whether a prompt demands structural rigor or creative fluidity.
*   **ACPO (Adaptive Constraint Policy