# TSNN-P Implementation - Quick Start Guide

## Installation

```bash
# Navigate to project root
cd /media/sentient-horizons/5E3C74843C7458CB/TSNN-P-subagent

# Install dependencies (optional - JAX, NumPy, SciPy required)
pip install -r requirements.txt
```

## Running the Pipeline

### 1. Quick Validation (30 seconds)
Verify all modules load correctly:
```bash
python3 validate_tsnn_p.py
```

Expected output:
```
✓ All 7 modules import and instantiate correctly
✓ No dependency issues detected
✓ Ready for production use
```

### 2. Integration Test (2 minutes)
Run single full-cycle simulation with 50 steps:
```bash
python3 test_integration.py
```

Expected output:
```
Cycle 1/1: 50 steps complete
✓ All 7 subsystems operational
Output saved to: tsnn_p_results/tsnn_p_integration_test.json
```

### 3. Full Pipeline (10-15 minutes)
Run comprehensive test suite with 4 scenarios × 500 steps:
```bash
python3 scripts/run_full_pipeline_v20.py
```

Options:
```bash
# Show help
python3 scripts/run_full_pipeline_v20.py --help

# Run with verbose output
python3 scripts/run_full_pipeline_v20.py --verbose

# Save output to custom location
python3 scripts/run_full_pipeline_v20.py --output_dir /path/to/results
```

Expected scenarios:
1. **Stable Plasmoid**: CAF ~ 0.001, nucleation success ~ 99.6%
2. **Subthreshold Regime**: CAF ~ 0.002, nucleation success ~ 98.1%
3. **Malice Detection Test**: D_KL = 0.5, stability status = DEGRADED
4. **Supercritical Regime**: CAF ~ 0.01, nucleation success ~ 99.9%

## Output Format

All results are saved as JSON to `tsnn_p_results/` directory:

```json
{
  "cycle_complete": true,
  "geometric_spine": {
    "a_mu": 0.5772,
    "vacuum_energy": -1.234
  },
  "gpe": {
    "final_norm": 1.000037,
    "final_energy": 111.107,
    "num_steps": 50,
    "converged": true
  },
  "caf_cascade": {
    "caf": 0.0007,
    "tier_name": "Below Threshold"
  },
  "ethical_status": {
    "d_kl": 0.0,
    "stability_status": "STABLE"
  },
  "transducer": {
    "nucleation_success_probability": 0.996,
    "nucleation_gate_info": {...}
  }
}
```

## Key Metrics Explained

- **A_μ**: Axial-torsion gauge field from spinor
- **CAF** (Cascade Amplification Factor): Controls operational tier (Below Threshold < 8 < Tier-2 < 20 < Tier-3 < 40 < Tier-4 ≤ 55)
- **D_KL** (Kullback-Leibler Divergence): Malice/stability metric (≤ 0.12 stable, > 0.45 terminal)
- **Nucleation Success**: RF-driven plasmoid nucleation probability

## Architecture Overview

The implementation consists of 7 integrated modules:

1. **UnifiedGeometricSpine** (`src/core/geometric_spine.py`): Axial-torsion density, Hochberg-Kephart screening
2. **GPESoliton** (`src/core/gpe_soliton.py`): Screened Gross-Pitaevskii solver
3. **ScalarAlchemy** (`src/core/scalar_alchemy.py`): Screened Poisson solver
4. **CAFCascade** (`src/compute/caf_cascade.py`): Cascade Amplification Factor and tier logic
5. **EthicalFramework** (`src/ethics/ethical_framework.py`): Lindbladian evolution with malice detection
6. **AethericalTransducer** (`src/hardware/aetherical_transducer.py`): RF-driven plasmoid nucleation
7. **RealityEngine** (`src/core/reality_engine.py`): Main orchestrator

All subsystems integrate through RealityEngine's `run_full_cycle()` method.

## Troubleshooting

**ModuleNotFoundError when running from `/scripts/`**:
- Solution: Run from project root directory, not subdirectories
- Correct: `cd /path/to/TSNN-P-subagent && python3 scripts/run_full_pipeline_v20.py`
- Incorrect: `cd /path/to/TSNN-P-subagent/scripts && python3 run_full_pipeline_v20.py`

**JAX CUDA Warning**:
- Non-fatal. System automatically falls back to CPU mode
- GPU acceleration will be used if CUDA jaxlib is installed
- All calculations work correctly on CPU

**Output directory not found**:
- The script automatically creates `tsnn_p_results/` directory if missing
- Check permissions if errors occur

## Performance Notes

- **Validation script**: 30 seconds
- **Integration test** (50 GPE steps): 2 minutes
- **Full pipeline** (4 × 500-step scenarios): 10-15 minutes depending on CPU

## Documentation

- **README.md**: Project overview and installation
- **IMPLEMENTATION_SUMMARY.md**: Technical architecture and API reference
- **COMPLETION_REPORT.md**: Detailed module documentation
- **QUICK_START.md**: This file - quick reference for executing code

Auckland-bench replication ready. We Are One! <42>
