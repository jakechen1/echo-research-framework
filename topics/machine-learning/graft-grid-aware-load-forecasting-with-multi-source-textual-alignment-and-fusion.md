---
title: GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion
created: 2024-05-22
source: https://arxiv.org/abs/2512.14400
tags: [machine-learning, power-grid, time-series-forecasting, natural-language-processing]
category: machine-learning
---

# GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion

**GRAFT** (GRid-Aware Forecasting with Text) is an advanced [[Machine Learning]] framework designed to enhance the accuracy of electric load forecasting within [[Power Grid]] management. While traditional load forecasting relies heavily on numerical data like weather and calendar rhythms, GRAFT introduces the integration of unstructured textual data to capture the impact of sudden socio-political events and policy changes.

## Architecture and Methodology

Building upon the STanHOP architecture, GRAFT implements a sophisticated approach to multi-source data integration. The framework focuses on two primary technical innovations:

1.  **Multi-Source Textual Alignment**: The model strictly aligns daily-aggregated textual inputs—including news reports, social media updates, and policy documents—with high-resolution, half-hour load data.
2.  **Text-Guided Fusion**: Utilizing [[Cross-Attention]] mechanisms, GRAFT realizes a fusion process that maps textual information to specific temporal positions. This occurs during both the training phase and the rolling forecasting phase, ensuring that the model captures temporal dependencies between text and load.

Furthermore, GRAFT features a plug-and-play external-memory interface. This design allows for the seamless addition of different information sources, making the model highly adaptable for various real-world industrial deployments.

## Benchmark and Experimental Results

The researchers have released a comprehensive, unified aligned benchmark covering the period from 2019 to 2021. The dataset encompasses five Australian states and includes:
*   Half-hour load measurements.
*   Daily-aligned weather and calendar variables.
*   Three distinct categories of external textual data.

Systematic evaluations across hourly, daily, and monthly scales demonstrate that GRAFT significantly outperforms strong baselines and reaches or surpasses current [[State-of-the-Art]] (SOTA) benchmarks across multiple regions and forecasting horizons.

## Key Contributions

*   **Event Robustness**: GRAFT remains highly accurate during event-driven scenarios where sudden textual shifts (like policy announcements) occur.
*   **Interpretability**: Through the use of attention read-outs, the model enables temporal localization and source-level interpretation, providing insights into how specific news or social media trends influence future load predictions.