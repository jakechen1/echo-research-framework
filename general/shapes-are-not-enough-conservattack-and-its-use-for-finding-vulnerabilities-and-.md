---
title: Shapes are not enough: CONSERVAttack and its use for finding vulnerabilities and uncertainties in machine learning applications
created: 2024-05-22
source: https://arxiv.org/abs/2603.13970
tags: [adversarial-attack, high-energy-physics, machine-learning-robustness, uncertainty-quantification]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "Shapes are not enough: CONSERVAttack and its use for finding vulnerabilities and uncertainties in machine learning applications"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/shapes-are-not-enough-conservattack-and-its-use-for-finding-vulnerabilities-and-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Shapes are not enough: CONSERVAttack

CONSERVAttack is an innovative [[explainability-guided-adversarial-attacks-on-transformer-based-malware-detectors|adversarial attack]] framework designed to identify unobserved vulnerabilities in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] models, specifically within the context of [[High Energy Physics]] (HEP).

## The Problem of Validation
In scientific domains like HEP, [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|deep learning]] models are increasingly utilized to analyze both simulated and experimental data. To ensure scientific integrity, researchers employ rigorous testing regimes to account for [[systematic uncertainties]]. Standard validation processes typically involve:
* Comparing the "shapes" of distributions between simulation and data.
* Evaluating marginal distributions.
* Analyzing linear feature correlations in "control regions."

However, the paper argues that being guided by physical motivation and specific region constraints does not guarantee that all potential sources of error or mismodelling are captured. There remains a "hidden" space of deviations that standard checks are not programmed to detect.

## The CONSERVAttack Mechanism
CONSERVAttack is specifically designed to exploit this remaining space of hypothetical deviations. The method generates adversarial perturbations that are mathematically engineered to stay within the established [[uncertainty bounds]]. 

Because these perturbations are technically consistent with the accepted margins of error, they are able to evade standard validation checks and appear as "allowable" statistical fluctuations. Despite this invisibility to traditional tests, the perturbations are potent enough to successfully fool the underlying [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] model, potentially leading to incorrect scientific conclusions.

## Implications and Mitigation
The research highlights a critical gap in how we assess the reliability of [[a-mathematical-theory-of-evolution-for-self-designing-ais|AI]] in science. It suggests that "shapes" and distribution matches are insufficient for guaranteeing model stability. The authors propose that [[adversarial-robustness-of-deep-state-space-models-for-forecasting|adversarial robustness]] must be treated as a fundamental component of the interpretation of deep learning results in particle physics. 

Beyond identifying vulnerabilities, the paper also proposes strategic approaches for [[crab-codebook-rebalancing-for-bias-mitigation-in-generative-recommendation|mitigation]], aiming to strengthen models against these types of stealthy, uncertainty-consistent attacks.