---
title: MedDialBench: Benchmarking LLM Diagnostic Robustness under Parametric Adversarial Patient Behaviors
created: 2024-05-23
source: https://arxiv.org/abs/2604.06846
tags: [LLM, Benchmarking, Medical AI, Adversarial Robustness, Clinical NLP]
category: ai, machine-learning
---

# MedDialBench

**MedDialBench** is a specialized benchmarking framework designed to evaluate the diagnostic robustness of [[Large Language Models]] (LLMs) during interactive [[Medical Diagnosis]] simulations. The benchmark specifically addresses the challenge of "non-cooperative patients"—scenarios where the user (acting as a patient) provides inconsistent, incomplete, or false information.

## Overview

Existing benchmarks for [[Natural Language Processing]] in medicine often treat patient non-cooperation as a static or unweighted variable. MedDialBench introduces a controlled, "dose-response" methodology. It decomposes patient behavior into five distinct, graded dimensions, allowing researchers to observe how increasing the severity of a specific behavior impacts model accuracy:

*   **Logic Consistency**: The internal coherence of the patient's medical narrative.
*   **Health Cognition**: The accuracy of the patient's medical knowledge.
*   **Expression Style**: The linguistic complexity or difficulty of the patient's communication.
*   **Disclosure**: The degree of information withholding (Information Deficit).
*   **Attitude**: The interpersonal tone and level of cooperation.

## Key Research Findings

Through the evaluation of five frontier LLMs across 7,225 simulated dialogues, the study uncovered several critical vulnerabilities in current [[Artificial Intelligence]] models:

1.  **Pollution vs. Deficit**: The study identifies a fundamental asymmetry in error types. "Information pollution" (the fabrication of false symptoms) causes a 1.7x to 3.4x larger drop in diagnostic accuracy than "information deficit" (the withholding of true information). 
2.  **Super-additive Interactions**: The researchers found that certain combinations of behaviors trigger "super-additive" failures. Specifically, when fabrication is combined with other adversarial dimensions, models fail at a significantly higher rate than the mathematical sum of the individual dimensions would suggest.
3.  **The Failure of Inquiry**: While advanced questioning strategies can help a model recover information lost to "information deficit," these strategies are almost entirely ineffective against "information pollution." Once a model accepts a fabricated symptom as truth, standard inquiry cannot rectify the error.

## Significance

MedDialBench provides a critical tool for the [[Robustness Testing]] of [[Clinical Decision Support]] systems. As LLMs are integrated into healthcare workflows, the findings suggest that developers must prioritize defenses against misinformation and "hallucinated" patient inputs to ensure patient safety and diagnostic reliability.