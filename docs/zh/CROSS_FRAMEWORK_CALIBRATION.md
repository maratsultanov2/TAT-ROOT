# 跨框架校准

用于比较 TAT 与 HeartFlow、Cophy Runtime 和 TLAA 在运行时逻辑审计、记忆保持和身份稳定性基准测试中的约定。

## 1. 阈值对齐

| TAT 指标 | TAT 阈值 | HeartFlow 等效项 | 备注 |
|----------|----------|------------------|------|
| 分歧 | < 0.10 (3 个头) | 归一化 < 0.10 (稳定) | 低分歧巩固 |
| 分歧 | 0.10 – 0.30 (5 个头) | 归一化 0.10 – 0.30 (漂移) | 保护性校正激活 |
| 分歧 | > 0.30 (7 个头) | 归一化 > 0.30 (发散) | 拒绝 / TURN 决策 |
| 谐波状态 | 活跃 / 弱 / 沉默 | 稳定 / 漂移 / 发散 | 结构性否决映射 |

HeartFlow 使用 0–100 标度。转换：`TAT_divergence = HeartFlow_divergence / 100`。

## 2. 决策词汇映射

| TAT 门 | HeartFlow 决策 | 语义 |
|--------|----------------|------|
| 巩固 | 保持、加速 | 正常运行，低分歧 |
| 升级 (5 个头) | 转向 | 检测到分歧，保护性校正 |
| 拒绝 (谐波沉默) | 愈合、暂停、休息、传输 | 操作被阻止或推迟 |

## 3. 数据格式约定

每个框架以其原生格式提供结果，并声明 `raw_format` 字段：

| 框架 | raw_format | 典型字段 |
|------|------------|----------|
| TAT | CSV | task_id, phase, position, coherence, divergence, harmony_status, heads, gate_decision |
| HeartFlow | CSV | scenario_id, timestamp, position, coherence, divergence, normalized, harmony_status, h_value, cognitive_load, decision, confidence |
| Cophy Runtime | CSV + markdown | scenario_id, pressure_type, preference_id, applied_correctly, causal_density_at_retrieval |

## 4. 设计理念差异

| 关注点 | TAT | HeartFlow | Cophy Runtime |
|--------|-----|-----------|---------------|
| 角色扮演期间的身份转变 | 当分歧 > 0.30 时触发升级 | 如果暂时则可接受 | 通过行为反事实测量 |
| 执行前与事后审计 | 谐波门在输出前阻止巩固 | 三路调度 (真相/教训/验证) 在执行前 | Dream Cycle 中的事后健康评分 |
| 记忆管理 | 块轮播 (冷却 + 凋亡) | 静态规则 + Q 表 | 基于 TTL 的因果密度修剪 |
| 静态与运行时更新规则 | 门阈值固定；谐波矩阵可学习 | 29 条规则可在不重新训练模型的情况下运行时更新 | 评估框架固定；场景可更新 |

## 5. 归属

| 概念 | 创始人 | 框架 |
|------|--------|------|
| 分歧追踪 (Position − Coherence) | Marat Sultanov | TAT |
| 谐波门 (结构性否决) | Marat Sultanov | TAT |
| 块轮播 | Marat Sultanov | TAT |
| 水壶原理 (充足性) | Marat Sultanov | TAT |
| 操作包络线 (93–96%) | Marat Sultanov | TAT |
| 镜像时间戳 | Marat Sultanov | TAT |
| 表面相干性 | icophy | Cophy Runtime |
| H 值 (0.4·U + 0.3·D − 0.3·A) | yun520-1 | HeartFlow |
| 执行前验证 | yun520-1 | HeartFlow |
| U/D/A/H 四维场 | luoxuejian000 | 独立综合 |

## 6. 参考文献

- [TAT 理论基础](docs/zh/THEORETICAL_FOUNDATION.md)
- [TAT 词汇表](docs/zh/GLOSSARY.md)
- [TAT 比较基准](docs/zh/benchmarks/COMPARATIVE_BENCHMARK.md)

---

*本文件在 TAT-ROOT 中进行版本控制。约定可以随着框架的发展和新数据的出现而更新。*
