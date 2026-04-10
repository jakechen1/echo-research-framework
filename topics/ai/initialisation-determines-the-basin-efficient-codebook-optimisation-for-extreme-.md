---
title: "Initialisation Determines the Basin: Efficient Codebook Optimisation for Extreme LLM Quantization"
created: 2024-05-23
source: https://arxiv.org/abs/2604.08118
tags: [quantization, LLM, optimization, compression, deep learning]
category: ai
---

# Initialisation Determines the Basin

The paper **"Initialisation Determines the Basin"** investigates a critical failure mode in the [[Quantization]] of [[Large Language Models]] (LLMs), specifically when attempting extreme [[Compression]] at 2-bit precision. While additive quantization offers highly efficient $O(1)$ lookup-table dequantization—making it ideal for [[Edge Computing]]—the authors demonstrate that at extremely low bitrates, the process often fails catastrophously.

## The Problem: Poor Optimization Basins

The researchers identified that the primary bottleneck in extreme quantization is not the lack of refinement through [[Beam Search]] or [[Post-Training Quantization]] (PTQ), but rather the initial state of the codebook. Traditional **greedy sequential initialization** often places the model into "poor optimization regions." Once the model is trapped in these suboptimal basins, subsequent fine-tuning and optimization algorithms struggle to recover the lost accuracy.

The severity of this issue is tied to the **representational ratio** ($\rho = N/KM$), which characterizes the relationship between weight groups and the available codebook capacity. The paper notes that the bottleneck is moderate at 3 bits per parameter (bpp) but becomes extreme at 2 bpp, where poor initialization can degrade model perplexity by orders of magnitude.

## The Solution: OA-EM

To resolve this, the authors propose **OA-EM** (Output-aware EM initialization). This novel method utilizes a **Hessian-weighted Mahalanobis distance** to perform an output-aware initialization of the codebook. By accounting for the importance of weight updates relative to the model's output, OA-EM places the optimization process in a much more favorable region of the loss landscape.

## Experimental Results

The effectiveness of OA-EM was tested across several state-of-the-art architectures:
* [[Llama 3.1 (8B)]]
* [[Llama 3.2 (3B)]]
* [[Qwen 2.5 (3B)]]

Across all tested compression rates and search budgets, OA-EM consistently dominated the **quality-compute frontier**, providing superior solutions after PV-tuning. The findings highlight that in the highly constrained geometry of compressed [[Neural Network]] spaces, the importance of initialization can outweigh the benefits of extensive search or fine-tuning.