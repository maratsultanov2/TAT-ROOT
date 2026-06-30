# Known Limitations

This document honestly describes what TAT can and cannot do as of June 2026.

## What TAT does well
## What TAT handles well

- **Noise immunity:** TAT-7 does not overfit on heterogeneous data. Stress test on 33,619 mixed fragments (code, logs, text) showed flat divergence (−0.028 ± 0.009) — the model correctly identified the absence of semantic phase transitions.
- **Energy efficiency:** 3 hours of continuous operation on standard CPU without thermal issues. See [Stress Test](data/STRESS_TEST_33619.md).

## What TAT does well (continued)

- **Continual learning (images):** TAT-7 retains 79% memory on Split Fashion-MNIST vs. 6–9% for EWC/SI/MAS. Divergence trace works as unsupervised leading indicator.
- **Supervised semantic phase detection (text):** TAT-7 with complex weights (θ=1.987), soft boundaries (37/73), and controlled noise (0.7%) distinguishes 5 semantic phases with ~1.0 separation when trained with phase labels.
- **Sequence prediction:** TAT-7 outperforms LSTM (2.3× faster) and MLP (2× faster) with superior accuracy on phase transition prediction.
- **Memory compression:** TAT-DIFF achieves 645× lossless compression vs. full context storage.

## What TAT cannot do yet

- **Unsupervised divergence on text:** Harmonic resonance does not activate on synthetic text with DistilGPT2 hidden states, even with complex weights enabled. A more powerful LLM is required.
- **Chinese language support:** Current extractor is calibrated for Russian and English. Chinese requires separate calibration.
- **Real dialog data:** Tests were run on synthetic data. Real dialog logs (Cophy, HeartFlow) are needed for production validation.

## Architectural limitations

- **Supervised training required for text:** Unlike Fashion-MNIST where divergence trace emerges naturally, text-based phase detection currently requires labeled training data.
- **LLM dependency:** The quality of divergence trace depends on the richness of hidden states from the underlying LLM. DistilGPT2 (82M) is insufficient; larger models are needed.
- **Compute:** All tests run on CPU (Google Colab free tier). Training time scales with sample size and LLM complexity.

## Next steps

1. Calibrate extractor for Chinese language (万象渊鉴 test set)
2. Scale to larger LLM (TinyLlama, DeepSeek) for unsupervised divergence
3. Run on real dialog data (Cophy session logs, HeartFlow traces)
