# TAT Public API Reference

## `tat_public.coherence`
- `to_complex(x: np.ndarray, theta: float = 1.987) -> np.ndarray` — Convert real-valued array to complex TAT space.
- `coherence(v1: np.ndarray, v2: np.ndarray, theta: float = 1.987) -> float` — Compute complex coherence between two vectors.
- `coherence_matrix(data: np.ndarray, theta: float = 1.987) -> np.ndarray` — Compute pairwise coherence matrix.

## `tat_public.anchors`
- `adaptive_anchors(series: np.ndarray, window: int = 5, tol: float = 0.1) -> np.ndarray` — Find structural minima in a 1D series.
- `anchor_depth(series: np.ndarray, anchors: np.ndarray) -> np.ndarray` — Compute relative depth of each anchor.

## `tat_public.monitor_base`
- `tat_monitor(series: np.ndarray, window: int = 3, sigma: float = 2.0) -> tuple` — Detect structural anomalies. Returns `(peaks, signal, threshold)`.
- `permutation_test(series: np.ndarray, n_perm: int = 1000, window: int = 3, sigma: float = 2.0) -> tuple` — Permutation test for monitor significance. Returns `(observed, null_distribution, p_value)`.

## `tat_public.utils`
- `normalize(x: np.ndarray) -> np.ndarray` — Normalize array to [0, 1].
- `standardize(x: np.ndarray) -> np.ndarray` — Standardize to zero mean and unit variance.
- `triadic_agreement(coarse, fine, error, invert_coarse=False, invert_fine=False) -> np.ndarray` — Compute triadic agreement.
- `estimate_drift(series: np.ndarray) -> float` — Estimate linear drift (slope) of a 1D series.
- `block_shuffle(series: np.ndarray, block_size: int = 3) -> np.ndarray` — Shuffle preserving local dependence.
