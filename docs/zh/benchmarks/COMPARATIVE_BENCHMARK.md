# 比较基准测试：TripleNet 对比 TAT-7

## 测试设置

- **数据集：** Split Fashion-MNIST (5 个任务 × 2 个类别)
- **每个任务的训练轮数：** 5
- **指标：** Divergence Trace (Position − Coherence + Harmony + Gate)
- **目标：** 衡量持续学习下的记忆保持

## 结果

| 指标 | TripleNet (无保护) | TAT-7 (谐波共振) |
|------|-------------------|------------------|
| 平均相干性 | ~0.15 | ~0.76 |
| 平均散度 | ~0.85 | ~0.13 |
| 谐波状态 | Silent (5/5) | Active (4/5) |
| 门决策 | Withhold (5/5) | Consolidate / Escalated |
| 任务 1 记忆保持 | ~0.05 | ~0.79 |

## 这证明了什么

1. **散度追踪是先行指标。** TripleNet 的相干性在任务 1 后崩溃，散度飙升至 0.30 以上——门正确阻止了所有后续整合。TAT-7 在所有任务中将散度保持在 0.20 以下，门允许整合。

2. **谐波共振保护记忆。** TAT-7 的谐波头在 4/5 任务中保持活跃，为虚假整合提供结构性否决。TripleNet 没有这种机制——谐波始终沉默。

3. **记忆保持是架构性的，而非偶然的。** 5 个任务后，TAT-7 在任务 1 上保持了 79% 的相干性。TripleNet 仅保持 5%。差异在于架构。

## 数据

- [TripleNet 散度追踪 (CSV)](../../data/triplenet_divergence_trace.csv)
- [TAT-7 散度追踪 (CSV)](../../data/tat7_divergence_trace.csv)
- [比较图表 (PNG)](../../data/comparative_benchmark.png)

## 复现

运行 Colab 笔记本：[TAT Comparative Benchmark](https://colab.research.google.com/)
