# TAT vs Autoencoder: Structural Anomaly Detection

Comparison on structural and statistical anomalies

## Results

| Dataset | TAT F1 | AE F1 | Difference |
|---|---|---|---|
| Hierarchical test (structural anomalies) | 0.520 | 0.080 | +0.440 |
| NASA test (time series with correlations) | 0.050 | 0.633 | -0.583 |


![Comparison](tat_vs_ae_comparison_en.png)

## Conclusion

TAT shows significant advantage on structural anomalies (F1 0.52 vs 0.08). On statistical outliers, autoencoder remains stronger. TAT is a tool for detecting structural breaks.

*Date: 2026-07-09 09:27*