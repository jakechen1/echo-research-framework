---
title: YMIR: A new Benchmark Dataset and Model for Arabic Yemeni Music Genre Classification Using Convolutional Neural Networks
created: 2024-05-23
source: https://arxiv.org/abs/2604.05011
tags: [Music Information Retrieval, Dataset, Convolutional Neural Networks, Yemen, Deep Learning]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "YMIR: A new Benchmark Dataset and Model for Arabic Yemeni Music Genre Classification Using Convolutional Neural Networks"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/ymir-a-new-benchmark-dataset-and-model-for-arabic-yemeni-music-genre-classificat.md
dc.language: en
dc.rights: CC-BY-4.0
---

# YMIR

The **Yemeni Music Information Retrieval (YMIR)** project introduces a specialized [[ymir-a-new-benchmark-dataset-and-model-for-arabic-yemeni-music-genre-classificat|Benchmark Dataset]] designed to address the significant lack of representation for non-Western musical traditions within the field of [[Music Information Retrieval]] (MIR). Historically, most automated genre classification models have been optimized for Western musical structures, leaving culturally distinct traditions, such as those from the Arabian Peninsula, underrepresented in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] research.

## The YMIR Dataset
The YMIR dataset comprises 1,475 carefully selected audio clips. The dataset is categorized into five distinct traditional Yemeni genres:
*   Sanaani
*   Hadhrami
*   Lahji
*   Tihami
*   Adeni

To ensure high-quality ground truth labels, the dataset underwent a rigorous annotation process performed by five Yemeni music experts. This structured protocol resulted in a strong inter-annotator agreement, evidenced by a Fleiss kappa score of 0.85.

## YMCM Architecture and Methodology
Alongside the dataset, the researchers proposed the **Yemeni Music Classification Model (YMCM)**. This system utilizes [[lipkernel-lipschitz-bounded-convolutional-neural-networks-via-dissipative-layers|Convolutional Neural Networks]] ([[cnn-based-surface-temperature-forecasts-with-ensemble-numerical-weather-predicti|CNN]]) to perform classification based on time-frequency features extracted from the audio.

The study performed an exhaustive evaluation consisting of 30 separate experiments. The researchers compared various [[Feature Extraction]] techniques, including:
*   Mel-spectrograms
*   [[MFCC]] (Mel-frequency cepstral coefficients) at 13, 20, and 40 coefficients
*   Chroma features
*   FilterBank

The performance of YMCM was benchmarked against several standard [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] architectures, including [[AlexNet]], [[VGG16]], and [[MobileNet]].

## Experimental Results
The findings revealed that YMCM is the most effective architecture for this specific task. The model achieved a peak accuracy of **98.8%** when utilizing Mel-spectrogram features. The research provides critical insights into the relationship between feature representation and model capacity, establishing YMIR as a foundational resource for ethnomusicology and [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] applications in diverse cultural contexts.