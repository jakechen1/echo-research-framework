---
title: "Good Rankings, Wrong Probabilities: A Calibration Audit of Multimodal Cancer Survival Models"
created: 2024-05-22
source: https://arxiv.org/abs/2604.04239
tags: [calibration, multimodal learning, oncology, deep learning, survival analysis]
categories: [ai, machine-learning, biology]
---

# Good Rankings, Wrong Probabilities: A Calibration Audit of Multimodal Cancer Survival Models

The research paper "Good Rankings, Wrong Probabilities" presents a critical evaluation of [[multimodal-deep-learning|multimodal deep learning]] models used for [[cancer-survival|cancer survival]] prediction. While these models—which integrate [[whole-slide-images|whole-slide images]] (WSI) with [[genomic-data|genomic data]]—frequently achieve high [[index|concordance index]] (C-index) scores, this study highlights a significant discrepancy between a model's ability to rank patients correctly and its ability to provide accurate [[survival-probabilities|survival probabilities]].

## Study Overview

The researchers conducted the first systematic "calibration audit" of multimodal WSI-genomics architectures. The study was divided into two primary experimental frameworks:

*   **Experiment A:** Focused on native discrete-time survival outputs using three models applied to the [[tcga-brca|TCGA-BRCA]] dataset.
*   **Experiment B:** Evaluated 11 different architectures across five different [[tcga|TCGA]] cancer types, specifically examining [[breslow-reconstructed|Breslow-reconstructed]] survival curves derived from scalar risk scores.

Using the [[benjamini-hochberg-correction|Benjamini-Hochberg correction]] to manage the [[false discovery rate|FDR]], the study found that the vast majority of models failed to meet the criteria for 1-calibration. Specifically, out of 290 fold-level tests, 166 rejected the null hypothesis of correct calibration at the median event time. Notably, the high-performing [[mcat|MCAT]] model, which boasts a strong C-index, failed 1-calibration across all five tested folds.

## Key Findings

The audit revealed several architectural and methodological insights:

1.  **Fusion Strategies:** The method used to merge data types significantly impacts reliability. [[gating-based-fusion|Gating-based fusion]] was associated with superior calibration, whereas [[bilinear-fusion|bilinear fusion]] and [[concatenation]] methods were not.
2.  **Post-hoc Refinement:** The study demonstrated that [[post-hoc-scaling|post-hoc scaling]], such as [[platt-scaling|Platt scaling]], can effectively reduce miscalibration at specific time horizons without degrading the model's discriminative power.
3.  **Metric Insufficiency:** The most significant takeaway is that the [[index|concordance index]] is an insufficient metric for evaluating [[survival-models|survival models]] intended for [[clinical-decision-support|clinical decision support]].

## Conclusion

For [[digital-pathology|digital pathology]] and [[precision-medicine|precision medicine]] to be safely integrated into clinical workflows, models must be evaluated not just on their ability to distinguish risk, but on the accuracy of their predicted probabilities. Relying solely on ranking metrics may lead to overconfident and clinically misleading prognostic assessments.