---
title: Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs
created: 2024-05-22
source: https://arxiv.org/abs/2604.06298
tags: [GRPO, SLM, Reinforcement Learning, Mathematical Reasoning, LoRA]
category: machine-learning
---

# Limits of Difficulty Scaling

The research paper **"Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs"** investigates the efficiency and limitations of using complex datasets during the alignment phase of [[Small Language Models (SLMs)]]. The study specifically focuses on whether increasing the difficulty of training samples during [[Reinforcement Learning]] leads to proportional gains in mathematical reasoning capabilities.

## Methodology
The researchers utilized [[GRPO]] (Group Relative Policy Optimization) combined with [[LoRA]] (Low-Rank Adaptation) to fine-tune models with parameters up to 3B. The experiments were conducted on two primary benchmarks for mathematical reasoning: [[GSM8K]] and [[MATH]]. The authors implemented a difficulty-stratified analysis to observe how the model's performance evolves as the complexity of the input prompts increases.

## Key Findings

* **The Capacity Boundary:** The study identifies a "capacity boundary" where accuracy plateaus as problem difficulty increases. The researchers conclude that [[GRPO]] primarily functions by reshaping output preferences (shifting probability mass toward correct reasoning paths) rather than fundamentally augmenting the model's ability to solve highly complex, unseen logic.
* **Diminishing Returns in Training:** A significant finding is that training on lower-difficulty problems alone can achieve performance parity with full-dataset training. By omitting the hardest tier of samples, the models reached comparable accuracy using only approximately 45% of the total training steps, suggesting that hard samples contribute significantly less to the learning signal in this regime.
* **Cross-Dataset Generalization:** The study observed an interesting generalization effect. Models trained on [[GSM8K]] actually outperformed those trained on [[MATH]] when tested on the numeric subsets of the [[MATH]] dataset (exceeding them by ~3-5% depending on model size).

## Conclusion
The success of [[alignment]] techniques in [[LLM]] training is heavily constrained by the base model's pre-existing [[reasoning competence]]. For resource-constrained environments, optimizing for simpler, high-signal data may be more efficient than attempting to scale via dataset complexity.