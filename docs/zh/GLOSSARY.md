# TAT 词汇表

本词汇表定义了 TAT 及相关框架（Cophy Runtime、HeartFlow、TLAA）中使用的关键术语。术语按字母顺序排列。

## 术语

| 术语 | 作者 | 定义 |
|------|------|------|
| **操作包络线 93–96% (Operational envelope)** | Marat Sultanov (TAT) | 充足性边界：下界 93% = 100% − 7%（7 个头，T_max=0.7，0.7% 噪声），上界 96% = 100% − 4%（连接权重乘数=4）。系统不追求 100% 准确率。 |
| **差异追踪 (Divergence trace)** | Marat Sultanov (TAT) | 通过 `divergence = Position − Coherence` 计算的诊断信号。记忆漂移的先行指标：差异上升可在表面指标显示退化之前预测相干性崩溃。 |
| **块轮播 (Chunk carousel)** | Marat Sultanov (TAT) | 无丢弃/延迟的记忆管理机制：活跃块（具有强连接）保持在前面，未使用的块自然冷却并后退，如果未来上下文共振则重新激活，如果连接完全断裂则发生凋亡。 |
| **镜像时间戳 (Mirror timestamp)** | Marat Sultanov (TAT) | 双格式时间戳 `DD.MM.YYYY / YYYY.MM.DD`，实现直接机器访问（右侧，整数比较，零解析）和人类可读性（左侧），对称轴（斜杠）用于部分损坏时的恢复。 |
| **前置验证 (Pre-execution verification)** | yun520-1 (HeartFlow) | 在工具执行之前进行的审计，允许在生成令牌和产生副作用之前做出 BLOCK/MODIFY 决定。 |
| **水壶原理 (Kettle Principle)** | Marat Sultanov (TAT) | 充足即能效：7 个头是沸水，仅在任务需要时使用。大多数巩固发生在沸点以下，这是正确的行为，而非退化。 |
| **表面相干性 (Surface coherence)** | icophy (Cophy Runtime) | 代理看似活跃（高 Position）且内部一致（正常 Coherence），但未将新信息与现有记忆有意义地整合（谐波沉默，低因果密度）的状态。 |
| **位置 (Position)** | Marat Sultanov (TAT) | 模型对其输出的信心，以最大 softmax 概率衡量。结构头（独奏）权重：0.55。 |
| **相干性 (Coherence)** | Marat Sultanov (TAT) | 头之间结构一致性的度量：`coherence = |w1 · conj(w2)| / (|w1| · |w2| + ε)`。低相干性触发谐波门。 |
| **谐波门（结构否决）(Harmony gate / Structural veto)** | Marat Sultanov (TAT) | 谐波头权重 2.0：如果谐波沉默，无论 Position 和 Coherence 的值如何，都拒绝巩固。 |
| **H 值 (H-value)** | yun520-1 (HeartFlow) | 场健康公式：`H = 0.4·U + 0.3·D − 0.3·A`，其中 U/D/A 是归一化的效用、方向和权威。 |

## 归属

- **Marat Sultanov** — TAT (TreeAngleTap) 的创造者。[GitHub](https://github.com/maratsultanov2)
- **icophy** — Cophy Runtime 的创造者。[GitHub](https://github.com/icophy)
- **yun520-1** — HeartFlow 的创造者。[GitHub](https://github.com/yun520-1)

## 参考文献

- [TAT 理论基础](THEORETICAL_FOUNDATION.md)
- [跨框架校准](CROSS_FRAMEWORK_CALIBRATION.md)（即将推出）

---

*本词汇表是 TAT-ROOT 的一部分。所有定义均为公开发表的现有技术，并在 GitHub 上带有时间戳。*
