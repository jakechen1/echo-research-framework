---
title: OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research
created: 2024-05-22
source: https://arxiv.org/abs/2504.15564
tags: [Python, LLM, Code Generation, Dataset, Software Engineering]
category: ai, technology
author: wiki-pipeline
dc.title: "OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/openclassgen-a-large-scale-corpus-of-real-world-python-classes-for-llm-research.md
dc.language: en
dc.rights: CC-BY-4.0
---

# OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research

OpenClassGen represents a major advancement in the training and evaluation of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) specifically tailored for [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] tasks. While previous benchmarks such as ClassEval and RealClassEval were limited by small sample sizes (ranging from 100 to 400 classes), OpenClassGen provides a massive-scale corpus of 324,843 Python classes extracted from 2,970 engineered open-source projects.

## Dataset Composition and Architecture
The primary innovation of OpenClassGen is its structured approach to class-level generation. Each entry in the corpus pairs a complete, human-written Python class with a "skeleton." This skeleton is a self-contained specification consisting of class and method signatures accompanied by their relevant docstrings. 

Unlike existing datasets that require complex repository-level context resolution, OpenClassGen's skeletons allow for standalone generation tasks. Furthermore, the dataset is enriched with 27 static code metrics, providing researchers with deep insights into:
* **Complexity metrics:** Cyclomatic complexity and depth.
* **Structural properties:** Coupling, cohesion, and inheritance patterns.

## Evaluation and Findings
To demonstrate the utility of the corpus, the authors evaluated several leading models, including GPT-o4-mini, Claude-4-Sonnet, and Qwen-3-Coder, on a curated subset of 300 executable classes. The evaluation utilized a test suite achieving 58% branch coverage.

The experimental results revealed a significant gap between semantic imitation and logical execution:
1. **High Semantic Similarity:** Models achieved