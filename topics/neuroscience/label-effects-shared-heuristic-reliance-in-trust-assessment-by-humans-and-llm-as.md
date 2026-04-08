---
title: Label Effects: Shared Heuristic Reliance in Trust Assessment by Humans and LLM-as-a-Judge
created: 2024-05-22
source: https://arxiv.org/abs/2604.05593
tags: [AI Evaluation, Cognitive Bias, LLM, Heuristics, LLM-as-a-Judge]
category: [ai, machine-learning, neuroscience]
---

# Label Effects: Shared Heuristic Reliance in Trust Assessment by Humans and LLM-as-a-Judge

The research paper "Label Effects: Shared Heuristic Reliance in Trust Assessment by Humans and LLM-as-a-Judge" investigates a critical vulnerability in the growing practice of using [[Large Language Models]] as automated evaluators, a paradigm known as [[LLM-as-a-Judge]]. The study demonstrates that both humans and AI judges are subject to significant biases based on the disclosed source labels of the content being evaluated.

## Methodology and Findings

Using a counterfactual design, the researchers presented identical content to both human and LLM participants, varying only the metadata label (e.g., "Human-authored" vs. "AI-generated"). The results revealed a consistent pattern of trust asymmetry: both cohorts assigned higher trust levels to information labeled as human-authored, regardless of the actual semantic quality of the text.

### Human Behavior
Through [[Eye-tracking]] analysis, the study found that humans rely heavily on source labels as **heuristic cues**. Instead of deep semantic processing of the content, human gaze patterns indicate a significant focus on the labels themselves when forming trust judgments, demonstrating a reliance on superficial markers over substantive analysis.

### LLM Internal States
The researchers analyzed the internal mechanics of [[Neural Networks]] to determine if LLMs mirrored this human behavior. They discovered:
* **Attention Dominance:** LLMs allocate denser [[Attention Mechanism]] weights to the label region than to the content region.
* **Label Sensitivity:** This dominance is even more pronounced under "Human" labels compared to "AI" labels, mirroring recorded human gaze patterns.
* **Logit Uncertainty:** Decision uncertainty, measured via [[