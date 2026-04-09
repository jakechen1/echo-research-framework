---
title: The Geometry of Forgetting
created: 2024-05-22
source: https://arxiv.org/abs/2604.06222
tags: [geometry, embeddings, memory, interference, error-modeling]
category: machine-learning
---

# The Geometry of Forgetting

The paper "The Geometry of Forgetting" proposes a paradigm shift in how we understand memory phenomena. Rather than attributing forgetting and [[false memories]] to biological decay or hardware limitations, the authors argue that these behaviors are inherent, emergent properties of the [[geometry]] found in [[high-dimensional embedding spaces]].

## Interference vs. Decay

One of the study's most significant findings is the distinction between memory decay and memory interference. Traditional models suggest that forgetting occurs due to the temporal degradation of information. However, this research demonstrates that [[power-law forgetting]] (with a study-derived exponent $b \approx 0.460$ compared to the human $b \approx 0.5$) is primarily driven by competition and interference among overlapping memories. 

When the researchers isolated the decay function by removing competing memories, the decay exponent plummeted to a negligible $b \approx 0.009$, fifty times smaller than the experimental result. This suggests that time alone is not the primary driver of forgetting; rather, it is the structural competition of signals within the [[semantic space]].

## Effective Dimensionality and Vulnerability

The researchers analyzed production [[embedding models]] typically ranging from 384 to 1,024 dimensions. They discovered that these models concentrate their variance in only approximately 16 effective dimensions. This significant reduction in functional dimensionality places these systems deep within an "interference-vulnerable" regime, making them susceptible to the same types of errors observed in human cognition.

## The Emergence of False Alarms

The study also successfully replicated the [[Deese–Roediger–McDermott (DRM) effect]]—a phenomenon where individuals falsely remember items that were not presented but are semantically related to the presented list. By applying [[cosine similarity]]