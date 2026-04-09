---
title: Mining Electronic Health Records to Investigate Effectiveness of Ensemble Deep Clustering
created: 2024-05-22
source: https://arxiv.org/abs/2604.07085
tags: [EHR, Deep Learning, Clustering, Ensemble Learning, Healthcare Informatics]
category: machine-learning, technology
---

# Mining Electronic Health Records to Investigate Effectiveness of Ensemble Deep Clustering

The paper "Mining Electronic Health Records to Investigate Effectiveness of Ensemble Deep Clustering" addresses a critical challenge in [[Healthcare Informatics]]: the identification of [[Disease Subtypes]] through the clustering of patients in [[Electronic Health Records]] (EHR). Successful clustering is vital for elucidating complex pathophysiology and supporting data-driven clinical decision-making processes.

Historically, clustering within medical informatics has relied heavily on traditional algorithms such as [[K-means]]. While recent research has attempted hybrid methods utilizing [[Autoencoders]] to learn embedding representations, these approaches often encounter significant limitations when applied to the unique, tabular structure of EHR data. The authors note that many [[Deep Learning]] architectures are specifically optimized for image-based clustering, a task that differs substantially from the sparse and heterogeneous nature of medical records.

To bridge this gap, the researchers introduce an innovative [[Ensemble Learning]] approach: an ensemble-based deep clustering framework. Unlike standard methods that rely on a single, fixed embedding space, this proposed method aggregates cluster assignments derived from multiple embedding dimensions. This dimensionality-based aggregation allows the model to capture a much richer variety of features present within the clinical dataset.

The effectiveness of this approach was validated using real-world EHR data from the [[All of Us Research Program]], specifically targeting patient cohorts diagnosed with [[Heart Failure]]. By comparing 14 diverse clustering methods, the study demonstrated that the proposed ensemble framework provides the highest overall performance ranking across multiple cohorts. 

Beyond the algorithmic improvements, the research emphasizes the critical importance of incorporating biological sex