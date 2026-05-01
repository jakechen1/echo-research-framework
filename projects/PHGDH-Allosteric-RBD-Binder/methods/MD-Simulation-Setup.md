---
title: "MD Simulation Setup — PHGDH SepTop Relative-Absolute Binding FE"
created: 2026-05-01
project: PHGDH-Allosteric-RBD-Binder
iteration: 6
category: methods
author: jakeclaw
tags: [methods, fep, openfe, septop, openmm, nagl]

> **Canonical:** [](https://github.com/jakechen1/phgdh-scavenger/blob/main/methods/MD-Simulation-Setup.md)  
> This wiki copy is mirrored for cross-project visibility from the dashboard. Edits should land in  first.

---

# MD Simulation Setup

## 1. Overview

We compute the relative binding free energy ΔΔG between a fixed
reference ligand (K4T, the cocrystal binder of PHGDH from PDB 6RIH)
and each de novo candidate from the iter-5 RL-tuned SELFIES transformer.
The end result, ΔΔG = ΔG_bind(candidate) − ΔG_bind(K4T), is anchored
to K4T's experimentally known IC₅₀ (∼µM, Pacold et al. 2016, taken as
ΔG_bind(K4T) ≈ −8 kcal/mol) to recover absolute ΔG_bind for each candidate.

We use the **separated-topology (SepTop) protocol** in OpenFE 1.11
(`openfe.protocols.openmm_septop.SepTopProtocol`) because it does not
require atom-level mapping between ligand pairs — the de novo
candidates share no scaffold with K4T, so dual-topology RBFE is
infeasible. SepTop places both ligands in the same simulation box
spatially separated by an alchemical bias, and λ swaps which one
interacts with the protein.

## 2. System preparation

### 2.1 Receptor

| Field | Value |
|---|---|
| Source PDB | **6RIH**, chain A |
| Resolution | 2.30 Å (X-ray) |
| Pocket | Allosteric site at RNA-binding domain, centred (14.84, −11.84, 73.28) Å |
| Box size (Vina) | 20 × 20 × 20 Å (used for orienting candidate placement) |
| Heterogen handling | All non-protein atoms removed (water, K4T cocrystal, ions); replaced with explicit solvent |
| Missing atoms / hydrogens | Filled by **PDBFixer** at pH 7.4 |
| Output | `6rih_chainA_protein_omm.pdb` (OpenMM-grade, 370 KB) |

### 2.2 Reference ligand K4T

Fetched from RCSB as the canonical idealised SDF
(`https://files.rcsb.org/ligands/download/K4T_ideal.sdf`) on first
run; cached thereafter. 33 heavy atoms; explicit stereochemistry
preserved.

### 2.3 Candidate ligands

Top-10 BBB-passing candidates from iter-5 RL output
(`top200_bbb_passing.csv`), ranked by composite score
(2·affinity + qed + novelty + 0.5·druglike_pass).

For each candidate:

```python
mol = Chem.MolFromSmiles(smi)
mol = Chem.AddHs(mol)
AllChem.EmbedMolecule(mol, randomSeed=42, useRandomCoords=True)
AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
Chem.AssignStereochemistryFrom3D(mol)        # resolve undefined stereo
# translate centroid to pocket centre (14.84, -11.84, 73.28)
```

The `AssignStereochemistryFrom3D` step is required: ETKDG-embedded
RDKit Mols can carry undefined chiral centres which OpenFF Toolkit
rejects with `UndefinedStereochemistryError`. Using the embedded
3D coords as ground truth, every chiral atom gets an explicit tag.

## 3. Force fields and parameterisation

### 3.1 Protein

Amber14SB (`amber/ff14SB.xml` via OpenMM `app.ForceField`).

### 3.2 Ligand

OpenFF Sage 2.2.0 (`openff-2.2.0.offxml`), wrapped through
`openff-interchange` 0.5.2 to OpenMM Topology and System.

### 3.3 Partial charges — **NAGL, not AM1-BCC/SQM**

**This was the most important architectural choice in the protocol** and
is responsible for the run-to-run reliability.

`OpenFFPartialChargeSettings` configured as:

```python
settings.partial_charge_settings.partial_charge_method = "nagl"
settings.partial_charge_settings.nagl_model           = "openff-gnn-am1bcc-1.0.0.pt"
```

**NAGL** (graph neural network AM1-BCC,
`openff-gnn-am1bcc-1.0.0.pt`, Wang et al. 2024) predicts AM1-BCC-quality
partial charges in **~1 second per molecule** on CPU.

Why this matters: the OpenFE default (`am1bcc` via the AmberTools
backend) shells out to `antechamber` → `sqm` (semi-empirical
single-point quantum-mechanical calculation). For drug-like molecules
(30–50 heavy atoms), `sqm` takes **30 minutes to several hours per
ligand**, and SepTop parameterises 8 (ligand × leg) instances per FEP
edge. Any retry triggered by minimisation NaNs or equilibration
failures restarts the whole charge-generation chain from scratch, with
no on-disk caching. In our prior (cancelled) cascade, four jobs ran
for 24 hours each with **0% GPU utilisation** — they were stuck in
SQM retry loops on CPU. NAGL eliminates this failure mode entirely.

Reference: Wang, Y., Pulido, I., Takaba, K., et al. *EspalomaCharge*
and AM1-BCC NAGL benchmarks (DOI: 10.26434/chemrxiv-2024-...)

### 3.4 Water and ions

| Field | Value |
|---|---|
| Water model | TIP3P |
| Ion concentration | 0.15 M NaCl |
| Source | `openfe.SolventComponent(ion_concentration=0.15 * unit.molar)` |

### 3.5 Hydrogen-mass repartitioning

`openff-interchange` default: H mass set to 3 amu, donor heavy-atom
mass reduced commensurately. Permits 4 fs MD timestep without
constraint instability.

## 4. SepTop alchemical setup

### 4.1 Topology

Both ligands (K4T and candidate) are loaded as
`SmallMoleculeComponent`s and combined with the
`ProteinComponent`+`SolventComponent` to form **two parallel
`ChemicalSystem`s**:

```
state_A (bound_K4T):       protein + K4T(interacting) + cand(decoupled)  + solvent
state_B (bound_cand):      protein + K4T(decoupled)   + cand(interacting) + solvent
```

The two ligands are spatially **separated** in the simulation box
(SepTop's name); a flat-bottom restraint keeps the decoupled ligand
out of the binding site so it doesn't interfere.

No atom mapping is supplied (`mapping=None`). SepTop's λ schedule
handles the alchemical interpolation between the two ligand-on-protein
states without requiring any structural correspondence.

### 4.2 λ schedule

| Phase | n_replicas | λ_electrostatic | λ_steric | λ_restraint |
|---|---|---|---|---|
| State A → B (electrostatic decouple) | 11 | 1.00 → 0.00 | 1.00 | active |
| State A → B (steric decouple) | (overlapping) | 0.00 | 1.00 → 0.00 | active |
| State A → B (recouple at site B) | 11 | 0.00 → 1.00 (cand) | 0.00 → 1.00 | flat-bottom |

`n_replicas = 11`. Default OpenFE `LambdaSettings` schedule.

### 4.3 Restraints

A Boresch-style orientational restraint (1 distance, 2 angles, 3 dihedrals)
is applied to the decoupled ligand to keep it solvent-exposed and
out of the binding pocket. The restraint contribution to ΔG is
analytically corrected at the end-state.

## 5. Sampling protocol

### 5.1 Hierarchy

| Level | Quantity |
|---|---|
| Edges per job | 1 (K4T → one candidate) |
| Phases per edge | 2 (complex + solvent) |
| λ-windows per phase | 11 |
| Replicas per window | 1 |
| Hamiltonian-replica-exchange | enabled (`MultiStateMethods.HREX`) |

### 5.2 Time per window (current settings)

| Setting | Production cascade | Smoke test |
|---|---|---|
| Equilibration | **30 ps** | 20 ps |
| Production | **80 ps** | 50 ps |
| Total per leg (11 windows) | 1.21 ns | 0.77 ns |
| Total per edge (4 legs) | **4.84 ns** | 3.08 ns |
| Frame interval | 10 ps | 10 ps |
| MD timestep | 4 fs (HMR) | 4 fs |

These are intentionally **light-sampling** — adequate for relative
ranking among 10 candidates with ~3 kcal/mol uncertainty, but
not for publication-grade ΔΔG. Production-grade settings (200+700
ps, ~40 ns/edge) require ~3× this wallclock; will be applied to the
top-3 candidates after the first-pass triage finishes.

### 5.3 Wallclock targets

| Setting | A100 80 GB walltime | Walltime budget |
|---|---|---|
| Production cascade (30+80 ps) | ~2-3 h/edge | 6 h (3× safety) |
| Smoke test (20+50 ps) | ~1.5-2 h | 3 h |

Throughput on Cheaha A100 80GB PCIe (measured): ~30-50 ns/day,
varying by node. PCIe-vs-SXM and Lustre I/O dominate; CUDA driver
12.4, OpenMM 8.2.

## 6. Free-energy estimator

`MultiStateReporter` writes per-replica reduced-potential matrices
to NetCDF. ΔG is computed via **MBAR** (Multistate Bennett Acceptance
Ratio, Shirts & Chodera 2008) at the end of production:

```python
ΔΔG = sep_top_protocol.gather([dag_result]).get_estimate()
σ   = sep_top_protocol.gather([dag_result]).get_uncertainty()
```

The σ reported is the bootstrap MBAR statistical uncertainty,
not including force-field or sampling-convergence error.

## 7. Hardware and software

| Component | Version |
|---|---|
| Cluster | UAB Cheaha — `amperenodes` (12 h) and `amperenodes-medium` (48 h) partitions |
| GPU | NVIDIA A100 80 GB PCIe (driver 550.90.07, CUDA 12.4) |
| OpenFE | 1.11.0 |
| OpenMM | 8.2.0 |
| OpenFF Toolkit | 0.16.x |
| OpenFF NAGL | 0.5.5 |
| AmberTools | 24.8 |
| RDKit | 2025.09.5 (librdkit 2025.09.5) |
| Python | 3.11 |
| Conda env | `openfe-py` |

## 8. Job orchestration and monitoring

Each FEP edge runs as one Slurm job submitted via
`abfe_production.sbatch`:

```bash
sbatch --job-name=abfe_phgdh_cand_NNN \
  --export=ALL,CAND_SMILES="<smi>",CAND_NAME="cand_NNN",TARGET=phgdh \
  abfe_production.sbatch
```

The cascade driver `submit_abfe_cascade.sh N M` submits the top N
candidates against PHGDH and the top M against counter-receptors
(PSAT1; PSPH dropped after the cofactor-aware re-screen showed it
non-druggable for our candidate class).

`#SBATCH --exclude=c0248` is set after empirical evidence of
`sqm`-loop failure on that node in the prior cascade.

The health monitor `cheaha_health.sh` runs on the login node and
writes `/data/user/jakechen/aim4_clm/runs/health.json` every 60 s,
classifying each running job's phase as one of:

- **SETUP** — parameterisation in progress (NAGL ~1 s; should not
  linger)
- **MD-RUNNING** — GPU util ≥ 50% AND GPU mem ≥ 1 GB
- **MD-WAITING** — GPU mem ≥ 1 GB but util < 50% (between λ
  windows or during checkpoint)
- **SQM-STALL** — `sqm` process detected ⟹ NAGL did not engage
  (treated as fatal; auto-cancel triggers)
- **RETRY-LOOP** — > 2 `_attempt_N` directories ⟹ silent retries;
  auto-cancel
- **STALLED** — newest trajectory file unchanged > 30 min;
  auto-cancel

## 9. Lessons learned (iter-6 in particular)

| Lesson | Detail |
|---|---|
| **Trajectory growth is not progress** | `solvent.nc` grows during checkpoint writes and CPU-platform fallback. Use GPU utilisation as ground truth. |
| **Job state `RUNNING` is not progress** | A job can run for 24 h with 0% GPU. `nvidia-smi` per node every poll, not job state. |
| **stderr clean ≠ no failures** | OpenFE retries silently. Count `_attempt_N` directories; > 1 means trouble. |
| **AM1-BCC/SQM is unfit for production cascades** | Single-threaded, hours per ligand, no on-disk cache, restarts every retry. NAGL or pre-computed Espaloma charges only. |
| **Auto-recorded AGE scores must be discounted** | Self-reported success doesn't imply outcome. Require artifact verification (ΔΔG present, MBAR σ < threshold) before crediting Achievement points. |

## 10. Reproducibility

```bash
git clone <repo>
cd aim4_clm
mamba env create -f env/openfe-py.yml -n openfe-py
mamba activate openfe-py

# fix protein once
sbatch protein_fix.sbatch

# pilot (one candidate, smoke test sampling)
sbatch smoke_fep.sbatch

# production (10 candidates, light sampling)
./submit_abfe_cascade.sh 10 0 real

# monitoring
./cheaha_health.sh --watch 60
```

All scripts at `/home/jakechen/jobs/aim4_clm/` on Cheaha;
mirrored to GitHub at `<repo URL>/scripts/`.
