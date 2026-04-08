---
title: Task-Centric Personalized Federated Fine-Tuning of Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.00050
tags: [Federated Learning, Large Language Models, Machine Learning, Clustering, Personalization]
category: machine-learning
---

# Task-Centric Personalized Federated Fine-Tuning of Language Models

The paper "Task-Centric Personalized Federated Fine-Tuning of Language Models" introduces **FedRouter**, a novel framework designed to optimize the training of [[Language Models]] within a [[Federated Learning]] (FL) ecosystem. 

## The Challenge of Heterogeneity
While [[Federated Learning]] is a powerful technique for training models on distributed, private datasets, it faces significant hurdles when dealing with "client heterogeneity." When clients possess data from diverse and different tasks, aggregating their models into a single global model often degrades the performance of individual participants. 

Existing [[Personalized Federated Learning]] (pFL) approaches attempt to tailor models to each specific client. However, the authors identify two critical limitations in current pFL methodologies:
1. **Poor Generalization**: The models struggle to remain effective when encountering unseen tasks or sudden shifts in data distributions.
2. **Intra-client Task Interference**: When a single client's dataset contains multiple distinct distributions, the local training process can suffer from conflicting gradients, leading to interference between tasks.

## The FedRouter Solution
To address these bottlenecks, the researchers propose **FedRouter**, a clustering-based pFL approach that shifts the architectural focus from a client-centric model to a **task-centric** model. Instead of building a unique model for every user, FedRouter builds specialized models for each identified task.

The framework utilizes [[Adapters]] to personalize the models through a dual-layer [[Clustering]] mechanism:
* **Local Clustering**: This layer associates specific adapters with individual task data samples within a single client's local dataset.
* **Global Clustering**: This layer identifies and aggregates similar adapters discovered across different clients, allowing the system to construct a shared, task-centric global model.

To handle inference, the authors implemented an **evaluation router mechanism**. This mechanism analyzes incoming test samples and routes them to the most compatible adapter based on the previously established clusters.

## Experimental Results
Experiments conducted on multi-task datasets demonstrate that FedRouter provides superior resilience compared to existing pFL methods. The framework achieved a 6.1% relative improvement under conditions of high task interference and a remarkable 136% relative improvement in [[Generalization]] evaluation, demonstrating its potential for large-scale, multi-task distributed learning.