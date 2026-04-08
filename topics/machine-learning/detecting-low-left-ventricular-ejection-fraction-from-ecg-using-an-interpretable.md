---
title: Detecting low left ventricular ejection fraction from ECG using an interpretable and scalable predictor-driven framework
created: 2024-05-22
source: https://arxiv.org/abs/2603.28532
tags: [ai, machine-learning, cardiology, healthcare-technology]
category: ai, machine-learning, technology
---

# Detecting low left ventricular ejection fraction from ECG using an interpretable and scalable predictor-driven framework

The research paper introduces **ECGPD-LEF**, a novel, structured framework designed for the detection of low [[Left Ventricular Ejection Fraction (LVEF)]] using [[Electrocardiography (ECG)]]. The primary goal of the study is to address the clinical challenge of detecting ventricular dysfunction before it progresses to symptomatic [[Heart Failure]].

### Problem Statement
Identifying low LVEF is critical for timely intervention, yet it often remains undiagnosed until advanced stages of disease. While [[Artificial Intelligence (AI)]]-enabled ECG analysis has shown promise, most current approaches rely on "black-box" end-to-end models that lack clinical interpretability. Furthermore, existing tabular systems often depend on commercial measurement algorithms that can yield suboptimal performance.

### The ECGPD-LEF Framework
To bridge the gap between performance and transparency, the researchers developed the **ECG-based Predictor-Driven LEF (ECGPD-LEF)**. Unlike traditional models, this framework integrates diagnostic probabilities derived from [[Foundation Models]] into an interpretable modeling structure. 

The framework was trained using the **EchoNext dataset**, a large-scale benchmark consisting of 72,475 ECG-echocardiogram pairs. The study's validation involved significant independent testing:
* **Internal Cohort (n=5,442):** Achieved an AUROC of 88.4% and an F1 score of 64.5%.
* **External Cohort (n=16,017):** Achieved an AUROC of 86.8% and an F1 score of 53.6%.

The model consistently outperformed standard end-to-end baselines across diverse clinical and demographic subgroups.

### Interpretability and Clinical Significance
A major contribution of this work is the identification of interpretable "high-impact predictors" that drive the risk estimation. The analysis highlighted specific ECG features, such as:
* Normal ECG patterns
* Incomplete [[Left Bundle Branch Block (LBBB)]]
* Subendocardial injury in anterolateral leads

The study found that these individual predictors were capable of "zero-shot-like" inference, meaning they could estimate risk without task-specific retraining. This suggests that the indicators of ventricular dysfunction are intrinsically encoded within the structured diagnostic probabilities. This level of mechanistic transparency supports the framework's scalability and its seamless integration into existing [[AI-ECG]] diagnostic ecosystems.