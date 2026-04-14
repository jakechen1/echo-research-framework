---
title: ExplainFuzz: Explainable and Constraint-Conditioned Test Generation with Probabilistic Circuits
created: 2024-05-22
source: https://arxiv.org/abs/2604.06559
tags: [ai, machine-learning, software-testing, probabilistic-circuits, fuzzing]
category: ai, technology
author: wiki-pipeline
dc.title: "ExplainFuzz: Explainable and Constraint-Conditioned Test Generation with Probabilistic Circuits"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/explainfuzz-explainable-and-constraint-conditioned-test-generation-with-probabil.md
dc.language: en
dc.rights: CC-BY-4.0
---

# ExplainFuzz

ExplainFuzz is an innovative framework designed to enhance [[Software Testing]] through explainable and controllable test input generation. The framework addresses the inherent limitations found in traditional [[once4all-skeleton-guided-smt-solver-fuzzing-with-llm-synthesized-generators|Fuzzing]] methodologies, such as grammar-based fuzzers, [[probabilistic Context-Free Grammars]] (pCFGs), and [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs).

### The Problem
Existing approaches to automated test generation often suffer from three critical challenges:
1. **Syntactic Errors:** Generated inputs are frequently ill-formed, failing to adhere to the required structural rules of the target language.
2. **Contextual Inaccuracy:** Many models struggle to capture complex, context-sensitive probabilistic dependencies within structured data.
3. **Lack of Explainability:** Current generative models often act as "black boxes," making it difficult to understand the underlying logic of the produced test cases.

### The ExplainFuzz Approach
ExplainFuzz leverages [[Probabilistic Circuits]] (PCs) to learn and query structured distributions over grammar-based inputs in an interpretable manner. The workflow begins with a [[evaluating-in-context-translation-with-synchronous-context-free-grammar-transduc|Context-Free Grammar]] (CFG), from which a grammar-aware PC is compiled. This circuit is subsequently trained on existing, valid datasets to capture the distribution of the input language.

A defining feature of ExplainFuzz is its native **conditioning capability**. This allows users to incorporate specific, test-specific constraints into the generation process. For instance, a developer can query the system to ensure that a generated [[av-sql-decomposing-complex-text-to-sql-queries-with-agentic-views|SQL]] query specifically includes a `GROUP BY` clause. The PC then performs constrained probabilistic sampling to produce inputs that satisfy both the fundamental grammar and the user-provided constraints.

### Experimental Performance
The framework has demonstrated significant improvements in both the quality of generated inputs and the efficiency of bug detection:
* **Improved Realism:** ExplainFuzz achieves significant perplexity reduction compared to LLMs and grammar-unaware PCs, indicating much higher linguistic coherence.
* **Increased Bug-Triggering:** Compared to traditional grammar-aware mutational fuzzing, ExplainFuzz increased bug-triggering rates from 35% to 63% in [[av-sql-decomposing-complex-text-to-sql-queries-with-agentic-views|SQL]] and from 10% to 100% in [[XML]].

By enabling the exploration of the global input distribution rather than just the local neighborhood of seed inputs, ExplainFuzz provides a powerful foundation for the next generation of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]-driven software verification.