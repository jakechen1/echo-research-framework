---
title: "CID-TKG: Collaborative Historical Invariance and Evolutionary Dynamics Learning for Temporal Knowledge Graph Reasoning"
created: 2024-05-22
source: https://arxiv.org/abs/2604.09600
tags: [temporal knowledge graphs, reasoning, machine learning, evolutionary dynamics, contrastive learning]
category: ai, machine-learning
dc.title: "CID-TKG: Collaborative Historical Invariance and Evolutionary Dynamics Learning for Temporal Knowledge Graph Reasoning"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/cid-tkg-collaborative-historical-invariance-and-evolutionary-dynamics-learning-f.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# CID-TKG: Collaborative Historical Invariance and Evolutionary Dynamics Learning

The paper **"CID-TKG: Collaborative Historical Invariance and Evolutionary Dynamics Learning for Temporal Knowledge Graph Reasoning"** introduces a novel framework designed to advance the field of [[Temporal Knowledge Graph Reasoning]] (TKGR).

## Problem Statement
[[Temporal Knowledge Graphs]] (TKGs) represent information where entities and relations change over time. The goal of TKGR is to infer future facts at unseen timestamps. However, existing [[machine learning]] approaches often suffer from significant limitations due to their reliance on time-invariant or weakly time-dependent structures. These models frequently overlook the critical [[evolutionary dynamics]]—the short-term shifts and transitions that define temporal data.

## The CID-TKG Framework
To overcome these hurdles, the researchers proposed **CID-TKG**, a collaborative learning framework. The core innovation lies in its use of a dual-graph architecture to establish a more effective [[inductive bias]] for reasoning. The framework operates through two specialized components:

1.  **Historical Invariance Graph**: This graph is engineered to capture long-term structural regularities and patterns that persist across the dataset.
2.  **Evolutionary Dynamics Graph**: This graph focuses on modeling short-term temporal transitions, capturing the fluid nature of how relations evolve.

## Methodology and Alignment
A primary challenge in dual-structure modeling is the presence of semantic discrepancies between the historical and evolutionary views. To solve this, CID-TKG utilizes dedicated encoders and a [[contrastive learning]] objective. The process involves:
*   Decomposing relations into view-specific representations.
*   Aligning view-specific query representations through a contrastive objective.

This alignment strategy promotes cross-view consistency and is specifically designed to suppress view-specific noise, ensuring that the learned representations are robust.

## Conclusion
Experimental results indicate that CID-TKG achieves state-of-the-art performance. The model is particularly effective in [[extrapolation]] settings, demonstrating a superior ability to predict future events in entirely new time periods compared to previous benchmarks.