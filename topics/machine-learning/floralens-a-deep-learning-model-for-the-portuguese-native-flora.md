---
title: "Floralens: a Deep Learning Model for the Portuguese Native Flora"
created: 2024-05-22
source: "https://arxiv.org/abs/2403.12072"
tags: [Deep Learning, Biodiversity, Portugal, AutoML, Citizen Science]
categories: [ai, machine-learning, biology, technology]
---

# Floralens: a Deep Learning Model for the Portuguese Native Flora

**Floralens** is a specialized [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] model designed for the automated identification of native plant species within the territory of Portugal. The project represents a significant bridge between [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] and [[citizen-science|Citizen Science]], providing a computational tool to assist in biodiversity monitoring and botanical classification.

### Dataset Construction
The efficacy of Floralens is rooted in its meticulously constructed dataset. The researchers anchored the training data in high-quality, verified botanical records provided by the [[sociedade-portuguesa-de-botnica|Sociedade Portuguesa de Botânica]]. To ensure broader coverage, the team augmented this primary source with additional research-grade samples extracted from [[gbif|GBIF]] (Global Biodiversity Information Facility). This dual-layered approach focuses on maximizing data fidelity, which is crucial for reducing error rates in species-level identification.

### Methodology and Architecture
A key finding of the research is that high-performance biological identification does not strictly require custom-built neural architectures. Instead, the study demonstrates that [[deep-convolutional-neural-networks|Deep Convolutional Neural Networks]] (CNNs) available through off-the-shelf cloud services can be highly effective. Specifically, the researchers utilized [[google-automl-vision|Google AutoML Vision]] to derive the Floralens model. The performance of this model was found to be comparable to [[plntnet|Pl@ntNet]], a globally recognized state-of-the-art platform for plant identification. This suggests that careful dataset engineering can compensate for the use of generic, automated [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] pipelines.

### Integration and Open Science
The Floralens model has been fully integrated into the public website of [[project-biolens|Project Biolens]], a centralized platform that hosts various taxonomic models for different biological groups. This integration supports large-scale ecological studies and community-driven science. In alignment with the principles of [[open-science|Open Science]], the dataset used to train the model is publicly available on [[zenodo|Zenodo]], allowing the global scientific community to reuse the data for further [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] research and ecological modeling.