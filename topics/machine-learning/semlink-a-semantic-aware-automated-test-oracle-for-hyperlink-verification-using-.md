---
title: SemLink: A Semantic-Aware Automated Test Oracle for Hyperlink Verification using Siamese Sentence-BERT
created: 2024-05-22
source: https://arxiv.org/abs/2604.05711
tags: [automated testing, semantic drift, NLP, web integrity, SBERT]
category: ai, machine-learning, technology
---

# SemLink: A Semantic-Aware Automated Test Oracle

The reliability of modern web applications depends heavily on the functional and contextual integrity of hyperlinks. While traditional verification tools are effective at identifying [[Link Rot]]—situations where target URLs return HTTP errors—they are fundamentally unable to detect [[Semantic Drift]]. This phenomenon occurs when a link remains technically active (returning an HTTP 200 status) but the destination content no longer aligns with the context provided by the source anchor text, compromising the user experience.

## The SemLink Architecture

To address this gap, the researchers introduced [[SemLink]], a novel [[Automated Test Oracle]] designed specifically for semantic hyperlink verification. While [[Large Language Models]] (LLMs) possess high-level semantic understanding, their application in large-scale [[Regression Testing]] is often hindered by high latency, significant computational costs, and potential privacy concerns.

[[SemLink]] overcomes these hurdles by leveraging a [[Siamese Neural Network]] architecture powered by a pre-trained [[Sentence-BERT]] (SBERT)