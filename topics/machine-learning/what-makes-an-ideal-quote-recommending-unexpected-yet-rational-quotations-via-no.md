---
title: What Makes an Ideal Quote? Recommending "Unexpected yet Rational" Quotations via Novelty
created: 2024-05-22
source: https://arxiv.org/abs/2602.22220
tags: [quotation recommendation, NLP, novelty, generative AI, information retrieval]
category: ai, machine-learning
---

# What Makes an Ideal Quote? Recommending "Unexpected yet Rational" Quotations via Novelty

The research paper "What Makes an Ideal Quote? Recommending 'Unexpected yet Rational' Quotations via Novelty" identifies a significant limitation in modern [[Natural Language Processing]] (NLP): the tendency of recommendation systems to prioritize surface-level topical relevance over the deep semantic and aesthetic qualities that make quotations memorable.

## The Problem of Contextual Boredom
Traditional quotation recommendation systems focus primarily on matching keywords or topics between a context and a quote. However, the authors argue that this approach ignores the "deeper" meaning of language. Through empirical user studies, the researchers discovered that humans do not simply want relevant quotes; they prefer quotations that are **"unexpected yet rational."** 

This principle suggests that an ideal quote should provide a sense of [[Novelty]] (a surprise or shift in perspective) while remaining logically anchored to the provided context (semantic coherence).

## The NovelQR Framework
To bridge the gap between topical relevance and aesthetic impact, the authors propose **NovelQR**, a novelty-driven framework grounded in [[Defamiliarization Theory]]. The system utilizes two innovative components:

1.  **Generative Label Agent:** Instead of simple keyword matching, this agent interprets both the quotation and its surrounding context into multi-dimensional, deep-meaning labels. This allows for a more nuanced form of [[Information Retrieval]] based on semantic essence rather than mere word overlap.
2.  **Token-level Novelty Estimator:** To prevent the system from merely suggesting the most predictable (and therefore boring) continuations, this estimator reranks candidates. It specifically addresses "auto-regressive continuation bias," ensuring the recommended text provides the desired "unexpected" element.

## Experimental Findings
Evaluations conducted on diverse bilingual datasets demonstrated that NovelQR significantly outperforms existing [[Machine Learning]] baselines. Human judges rated the system's recommendations as more appropriate, more novel, and more engaging. The study concludes that incorporating novelty estimation is crucial for developing [[Generative AI]] that mimics the sophisticated aesthetic preferences of human writers.