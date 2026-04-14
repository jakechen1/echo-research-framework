---
title: Steered LLM Activations are Non-Surjective
created: 2024-05-22
source: https://arxiv.org/abs/2604.09839
tags: [activation steering, interpretability, large language models, manifold hypothesis, surjectivity]
categories: [ai, machine-learning, technology]
---

# Steered LLM Activations are Non-Surjective

The research paper "Steered LLM Activations are Non-Surjective" investigates a fundamental mathematical gap between white-box interventions and black-box inputs within [[Large Language Models]]. 

### Overview of Activation Steering
[[Activation Steering]] is a prominent technique in [[Mechanistic Interpretability]] used to control model outputs by directly modifying internal activations. It has become a standard tool for research in [[AI Safety]], particularly in studying phenomena such as [[Jailbreaking]], truthfulness, and the translation of internal activations into human-readable explanations. While steering allows for precise control over a model's behavior, a critical question remains: can every manually steered activation state be replicated through a sequence of textual prompts?

### The Surjectivity Problem
The authors frame this inquiry as a problem of surjectivity. Specifically, they analyze whether the mapping from discrete prompts to a model's internal states is surjective—essentially asking if every "steered" state in the residual stream has a corresponding textual "pre-image" (an input prompt that produces that exact state).

The paper proves that, under practical assumptions, activation steering pushes the model's internal representations off the "manifold" of states that are reachable via discrete tokens. Consequently, the authors demonstrate that, almost surely, no prompt can reproduce the exact internal behavior induced by manual steering.

### Key Implications
The findings establish a formal separation between white-box steerability and black-box prompting. This discovery has significant implications for the field of [[AI Alignment]]:

1.  **Interpretability Caution:** Researchers are cautioned against interpreting the success of activation steering as evidence that those same behaviors are achievable via standard [[Prompt Engineering]].
2.  **Evaluation Discrepancies:** The study suggests that behaviors we can "steer" into a model might exist in a mathematical space that is inaccessible to human-readable text.
3.  **Methodological Reform:** The authors argue for the development of new evaluation protocols that explicitly decouple white-box interventions from black-box input-based assessments to prevent misleading conclusions regarding model [[Vulnerability]].

By showing that steered states are non-surjective, the paper highlights a fundamental disconnect between how we can manipulate the "brain" of an AI and how we can communicate with it via language.