---
title: Cloudflare targets 2029 for full post-quantum security
created: 2024-05-23
source: https://blog.cloudflare.com/post-quantum-roadmap/
tags: [cryptography, cloudflare, cybersecurity, quantum-computing, network-security]
category: technology
---

# Cloudflare targets 2029 for full post-quantum security

Cloudflare has unveiled a strategic roadmap aimed at achieving comprehensive [[Post-Quantum Cryptography]] (PQC) across its global network by 2029. This initiative is designed to mitigate the existential threat that [[Quantum Computing]] poses to current global [[Cybersecurity]] standards.

## The Quantum Threat
Modern digital security relies heavily on asymmetric encryption protocols, such as [[RSA]] and [[Elliptic Curve Cryptography]] (ECC). While these methods are currently impenetrable by classical computers, the advent of large-scale quantum computers could allow for the execution of [[Shor's Algorithm]], which is capable of breaking these fundamental cryptographic primitives. 

A primary driver for this transition is the "Harvest Now, Decrypt Later" threat. Adversaries are currently intercepting and storing encrypted sensitive data, intending to decrypt it once quantum hardware becomes sufficiently powerful. To counter this, Cloudflare is prioritizing the migration of protocols that protect long-term data value.

## The Roadmap to 2029
Cloudflare's transition strategy focuses on a phased, "hybrid" implementation. Rather than a sudden replacement of existing standards—which could introduce new [[Network Security]] vulnerabilities—Cloudflare is integrating quantum-resistant algorithms alongside classical ones. This ensures that the security of a connection remains at least as strong as current standards, even if a new algorithm is later found to have a classical flaw.

Key elements of the roadmap include:
* **Algorithm Integration:** Implementing NIST-standardized algorithms, such as those based on lattice-based cryptography, into the [[TLS/SSL]] handshake process.
* **Infrastructure Scalability:** Updating [[Edge Computing]] nodes and [[CDN]] infrastructure to handle the increased computational overhead and larger key sizes associated with PQC.
* **Cryptographic Agility:** Enhancing the ability of Cloudflare's systems to rapidly pivot to new cryptographic primitives as the threat landscape evolves.

## Conclusion
The transition to a quantum-resistant internet is a massive logistical undertaking involving the global [[Digital Infrastructure]] ecosystem. Cloudflare's 2029 target represents a significant commitment to [[Cryptographic Agility]], providing a blueprint for how large-scale service providers can navigate the transition into the post-quantum era.