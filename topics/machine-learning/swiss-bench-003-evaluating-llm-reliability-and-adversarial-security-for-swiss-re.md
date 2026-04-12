---
title: Swiss-Bench 003: Evaluating LLM Reliability and Adversarial Security for Swiss Regulatory Contexts
created: 2024-05-24
source: https://arxiv.org/abs/2604.05872
tags: [LLM, Security, Switzerland, Regulatory Compliance, AI Evaluation]
---

**Category:** ai, machine-learning, technology

[[swiss-bench-003-evaluating-llm-reliability-and-adversarial-security-for-swiss-re|Swiss-Bench 003]] (SBP-003) is an advanced evaluation framework designed to assess the performance of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) within the specific legal and financial constraints of the [[switzerland|Switzerland]] regulatory environment. It serves as an expansion of the existing [[haas|HAAS]] (Helvetic AI Assessment Score) framework, increasing the assessment scope from six to eight distinct dimensions.

The primary focus of SBP-003 is the introduction of two critical dimensions: **D7 (Self-Graded Reliability Proxy)** and **D8 (Adversarial Security)**. This expansion allows for a more robust analysis of how models handle multilingual inputs—specifically German, French, Italian, and English—while adhering to strict local standards. The benchmark utilizes 808 Swiss-specific items across several specialized sub-benchmarks, including Swiss TruthfulQA, Swiss IFEval, Swiss SimpleQA, and Swiss PII-Scope.

Crucially, the framework aligns its evaluation metrics with established regulatory and security standards, creating a conceptual mapping between AI performance and legal obligations:
* **FINMA Guidance 08/2024**: Targeting model validation requirements for financial institutions.
* **nDSG (revised Federal Act on Data Protection)**: Addressing data protection and privacy compliance.
* **OWASP Top 10 for LLMs**: Identifying adversarial vulnerabilities and software security risks.

The research findings reveal a significant disparity between perceived and actual model performance. While models demonstrated high self-graded reliability (D7 scores ranging from 73-94%), their resistance to adversarial attacks (D8) was considerably lower, ranging from 20-61%. Notably, the study identified critical weaknesses in [[pii|PII]] (Personally Identifiable Information) extraction defenses, with protection levels remaining low (14-42%) across all tested frontier models. 

In terms of model-specific results, **Qwen 3.5 Plus** achieved the highest self-graded reliability score (94.4%), whereas **GPT-oss 120B** proved most resilient against adversarial security threats (60.7%), despite being the most cost-effective model in the study.