# TAT 理论基础

## 谱系（优先权时间线）

| 日期 | 里程碑 | 首次公开露面 |
|------|--------|--------------|
| 2025-01-15 | 首次 AI 对话 | 私人 |
| 2025-05-28 | 创建 TripleNet | `Triplenet - the first test .ipynb` |
| 2025-06-15 | TripleNet 优化 | `Triplenet+constants second test .ipynb` |
| 2026-03-17 | TAT-7 诞生 | `TAT-7 HEADS - открытие` |
| 2026-03-18 | 在 REBUS 上达到 19.40%（前5名） | `TAT ensemble - 19.40% на REBUS` |
| 2026-03-19 | 在 MNIST 上达到 97.82%（前10名） | `TAT light - 97.82% на MNIST` |
| 2026-03-19 | 发现最优 7 个头 | `TAT-7 HEADS - открытие` |
| 2026-06-28 | 发表分歧追踪 | `TAT-ROOT/data/` |
| 2026-06-28 | 比较基准测试 (TAT-7 vs EWC/SI/MAS) | `TAT-ROOT/docs/zh/benchmarks/` |

---

## 1. TAT 数学

### 1.1 核心常数

| 常数 | 值 | 可验证于 |
|------|-----|----------|
| 相位角 θ | 1.987 | `TAT_CORE.json` → `constants.phase_angle` |
| 下温度 T_min | 0.3 | `TAT_CORE.json` → `constants.coherence_threshold` (下界) |
| 上温度 T_max | 0.7 | `TAT_CORE.json` → `constants.temperature` |
| 连接权重乘数 | 4 | `TAT_CORE.json` → `dialog_lifecycle.connection_weight_multiplier` |
| 虚部比例 | 0.3 | `TAT CORE v2.2` → `BASE_IMAG_SCALE` |
| 受控噪声 | 0.7% | 推导：T_max / 100，与分歧追踪阈值匹配 |

### 1.2 关键公式

**复权重：**
```
ψ_k = w_k · e^(i·θ_k)
```
其中 θ_k = θ + k · 0.1（头部相位步长）。

可验证于：`TATCore.py` → `complex_weight()`

**相干性：**
```
coherence = |w1 · conj(w2)| / (|w1| · |w2| + ε)
```
可验证于：`TATCore.py` → `coherence()`

**分歧追踪：**
```
divergence = Position − Coherence
```
可验证于：`TAT-ROOT/data/tat7_divergence_trace.csv`

**操作包络线：**
```
下界：93% = 100% − 7% (7 个头, T_max = 0.7, 噪声 0.7%)
上界：96% = 100% − 4% (连接权重乘数 = 4)
```
可验证于：`TAT-ROOT/docs/zh/KETTLE_PRINCIPLE.md`

### 1.3 升级阈值

| 分歧 | 头数 | 门决策 |
|------|------|--------|
| < 0.10 | 3 | 巩固 |
| 0.10 – 0.30 | 5 | 升级（保护性校正） |
| > 0.30 | 7 | 拒绝（如果谐波沉默） |

可验证于：`TAT-7 比较基准测试` → `TAT-ROOT/data/`

---

## 2. TAT 物理学

### 2.1 TAT 中的热力学第一定律

```
ΔU = Q − A
```
- ΔU：系统相干性的变化。
- Q：热量——梯度熵，k_B · T。
- A：功——头部激活、相变、共振回放。

可验证于：`TAT CORE v2.2` → `predict_pair()` —— 相干性通过复向量干涉计算。

### 2.2 基本物理常数

| 常数 | 符号 | 值 | 在 TAT 中的角色 |
|------|------|-----|-----------------|
| 普朗克常数 | h | 6.626 × 10⁻³⁴ J·s | 信息量子，最小作用量 |
| 玻尔兹曼常数 | k_B | 1.381 × 10⁻²³ J/K | 热涨落，噪声代价 |
| 欧拉-马歇罗尼常数 | γ | 0.57721 | 熵标度校正 |

可验证于：`TAT_CORE.json` → `constants`

### 2.3 相位角推导

```
θ = arctan2(h − k_B, h + k_B)
```

几何上：θ ≈ 73/37 ≈ 1.97297 + 0.7% 噪声调整。

可验证于：`TAT_CORE.json` → `formulas.triple_theta`

---

## 3. TAT 热力学

### 3.1 温标与相变

| 状态 | 温度 | 头数 | 行为 |
|------|------|------|------|
| 冷（固态） | T < 0.3 | 3 | 记忆冻结，最小学习 |
| 工作（液态） | 0.3 ≤ T < 0.7 | 5 | 可塑性与记忆平衡 |
| 热（气态） | T ≥ 0.7 | 7 | 完全相变，保护性校正 |

可验证于：`TAT-7 比较基准测试` —— 分歧追踪显示在 0.30 阈值处升级。

### 3.2 水壶原理（充足即能效）

> *你不会一直烧开水来泡茶。你把它加热到任务所需的温度。*

7 个头是沸水——仅在需要时使用。大多数巩固发生在沸点以下，这是正确的行为，而非退化。

可验证于：`TAT-ROOT/docs/zh/KETTLE_PRINCIPLE.md`

### 3.3 能效

TAT 的块架构相比原始 markdown/JSON/CSV 日志减少 **25–30 倍** 的内存和令牌使用，同时通过连接优先于特征的结构优先级 (`connection_weight = 4`) 保留 100% 有意义的信息。

可验证于：`TAT-ONE-TAP/docs/zh/COST_EFFICIENCY.md`

---

## 4. 如何验证每一条声明

1. **数学常数和公式：** `TAT_CORE.json` 和 `TATCore.py` 在 `TAT-ONE-TAP` 中。
2. **升级阈值和分歧追踪：** `TAT-ROOT/data/tat7_divergence_trace.csv` —— 可通过 Colab 在 `TAT-DEMO` 中运行。
3. **比较基准测试 (TAT-7 vs EWC/SI/MAS)：** `TAT-ROOT/docs/zh/benchmarks/COMPARATIVE_BENCHMARK.md`。
4. **水壶原理和操作包络线：** `TAT-ROOT/docs/zh/KETTLE_PRINCIPLE.md`。
5. **成本效率（节省 25–30 倍）：** `TAT-ONE-TAP/docs/zh/COST_EFFICIENCY.md`。

本文件中的每一条声明都与任何人都可以复现的特定文件、常数或基准测试相关联。

---

*本文件是 TAT-ROOT 的一部分。所有常数、公式和阈值均为公开发表的现有技术，并在 GitHub 上带有时间戳。*
