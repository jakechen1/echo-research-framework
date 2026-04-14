---
title: Predicting Intermittent Job Failure Categories for Diagnosis Using Few-Shot Fine-Tuned Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2601.22264
tags: [ai, machine-learning, technology, software-engineering, NLP]
author: wiki-pipeline
dc.title: "Predicting Intermittent Job Failure Categories for Diagnosis Using Few-Shot Fine-Tuned Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/predicting-intermittent-job-failure-categories-for-diagnosis-using-few-shot-fine.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Predicting Intermittent Job Failure Categories for Diagnosis

## Overview
In modern [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] workflows, [[Continuous Integration (CI)]] pipelines are essential for maintaining code quality. However, pipelines frequently suffer from intermittent (flaky) job failures caused by non-deterministic tests, network outages, and resource exhaustion. While existing [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] research has focused on detecting these failures, there remains a significant gap in the ability to diagnose them. 

This paper introduces a framework designed to move beyond detection toward automated [[Automated Triage]] and diagnosis.

## Technical Approach

### FlaXifyer
The authors present **FlaXifyer**, a [[cross-domain-few-shot-learning-for-hyperspectral-image-classification-based-on-m|few-shot learning]] approach that utilizes pre-trained [[$s^3$-stratified-scaling-search-for-test-time-in-diffusion-language-models|Language Models]] to categorize the root causes of intermittent failures. A key advantage of FlaXifyer is its efficiency; it requires only job execution logs as input and can achieve high performance with minimal supervision—specifically, only 12 labeled examples per failure category.

### LogSift
To address the "black box" nature of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models, the researchers developed **LogSift**. This is an interpretability technique aimed at identifying the most influential log statements contributing to a prediction. LogSift is designed for high-speed performance, processing logs in under one second to reduce the manual oversight required by developers.

## Key Results
The study evaluated the framework using a dataset of 2,458 job failures from TELUS, yielding the following results:

* **Predictive Accuracy:** FlaXifyer achieved an **84.3% Macro F1** and a **92.0% Top-2 accuracy**.
* **Reduced Cognitive Load:** LogSift reduced manual log review effort by **74.4%**.
* **Information Relevance:** The interpretability tool successfully surfaced relevant failure information in **87%** of investigated cases.

## Significance
The combination of FlaXifyer and LogSift provides a scalable pathway toward the automated resolution of infrastructure instabilities. By reducing the time developers spend on manual diagnosis, this technology helps mitigate the wasted computational resources and productivity losses associated with [[DevOps]] pipeline instability.