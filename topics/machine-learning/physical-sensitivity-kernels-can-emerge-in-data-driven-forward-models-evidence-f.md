---
title: Physical Sensitivity Kernels Can Emerge in Data-Driven Forward Models: Evidence From Surface-Wave Dispersion
created: 2024-05-23
source: https://arxiv.org/abs/2604.04107
tags: [geophysics, neural networks, sensitivity kernels, surface-wave dispersion, surrogate modeling]
category: machine-learning
---

# Physical Sensitivity Kernels in Data-Driven Forward Models

This research addresses a fundamental question in the application of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] to [[geophysics]]: do neural network surrogate models merely learn a mathematical mapping of input-output data, or do they successfully recover the underlying [[physical-sensitivity-kernels-can-emerge-in-data-driven-forward-models-evidence-f|physical sensitivity kernels]]? 

## Overview

As [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|neural networks]] become increasingly integrated into geophysical workflows, they are often used as computationally efficient "surrogates" to replace expensive traditional forward models. However, the "black-box" nature of these models has historically raised concerns regarding their ability to represent the true physical gradients—the sensitivities that describe how changes in subsurface properties affect observable data.

## Methodology and Findings

The study utilizes [[surface-wave-dispersion|surface-wave dispersion]] as a primary testbed for this investigation. By leveraging [[automatic-differentiation|automatic differentiation]] within the neural network architecture, the researchers were able to extract gradients directly from the trained surrogate. When these learned gradients were compared against established theoretical sensitivity kernels, the results demonstrated that the neural-network models could recover the essential depth-dependent structures across a wide range of seismic periods.

This finding is significant because it proves that [[surrogate-models|surrogate models]] are capable of capturing physically meaningful differential information. This capability is vital for the advancement of [[gradient-based-optimization|gradient-based optimization]] and complex [[physics-informed-neural-networks-for-source-inversion-and-parameters-estimation-|inversion]] tasks.

## Limitations and Implications

Despite the success in recovering physical structures, the study identifies a critical caveat: the role of the [[training-distribution|training distribution]]. The researchers found that strong structural priors within the training data can introduce systematic artifacts into the inferred sensitivities. This suggests that while the model architecture is capable of learning physics, the reliability of the output is heavily contingent upon the diversity and quality of the training dataset.

In conclusion, the research provides a foundation for using [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|neural networks]] in [[uncertainty-analysis|uncertainty analysis]] and seismic imaging, provided that the conditions for [[physical-consistency|physical consistency]] are carefully managed during the training phase.