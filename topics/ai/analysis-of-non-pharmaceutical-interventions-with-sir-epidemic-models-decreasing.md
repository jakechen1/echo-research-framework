---
title: Analysis of non pharmaceutical interventions with SIR epidemic models: decreasing the infection peak vs. minimizing the epidemic size
created: 2024-05-22
source: https://arxiv.org/abs/2604.08420
tags: [epidemiology, mathematical modeling, public health, SIR models]
category: biology
---

# Analysis of NPIs with SIR Epidemic Models

This article examines the impact of various [[analysis-of-non-pharmaceutical-interventions-with-sir-epidemic-models-decreasing|non-pharmaceutical interventions]] (NPIs) on the trajectory of infectious disease outbreaks using [[sir-models|SIR models]]. The research specifically investigates the optimization of two different public health objectives: reducing the peak number of concurrent infections (often referred to as "flattening the curve") and minimizing the total [[epidemic-size|epidemic size]] (the total number of people infected throughout the duration of the outbreak).

## Analytical Methodology

The study utilizes [[compartmental-models|compartmental models]] to derive analytical approximations for the critical points of the infection curve. By employing [[degree-based-mean-field-networks|degree-based mean-field networks]], the authors differentiate between two functional types of interventions:
* **Transmission Reduction:** Interventions focusing on individual or environmental measures designed to lower the transmission rate.
* **Contact Reduction:** Measures similar to [[lockdown-measures|lockdown measures]] that focus on decreasing the density of social interactions.

Through this framework, the researchers identified six distinct possible scenarios for how an epidemic evolves when a single NPI is introduced.

## Key Research Findings

The study presents several critical insights into the efficiency of NPIs:
1. **Efficiency of Measures:** When assuming an equal effect on the [[reproduction-number|reproduction number]], interventions that focus on reducing the transmission rate are more effective at minimizing the final epidemic size than those focused solely on reducing social contact.
2. **Peak vs. Size Dynamics:** The effectiveness of both types of NPIs fluctuates significantly when measuring their impact on primary versus secondary infection peaks.
3. **The Importance of Timing:** A vital conclusion is that minimizing the infection peak requires the implementation of NPIs much earlier than is required to minimize the total epidemic size.

## Implications for Public Health

These findings offer essential guidance for [[a-multi-agent-reinforcement-learning-framework-for-public-health-decision-analys|public health]] strategy. The results suggest that timing is just as critical as the type of intervention chosen. Effective management of healthcare capacity requires proactive, early-stage interventions to prevent the surge of peak infections, whereas late-stage interventions may still influence the total scale of the outbreak but will fail to prevent the healthcare system from being overwhelmed.