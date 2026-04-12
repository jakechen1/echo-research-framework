---
title: Revisulating Fairness Impossibility with Endogenous Behavior
created: 2024-05-23
source: https://arxiv.org/abs/2604.06378
tags: [algorithmic fairness, machine learning, decision theory, behavioral economics]
category: ai, machine-learning
---

# Revisiting Fairness Impossibility with Endogenous Behavior

The paper "Revisiting Fairness Impossibility with Endogenous Behavior" addresses a critical oversight in traditional [[algorithmic-fairness|algorithmic fairness]] literature: the assumption of fixed human behavior. Most current frameworks treat demographic behavioral differences as [[exogenous-features|exogenous features]], assuming that classification decisions do not alter the underlying patterns of the population. However, in high-stakes environments—such as [[legal-sentencing|legal sentencing]], credit scoring, or taxation—the consequences (or "stakes") attached to a classification can trigger strategic responses from individuals.

### The Problem of Endogenous Behavior
In real-world settings, people often adjust their actions in anticipation of how they will be classified. This is known as [[revisiting-fairness-impossibility-with-endogenous-behavior|endogenous behavior]]. When the consequences of an algorithmic decision (e.g., the size of a fine or the length of a sentence) influence how people act, the traditional mathematical models of fairness begin to break down.

The authors investigate the classic "impossibility results" in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]], specifically the fundamental incompatibility between [[error-rate-balance|error-rate balance]] and [[predictive-parity|predictive parity]]. Under the assumption of stagnant behavior, these two metrics cannot be satisfied simultaneously.

### Proposed Two-Stage Design
The research demonstrates that in an environment with strategic actors, this incompatibility can be resolved through a specific two-stage design:
1. **Statistical Standardization:** The [[a-giant-step-baby-step-classifier-for-scalable-and-real-time-anomaly-detection-i|classifier]] is first tuned to ensure statistical performance is balanced across different groups.
2. **Stake Adjustment:** The system then adjusts the "stakes" (the consequences attached to the decision) to induce comparable patterns of behavior across groups.

### New Ethical Tradeoffs
While this approach successfully bridges the gap between statistical error rates and parity, it introduces a new form of qualitative inequality. To achieve behavioral alignment, the system must treat groups differently by attaching different consequences to identical classification outcomes. 

This finding shifts the focus of [[automated-decision-making|automated decision-making]] research. The authors argue that fairness cannot be assessed solely by how an algorithm maps data to decisions. Instead, the human consequences of classification must be treated as primary design variables. Ultimately, the research highlights that solving technical disparities may inadvertently create new, complex forms of [[social-consequences|social consequences]] that require