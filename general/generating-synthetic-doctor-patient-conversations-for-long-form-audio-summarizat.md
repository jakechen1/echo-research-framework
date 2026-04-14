---
title: Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization
created: 2024-05-23
source: https://arxiv.org/abs/2604.06138
tags: [synthetic-data, audio-processing, medical-ai, long-context, machine-learning]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/generating-synthetic-doctor-patient-conversations-for-long-form-audio-summarizat.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization

The research paper "Generating Synthetic Doctor-Patient Conversations for Long-form Audio Summarization" addresses a critical gap in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] research: the lack of high-quality training and evaluation data for long-context [[Audio Processing]]. While existing benchmarks are proficient at handling short-context audio tasks, they struggle with the open-ended, long-form reasoning required for complex scenarios, such as medical consultations.

## The Synthetic Generation Pipeline

To bridge this gap, the authors propose a robust three-stage pipeline designed to function as both a training resource and a controlled evaluation environment. Notably, the entire pipeline is built using [[the-end-of-the-foundation-model-era-open-weight-models-sovereign-ai-and-inferenc|Open-Weight Models]], ensuring accessibility for the broader research community. The pipeline consists of:

1.  **Persona-Driven Dialogue Generation**: Creating nuanced, medically relevant scripts based on specific patient and physician personas.
2.  **Multi-Speaker Audio Synthesis**: Generating complex audio that incorporates realistic human elements such as overlapping speech, pauses, and ambient room acoustics, alongside various environmental sound events.
3.  **LLM-based Reference Production**: Utilizing [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] to produce standardized SOAP (Subjective, Objective, Assessment, and Plan) notes based on the synthesized dialogues to serve as ground truth.

## Dataset and Key Findings

The researchers released a substantial dataset comprising 8,800 synthetic conversations, totaling approximately 1