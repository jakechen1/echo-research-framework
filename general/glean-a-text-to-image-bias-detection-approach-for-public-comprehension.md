---
title: GLEaN: A Text-to-image Bias Detection Approach for Public Comprehension
created: 2024-05-22
source: https://arxiv.org/abs/2604.09923
tags: [AI Ethics, Computer Vision, Bias Detection, Explainable AI]
category: ai
---

# GLEaN: A Text-to-image Bias Detection Approach for Public Comprehension

**GLEaN** (Generative Likeness Evaluation at N-Scale) is an automated, portrait-based [[Explainable AI]] (XAI) pipeline designed to bridge the gap between technical bias auditing and [[Public Comprehension]]. While current methods for measuring bias in [[Text-to-image (T2I) models]] are highly effective for researchers, they often rely on complex statistical metrics that are inaccessible to non-experts. GLEaN addresses this by transforming abstract data into intuitive, visual representations.

## Methodology

The GLEaN framework utilizes a three-stage process to distill the inherent biases of a generative model into a single, representative "central tendency" portrait:

1.  **Large-scale Generation**: The system automatically generates a massive corpus of images based on specific identity-based prompts (e.g., various occupations or social identities).
2.  **Filtering and Alignment**: Using facial landmark detection, the pipeline filters the results and performs spatial alignment to ensure consistent facial positioning across the dataset.
3.  **Median-pixel Composition**: Through a median-pixel aggregation technique, the framework compresses the entire dataset into a single composite image. This image serves as a visual "average" of what the model perceives for a given prompt.

## Key Findings

Researchers demonstrated the efficacy of GLEaN using [[Stable Diffusion XL]] across 40 different social and occupational prompts. The tool successfully surfaced documented biases and identified new correlations, such as unexpected associations between skin tone and predicted facial emotions. 

In a large-scale user study (N = 291), participants found that GLEaN portraits communicated model biases as effectively as traditional data tables, but with significantly reduced cognitive load and viewing time.

## Advantages

*   **Model-Agnostic**: Because the methodology relies exclusively on model outputs, it can be applied to [[Black-box systems]] and [[Closed-weight models]] without requiring access to the underlying architecture or training data.
*   **Scalability**: The pipeline is designed for high-throughput processing, allowing for rapid auditing of emerging [[Generative AI]] technologies.
*   **Accessibility**: By replacing spreadsheets with portraits, GLEaN makes the socioeconomic implications of [[Machine Learning]] bias visible to the general public.