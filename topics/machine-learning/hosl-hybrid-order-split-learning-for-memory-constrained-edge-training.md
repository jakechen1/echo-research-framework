---
title: HOSL: Hybrid-Order Split Learning for Memory-Constrained Edge Training
created: 2024-05-22
source: https://arxiv.org/abs/2601.10940
tags: [edge computing, optimization, split learning, LLM training]
category: ai, machine-learning, technology
---

# HOSL: Hybrid-Order Split Learning for Memory-Constrained Edge Training

**HOSL** (Hybrid-Order Split Learning) is a novel framework designed to facilitate the collaborative training of [[Large Language Models (LLMs)]] between resource-constrained edge devices and compute-rich servers. The framework operates within the paradigm of [[Split Learning (SL)]], where the architecture of a neural network is partitioned across a network boundary to balance computational load.

## The Optimization Trade-off

Traditionally, Split Learning systems have relied on [[First-Order (FO) Optimization]]. While effective, FO optimization requires edge clients to store intermediate quantities, such as activations, to facilitate backpropagation. In the context of massive models, this memory overhead often negates the primary benefits of offloading computation to a server.

An alternative approach is [[Zeroth-Order (ZO) Optimization]]. Because ZO optimization eliminates the need for backpropagation, it significantly reduces the client's memory footprint. However, this method is notorious for slow convergence rates and degraded model performance, making it difficult to train complex architectures efficiently.

## The HOSL Solution

HOSL addresses this fundamental tension by strategically integrating both optimization types into a single framework. The system employs a hybrid strategy:

*   **Client-Side:** Utilizes **ZO optimization** for gradient estimation. This eliminates the need for storing activations, thereby drastically reducing the GPU memory required by the edge device.
*   **Server-Side:** Utilizes **FO optimization** to maintain high performance and ensure rapid convergence.

## Performance and Results

Theoretical analysis shows that HOSL achieves a convergence rate of $\mathcal{O}(\sqrt{d_c/TQ})$, where the rate is dependent on the client-side model dimension ($d_c$) rather than the total model dimension ($d$). This implies that increasing the amount of computation offloaded to the server directly improves convergence efficiency.

Extensive testing on [[OPT Models]] (125M and 1.3B parameters) demonstrates the practical advantages of HOSL:
*   **Memory Efficiency:** Reduces client-side GPU memory consumption by up to **3.7$\times$** compared to standard FO methods.
*   **Accuracy:** Maintains high-fidelity training, with accuracy remains within 0.20%–4.23% of the FO baseline.
*   **Superiority over ZO:** Outperforms pure ZO-based training benchmarks by up to **15.55%**.