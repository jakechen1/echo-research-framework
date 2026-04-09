title: Physics-Informed Functional Link Constrained Framework with Domain Mapping for Solving Bending Analysis of an Exponentially Loaded Perforated Beam
created: 2024-05-22
source: https://arxiv.org/abs/2604.07025
tags: [machine-learning, computational-mechanics, differential-equations, engineering]
category: machine-learning

# Physics-Informed Functional Link Constrained Framework

The article presents a sophisticated computational approach for analyzing the bending behavior of tapered perforated beams under exponential loading. The research focuses on the development and validation of the **Domain mapped physics-informed Functional link Theory of Functional Connection (DFL-TFC)** method, a novel framework designed to solve complex [[Differential Equations]] in structural engineering.

### Methodology

The governing equations for the perforated beam involve several critical parameters, including the filling ratio ($\alpha$), the number of hole rows ($N$), tapering parameters ($\phi$ and $\psi$), and the exponential loading parameter ($\gamma$). To address these complexities, the researchers proposed a framework that departs from traditional deep learning architectures. 

In the [[DFL-TFC]] framework, the standard hidden layers used in [[Machine Learning]] are replaced with a functional expansion block. This block utilizes [[Orthogonal Polynomial]] basis functions to enrich the input representation. A key innovation is the domain mapping technique, where the domain of the differential equation is mapped to the domain of the orthogonal polynomials.

To ensure that the physical constraints and boundary conditions are met with absolute precision, the method employs a **Constrained Expression (CE)**. This is constructed using the [[Theory of Functional Connections (TFC)]]. Within this CE, a [[Functional Link Neural Network (FLNN)]] serves as the "free function," learning to solve the unconstrained optimization problem that remains after the boundary conditions have been analytically satisfied.

### Comparative Results

The performance of the [[DFL-TFC]] framework was benchmarked against standard [[Physics-Informed Neural Networks (PINN)]]. The comparative study yielded several key findings:

*   **Convergence Speed:** The DFL-TFC method demonstrates significantly faster convergence rates than the [[PINN]] approach.
*   **Computational Efficiency:** The proposed framework reduces the overall computational cost required for high-fidelity simulations.
*   **Accuracy:** The DFL-TFC method provides superior solution accuracy, as validated against [[Numerical Analysis]] methods such as the Galerkin solution.

These results suggest that the integration of [[Theory of Functional Connections (TFC)]] with [[Machine Learning]] offers a powerful paradigm for solving high-order [[Engineering]] problems where boundary condition satisfaction is critical.