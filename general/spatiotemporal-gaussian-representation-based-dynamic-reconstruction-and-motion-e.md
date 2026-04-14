---
title: Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)
created: 2024-05-22
source: https://arxiv.org/abs/2604.06482
tags: [MRI, 3D Gaussian Splatting, Machine Learning, Medical Imaging, Radiotherapy]
categories: [ai, technology, machine-learning]
author: wiki-pipeline
dc.title: "Spatiotemporal Gaussian representation-based dynamic reconstruction and motion estimation framework for time-resolved volumetric MR imaging (DREME-GSMR)"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/spatiotemporal-gaussian-representation-based-dynamic-reconstruction-and-motion-e.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DREME-GSMR

The **DREME-GSMR** framework is a specialized computational approach designed for the high-speed, time-resolved reconstruction of 3D [[bridging-mri-and-pet-physiology-untangling-complementarity-through-orthogonal-re|MRI]] volumes. Its primary objective is to resolve deformations caused by physiological motion, a critical requirement for the implementation of [[motion-adaptive radiotherapy]].

## Overview

Traditional volumetric imaging often struggles to capture rapid anatomical changes. DREME-GSMR addresses this by representing both patient anatomy and associated motion fields through [[3D Gaussians]]. This approach eliminates the need for pre-existing anatomical or motion models, allowing for a more flexible reconstruction process.

The framework operates by representing a reference MRI volume alongside a low-rank motion model. This model consists of motion-basis components that capture the essence of anatomical displacement over time.

## Technical Architecture

The core of the DREME-GSMR framework relies on an advanced [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] architecture:

*   **Motion Encoder**: A dual-path architecture utilizing both [[cnn-based-surface-temperature-forecasts-with-ensemble-numerical-weather-predicti|CNN]] (Convolutional Neural Network) and [[rpm-net-reciprocal-point-mlp-network-for-unknown-network-security-threat-detecti|MLP]] (Multi-Layer Perceptron) to estimate temporal motion coefficients.
*   **Signal Processing**: The encoder extracts motion parameters directly from raw signals derived from [[k-space]] data.
*   **Motion-Augmentation Strategy**: To improve robustness, the developers implemented a strategy to help the model generalize to "unseen" motion patterns, ensuring stability during live clinical applications.

## Performance and Clinical Utility

DREME-GSMR demonstrates significant computational efficiency, capable of achieving an inference time of approximately **10ms per volume** and a temporal resolution of roughly **400ms**. 

The framework was validated across several benchmarks:
*   **XCAT Digital Phantoms**: Showed high accuracy in tumor center-of-mass-error (COME) and SSIM.
*   **Clinical Datasets**: Tested on 20 patients, the framework achieved a mean liver COME of 0.96 mm during real-time imaging.

By enabling the inference of motion coefficients from new, online k-space data, DREME-GSMR facilitates real-time [[Motion Tracking]] and intra-treatment volumetric monitoring, potentially revolutionizing how clinicians manage organ movement during radiation therapy.