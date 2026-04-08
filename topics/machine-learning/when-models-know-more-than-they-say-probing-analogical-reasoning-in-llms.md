---
title: When Models Know More Than They Say: Probing Analogical Reasoning in LLMs
created: 2024-05-24
source: https://arxiv.org/abs/2604.03877
tags: [LLM, Analogical Reasoning, Model Probing, Prompt Engineering, Cognitive Science]
category: ai
---

# When Models Know More Than They Say: Probing Analogical Reasoning in LLMs

The research paper arXiv:2604.03877 investigates the discrepancy between the internal [[Neural Network]] representations and the observable output of [[Large Language Models]] (LLMs) during tasks involving **analogical reasoning**. Analogical reasoning is a fundamental component of [[Cognitive Science]] and is essential for deep narrative understanding and [[Machine Learning]]-driven pattern recognition.

### The Research Problem
While LLMs excel at identifying analogies where surface-level linguistic cues align with structural patterns, they struggle significantly when the analogy relies on latent information—details not explicitly stated in the text. This limitation highlights a potential deficiency in the model's ability to perform high-level [[abstraction]] and [[Generalization]].

### Probing vs. Prompting
The researchers utilized a dual-method approach to observe how models handle two specific types of analogies: **rhetorical** and **narrative**.

1.  **Prompting**: Assessing performance via standard text-based input/output (evaluating how the model communicates).
2.  **Probing**: Analyzing the internal [[vector representations]] within hidden layers (evaluating what the model "knows" internally).

### Key Findings
The study revealed a significant **asymmetry** between internal knowledge and external performance:

*   **Rhetorical Analogies**: In open-source models, probing significantly outperformed prompting. This indicates that the model's internal weights contain the necessary information to identify the analogy, but the model is unable to effectively retrieve or "surface" that information through text generation.
*   **Narrative Analogies**: Both prompting and probing yielded similarly low performance, suggesting a deeper-seated failure in modeling complex, non-obvious narrative structures.

### Conclusion and Implications
The findings suggest that the effectiveness of [[Prompt Engineering]] is highly task-dependent. The discrepancy implies that the limitations of modern [[Artificial Intelligence]] may not always reside in a lack of underlying knowledge, but rather in a failure of the prompting interface to access available latent information. This research has significant implications for the future of [[Cognitive Modeling]] and the development of more transparent [[Large Language Models]].