title: AFL: A Single-Round Analytic Approach for Federated Learning with Pre-trained Models
created: 2024-05-24
source: https://arxiv.org/abs/2405.16240
tags: [federated-learning, analytic-learning, pre-trained-models, optimization, communication-efficiency]
category: machine-learning

# AFL: A Single-Round Analytic Approach for Federated Learning with Pre-trained Models

The paper introduces **Analytic Federated Learning (AFL)**, a transformative training paradigm designed for [[Federated Learning]] (FL) utilizing [[pre-trained models]]. Moving away from traditional iterative gradient descent, AFL adopts a gradient-free approach that utilizes closed-form analytical solutions to achieve efficient model updates.

## Methodology
AFL is heavily inspired by the principles of [[Analytic Learning]], a technique that allows for training neural networks via analytical solutions within a single epoch. The framework operates through two primary stages:

1.  **Local Client Training**: AFL facilitates a single-epoch training process on the client side, effectively removing the need for the computationally expensive multi-epoch updates common in