---
title: Enforcing Fair Predicted Scores on Intervals of Percentiles by Difference-of-Convex Constraints
created: 2024-05-23
source: https://arxiv.org/abs/2505.12530
tags: [machine-learning, algorithmic-fairness, optimization, mathematical-programming]
---

# Enforcing Fair Predicted Scores on Intervals of Percentiles by Difference-of-Convex Constraints

The research paper "Enforcing Fair Predicted Scores on Intervals of Percentiles by Difference-of-Convex Constraints" addresses a significant limitation in current [[Machine Learning]] fairness paradigms. Traditionally, efforts to mitigate bias focus on achieving "full fairness" across the entire distribution of predicted scores. While this approach seeks mathematical parity across all populations, it often imposes a heavy penalty on [[Predictive Performance]], creating a fundamental tension between model accuracy and social equity.

### The Concept of Partial Fairness

The authors propose a novel framework centered on the concept of **partial fairness**. Unlike existing methods that force fairness across all high- and low-percentile populations, this approach allows practitioners to define a specific [[Percentile Interval]] of interest. This is particularly useful in real-world applications where stakeholders may only be concerned with fairness at specific decision thresholds (e.g., the top decile of credit applicants). By focusing constraints only on these critical regions, the model avoids unnecessary sacrifices in accuracy for the rest of the distribution.

### Technical Methodology

To implement this localized fairness, the paper treats model training as a [[Constrained Optimization]] problem. The researchers utilize [[Difference-of-Convex (DC) Constraints]] to mathematically represent the fairness requirements within the chosen intervals. Because optimizing DC constraints is computationally challenging, the authors introduce an **Inexact Difference-of-Convex Algorithm (IDCA)**.

The paper provides a rigorous complexity analysis, demonstrating that the IDCA can efficiently find a nearly [[KKT (Karush-Kuhn-Tucker) Conditions]] point. This ensures that the optimization process is both mathematically sound and computationally feasible for large-scale datasets.

### Experimental Results

Numerical experiments conducted on real-world datasets indicate that the proposed framework effectively balances competing objectives. The methodology achieves high predictive accuracy while strictly enforcing fairness within the targeted percentiles. This approach offers a flexible, mathematically robust alternative for deploying [[Algorithmic Fairness]] in high-stakes environments where precision and equity must coexist.