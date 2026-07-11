# TAT vs Baseline：Value‑Obscuring Reversion 的结构异常检测

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Code: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)

## 引言

**Value‑obscuring reversion** 是在对话系统中检测"静默回滚"尝试的任务。用户想要恢复之前更改的值，但**既不命名该值，也不使用明确的回滚命令**（例如"go back to what we had"、"undo that change"）。标准方法（余弦相似度、关键字搜索、值匹配）在此几乎无效——F1 在 0.03 到 0.60 之间。

**TAT (TreeAngleTap)** 展示了捕获**结构信号**的能力——话语与编辑历史之间的联系，而非表面的词汇匹配。

数据由独立合著者 **Rastislav Drahos** (DanceNitra) 提供。数据集设计用于逐步排除可能的"捷径"：实体记忆、关键字、值字符串。每个后续版本都比前一个更难。

## 方法论

### 特征

对于每个示例 (old → new → candidate)，构建反映**对话结构**而非语义的特征向量：

- **Theme** — 实体标识符（归一化哈希）。
- **Role** — 链条中的位置 (0.0, 0.5, 1.0)。
- **Emotion** — 意图标记 (1.0 revert, 0.0 keep, 0.5 未知)，基于固定词典计算。
- **Meaning** — 新旧值的长度比。
- **Goal / Asserted Value** — 候选者断言哪个值（旧、新或无）。
- **Cosine Similarity** (v4) — 候选者与旧/新上下文行的余弦相似度。

### 模型

**Triplenet** — 具有三条并行路径 (Yang, Yin, To) 和从训练集中提取的常量模式的架构。训练：100 epoch，CPU，不到2秒。

### 协议

训练**仅**在源数据（original fixture + first heldout）上进行。测试集 (v2, v3, v4) **不用于**训练、特征构建或阈值调整。阈值固定 (0.5)。

## 结果

| 测试 | F1 (TAT) | F1 (Baseline) | AUROC | 关键挑战 |
|------|----------|---------------|-------|----------|
| v2 (新短语) | 1.0000 | 0.6000 (cosine) | 1.0000 | 无回滚词的解释 |
| v3 (断言值) | 1.0000 | N/A | 1.0000 | 仅结构值断言 |
| v4 (共指，已修正) | 0.6667 | N/A | 0.6362 | 未命名值的共指 |

**基线对比 (v2)：**
- Object/value match: F1 = 0.03
- Cosine similarity: F1 = 0.60
- Keyword rule (基于回滚/保留词): F1 = 1.00 (v2)，但在 v3 和 v4 上降至随机水平

只有 TAT 在三个难度级别上保持高检测质量。

在修正后的 v4 上，TAT 实现了 **recall 1.0**（检测到所有回滚），但由于误报，precision 为 0.5。失败点被精确定位：模型完美检测到候选者是否引用了上下文中的角色 (named_new 20/20)，但无法将该角色链接到特定锚点（旧值或当前值）。这是链的第二跳，也是下一个改进目标。

## 致谢

特别感谢 **Rastislav Drahos** (DanceNitra) 构建数据集、独立验证结果并进行建设性科学讨论。

**链接：**
- Rastislav 的仓库：[github.com/DanceNitra/agora](https://github.com/DanceNitra/agora/tree/main/agora_output/public_fixtures)
- TAT-ROOT: [github.com/maratsultanov2/TAT-ROOT](https://github.com/maratsultanov2/TAT-ROOT)

## 许可证

- **代码** (notebooks, scripts): AGPL v3.0
- **文档、结果、图形**: CC BY-NC-ND 4.0
- **数据 (fixtures)**: MIT (归 Rastislav Drahos 所有)
- **模型 (.pt)**: Custom TAT License (商业使用需授权)

## 如何复现

所有 Google Colab notebook 位于 [`notebooks/`](notebooks/) 文件夹中。它们加载预训练模型并输出与上表相同的指标。无需额外数据——数据集自动从 DanceNitra 仓库下载。

*发布日期：2026-07-11 09:49*
