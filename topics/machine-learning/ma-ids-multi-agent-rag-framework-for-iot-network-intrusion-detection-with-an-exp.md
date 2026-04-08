---
title: "MA-IDS: Multi-Agent RAG Framework for IoT Network Intrusion Detection with an Experience Library"
created: 2024-05-23
source: https://arxiv.org/abs/2604.05458
tags: [ai, machine-learning, iot, cybersecurity, rag, llm]
category: machine-learning
---

# MA-IDS

**MA-IDS** is an innovative Multi-Agent Intrusion Detection System designed to address the critical vulnerabilities of traditional [[Network Intrusion Detection Systems]] (NIDS) within [[Internet of Things]] (IoT) ecosystems. While traditional signature-based methods struggle with zero-day attacks and many [[Machine Learning]] models lack transparency, MA-IDS utilizes [[Large Language Models]] (LLMs) and [[Retrieability Augmented Generation]] (RAG) to provide a reasoning-driven approach to security.

## Architecture and Mechanism

The core of the framework is a self-building **Experience Library**, which utilizes a [[FAISS]]-based vector database to store historical detection data and rules. This allows for "continual learning" without the need to retrain the underlying language models. The system operates through the collaboration of two specialized autonomous agents:

*   **Traffic Classification Agent**: Before performing inference, this agent queries the Experience Library to retrieve relevant past error rules, grounding the LLM's reasoning in historical context.
*   **Error Analysis Agent**: This agent monitors classification outcomes. When misclassifications occur, it converts these errors into human-readable detection rules, which are then appended to the Experience Library for future retrieval.

## Performance and Impact

The framework was evaluated using the NF-BoT-IoT and NF-ToN-IoT benchmark datasets. The results demonstrate significant leaps in performance:
*   **NF-BoT-IoT**: Achieved a Macro F1-Score of 89.75%.
*   **NF-ToN-IoT**: Achieved a Macro F1-Score of 85.22%.

These results represent a massive improvement (over 72 and 80 percentage points, respectively) compared to zero-shot baselines. Notably, MA-IDS remains competitive with traditional [[Support Vector Machines]] (SVM) while providing a critical advantage: **explainability**. By providing rule-level explanations for every classification decision, MA-IDS offers a principled path toward [[Explainable AI]] (XAI) in highly heterogeneous and resource-constrained IoT environments.