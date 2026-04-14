---
title: HingeMem: Boundary Guided Long-Term Memory with Query Adaptive Retrieval for Scalable Dialogues
created: 2024-05-22
source: https://arxiv.org/abs/2604.06845
tags: [ai, llm, retrieval, machine-learning, memory]
category: ai
---

# HingeMem

**HingeMem** is a novel framework designed to enhance the long-term memory capabilities of dialogue systems. As [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) move toward more personalized and continuous interactions, the ability to efficiently store, retrieve, and manage historical context becomes critical for sustainable conversation.

### The Problem: Inefficiency in Existing Methods
Traditional approaches to long-term memory often rely on continuous summarization or complex graph construction (such as [[openie|OpenIE]]-based methods). These systems typically utilize a fixed **Top-k retrieval** strategy, which fails to adapt to different types of user queries and often incurs significant [[computational-overhead|computational overhead]]. This lack of adaptability makes it difficult to maintain context across very long, multi-topic interactions.

### The Solution: Boundary-Guided Memory
Inspired by **event segmentation theory** from [[neuroscience]], HingeMem introduces a method to partition memory into distinct, meaningful segments. Instead of continuous, redundant updates, the system draws a "boundary" whenever a significant change occurs in one of four key elements:
*   **Person**
*   **Time**
*   **Location**
*   **Topic**

By creating boundary-triggered hyperedges over these elements, HingeMem builds an interpretable indexing