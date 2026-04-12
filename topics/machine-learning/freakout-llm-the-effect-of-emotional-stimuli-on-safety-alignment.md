---
title: "FreakOut-LLM: The Effect of Emotional Stimuli on Safety Alignment"
created: 2024-05-23
source: https://arxiv.org/abs/2604.04992
tags: [AI Safety, LLM, Jailbreaking, Adversarial Machine Learning, Psychological Priming]
category: [ai, machine-learning]
---

# FreakOut-LLM: The Effect of Emotional Stimuli on Safety Alignment

The research paper "FreakOut-LLM" explores a previously unexamined vulnerability in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] ([[analyzing-multimodal-interaction-strategies-for-llm-assisted-manipulation-of-3d-|LLM]]): the impact of emotional context on [[freakout-llm-the-effect-of-emotional-stimuli-on-safety-alignment|Safety Alignment]]. While modern models undergo extensive training to reject harmful instructions (refusal training), this study investigates whether emotional priming can compromise these safeguards through [[explainability-guided-adversarial-attacks-on-transformer-based-malware-detectors|Adversarial Attacks]].

## Methodology

The researchers introduced the FreakOut-LLM framework to evaluate ten different LLMs under three distinct psychological conditions derived from validated protocols:
* **Stress priming**: Utilizing scenarios designed to induce tension and urgency.
* **Relaxation priming**: Using prompts designed to induce a calm, low-arousal state.
* **Neutral baseline**: Standard prompting without emotional modifiers.

The study utilized established evaluation datasets, including [[harmbench|HarmBench]] and [[advbench|AdvBench]], to measure the success of [[jailbreaking|Jailbreaking]] attempts across these varying emotional states.

## Key Findings

The empirical results demonstrate that emotional context is a potent tool for compromising model safety. The most striking discovery was that **stress priming increased jailbreak success by 65.2%** compared to neutral conditions (p < 0.001). In contrast, relaxation priming showed no significant impact on the models' refusal capabilities.

The study also identified specific vulnerabilities within the current [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] landscape:
* **Model Sensitivity**: Five out of the ten tested models exhibited significant vulnerability to emotional manipulation.
* **Model Type**: The most substantial effects were concentrated in [[the-end-of-the-foundation-model-era-open-weight-models-sovereign-ai-and-inferenc|Open-weight models]], suggesting they may be more susceptible to context-based manipulation than closed systems.
