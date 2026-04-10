---
title: Time series generation for option pricing on quantum computers using tensor network
created: 2024-05-22
source: https://arxiv.org/abs/2402.17148
tags: [quantum-computing, tensor-networks, finance, machine-learning]
category: machine-learning
---

The research paper explores a novel methodology for enhancing [[Quantum Computing]] applications within the [[Finance]] sector, specifically targeting the algorithmic complexities of [[Option Pricing]]. A significant bottleneck in current quantum algorithms for pricing derivatives is the high computational cost associated with preparing quantum states that accurately represent the probability distribution of underlying asset prices. This technical challenge is further intensified when dealing with [[path-dependent options]], which require the generation of a complex quantum state encoding a joint distribution of the asset price across multiple, successive time points.

To address these computational inefficiencies, the researchers propose utilizing a [[Matrix Product State]] (MPS)—a specialized form of [[Tensor Network]]—as a generative model for [[Time Series Generation]]. Because an MPS can be efficiently mapped and encoded into the computational state of qubits, it provides a mathematically compact and hardware-efficient way to represent complex probability distributions. The paper provides a detailed procedural framework for the training of such an MPS, focusing on optimizing its ability to capture the intricate temporal dynamics and correlations inherent in financial time series.

To validate the efficacy of the proposed approach, the authors conducted numerical experiments using the [[Heston model]], a prominent stochastic volatility model used extensively in quantitative finance. The experimental results demonstrate that the MPS-based generative model is capable of accurately reconstructing the paths predicted by the Heston model. These findings highlight the potential of integrating [[Machine Learning]]-inspired architectures with quantum circuits, offering a promising pathway toward efficient, large-scale [[path-dependent option pricing]] on both NISQ-era and future [[quantum computers]].