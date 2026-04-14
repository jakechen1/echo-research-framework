---
title: Entropy After </Think> for reasoning model early exiting
created: 2024-05-22
source: https://arxiv.org/abs/2509.26522
tags: [LLM, Reasoning, Early Exiting, Entropy, Inference Optimization]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "Entropy After </Think> for reasoning model early exiting"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/entropy-after-think-for-reasoning-model-early-exiting.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Entropy After </Think> for reasoning model early exiting

The research paper "Entropy After </Think> for reasoning model early exiting" addresses the phenomenon of "overthinking" in modern [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) that utilize [[tool-mcot-tool-augmented-multimodal-chain-of-thought-for-content-safety-moderati|Chain-of-Thought]] (CoT) reasoning. While extended reasoning steps generally improve performance on complex tasks, recent studies have shown that these models often continue generating redundant tokens even after the correct solution has been determined. This leads to significant [[computational inefficiency]] and unnecessary resource consumption during [[epistemic-blinding-an-inference-time-protocol-for-auditing-prior-contamination-i|inference]].

To mitigate this, the authors propose a novel, inexpensive signal called **Entropy After </Think> (EAT)**. The mechanism works by appending a stop-thinking token (`</Think>`) and monitoring the probabilistic entropy of the following token as the model proceeds through its reasoning trajectory. The researchers found that as the model's accuracy (Pass@1) reaches a plateau, the entropy of the token following the stop tag begins to decrease and stabilize. By applying a threshold to the variance of this entropy—using an exponential moving average (EMA)—the system can implement an effective [[entropy-after-think-for-reasoning-model-early-exiting|early exiting]] rule.

The primary advantage of EAT is its ability to facilitate **adaptive compute allocation**. Instead of using a fixed token budget for every prompt, EAT allows the model to terminate reasoning as soon as confidence is high, effectively spending more compute on difficult queries and less on simpler ones. Empirical evaluations on challenging benchmarks, such as MATH500 and AIME2025, demonstrate that EAT reduces total token usage by **12% to 22%** without any loss in model accuracy.

Notably, EAT is highly versatile and functions effectively in [[robust-adaptation-of-foundation-models-with-black-box-visual-prompting|black-box]] settings. The authors demonstrated that the