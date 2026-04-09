---
title: Bridging MRI and PET physiology: Untangling complementarity through orthogonal representations
created: 2023-10-27
source: https://arxiv.org/abs/2604.07154
tags: [multimodal imaging, machine learning, prostate cancer, medical imaging, subspace decomposition]
category: machine-learning
---

# Bridging MRI and PET physiology

The research paper "Bridging MRI and PET physiology: Untangling complementarity through orthogonal representations" addresses a fundamental challenge in [[Multimodal Imaging]]: the difficulty in distinguishing shared information from information unique to a specific modality. While traditional fusion methods often attempt to translate one modality into another, this study proposes a framework centered on [[Subspace Decomposition]].

### Methodology
The authors introduce a method to decompose [[PSMA PET]] uptake into two distinct components: an "MRI-explainable" physiological envelope and an orthogonal residual. This residual represents signal components that are mathematically irrecoverable from the [[MRI]] feature manifold. 

To achieve this, the researchers utilized an [[Implicit Neural Representation]] (INR) composed of non-spatial, intensity-based features derived from multiparametric MRI. To ensure the mathematical separation of these signals, they implemented a projection-based regularization technique using [[Singular Value Decomposition]] (SVD). This technique penalizes any residual components that fall within the span of the MRI-derived features, effectively enforcing [[Orthogonality]] between structural, diffusion, and perfusion data and intracellular protein expression.

### Key Findings
Tested on a cohort of 13 [[Prostate Cancer]] patients, the model demonstrated that the orthogonal residual—the signal purely belonging to the PET modality—is significantly larger in tumor regions. This finding provides empirical evidence that [[PET Imaging]] captures critical physiological data, such as specific cellular activity, that cannot be reconstructed through [[Medical Imaging]] techniques like [[Diffusion-Weighted Imaging]] or perfusion MRI alone.

### Significance
By framing modality complementarity through the lens of [[Representation Geometry]] rather than simple image translation, this work offers a structured approach to understanding the synergistic value of [[Hybrid Imaging]]. This framework has significant implications for optimizing [[Clinical Workflow]] and developing more rational [[Radiology]] acquisition strategies by delineating the irreducible contribution of each imaging modality.