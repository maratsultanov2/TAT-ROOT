# TAT-T 三头联盟：三演员架构

## 概述
TAT-T（三重 TAT-7）使用三个并行的演员，具有不同的相移和结构记忆。本文档展示了两个独立的验证。

## 1. 合成基准
| 阶段 | 平均发散 | 超过阈值 |
|------|---------|----------|
| 单一 TAT-7 | 2.1 | 9/10 |
| 双阶段 | 1.7 | 8/10 |
| **三阶段** | **0.13** | **3/10** |

*减少：从单一到三阶段减少 94%*

![合成基准比较](../images/triumvirate_synthetic.png)

## 2. 跨框架验证
| 数据集 | 单一 | 三阶段 |
|--------|------|--------|
| Cophy (31 步) | 0.154 | **-0.146** |
| Resonance-Missile (101 步) | 0.006 | **-0.245** |
| Agora/mnemo (5 步) | 0.002 | **-0.450** |

![跨框架验证结果](../images/triumvirate_cross_framework.png)

## 结论
TAT-T 在合成数据和真实数据上均能持续提高相干性。

## 可复现性
见 `/notebooks/TAT-T_Triumvirate_Synthetic.ipynb` 和 `/notebooks/TAT-T_CrossFramework_Validation.ipynb`.
