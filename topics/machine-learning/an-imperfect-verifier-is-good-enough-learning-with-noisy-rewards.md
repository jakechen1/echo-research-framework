---
title: An Imperfect Verifier is Good Enough: Learning with Noisy Rewards
created: 2024-05-23
source: https://arxiv.org/abs/2604.07666
tags: [Reinforcement Learning, LLM, RLVR, Robustness, Machine Learning]
category: ai, machine-learning
---

# An Imperfect Verifier is Good Enough: Learning with Noisy Rewards

## Overview
This research paper examines the stability of [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] with [[verifiable-rewards|Verifiable Rewards]] (RLVR), a prominent methodology used during the post-training phase of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). The study addresses a critical uncertainty in [[a-mathematical-theory-of-evolution-for-self-designing-ais|AI]] development: how much error can a reward-giving "verifier" possess before it breaks the learning process?

## The Problem of Verifier Noise
In modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] workflows, verifiers are used to provide feedback on tasks such as code generation and scientific reasoning. While some verifiers are deterministic (e.g., compilers), there is an increasing reliance on [[model-based-judges|Model-based Judges]] to evaluate complex, non-binary outputs. These judges are rarely error-free. The researchers investigated whether this inherent noise—either through inaccurate deterministic checks or probabilistic model errors—acts as a fundamental barrier to effective [[rl-training|RL training]].

## Methodology and Scope
The researchers conducted extensive experiments by intentionally introducing noise into the reward signals. The scope of the study was broad, encompassing:
* **Domains:** Code generation and scientific reasoning.
* **Model Architectures:** Testing across multiple families, including [[llama-31|Llama 3.1]], [[qwen|Qwen]], and [[glm|GLM]].
* **Scalability:** Evaluating model sizes ranging from 4B to 9B parameters.

The study compared "clean" baselines against various levels of injected noise, simulating both controlled and model-driven inaccuracies.

## Key Findings
The research yields highly optimistic results for practitioners of [[mitigating-distribution-sharpening-in-math-rlvr-via-distribution-aligned-hint-sy|RLVR]]:
* **High Tolerance for Noise:** The training process remains remarkably robust. Even with noise rates as high as 15%, the peak validation accuracy dropped by no more than 2 percentage points compared to the clean baseline.
* **Universal Robustness:** These results were consistent across different model families and sizes, suggesting that the phenomenon is not an artifact of a specific architecture.
* **Strategic Recommendation:** The authors suggest that developers should prioritize **high precision** over absolute accuracy. In the context of automated evaluation, ensuring that a "correct" signal is truly correct is more vital than ensuring every single signal is perfectly vetted.

## Conclusion
The study concludes that imperfect verification is not a fundamental obstacle to scaling [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] for LLMs