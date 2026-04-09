---
title: ODE-free Neural Flow Matching for One-Step Generative Modeling
created: 2024-05-22
source: https://arxiv.org/abs/2604.06413
tags: [generative-models, optimal-transport, neural-networks, computer-vision]
category: machine-learning
---

# ODE-free Neural Flow Matching for One-Step Generative Modeling

The paper **"ODE-free Neural Flow Matching for One-Step Generative Modeling"** introduces a novel approach to accelerating the inference process in [[Generative AI]]. Traditionally, state-of-the-art frameworks such as [[Diffusion Models]] and [[Flow Matching]] operate by learning time-dependent vector fields. To generate a sample, these models require the integration of an [[Ordinary Differential Equation]] (ODE), a process that often necessitates dozens or even hundreds of sequential network evaluations, leading to significant computational latency.

### The OT-NFM Framework

To overcome the bottleneck of iterative sampling, the authors propose **Optimal Transport Neural Flow Matching (OT-NFM)**. This is an ODE-free generative framework designed to parameterize the transport map directly via neural flows. By bypassing the need for step-by-step integration, OT-NFM enables **true one-step generation**, allowing the model to produce high-quality samples with a single forward pass through the [[Neural Network]].

### Addressing Mean Collapse

A primary challenge in direct map learning is the phenomenon known as **mean collapse**. The researchers demonstrate that in naive flow-map training, inconsistent pairings between the input noise and the target data distribution drive the model's predictions toward the global mean of the dataset, resulting in a loss of sample diversity. The authors mathematically prove that **consistent coupling** is a fundamental requirement for non-degenerate learning.

To mitigate this, the paper utilizes [[Optimal Transport]] (OT) pairings. By employing scalable minibatch and online coupling strategies, the framework ensures that the mapping from noise to data remains mathematically coherent and efficient.

### Experimental Results

The efficacy of OT-NFM was evaluated on standard computer vision benchmarks, including [[MNIST]] and [[CIFAR-10]]. The results indicate that the model achieves sample quality competitive with traditional multi-step methods while drastically reducing the computational cost of inference. This advancement holds significant implications for the deployment of large-scale generative models on resource-constrained hardware.