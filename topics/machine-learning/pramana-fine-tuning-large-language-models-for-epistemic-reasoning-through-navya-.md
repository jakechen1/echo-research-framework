---
title: "Pramana: Fine-Tuning Large Language Models for Epistemic Reasoning through Navya-Nyaya"
created: 2024-05-22
source: https://arxiv.org/abs/2604.04937
tags: [AI, Machine Learning, Logic, Epistemology, LLM]
category: ai, machine-learning
---

# Pramana: Fine-Tuning Large Language Models for Epistemic Reasoning through Navya-Nyaya

While [[Large Language Models]] (LLMs) demonstrate remarkable linguistic fluency, they frequently struggle with [[Systematic Reasoning]], often generating "hallucinations" that appear confident but lack logical grounding. Research indicates that adding irrelevant context to mathematical problems can degrade LLM performance by as much as 65%, exposing a "brittle pattern-matching" mechanism beneath their apparent reasoning capabilities. This epistemic gap—the inability to ground claims in traceable evidence—poses a significant barrier to the deployment of AI in high-stakes domains.

## The Pramana Framework

To bridge this gap, the **Pramana** approach introduces a method for teaching LLMs explicit [[Epistemology]] by fine-tuning them on the principles of [[Navya-Nyaya]], a 2,500-year-old Indian framework of logic. Unlike standard [[Chain-of-Thought]] prompting, which relies on unstructured step-by-step generation, Pramana enforces a rigorous six-phase reasoning methodology:

1.  **Samshaya**: Detailed analysis of doubt.
2.  **Pramana**: Identification of valid evidence sources.
3.  **Pancha Avayava**: A five-member syllogism utilizing universal rules.
4.  **Tarka**: Implementation of counterfactual verification.
5.  **Hetvabhasa**: Systematic detection of logical fallacies.
6.  **Nirnaya**: The final ascertainment that distinguishes established knowledge from mere hypothesis.

## Implementation and Results

The researchers fine-tuned advanced architectures, including [[Llama 3.2-3B]] and [[DeepSeek-R1-Distill-Llama-8B]], using a specialized dataset of 55 Nyaya-structured logical problems, encompassing [[Boolean SAT]], constraint satisfaction, and multi-step deduction. 

The initial results are promising; Stage 1 fine-tuning achieved 100% semantic correctness on held-out evaluations. Interestingly, the models demonstrated the ability to internalize the core reasoning content even when they failed to strictly adhere to the required structural format. This suggests that the integration of classical logic provides a necessary "cognitive scaffolding" for more reliable [[Artificial Intelligence]].

All models, datasets, and training infrastructures associated with this research have been released on [[Hugging Face]] to support continued innovation in epistemic AI frameworks.