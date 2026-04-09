---
title: ECLIPSE: A Composable Pipeline for Predicting ecDNA Formation, Evolution, and Therapeutic Vulnerabilities in Cancer
created: 2024-05-23
source: https://arxiv.org/abs/2604.06569
tags: [ecDNA, computational oncology, machine learning, causal inference, genomics]
categories: [ai, machine-learning, drug-discovery, biology]
---

# ECLIP\_SE

[[Extrachromosomal DNA]] (ecDNA) represents a significant driver in aggressive [[cancer]] progression. These circular DNA structures are known to amplify oncogenes, evade targeted therapies, and accelerate tumor evolution in approximately 30% of aggressive malignancies. Despite its clinical importance, the field of computational [[genomics]] regarding ecDNA has historically struggled with "circular reasoning," where models were trained on features that implicitly required prior knowledge of ecDNA status, leading to artificially inflated performance metrics.

## The ECLIPSE Framework

ECLIPSE is introduced as the first methodologically sound framework for ecDNA analysis. It is designed to eliminate data leakage and provide reliable predictions regarding the formation, evolution, and targetability of these structures. The framework is composed of three distinct, integrated modules:

### 1. ecDNA-Former
This module focuses on predicting ecDNA status using only standard genomic features. It addresses the issue of feature leakage that previously inflated AUROC values from 0.724 to 0.967 in flawed studies. By prioritizing careful feature curation over architectural complexity, ecDNA-Former achieves a robust AUROC of 0.812, demonstrating that ecDNA status is predictable without specialized sequencing.

### 2. CircularODE
To model the unique, stochastic evolutionary dynamics of ecDNA, this module utilizes physics-constrained [[Neural SDEs]] (Stochastic Differential Equations). The module is capable of zero-shot transfer and has achieved remarkable accuracy ($r > 0.997$) on experimental data, effectively capturing the complex life cycle of circular DNA within a tumor.

### 3. VulnCausal
The final module applies [[Causal Inference]] to identify therapeutic vulnerabilities. By filtering out spurious correlations that often plague standard [[Machine Learning]] approaches, VulnCausal achieves 80x enrichment over chance and provides a much higher validation rate, making it a powerful tool for [[Drug Discovery]].

## Conclusion

The development of ECLIPSE highlights a fundamental principle in [[Biomedical Machine Learning]]: methodological rigor—specifically the elimination of leakage and the encoding of domain physics—is more important than increasing model complexity. ECLIPSE provides a new, principled template for the future of [[Computational Oncology]].