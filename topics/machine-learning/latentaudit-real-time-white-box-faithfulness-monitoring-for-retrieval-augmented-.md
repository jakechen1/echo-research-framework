---
title: "LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retrieval-Augmented Generation with Verifiable Deployment"
created: 2024-05-22
source: https://arxiv.org/abs/2604.05358
tags: [RAG, Hallucination, Machine Learning, Verifiable Computing, LLM]
category: ai
---

# LatentAudit

**LatentAudit** is a novel white-box auditing framework designed to enhance the reliability of [[Retrieval-Augmented Generation]] (RAG) systems. While RAG is widely used to mitigate [[Hallucination]], the technology does not inherently guarantee that a model's output is strictly grounded in the retrieved context. LatentAudit addresses this by providing a real-time mechanism to monitor the faithfulness of an LLM's response during the inference process.

## Methodology

Unlike traditional auditing methods that rely on an auxiliary [[Large Language Model]] (LLM) to act as a "judge," LatentAudit utilizes the internal geometry of the generator itself. The system functions as a white-box auditor by pooling mid-to-late [[Residual Stream]] activations from open-weight models. It calculates the [[Mahalanobis Distance]] between these internal activations and the representation of the retrieved evidence.

The resulting quadratic rule is computationally efficient and requires no additional model parameters. This allows the monitor to run concurrently with the generation process with minimal latency. The framework is simple enough to be calibrated using small, held-out datasets, making it accessible for various deployment scales.

## Performance and Robustness

Experimental results demonstrate that residual-stream geometry contains a highly usable signal for faithfulness. On the [[PubMedQA]] benchmark using [[Llama-3-8B]], LatentAudit achieved an AUROC of 0.942 with a negligible overhead of only 0.77ms. The system proves highly stable across diverse model families, including [[Llama-2]], [[Qwen-2.5]], and [[Mistral]].

Under rigorous stress tests—which include retrieval misses, contradictory evidence, and partial-support noise—the monitor maintained high precision, reaching an AUROC of up to 0.9815 on PubMedQA and 0.9315 on [[HotpotQA]].

## Verifiable Deployment

A key innovation of LatentAudit is its compatibility with [[Verifiable Computing]]. By utilizing 16-bit fixed-point precision, the audit rule preserves 99.8% of the original FP16 AUROC. This precision level enables the implementation of [[Groth16]]-based proofs, allowing for public verification of the model's faithfulness. This feature is critical for secure deployments where users must verify that a model is adhering to its retrieved context without requiring access to the proprietary model weights or sensitive activations.