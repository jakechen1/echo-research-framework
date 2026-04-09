---
title: FedDAP: Domain-Aware Prototype Learning for Federated Learning under Domain Shift
created: 2024-05-22
source: https://arxiv.org/abs/2604.06795
tags: [Federated Learning, Domain Shift, Prototype Learning, Machine Learning]
category: ai, machine-learning
---

# FedDAP: Domain-Aware Prototype Learning for Federated Learning under Domain Shift

[[Federated Learning]] (FL) provides a decentralized framework for training models across multiple clients without the need to expose private, sensitive data. While ideal for privacy-preserving [[Machine Learning]], real-world FL applications often struggle with [[Domain Shift]], where data distributions vary significantly between different clients, causing a decline in global model accuracy.

## The Challenge of Domain Shift
One of the most promising solutions to address non-IID (independent and identically distributed) data is [[Prototype Learning]], which uses class-wise feature representations to capture essential data characteristics. However, current prototype-based FL methods suffer from two primary flaws:

1.  **Loss of Domain Information:** Existing methods typically aggregate local prototypes from all participants into a single, "one-size-fits-all" global prototype per class. This process destroys the unique features that distinguish one domain from another.
2.  **Domain-Agnostic Alignment:** Current training processes force all clients to align their local features with the same global prototype, regardless of their