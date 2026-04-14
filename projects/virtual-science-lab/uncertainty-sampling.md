---
title: "Uncertainty Sampling"
created: 2026-04-12
category: machine-learning
tags: [active learning, query strategy, information theory, machine learning]
source_urls:
  - "https://pubmed.ncbi.nlm.nih.gov/35138957/"
  - "https://pubmed.ncbi.nlm.nih.gov/37348366/"
  - "https://pubmed.ncbi.nlm.nih.gov/31099917/"
author: wiki-dashboard
dc.title: "Uncertainty Sampling"
dc.creator: wiki-dashboard
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: projects/virtual-science-lab/uncertainty-sampling.md
dc.language: en
dc.rights: CC-BY-4.0
---

**Uncertainty Sampling** is a fundamental query strategy used within the framework of [[Active Learning]] to improve the efficiency of model training. The primary objective of uncertainty sampling is to identify and label the most "informative" instances within an [[unlabeled dataset]], thereby maximizing the predictive performance of a [[machine-learning|machine learning model]] while minimizing the total number of required human-annotated labels. By focusing on data points where the current model exhibits low confidence or high ambiguity, the algorithm avoids the redundant acquisition of easy-to-classify samples, significantly reducing the computational and financial costs associated with data annotation. This concept is closely associated with the methodologies discussed in [[Freeman S et al., 2014]], particularly regarding how specific data selection criteria can drive feature importance and model refinement.

## Core Mechanism

In a standard supervised learning setup, a model is trained on a fixed, pre-labeled dataset. In contrast, uncertainty sampling operates within an iterative [[Active Learning]] loop. The process typically follows these steps:

1.  **Initial Training:** A model is trained on a small, initially labeled set of data ($L$).
2.  **Probability Estimation:** The model is applied to a large pool of unlabeled data ($U$), and for each instance, the model predicts the class probabilities.
3.  **Query Function Application:** A specific [[Uncertainty Sampling]] metric (the "query function") is applied to evaluate the "uncertainty" of each instance in $U$.
4.  **Selection and Labeling:** The instances with the highest uncertainty scores are selected and passed to an "oracle" (typically a human annotator) for labeling.
5.  **Model Update:** The newly labeled instances are added to $L$, and the model is retrained.

The effectiveness of this process relies entirely on the mathematical definition of "uncertainty." While several metrics exist, they generally fall into three distinct categories.

## Primary Query Strategies

### 1. Least Confidence
The Least Confidence strategy is the simplest form of uncertainty sampling. The algorithm identifies the instance $x$ for which the probability of the most likely predicted class is the lowest. Mathematically, if $y^*$ is the class with the highest predicted probability, the strategy selects $x$ that minimizes:

$$P(y^* | x; \theta)$$

where $\mathcal{\theta}$ represents the model parameters. This method targets instances where the model lacks a strong "winner" among its predictions, effectively pushing the decision boundary toward more ambiguous regions of the feature space.

### 2. Margin Sampling
Margin Sampling seeks to identify instances that are "ambiguous" between the two most likely classes. This is particularly useful in multi-class classification tasks where the model might be confident about a primary class but unable to distinguish it from a secondary runner-up. The margin is calculated as the difference between the probabilities of the highest and second-highest predicted classes:

$$\text{Margin}(x) = P(y_1 | x; \theta) - P(y_2 | x; \theta)$$

The algorithm selects the instance $x$ with the smallest margin. By minimizing this gap, the strategy focuses on instances residing near the [[decision boundary]], ensuring that the model learns to differentiate between closely related classes.

### 3. Entropy-Based Sampling
Entropy-based sampling utilizes information theory to quantify the total "chaos" or lack of information in a prediction. Unlike Least Confidence or Margin Sampling, which only consider the top one or two classes, Entropy considers the entire probability distribution across all possible labels. The Shannon Entropy $H(x)$ is calculated as:

$$H(x) = -\sum_{i=1}^{C} P(y_i | x; \theta) \log P(y_i | x; \theta)$$

where $C$ is the total number of classes. An instance with high entropy is one where the probability mass is spread across many classes, indicating maximum confusion. This is often considered the most robust method for complex, high-dimensional classification tasks, as it captures the global uncertainty of the model's state.

## The Distinction Between Sampling and Method Uncertainty

While [[Uncertainty Sampling]] in [[machine learning]] focuses on the uncertainty of a model's inference regarding an unknown label, the concept of "uncertainty" in scientific measurement encompasses a broader range of-stochastic processes. Understanding the distinction is critical for researchers working at the intersection of [[data science]] and physical sciences.

In the context of experimental sciences, uncertainty is often categorized into two distinct frameworks: **sampling uncertainty** and **method (or analytical) uncertainty**. As noted by [[Klau S et al., 2020]], a framework is required to differentiate between the uncertainty arising from the selection of a subset of a population (sampling) and the uncertainty inherent in the measurement process itself (method). In machine learning, the "sampling" component is an intentional, algorithmic choice designed to reduce error, whereas in chemical or biological analyses, sampling uncertainty refers to the variance introduced by the inability to measure every component of a bulk sample.

Furthermore, in physiological or chemical monitoring, such as the testing of pharmaceutical dissolution, the uncertainty is compounded by multiple stages of the analytical pipeline. As explored by [[Sano AY et al., 2023]], the fluctuations in measurement can arise from both the sampling of the tablets and the subsequent analytical steps. Similarly, in complex chemical and physicochemical analyses, the measurement uncertainty is not merely a byproduct of poor models but a fundamental limitation of the sampling process itself [[Medeiros KAR et al., 2023]].

Therefore, while a machine learning practitioner uses uncertainty sampling to *minimize* model ignorance, the analytical scientist must work to *quantify and mitigate* the intrinsic uncertainties present in the physical sampling of the subjects under study.

## Challenges and Limitations

Despite its efficiency, uncertainty sampling faces several significant bottlenecks:

*   **Sampling Bias:** Because the algorithm preferentially selects instances that are difficult to classify, it can lead to a "blind spot" where the model over-indexes on outliers or noisy data, potentially neglecting representative regions of the data distribution. This can result in a model that is highly accurate on the boundary but poor at generalizing to the center of the class clusters.
*   **The Exploration vs. Exploitation Tradeoff:** Uncertainty sampling is inherently an "exploitation" strategy—it exploits the current model's knowledge to find boundaries. However, without an "exploration" component (searching for entirely new clusters of data), the model may never discover important features located in previously unvisited parts of the [[feature space]].
*   **Sensitivity to Outliers:** High-entropy or low-margin instances are often noisy or corrupted data points. If the algorithm repeatedly selects outliers for labeling, the [[training set]] becomes polluted, leading to degraded performance.
*   **Computational Overhead:** In large-scale datasets, calculating the entropy or margin for every single unlabeled instance in every iteration can be computationally prohibitive, especially for deep neural networks with high-dimensional output layers.

## Current State and Future Directions (2025-2026)

As of 2025, the field has moved toward **Hybrid Query Strategies**. Modern frameworks often combine uncertainty sampling with **Representative Sampling** (such as [[Core-set]] approaches or [[a-data-informed-variational-clustering-framework-for-noisy-high-dimensional-data|Clustering]]-based methods). These hybrid methods ensure that the selected samples are not only uncertain but also representative of the overall data distribution, thus mitigating the risk of sampling bias.

Another emerging direction is the integration of **Bayesian Neural Networks (BNNs)** into the active learning loop. Traditional uncertainty sampling relies on the "softmax" approximation of probability, which is notoriously overconfident. BNNs, however, provide a more mathematically rigorous estimate of [[epistemic uncertainty]] (uncertainty due to lack of data) versus [[aleatoric-uncertainty-medical-image-segmentation-estimation-via-flow-matching|aleatoric uncertainty]] (inherent noise in the data).

Furthermore, the rise of **Self-Supervised Learning (SSL)** has changed the landscape. Researchers are now using uncertainty sampling to select which parts of a massive, self-supervised pretext task should be fine-tuned with human labels, creating a highly efficient pipeline that leverages unlabeled data for representation learning before applying active sampling for task-specific refinement.

## References

- Medeiros KAR et al., 2023. Drawing Attention to the Measurement Uncertainty Arising from Sampling in Chemical and Physicochemical Analyses: An Overview. Crit Rev Anal Chem. [https://pubmed.ncbi.nlm.nih.gov/35138957/](https://pubmed.ncbi.nlm.nih.gov/35138957/)
- Sano AY et al., 2023. Measurement uncertainty arising from sampling and analytical steps of dissolution test of prednisone tablets. J Pharm Biomed Anal. [https://pubmed.ncbi.nlm.nih.gov/37348366/](https://pubmed.ncbi.nlm.nih.gov/37348366/)
- Klau S et al., 2020. Sampling uncertainty versus method uncertainty: A general framework with applications to omics biomarker selection. Biom J. [https://pubmed.ncbi.nlm.nih.gov/31099917/](https://pubmed.ncbi.nlm.nih.gov/31099917/)