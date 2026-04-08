---
title: "Which English Do LLMs Prefer? Triangulating Structural Bias Towards American English in Foundation Models"
created: 2024-05-23
source: https://arxiv.org/abs/2604.04204
tags: [LLM, Linguistic Bias, NLP, Machine Learning, American English]
category: ai
---

# Which English Do LLMs Prefer?

The research paper **"Which English Do LLMs Prefer? Triangulating Structural Bias Towards American English in Foundation Models"** investigates the systemic preference for [[American English]] (AmE) within [[Large Language Models]] (LLMs). The study examines how the intersection of geopolitical history, data curation, and digital dominance creates a structural bias that favors one dialect over others, specifically [[British English]] (BrE).

## Methodology
To quantify this phenomenon, the authors introduced **DiAlign**, a dynamic, training-free method designed to estimate dialectal alignment through distributional evidence. The researchers constructed a curated corpus consisting of 1,813 AmE–BrE variants to analyze the entire development lifecycle of [[Foundation Models]].

## The Three Pillars of Structural Bias
The study employs a "triangulated" approach to demonstrate that bias is embedded across three distinct stages of the [[Machine Learning]] pipeline:

1.  **Data Curation**: Audits of six major pretraining corpora revealed a systematic skew toward AmE during the initial data collection and curation phases.
2.  **Tokenization**: Analysis of the [[Tokenizer]] layer demonstrated that BrE forms incur higher segmentation costs