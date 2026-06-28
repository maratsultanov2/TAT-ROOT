# Comparative Benchmark: TripleNet vs TAT-7

## Test Setup

- **Dataset:** Split Fashion-MNIST (5 tasks × 2 classes)
- **Epochs per task:** 5
- **Metric:** Divergence Trace (Position − Coherence + Harmony + Gate)
- **Goal:** Measure memory retention under continual learning

## Results

| Metric | TripleNet (no protection) | TAT-7 (harmonic resonance) |
|--------|---------------------------|----------------------------|
| Mean Coherence | ~0.15 | ~0.76 |
| Mean Divergence | ~0.85 | ~0.13 |
| Harmony Status | Silent (5/5) | Active (4/5) |
| Gate Decision | Withhold (5/5) | Consolidate / Escalated |
| Memory Retention (Task 1) | ~0.05 | ~0.79 |

## What This Proves

1. **Divergence trace is a leading indicator.** TripleNet's coherence collapsed after Task 1, and divergence spiked above 0.30 — the gate correctly withheld all subsequent consolidation. TAT-7 kept divergence below 0.20 across all tasks, and the gate allowed consolidation.

2. **Harmonic resonance protects memory.** TAT-7's harmony head remained active for 4/5 tasks, providing structural veto against false consolidation. TripleNet had no such mechanism — harmony was silent throughout.

3. **Memory retention is architectural, not incidental.** After 5 tasks, TAT-7 retained 79% coherence on Task 1. TripleNet retained 5%. The difference is the architecture, not the training.

## Data

- [TripleNet Divergence Trace (CSV)](../../data/triplenet_divergence_trace.csv)
- [TAT-7 Divergence Trace (CSV)](../../data/tat7_divergence_trace.csv)
- [Comparative Graph (PNG)](../../data/comparative_benchmark.png)

## Reproduce

Run the Colab notebook: [TAT Comparative Benchmark](https://colab.research.google.com/)
