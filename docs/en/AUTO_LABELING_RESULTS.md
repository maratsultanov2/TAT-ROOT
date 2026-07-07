# Automatic Labeling Results (without teacher)

Two approaches tested on combined dataset (142 steps, 3 features):

- **Fixed:** 5 manually selected pivot points.
- **Adaptive:** threshold and number of points automatically determined by structural analysis.

| Approach | Points | Mean correlation | Note |
|---|---|---|---|
| Fixed | 5 | 0.538 | Baseline |
| Adaptive | 10 (system‑detected) | **0.721** | Self‑discovered structure |

The adaptive approach significantly outperforms the fixed baseline, confirming that the system can identify its own optimal structure.

A production module based on this method is under development and will be released soon.

📊 Graphs:
- [Fixed 5 pivots](../images/tat_crystal_auto_labels_5d.png)
- [Adaptive pivots](../images/tat_crystal_adaptive_labels_auto_fixed.png)
