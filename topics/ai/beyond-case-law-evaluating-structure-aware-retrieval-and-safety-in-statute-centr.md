---
title: Beyond Case Law: Evaluating Structure-Aware Retrieval and Safety in Statute-Centric Legal QA
created: 2024-05-22
source: https://arxiv.org/abs/2604.06173
tags: [Legal AI, RAG, Benchmarking, Hallucination, Regulatory Compliance]
category: ai
---

# Beyond Case Law: Evaluating Structure-Aware Retrieval and Safety in Statute-Centric Legal QA

The research paper "Beyond Case Law: Evaluating Structure-Aware Retrieval and Safety in Statute-Centric Legal QA" addresses a critical oversight in current [[Legal QA]] benchmarking: the unique structural complexities of statute-centric regulatory reasoning. While existing benchmarks primarily focus on case law, the authors argue that statutory domains present a "statutory retrieval gap" due to evidence being distributed across hierarchically linked documents.

To address this, the authors introduce **SearchFireSafety**, a new benchmark designed to evaluate both structure-aware retrieval and model safety. Using fire-safety regulations as a domain-specific use case, the benchmark assesses the ability of [[Large Language Models (LLMs)]] to navigate fragmented, hierarchical evidence. The evaluation framework is dual-faceted:
1. **Citation-Aware Retrieval:** Real-world questions that require locating specific, linked regulatory evidence.
2. **Safety Stress-Testing:** Synthetic partial-context scenarios designed to test for [[Hallucination]] and the model's ability to safely abstain from answering when statutory context is insufficient.

The experimental results highlight the effectiveness of [[Graph-guided retrieval]] in improving retrieval accuracy within complex, interconnected legal structures. However, the study also uncovers a significant safety risk: domain-adapted models exhibit a higher propensity for [[Hallucination]] when essential statutory context is missing. This suggests a critical trade-off between domain expertise and adherence to safety protocols (the ability to refuse uncertain answers).

Ultimately, the paper underscores the necessity for future development in [[Retrieval-Augmented Generation (RAG)]] to prioritize benchmarks that simultaneously evaluate hierarchical retrieval capabilities and the safety of model responses in evidence-deprived, regulatory-heavy environments. This work is vital for the advancement of [[Regulatory Technology]] and the deployment of reliable [[Artificial Intelligence]] in high-stakes legal settings.