---
title: FLeX: Fourier-based Low-rank EXpansion for multilingual transfer
created: 2024-05-22
source: https://arxiv.org/abs/2604.06253
tags: [machine-learning, code-generation, LLM, cross-lingual-transfer]
category: machine-learning
---

# FLeX: Fourier-based Low-rank EXpansion

**FLeX** (Fourier-based Low-rank EXpansion) is a research framework designed to optimize cross-lingual code generation within [[Large Language Models]] (LLMs). As software engineering environments increasingly require the maintenance of diverse codebases, the ability to transfer logical structures from a source language—such as Python—to a target language—such as Java—is vital. However, the traditional approach of performing full-parameter fine-tuning for every supported programming language is computationally expensive and resource-intensive.

## Methodology

The FLeX study investigates how [[Parameter-Efficient Fine-Tuning]] (PEFT) techniques and specialized optimizers can facilitate efficient cross-lingual transfer. The researchers utilized [[LoRA]] (Low-Rank Adaptation) on the [[Code Llama 7B]] model to optimize only a small subset of parameters. 

The research specifically compared the efficacy of two optimization algorithms:
* **[[Adam]]**: A widely used adaptive learning rate optimizer.
* **[[Sophia]]**: An optimizer designed for faster convergence in large-scale models.

In addition to parameter optimization, the paper introduces a novel **Fourier-based regularization** technique. This method applies regularization within the frequency domain during the fine-tuning process to better capture the underlying structural patterns of code across different syntaxes.

## Key Findings

The experimental results yielded three primary conclusions:

1. **Efficiency of LoRA**: Fine-tuning using [[LoRA]] on a small, high-quality dataset (MBPP) can outperform much larger, broadly fine-tuned models. Specifically, the FLeX approach achieved a pass@1 of 40.1%, exceeding the 38.4% score of the standard Code Llama-Python-7B model.
2. **Optimizer Convergence**: While the [[Sophia]] optimizer demonstrated faster convergence rates than [[Adam]], the final