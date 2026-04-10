---
title: RQR3D: Reparametrizing the regression targets for BEV-based 3D object detection
created: 2024-05-24
source: https://arxiv.org/abs/2505.17732
tags: [3D Object Detection, Bird's-Eye View, Radar Fusion, Autonomous Driving, Computer Vision]
category: machine-learning
---

# RQR3D: Reparametrizing the regression targets for BEV-based 3D object detection

The RQR3D framework introduces a novel approach to [[3D Object Detection]] within [[Bird's-Eye View]] (BEV) perception, specifically designed to enhance the accuracy and reliability of [[Autonomous Driving]] systems.

## The Problem: Angular Discontinuity
Traditional BEV-based detection methods often rely on angle-based representations to estimate the size and orientation of rotated bounding boxes. However, the authors observed that these methods suffer from discontinuities in their loss functions—a mathematical challenge also prevalent in aerial-oriented object detection. These discontinuities can hinder the learning process and lead to imprecise orientation predictions, which are critical for safe vehicle navigation.

## The Innovation: Restricted Quadrilateral Representation
To mitigate this, the researchers proposed the **Restified Quadrilateral Representation (RQR3D)**. Instead of regressing angles directly, the method reparameterizes the regression targets into a [[Keypoint Regression]] task. The RQR3D approach regresses two primary components:
1. The smallest horizontal bounding box that encapsulates the oriented box.
2. The specific offsets between the corners of this horizontal box and the actual corners of the oriented object.

By transforming the oriented object detection problem into a keypoint-based task, the model avoids the instabilities associated with angular discontinuities.

## Efficient Radar Fusion
In addition to geometric reparameterization, the paper introduces a streamlined [[Radar Fusion]] backbone. While many existing models utilize complex voxel grouping or [[Sparse Convolutions]], RQR3D utilizes standard 2D convolutions applied to radar features. This backbone leverages the inherent 2D structure of the sensor data to ensure computationally efficient and geometrically consistent processing without the need for heavy over-parameterization.

## Experimental Results
Extensive evaluations on the [[nuScenes dataset]] demonstrate that RQR3D achieves state-of-the-art (SOTA) performance for camera-radar 3D object detection. The model reached a **67.5 NDS** and **59.7 mAP**, specifically showing significant reductions in translation and orientation errors. These improvements are crucial for the high-precision requirements of autonomous planning and safety.