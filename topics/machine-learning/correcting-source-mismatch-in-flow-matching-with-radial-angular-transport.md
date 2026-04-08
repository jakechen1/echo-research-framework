---
title: Correcting Source Mismatch in Flow Matching with Radial-Angular Transport
created: 2024-05-23
source: https://arxiv.org/abs/2604.04291
tags: [generative-models, flow-matching, probability-theory, machine-learning]
category: machine-learning
---

# Correcting Source Mismatch in Flow Matching with Radial-Angular Transport

The paper "Correcting Source Mismatch in Flow Matching with Radial-Angular Transport" addresses a fundamental limitation in modern [[Generative Modeling]]. Standard [[Flow Matching]] architectures are typically constructed using a [[Gaussian Distribution]] as the base source and Euclidean probability paths. While this approach is highly efficient, it introduces a structural "source mismatch" when attempting to model data that is inherently heavy-tailed or anisotropic.

## The Problem: Source Mismatch
In many real-world datasets, the radial distribution of the data does not align with the radial properties of a Gaussian source. This mismatch occurs at the level of the radial distribution, creating a discrepancy that standard Euclidean transport methods struggle to bridge efficiently. When the source distribution fails to reflect the underlying structure of the target data, the training process becomes unnecessarily complex.

## The Solution: RAFM
To resolve this, the authors introduce **Radial-Angular Flow Matching (RAFM)**. This framework explicitly corrects the source mismatch within the existing simulation-free Flow Matching template. 

The core mechanism of RAFM involves:
* **Radial Law Matching**: Utilizing a source whose radial law is designed to match that of the target data.
* **Angular Uniformity**: Implementing a conditional angular distribution that is uniform on a sphere.
* **Spherical Geodesic Interpolation**: Reducing the transport problem to an angular alignment task using paths defined on scaled spheres.

By matching the radial law by construction, the framework removes the Gaussian radial penalty, leaving only the task of angular alignment.

## Technical Contributions and Results
The authors provide a rigorous mathematical foundation for RAFM, establishing the exact density of the matched-radial source and proving a **radial-angular KL decomposition**. This decomposition is critical as it isolates the specific error penalty associated with Gaussian radial assumptions. Furthermore, the paper derives a stability result that links the error in [[Flow Matching]] directly to the error in the final generated samples.

Empirically, RAFM substantially outperforms standard Gaussian-based Flow Matching on heavy-tailed and extreme-event data. Notably, it achieves these improvements while remaining competitive with other non-Gaussian alternatives and maintaining the lightweight, deterministic training pipeline essential for scalable [[Artificial Intelligence]] applications.