---
title: "Don't Label Twice: Quantity Beats Quality when Comparing Binary Classifiers on a Budget"
created: 2024-05-22
source: "https://arxiv.org/abs/2402.02249"
tags: [binary classification, noisy labels, large deviations, machine learning benchmarking]
category: machine-learning
---

# Don't Label Twice: Quantity Beats Quality when Comparing Binary Classifiers on a Budget

In the field of [[machine learning]], determining whether one [[binary classifier]] outperforms another is a fundamental task. However, when researchers operate under a fixed budget for [[data labeling]], they face a critical strategic dilemma: Is it better to spend the budget on a small number of highly accurate, "clean" labels, or on a much larger pool of "noisy" labels?

## The Conventional Approach vs. New Findings

Traditionally, the standard practice for mitigating [[noisy labels]] involves collecting multiple labels for the same data point and using a [[majority vote]] to aggregate them into a single, more reliable label. This "quality-over-quantity" approach aims to reduce the error rate of the ground truth.

The paper "Don't Label Twice" presents a theorem that directly challenges this conventional wisdom. The authors prove that if the primary objective is specifically to **compare the accuracy** of two classifiers, the optimal strategy is to prioritize sample quantity over label precision. In other words, it is more effective to spend the budget on collecting a single, noisy label for as many different samples as possible, rather than spending that same budget to refine the labels of a smaller subset of data.

## Theoretical Framework

The mathematical foundation for this finding relies on a non-trivial application of [[Cramér's theorem]], a cornerstone of [[Large Deviation Theory]]. By analyzing the probability of deviations in the estimated error rates, the authors demonstrate that the increased sample size provides more statistical power than the reduction in label noise. Furthermore, the paper provides sample size bounds that are mathematically superior to those derived from the widely used [[Hoeffding's bound]].

## Implications for Machine Learning

These results have profound implications for the design of [[machine learning benchmarks]]. As the industry moves toward more automated and large-scale model evaluation, the methodology used to validate models may need to be redesigned. The research suggests that current benchmarks may be significantly less efficient than they could be, and that a shift toward larger, noisier datasets could lead to more robust and cost-effective model comparisons.