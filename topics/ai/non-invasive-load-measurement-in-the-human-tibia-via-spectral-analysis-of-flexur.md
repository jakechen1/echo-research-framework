---
title: Non-invasive load measurement in the human tibia via spectral analysis of flexural waves
created: 2024-05-22
source: https://arxiv.org/abs/2511.06140
tags: [biomechanics, wearable-technology, signal-processing, medical-sensors]
category: technology
---

# Non-invasive Tibial Load Measurement via Spectral Analysis

The measurement of forces transmitted through the skeletal system is a fundamental aspect of [[biomechanics]], yet performing these measurements non-invasively outside of specialized laboratory settings remains a significant technical hurdle. Recent advancements have introduced a technique for the *in vivo* measurement of tibial compressive force by utilizing the propagation of [[flexural-waves|flexural waves]] through the tibia.

### Methodology and Theory
The core of this technique involves modeling the tibia as an axially compressed [[euler-bernoulli-beam|Euler-Bernoulli beam]]. The research demonstrates that tibial flexural waves possess frequency spectra that are inherently dependent on the mechanical load applied to the bone. Under typical physiological conditions, the peak locations within the wave acceleration spectra exhibit a linear relationship with the compressive force acting on the tibia. This allows these spectral peaks to serve as highly accurate proxies for measurement.

### Experimental Validation
To test the efficacy of this method, a proof-of-concept [[wearable-sensor|wearable sensor]] system was implemented. The hardware configuration includes:
*   A **mechanical transducer** mounted to the skin to generate controlled flexural waves.
*   A **skin-mounted accelerometer** to capture the resulting wave spectra.

The validity of the system was tested on nine participants during activities such as walking trials and medial-lateral swaying. The results showed exceptional correlation, with Pearson coefficients ($r$) ranging from $0.81$ to $0.99$ (mean $r=0.93$) for swaying and $0.81$ to $0.98$ (mean $r=0.93$) for walking.

### Applications in Medicine and Sport
This technique represents a significant step forward in [[signal-processing|signal processing]] applications for health monitoring. By enabling a new class of wearable sensors, this technology could revolutionize [[sports-medicine|sports medicine]] and the study of [[human-locomotion|human locomotion]]. Continuous, non-invasive monitoring of bone loading could assist in injury prevention, the management of bone density diseases, and the optimization of athletic training protocols.