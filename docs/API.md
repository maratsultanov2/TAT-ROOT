# TAT Public API

## Anchors
- adaptive_anchors(series, window=5, tol=0.1)
- anchor_depth(series, anchors)

## Coherence
- coherence(v1, v2, theta=1.987)
- to_complex(x, theta=1.987)
- coherence_matrix(data, theta=1.987)

## Monitor
- tat_monitor(series, window=3, sigma=2.0)
- permutation_test(series, n_perm=1000)

## Utils
- normalize(x)
- standardize(x)
- triadic_agreement(coarse, fine, error)
- estimate_drift(series)
- block_shuffle(series, block_size=3)
