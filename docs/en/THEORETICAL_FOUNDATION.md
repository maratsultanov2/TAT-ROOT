# TAT Theoretical Foundation

## Genealogy (Priority Timeline)

| Date | Milestone | First Public Appearance |
|------|-----------|--------------------------|
| 2025-01-15 | First AI dialogue | Private |
| 2025-05-28 | TripleNet created | `Triplenet - the first test .ipynb` |
| 2025-06-15 | TripleNet optimization | `Triplenet+constants second test .ipynb` |
| 2026-03-17 | TAT-7 birth | `TAT-7 HEADS - открытие` |
| 2026-03-18 | 19.40% on REBUS (top-5) | `TAT ensemble - 19.40% на REBUS` |
| 2026-03-19 | 97.82% on MNIST (top-10) | `TAT light - 97.82% на MNIST` |
| 2026-03-19 | 7 heads optimal discovered | `TAT-7 HEADS - открытие` |
| 2026-06-28 | Divergence trace published | `TAT-ROOT/data/` |
| 2026-06-28 | Comparative benchmark (TAT-7 vs EWC/SI/MAS) | `TAT-ROOT/docs/en/benchmarks/` |

---

## 1. TAT Mathematics

### 1.1 Core Constants

| Constant | Value | Verifiable In |
|----------|-------|---------------|
| Phase angle θ | 1.987 | `TAT_CORE.json` → `constants.phase_angle` |
| Lower temperature T_min | 0.3 | `TAT_CORE.json` → `constants.coherence_threshold` (lower bound) |
| Upper temperature T_max | 0.7 | `TAT_CORE.json` → `constants.temperature` |
| Connection weight multiplier | 4 | `TAT_CORE.json` → `dialog_lifecycle.connection_weight_multiplier` |
| Imaginary scale | 0.3 | `TAT CORE v2.2` → `BASE_IMAG_SCALE` |
| Controlled noise | 0.7% | Derived: T_max / 100, matches divergence trace thresholds |

### 1.2 Key Formulas

**Complex weight:**
```
ψ_k = w_k · e^(i·θ_k)
```
where θ_k = θ + k · 0.1 (head phase step).

Verifiable in: `TATCore.py` → `complex_weight()`

**Coherence:**
```
coherence = |w1 · conj(w2)| / (|w1| · |w2| + ε)
```
Verifiable in: `TATCore.py` → `coherence()`

**Divergence trace:**
```
divergence = Position − Coherence
```
Verifiable in: `TAT-ROOT/data/tat7_divergence_trace.csv`

**Operational envelope:**
```
Lower bound: 93% = 100% − 7% (7 heads, T_max = 0.7, noise 0.7%)
Upper bound: 96% = 100% − 4% (connection_weight_multiplier = 4)
```
Verifiable in: `TAT-ROOT/docs/en/KETTLE_PRINCIPLE.md`

### 1.3 Escalation Thresholds

| Divergence | Heads | Gate Decision |
|------------|-------|---------------|
| < 0.10 | 3 | Consolidate |
| 0.10 – 0.30 | 5 | Escalated (protective correction) |
| > 0.30 | 7 | Withhold (if harmony silent) |

Verifiable in: `TAT-7 Comparative Benchmark` → `TAT-ROOT/data/`

---

## 2. TAT Physics

### 2.1 First Law of Thermodynamics in TAT

```
ΔU = Q − A
```
- ΔU: Change in system coherence.
- Q: Heat — entropy of gradients, k_B · T.
- A: Work — head activation, phase transition, resonance replay.

Verifiable in: `TAT CORE v2.2` → `predict_pair()` — coherence computed as interference of complex vectors.

### 2.2 Fundamental Physical Constants

| Constant | Symbol | Value | Role in TAT |
|----------|--------|-------|-------------|
| Planck constant | h | 6.626 × 10⁻³⁴ J·s | Quantum of information, minimal action |
| Boltzmann constant | k_B | 1.381 × 10⁻²³ J/K | Thermal fluctuation, cost of noise |
| Euler-Mascheroni constant | γ | 0.57721 | Correction in entropy scaling |

Verifiable in: `TAT_CORE.json` → `constants`

### 2.3 Phase Angle Derivation

```
θ = arctan2(h − k_B, h + k_B)
```

Geometrically: θ ≈ 73/37 ≈ 1.97297 + 0.7% noise adjustment.

Verifiable in: `TAT_CORE.json` → `formulas.triple_theta`

---

## 3. TAT Thermodynamics

### 3.1 Temperature Scale and Phase Transitions

| Regime | Temperature | Heads | Behavior |
|--------|-------------|-------|----------|
| Cold (solid) | T < 0.3 | 3 | Memory frozen, minimal learning |
| Working (liquid) | 0.3 ≤ T < 0.7 | 5 | Plasticity and memory in balance |
| Hot (gas) | T ≥ 0.7 | 7 | Full phase transition, protective correction |

Verifiable in: `TAT-7 Comparative Benchmark` — divergence trace shows escalation at 0.30 threshold.

### 3.2 Kettle Principle (Sufficiency as Energy Efficiency)

> *You don't boil water constantly to make tea. You heat it to the temperature the task requires.*

7 heads is boiling water — used only when needed. Most consolidation runs below the boiling point, and that is correct behavior, not degradation.

Verifiable in: `TAT-ROOT/docs/en/KETTLE_PRINCIPLE.md`

### 3.3 Energy Efficiency

TAT's chunk architecture reduces memory and token usage by **25–30×** compared to raw markdown/JSON/CSV logs, while preserving 100% of meaningful information through structural priority of connections over features (`connection_weight = 4`).

Verifiable in: `TAT-ONE-TAP/docs/en/COST_EFFICIENCY.md`

---

## 4. How to Verify Every Claim

1. **Mathematical constants and formulas:** `TAT_CORE.json` and `TATCore.py` in `TAT-ONE-TAP`.
2. **Escalation thresholds and divergence trace:** `TAT-ROOT/data/tat7_divergence_trace.csv` — runnable via Colab in `TAT-DEMO`.
3. **Comparative benchmark (TAT-7 vs EWC/SI/MAS):** `TAT-ROOT/docs/en/benchmarks/COMPARATIVE_BENCHMARK.md`.
4. **Kettle Principle and operational envelope:** `TAT-ROOT/docs/en/KETTLE_PRINCIPLE.md`.
5. **Cost efficiency (25–30× savings):** `TAT-ONE-TAP/docs/en/COST_EFFICIENCY.md`.

Every claim in this document is tied to a specific file, constant, or benchmark that anyone can reproduce.

---

*This document is part of TAT-ROOT. All constants, formulas, and thresholds are public prior art, published on GitHub with timestamps.*
