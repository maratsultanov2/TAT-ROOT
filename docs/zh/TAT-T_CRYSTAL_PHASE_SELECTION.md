# TAT-T Crystal: 通过网格扫描选择相位

## 概述
TAT-T Crystal 是一个三层架构（DNA/RNA/Protein），具有可配置的相移。本文档展示了相位空间扫描的结果。

## 方法论
- **架构:** 3/5/11 头。
- **相位扫描:** 4×4×4 网格（64 组合），相位 0.00–0.15 步长 0.05。
- **训练:** 每个组合 30 个周期。
- **数据:** 来自 Resonance-Missile、Cophy、Agora/mnemo 的组合 142 步。
- **硬件:** NVIDIA T4 GPU，运行时间约 2 小时 5 分钟。

## 指标与结果
| 配置 | mean_div | corr_rna_protein | low_ratio | high_ratio | score |
|------|----------|------------------|-----------|------------|-------|
| Baseline (0.00, 0.05, 0.10) | 0.151 | 0.696 | 3.5% | 0% | 0.911 |
| **Candidate (0.00, 0.15, 0.15)** | **0.173** | **0.854** | **5.6%** | **0%** | **0.802** |

![发散轨迹对比](../images/tat_crystal_phase_comparison.png)

## 结论
最佳相位配置为 **(0.00, 0.15, 0.15)**。它将 RNA–Protein 相关性提高了 +0.158，同时保持 high_ratio = 0%。

## 可复现性
见 `/notebooks/TAT-T_Crystal_Phase_Scan.ipynb`.
