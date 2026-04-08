---
title: RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models
created: 2024-05-24
source: https://arxiv.org/abs/2602.04448
tags: [ai-safety, moe, machine-learning, alignment, largelanguagemodels]
category: ai, machine-learning
---

# RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models

The paper "RASA: Routing-Aware Safety Alignment for Mixture-of-Experts Models" introduces a specialized framework designed to address the unique vulnerabilities present in [[Mixture-of-Experts (MoE)]] architectures during the [[Safety Alignment]] process.

## The Challenge of MoE Safety
Standard [[Large Language Models (LLMs)]] typically undergo full-parameter fine-tuning to mitigate [[Jailbreaking Attacks]]. However, in [[Mixture-of-Experts (MoE)]] models, the sparse routing mechanism introduces a unique failure mode known as "degenerate optimization." 

The researchers observed that naive fine-tuning often leads to "routing-based bypasses" or "expert dominance effects." Rather than actually repairing the specific "Safety-Critical Experts" responsible for processing harmful prompts, the model learns to manipulate the router to avoid certain weights or reroute traffic. This results in a superficial layer of safety that is easily circumvented by sophisticated adversarial prompts.

## The RASA Framework
To combat this, the authors propose **RASA** (Routing-Aware Safety Alignment). Unlike traditional global updates, RASA operates through a targeted, expert-level approach:

1. **Identification**: The framework identifies specific experts that are disproportionately activated during successful jailbreak attempts.
2. **Selective Fine-tuning**: RASA performs fine-tuning only on these identified Safety-Critical Experts while keeping the routing mechanism fixed. This prevents the model from learning to "bypass" the problem through routing manipulation.
3. **Routing Consistency**: The framework subsequently enforces routing consistency, ensuring that the model maintains safe behavior even when provided with safety-aligned contexts.

## Results and Impact
Experimental results across diverse MoE architectures demonstrate that RASA achieves near-perfect robustness against various [[Jailbreaking Attacks]] and shows strong cross-attack generalization. Notably, RASA significantly reduces the issue of [[Over-refusal]]—a common side effect of safety training where models refuse harmless queries—while maintaining high performance on core reasoning and knowledge benchmarks such as [[MMLU]], [[GSM8K]], and [[TruthfulQA]].

By focusing on targeted expert repair rather than global parameter shifts, RASA provides a more efficient and architecture-preserving method for securing the next generation of sparse [[Machine Learning]] models.