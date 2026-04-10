---
title: Accordion-Thinking: Self-Regulated Step Summaries for Efficient and Readable LLM Reasoning
created: 2024-05-22
source: https://arxiv.org/abs/2602.03249
tags: [AI, Machine Learning, Inference Optimization, LLM, Reinforcement Learning]
category: ai, machine-learning
---

# Accordion-Thinking

**Accordion-Thinking** is an innovative end-to-end framework designed to optimize the scaling of [[Large Language Model]] (LLM) reasoning. As modern models leverage extended [[Chain-of-Thought]] (CoT) processes to improve accuracy, they face significant computational hurdles, specifically the linear growth of the [[KV cache]] and the quadratic complexity of the [[Attention mechanism]].

### The Mechanism: Fold vs. Unfold
The framework introduces a method for LLMs to self-regulate the granularity of their reasoning steps through dynamic summarization. The system operates in two primary states:

*   **Unfold Mode:** The model performs exhaustive, granular reasoning, maintaining a full history of all tokens used in the thought process.
*   **Fold Mode:** The model periodically summarizes its preceding thoughts and discards the original, heavy historical tokens. This "self-compression" drastically reduces the dependency on long-term token history, effectively "folding" the context to save memory.

### Reinforcement Learning and Self-Compression
The researchers applied [[Reinforcement Learning]] to train models to master this periodic summarization. A critical discovery during training was that the accuracy gap between the computationally expensive Unfold mode and the efficient Fold mode progressively narrows and eventually disappears. This indicates that the model successfully learns to encode all vital reasoning logic into compact, high-density summaries.

### Key Advantages
The implementation of Accordion-Thinking provides several transformative benefits for [[Inference Optimization]]:

1.  **Increased Throughput:** The framework achieves up to three times the throughput of standard reasoning methods.
2.  **Memory Efficiency:** It enables complex reasoning on hardware with limited capacity, such as a 48GB GPU configuration, by minimizing token overhead.
3.  **Human Readability:** Unlike opaque compression methods, the structured step summaries provide a clear, human-readable account of the model's logical progression.

By demonstrating successful [[Self-Compression]], Accordion-Thinking proves that LLMs can tackle increasingly complex tasks without the prohibitive costs typically associated with expanding context length.