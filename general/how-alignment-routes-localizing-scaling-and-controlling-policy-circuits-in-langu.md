---
title: How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.04385
tags: [ai, machine-learning, mechanistic-interpretability, alignment, language-models]
category: ai
author: wiki-pipeline
dc.title: "How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/how-alignment-routes-localizing-scaling-and-controlling-policy-circuits-in-langu.md
dc.language: en
dc.rights: CC-BY-4.0
---

# How Alignment Routes

The research paper **"How Alignment Routes: Localizing, Scaling, and Controlling Policy Circuits in Language Models"** identifies a recurring sparse routing mechanism within [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) that is responsible for enforcing [[rlaif-spa-structured-ai-feedback-for-semantic-prosodic-alignment-in-speech-synth|alignment]] and safety policies. The study moves beyond simple observation of refusal behaviors to map the specific "circuitry" used during [[ahcq-sam-toward-accurate-and-hardware-compatible-post-training-segment-anything-|post-training]].

## The Policy Circuit Mechanism

The researchers discovered a functional circuit composed of two primary components within the model's [[attention heads]]:

1.  **Gate Heads:** These act as the detection layer. They monitor incoming tokens for specific patterns associated with sensitive or restricted content (such as political censorship or safety violations).
2.  **Amplifier Heads:** Once the gate heads detect a match, they trigger these downstream heads, which amplify the neural signal to drive the model toward a "refusal" response.

This mechanism was validated across nine different models from six major AI laboratories, demonstrating that this routing architecture is a consistent feature of modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] alignment techniques.

## Scaling and Control

The paper provides significant evidence regarding the scalability of these circuits. By testing same-generation scaling pairs, the authors showed that the routing mechanism distributes more broadly as models grow in size, yet the core functionality remains detectable. 

Furthermore, the study demonstrates that the policy strength is not binary. By continuously modulating the signal from the detection layer, researchers could steer the model through a spectrum of behaviors: from **hard refusal** to **steering** and, ultimately, to **factual compliance**.

## Intent Recognition vs. Policy Routing

A critical discovery is the structural decoupling between **intent recognition** and **policy routing**. Using [[cipher encoding]] (input transformations that obscure text), the researchers found that while the model's deeper layers still represented the harmful underlying content, the gate heads failed to trigger. 

This suggests a fundamental asymmetry in [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|neural networks]]: 
*   **Pre-training** builds robust, broad semantic understanding.
*   **Post-training/Alignment** creates a narrower, more brittle layer of policy binding that can be bypassed by certain input transformations, even when the model "understands" the prompt.