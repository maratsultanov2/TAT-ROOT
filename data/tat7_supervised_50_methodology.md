# TAT-7 Supervised Divergence Trace — Methodology

**Timestamp:** 30.06.2026 / 2026.06.30
**Device:** cpu (Google Colab, free tier)
**Total time:** 32.2s (extraction: 17.1s, training: 15.2s)

## Test Setup

- **Samples:** 50 synthetic Russian-language texts
- **Phases:** 5 (Stable, Doubt, Conflict, Synthesis, New Stable)
- **Samples per phase:** 10
- **LLM for hidden states:** DistilGPT2 (82M parameters, frozen)
- **Hidden state extraction:** Last layer, mean pooling → 768-dimensional vectors

## TAT-7 Architecture

| Component | Value |
|-----------|-------|
| Phase angle θ | 1.987 |
| Imaginary scale | 0.3 |
| Controlled noise | 0.7% |
| Soft boundaries | 37/73 |
| Heads | 7 |
| Head dimension | 64 |
| Hidden dimension | 384 |
| Harmonic matrix | 7×64×64 (learnable) |
| Temperature | Learnable, initial 0.7 |

## Training

- **Objective:** MSE between divergence (Position − Coherence) and phase label (0–4)
- **Optimizer:** Adam, lr=1e-3
- **Epochs:** 500
- **Complex weights:** Enabled (θ=1.987, imag_scale=0.3)
- **Noise injection:** 0.7% per forward pass
- **Soft boundaries:** 37/73 applied to position

## Results

| Phase | Mean Divergence | ±σ |
|-------|----------------|-----|
| Stable | 0.0009 | ±0.0069 |
| Doubt | 0.9996 | ±0.0199 |
| Conflict | 1.9989 | ±0.0259 |
| Synthesis | 2.9987 | ±0.0188 |
| New Stable | 3.9995 | ±0.0169 |

Divergence distinguishes all 5 phases with ~1.0 separation. Standard deviation < 0.03.

## Data

- [CSV](https://raw.githubusercontent.com/maratsultanov2/TAT-ROOT/master/data/tat7_supervised_50.csv)
- [Graph](https://raw.githubusercontent.com/maratsultanov2/TAT-ROOT/master/data/tat7_supervised_50.png)

## Limitations

- Synthetic data only
- DistilGPT2 (82M) — limited representation capacity
- Russian language — not calibrated for Chinese
- Supervised training — requires phase labels
