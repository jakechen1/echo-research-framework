---
title: "An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.08271"
tags: [machine unlearning, feature representation, neural collapse, model evaluation, AI safety]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/an-illusion-of-unlearning-assessing-machine-unlearning-through-internal-represen.md
dc.language: en
dc.rights: CC-BY-4.0
---

# An Illusion of Unlearning? Assessing Machine Unlearning Through Internal Representations

This research investigates a fundamental flaw in current [[an-illusion-of-unlearning-assessing-machine-unlearning-through-internal-represen|Machine Unlearning]] (MU) methodologies. While contemporary techniques have demonstrated success in altering a model's output-level behavior—effectively making it "forget" specific classes or datasets—this paper argues that such erasure is often superficial and potentially illusory.

## The Phenomenon of Misalignment

The authors identify a critical phenomenon termed [[Feature-Classifier Misalignment]]. Most state-of-the-art MU methods focus on modifying the final layer of a neural network to suppress the predicted probability of certain classes. However, the researchers discovered that the underlying [[Internal Representations]] (the hidden features) within the model remain largely intact and highly discriminative. 

As a result, the "forgotten" information is not truly deleted; it is merely disconnected from the final classifier. This creates a vulnerability where simple [[convolearn-a-dataset-for-fine-tuning-dialogic-ai-tutors|Fine-tuning]] can inadvertently reintroduce the erased concepts by re-aligning the features with a new classifier.

## Evidence via Linear Probing

To prove that information persists within the network, the study employs [[Linear Probing]]. By training a simple linear layer on the frozen weights of an "unlearned" model, the researchers were able to recover near-original accuracy for the supposedly forgotten classes. This demonstrates that the latent features still encode the prohibited information, rendering purely output-centric evaluation metrics insufficient.

The paper also references [[Neural Collapse]], noting that since the original model's features are highly structured, adjusting only the classifier allows for significant "forgetting" at the output level while leaving the true knowledge of the model untouched.

## Proposed Solution: CMF Classifier

To rectify this, the paper proposes a new unlearning paradigm based on the [[Class-Mean Features (CMF) Classifier]]. Unlike previous methods, CMF-based unlearning explicitly enforces alignment between features and classifiers. By targeting the feature-level distribution, this method ensures that the unlearned information is actually removed from the model's representations, rather than just masked at the output.

## Conclusion

This work highlights a vital need for more rigorous [[Representation-level Evaluation]] in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] security. Achieving true privacy and data deletion requires moving beyond output-level behavior to ensure that information is purged from the model's fundamental architecture.