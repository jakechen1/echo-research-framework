---
title: "ConfusionPrompt: Practical Private Inference for Online Large Language Models"
created: 2024-05-22
source: https://arxiv.org/abs/2401.00870
tags: [privacy, LLM, inference, security, machine-learning]
category: ai
---

# ConfusionPrompt: Practical Private Inference for Online Large and Cloud-based LLMs

## Overview
As [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) become central to modern digital workflows, the industry standard has shifted toward online services hosted on [[cloud-computing|Cloud Computing]] infrastructure. While highly accessible, this model necessitates that users transmit detailed, often sensitive, prompts to remote servers, creating significant [[data-privacy|Data Privacy]] vulnerabilities. **ConfusionPrompt** is a novel framework designed to facilitate private [[epistemic-blinding-an-inference-time-protocol-for-auditing-prior-contamination-i|Inference]] for these online services.

## Methodology
ConfusionPrompt mitigates privacy risks by preventing the server from reconstructing the original, sensitive intent of the user. The framework operates through a specialized two-step process:

1.  **Prompt Decomposition**: The original user prompt is decomposed into several smaller, less descriptive sub-prompts.
2.