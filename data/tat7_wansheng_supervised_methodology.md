# TAT-7 on 万象渊鉴 — Methodology

**Test set:** 万象渊鉴 V2 (Chinese-Russian mixed text, 26 fragments)
**Mode:** Supervised, auto-labeled phases
**Extractor:** paraphrase-multilingual-MiniLM-L12-v2 (multilingual, 384-dim embeddings)
**Architecture:** TAT-7 with complex weights (θ=1.987), soft boundaries 37/73, controlled noise 0.7%
**Training:** 500 epochs, Adam lr=1e-3, MSE loss

## Results

| Phase | Mean Divergence | ±σ | Fragments |
|-------|----------------|-----|-----------|
| Stable | 0.001 | ±0.004 | 8 |
| Doubt | 0.999 | ±0.002 | 5 |
| Conflict | 1.996 | ±0.003 | 7 |
| Synthesis | 2.991 | ±0.001 | 2 |
| New Stable | 3.993 | ±0.001 | 4 |

Divergence clearly distinguishes all 5 phases with ~1.0 separation.

## Limitations

- Auto-labeling by keywords (not manual expert annotation)
- Small sample size (26 fragments)
- Multilingual extractor may have uneven quality across languages
- Supervised training (requires phase labels)
