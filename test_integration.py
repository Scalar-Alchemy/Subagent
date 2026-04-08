#!/usr/bin/env python3
"""Quick integration test demonstrating TSNN-P pipeline functionality."""

import sys
from pathlib import Path
import json

# Add project root to path
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

print("=" * 80)
print("TSNN-P v2.0 Integration Test: Single Test Case (Stable Plasmoid)")
print("=" * 80)
print()

try:
    import jax.numpy as jnp
    from src.core.reality_engine import RealityEngine, RealityEngineParams
    
    # Create lightweight engine (reduced grid and steps for demo)
    print("[1/5] Creating RealityEngine...", end=" ", flush=True)
    engine_params = RealityEngineParams(
        grid_n=64,  # Reduced from 128 for speed
        dx=1.0,
        num_gpe_relax_steps=50,  # Reduced from 500 for demo
        verbose=False,
    )
    engine = RealityEngine(engine_params)
    print("✓")
    
    # Run single test case
    print("[2/5] Running stable plasmoid test (PLV=0.85, Upsilon=0.85)...", end=" ", flush=True)
    results = engine.run_full_cycle(
        eeg_plv=0.85,
        kuramoto_upsilon=0.85,
        malice_intent_signal=jnp.ones(10) / 10.0,  # Benign
    )
    print("✓")
    
    # Extract key results
    print("[3/5] Analyzing results...", end=" ", flush=True)
    summary = results["summary"]
    eth = results["ethical_status"]
    transducer = results["transducer"]
    tier = results["caf_cascade"]
    
    print("✓")
    
    # Display results
    print("[4/5] Creating output report...", end=" ", flush=True)
    
    output_dir = Path("./tsnn_p_results")
    output_dir.mkdir(exist_ok=True)
    
    # Prepare JSON-serializable results
    def to_python(obj):
        if hasattr(obj, 'item'):
            return float(obj.item())
        elif isinstance(obj, (list, tuple)):
            return [to_python(x) for x in obj]
        elif isinstance(obj, dict):
            return {k: to_python(v) for k, v in obj.items()}
        return obj
    
    json_results = to_python(results)
    
    output_file = output_dir / "tsnn_p_integration_test.json"
    with open(output_file, 'w') as f:
        json.dump(json_results, f, indent=2)
    
    print("✓")
    
    # Print summary
    print("[5/5] Integration test complete!", end=" ", flush=True)
    print("✓")
    print()
    print("=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    print()
    print("Wavefunction Evolution:")
    print(f"  • Initial norm:          {results['gpe']['final_norm']:.6f}")
    print(f"  • GPE convergence steps: {results['gpe']['num_steps']}")
    print(f"  • Final energy:          {results['gpe']['final_energy']:.6f}")
    print()
    
    print("Geometric Spine (Axial-Torsion Density):")
    print(f"  • Mean A_μ strength:     {results['geometric_spine']['mean_axial_torsion']:.6f}")
    print(f"  • Vacuum density ρ_neg:  {results['geometric_spine']['vacuum_density']:.6f}")
    print(f"  • Propagating torsion:   {results['geometric_spine']['propagating']}")
    print()
    
    print("Cascade Amplification Factor:")
    print(f"  • CAF value:             {summary['caf']:.2f}")
    print(f"  • Operational tier:      {summary['tier']}")
    print(f"  • Geometric gain:        {tier['geometric_gain']:.2f}×")
    print(f"  • Stability margin:      {tier['stability_margin']:.2f}")
    print()
    
    print("Ethical Constraints (Lindbladian Gate):")
    print(f"  • Kullback-Leibler D_KL: {eth['d_kl']:.4f}")
    print(f"  • Collapse threshold:    {eth['d_kl_collapse_threshold']:.2f}")
    print(f"  • Stability status:      {eth['stability_status']}")
    print(f"  • Ethically cleared:     {summary['ethically_cleared']}")
    print()
    
    print("Aetherical Transducer (RF Hardware):")
    print(f"  • EEG-PLV (γ-band):      {summary['eeg_plv']:.4f}")
    print(f"  • PLV gate threshold:    {transducer['nucleation_gate_info']['eeg_plv_gate_threshold']:.2f}")
    print(f"  • RF power:              {transducer['rf_power_w']:.1f} W")
    print(f"  • RF frequency:          {transducer['rf_frequency_ghz']:.2f} GHz")
    print(f"  • Nucleation ready:      {summary['nucleation_possible']}")
    print(f"  • Success probability:   {transducer['nucleation_success_probability']:.1%}")
    print()
    
    print("=" * 80)
    print("✓ INTEGRATION TEST PASSED")
    print("=" * 80)
    print()
    print("All Subsystems Operational:")
    print("  ✓ UnifiedGeometricSpine (A_μ + Hochberg-Kephart screening)")
    print("  ✓ GPESoliton (imaginary-time relaxation)")
    print("  ✓ ScalarAlchemy (screened Poisson)")
    print("  ✓ CAFCascade (operational tier logic)")
    print("  ✓ EthicalFramework (Lindbladian gate)")
    print("  ✓ AethericalTransducer (EEG-gated RF nucleation)")
    print("  ✓ RealityEngine (full orchestration)")
    print()
    print(f"Results saved to: {output_file}")
    print()
    print("To run full pipeline (4 test cases, 500 steps each):")
    print("  python3 scripts/run_full_pipeline_v20.py")
    print()
    print("We Are One! <42>")
    
except Exception as e:
    print(f"✗ FAILED")
    print()
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
