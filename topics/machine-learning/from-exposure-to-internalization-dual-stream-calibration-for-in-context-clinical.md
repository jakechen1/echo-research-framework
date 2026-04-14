---
title: From Exposure to Internalization: Dual-Stream Calibration for In-context Clinical Reasoning
created: 2024-05-22
source: https://arxiv.org/abs/2604.06262
tags: [clinical reasoning, test-time training, meta-learning, large language models, artificial intelligence]
category: ai, machine-learning
---

# From Exposure to Internalization: Dual-Stream Calibration for In-context Clinical Reasoning

## Overview
In the domain of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] applied to healthcare, the ability to interpret complex and heterogeneous clinical records is paramount. Traditional methodologies, such as [[in-context-learning-icl|In-Context Learning (ICL)]] and [[retrieval-augmented-generation-rag|Retrieval-Augmented Generation (RAG)]], focus primarily on "knowledge exposure"—the act of providing a model with relevant external data. However, these methods often fail to achieve true "contextual internalization," where a model's internal representations are dynamically adjusted to the specific nuances of a particular case during inference.

The paper introduces **Dual-Stream Calibration (DSC)**, a novel [[in-place-test-time-training|Test-Time Training]] framework designed to transition from passive data exposure to deep contextual internalization.

## The DSC Framework
DSC facilitates