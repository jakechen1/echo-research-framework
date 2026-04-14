---
title: All elementary functions from a single binary operator
created: 2024-05-22
source: https://arxiv.org/abs/2603.21852
tags: [mathematics, symbolic-regression, computation, artificial-intelligence]
category: machine-learning
author: wiki-pipeline
dc.title: "All elementary functions from a single binary operator"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/all-elementary-functions-from-a-single-binary-operator.md
dc.language: en
dc.rights: CC-BY-4.0
---

# All elementary functions from a single binary operator

The paper "All elementary functions from a single binary operator" introduces a significant discovery in the field of computational [[artificial-intelligence-and-the-structure-of-mathematics|mathematics]]. In digital hardware, it is well-established that a single universal gate, such as NAND, is sufficient to construct all forms of [[logic|Boolean logic]]. However, in continuous mathematics, computing the standard repertoire of a scientific calculator—including [[transcendental functions]] like $\sin(x)$ and $\log(x)$—has traditionally required a variety of distinct, multi-input operations.

The authors present a new primitive known as the **EML (Exp-Minus-Log)** operator, defined as:
$$eml(x,y) = \exp(x) - \ln(y)$$

In conjunction with the constant $1$, this single binary operator is mathematically sufficient to generate the entire set of elementary functions. This includes basic [[arithmetic operations]] such as addition, subtraction, multiplication, division, and exponentiation, as well as fundamental constants such as $e$, $\pi$, and the imaginary unit $i$. For example, the researchers demonstrate that the exponential function can be simplified to $exp(x) = eml(x, 1)$, and the natural logarithm can be constructed through nested EML operations.

The discovery was achieved via a systematic exhaustive search rather than traditional analytical derivation. This approach revealed that all EML expressions can be represented as a uniform binary tree of identical nodes, governed by the simple grammar: $S \to 1 \mid eml(S, S)$.

The implications for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] are particularly profound, specifically for the field of [[Symbolic Regression]]. Because the EML structure is uniform, these trees can be used as trainable circuits. By employing [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|Gradient Descent]] and standard optimizers like [[flowadam-implicit-regularization-via-geometry-aware-soft-momentum-injection|Adam]], the authors demonstrated that it is possible to perform the exact recovery of closed-form elementary functions from numerical data at shallow tree depths (up to 4). This suggests a new paradigm for [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] where complex mathematical laws can be rediscovered through highly simplified, unified computational architectures.