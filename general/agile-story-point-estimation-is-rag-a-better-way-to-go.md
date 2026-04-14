---
title: "Agile Story-Point Estimation: Is RAG a Better Way to Go?"
created: 2024-05-22
source: https://arxiv.org/abs/2604.03443
tags: [Agile, RAG, Software Engineering, Automation, Machine Learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Agile Story-Point Estimation: Is RAG a Better Way to Go?"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/agile-story-point-estimation-is-rag-a-better-way-to-go.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Agile Story-Point Estimation: Is RAG a Better Way to Go?

## Overview
In [[Agile Software Development]], estimating the effort required to complete tasks is a fundamental component of the sprint planning process. Developers typically use a unit of measurement known as [[Story Points]] to represent the complexity and time required for specific tasks. Traditional estimation techniques, such as [[Planning Poker]], rely on manual, consensus-based human interaction. While effective for alignment, these manual processes are incredibly time-consuming. This paper investigates whether [[contradictions-in-context-challenges-for-retrieval-augmented-generation-in-healt|Retrieval Augmented Generation]] (RAG) can be utilized to automate this estimation process.

## Methodology
The researchers proposed an automated framework using a RAG architecture, which consists of two core components: a "Retriever" and a "Generator." To test the efficacy of this approach, the study analyzed 23 open-source software projects of varying sizes. The researchers specifically examined the impact of different [[Embedding Models]] on the accuracy of the estimations, utilizing:
* **bge-large-en-v1.5**
* **Sentence-Transformers' all-mpnet-base-v2**

The study was structured to evaluate four key research dimensions:
1. The influence of retrieval hyper-parameters on system performance.
2. The relationship between project scale and estimation accuracy.
3. The comparative impact of different embedding model selections.
4. The performance of the RAG-based approach against existing baseline models.

## Key Findings
The study found that while the RAG-based approach outperformed existing baseline models on several occasions, the results did not demonstrate statistically significant differences in performance across the various projects or embedding models tested. This implies that while the framework shows promise, it is not yet a definitive replacement for manual estimation.

## Conclusion
The findings highlight a significant opportunity for further research in [[Natural Language Processing]] and [[Automated Software Engineering]]. To achieve reliable accuracy in automatically estimating user stories, future studies must focus on refining [[Retrie