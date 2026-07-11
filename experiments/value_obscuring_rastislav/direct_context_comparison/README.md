# Direct Context Comparison Method for Structural Anomaly Detection

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## Authors and Roles

- **Marat Sultanov** — author of the direct context comparison method, TAT architecture, Triplenet model, and all experiments on v2, v3, v4, and v4nat.
- **Rastislav Drahos (DanceNitra)** — independent co‑author. Designed the value‑obscuring reversion fixtures, conducted multiple audits, reproduced the method with a different embedder, and discovered the factorization of the task.

## Results on v4nat heldout (46 examples)

- Accuracy: 0.9130
- Precision: 0.8636
- Recall: 0.9500
- F1: **0.9048**
- AUROC: **0.9635**
- Confusion matrix: [23 3; 1 19]

## Independent reproduction

Rastislav Drahos reproduced the method with a different embedder: F1 0.930, AUROC 1.000.

## Full report and artifacts

- [English](README.md) | [Русский](README.ru.md) | [中文](README.zh.md)
- [Predictions (CSV)](predictions.csv)
- [Metrics (JSON)](metrics.json)
- [Report graph](final_report.png)

*Published: 2026-07-11 21:21*
