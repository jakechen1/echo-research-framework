---
title: Watch Before You Answer: Learning from Visually Grounded Post-Training
created: 2024-05-22
source: https://arxiv.org/abs/2604.05117
tags: [VidGround, VLM, Video Understanding, Data Curation, Post-training]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "Watch Before You Answer: Learning from Visually Grounded Post-Training"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/watch-before-you-answer-learning-from-visually-grounded-post-training.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Watch Before You Answer: Learning from Visually Grounded Post-Training

The research paper **"Watch Before You Answer: Learning from Visually Grounded Post-Training"** addresses a fundamental flaw in the current development of [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs): the reliance on linguistic cues rather than actual visual observation during video understanding tasks.

## The Problem: Linguistic Bias
The authors identify a significant discrepancy between reported performance and actual video comprehension. Their investigation into common long-video understanding benchmarks revealed that between 40% and 60% of questions can be answered accurately using textual cues alone, without any need to process the underlying video frames. This phenomenon, often referred to as linguistic bias, suggests that models are performing text-based reasoning rather than true multimodal integration. 

Crucially, this issue is not limited to evaluation benchmarks; it is also pervasive in widely used post-training datasets. This implies that much of the current progress in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] applied to video may be an illusion caused by models learning to exploit linguistic shortcuts rather than developing deep visual understanding.

## The Solution: VidGround
To mitigate this, the researchers introduce **VidGround**, a novel approach to post-training. The methodology focuses on extreme data curation, utilizing only questions that are strictly grounded in visual evidence, thereby stripping away the ability of the model to rely on linguistic biases.

When paired with [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL)-based post-training algorithms, VidGround demonstrated remarkable efficiency and effectiveness:
* **Performance Boost:** Improved performance by up to 6.2 points compared to using full, uncurated datasets.
* **Data Efficiency:** Achieved these gains using only 69.1% of the original post-training data.

## Conclusion
The study concludes that data quality is the primary bottleneck in advancing [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] for video understanding. The authors demonstrate that simple, focused data curation can outperform more complex, computationally expensive post-training techniques. This highlights a critical need for the community to develop new, rigorously grounded benchmarks to ensure the next generation of VLMs truly "watch" the content they process.