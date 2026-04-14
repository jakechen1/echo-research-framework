---
title: Spatiotemporal Interpolation of GEDI Biomass with Calibrated Uncertainty
created: 2024-05-22
source: https://arxiv.org/abs/2604.03874
tags: [GEDI, biomass, machine-learning, remote-sensing, uncertainty-quantification]
category: machine
author: wiki-pipeline
dc.title: "Spatiotemporal Interpolation of GEDI Biomass with Calibrated Uncertainty"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/spatiotemporal-interpolation-of-gedi-biomass-with-calibrated-uncertainty.md
dc.language: en
dc.rights: CC-BY-4.0
---

## Overview

The research presented in "Spatiotemporal Interpolation of GEDI Biomass with Calibrated Uncertainty" addresses one of the most significant challenges in modern [[asking-like-socrates-socrates-helps-vlms-understand-remote-sensing-images|Remote Sensing]]: the conversion of discrete, track-based LiDAR measurements into continuous, high-resolution global maps of [[Aboveground Biomass (AGB)]]. While the [[Global Ecosystem Dynamics Investigation (GEDI)]] mission provides unprecedented insights into forest structure, its sampling strategy is inherently sparse, leaving vast spatial gaps between its laser footprints. 

This paper introduces a novel framework that leverages [[machine-learning|Machine Learning]] to perform spatiotemporal interpolation, effectively "filling in" the gaps between GEDI tracks. Crucially, the methodology goes beyond simple estimation by implementing a rigorous [[uncertainty-quantification-for-distribution-to-distribution-flow-matching-in-sci|Uncertainty Quantification]] (UQ) protocol. By ensuring that the predicted uncertainties are "calibrated"—meaning the predicted error margins accurately reflect the true statistical error—the framework provides a reliable foundation for [[Climate Change]] modeling and [[Carbon Accounting]].

## The GEDI Sampling Challenge

The GEDI instrument, mounted on the [[International Space Station (ISS)]], utilizes a LiDAR-based approach to measure the vertical structure of forest canopies. Unlike optical sensors such as [[Landsat]] or [[Sentinel-2]], which provide continuous coverage of the Earth's surface, GEDI operates via a series of sampling tracks. Each track consists of a sequence of "footprints" (approximately 25 meters in diameter) that sample the forest canopy along a specific path.

This sampling strategy presents two primary difficulties for researchers:
1.  **Spatial Sparsity:** Large areas of the globe, particularly in dense tropical forests, are not directly observed by a GEDI footprint. This creates a "swiss cheese" effect in biomass datasets, making it impossible to calculate a continuous biomass density without interpolation.
2.  **Temporal Dynamics:** Vegetation is not static. Biomass fluctuates due to seasonal changes, disturbances like [[Wildfires]], and long-term [[Deforestation]]. An interpolation model that ignores the temporal dimension risks using outdated information to predict current forest states.

## Methodology: Spatiotemporal Interpolation

The core innovation of this work lies in its integrated approach to both space and time. Rather than treating each GEDI footprint as an isolated data point, the proposed model treats biomass as a continuous [[Spatiotemporal Field]].

### Feature Integration
To bridge the gaps between GEDI tracks, the model utilizes auxiliary data sources that provide continuous spatial coverage. These include:
*   **Optical Indices:** Derived from [[Sentinel-2]] and [[MODIS]], such as the [[index|Normalized Difference Vegetation Index (NDVI)]] and [[index|Enhanced Vegetation Index (EVI)]].
*   **Topographic Data:** Digital Elevation Models (DEMs) to account for the influence of terrain on biomass accumulation.
*   **Climate Variables:** Precipitation and temperature datasets that drive primary productivity.

### The Interpolation Engine
The framework employs advanced [[deep-learning|Deep Learning]] architectures, specifically designed to handle irregular sampling patterns. By training on the available GEDI footprints and using the continuous auxiliary layers as "guides," the model learns the underlying relationship between surface reflectance/topography and biomass. The interpolation process uses a kernel-based or neural-based approach to propagate information from the observed GEDI tracks into the unobserved gaps, effectively creating a seamless biomass surface.

## Uncertainty Quantification and Calibration

A critical failure point in many machine learning-based remote sensing products is "overconfidence." A model may predict a specific biomass value with high precision, but if the predicted error bars do not encompass the true value in a statistically predictable way, the model is "uncalibrated."

### Aleatoric vs. Epistemic Uncertainty
The paper distinguishes between two fundamental types of uncertainty:
*   **Aleatoric Uncertainty:** This refers to the inherent noise in the data, such as sensor error in the GEDI waveform or atmospheric interference in optical imagery.
*   **Epistemic Uncertainty:** This refers to the uncertainty in the model itself, stemming from a lack of training data in specific regions (e.g., highly complex terrains or extremely high-biomass forests).

### The Calibration Process
To achieve "calibrated uncertainty," the authors implement a post-processing step using [[Probability Calibration]] techniques (such as [[Platt Scaling]] or [[Isotonic Regression]]). The goal is to ensure that if the model predicts a 95% confidence interval, the actual observed biomass falls within that interval 95% of the time. 

This is achieved by comparing the model's predicted variance against [[In situ measurements]] and [[Ground Truth Data]]. By minimizing the gap between predicted and observed error, the framework allows policymakers and scientists to use the resulting maps for high-stakes decision-making, such as verifying [[Carbon Credit]] claims or assessing the impact of [[Ecosystem Services]] loss.

## Applications in Global Ecology

The ability to generate continuous, uncertainty-aware biomass maps has profound implications across several scientific domains:

### 1. Carbon Cycle Modeling
Accurate biomass maps are essential for quantifying the [[Global Carbon Cycle]]. By providing a continuous view of forest carbon stocks, the model allows for more precise calculations of how much carbon is being sequestered by terrestrial ecosystems versus how much is being released through decay or combustion.

### 2. Deforestation Monitoring
By integrating the temporal aspect of the interpolation, the framework can detect changes in biomass over time. This is vital for monitoring illegal logging and the impact of land-use changes in the [[Amazon Rainforest]] and the [[Congo Basin]].

###3. Climate Policy and Carbon Markets
As the [[Paris Agreement]] drives the need for transparent [[Carbon Accounting]], the "calibrated uncertainty" feature becomes a cornerstone for the [[Carbon Credit]] industry. Stakeholders can use the quantified error margins to assess the risk and legitimacy of forest-based carbon offsets, ensuring that "additionality" is scientifically verifiable.

## Comparison with Traditional Methods

Traditional methods for filling GEDI gaps often relied on simple [[Kriging]] or [[Inverse Distance Weighting (IDW)]]. While these methods are computationally efficient, they struggle with:
*   **Non-Stationarity:** They assume that the relationship between variables is constant across the landscape, which is rarely true in complex ecosystems.
*   **Feature Neglect:** They often fail to incorporate the rich, multi-dimensional information provided by auxiliary satellite imagery.
*   **Error Misrepresentation:** They often provide a measure of spatial variance but fail to account for the complex, non-Gaussian error structures present in modern machine learning outputs.

The proposed spatiotemporal approach outperforms these traditional methods by explicitly modeling the complex, non-linear interactions between forest structure, climate, and topography.

## Limitations and Future Directions

Despite its advancements, the framework faces certain limitations:
*   **Computational Complexity:** The integration of high-resolution [[Sentinel-2]] data with deep learning architectures requires significant computational resources, particularly for global-scale applications.
*   **Dependency on Auxiliary Data:** The accuracy of the interpolation is heavily dependent on the quality and temporal alignment of the auxiliary datasets (e.g., if NDVI is outdated, the biomass prediction will suffer).

Future research will focus on integrating [[Multi-modal Remote Sensing]]—combating the limitations of optical data by incorporating [[Synthetic Aperture Radar (SAR)]] from missions like [[Sentinel-1]]. This would allow for even more robust biomass estimation, particularly in areas with persistent cloud cover.

## See Also
*   [[learned-elevation-models-as-a-lightweight-alternative-to-lidar-for-radio-environ|LiDAR]]
*   [[Forestry]]
*   [[Biogeochemistry]]
*   [[machine-learning|Machine Learning in Earth Observation]]
*   [[Vegetation Indices]]
