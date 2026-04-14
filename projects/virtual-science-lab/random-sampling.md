---
title: "Random Sampling"
created: 2026-04-12
category: machine-learning
tags: [statistics, data-science, experimental-design, methodology]
source_urls:
  - "https://pubmed.ncbi.nlm.nih.gov/22951546/"
  - "https://pubmed.ncbi.nlm.nih.gov/2647799/"
  - "https://pubmed.ncbi.nlm.nih.gov/9973070/"
author: wiki-dashboard
dc.title: "Random Sampling"
dc.creator: wiki-dashboard
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: projects/virtual-science-lab/random-sampling.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Random Sampling

**Random sampling** is a fundamental technique in statistics and [[machine-learning]] used to select a subset of individuals (a sample) from a larger group (a population) such that every member of the population has a known, non-zero probability of being selected. The primary objective of random sampling is to ensure that the sample is representative of the population, thereby allowing researchers to make valid inferences about the whole from the observed part. In the context of experimental design, such as the methodologies discussed in [[Freeman S et al., 2014]], random sampling is critical for mitigating selection bias and ensuring that the observed effects are not the result of systematic errors in data collection.

## Core Principles and Mechanisms

The power of random sampling lies in its ability to approximate the underlying distribution of a population without the need to observe every single data point. This is particularly vital in modern [[machine-learning]] workflows, where datasets often reach petabyte scales, making exhaustive processing computationally prohibitive.

At its core, random sampling relies on the principle of **stochasticity**. By introducing randomness, the researcher removes human subjectivity and systematic preference from the selection process. This facilitates the law of large numbers, which suggests that as a sample size grows, its characteristics will more closely resemble those of the population.

### Probability of Selection
A key distinction in sampling theory is between probability sampling and non-probability sampling. In probability sampling, the probability of any member being chosen is quantifiable. This allows for the calculation of **sampling error**—the discrepancy between the sample statistic and the true population parameter. Without a known probability of selection, the ability to apply frequentist or Bayesian inferential frameworks is significantly compromised.

## Common Methods of Random Sampling

Different research objectives and population structures necessitate different sampling strategies. The choice of method directly impacts the variance of the estimates and the potential for bias.

### 1. Simple Random Sampling (SRS)
Simple Random Sampling is the most basic form of sampling, where every individual in the population has an equal chance of being selected. This is typically achieved using a random number generator applied to a list of the population (a sampling frame). While SRS is the gold standard for minimizing bias, it can be inefficient if the population is highly heterogeneous.

### 2. Stratified Random Sampling
Stratified sampling involves dividing the population into mutually exclusive subgroups, known as **strata**, based on specific characteristics (e.g., age, gender, or income). A random sample is then drawn from each stratum. This method is particularly effective when the researcher wants to ensure that minority subgroups are adequately represented. In clinical and experimental research, the nuances of this method are well-documented; for instance, [[Kernan WN et al., 1999]] discusses how stratified randomization is employed in clinical trials to balance known prognostic factors across treatment groups, thereby reducing experimental error.

### 3. Cluster Sampling
Cluster sampling is used when the population is naturally divided into groups, or "clusters" (e.g., schools, cities, or hospital wards). Instead of sampling individuals, the researcher randomly selects entire clusters. This is often more logistically feasible and cost-effective than SRS. However, it introduces a "design effect" where observations within a cluster may be more similar to each other than to the rest of the population, potentially increasing sampling error. The complexities of this approach, especially in the context of large-scale trials, are explored in the [[Campbell MK et al., 2012]] statement regarding the extension of CONSORT to cluster randomized trials.

### 4. Systematic Sampling
In systematic sampling, researchers select elements from an ordered population using a fixed, periodic interval (e.g., selecting every $k$-th person from a list). While computationally efficient, it carries the risk of **periodicity bias** if the sampling interval coincides with a hidden pattern in the data.

## Random Sampling in Machine Learning

In the domain of [[machine-learning]], random sampling is not merely a data collection tool but a core component of the model training and evaluation pipeline.

### Data Partitioning and Cross-Validation
The most ubiquitous application of random sampling in ML is the division of a dataset into **training**, **validation**, and **test** sets. A random split ensures that the model's performance is evaluated on data that is statistically similar to the training data. To mitigate the risk of a "lucky" or "unlucky" split, techniques like **k-fold cross-validation** are used. In k-fold CV, the dataset is randomly partitioned into $k$ subsets, and the model is trained $k$ times, each time using a different subset as the validation set and the remaining $k-1$ subsets as the training set.

### Handling Class Imbalance
In many real-world scenarios, such as fraud detection or rare disease diagnosis, the target class is significantly underrepresented. Random sampling techniques are adapted here through:
*   **Random Undersampling:** Removing instances from the majority class.
*   **Random Oversampling:** Duplicating instances from the minority class.
*   **Synthetic Data Generation:** Using algorithms like SMOTE (Synthetic Minority Over-sampling Technique) to create new, "randomly" interpolated examples.

### Importance Sampling
In reinforcement learning and large-scale generative modeling, **importance sampling** is a technique used to estimate properties of a particular distribution using samples drawn from a different distribution. By weighting the samples, researchers can correct for the discrepancy between the sampling distribution and the target distribution, a concept essential for the convergence of many stochastic gradient descent (SGD) variants.

## Challenges and Limitations

Despite its utility, random sampling is subject to several critical challenges:

### 1. Sampling Bias and Representativeness
The greatest threat to random sampling is when the "random" process is flawed. If the sampling frame is incomplete (e.g., excluding individuals without internet access from an online survey), the resulting sample will suffer from **undercoverage bias**. As noted in the literature regarding experimental outcomes, distinguishing between the act of random sampling (selecting the subjects) and **randomization** (assigning treatments) is vital for ensuring group equivalence and avoiding confounding variables [[Hsu LM et al., 1989]].

### 2. Sampling Error and Variance
Even with perfect sampling, a sample is only an approximation. The variance of the sample estimate decreases as the sample size $n$ increases, typically at a rate of $1/\sqrt{n}$. In high-dimensional [[machine-learning]] tasks, the amount of data required to achieve a low-variance estimate can be astronomically high, leading to the "curse of dimensionality."

### 3. Computational Scalatibility
In the era of Big Data, traditional sampling methods can become a bottleneck. Generating truly independent and identically distributed (i.i.d.) samples from a stream of massive data requires sophisticated reservoir sampling algorithms to ensure that the sample remains representative as the stream evolves.

## Future Directions

As we move deeper into the 2020s, the evolution of random sampling is being driven by three primary frontiers:

1.  **Active Learning:** Instead of random sampling, researchers are developing algorithms that "sample" the most informative points from an unlabeled pool. This direction seeks to minimize the cost of labeling by focusing only on the most "uncertain" or "difficult" examples.
2.  **Differentially Private Sampling:** With increasing scrutiny on data privacy, new sampling methodologies are being developed to ensure that the act of sampling does not inadvertently leak sensitive information about individual members of the population.
3.  **Automated Sampling in AutoML:** Future frameworks will likely include self-tuning sampling strategies that automatically detect population drift and adjust stratification or cluster parameters without human intervention, ensuring robust model performance in non-stationary environments.

## Summary Table of Sampling Methods

| Method | Description | Primary Advantage | Primary Risk |
| :--- | :--- | :--- | :--- |
| **Simple Random** | Every member has equal probability. | Unbiased; easy to implement. | High variance in small samples. |
| **Stratified** | Population divided into strata; sample from each. | High representativeness; lower variance. | Requires prior knowledge of strata. |
| **Cluster** | Groups (clusters) are selected randomly. | Cost-effective for large geographies. | High design effect/intra-cluster correlation. |
| **Systematic** | Selection based on a fixed interval $k$. | Computationally efficient. | Periodicity/pattern bias. |

## References

*   Campbell MK et al., 2012. Consort 2010 statement: extension to cluster randomised trials. BMJ. [https://pubmed.ncbi.nlm.nih.gov/22951546/](https://pubmed.ncbi.nlm.nih.gov/22951546/)
*   Hsu LM et al., 1989. Random sampling, randomization, and equivalence of contrasted groups in psychotherapy outcome research. J Consult Clin Psychol. [https://pubmed.ncbi.nlm.nih.gov/2647799/](https://pubmed.ncbi.nlm.nih.gov/2647799/)
*   Kernan WN et al., 1999. Stratified randomization for clinical trials. J Clin Epidemiol. [https://pubmed.ncbi.nlm.nih.gov/9973070/](https://pubmed.ncbi.nlm.nih.gov/9973070/)