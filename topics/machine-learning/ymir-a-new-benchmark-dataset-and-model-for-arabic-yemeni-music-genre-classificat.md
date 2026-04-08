---
title: YMIR: A new Benchmark Dataset and Model for Arabic Yemeni Music Genre Classification Using Convolutional Neural Networks
created: 2024-05-23
source: https://arxiv.org/abs/2604.05011
tags: [Music Information Retrieval, Dataset, Convolutional Neural Networks, Yemen, Deep Learning]
category: [ai, machine-learning, technology]
---

# YMIR

The **Yemeni Music Information Retrieval (YMIR)** project introduces a specialized [[Benchmark Dataset]] designed to address the significant lack of representation for non-Western musical traditions within the field of [[Music Information Retrieval]] (MIR). Historically, most automated genre classification models have been optimized for Western musical structures, leaving culturally distinct traditions, such as those from the Arabian Peninsula, underrepresented in [[Artificial Intelligence]] research.

## The YMIR Dataset
The YMIR dataset comprises 1,475 carefully selected audio clips. The dataset is categorized into five distinct traditional Yemeni genres:
*   Sanaani
*   Hadhrami
*   Lahji
*   Tihami
*   Adeni

To ensure high-quality ground truth labels, the dataset underwent a rigorous annotation process performed by five Yemeni music experts. This structured protocol resulted in a strong inter-annotator agreement, evidenced by a Fleiss kappa score of 0.85.

## YMCM Architecture and Methodology
Alongside the dataset, the researchers proposed the **Yemeni Music Classification Model (YMCM)**. This system utilizes [[Convolutional Neural Networks]] ([[CNN]]) to perform classification based on time-frequency features extracted from the audio.

The study performed an exhaustive evaluation consisting of 30 separate experiments. The researchers compared various [[Feature Extraction]] techniques, including:
*   Mel-spectrograms
*   [[MFCC]] (Mel-frequency cepstral coefficients) at 13, 20, and 40 coefficients
*   Chroma features
*   FilterBank

The performance of YMCM was benchmarked against several standard [[Deep Learning]] architectures, including [[AlexNet]], [[VGG16]], and [[MobileNet]].

## Experimental Results
The findings revealed that YMCM is the most effective architecture for this specific task. The model achieved a peak accuracy of **98.8%** when utilizing Mel-spectrogram features. The research provides critical insights into the relationship between feature representation and model capacity, establishing YMIR as a foundational resource for ethnomusicology and [[Machine Learning]] applications in diverse cultural contexts.