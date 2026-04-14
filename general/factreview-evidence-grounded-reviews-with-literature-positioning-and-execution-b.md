---
title: FactReview: Evidence-Grounded Reviews with Literature Positioning and Execution-Based Claim Verification
created: 2024-05-22
source: https://arxiv.org/abs/2604.04074
tags: [automated-review, LLM, peer-review, software-verification]
category: ai, machine-learning
author: wiki-pipeline
dc.title: "FactReview: Evidence-Grounded Reviews with Literature Positioning and Execution-Based Claim Verification"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/factreview-evidence-grounded-reviews-with-literature-positioning-and-execution-b.md
dc.language: en
dc.rights: CC-BY-4.0
---

# FactReview

**FactReview** is an innovative, evidence-grounded automated reviewing system designed to mitigate the growing pressure on the [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] peer review process. As submission volumes continue to surge, human reviewers face significant time constraints. Most existing [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) used for reviewing are limited to reading the manuscript provided, which makes them susceptible to being misled by high-quality writing that may lack underlying empirical truth.

## Core Methodology

To overcome the limitations of text-only analysis, FactReview implements a multi-faceted approach to verification:

*   **Claim Extraction**: The system identifies the primary technical claims and reported empirical results presented in the submission.
*   **Literature Positioning**: The framework retrieves and analyzes related research to ascertain the paper's technical position within the broader [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] landscape.
*   **Execution-Based Verification**: When the authors provide a repository, FactReview executes the released code under a bounded budget. This allows the system to perform direct empirical testing of the paper's central claims.

## The Evidence Report

The output of FactReview consists of a concise review paired with a structured **Evidence Report**. This report assesses each identified claim using one of five specific reliability labels:
1.  **Supported**
2.  **Supported by the paper**
3.  **Partially supported**
4.  **In conflict**
5.  **Inconclusive**

## Case Study: CompGCN

In a practical application involving the **CompGCN** paper, FactReview successfully reproduced results for link prediction and node classification. However, the system's execution-based verification revealed that the paper's broader performance claim regarding the MUTAG graph classification task was not fully sustained; the reproduced result was 88.4%, whereas the paper reported a baseline of 92.6%. Consequently, the claim was flagged as "Partially supported."

## Research Philosophy

The developers of FactReview suggest that the most effective role for AI in [[Peer Review]] is not to serve as a final decision-maker. Instead, AI should function as a sophisticated tool for evidence gathering, assisting human experts in producing more rigorous, transparent, and evidence-grounded assessments.

***

**Related Resources:**
*   [Review-Assistant GitHub Repository](https://github.com/DEFENSE-SEU/Review-Assistant)
*   [[Automated Software Testing]]
*   [[Reproducibility in Science]]