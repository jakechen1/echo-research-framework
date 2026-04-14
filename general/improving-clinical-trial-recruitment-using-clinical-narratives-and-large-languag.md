---
title: Improving Clinical Trial Recruitment using Clinical Narratives and Large Language Models
created: 2024-05-23
source: https://arxiv.org/abs/2604.05190
tags: [clinical trials, LLM, RAG, medical AI, patient screening, drug discovery]
categories: [ai, machine-learning, drug-discovery, technology]
author: wiki-pipeline
dc.title: "Improving Clinical Trial Recruitment using Clinical Narratives and Large Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/improving-clinical-trial-recruitment-using-clinical-narratives-and-large-languag.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Improving Clinical Trial Recruitment using Clinical Narraries and LLMs

The process of screening patients for [[Clinical Trials]] enrollment remains a significant bottleneck in the [[targeting-phgdh-for-alzheimers-disease-drug-discovery-strategies|Drug Discovery]] pipeline. Manual screening is labor-intensive and prone to error, often leading to under-enrollment and subsequent trial failures. The research paper "Improving Clinical Trial Recruitment using Clinical Narratives and Large Language Models" explores how advancements in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] can automate and optimize this screening process.

## Methodology

The study systematically investigates the efficacy of both encoder-based and decoder-based [[Large Language Models (LLMs)]], comparing general-purpose models against those specifically adapted for the medical domain. A primary focus of the research is addressing the "Lost in the Middle" phenomenon, where models struggle to process information located in the center of large datasets. To combat this, the researchers tested three primary strategies:

1.  **Original Long-Context:** Utilizing the standard, default context windows provided by LLMs.
2.  **NER-based Extractive Summarization:** Transforming lengthy clinical narratives into condensed versions using [[Named Entity Recognition (NER)]].
3.  **Retrieval-Augmented Generation (RAG):** Implementing dynamic evidence retrieval based on specific trial eligibility criteria to focus the model's attention.

## Key Findings

Using the 2018 N2C2 Track 1 benchmark dataset, the study found that the **MedGemma** model, when paired with a [[leveraging-wireless-sensor-networks-for-real-time-monitoring-and-control-of-indu|RAG]] strategy, achieved the highest performance with a micro-F1 score of 89.05%. 

The research highlights a divergence in utility based on task complexity:
*   **Generative LLMs** show remarkable improvements for trial criteria that require deep, long-term reasoning across fragmented parts of long documents.
*   **Short-context criteria** (such as simple lab test results) saw only incremental improvements from the more complex generative architectures.

## Conclusion

For the implementation of [[Medical AI]] in real-world clinical settings, the study emphasizes that model selection must be strategic. Developers must weigh the computational costs of generative LLMs against the efficiency of rule-based queries or encoder-based models to find the optimal balance for specific recruitment tasks.