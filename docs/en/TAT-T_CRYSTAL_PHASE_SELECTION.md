# TAT-T Crystal: Phase Selection via Grid Scan

## Overview
TAT-T Crystal is a 3-layer architecture (DNA/RNA/Protein) with configurable phase shifts. This document presents the phase-space scan results.

## Methodology
- **Architecture:** 3/5/11 heads.
- **Phase scan:** 4×4×4 grid (64 combos), phases 0.00–0.15 step 0.05.
- **Training:** 30 epochs per combo.
- **Data:** Combined 142 steps from Resonance-Missile, Cophy, Agora/mnemo.
- **Hardware:** NVIDIA T4 GPU, runtime ~2h05m.

## Metrics & Results
| Configuration | mean_div | corr_rna_protein | low_ratio | high_ratio | score |
|---------------|----------|------------------|-----------|------------|-------|
| Baseline (0.00, 0.05, 0.10) | 0.151 | 0.696 | 3.5% | 0% | 0.911 |
| **Candidate (0.00, 0.15, 0.15)** | **0.173** | **0.854** | **5.6%** | **0%** | **0.802** |

![Divergence trace comparison](../images/tat_crystal_phase_comparison.png)

## Conclusion
The optimal phase configuration is **(0.00, 0.15, 0.15)**. It improves RNA–Protein correlation by +0.158 while keeping high_ratio at 0%.

## Reproducibility
See `/notebooks/TAT-T_Crystal_Phase_Scan.ipynb`.
