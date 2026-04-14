---
title: Physical Adversarial Attacks on AI Surveillance Systems: Detection, Tracking, and Visible--Infrared Evasion
created: 2024-05-23
source: https://arxiv.org/abs/2604.06865
tags: [adversarial_attacks, surveillance, computer_vision, multi_object_tracking, infrared_imaging]
category: ai
---

# Physical Adversarial Attacks on AI Surveillance Systems

This paper provides a critical review of [[physical-adversally-attacks|Physical Adversally Attacks]] through the lens of modern [[physical-adversarial-attacks-on-ai-surveillance-systemsdetection-tracking-and-vi|AI Surveillance]] systems. Moving away from traditional benchmarks that focus on isolated, single-frame image perturbations, the authors argue for a "surveillance-oriented" perspective. In real-world deployments, effectiveness is not merely about suppressing an [[telescope-learnable-hyperbolic-foveation-for-ultra-long-range-object-detection|Object Detection]] algorithm in a single frame, but about disrupting the entire integrated [[computer-vision|Computer Vision]] pipeline.

### Key Dimensions of Attack Evaluation

The research identifies several technical pillars that define the efficacy of an attack in a surveillance context:

*   **Temporal Persistence:** An attack must evade [[multi-object-tracking|Multi-Object Tracking]] (MOT) over time. If a perturbation suppresses a detector in one frame but the identity is recovered via tracking in subsequent frames, the attack loses its practical utility.
*   **Sensing Modality:** Modern security infrastructures often utilize [[multi-modal-sensing|Multi-Modal Sensing]], such as [[visible-infrared-rgb-t-imaging|Visible-Infrared (RGB-T) Imaging]]. Effective attacks must address both RGB and thermal inputs to prevent detection during night-time operations or low-light conditions.
*   **Carrier Realism:** The physical medium of the attack (the "carrier") is a critical factor. The paper distinguishes between conspicuous, easily detected patches and more sophisticated, stealthy methods like [[adversarial-clothing|Adversarial Clothing]] or selectively activated wearables.

### System-Level Robustness

The authors highlight that evaluating [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] robustness using standard per-frame accuracy metrics is insufficient for high-stakes surveillance. A robust evaluation framework must account for:

1.  **Distance Robustness:** The degradation of attack efficacy as the subject moves further from the sensor.
2.  **Camera-Pipeline Variation:** Resilience against different lens distortions, resolutions, and preprocessing steps.
3.  **Identity-Level Metrics:** Assessing whether an individual's identity can be maintained through a tracking sequence despite adversarial perturbations.

The paper concludes that the field is shifting toward viewing surveillance security as a complex, system-wide problem involving temporal, sensor-based, and physical deployment constraints, rather than a simple image-classification challenge.