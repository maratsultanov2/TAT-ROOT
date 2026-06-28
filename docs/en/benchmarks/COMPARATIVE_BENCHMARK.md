# Comparative Benchmark: TAT-7 vs EWC / SI / MAS

## Test Setup

- **Dataset:** Split Fashion-MNIST (5 tasks × 2 classes)
- **Epochs per task:** 5
- **Metric:** Divergence Trace (Position − Coherence + Harmony + Gate)
- **Goal:** Measure memory retention under continual learning

## Methods Compared

| Method | Mechanism | Fails? |
|--------|-----------|--------|
| **TripleNet (vanilla)** | No protection | ❌ Memory ~0.05 |
| **EWC** (Elastic Weight Consolidation) | Fisher penalty on important weights | ❌ Memory ~0.02–0.09 |
| **SI** (Synaptic Intelligence) | Accumulated importance per synapse | ❌ Memory ~0.02–0.11 |
| **MAS** (Memory Aware Synapses) | Importance by output sensitivity | ❌ Memory ~0.02–0.09 |
| **TAT-7** | Harmonic resonance + phase coherence | ✅ Memory ~0.79 |

## Key Finding

**EWC, SI, and MAS fail because they protect weights, not connections.** 
On Split Fashion-MNIST, the problem is not weight drift — it's the breakdown of coherence between heads. 
TripleNet's three heads (yang, yin, to) diverge catastrophically, and EWC/SI/MAS do nothing to prevent this.

**TAT-7 solves the coherence problem directly.** 
The harmonic resonance matrix maintains inter-head phase alignment even as individual weights change. 
Harmony stays active, divergence stays below 0.20, and memory retention reaches 79% after 5 tasks.

## Results

| Metric | TripleNet | EWC | SI | MAS | TAT-7 |
|--------|-----------|-----|----|-----|-------|
| Mean Coherence | ~0.07 | ~0.09 | ~0.08 | ~0.10 | ~0.76 |
| Final Memory (Task 1) | ~0.06 | ~0.09 | ~0.09 | ~0.09 | ~0.79 |
| Harmony Status | Silent (5/5) | Silent (5/5) | Silent (5/5) | Silent (5/5) | Active (4/5) |
| Gate Decision | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Consolidate / Escalated |

## Data

- [TripleNet (CSV)](../../data/triplenet_divergence_trace.csv)
- [EWC (CSV)](../../data/ewc_divergence_trace.csv)
- [SI (CSV)](../../data/si_divergence_trace.csv)
- [MAS (CSV)](../../data/mas_divergence_trace.csv)
- [TAT-7 (CSV)](../../data/tat7_divergence_trace.csv)
- [Full Comparison Graph (PNG)](../../data/comparative_benchmark_all_methods.png)

## Reproduce

Run the Colab notebook: [TAT Comparative Benchmark](https://colab.research.google.com/)
