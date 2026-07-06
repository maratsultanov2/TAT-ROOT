# TAT-T Crystal on Financial Data — Adaptive Phases

**Status:** Validated — empirical case study.

## Overview

This document presents a case study of TAT-T Crystal applied to financial time series. The model was trained to predict market volatility using only price data of three stocks (AAPL, MSFT, GOOGL). Unlike previous benchmarks on LLM data, this case demonstrates TAT's ability to adapt to noisy, high‑frequency numerical streams.

## Architecture & Setup

- **Layers:** DNA (3 heads), RNA (5 heads), Protein (11 heads) — total 19 heads.
- **Parameters:** ~1.94M (FP32), memory footprint ~7.75 MB.
- **Phases:** learnable (adaptive) — initialised at (0.00, 0.15, 0.15).
- **Training:** 300 epochs, Adam lr=1e-3, loss = MSE(divergence, volatility) + 0.1×harmony.
- **Hardware:** NVIDIA T4 GPU, runtime ~5–7 minutes.

## Data & Target

- **Source:** Yahoo Finance (90 days, daily close prices for AAPL, MSFT, GOOGL).
- **Features:** 3-dimensional price vector.
- **Target:** Normalised 5-day rolling volatility (standard deviation / mean).

## Results

| Metric | Value |
|---|---|
| Correlation (divergence vs volatility) | **0.952** |
| Mean divergence | 0.402 |
| Fraction in 0.3–0.5 corridor | 37.1% |
| Fraction >0.5 | 32.3% |
| Final phases | DNA=0.000, RNA=0.150, Protein=0.147 |

The model learned to track volatility with high fidelity. The Protein phase shifted slightly from 0.150 to 0.147, indicating that the system self‑calibrated to the data structure.

## Visualisation

![Divergence vs Volatility](../images/tat_crystal_financial_adaptive_phases.png)

## Reproducibility

A fully self‑contained Colab notebook is available in `/notebooks/TAT-T_Crystal_Financial_Adaptive_Phases.ipynb`. It downloads the data, runs the training, and reproduces all metrics and plots.

## Conclusion

TAT-T Crystal with adaptive phases successfully captures financial market dynamics, achieving high correlation with volatility. This case extends the applicability of TAT beyond language models to general time‑series analysis.

## References

- TAT-T Crystal Phase Selection
- Cross‑Framework Report #1466
