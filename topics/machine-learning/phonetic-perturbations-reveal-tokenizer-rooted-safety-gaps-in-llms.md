---
title: Phonetic Perturbations Reveal Tokenizer-Rooted Safety Gaps in LLMs
created: 2024-05-23
source: https://arxiv.org/abs/2505.14226
tags: [AI Safety, Tokenization, Adversarial Attacks, Red-Teaming]
category: ai, machine-learning, technology
---

# Phonetic Perturbations Reveal Tokenizer-Rooted Safety Gaps in LLMs

The research paper "Phonetic Perturbations Reveal Tokenizer-Rooted Safety Gaps in LLMs" identifies a significant vulnerability in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) regarding their safety-alignment mechanisms. While modern models are rigorously trained to avoid generating harmful content, they remain susceptible to phonetic perturbations—non-canonical text variations (such as "textese") that alter the spelling of a word while preserving its spoken phonetic structure.

## The CMP-RT Framework

To diagnose this vulnerability, the researchers introduced **CMP-RT** (code-mixed phonetic perturbations for red-teaming). This novel diagnostic probe allows researchers to test how much a model's safety filters can be bypassed by changing how a word looks without changing how it sounds.

## The Role of Tokenization

The study's core finding is that the root cause of this vulnerability lies within the [[the-geometric-alignment-tax-tokenization-vs.-continuous-geometry-in-scientific-f|Tokenization]] process. The mechanistic analysis reveals that when a safety-critical token is phonetically perturbed, the tokenizer fragments the original token into several benign-looking sub-words. 

Although the model's internal layers still recognize the semantic intent of the prompt—maintaining high interpretability—the "attribution scores" (the weights assigned to the importance of specific tokens) for the safety-critical components are suppressed. Because the safety mechanisms are looking for specific, high-risk token patterns, the fragmentation into harmless sub-words causes the [[freakout-llm-the-effect-of-emotional-stimuli-on-safety-alignment|Safety Alignment]] to fail.

## Experimental Findings and Implications

The research demonstrates several critical points regarding the robustness of current [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] architectures:

* **Persistence:** The vulnerability is observed in state-of-the-art models, including [[gemini-3-pro|Gemini-3-Pro]].
* **Scalability:** The vulnerability is not easily patched and can actually be scaled through [[supervised-fine-tuning|Supervised Fine-Tuning]] (SFT).
* **Structural Gap:** Layer-wise probing shows that representations of canonical and perturbed inputs align only up to a critical layer depth. By enforcing output equivalence, researchers can recover the lost representations, providing causal evidence of a structural gap between the [[adaptive-input-training-for-many-to-one-pre-training-on-time-series-classificati|Pre-training]] and [[rlaif-spa-structured-ai-feedback-for-semantic-prosodic-alignment-in-speech-synth|Alignment]] phases.

The paper concludes that [[the-geometric-alignment-tax-tokenization-vs.-continuous-geometry-in-scientific-f|Tokenization]] represents a critical, under-examined surface for [[explainability-guided-adversarial-attacks-on-transformer-based-malware-detectors|Adversarial Attacks]] and must be addressed in future safety pipelines.