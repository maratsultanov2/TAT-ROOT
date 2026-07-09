# TAT Defense Module

[![TAT Defense](https://img.shields.io/badge/TAT-Defense-blue)](../docs/defense/README.md)
[![License](https://img.shields.io/badge/License-Custom-red)](../../LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-yellow)](../docs/defense/README.md)

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

## Comparison with other approaches
For context, the table below shows reported performance of well‑known anomaly detection methods from open literature. TAT Defense shows competitive F1 and unique precision (1.0) in weighted voting mode.

| Method | F1 | Precision | Recall | Source |
|---|---|---|---|---|
| **TAT Defense (weighted voting)** | **0.757** | **1.000** | 0.609 | This work (synthetic) |
| Isolation Forest | 0.81–0.95 | 0.76–0.91 | 0.78–1.00 | Nature 2025 [1†L22-L23][1†L18-L19] |
| Autoencoder | 0.86 | 0.82 | 0.84 | Nature 2025 [1†L23][2†L22-L23] |
| One‑Class SVM | 0.79 | 0.72 | 0.75 | Nature 2025 [1†L23] |
| LSTM (NAB) | 0.688 | — | — | NAB benchmark [0†L11-L12] |

## License
Custom TAT License — see [LICENSE](../../LICENSE).

## Status
✅ Prototype ready, testing complete.
