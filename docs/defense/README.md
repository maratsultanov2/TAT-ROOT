# TAT Defense Module

[![TAT Defense](https://img.shields.io/badge/TAT-Defense-blue)](../docs/defense/README.md)
[![License](https://img.shields.io/badge/License-Custom-red)](../../LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-yellow)](../docs/defense/README.md)
[![Comparison with AE](https://img.shields.io/badge/Comparison-AE-green)](../docs/defense/COMPARISON_WITH_AE.md)

Multi‑layer anomaly detection and flood management for TAT‑based systems.

## Capabilities
- Structural fault detection (divergence)
- Coherence loss tracking (harmony)
- Temporal anomaly detection
- Flood stream redirection
- Graph encryption and shifting

## Configuration
Two operational modes:
- **High precision** — minimal false positives.
- **High recall** — maximum anomaly detection.

## Performance (synthetic benchmark)
| Variant | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Fixed thresholds | 0.690 | 0.571 | 0.870 | 0.690 |
| Weighted voting | **0.845** | **1.000** | 0.609 | **0.757** |
| Adaptive weight | 0.828 | 0.933 | 0.609 | 0.737 |

The weighted voting variant achieves perfect precision (no false positives) while maintaining good recall.

## Where to use TAT Defense

TAT Defense is designed for detecting **structural breaks** — not statistical outliers, but violations of order, hierarchy, or coherence.

### Example 1: Hierarchical anomalies (synthetic data)

Data consists of ordered blocks (e.g., categories, steps, modules). Anomaly = swapped blocks or broken order.

- **TAT Defense:** F1 = 0.52
- **Autoencoder:** F1 = 0.08

TAT clearly wins because it detects the break in structure, not the deviation in values.

### Example 2: Time-series correlations (NASA-like data)

Data consists of correlated time series. Anomaly = one channel breaks correlation with others.

- **TAT Defense:** F1 = 0.05
- **Autoencoder:** F1 = 0.63

Here the autoencoder wins, because the anomaly is a statistical outlier in the reconstruction error. This is where TAT is not designed to compete.

### When to choose TAT Defense

- **Use TAT** when anomalies are about **order, hierarchy, or sequence** (logistics, dialog flow, manufacturing steps, code structure, knowledge taxonomies).
- **Use autoencoders** when anomalies are about **rare values or distributional outliers** (financial fraud, sensor spikes, quality control by value).

TAT is not a universal anomaly detector. It is a specialist for structural breaks.

## Comparison with other approaches
For context, the table below shows reported performance of well‑known anomaly detection methods from open literature. TAT Defense shows competitive F1 and unique precision (1.0) in weighted voting mode.

| Method | F1 | Precision | Recall | Source |
|---|---|---|---|---|
| **TAT Defense (weighted voting)** | **0.757** | **1.000** | 0.609 | This work (synthetic) |
| Isolation Forest | 0.81–0.95 | 0.76–0.91 | 0.78–1.00 | Nature 2025 |
| Autoencoder | 0.86 | 0.82 | 0.84 | Nature 2025 |
| One‑Class SVM | 0.79 | 0.72 | 0.75 | Nature 2025 |
| LSTM (NAB) | 0.688 | — | — | NAB benchmark |

## License
Custom TAT License — see [LICENSE](../../LICENSE).

## Status
✅ Prototype ready, testing complete.
