---
title: From Scalars to Tensors: Declared Losses Recover Epistemic Distinctions That Neutrosophic Scalars Cannot Express
created: 2024-05-22
source: https://arxiv.org/abs/2604.09602
tags: [LLM, Neutrosochic Logic, Epistemic Uncertainty, AI Evaluation, Hyper-truth]
category: [ai, machine-learning]
dc.title: "From Scalars to Tensors: Declared Losses Recover Epistemic Distinctions That Neutrosophic Scalars Cannot Express"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/from-scalars-to-tensors-declared-losses-recover-epistemic-distinctions-that-neut.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# From Scalars to Tensors: Declared Losses Recover Epistemic Distinctions

## Overview
This paper investigates the limitations of using scalar-based [[Neutrosophic Logic]] to represent the [[Epistemic Uncertainty]] of [[Large Language Models]] (LLMs). Building on the framework of Truth (T), Indeterminacy (I), and Falsity (F), the research addresses how modern AI can better communicate the nuances of what it does and does not know.

## The Hyper-Truth Phenomenon
The study expands upon previous research by Leyva-Vázquez and Smarandache, which identified "hyper-truth"—a state where the sum of T, I, and F exceeds 1.0 (T + I + F > 1.0). By testing five major model families from vendors including [[Anthropic]], [[Meta]], [[DeepSeek]], [[Alibaba]], and [[Mistral]], the authors found that hyper-truth occurs in 84% of unconstrained evaluations. This confirms that the phenomenon is a cross-vendor characteristic of current [[Artificial Intelligence]] architectures when evaluated under specific protocols.

## The Problem of Scalar Collapse
The researchers identify a significant flaw in using purely scalar T/I/F values: the "Absorption" position. In scenarios where a model outputs (T=0, I=1, F=0), the scalar values become identical for fundamentally different epistemic states, such as a