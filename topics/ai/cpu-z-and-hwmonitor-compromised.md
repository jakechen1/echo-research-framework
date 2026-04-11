---
title: CPU-Z and HWMonitor compromised
created: 2026-04-10
source: https://www.theregister.com/2026/04/10/cpuid_site_hijacked/
tags: [cybersecurity, malware, supply-chain-attack, software-security]
category: technology
---

# CPU-Z and HWMonitor Compromised

Recent security intelligence indicates a critical [[supply chain attack]] involving the official website of CPUID, the developer of widely used system diagnostic utilities [[CPU-Z]] and [[HWMonitor]]. Reports from [[BleepingComputer]] and security researchers at [[vxunderground]] suggest that the CPUID website was hijacked to distribute malicious payloads disguised as legitimate software updates.

## Incident Overview

The compromise focuses on the integrity of the download pipeline. Attackers gained the ability to manipulate the files hosted on the official CPUID servers, effectively turning a trusted utility into a delivery mechanism for [[malware]]. Specifically, certain versions of [[HWMonitor]] (notably version 1.63) have been flagged as potentially containing malicious code. 

Users who download these installers directly from the compromised website may inadvertently install unauthorized software that facilitates remote access or data exfiltration on the host system.

## Community Response and Detection

The breach was brought to widespread attention through community monitoring on platforms such as [[Reddit]] and [[Hacker News]]. Security enthusiasts noticed discrepancies in file signatures and anomalous behavior in recent downloads. The incident has raised significant alarms within the [[cybersecurity]] community regarding the extreme vulnerability of essential system-level tools.

## Recommended Actions

1. **Cease Downloads:** Avoid downloading any software, installers, or updates directly from the official CPUID website until a formal cleanup and verification process is completed by the developer.
2. **Verify Integrity:** If you have recently updated these tools, compare the file hashes of your current installation against known legitimate hashes provided by trusted, uncompromised third-party archives.
3. **Scan Systems:** Run comprehensive scans using updated [[antivirus]] and [[endpoint-detection]] software on any machine that has recently executed installers from the CPUID site.
4. **Monitor Network Traffic:** Observe systems for unexpected outgoing connections or unauthorized network activity originating from system diagnostic processes.

As the situation evolves, security researchers continue to analyze the specific indicators of compromise (IoCs) associated with this breach.