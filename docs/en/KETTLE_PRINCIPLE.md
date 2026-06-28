# The Kettle Principle: Sufficiency as Energy Efficiency

TAT does not chase 100% accuracy. This is not a compromise. It is a design constraint derived from the architecture itself.

## Why "kettle"?

You don't boil water constantly to make tea. You heat it to the temperature the task requires — hot, not boiling. Boiling water is a specific mode for a specific thermal requirement. Keeping it at a boil wastes energy.

TAT's heads work the same way.

- **3 heads** — hot water. Simple tasks, low entropy. The system is stable.
- **5 heads** — hotter water. Moderate tasks, working regime.
- **7 heads** — boiling water. High entropy, complex tasks. Full phase transition with protective correction.

Most consolidation runs below the boiling point, and that is correct behavior, not degradation. 7-head mode is not the default that gets downgraded — it is a specific tool for a specific thermal requirement.

## What this means in practice

- The **93–96% operational envelope** is not a calibrated target. It is a consequence of structural constants: 7 heads, T_max=0.7, and the 0.7% noise budget.
- When a task falls within the envelope, TAT consolidates. When it falls below 93%, TAT escalates to 7 heads. If escalation fails to restore coherence, TAT withholds — it does not produce low-quality output.
- **Sufficiency** does not mean "good enough." It means the architecture uses exactly the energy required, and no more.

New readers often ask: *"Why not 100%?"* This section is the answer.
