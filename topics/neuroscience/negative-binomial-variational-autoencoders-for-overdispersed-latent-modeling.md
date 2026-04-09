title: Negative Binomial Variational Autoencoders for Overdispersed Latent Modeling
created: 2024-05-22
source: https://arxiv.org/abs/2508.05423
tags: [vae, negative-binomial, neural-coding, latent-variable-models, overdispersion, generative-models]
category: machine-learning, neuroscience

# Negative Binomial Variational Autoencoders for Overdispersed Latent Modeling

The paper "Negative Binomial Variational Autoencoders for Overdispersed Latent Modeling" introduces **NegBio-VAE**, a novel architecture designed to bridge the gap between [[Machine Learning]]-based representations and the biological realities of [[Neuroscience]].

### The Problem of Biological Plausibility
Most modern [[Artificial Neural Networks]], specifically [[Variational Autoencoders]] (VAES), rely on continuous activation functions and continuous latent variables. While these are highly effective for many computer vision and language tasks, they lack biological plausibility because real neurons communicate via discrete, spike-based signaling. 

Previous attempts to move toward discrete models, such as the [[Poisson VAE]], introduce count-based latents. However, these models are fundamentally limited by the Poisson assumption, where the mean is equal to the variance. In real-world neural spike data, "overdispersion"—a phenomenon where the variance exceeds the mean—is a widespread and critical feature. Failure to capture this dispersion leads to less expressive and less informative latent representations.

### The NegBio-VAE Approach
To address these limitations, the authors propose **NegBio-VAE**, a negative-binomial latent-variable model. By incorporating a dedicated dispersion parameter, the model can flexibly capture the overdispersed nature of spike counts. 

Key technical contributions include:
* **Novel KL Estimation:** New methods for estimating Kullback-Leibler divergence in a discrete-count context.
* **Reparameterization:** Advanced reparameterization techniques that ensure training feasibility and gradient stability during backpropagation.

### Experimental Results and Performance
Experiments conducted on four distinct datasets demonstrate that NegBio-VAE consistently outperforms competing single-layer VAE baselines in both reconstruction and generative performance. Furthermore, the model yields robust, informative latent representations that are highly effective for various downstream tasks. Extensive ablation studies were performed to verify that the model's success is directly tied to its ability to handle the dispersion characteristics of neural data.

The codebase for NegBio-VAE is available via the authors' GitHub repository.