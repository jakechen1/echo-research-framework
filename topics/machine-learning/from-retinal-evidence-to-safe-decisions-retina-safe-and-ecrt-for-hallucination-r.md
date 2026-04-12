---
title: "From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT for Hallucination Risk Triage in Medical LLMs"
created: 2024-05-22
source: https://arxiv.org/abs/2604.05348
tags: [medical-ai, hallucination-detection, diabetic-retinopathy, LLM-safety, machine-learning]
category: ai
---

# From Retinal Evidence to Safe Decisions: RETINA-SAFE and ECRT

The paper "From Retinal Evidence to Safe Decisions" addresses one of the most critical barriers to the clinical deployment of [[large-language-models-llms|Large Language Models (LLMs)]]: the phenomenon of [[blending-human-and-llm-expertise-to-detect-hallucinations-and-omissions-in-menta|hallucination]]. Specifically, the research focuses on the risks present when medical models encounter insufficient or conflicting clinical evidence during the assessment of [[diabetic-retinopathy|Diabetic Retinopathy]].

## The RETINA-SAFE Benchmark
To study these risks systematically, the authors introduced **RETINA-SAFE**, an evidence-grounded benchmark consisting of 12,522 samples. The dataset is uniquely structured around retinal grading records and is organized into three distinct evidence-relation tasks:

*   **E-Align**: Scenarios where the model's output is consistent with the provided evidence.
*   **E-Conflict**: Scenarios where the provided evidence contains contradictions.
*   **E-Gap**: Scenarios where the evidence provided is insufficient to make a definitive diagnosis.

## ECRT: A Two-Stage Detection Framework
The authors propose **ECRT (Evidence-Conditioned Risk Triage)**, a "white-box" detection framework designed to identify unsafe model outputs. Unlike "black-box" methods that only look at final text, ECRT analyzes internal [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] signals.

1.  **Stage 1 (Risk Triage)**: The framework performs a high-level classification to separate "Safe" outputs from "Unsafe" outputs.
2.  **Stage 2 (Subtype Attribution)**: For the "Unsafe" cases, the framework refines the error type, identifying whether the risk stems from a contradiction-driven error or an evidence-gap error.

ECRT operates by leveraging internal representations and [[logit-shifts|logit shifts]] observed when comparing context-dependent (CTX) to no-context (NOCTX) inputs.

## Results and Clinical Significance
The ECRT framework demonstrates superior performance compared to traditional [[scientific-graphics-program-synthesis-via-dual-self-consistency-reinforcement-le|self-consistency]] and [[uncertainty-based]] baselines. In Stage-1 triage, ECRT improved balanced accuracy by +0.15 to +0.19 over external uncertainty methods. These findings suggest that using internal model signals grounded in clinical evidence provides a robust, [[interpretable-ai|interpretable AI]] pathway for mitigating risks in [[before-humans-join-the-team-diagnosing-coordination-failures-in-healthcare-robot|healthcare]]-focused [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]].