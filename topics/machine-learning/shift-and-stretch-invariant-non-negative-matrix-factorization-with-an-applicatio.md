---
title: Shift- and stretch-invariant non-negative matrix factorization with an application to brain tissue delineation in emission tomography data
created: 2024-05-22
source: https://arxiv.org/abs/2604.08161
tags: [non-negative matrix factorization, neuroimaging, signal processing, PyTorch, emission tomography]
category: machine-learning
---

# Shift- and Stretch-Invariant NMF

The research paper "Shift- and stretch-invariant non-negative matrix factorization with an application to brain tissue delineation in emission tomography data" (arXiv:2604.08161) introduces a novel computational framework designed to improve the analysis of dynamic [[neuroimaging]] data.

## The Problem: Temporal Distortion in Imaging

In applications involving [[emission tomography]], such as tracking radiotracer transport in blood or cerebrospinal fluid, the data often exhibits diffusion-like properties. These biological processes introduce complex temporal irregularities, including:

*   **Temporal Shifts:** Distance-dependent delays where signals arrive at different times.
*   **Stretching Effects:** Scale-differences in the temporal dimension of the signal.

Standard [[Non-negative matrix factorization]] (NMF) and other conventional linear modeling methods typically assume temporal alignment and scale consistency. Consequently, these traditional methods struggle to accurately decompose signals that have undergone significant diffusion-induced distortion, leading to imprecise [[brain tissue delineation]].

## The Proposed Solution

To address these challenges, the authors present a **shift- and stretch-invariant NMF** framework. The core innovation lies in performing the decomposition within the [[frequency domain]]. By operating in this domain, the model can elegantly handle distortions through specific mathematical transformations:

1.  **Shifts as Phase Modifications:** Temporal delays are modeled as modifications to the phase of the signal, allowing the model to account for both integer and non-integer shifts.
2.  **Stretching via Padding/Truncation:** Temporal stretching and compression are managed via zero-padding or truncation of the signal.

The model is implemented using [[PyTorch]], facilitating its use in modern [[machine-learning]] and [[deep learning]] workflows.

## Results and Applications

The effectiveness of the framework was demonstrated using both synthetic datasets and actual brain emission tomography data. The researchers proved that the shift- and stretch-invariant approach can successfully account for temporal distortions that would otherwise obscure structural details. By overcoming these artifacts, the model provides a significantly more detailed and accurate characterization of complex brain tissue structures, marking a significant advancement for high-precision [[neuroimaging]] analysis.