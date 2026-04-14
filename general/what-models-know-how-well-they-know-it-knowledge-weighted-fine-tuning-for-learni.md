---
title: "What Models Know, How Well They Know It: Knowledge-Weighted Fine-Tuning for Learning When to Say 'I Don't Know'"
created: 2024-05-22
source: https://arxiv.org/abs/2604.05779
tags: [Large Language Models, Hallucination, Fine-Tuning, Uncertainty Quantification, Machine Learning]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "What Models Know, How Well They Know It: Knowledge-Weighted Fine-Tuning for Learning When to Say 'I Don't Know'"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/what-models-know-how-well-they-know-it-knowledge-weighted-fine-tuning-for-learni.md
dc.language: en
dc.rights: CC-BY-4.0
---

# What Models Know, How Well They Know It

The research paper **"What Models Know, How Well They Know It"** addresses one of the most persistent challenges in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]: the phenomenon of **hallucination** in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). While LLMs excel at diverse user queries, they frequently generate confident but incorrect information, a problem largely attributed to "knowledge misalignment" between the initial pre-training stage and the subsequent fine-tuning stage.

## The Problem: Knowledge Misalignment
The authors identify that hallucinations often arise when there is a discrepancy between the model's internal knowledge (acquired during pre-training) and the new instructions or data presented during fine-tuning. When a model is forced to respond to queries that fall outside its pre-trained knowledge base, it lacks the mechanism to signal its own ignorance, leading to inaccurate outputs.

## The Solution: Knowledge-Weighted Fine-Tuning
To mitigate this, the researchers propose a novel training approach called **Knowledge-Weighted Fine-Tuning**. The methodology relies on several key components:

1.  **Instance-Level Scoring**: The researchers use multi-sampled inference to reliably estimate a fine-grained, instance-level knowledge score for each query.
2.  **Scaled Learning Signals**: Instead of treating all training data equally, the system scales the learning signal based on the model's existing knowledge of the topic.
3.  **Explicit Uncertainty**: The fine-tuning process is designed to encourage the model to provide explicit "I don't know" responses for queries that are determined to be out-of-scope.

## Experimental Results and Impact
Experimental evaluations demonstrate that this approach allows models to effectively distinguish between known and unknown information. Crucially, the model can express uncertainty without sacrificing accuracy on queries it is capable of answering. 

Furthermore, the paper introduces new evaluation metrics for **uncertainty quantification**, providing a standardized way to measure how effectively a model can discriminate between known instances and unknown, out-of-scope queries. This advancement is vital for developing more reliable [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] systems for high-stakes applications in [[us-cities-are-axing-flock-safety-surveillance-technology|Technology]] and science.