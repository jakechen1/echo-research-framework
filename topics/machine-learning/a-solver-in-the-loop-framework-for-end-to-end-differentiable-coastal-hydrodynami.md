---
title: A solver-in-the-loop framework for end-to-end differentiable coastal hydrodynamics
created: 2023-10-27
source: https://arxiv.org/abs/2604.07129
tags: [AegirJAX, differentiable_physics, SciML, hydrodynamics, coastal_engineering]
category: machine-learning
---

# A solver-in-the-loop framework for end-to-end differentiable coastal hydrodynamics

## Overview
The paper introduces **AegirJAX**, a novel [[scientific-machine-learning|Scientific Machine Learning]] framework designed to bridge the gap between traditional [[hydrodynamics|Hydrodynamics]] simulations and modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] optimization. Numerical simulations of wave propagation and run-up are vital for [[coastal-engineering|Coastal Engineering]] and tsunami hazard assessment. However, using these models for inverse problems—such as estimating bathymetry—is historically difficult due to the high computational cost of deriving discrete adjoints.

## Technical Approach
AegirJAX implements a solver based on the depth-integrated, non-hydrostatic [[shallow-water-equations|Shallow-Water Equations]]. The core innovation lies in its implementation within a reverse-mode [[automatic-differentiation|Automatic Differentiation]] framework. By doing so, the framework treats the entire physics-based time-marching loop as a continuous computational graph. This allows gradients to propagate through the physics engine, enabling a "solver-in-the-loop" architecture that facilitates end-to-end differentiable modeling.

## Key Applications
The researchers demonstrate the framework's versatility across four critical scientific tasks:

1.  **Neural Model Correction**: Using [[Neural