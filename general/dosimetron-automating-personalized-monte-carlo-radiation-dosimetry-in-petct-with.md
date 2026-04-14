---
title: DosimeTron: Automating Personalized Monte Carlo Radiation Dosimetry in PET/CT with Agentic AI
created: 2024-05-22
source: https://arxiv.org/abs/2604.06280
tags: [agentic AI, dosimetry, monte carlo, pet/ct, automation]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "DosimeTron: Automating Personalized Monte Carlo Radiation Dosimetry in PET/CT with Agentic AI"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/dosimetron-automating-personalized-monte-carlo-radiation-dosimetry-in-petct-with.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DosimeTron

**DosimeTron** is an advanced [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]] system engineered to automate the complex, multi-step process of patient-specific internal radiation dosimetry within [[dosimetron-automating-personalized-monte-carlo-radiation-dosimetry-in-petct-with|PET/CT]] examinations. By leveraging a sophisticated reasoning engine (GPT-5.2) and integrating 23 specialized tools via [[Model Context Protocol]] (MCP) servers, the system streamlines the entire dosimetry pipeline through natural-language interaction.

## Overview

The primary challenge in [[nuclear medicine]] dosimetry is the computational intensity and manual labor required to calculate radiation energy deposition in various organs. DosimeTron addresses this by automating a high-fidelity pipeline that includes:

*   **Data Acquisition**: Automated DICOM metadata extraction.
*   **Image Processing**: Preprocessing and automated organ segmentation.
*   **Computational Physics**: Executing intensive [[Monte Carlo simulation]] to model radiation transport.
*   **Reporting**: Generating comprehensive, automated dosimetric reports.

## Methodology and Validation

In a retrospective evaluation involving 597 [[PSMA-PET/CT]] studies, DosimeTron was benchmarked against [[OpenDose3D]]. The system's performance was assessed using various prompt templates, ranging from single-turn instructions to complex, multi-turn conversational exchanges, all monitored via OpenTelemetry traces.

The results demonstrated exceptional precision:
*   **Correlation**: Achieved a median Pearson's $r$ of 0.997.
*   **Concordance**: Achieved a median Concordance Correlation Coefficient (CCC) of 0.996.
*   **Accuracy**: The mean absolute percentage difference remained below 5% for 19 out of 22 analyzed organs.
*   **Efficiency**: The total processing time per study averaged approximately 32.3 minutes.

## Significance

DosimeTron represents a significant milestone in the application of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] and [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|agentic AI]] within [[medical imaging]]. By eliminating execution failures and "hallucinations" in the dosimetry pipeline, it provides a robust framework for [[precision medicine]], allowing for highly personalized and scalable radiation therapy planning.