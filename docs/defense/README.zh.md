# TAT 防御模块

[![TAT Defense](https://img.shields.io/badge/TAT-防御-blue)](../docs/defense/README.zh.md)
[![License](https://img.shields.io/badge/License-自定义-red)](../../LICENSE)
[![Status](https://img.shields.io/badge/Status-实验性-yellow)](../docs/defense/README.zh.md)
[![Comparison with AE](https://img.shields.io/badge/比较-AE-green)](../docs/defense/COMPARISON_WITH_AE.md)

基于 TAT 的多层异常检测和洪流管理模块。

## 功能
- 结构故障检测（发散）
- 一致性损失跟踪（和谐）
- 时间异常检测
- 洪流重定向
- 图加密和偏移

## 配置
两种运行模式：
- **高精度** — 最小化误报。
- **高召回** — 最大化异常检测。

## 性能（合成基准）
| 变体 | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| 固定阈值 | 0.690 | 0.571 | 0.870 | 0.690 |
| 加权投票 | **0.845** | **1.000** | 0.609 | **0.757** |
| 自适应权重 | 0.828 | 0.933 | 0.609 | 0.737 |

加权投票变体实现了完美精度（无误报），同时保持良好召回。

## 何处使用 TAT Defense

TAT Defense 专为检测**结构断裂**而设计——不是统计离群值，而是顺序、层次结构或一致性的破坏。

### 示例 1：层次异常（合成数据）

数据由有序块组成（例如，类别、步骤、模块）。异常 = 块交换或顺序破坏。

- **TAT Defense:** F1 = 0.52
- **自编码器:** F1 = 0.08

TAT 明显胜出，因为它检测的是结构断裂，而不是数值偏差。

### 示例 2：时间序列相关性（类似 NASA 的数据）

数据由相关时间序列组成。异常 = 一个通道破坏与其他通道的相关性。

- **TAT Defense:** F1 = 0.05
- **自编码器:** F1 = 0.63

这里自编码器胜出，因为异常是重建误差中的统计离群值。这是 TAT 不擅长的领域。

### 何时选择 TAT Defense

- **当异常涉及顺序、层次结构或序列时，使用 TAT**（物流、对话流、制造步骤、代码结构、知识分类法）。
- **当异常涉及罕见值或分布离群值时，使用自编码器**（金融欺诈、传感器尖峰、基于值的质量控制）。

TAT 不是通用的异常检测器。它是结构断裂的专家。

## 与其他方法比较
下表列出了已知异常检测方法在公开文献中的报告性能。TAT Defense 在加权投票模式下表现出具有竞争力的 F1 和独特的精度（1.0）。

| 方法 | F1 | Precision | Recall | 来源 |
|---|---|---|---|---|
| **TAT Defense（加权投票）** | **0.757** | **1.000** | 0.609 | 本工作（合成） |
| Isolation Forest | 0.81–0.95 | 0.76–0.91 | 0.78–1.00 | Nature 2025 |
| Autoencoder | 0.86 | 0.82 | 0.84 | Nature 2025 |
| One‑Class SVM | 0.79 | 0.72 | 0.75 | Nature 2025 |
| LSTM (NAB) | 0.688 | — | — | NAB benchmark |

## 许可证
自定义 TAT 许可证 — 见 [LICENSE](../../LICENSE)。

## 状态
✅ 原型就绪，测试已完成。
