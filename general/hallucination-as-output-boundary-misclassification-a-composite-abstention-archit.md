---
title: "Hallucination as output-boundary misclassification: a composite abstention architecture for language models"
created: 2024-05-22
source: https://arxiv.org/abs/2604.06195
tags: [hallucination, LLM, machine-learning, uncertainty-quantification, abstain-mechanism]
category: ai
author: wiki-pipeline
dc.title: "Hallucination as output-boundary misclassification: a composite abstention architecture for language models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/hallucination-as-output-boundary-misclassification-a-composite-abstention-archit.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Hallucination as output-boundary misclassification

The research paper "Hallucination as output-boundary misclassification" proposes a novel framework for mitigating [[blending-human-and-llm-expertise-to-detect-hallucinations-and-omissions-in-menta|hallucinations]] in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). Rather than treating hallucinations as stochastic errors, the authors frame them as a specific type of "output-boundary misclassification." In this view, the model erroneously treats internally generated, ungrounded completions as if they were statistically supported by training evidence.

## The Composite Architecture

To address this boundary error, the authors introduce a **composite abstention architecture** designed to intercept errors before they reach the user. The system integrates two complementary layers:

1.  **Instruction-based Refusal:** This layer uses high-level prompting to instruct the model to decline answering when it lacks sufficient confidence.
2.  **Structural Abstention Gate:** A mathematical layer that evaluates the reliability of the output via a "support deficit score" ($S_t$).

The structural gate does not require access to the model's internal weights, instead relying on three "black-box" signals:
*   **Self-consistency ($A_t$):** Measuring the variance in outputs across multiple sampling iterations.
*   **Paraphrase Stability ($P_t$):** Assessing how sensitive the response is to changes in the input phrasing.
*   **Citation Coverage ($C_t$):** Evaluating the density and strength of supporting evidence or references.

## Evaluation and Findings

The study evaluated the architecture across several models, including [[GPT-3.5-turbo]], under various epistemic regimes. The findings revealed that single-layer interventions are insufficient:
*   **Instruction-only prompting** successfully reduced hallucinations but introduced high "over-abstention," where the model refused to answer perfectly valid questions.
*   **The structural gate** preserved accuracy on answerable items but failed to detect "confident confabulations" in scenarios involving conflicting evidence.

The **composite architecture** successfully bridged these gaps, achieving high overall accuracy and low hallucination rates. This suggests that effective