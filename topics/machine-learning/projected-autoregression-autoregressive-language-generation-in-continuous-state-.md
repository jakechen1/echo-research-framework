---
title: Projected Autoregression: Autoregressive Language Generation in Continuous State Space
created: 2024-05-22
source: https://arxiv.org/abs/2601.04854
tags: [machine-learning, autoregressive-models, generative-ai, neural-networks]
category: machine-learning
---

# Projected Autoregression: Autoregressive Language Generation in Continuous State Space

Traditional [[privacy-attacks-on-image-autoregressive-models|Autoregressive Models]] rely on a process of repeated, discrete token selection. In these standard frameworks, every step of the generation process involves an irreversible commitment to a specific token, which can limit the flexibility of the generative process. The paper **"Projected Autoregression"** proposes a fundamental shift away from this paradigm.

## Overview of Projected Autoregression

Instead of selecting discrete tokens at every timestep, **Projected Autoregression** utilizes continuous prediction within the [[geometric-organization-of-cognitive-states-in-transformer-embedding-spaces|Embedding Space]]. The model predicts next-token vectors through a combination of regression and contrastive objectives. In this architecture, discrete tokens are not the primary driver of the generation; instead, they emerge only during the "commitment" phase via a nearest-neighbor projection.

This method introduces an optional "liquid tail"—a mutable suffix that allows the model to perform iterative refinement of the continuous state before finalizing a discrete token. Unlike the global denoising seen in [[diffhdr-re-exposing-ldr-videos-with-video-diffusion-models|Diffusion Models]], this refinement is localized to a short causal suffix, maintaining the efficiency of a left-to-right causal process.

## Key Innovations and Implications

The shift from discrete selection to continuous-state prediction results in two significant breakthroughs:

1.  **A Distinct Generation Regime:** Even in configurations where projection is immediate (where $K=1$), the continuous prediction method produces text structures and dynamics that differ fundamentally from traditional token-space [[autoregressive-interfaces|Autoregressive Interfaces]]. This suggests that the underlying dynamics of language generation can be fundamentally altered by changing the mathematical interface of prediction.
2.  **A Continuous Control Surface:** The authors reveal that continuous prediction exposes a "control surface" within the generative process. Developers can directly manipulate parameters such as direction rate, history noise, and embedding geometry on the evolving state before any discrete token is ever committed.

## Conclusion

By demonstrating that token selection is merely one subset of a much larger family of possible autoregressive interfaces, this research positions [[continuous-state-space|Continuous State Space]] as a vital new design space for the future of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] and [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]].