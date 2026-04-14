---
title: "Aces Who Tests The Tests Leave One Out Auc Consistency For Code Generation"
category: machine-learning
created: 2026-04-12
---

title: "ACES: Who Tests the Tests? Leave-One-Out AUC Consistency for Code Generation"
created: 2024-05-22
source: https://arxiv.org/abs/2604.03922
tags: [ai, machine-learning, code-generation, evaluation]
category: [ai, machine-learning, technology]

# ACES: Who Tests the Tests?

The **ACES** (AUC Consistency Scoring) framework is a specialized methodology designed to resolve the "circular dependency" problem inherent in the evaluation of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|large language models]] for [[compiled-ai-deterministic-code-generation-for-llm-based-workflow-automation|code generation]].

### The Problem: Circular Dependency
In modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] workflows, researchers increasingly use LLM-generated tests to evaluate LLM-generated code candidates. This introduces a significant reliability risk: if the generated tests are incorrect, they cannot be trusted to validate the code. Historically, determining whether a test is "correct" has been a major hurdle because verifying a test's accuracy typically requires knowing which code samples are already known to be correct, creating a logical loop where neither the code nor the test can be independently verified.

### The Solution: LOO