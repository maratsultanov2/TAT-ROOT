# TAT-ROOT — Architectural Core of TreeAngleTap

[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue.svg)](LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE-DATA)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![Cross-Framework](https://img.shields.io/badge/Cross--Framework-5%20frameworks-purple)]()

TAT-ROOT contains the theoretical foundation, glossary, benchmarks, and calibration documents for the TAT ecosystem.

## Quick Links

- [Theoretical Foundation](docs/en/THEORETICAL_FOUNDATION.md)
- [Glossary](docs/en/GLOSSARY.md)
- [Cross-Framework Calibration](CROSS_FRAMEWORK_CALIBRATION.md)
- [Known Limitations](docs/en/KNOWN_LIMITATIONS.md)
- [Comparative Benchmark](docs/en/benchmarks/COMPARATIVE_BENCHMARK.md)
- [Kettle Principle](docs/en/KETTLE_PRINCIPLE.md)
- [Cost Efficiency](https://github.com/maratsultanov2/TAT-ONE-TAP/blob/main/docs/en/COST_EFFICIENCY.md)

## Ecosystem

| Repository | Purpose |
|------------|---------|
| [TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT) | Architecture, theory, benchmarks |
| [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) | Memory for LLM, TAT-DIFF, TAT-Secretary |
| [TAT-DEMO](https://github.com/maratsultanov2/TAT-DEMO) | Visualization, Colab demos |
| [TAT7-logistics](https://github.com/maratsultanov2/TAT7-logistics) | Industrial prototype for warehouse |

## Cross-Framework Validation

TAT participates in the cross-framework field health observation with HeartFlow, Cophy, TLAA, and U/D/A/H. See #1466 in DeepSeek-V3.

## Stress Test (33,619 fragments)

TAT-7 stress-tested on 33,619 heterogeneous fragments (code + logs + research texts) with TinyLlama-1.1B. No overfitting, flat divergence, 3 hours continuous operation without thermal issues.

📖 [Full Methodology](data/STRESS_TEST_33619.md) | 📊 [Graph](data/stress_test_33619.png)


## TAT-7 on 万象渊鉴 (Cross-Framework Test Set)

TAT-7 supervised divergence trace on the shared 万象渊鉴 test set (Chinese-Russian mixed text). Auto-labeled phases, 26 fragments, 5 phases clearly distinguished.

📖 [Methodology](data/tat7_wansheng_supervised_methodology.md) | 📊 [CSV](data/tat7_wansheng_supervised.csv) | 📈 [Graph](data/tat7_wansheng_supervised.png)

## TAT-7: Basic vs Full Architecture Comparison

TAT-7 Full with complex weights (θ=1.987), soft boundaries 37/73, and controlled noise 0.7% achieves R²=0.989 — matching MLP baseline with interpretable divergence trace output. All tests on CPU (x86_64, 2 cores, Google Colab free tier).

| Model | R² | MAE | Time |
|-------|-----|-----|------|
| MLP | 0.990 | 0.064 | — |
| TAT-7 Basic | 0.943 | 0.214 | ~25s |
| TAT-7 Full | **0.989** | **0.118** | ~35s |

📖 [Methodology](data/tat7_basic_vs_full_methodology.md) | 📊 [Basic CSV](data/tat7_basic_250.csv) | 📊 [Full CSV](data/tat7_full_250.csv) | 📈 [Graphs](data/)

## TAT-7: Architecture Evolution

TAT-7 Full Harmony with 7×64×64 harmonic matrix surpasses MLP baseline (R²=0.995 vs 0.990). Each architectural component adds measurable value.

| Model | R² | MAE | Time |
|-------|-----|-----|------|
| MLP | 0.990 | 0.064 | — |
| TAT-7 Basic | 0.943 | 0.214 | ~25s |
| TAT-7 Full | 0.989 | 0.118 | ~35s |
| **TAT-7 Full Harmony** | **0.995** | **0.063** | ~40s |

📖 [Methodology](data/tat7_architecture_evolution.md) | 📊 [Data](data/)
