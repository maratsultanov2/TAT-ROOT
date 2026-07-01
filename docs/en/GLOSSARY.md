# TAT Glossary

This glossary defines the key terms used across TAT and related frameworks (Cophy Runtime, HeartFlow, TLAA). Terms are listed alphabetically.

## Terms

| Term | Author | Definition |
|------|--------|------------|
| **Chunk carousel** | Marat Sultanov (TAT) | Memory management mechanism without discard/defer: active chunks (with strong connections) stay at the front, unused chunks naturally cool down and recede, reactivating if future context resonates, or undergoing apoptosis if connections break entirely. |
| **Coherence** | Marat Sultanov (TAT) | Measure of structural agreement between heads: `coherence = |w1 · conj(w2)| / (|w1| · |w2| + ε)`. Low coherence triggers harmony gate. |
| **Divergence trace** | Marat Sultanov (TAT) | Diagnostic signal computed as `divergence = Position − Coherence`. Leading indicator of memory drift: rising divergence predicts coherence collapse before surface metrics register it. |
| **Harmony gate (Structural veto)** | Marat Sultanov (TAT) | harmony head with weight 2.0: if harmony is silent, consolidation is withheld regardless of Position and Coherence values. |
| **H-value** | yun520-1 (HeartFlow) | Field health formula: `H = 0.4·U + 0.3·D − 0.3·A`, where U/D/A are normalized utility, direction, and authority. |
| **Kettle Principle** | Marat Sultanov (TAT) | Sufficiency as energy efficiency: 7 heads is boiling water, used only when the task requires it. Most consolidation runs below the boiling point, and that is correct behavior, not degradation. |
| **Mirror timestamp** | Marat Sultanov (TAT) | Dual-format timestamp `DD.MM.YYYY / YYYY.MM.DD` enabling direct machine access (right side, integer comparison, zero parsing) and human readability (left side), with symmetry axis (slash) for recovery from partial damage. |
| **Operational envelope (93–96%)** | Marat Sultanov (TAT) | Bounds of sufficiency: lower bound 93% = 100% − 7% (7 heads, T_max=0.7, 0.7% noise), upper bound 96% = 100% − 4% (connection_weight_multiplier=4). The system does not pursue 100% accuracy. |
| **Position** | Marat Sultanov (TAT) | Model's confidence in its output, measured as the maximum softmax probability. Structural head (solo) weight: 0.55. |
| **Pre-execution verification** | yun520-1 (HeartFlow) | Audit that occurs before tool execution, allowing BLOCK/MODIFY decisions before tokens are generated and side effects occur. |
| **Surface coherence** | icophy (Cophy Runtime) | State where an agent appears active (high Position) and internally consistent (normal Coherence) but is not meaningfully integrating new information with existing memory (harmony silent, low causal density). |

| **Dialogue ring (Диалоговое кольцо)** | Marat Sultanov (TAT) | Multi-agent iterative reconciliation mechanism: models exchange data across multiple rounds until coherence reaches the 0.5 threshold. Deeper than single-round verification — agents negotiate, coherence rises at each turn. |
## Attribution

- **Marat Sultanov** — creator of TAT (TreeAngleTap). [GitHub](https://github.com/maratsultanov2)
- **icophy** — creator of Cophy Runtime. [GitHub](https://github.com/icophy)
- **yun520-1** — creator of HeartFlow. [GitHub](https://github.com/yun520-1)

## References

- [TAT Theoretical Foundation](THEORETICAL_FOUNDATION.md)
- [Cross-Framework Calibration](CROSS_FRAMEWORK_CALIBRATION.md) (forthcoming)

---

*This glossary is part of TAT-ROOT. All definitions are public prior art, published on GitHub with timestamps.*
