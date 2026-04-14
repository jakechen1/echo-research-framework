---
title: Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences
created: 2024-05-24
source: https://arxiv.org/abs/2604.05953
tags: [voting-theory, algorithms, computational-social-choice, human-ai-collaboration]
category: technology
author: wiki-pipeline
dc.title: "Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/polynomial-time-algorithm-for-thiele-voting-rules-with-voter-interval-preference.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences

The paper "Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences" presents a significant breakthrough in the field of [[Computational Social Choice]]. The research provides a polynomial-time algorithm for computing an optimal committee of size $k$ under any given [[polynomial-time-algorithm-for-thiele-voting-rules-with-voter-interval-preference|Thiele voting rules]]. This is specifically achieved within the "Voter Interval domain," a setting where voters can be ordered such that each candidate is approved by a consecutive sequence of voters.

## Problem Context
For over a decade, finding optimal committees under specific scoring rules has remained an open challenge. This research resolves a problem originally posed for [[Proportional Approval Voting]] (PAV) and later extended to all Thiele rules. The complexity of these problems traditionally stems from the difficulty of selecting a subset of candidates that maximizes a specific scoring sequence across diverse voter preferences.

## Technical Contributions
The authors introduce a novel structural result: a **concavity theorem for families of intervals**. This theorem proves that if two solutions of different sizes exist, a solution of any intermediate size can be constructed such that its score is at least the linear interpolation of the two original scores. Consequently, the optimal total Thiele score functions as a concave function of the committee size.

To implement this, the researchers utilize an optimization framework based on [[Lagrangian relaxation]] of a natural [[Integer Linear Programming]] (ILP) formulation. By moving the cardinality constraint into the objective function, they demonstrate that the resulting constraint matrix is [[Total unimodularity]]. This property is crucial as it allows the problem to be solved efficiently in polynomial time.

## Human-AI Collaboration
A unique aspect of this paper is the methodology of its discovery. The authors report that the primary algorithm and its formal proof were developed through [[Human-AI Collaboration]]. Notably, a simplified version of the main structural theorem used in the algorithm was derived through a single interaction with the [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] model, Gemini Deep Think.

## Related Topics
* [[Algorithm Design]]
* [[Social Choice Theory]]
* [[a-firefly-algorithm-for-mixed-variable-optimization-based-on-hybrid-distance-mod|Optimization]]
* [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]