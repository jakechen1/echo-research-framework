---
title: "$\pi^2$: Structure-Originated Reasoning Data Improves Long-Context Reasoning Ability of Large Language Models"
created: 2024-05-23
source: https://arxiv.org/abs/2604.05114
tags: [LLM, long-context, reasoning, data curation, self-distillation]
category: ai
---

# $\pi^2$: Structure-Originated Reasoning Data Improves Long-Context Reasoning Ability of Large Language Models

The $\pi^2$ framework introduces a novel pipeline designed to enhance the [[Long-Context Reasoning]] capabilities of [[Large Language Models]] (LLMs) through the curation of high-quality, structure-originated reasoning data. As modern models struggle to maintain accuracy when retrieving and reasoning over extended sequences, $\pi^2$ provides a systematic method to synthesize training data that mimics complex, multi-step analytical tasks.

## Methodology

The $\pi^2$ pipeline follows a rigorous three-stage QA (Question Answering) curation process:

1.  **Data Extraction**: The process begins by extracting and expanding structured information from [[Wikipedia]] tables. This creates a foundational layer of factual, organized data from which complex relationships can be identified.
2.  **Question Generation & Verification**: Using the collected tables and relevant context, the system generates complex, multi-hop analytical reasoning questions. To ensure high precision and prevent [[Hallucination]], the answers are automatically verified through a **dual-path code execution** mechanism, ensuring that the ground truth is computationally sound.
3.  **Reasoning Trace Synthesis**: The final stage involves "back-translating" structured data into step-by-step reasoning traces. These traces are presented as solutions to the QA pairs, framed within realistic [[Web-Search]] contexts to simulate real-world information retrieval and processing.

## Performance and Results