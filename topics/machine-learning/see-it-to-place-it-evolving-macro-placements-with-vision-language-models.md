---
title: "See it to Place it: Evolving Macro Placements with Vision-Language Models"
created: 2024-05-23
source: "https://arxiv.org/abs/2603.28733"
tags: [ai, machine-learning, EDA, chip-design]
category: ai
---

# See it to Place it: Evolving Macro Placements with Vision-Language Models

The research paper "See it to Place it" introduces a significant advancement in [[electronic-design-automation|Electronic Design Automation]] (EDA) through the integration of [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs) into the chip floorplanning process. Chip floorplanning is a notoriously complex optimization task involving the strategic arrangement of macros on a silicon canvas to minimize wirelength and optimize performance.

### The VeoPlace Framework

The authors propose a novel framework called **VeoPlace** (Visual Evolutionary Optimization Placement). The core premise of the research is that modern VLMs possess advanced spatial reasoning capabilities that closely mimic the intuitive visual logic used by human hardware designers. 

Unlike many recent trends in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] that require massive-scale fine-tuning, VeoPlace operates using a zero-shot approach. It utilizes the inherent strengths of existing VLMs to guide a base placer by proposing and constraining macro placements to specific subregions of the chip canvas. To