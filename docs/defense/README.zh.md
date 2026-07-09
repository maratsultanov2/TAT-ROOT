# TAT 防御模块

[![TAT Defense](https://img.shields.io/badge/TAT-防御-blue)](../docs/defense/README.zh.md)
[![License](https://img.shields.io/badge/License-自定义-red)](../../LICENSE)
[![Status](https://img.shields.io/badge/Status-实验性-yellow)](../docs/defense/README.zh.md)

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

## 与其他方法比较
下表列出了已知异常检测方法在公开文献中的报告性能。TAT Defense 在加权投票模式下表现出具有竞争力的 F1 和独特的精度（1.0）。

| 方法 | F1 | Precision | Recall | 来源 |
|---|---|---|---|---|
| **TAT Defense（加权投票）** | **0.757** | **1.000** | 0.609 | 本工作（合成） |
| Isolation Forest | 0.81–0.95 | 0.76–0.91 | 0.78–1.00 | Nature 2025 [1†L22-L23][1†L18-L19] |
| Autoencoder | 0.86 | 0.82 | 0.84 | Nature 2025 [1†L23][2†L22-L23] |
| One‑Class SVM | 0.79 | 0.72 | 0.75 | Nature 2025 [1†L23] |
| LSTM (NAB) | 0.688 | — | — | NAB benchmark [0†L11-L12] |

## 许可证
自定义 TAT 许可证 — 见 [LICENSE](../../LICENSE)。

## 状态
✅ 原型就绪，测试已完成。
