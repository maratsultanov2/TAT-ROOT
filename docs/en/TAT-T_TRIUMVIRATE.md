# TAT-T Triumvirate: Three-Actor Architecture

## Overview
TAT-T (Triple TAT-7) uses three parallel actors with different phase shifts and a structural memory. This document presents two independent validations.

## 1. Synthetic Benchmark
| Phase | Mean divergence | Threshold exceeded |
|-------|-----------------|--------------------|
| Single TAT-7 | 2.1 | 9/10 |
| Dual-phase | 1.7 | 8/10 |
| **Triple-phase** | **0.13** | **3/10** |

*Reduction: 94% from single to triple.*

![Synthetic benchmark comparison](../images/triumvirate_synthetic.png)

## 2. Cross-Framework Validation
| Dataset | Single | Triple |
|---------|--------|--------|
| Cophy (31 steps) | 0.154 | **-0.146** |
| Resonance-Missile (101 steps) | 0.006 | **-0.245** |
| Agora/mnemo (5 steps) | 0.002 | **-0.450** |

![Cross-framework validation results](../images/triumvirate_cross_framework.png)

## Conclusion
TAT-T consistently improves coherence across synthetic and real-world data.

## Reproducibility
See `/notebooks/TAT-T_Triumvirate_Synthetic.ipynb` and `/notebooks/TAT-T_CrossFramework_Validation.ipynb`.
