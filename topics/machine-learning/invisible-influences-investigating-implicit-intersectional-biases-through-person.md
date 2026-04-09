---
title: "Invisible Influences: Investigating Implicit Intersectional Biases through Persona Engineering in Large Language Models"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06213"
tags: [bias-detection, llm-evaluation, persona-engineering, ai-ethics, machine-learning]
category: ai
---

# Invisible Influences: Investigating Implicit Intersectional Biases through Persona Engineering in Large Language Models

The research paper "Invisible Influences" explores how [[Large Language Models]] (LLMs) amplify implicit, intersectional biases through the mechanism of [[Persona Engineering]]. While LLMs excel at human-like language generation, their behavior changes significantly when prompted to adopt specific social roles, potentially surfacing latent prejudices that remain hidden during standard testing.

### The Limitation of Static Audits
Existing bias audits—including metrics such as CEAT, I-WEAT, and I-SEAT—primarily rely on static, embedding-based tests. These methods quantify absolute association strengths but fail to capture the dynamic shifts in bias that occur when a model adopts different social identities