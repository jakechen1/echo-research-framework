---
title: From Universal to Individualized Actionability: Revisiting Personalization in Algorithmic Recourse
created: 2024-05-22
source: https://arxiv.org/abs/2604.08030
tags: [algorithmic recourse, personalization, machine learning, fairness, AI ethics]
category: ai, machine-learning
author: wiki-pipeline
dc.title: "From Universal to Individualized Actionability: Revisiting Personalization in Algorithmic Recourse"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/from-universal-to-individualized-actionability-revisiting-personalization-in-alg.md
dc.language: en
dc.rights: CC-BY-4.0
---

# From Universal to Individualized Actionability

The research paper, "From Universal to Individualized Actionability: Revisiting Personalization in Algorithmic Recourse," addresses a significant gap in the study of [[algorithmic recourse]]. While much of the existing literature in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] focuses on the universal properties of recourse—such as efficiency, robustness, and [[cafp-a-post-processing-framework-for-group-fairness-via-counterfactual-model-ave|fairness]]—the role of personalized user preferences remains largely unquantified and structurally undefined.

## The Framework of Individual Actionability

The authors propose moving away from implicit personalization toward a formal definition termed **individual actionability**. This framework categorizes personalization into two distinct dimensions:

1.  **Hard Constraints:** These represent the absolute boundaries of what an individual can change, defining which features are physically or legally actionable (e.g., one can change a credit limit, but not their date of birth).
2.  **Soft Constraints:** These capture the subjective preferences of a user, specifically relating to the perceived costs and values associated with various actions (e.g., a preference for minimizing financial expenditure over minimizing time spent).

To operationalize these dimensions, the paper utilizes a [[causal algorithmic recourse]] framework. It employs a **pre-hoc user-prompting approach**, where individuals express their preferences through rankings or scores prior to the generation of any algorithmic recommendation.

## Critical Trade-offs and Findings

Through extensive empirical evaluation, the study identifies several critical tensions between personalization and standard recourse desiderata:

*   **Impact on Validity and Plausibility:** The implementation of individual