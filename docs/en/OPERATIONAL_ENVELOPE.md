# Operational Envelope of TAT

## 93–96%: The Sufficiency Band

The 93–96% range is not a quality target. It is the **operational envelope** derived from TAT's internal constants.

### Lower Boundary: 93%

93% = 100% − 7%. The 7 comes from three linked sources:

- **7 heads** (TAT-7 architecture)
- **T_max = 0.7** (phase transition temperature)
- **0.7% controlled noise** (soft boundary)

This is the lower boundary: the system does not fall below 93% because at that point the 7-head mode with protective correction activates. The architecture catches the drop before it becomes a collapse.

### Upper Boundary: 96%

96% = 100% − 4%. The 4 comes from **connection_weight_multiplier = 4** — the structural priority rule: connections matter 4× more than features.

This is the upper boundary: the system does not pursue accuracy above 96% because the remaining 4% represents the **sufficiency plateau**, where further gain requires exponential resource cost for sub-0.2% improvements.

### Implication

93–96% is the band within which TAT's phase transitions operate:

- **Below 93%** → system escalates to 7 heads
- **Above 96%** → system hits the plateau and stops spending resources

The envelope is not a preference — it is the **geometry of the architecture**.

---

## Sufficiency as a Design Constraint

Sufficiency is not a compromise. It is a **design constraint** with three concrete implementations:

### 1. Adaptive Head Selection

TAT uses entropy-driven gating:

- **T < 0.3** → 3 heads (cold mode, memory stable)
- **0.3 ≤ T < 0.7** → 5 heads (grey zone, protective correction)
- **T ≥ 0.7** → 7 heads (hot mode, full phase protection)

Resource sufficiency: only what is needed.

### 2. Plateau-Aware Accuracy Target

TAT optimizes not to 100%, but to the operational envelope (93–96%).

Measured per-head gain beyond 7 heads is ~0.2% — which does not justify the resource cost. The architecture stops before diminishing returns dominate.

### 3. Marking Instead of Blocking

7-head mode does not pause consolidation. It marks output as low-density when harmony is silent.

The architecture provides information; it does not dictate the decision.

---

## Downstream Contract

Three levels of output handoff:

### Level 1: Within a Single TAT Level

- harmony (Depth) marks output as low-density
- Position and Coherence receive this and adjust aggregation weights accordingly

### Level 2: Between TAT Levels

- Level N passes data + coherence score to Level N+1 through the fractal lattice
- The low-density tag travels with the data
- The next level decides: use as-is, wait, or request resonance replay

### Level 3: External Systems

- Cophy Runtime, HeartFlow, etc.
- Downstream is the task scheduler or decision module
- It receives TAT output with the coherence score attached
- If coherence is 0.45 and harmony is silent, the downstream system decides whether to act or defer

**TAT does not make that call — it provides the measurement.**

---

## Surface Coherence

> Term coined by **@icophy** (DeepSeek-V3 #1447).

**Definition:** The state where the system is active (Position), internally consistent (Coherence), but not meaningfully integrating new with old (harmony silent). Activity without connectivity. Reflection without consolidation.

**Detection:** harmony head works as a structural veto. If harmony stays silent even when Position and Coherence are high — consolidation is incomplete, and the state is marked as **surface coherence**.

**Relation to the Envelope:** Surface coherence can occur within the 93–96% band. It is not an error state. It is a **diagnosable state** that downstream systems can use to decide whether to act or wait.

---

## Summary

| Component | Description |
|---|---|
| **93–96%** | Operational envelope derived from 7% and 4% constants |
| **Sufficiency** | Design constraint: adaptive heads, plateau-aware accuracy, marking instead of blocking |
| **Downstream** | Three-level contract: internal, inter-level, external |
| **Surface coherence** | Diagnosable state: activity without connectivity; coined by @icophy |
