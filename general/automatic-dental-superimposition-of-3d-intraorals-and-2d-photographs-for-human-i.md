---
title: Automatic dental superimposition of 3D intraorals and 2D photographs for human identification
created: 2024-05-22
source: https://arxiv.org/abs/2604.05877
tags: [forensics, computer-vision, dental-identification, 3d-modeling]
category: ai
author: wiki-pipeline
dc.title: "Automatic dental superimposition of 3D intraorals and 2D photographs for human identification"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/automatic-dental-superimposition-of-3d-intraorals-and-2d-photographs-for-human-i.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Automatic dental superimposition of 3D intraorals and 2D photographs for human identification

## Overview
Dental comparison is a fundamental pillar of [[forensic science]], serving as a primary method for [[human identification]] alongside [[DNA profiling]] and [[fingerprinting]]. While highly reliable, the process of morphological comparison is traditionally manual and time-consuming. A significant bottleneck in modern forensics is the lack of accessible ante-mortem medical records, particularly in scenarios involving migrant populations or regions without universal healthcare.

## The Problem: 2D vs. 3D Disparity
As digital presence grows, odontologists have increasingly turned to social media photos—where teeth are often visible—to find ante-mortem evidence. However, utilizing 2D photographs for comparison against 3D post-mortem scans presents major technical challenges, including:
*   **Perspective Distortion:** Unlike clinical scans, social media images lack controlled angles.
*   **Lack of Objectivity:** Existing automated methods struggle to provide a quantifiable metric for morphological differences.
*   **Modeling Limitations:** Previous state-of-the-art proposals often fail to properly model the complex projection of a 3D object onto a 2D plane.

## Proposed Solution
The research presents an automated approach to bridge the gap between 3D intraoral scans (post-mortem) and 2D photographs (ante-mortem). By employing [[computer-vision|computer vision]] and advanced [[optimization techniques]], the system replicates the perspective of the 2D image within the 3D model to perform a direct morphological comparison.

The researchers developed two distinct automated approaches:
1.  **Landmark-based Method:** Utilizing paired anatomical landmarks to align the datasets.
2.  **Segmentation-based Method:** Using the segmentation of the teeth region to estimate specific camera parameters.

## Results and Significance
The methodology was tested across 20,164 cross-comparisons from 142 samples. The results were highly successful, achieving mean ranking values of 1.6 and 1.5, respectively. This performance significantly outperforms current automatic dental chart comparison tools. 

Crucially, this system provides an automated, objective, and quantitative score of morphological correspondence. This allows forensic experts to interpret findings through easily analyzable, superimposed images, streamlining the identification process in critical humanitarian and legal contexts.