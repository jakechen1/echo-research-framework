---
title: Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery
created: 2024-05-22
source: https://arxiv.org/abs/2604.07512
tags: [ai, machine-learning, drug-discovery, generative-models, chemistry]
category: drug-discovery
author: wiki-pipeline
dc.title: "Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/rhizome-os-1-rhizomes-semi-autonomous-operating-system-for-small-molecule-drug-d.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Rhizome OS-1

**Rhizome OS-1** is a pioneering semi-autonomous discovery system designed to function as an "operating system" for [[small molecule drug discovery]]. The system integrates [[agents|multi-modal AI agents]] to simulate a multidisciplinary research team, comprising specialized roles such as [[computational chemists]], [[medicinal chemists]], and [[agents|patent agents]].

## System Architecture

The core of the Rhizome OS-1 engine is **r1**, a 246M-parameter [[openglt-a-comprehensive-benchmark-of-graph-neural-networks-for-graph-level-tasks|Graph Neural Network]] (GNN). Unlike traditional generative models that rely on string-based representations, r1 is trained on a massive dataset of 800 million molecules and operates directly on molecular graphs. This allows for more precise [[de novo drug design]] by manipulating the fundamental structural topology of chemical matter.

The system's agentic framework is capable of:
* Writing and executing complex analysis code.
* Performing visual evaluations of molecular candidates.
* Assessing the [[patentability]] of newly generated structures.
* Adapting generation strategies based on empirical feedback from screening campaigns.

## Performance and Validation

The efficacy of Rhizome OS-1 was demonstrated through two intensive [[oncology|oncology]] campaigns targeting **BCL6** and **EZH2**. During these campaigns, the system generated libraries of approximately 2,355 to 2,876 novel molecules per target.

Key performance metrics include:
* **Chemical Novelty:** 91.9% of the generated Murcko scaffolds were entirely absent from the [[ChEMBL]] database for their respective targets.
* **Structural Divergence:** Tanimoto distances of 0.56–0.69 from the nearest known actives confirm that the system generates structurally distinct chemical matter rather than simple derivatives.
* **Predictive Accuracy:** Utilizing **Boltz-2** for binding affinity predictions, the system achieved ROC AUC values between 0.88 and 0.93 when calibrated against experimental data.

## Implications for [[biotechnology]]

Rhizome OS-1 introduces a new paradigm for [[understanding-and-inverse-design-of-implicit-bias-in-stochastic-learning-a-geome|inverse design]] in the pharmaceutical industry. By combining [[tools|graph-native generative tools]] with [[physics-informed scoring]], the system enables a scaled, rapid, and adaptive approach to identifying novel therapeutic candidates, significantly reducing the manual overhead typically required in early-stage drug development.