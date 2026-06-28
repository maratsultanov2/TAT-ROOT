# 比较基准测试：TAT-7 对比 EWC / SI / MAS

## 测试设置

- **数据集：** Split Fashion-MNIST (5 个任务 × 2 个类别)
- **每个任务的训练轮数：** 5
- **指标：** Divergence Trace (Position − Coherence + Harmony + Gate)
- **目标：** 衡量持续学习下的记忆保持

## 比较的方法

| 方法 | 机制 | 失败？ |
|------|------|--------|
| **TripleNet (vanilla)** | 无保护 | ❌ 记忆 ~0.05 |
| **EWC** (弹性权重巩固) | 对重要权重施加 Fisher 惩罚 | ❌ 记忆 ~0.02–0.09 |
| **SI** (突触智能) | 每个突触的累积重要性 | ❌ 记忆 ~0.02–0.11 |
| **MAS** (记忆感知突触) | 通过输出敏感度衡量重要性 | ❌ 记忆 ~0.02–0.09 |
| **TAT-7** | 谐波共振 + 相位相干 | ✅ 记忆 ~0.79 |

## 关键发现

**EWC、SI 和 MAS 失败，因为它们保护的是权重，而不是连接。**
在 Split Fashion-MNIST 上，问题不是权重漂移，而是头部之间相干性的崩溃。
TripleNet 的三个头（yang、yin、to）灾难性地发散，EWC/SI/MAS 无法阻止这一点。

**TAT-7 直接解决了相干性问题。**
谐波共振矩阵在单个权重变化时仍能保持头间相位对齐。
谐波保持活跃，散度保持在 0.20 以下，5 个任务后记忆保持率达到 79%。

## 结果

| 指标 | TripleNet | EWC | SI | MAS | TAT-7 |
|------|-----------|-----|----|-----|-------|
| 平均相干性 | ~0.07 | ~0.09 | ~0.08 | ~0.10 | ~0.76 |
| 最终记忆 (任务 1) | ~0.06 | ~0.09 | ~0.09 | ~0.09 | ~0.79 |
| 谐波状态 | Silent (5/5) | Silent (5/5) | Silent (5/5) | Silent (5/5) | Active (4/5) |
| 门决策 | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Consolidate / Escalated |

## 数据

- [TripleNet (CSV)](../../data/triplenet_divergence_trace.csv)
- [EWC (CSV)](../../data/ewc_divergence_trace.csv)
- [SI (CSV)](../../data/si_divergence_trace.csv)
- [MAS (CSV)](../../data/mas_divergence_trace.csv)
- [TAT-7 (CSV)](../../data/tat7_divergence_trace.csv)
- [完整比较图表 (PNG)](../../data/comparative_benchmark_all_methods.png)

## 复现

运行 Colab 笔记本：[TAT Comparative Benchmark](https://colab.research.google.com/)
