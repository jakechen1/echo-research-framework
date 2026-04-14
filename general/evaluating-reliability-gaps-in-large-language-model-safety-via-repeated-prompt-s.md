---
title: Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling
created: 2024-05-22
source: https://arxiv.org/abs/2604.09606
tags: [LLM, Safety, Reliability, APST, Benchmarking, Machine Learning]
category: ai
dc.title: "Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/evaluating-reliability-gaps-in-large-language-model-safety-via-repeated-prompt-s.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling

## Overview
Traditional evaluation frameworks for [[Large Language Models]] (LLMs), such as [[HELM]] and [[AIR-BENCH]], primarily focus on breadth-oriented assessment. These benchmarks measure a model's ability to generalize across a wide variety of diverse tasks but often overlook the specific operational risks encountered during continuous, real-world deployment. 

The research paper "Evaluating Reliability Gaps in Large Language Model Safety via Repeated Prompt Sampling" argues that the true risk in high-stakes environments stems from "depth-oriented" failures—stochastic errors that emerge from repeated generations of the same prompt rather than from a lack of task variety.

## Accelerated Prompt Stress Testing (APST)
To identify these latent vulnerabilities, the authors introduce **Accelerated Prompt Stress Testing (APST)**. This framework is inspired by highly accelerated stress testing methodologies found in [[Reliability Engineering]]. Instead of treating safety failures as isolated, one-off events, APST treats them as statistical outcomes of repeated inference.

The APST framework probes LLM behavior by repeatedly sampling identical prompts under controlled operational conditions, including:
*   **Temperature Variation:** Testing how increased stochasticity affects the likelihood of unsafe outputs.
*   **Prompt Perturbation:** Analyzing how slight modifications to input affect consistency.
*   **Statistical Modeling:** Using [[Bernoulli]] and [[Binomial]] distributions to estimate the probability of per-inference failures, such as [[Hallucinations]], refusal inconsistencies, and unsafe completions.

## Key Findings
Applying APST to multiple instruction-tuned LLMs revealed a significant "reliability gap." The researchers found that while various models may exhibit similar performance during conventional evaluations (where sample sizes are very low, $N \le 3$), repeated sampling exposes substantial variation in failure probabilities. These discrepancies become particularly visible as temperature settings increase.

## Conclusion
The study demonstrates that shallow, single-shot benchmarks can dangerously obscure meaningful differences in model reliability. For [[Artificial Intelligence]] to be safely deployed in critical infrastructure, evaluation must evolve from assessing breadth to quantifying the statistical stability of models under sustained, repeated use.