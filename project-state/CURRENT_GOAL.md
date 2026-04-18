# Current Sub-Goal

**Aim:** Aim 4 — Structure-based virtual screening on Cheaha HPC
**Task:** Task 4.1
**Legacy ID:** G-006
**Started:** 2026-04-18
**Tier:** cheaha (UAB HPC)

## Goal
Establish Cheaha workspace: home + scratch dirs, seed SMILES rsync
(top-500 by pChEMBL), conda env smoke-test on amperenodes partition.

## Definition of done
- [ ] SSH keyauth to cheaha.rc.uab.edu working (sshpiper, no VPN for login)
- [ ] `~/phgdh-sbdd/` dir initialised on Cheaha with seed SMILES
- [ ] conda env with rdkit + autodock + smina created
- [ ] `smoke_test.sbatch` submits + completes on express partition

## Dependencies
- UAB VPN (needed for compute beyond login)
- SSH key from MacBook or W0 uploaded to Cheaha
- `data/aim4_smiles/smiles_potency_sorted.tsv` (ready)

## Blocker note
Cheaha SSH access requires Jake's key — cannot proceed autonomously without
confirmation that the key is registered. Will attempt connectivity probe;
if it fails, enqueue a 🚨 to the Resolver.
