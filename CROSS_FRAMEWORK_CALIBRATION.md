# Cross-Framework Calibration

Conventions for comparing TAT with HeartFlow, Cophy Runtime, and TLAA on runtime logic audit, memory retention, and identity stability benchmarks.

## 1. Threshold Alignment

| TAT Metric | TAT Threshold | HeartFlow Equivalent | Notes |
|------------|---------------|----------------------|-------|
| Divergence | < 0.10 (3 heads) | Normalized < 0.10 (stable) | Low-divergence consolidation |
| Divergence | 0.10 – 0.30 (5 heads) | Normalized 0.10 – 0.30 (drifting) | Protective correction active |
| Divergence | > 0.30 (7 heads) | Normalized > 0.30 (divergent) | Withhold / TURN decision |
| Harmony status | active / weak / silent | stable / drifting / divergent | Structural veto mapping |

HeartFlow uses a 0–100 scale. Conversion: `TAT_divergence = HeartFlow_divergence / 100`.

## 2. Decision Vocabulary Mapping

| TAT Gate | HeartFlow Decision | Semantics |
|----------|-------------------|-----------|
| Consolidate | hold, accelerate | Normal operation, low divergence |
| Escalated (5-head) | turn | Divergence detected, protective correction |
| Withhold (harmony silent) | heal, pause, rest, transmit | Action blocked or deferred, depending on harmony_status |

## 3. Data Format Conventions

Each framework provides results in its native format, with a `raw_format` field declared:

| Framework | raw_format | Typical Fields |
|-----------|------------|----------------|
| TAT | CSV | task_id, phase, position, coherence, divergence, harmony_status, heads, gate_decision |
| HeartFlow | CSV | scenario_id, timestamp, position, coherence, divergence, normalized, harmony_status, h_value, cognitive_load, decision, confidence |
| Cophy Runtime | CSV + markdown | scenario_id, pressure_type, preference_id, applied_correctly, causal_density_at_retrieval |

## 4. Design Philosophy Differences

| Concern | TAT | HeartFlow | Cophy Runtime |
|---------|-----|-----------|---------------|
| Identity shift during roleplay | Triggers escalation at divergence > 0.30 | Considered acceptable if temporary | Measured via behavioral counterfactuals |
| Pre-execution vs. post-hoc audit | Harmony gate blocks consolidation before output | Three-way dispatch (truth/lesson/verify) before execution | Post-hoc health scoring in Dream Cycle |
| Memory management | Chunk carousel (cooling + apoptosis) | Static rules + Q-table | TTL-based pruning with causal density |
| Static vs. runtime-updatable rules | Gate thresholds fixed; harmony matrix learnable | 29 rules runtime-updatable without model retraining | Evaluation framework fixed; scenarios updatable |

## 5. Attribution

| Concept | Originator | Framework |
|---------|------------|-----------|
| Divergence trace (Position − Coherence) | Marat Sultanov | TAT |
| Harmony gate (structural veto) | Marat Sultanov | TAT |
| Chunk carousel | Marat Sultanov | TAT |
| Kettle Principle (sufficiency) | Marat Sultanov | TAT |
| Operational envelope (93–96%) | Marat Sultanov | TAT |
| Mirror timestamp | Marat Sultanov | TAT |
| Surface coherence | icophy | Cophy Runtime |
| H-value (0.4·U + 0.3·D − 0.3·A) | yun520-1 | HeartFlow |
| Pre-execution verification | yun520-1 | HeartFlow |
| U/D/A/H four-dimensional field | luoxuejian000 | Independent synthesis |

## 6. References

- [TAT Theoretical Foundation](docs/en/THEORETICAL_FOUNDATION.md)
- [TAT Glossary](docs/en/GLOSSARY.md)
- [TAT Comparative Benchmark](docs/en/benchmarks/COMPARATIVE_BENCHMARK.md)

---

*This document is versioned in TAT-ROOT. Conventions can be updated as frameworks evolve and new data becomes available.*
