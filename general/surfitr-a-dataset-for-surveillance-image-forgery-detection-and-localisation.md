---
title: SurFITR: A Dataset for Surveillance Image Forgery Detection and Localisation
created: 2024-05-22
source: https://arxiv.org/abs/2604.07101
tags: [computer vision, digital forensics, dataset, surveillance, generative ai]
category: ai
author: wiki-pipeline
dc.title: "SurFITR: A Dataset for Surveillance Image Forgery Detection and Localisation"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/surfitr-a-dataset-for-surveillance-image-forgery-detection-and-localisation.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SurFITR: A Dataset for Surveillance Image Forgery Detection and Localisation

**SurFITR** (Surveillance Forgery Image Test Range) is a specialized dataset engineered to address the evolving challenges of detecting and localizing image manipulations within surveillance-style imagery. As advancements in [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]] and open-access image generation models become more accessible, the risk of creating fraudulent visual evidence—commonly referred to as [[Deepfakes]]—has increased significantly.

### The Problem of Generalization
Most existing forgery detection models are trained on datasets that focus on "object-centric" images, where manipulations are often large-scale or involve full-image synthesis. These models struggle to generalize to surveillance scenarios. In real-world surveillance, digital tampering is typically:
* **Localized and Subtle:** Changes are often small and difficult to perceive.
* **Environmentally Complex:** Sceneries involve varied viewpoints, occlusions, and low-resolution textures.
* **Low Visual Quality:** The inherent noise and compression in surveillance footage can mask forgery artifacts.

### Methodology and Dataset Composition
To bridge this gap, the SurFITR project utilizes a sophisticated pipeline powered by [[multimodal-large-language-models-for-multi-subject-in-context-image-generation|Multimodal Large Language Models]] (MLLMs). This approach allows for semantically aware, fine-grained editing, ensuring that the generated forgeries are realistic and contextually integrated into the scene.

The dataset comprises over **137,000 tampered images**. Key features include:
* **Diverse Resolutions:** A wide range of image qualities to simulate various camera types.
* **Multiple Edit Types:** Various manipulation techniques implemented via different image editing models.
* **Semantic Precision:** High-fidelity localized edits that mimic actual forensic tampering.

### Experimental Findings
Extensive testing reveals that current state-of-the-art detectors suffer significant performance degradation when evaluated on the SurFITR dataset. However, the researchers demonstrated that training models specifically on SurFITR data yields substantial improvements in both [[domain|In-domain]] and [[cross-domain-few-shot-learning-for-hyperspectral-image-classification-based-on-m|Cross-domain]] performance. This suggests that SurFITR is a vital resource for training robust [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models capable of maintaining integrity in high-stakes forensic environments.

The SurFITR dataset is publicly available on GitHub for use in the [[computer-vision|Computer Vision]] and digital forensics research communities.