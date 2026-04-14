---
title: Illocutionary Explanation Planning for Source-Faithful Explanations in Retrieval-Augmented Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.06211
tags: [ai, machine-learning, RAG, XAI, NLP]
category: ai
author: wiki-pipeline
dc.title: "Illocutionary Explanation Planning for Source-Faithful Explanations in Retrieval-Augmented Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/illocutionary-explanation-planning-for-source-faithful-explanations-in-retrieval.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Illocutionary Explanation Planning for Source-Faithful Explanations in Retrieval-Augmented Language Models

## Introduction
A fundamental challenge in [[explainable-ai-for-microseismic-event-detection|Explainable AI]] (XAI) is the "scrutability" of natural language explanations. While [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) are highly persuasive, their outputs often lack **faithfulness** and **traceability**. Users frequently find it difficult to verify whether the claims made in an explanation are actually supported by the underlying evidence or retrieved documents.

## The Research Problem
This study specifically examines these issues within the framework of [[contradictions-in-context-challenges-for-retrieval-augmented-generation-in-healt|Retrieval-Augmented Generation]] (RAG), focusing on its application in programming education. Using Stack Overflow questions grounded in authoritative programming textbooks, the researchers benchmarked six LLMs to quantify **source adherence**—the degree to which an explanation's claims can be traced back to an explicit source.

The baseline results were concerning:
* **Non-RAG models** demonstrated a median source adherence of 0%.
* **Baseline RAG systems** struggled with low median adherence, ranging between 22% and 40% depending on the specific model used.

##