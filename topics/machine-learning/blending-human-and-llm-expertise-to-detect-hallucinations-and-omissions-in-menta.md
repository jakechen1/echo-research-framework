---
title: Blending Human and LLM Expertise to Detect Hallucinations and Omissions in Mental Health Chatbot Responses
created: 2024-05-22
source: https://arxiv.org/abs/2604.06216
tags: [mental health, LLM, hallucination, healthcare AI, machine learning, evaluation]
category: ai
---

# Blending Human and LLM Expertise to Detect Hallucinations and Omissions in Mental Health Chatbot Responses

As [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) are increasingly integrated into [[human-computer-interactions-predict-mental-health|mental health]] services, the ability to detect [[blending-human-and-llm-expertise-to-detect-hallucinations-and-omissions-in-menta|hallucination]] and omissions is vital for user safety. Current "LLM-as-a-judge" methodologies often struggle in high-risk [[before-humans-join-the-team-diagnosing-coordination-failures-in-healthcare-robot|healthcare]] environments, where subtle errors can lead to significant clinical consequences. 

## The Problem of LLM Reliability
Research indicates that state-of-the-art LLM judges achieve only 52% accuracy when evaluated against mental health counseling data. Notably, some approaches for detecting hallucinations demonstrate near-zero recall. The fundamental issue lies in the inability of LLMs to capture the nuanced linguistic and therapeutic patterns that [[domain-experts|domain experts]] recognize. These "black-box" evaluation methods fail to account for the specific complexities of psychiatric discourse.

## A Hybrid Framework for Detection
To address these limitations, a new framework has been proposed that integrates human expertise with automated processes. Instead of relying solely on LLM intuition, this method extracts interpretable, domain-informed features across five analytical dimensions:
1. **Logical consistency**
2. **Entity verification**
3. **Factual accuracy**
4.