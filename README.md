# TSNN-P

**Unified Geometric Spine for Temporal Spatial Navigation and Plasmoid Reality Engineering**

TSNN-P delivers a computationally efficient framework that integrates spacetime torsion, gamma-band neural entrainment, superfluid vacuum phase guidance, and adaptive ethical-topological pruning into exascale digital twins of toroidal fusion devices and atmospheric coherent plasma structures.

## Quick Start

```bash
python -m pip install -e ".[dev]"
pytest
```

## Architecture

```
src/
  core/          GPE solver, torsion geometry (Poincare gauge / Proca), master equation
  neural/        gamma-band entrainment, Kuramoto synchronisation, PLV
  vacuum/        Dynamical Casimir Effect, quantum vacuum thrust
  ethics/        topological pruning, malice gate, Lindbladian MMD projection
  plasma/        FRC, helical devices, fusion utilities
  atmosphere/    planetary-wave reflection, coherent structure detection
  signal/        neutrino, EEG, quantum-ionospheric interaction
  compute/       JAX solvers, DFT (PySCF), gyrokinetic surrogates, federated cloud
  nanopore/      MOF, zeolite, aerogel substrate models
tests/           unit / integration / benchmarks
configs/         parameter YAML files
notebooks/       exploratory notebooks
docs/            theory, API, experiment logs
```

## Core Equation

Extended Gross-Pitaevskii in the nanopore volume:

```
i hbar dPsi/dt = [-hbar^2/(2m) nabla^2 + V_free + V_torsion + V_neural + V_ethical + g|Psi|^2] Psi
```

## Key Parameters

| Parameter | Range | Default | Source |
|-----------|-------|---------|--------|
| Grid resolution | 512^3 - 2048^3 | 1024^3 | Memory / resolution balance |
| Time step | 0.1 - 1 fs | 0.5 fs | Torsion-term stability |
| Torsion coupling q | 0.1 - 1.5 | 0.8 | Helical mode stabilisation |
| Gamma-band freq | 40 - 44 Hz | 42 Hz | Entrainment window |
| MMD threshold | 0.20 - 0.35 | 0.28 | Malice pruning sensitivity |
| Kuramoto Upsilon | 0.80 - 0.90 | 0.85 | Supercritical coherence onset |
| Nanopore radius | 10 - 50 nm | 25 nm | YAG:Ce aerogel typical |
| CAF Tier-2 cutoff | -- | > 12 | Empirical (afterglow & buoyancy) |

## License

See LICENSE for details.
