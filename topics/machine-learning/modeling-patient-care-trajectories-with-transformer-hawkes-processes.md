---
title: "Modeling Patient Care Trajectories With Transformer Hawkes Processes"
category: machine-learning
created: 2026-04-12
---

title: Modeling Patient Care Trajectories with Transformer Hawkes Processes
created: 2024-05-23
source: https://arxiv.org/abs/2604.05844
tags: [transformer, hawkes-process, healthcare-analytics, machine-learning]
category: machine-learning

# Modeling Patient Care Trajectories with Transformer Hawkes Processes

The research paper "Modeling Patient Care Trajectories with Transformer Hawkes Processes" (arXiv:2604.05844) addresses the complex challenge of analyzing longitudinal patient data. Healthcare utilization is characterized by irregularly time-stamped events, including [[outpatient-visits|outpatient visits]], [[inpatient-admissions|inpatient admissions]], and [[emergency-encounters|emergency encounters]]. These sequences, known as individual care trajectories, are difficult to model using standard [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] due to their temporal irregularity and the extreme [[class-imbalance|class imbalance]] inherent in medical datasets.

### The Transformer Hawkes Process Framework

To address these issues, the authors propose an architecture based on the [[modeling-patient-care-trajectories-with-transformer-hawkes-processes|Transformer Hawkes Process]]. This framework integrates the powerful history-encoding capabilities of the [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] architecture with the continuous-time dynamics of [[modeling-patient-care-trajectories-with-transformer-hawkes-processes|Hawkes processes]]. By combining these two methodologies, the model can effectively capture the complex event dependencies within a patient's history and jointly predict both the nature of the next medical event and the predicted [[time-to-event]].

### Overcoming Data Imbalance

A significant hurdle in clinical [[predictive-modeling|predictive modeling]] is the scarcity of high-impact, rare medical events compared to routine healthcare interactions. The researchers introduce an "