"""
TAT Public — Advanced Usage Example
=====================================
Demonstrates: adaptive anchors, coherence, TAT-Monitor, triadic agreement,
drift estimation, and block-shuffle permutation on synthetic data
that mimics a real-world scenario (two correlated time series with drift).
"""

import numpy as np
import matplotlib.pyplot as plt
from tat_public import (
    adaptive_anchors, coherence, tat_monitor,
    triadic_agreement, estimate_drift, block_shuffle
)
from scipy.stats import pearsonr

print("=" * 60)
print("TAT ADVANCED USAGE EXAMPLE")
print("=" * 60)

# ------------------------------------------------------------
# 1. Generate synthetic data: two correlated series with drift
# ------------------------------------------------------------
np.random.seed(42)
n_points = 50
step = np.arange(n_points)
drift_true = 0.15
shared_signal = drift_true * step + np.random.randn(n_points) * 0.3
series1 = shared_signal + np.random.randn(n_points) * 0.2  # framework A
series2 = shared_signal + np.random.randn(n_points) * 0.2  # framework B

print(f"Series 1 drift: {estimate_drift(series1):.3f}")
print(f"Series 2 drift: {estimate_drift(series2):.3f}")
r, _ = pearsonr(series1, series2)
print(f"Pearson correlation: {r:.3f}")

# ------------------------------------------------------------
# 2. Adaptive Anchors — find structural minima
# ------------------------------------------------------------
anchors1 = adaptive_anchors(series1, window=5, tol=0.1)
anchors2 = adaptive_anchors(series2, window=5, tol=0.1)
print(f"Anchors in series1: {len(anchors1)}")
print(f"Anchors in series2: {len(anchors2)}")

# ------------------------------------------------------------
# 3. TAT-Monitor — detect anomalies
# ------------------------------------------------------------
peaks1, sig1, thr1 = tat_monitor(series1, window=3, sigma=2.0)
peaks2, sig2, thr2 = tat_monitor(series2, window=3, sigma=2.0)
print(f"Monitor peaks in series1: {len(peaks1)}")
print(f"Monitor peaks in series2: {len(peaks2)}")

# ------------------------------------------------------------
# 4. Coherence between segments
# ------------------------------------------------------------
c = coherence(series1[10:30], series2[10:30])
print(f"Coherence between segments: {c:.4f}")

# ------------------------------------------------------------
# 5. Triadic Agreement (using three metrics)
# ------------------------------------------------------------
# For demonstration, use series1 as coarse, series2 as fine, and their difference as error
error_metric = np.abs(np.diff(series1, prepend=series1[0]))
agreement = triadic_agreement(series1, series2, error_metric)
print(f"Triadic agreement (mean): {agreement.mean():.4f}")

# ------------------------------------------------------------
# 6. Block-shuffle permutation test for correlation significance
# ------------------------------------------------------------
n_perm = 5000
null_r = []
drift1 = estimate_drift(series1)
for _ in range(n_perm):
    residuals = series1 - drift1 * step
    shuffled_residuals = block_shuffle(residuals, block_size=3)
    shuffled_series = drift1 * step + shuffled_residuals
    null_r.append(pearsonr(shuffled_series, series2)[0])
null_r = np.array(null_r)
p_value = np.mean(null_r >= r)
print(f"Permutation test p-value: {p_value:.4f}")
print(f"Null mean correlation: {null_r.mean():.4f}")

# ------------------------------------------------------------
# 7. Visualisation
# ------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("TAT Advanced Analysis", fontsize=14, fontweight="bold")

axes[0,0].plot(step, series1, "b-o", label="Framework A")
axes[0,0].plot(step, series2, "r-s", label="Framework B")
axes[0,0].scatter(step[anchors1], series1[anchors1], c="blue", s=80, marker="v")
axes[0,0].scatter(step[anchors2], series2[anchors2], c="red", s=80, marker="v")
axes[0,0].set_title("Time Series with Adaptive Anchors")
axes[0,0].legend(fontsize=7)
axes[0,0].grid(alpha=0.3)

axes[0,1].plot(step, sig1, "b-", label="Monitor A")
axes[0,1].plot(step, sig2, "r-", label="Monitor B")
axes[0,1].axhline(thr1, color="blue", linestyle="--", alpha=0.3)
axes[0,1].axhline(thr2, color="red", linestyle="--", alpha=0.3)
axes[0,1].scatter(step[peaks1], sig1[peaks1], c="blue", s=60, marker="^")
axes[0,1].scatter(step[peaks2], sig2[peaks2], c="red", s=60, marker="^")
axes[0,1].set_title("TAT-Monitor")
axes[0,1].legend(fontsize=7)
axes[0,1].grid(alpha=0.3)

axes[1,0].hist(null_r, bins=30, alpha=0.7, color="steelblue")
axes[1,0].axvline(r, color="red", linestyle="--", linewidth=2, label=f"Observed r = {r:.3f}")
axes[1,0].set_title(f"Block-Shuffle Permutation Test (p = {p_value:.4f})")
axes[1,0].legend()
axes[1,0].grid(alpha=0.3)

axes[1,1].axis("off")
summary = (
    f"Drift A: {drift1:.3f}\n"
    f"Drift B: {estimate_drift(series2):.3f}\n"
    f"Correlation: {r:.3f}\n"
    f"Permutation p: {p_value:.4f}\n"
    f"Anchors A: {len(anchors1)}\n"
    f"Anchors B: {len(anchors2)}\n"
    f"Monitor peaks A: {len(peaks1)}\n"
    f"Monitor peaks B: {len(peaks2)}\n"
    f"Coherence: {c:.4f}\n"
    f"Agreement (mean): {agreement.mean():.4f}"
)
axes[1,1].text(0.1, 0.9, summary, transform=axes[1,1].transAxes, fontsize=10, family="monospace", va="top")

plt.tight_layout()
plt.savefig("tat_advanced_example.png", dpi=150)
plt.show()
print("\n✅ Advanced example completed.")
