---
title: "Bias Detection in Emergency Psychiatry: Linking Negative Language to Diagnostic Disparities"
created: 2024-05-23
source: "https://arxiv.org/abs/2509.02651"
tags: [psychiatry, clinical-bias, NLP, healthcare-disparities, medical-ethics]
category: [ai, machine-learning, neuroscience]
---

# Bias Detection in Emergency Psychiatry

The emergency department (ED) is a high-stress medical environment where clinicians are susceptible to various forms of [[Clinical Bias]]. This study investigates the critical link between clinician bias exposure and psychiatric diagnostic outcomes, specifically focusing on the disproportionate diagnosis of [[Schizophrenia]] (SCZ) among racialized groups.

## Research Methodology

The study analyzed a large-scale dataset comprising 29,005 patients from a diverse medical center, encompassing diagnoses such as anxiety, bipolar disorder, depression, and trauma. To operationalize the concept of "bias exposure," the researchers utilized [[Natural Language Processing]] (NLP) to analyze psychiatric clinical notes. 

Central to the methodology was the development of the **Negative Sentence Ratio (NSR)**. This metric was calculated by quantifying the ratio of negative to total sentences within a patient's medical record. To achieve this, the researchers employed a [[Large Language Model]] (specifically [[Mistral]]) to perform automated sentiment labeling of the clinical text.

## Key Findings

Using [[Logistic Regression]], the study provided empirical evidence of how linguistic patterns correlate with diagnostic disparities:

* **Increased Diagnostic Risk:** A high NSR was found to significantly increase the odds of a patient receiving an SCQ diagnosis.
* **Mediating Role of Language:** The research demonstrated that high NSR can attenuate the visible effects of race in data by revealing that the bias is embedded in the linguistic presentation of the notes.
* **At-Risk Demographics:** The highest probability of an SCZ diagnosis was observed in Black male patients subjected to high NSR.

## Implications for Healthcare

These findings suggest that [[Sentiment Analysis]] can serve as a vital tool for auditing [[Medical Ethics]] in real-world clinical settings. By utilizing [[Machine Learning]] to identify patterns of negative language, healthcare institutions can better detect and mitigate the systemic biases that lead to [[Healthcare Equity]] disparities. This research highlights the potential of [[Artificial Intelligence]] to transform patient advocacy and promote nondiscriminatory decision-making in acute care environments.