---
title: "WRAP++: Web discoveRy Amplified Pretraining"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06829"
tags: [LLM, Synthetic Data, Pretraining, Knowledge Discovery, NLP]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "WRAP++: Web discoveRy Amplified Pretraining"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/wrap-web-discovery-amplified-pretraining.md
dc.language: en
dc.rights: CC-BY-4.0
---

# WRAP++: Web discoveRy Amplified Pretraining

## Overview
**WRAP++ (Web discoveRy Amplified Pretraining)** is an advanced framework designed to enhance the knowledge acquisition process during the [[prime-prototype-driven-multimodal-pretraining-for-cancer-prognosis-with-missing-|Pretraining]] phase of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). While current trends in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] leverage [[dynamic-context-evolution-for-scalable-synthetic-data-generation|Synthetic Data]] to augment training sets, WRAP++ moves beyond simple text rephrasing by focusing on the discovery and amplification of cross-document relationships.

## The Limitation of Single-Document Rewriting
Traditional synthetic data techniques typically operate at the single-document level, rewriting individual web pages in isolation. This approach creates a significant bottleneck: the synthesized examples are confined to "intra-document" knowledge. Consequently, the models miss critical cross-document connections, and the resulting factual data lacks the associative context necessary for complex reasoning.

## The WRAP++ Approach
WRAP++ addresses these limitations by identifying and exploiting the interconnected nature of the web. The framework focuses on two primary methods of discovery:
* **Relational Motifs:** The system identifies high-confidence connections, such as **dual-links** (where two pages link to each other) and **co-mentions** (where two entities are mentioned within the same context).
* **Joint QA Synthesis:** Once document pairs are identified, WRAP++ synthesizes Question Answering (QA) pairs that specifically require reasoning across both documents.

This method produces "relational knowledge"—information that is not explicitly present in either source document alone but emerges from their intersection. Because the potential for entity pairing grows combinatorially, WRAP++ serves as a massive data amplifier.

## Empirical Results
The power of the framework was demonstrated by applying it to [[Wikipedia]]. The process amplified roughly 8.4 billion tokens of raw text into a massive 80 billion tokens of cross-document QA data. 

When implemented on [[hardware-oriented-inference-complexity-of-kolmogorov-arnold-networks|OLMo]] architectures at the 7B and 32B scales, models trained with WRAP++ showed significant performance improvements on the [[SimpleQA]] benchmark compared to single-document rewriting methods. The results indicate sustained scaling gains, suggesting that cross-document knowledge discovery is a key driver for the future of [[Natural Language Processing]].