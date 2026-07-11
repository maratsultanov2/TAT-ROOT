# 用于结构异常检测的直接上下文比较方法

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## 作者与角色

- **Marat Sultanov** — 直接上下文比较方法、TAT 架构、Triplenet 模型以及 v2、v3、v4 和 v4nat 所有实验的作者。
- **Rastislav Drahos (DanceNitra)** — 独立合著者。设计了 value‑obscuring reversion 固定装置，进行了多次审计，用不同的嵌入器重现了该方法，并发现了任务的分解。

## v4nat heldout 结果（46 个示例）

- Accuracy: 0.9130
- Precision: 0.8636
- Recall: 0.9500
- F1: **0.9048**
- AUROC: **0.9635**
- 混淆矩阵: [23 3; 1 19]

## 独立复现

Rastislav Drahos 使用不同的嵌入器复现了该方法：F1 0.930, AUROC 1.000。

## 完整报告与附件

- [English](README.md) | [Русский](README.ru.md) | [中文](README.zh.md)
- [预测 (CSV)](predictions.csv)
- [指标 (JSON)](metrics.json)
- [报告图表](final_report.png)

*发布日期: 2026-07-11 21:21*
