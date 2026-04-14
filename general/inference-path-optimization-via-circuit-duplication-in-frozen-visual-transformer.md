---
title: Inference-Path Optimization via Circuit Duplication in Frozen Visual Transformers for Marine Species Classification
created: 2024-05-22
source: https://arxiv.org/abs/2604.03428
tags: [ai, machine-learning, computer-vision, marine-biology, transformers]
category: ai
author: wiki-pipeline
dc.title: "Inference-Path Optimization via Circuit Duplication in Frozen Visual Transformers for Marine Species Classification"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/inference-path-optimization-via-circuit-duplication-in-frozen-visual-transformer.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Inference-Path Optimization via Circuit Duplication

The research paper "Inference-Path Optimization via Circuit Duplication in Frozen Visual Transformers for Marine Species Classification" introduces an innovative approach to improving the performance of [[inside-out-measuring-generalization-in-vision-transformers-through-inner-working|Vision Transformers]] in the field of [[Marine Biology]] without the computational burden of [[convolearn-a-dataset-for-fine-tuning-dialogic-ai-tutors|Fine-tuning]].

## Context and Problem
Automated underwater species classification is inherently difficult due to the high cost of manual data annotation and the extreme environmental variations, such as lighting and turbidity, that limit the transferability of [[loft-parameter-efficient-fine-tuning-for-long-tailed-semi-supervised-learning-in|Supervised Learning]] models. While [[Self-Supervised Learning]] models—specifically those providing frozen embeddings—provide a strong foundation for label-efficient classification, there has been limited research into optimizing these models at the inference stage without altering their underlying weights.

## Methodology: Circuit Duplication
The authors adapt **Circuit Duplication**, a technique originally developed for [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]], for use in [[computer-vision|Computer Vision]]. The method involves selecting a specific range of transformer layers to be traversed twice during a single forward pass. This process optimizes the inference path without requiring [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|Gradient Descent]] or any permanent changes to the model weights.

The