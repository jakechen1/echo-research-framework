---
title: MG$^2$-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation
created: 2024-05-23
source: https://arxiv.org/abs/2604.04969
tags: [multimodal, RAG, knowledge-graphs, MLLM, computer-vision]
categories: [ai, machine-learning]
---

# MG$^2$-RAG: Multi-Granularity Graph for Multimodal Retrieval-Augmented Generation

[[Retrieval-Augmented Generation]] (RAG) has become a standard technique for mitigating [[hallucinations]] in [[Large Language Models]] (LLMs). However, extending these capabilities to [[Multimodal Large Language Models]] (MLLMs) presents significant challenges, particularly regarding complex cross-modal reasoning. Existing systems often suffer from the limitations of "flat" vector retrieval, which ignores structural dependencies, or rely on inefficient "translation-to-text" pipelines that discard vital fine-grained visual information.

## The MG$^2$-RAG Framework

To overcome these hurdles, the **MG$^2$-RAG** framework introduces a lightweight approach to building a hierarchical multimodal [[Knowledge Graph]]. The core innovation lies in its ability to jointly improve graph construction, modality fusion, and cross-modal retrieval.

### Key Methodologies

*   **Hierarchical Construction:** The framework combines lightweight textual parsing with entity-driven [[Visual Grounding]]. This enables the system to fuse textual entities and specific visual regions into unified multimodal nodes, ensuring that atomic visual evidence is preserved rather than lost in text conversion.
*   **Multi-Granularity Retrieval:** Instead of simple similarity searches, MG$^2$-RAG utilizes a mechanism that aggregates dense similarities and propagates relevance across the graph. This structure supports complex [[multi-hop reasoning]], allowing the model to traverse relationships between different segments of data.

## Performance and Efficiency

Experimental results across four fundamental multimodal tasks—retrieval, [[Visual Question Answering]] (VQA), reasoning, and classification—indicate that MG$^2$-RAG consistently achieves state-of-the-art performance. 

Beyond accuracy, the framework offers substantial computational advantages over existing advanced graph-based architectures. MG$^2$-RAG demonstrates:
*   An average **43.3$\times$ speedup** in graph construction.
*   An average **23.9$\times$ reduction in cost**.

These efficiencies make MG$^2$-RAG a highly scalable solution for the next generation of multimodal AI applications, providing robust reasoning capabilities without the prohibitive overhead of previous graph-based methods.