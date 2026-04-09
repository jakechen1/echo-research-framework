---
title: "FedSpy-LLM: Towards Scalable and Generalizable Data Reconstruction Attacks from Gradients on LLMs"
created: 2024-05-22
source: https://arxiv.org/abs/2604.06297
tags: [Federated Learning, LLM, Privacy, Data Reconstruction, PEFT]
category: machine-learning
---

# FedSpy-LLM

FedSpy-LLM is a research framework designed to demonstrate the vulnerabilities inherent in [[Federated Learning]] (FL) when applied to [[Large Language Models]] (LLMs). As training workflows increasingly rely on [[Parameter-Efficient Fine-Tuning]] (PEFT) to manage the enormous scale of modern models, the security of shared gradients becomes a primary concern for [[AI Privacy]].

### The Problem: Limitations of Previous Attacks
While it has been established that private data can be extracted from shared gradients, traditional [[Data Reconstruction Attacks]] face significant hurdles in modern distributed environments. Prior research was largely constrained by:
* **Scale:** Previous methods struggled to reconstruct datasets with large batch sizes or long input sequences.
* **Architectural Constraints:** Most existing attacks were specialized for either encoder-only or decoder-only architectures.
* **PEFT Interference:** The use of [[Parameter-Efficient Fine-Tuning]] introduces a substantial "null space" in gradients, which significantly degrades the quality of reconstruction attempts.

### The FedSpy-LLM Innovation
FedSpy-LLM introduces a scalable and generalizable attack vector capable of overcoming these barriers. The framework utilizes two core technical advancements:

1. **Gradient Decomposition Strategy:** By exploiting the rank deficiency and specific subspace structure found in gradients, FedSpy-LLM can efficiently extract tokens while preserving the essential signal components necessary for reconstruction. This allows the attack to scale effectively across larger datasets.
2. **Iterative Alignment:** To combat the loss of sequence integrity, the approach iteratively aligns the gradients of partial sequences with the full-sequence gradient. This ensures that the reconstructed text maintains the correct order of tokens.

### Implications for [[Machine Learning Security]]
The results of the FedSpy-LLM study suggest that current privacy-preserving assumptions in [[Federated Learning]] may be insufficient. Because the attack remains robust across encoder, decoder, and encoder-decoder architectures—even when utilizing PEFT—it identifies a critical need for more advanced [[Differential Privacy]] or robust gradient-masking techniques to protect sensitive training data in decentralized [[Artificial Intelligence]] ecosystems.