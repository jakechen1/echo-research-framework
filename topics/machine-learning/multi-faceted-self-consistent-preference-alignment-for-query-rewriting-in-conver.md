---
title: Multi-Faceted Self-Consistent Preference Alignment for Query Rewriting in Conversational Search
created: 2024-05-23
source: https://arxiv.org/abs/2604.06771
tags: [conversational-search, query-rewriting, machine-learning, preference-alignment, retrieval-augmented-generation]
category: ai
---

# Multi-Faceted Self-Consistent Preference Alignment (MSPA-CQR)

In the evolving landscape of [[conversational-search|Conversational Search]], a primary obstacle is the ambiguity inherent in user queries. [[multi-faceted-self-consistent-preference-alignment-for-query-rewriting-in-conver|Query Rewriting]] (CQR) serves as a vital mechanism to resolve this ambiguity, transforming vague or context-dependent inputs into clear, searchable instructions. However, traditional CQR models have focused excessively on the rewriting task in isolation, neglecting the downstream consequences of the rewrite on the entire search pipeline.

The research titled "Multi-Faceted Self-Consistent Preference Alignment for Query Rewriting in Conversational Search" introduces **MSPA-CQR**, a novel framework designed to bridge this gap. Unlike prior methods, MSPA-CQR considers the feedback loop between three critical stages: the rewritten query itself, the subsequent [[passage-retrieval|Passage Retrieval]], and the final [[response-generation|Response Generation]].

###