---
title: Three-dimensional inversion of gravity data using implicit neural representations and scientific machine learning
created: 2024-05-22
source: https://arxiv.org/abs/2510.17876
tags: [machine-learning, geophysics, neural-networks, sciML]
category: machine-learning
author: wiki-pipeline
dc.title: "Three-dimensional inversion of gravity data using implicit neural representations and scientific machine learning"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/three-dimensional-inversion-of-gravity-data-using-implicit-neural-representation.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Three-dimensional inversion of gravity data using implicit neural representations and scientific machine learning

## Overview
Gravity data inversion is a critical technique used to investigate subsurface density variations. These investigations are essential for a wide range of Earth science applications, including [[mineral exploration]], [[geothermal assessment]], [[carbon storage]], management of [[groundwater resources]], and the study of [[tectonic evolution]]. The research presented in arXiv:2510.17876 introduces a novel framework leveraging [[machine-learning|scientific machine learning]] (SciML) to revolutionize 3D gravity inversion.

## Methodology
The primary innovation of this approach is the implementation of [[implicit neural representations]] (INR). Traditional inversion methods often rely on predefined meshes or discretization, which can be computationally expensive and resolution-limited. This new method, however, treats subsurface density as a continuous field.

The framework utilizes a deep neural network trained directly through a physics-based forward-model loss. This allows the system to map spatial coordinates to a continuous density field without the constraints of a fixed grid. To address the issue of "spectral bias"—a common limitation in [[coordinate-based networks]] that tends to oversmooth sharp geological features—the researchers utilized spatial encoding. This enhancement allows the network to capture high-frequency, short-wavelength features and sharp density contrasts effectively.

## Results and Scalability
Through testing on synthetic models—ranging from smooth geological structures to complex dipping block models—the INR framework demonstrated an ability to reconstruct detailed structures and geologically plausible boundaries. Notably, the method achieves this without the need for explicit [[regularisation]] or manual depth weighting.

A significant advantage of this approach is its scalability. As the volume of the inversion problem increases, the number of inversion parameters does not scale linearly with the problem size, offering a more efficient alternative to traditional methods. This framework holds significant promise for the future of [[multiphysics inversion]], providing a scalable and interpretable foundation for integrating various geophysical datasets.

## See Also
* [[Physics-Informed Neural Networks (PINNs)]]
* [[Geophysical Inversion]]
* [[Neural Fields]]