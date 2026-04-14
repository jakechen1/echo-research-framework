---
title: "Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06723"
tags: [AI, LLM, Software Engineering, Machine Learning, Calibration, Automated Code Revision]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/fine-grained-approaches-for-confidence-calibration-of-llms-in-automated-code-rev.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision

## Overview
In the modern landscape of [[AI-assisted software engineering]], developers are increasingly dependent on [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to augment productivity. However, because these models are inherently imperfect, their tendency to produce incorrect outputs presents a significant risk. To mitigate this, researchers focus on [[fine-grained-approaches-for-confidence-calibration-of-llms-in-automated-code-rev|Confidence Calibration]]—the process of ensuring that a model's reported confidence scores accurately reflect its actual likelihood of being correct.

## The Limitation of Global Calibration
A standard approach to calibration is the use of "global Platt-scaling," which applies a scaling factor to sequence-level confidence scores. While this method has been effective in various generative tasks, the authors of this study argue that it is insufficient for [[Automated Code Revision]] (ACR) tasks, such as program repair, vulnerability repair, and code refinement.

The core hypothesis is that the coarse-grained nature of global methods is ill-suited for ACR. In code revision, correctness is often dictated by precise, local edit decisions. Because miscalibration can be highly sample-dependent, a single global metric fails to capture the nuances of the specific changes made to a codebase.

## Proposed Fine-grained Approach
To address these shortcomings, the study proposes a **local Platt-scaling** method. Rather than relying on a single score for an entire code sequence, the researchers applied scaling separately to three different fine-grained confidence scores. This allows the model to communicate confidence at a more granular level, closely aligning with the local nature of code edits.

## Experimental Findings
The study evaluated the proposed approach across three distinct tasks and 14 different [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models of varying scales. The findings include:
* **Improved Accuracy:** Fine-grained confidence scores consistently achieved lower calibration error across a wider range of probability intervals compared to traditional methods.
* **Enhanced Scaling:** The benefits of the fine-grained approach were further amplified when integrated with global Platt-scaling.

## Conclusion
The development of fine-grained calibration offers a practical solution for eliciting trustworthy scores from imperfect models. By providing a more reliable metric for output acceptance, this methodology enables a more streamlined and dependable integration of LLMs into the [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] lifecycle.