---
title: "DeepReviewer 2.0: A Traceable Agentic System for Auditable Scientific Peer Review"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.09590"
tags: [agentic_systems, peer_review, automation, traceability, LLM]
category: [ai, machine-learning]
dc.title: "DeepReviewer 2.0: A Traceable Agentic System for Auditable Scientific Peer Review"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/deepreviewer-2.0-a-traceable-agentic-system-for-auditable-scientific-peer-review.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# DeepReviewer 2.0: A Traceable Agentic System for Auditable Scientific Peer Review

DeepReviewer 2.0 represents a paradigm shift in [[Automated Peer Review]] by moving beyond the generation of fluent critiques toward the production of auditable, evidence-based judgments. While many current applications of [[Large Language Models]] in science focus on summarization, DeepReviewer 2.0 addresses the fundamental needs of reviewers and area chairs: the ability to audit claims, locate supporting evidence, and identify required follow-up actions.

## Methodology

The system is designed as a process-controlled [[Agentic System]] governed by a strict "output contract." Rather than generating a single block of text, it produces a **traceable review package**. The architecture follows a multi-stage workflow:

1.  **Ledger Formulation**: The agent first constructs a manuscript-only ledger that maps out claims, evidence, and potential risks, alongside a structured verification agenda.
2.  **Agenda-Driven Retrieval**: Using the verification agenda, the system performs targeted retrieval to substantiate or challenge the identified claims.
3.  **Export Gate**: To ensure quality, the system utilizes an "export gate" mechanism. A review is only finalized and exported if it meets predefined minimum budgets for traceability and coverage.

This process results in critiques featuring anchored annotations and localized evidence, making the reasoning process transparent and reproducible.

## Performance and Benchmarks

In evaluations conducted on 134 ICLR 2025 submissions, the DeepReviewer 2.0 framework—running on an un-finetuned 196B parameter model—demonstrated significant advantages over existing [[Machine Learning]] approaches. Key findings include:

*   **Superior Coverage**: The system achieved a strict major-issue coverage of 37.26%, significantly outperforming Gemini-3.1-Pro-preview at 23.57%.
*   **Human-Level Comparison**: In micro-averaged blind comparisons against a human review committee, DeepReviewer 2.0 won 71.63% of the trials.
*   **System Ranking**: The framework ranked first among all automated systems tested in the study pool.

## Conclusion and Future Work

The developers position DeepReviewer 2.0 as an assistive tool for the scientific community rather than