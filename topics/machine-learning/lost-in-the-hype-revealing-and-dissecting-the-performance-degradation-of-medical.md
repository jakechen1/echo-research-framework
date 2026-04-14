---
title: "Lost in the Hype: Revealing and Dissecting the Performance Degradation of Medical Multimodal Large Language Models in Image Classification"
created: 2024-05-23
source: https://arxiv.org/abs/2604.08333
tags: [medical imaging, MLLM, feature probing, deep learning, performance analysis, computer vision]
category: ai, machine-learning
---

# Lost in the Hype: Revealing and Dissecting the Performance Degradation of Medical Multimodal Large Language Models in Image Classification

The research paper "Lost in the Hype" addresses a critical paradox within the field of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]. It investigates why [[multimodal-large-language-models-mllms|Multimodal Large Language Models (MLLMs)]]—despite their massive parameter counts and extensive pre-training data—consistently underperform compared to traditional [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models when applied to the fundamental task of [[medical-image-classification|Medical Image Classification]].

### Methodology
To investigate the origins of this performance gap, the authors conducted an exhaustive study of 14 open-source medical MLLMs across three representative datasets. Rather than performing mere superficial benchmarking, the study employs [[feature-probing|Feature Probing]] to meticulously track the flow of visual information. By analyzing the model pipeline layer-by-layer, the researchers are able to visualize exactly where