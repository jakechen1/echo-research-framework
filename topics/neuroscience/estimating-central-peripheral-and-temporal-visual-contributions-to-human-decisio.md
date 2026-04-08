---
title: Estimating Central, Peripheral, and Temporal Visual Contributions to Human Decision Making in Atari Games
created: 2024-05-22
source: https://arxiv.org/abs/2604.04439
tags: [eye-tracking, Atari, decision-making, ablation-study, peripheral-vision, machine-learning]
category: neuroscience
---

# Estimating Central, Peripheral, and Temporal Visual Contributions to Human Decision Making in Atari Games

This research investigates the specific roles played by different visual information streams in driving human decision-making within dynamic, high-speed environments. Utilizing the [[Atari-HEAD]] dataset—a large-scale collection of [[Atari]] gameplay paired with synchronized [[eye-tracking]] data—the study employs a novel controlled ablation framework to quantify the importance of various sensory inputs.

## Methodology
The study aims to reverse-engineer human behavior by training [[action-prediction networks]] under six distinct experimental settings. The researchers selectively included or excluded three primary information sources to observe the impact on prediction accuracy:

1.  **Peripheral Visual Information**: Visual data located outside the current point of gaze.
2.  **Gaze Information**: Explicit gaze maps representing the current focus of attention (foveal vision).
3.  **Past-State Information**: Temporal data and state information derived from previous frames of gameplay.

## Key Findings
The results reveal a surprising hierarchy of importance regarding how humans process visual stimuli during gameplay. Contrary to the intuition that eye movements (gaze) are the primary drivers of action, the study found that [[peripheral vision]] is the most critical component. 

*   **Peripheral Impact**: Removing peripheral information caused a massive median prediction-accuracy drop ranging from **35.27% to 43.90%**.
*   **Gaze Impact**: The loss of explicit gaze information yielded much smaller accuracy decreases, between **2.11% and 2.76%**.
*   **Temporal Impact**: The influence of past-state information varied more broadly