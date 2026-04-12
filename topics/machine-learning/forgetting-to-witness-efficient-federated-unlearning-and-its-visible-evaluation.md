---
title: "Forgetting to Witness: Efficient Federated Unlearning and Its Visible Evaluation"
created: 2024-05-22
source: https://arxiv.org/abs/2604.04800
tags: [federated-learning, machine-unlearning, privacy-preserving, GAN, knowledge-distillation]
category: machine-learning
---

# Forgetting to Witness: Efficient Federated Unlearning and Its Visible Evaluation

As [[data-privacy|Data Privacy]] and security become paramount in the era of decentralized computing, the field of [[afl-a-single-round-analytic-approach-for-federated-learning-with-pre-trained-mod|Federated Learning]] faces a significant challenge: how to effectively remove the influence of specific data points once they are deleted. This paper, titled "Forgetting to Witness," introduces a pioneering pipeline designed to handle both the execution of [[an-illusion-of-unlearning-assessing-machine-unlearning-through-internal-represen|Machine Unlearning]] and the visible verification of that unlearning process.

## The Federated Unlearning Approach

The authors propose a novel approach to federated unlearning that prioritizes both computational efficiency and model accuracy. Traditional methods often require storing historical snapshots of models or datasets, which can be resource-intensive and potentially counterproductive to privacy goals. 

The proposed method eliminates the need for historical data storage. Instead, it utilizes [[geometric-limits-of-knowledge-distillation-a-minimum-width-theorem-via-superposi|Knowledge Distillation]] integrated with various optimization mechanisms. This allows the global model to "forget" specific client contributions while maintaining high performance on the remaining data, ensuring that the model's utility is not compromised by the unlearning operation.

## The Skyeye Evaluation Framework

A significant contribution of this research is the **Skyeye** framework, an evaluation system designed to provide a "visible" metric for forgetting capacity. One of the primary difficulties in unlearning is proving that the model has truly suppressed the information related to the deleted data.

Skyeye leverages the architecture of [[generative-adversarial-networks|Generative Adversarial Networks]] (GANs) to achieve this visibility:
1. **Integration**: The unlearning model is integrated into a GAN as the primary classifier.
2. **Training**: Both the classifier and the discriminator guide a generator to produce synthetic samples.
3. **Knowledge Extraction**: As the generator learns from the classifier, it begins to replicate features present in the training data.
4. **Visualization**: The generator produces samples that represent the "knowledge" held by the model.

The efficacy of the unlearning process is evaluated by measuring the statistical relevance between the original deleted data and the samples produced by the Skyeye generator. If the generated samples no longer resemble the deleted data, the unlearning is considered successful. Experimental results confirm that this pipeline provides a robust and interpretable method for maintaining privacy in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] ecosystems.