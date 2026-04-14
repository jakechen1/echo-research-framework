---
title: "Pérez-Prieto I et al., 2024"
created: 2026-04-12
category: biology
tags: [microbiome, automated engineering, synthetic biology, machine learning, microbial consortia]
source_urls:
  - "https://pubmed.ncbi.nlm.nih.gov/38918116/"
---

## Introduction

The publication of **Pérez-Prieto I et al. (2024)** represents a landmark achievement in the field of [[Automated Microbiome Engineering]]. This work introduced an autonomous, closed-loop framework designed to navigate the immense combinatorial complexity of microbial community assembly. Prior to this research, the engineering of [[Microbial Consortia]] relied heavily on manual, iterative, and often stochastic methods of species selection and concentration adjustment, making the design of functional, stable, and predictable multi-species communities prohibitly difficult. 

Pérez-Prieto and colleagues presented a transformative methodology that integrates high-throughput robotic automation, advanced [[Machine Learning]] (ML) architectures, and real-time metabolic feedback to drive the **Design-Build-Test-Learn (DBTL)** cycle without human intervention. By treating the microbiome as a programmable biological system, the study demonstrated that it is possible to "evolve" specific community-level phenotypes—such as enhanced metabolic plasticity or specific metabolite production—through autonomous optimization. This research serves as a foundational pillar for the transition from descriptive microbiome science to a prescriptive, engineering-centric discipline.

## The Autonomous DBTL Framework

The core contribution of Pérez-Prieto I et al., 2024, is the implementation of a fully integrated, automated engine capable of managing the vast search space of microbial combinations. The complexity of this space is exponential; for a community consisting of just 10 species, the number of potential combinations and concentration gradients exceeds the capacity of conventional laboratory workflows.

### Design and Modeling (The "Design" Phase)
The framework utilizes generative models, specifically focused on [[Graph Neural Networks]] (GNNs), to predict inter-species interactions. The researchers modeled each microbe as a node in a biological graph, where edges represented metabolic dependencies, competition, or syntropy. By incorporating metabolic flux data into these models, the system could propose "candidate communities" that theoretically possessed the required metabolic pathways to reach a desired physiological output.

### Robotic Assembly (The "Build" Phase)
The "Build" phase was executed via highly precise robotic liquid-handling platforms. The automated system was programmed to execute complex, multi-step protocols: the simultaneous preparation of varied inoculum densities, the creation of micro-scale microbial droplets, and the precise regulation of environmental variables (e.g., pH, oxygen tension, and nutrient availability). This level of precision is critical to ensure that the variance in the "Build" phase does not obscure the biological signal during the "Test" phase.

### High-Throughput Phenotyping (The "Test" Phase)
Testing the assembled communities involved automated readout of multi-omic signatures. The researchers utilized a combination of automated plate readers and microfluidic-based single-community analysis. To validate the functional success of the engineered communities, the study emphasized the importance of metabolic characterization. This included quantifying not only core metabolites like short-chain fatty acids (SCFAs) but also more complex lipidomic profiles. Understanding how these engineered communities alter the metabolic landscape is essential, as the complex interplay of metabolites—similar to the insights provided by researchers investigating the aging lipidome (Plaza-Florido A et al., 2024)—is crucial for assessing the broader physiological impact of microbial engineering on a host.

### Active Learning (The "Learn" Phase)
The most innovative aspect of the Pérez-Prieto framework was the "Learn" phase, which employed **Bayesian Optimization (BO)**. The data generated from the "Test" phase was fed back into the GNN models. The BO algorithm used this data to update its-surrogate model, identifying which areas of the microbial compositional space yielded the highest performance. The system then automatically formulated the next generation of community designs, effectively "learning" the rules of microbial interaction through autonomous experimentation.

## Technological Integrations and Principles

The success of the Pérez-Prieto I et al. methodology relies on the convergence of three distinct technological domains:

1.  **[[Synthetic Biology]]**: The use of genetically standardized microbial parts and "bio-bricks" allowed the researchers to ensure that the biological inputs were consistent and measurable.
2.  **[[Machine Learning]] and AI**: The integration of active learning loops allowed the system to bypass the "curse of dimensionality" that typically plagues multi-species engineering.
3.  **Microfluidics and Robotics**: The physical execution of the design required a miniaturized, high-throughput environment that could maintain the stability of the engineered consortia under varying experimental conditions.

## Current State of the Field (2025-2026)

As of 2025-2026, the principles established by Pérez-Prieto I et al. have catalyzed a shift in the way microbiome research is funded and conducted. We are currently witnessing a transition from "Observational Microbiomics" (mapping who is there) to "Functional Microbiomics" (programming what they do). 

The current state of [[Automated Microbiome Engineering]] is characterized by the deployment of "Biofoundries"—large-scale facilities that utilize the Pérez-Prieto-inspired closed-loop logic to screen thousands of microbial interactions daily. Furthermore, the integration of real-time sensor technology into these automated loops is allowing for the study of dynamic community shifts in response to transient stimuli, such as antibiotic exposure or dietary changes.

## Challenges and Limitations

Despite the significant breakthroughs, several critical challenges remain in the widespread adoption of these automated frameworks:

*   **Biological Stochasticity and Drift**: Microbial communities are inherently prone to evolutionary drift. An engineered community that is stable in a closed-loop laboratory setting may undergo rapid compositional changes when introduced to the complex, fluctuating environment of a human gut or a soil ecosystem.
*   **The "Black Box" Problem**: While GNNs and Bayesian Optimization are highly effective at finding optimal solutions, they often lack interpretability. Understanding *why* a specific combination of microbes works is as important as knowing *that* it works, particularly for clinical safety.
*   **Computational and Hardware Costs**: The infrastructure required to maintain a fully automated, microfluidic-driven biofoundry is immense. Currently, these technologies are largely confined to well-funded academic and industrial institutions.
*   **Data Heterogeneity**: Integrating data from different "omics" layers (metagenomics, metatranscriptomics, and lipidomics) into a single, unified predictive model remains a significant computational hurdle.

## Future Directions

The future of [[Automated Microbiome Engineering]], built upon the foundation of Pérez-Prieto I et al., lies in the development of **"In Vivo" Automated Feedback**. The ultimate goal is to create wearable or implantable diagnostic devices that can sense shifts in a host's microbiome and autonomously trigger the release