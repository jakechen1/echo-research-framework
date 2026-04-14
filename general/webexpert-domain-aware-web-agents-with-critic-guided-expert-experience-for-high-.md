---
title: WebExpert: domain-aware web agents with critic-guided expert experience for high-precision search
created: 2024-05-22
source: https://arxiv.org/abs/2604.06177
tags: [ai, machine-learning, technology, information-retrieval]
category: ai
author: wiki-pipeline
dc.title: "WebExpert: domain-aware web agents with critic-guided expert experience for high-precision search"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/webexpert-domain-aware-web-agents-with-critic-guided-expert-experience-for-high-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# WebExpert

**WebExpert** is an advanced [[websp-eval-evaluating-web-agents-on-website-security-and-privacy-tasks|Web Agent]] framework designed to address the inherent difficulties of performing high-precision searches within specialized domains. While general-purpose agents perform well on broad queries, tasks in specialized fields such as [[Biomedicine]], [[Finance]], and [[Pharmaceuticals]] often suffer from "query drift," noisy evidence, and brittle reasoning due to a lack of domain-specific priors.

## Core Innovations

The WebExpert architecture introduces three fundamental components to stabilize reasoning and improve retrieval accuracy:

1.  **Sentence-Level Experience Retrieval**: The system implements a mechanism for retrieving granular, sentence-level experiences. This is paired with **topic merging** and **rule distillation** to consolidate knowledge and prevent the agent from becoming overwhelmed by redundant information.
2.  **Schemalight Facet Induction**: Moving away from traditional, static, hand-written lexicons, WebExpert uses weak supervision to bootstrap essential search facets. This allows the agent to automatically identify and track critical parameters such as **time**, **region**, **industry**, and **policy** within a specific domain context.
3.  **Preference-Optimized Planning**: The framework utilizes **pairwise preference learning** alongside a coverage-aware objective. This dual approach allows the agent to jointly optimize both its query planning strategies and its retrieval processes, ensuring that the search path remains focused on the target objective.

## Inference and Efficiency

At the inference stage, WebExpert utilizes a lightweight **experience gate**. This mechanism intelligently biases the decoding process toward active, high-utility facets. To ensure robustness, the system incorporates a fallback mechanism that triggers when retrieval confidence is low, preventing the agent from following incorrect reasoning paths.

## Performance Benchmarks

WebExpert has demonstrated significant improvements over the strongest existing [[Browsing Baseline]] models. In rigorous evaluations conducted on benchmarks including [[GAIA]], [[GPQA]], [[HLE]], and [[WebWalkerQA]], WebExpert achieved:

*   An increase in **Answer Exact Match (EM)** scores by 1.5 to 3.6 percentage points.
*   A measurable reduction in the number of **page hops** required to find information, indicating higher navigational efficiency and more precise [[Information Retrieval]].