---
title: Investigating Data Interventions for Subgroup Fairness: An ICU Case Study
created: 2023-10-27
source: https://arxiv.org/abs/2604.03478
tags: [algorithmic bias, healthcare, machine learning, data-centric AI, fairness]
categories: [ai, machine-learning, technology]
---

# Investigating Data Interventions for Subgroup Fairness: An ICU Case Study

The paper "Investigating Data Interventions for Subgroup Fairness: An ICU Case Study" addresses the critical challenge of [[algorithmic-bias|Algorithmic Bias]] in high-stakes [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] environments. As automated decision-making becomes more integrated into healthcare, the potential for models to exacerbate systemic harms to specific subgroups has become a primary concern for developers and clinicians alike.

### The Problem of Data Scaling
A common approach to mitigating bias is to "fix the data" by increasing the diversity and volume of the training set. However, this research highlights that the benefits of data scaling are often volatile. When new data sources are introduced, the improvements gained from a larger sample size can be counteracted by the introduction of [[learning-stable-predictors-from-weak-supervision-under-distribution-shift|Distribution Shift]]. This occurs when the new data possesses statistical characteristics that differ significantly from the original training distribution, leading to unpredictable changes in model behavior.

### Empirical Case Study
The study utilizes two prominent [[mining-electronic-health-records-to-investigate-effectiveness-of-ensemble-deep-c|Electronic Health Records]] (EHR) datasets:
*   **eICU Collaborative Research Database**
*   **MIMIC-IV dataset**

By analyzing clinical models trained on these datasets, the researchers discovered that simply adding more data can both help and hurt both model performance and [[investigating-data-interventions-for-subgroup-fairness-an-icu-case-study|Subgroup Fairness]]. The study indicates that many intuitive strategies for data selection—often relied upon to improve model robustness—are frequently unreliable in a clinical context.

### Proposed Solutions
The authors compare two primary intervention methods:
1.  **Data-Centric Strategies:** Interventions focused on the selection and addition of new data.
2.  **Model-Based Approaches:** Techniques such as [[post-hoc-calibration|Post-hoc Calibration]] to adjust model outputs after training.

The findings suggest that neither strategy is sufficient in isolation. Instead, the most effective way to improve performance across different subgroups is through a hybrid approach that combines both data-centric addition and model-based calibration. Ultimately, the paper challenges the traditional "better data" dogma, advocating for a more nuanced, multi-faceted approach to building fair and robust [[clinical-decision-support-systems|Clinical Decision Support Systems]].