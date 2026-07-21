# TAT 出版物

本页面汇集了在不同领域中验证 TAT 框架的同行评审和存档出版物。结合理论基础和跨框架校准，这些出版物构成了 TAT‑ROOT 生态系统的核心。

## 📊 关键结果一览

| 领域 | 方法 | 关键指标 | DOI |
|------|------|----------|-----|
| **代理系统（回退检测）** | TAT‑Monitor | F1 = 0.926, AUROC = 0.986 | [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757) |
| **凝聚态物理（自旋-电荷分离）** | TAT‑Defense | 跨框架收敛 | [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316) |

---

## 📄 出版物 1：TAT-Monitor

**标题:** *When the Benchmark Shortcut Becomes the Answer*  
**作者:**  
- **Marat Sultanov** ([@maratsultanov2](https://github.com/maratsultanov2)) — 独立研究员，俄罗斯联邦  
- **Rastislav Drahos** ([@DanceNitra](https://github.com/DanceNitra)) — Agora Scientific，捷克共和国  

**状态:** 预印本 / Zenodo 存档 (DOI)  
**年份:** 2026  
**DOI:** [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757)  
**仓库:** [TAT-ONE-TAP/tat_monitor](https://github.com/maratsultanov2/TAT-ONE-TAP/tree/main/tat_monitor)

### 问题
在代理系统中，用户经常在不明确命名的情况下回退一个值。他们引用一个角色：“按照负责访问权限的人的决定来做。”要检测这种回退，系统必须解析一个链条：**角色 → 锚点 → 旧值**。

### 方法
我们开发了 **直接上下文比较**：计算候选语句与上下文中角色字符串的余弦相似度。如果候选语句更接近旧角色而非新角色，则为回退。

### 关键结果
- 在最难的 v4 测试集上 **F1 = 0.926**，**AUROC = 0.986**。
- 在两个嵌入器上复现：all‑MiniLM (0.905) 和 nomic (0.930)。
- 在带有来源信息的真实 mnemo 数据上：**F1 = 0.895**，锚定召回率从 14/26 提升至 26/26。

### 意义
内存系统可以 **无需 LLM、无需训练、无需 GPU** 地检测回退 — 并且可以嵌入到任何带有上下文和角色的代理应用中。

---

## 📄 出版物 2：自旋-电荷分离的跨框架验证

**标题:** *Charge and Spin Response of One‑Dimensional Electron Delocalization Relation Networks*  
**作者:**  
- **Guanghao Li** ([@luoxuejian000](https://github.com/luoxuejian000)) — 独立研究员，中国合肥  
- **Rastislav Drahos** ([@DanceNitra](https://github.com/DanceNitra)) — Agora Scientific，捷克共和国  
- **Marat Sultanov** ([@maratsultanov2](https://github.com/maratsultanov2)) — 独立研究员，俄罗斯联邦  

**状态:** 预印本 / Zenodo 存档 (DOI)  
**年份:** 2026  
**DOI:** [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316)  
**仓库:** [luoxuejian000/edrn-dmrg-verification](https://github.com/luoxuejian000/edrn-dmrg-verification)

### 问题
如何在不将数据拟合到期望答案的情况下检验理论？在凝聚态物理中，预测强关联系统的标度指数是出了名的困难。

### 方法
我们结合了三个独立的诊断框架：
- **DMRG**（密度矩阵重整化群）用于数值数据。
- **精确 Bethe-ansatz 解**作为理论锚点。
- **TAT‑Defense** 作为盲测结构诊断工具。

TAT 在六个 DMRG 数据集上运行，没有预先了解物理，检测到：
- 在电荷压缩率数据上 **保持沉默**（没有结构可发现）。
- 在 U=1 数据中 **L=120 和 160 处的锚点** — 后来被确认为数值收敛伪影（χ_max=100）。
- 在干净的 U=2 阳性对照中 **仅边界锚点**。

### 关键结果
- 原始预测（电荷压缩率 α=1.75）被证伪。
- 修订后的预测：自旋能隙按 Δs ~ 1/L 标度，α_spin = −0.94。
- 恒等式 α_charge + α_spin = −1 被确认为 Mott 绝缘体中自旋-电荷分离的数值表现。

### 意义
TAT 作为一个独立的诊断层，与 DMRG 和 Bethe-ansatz 锚点 **无需对齐** 地收敛于同一数值边界。这表明 TAT 可以成为数据质量评估和跨框架验证的可靠工具。

---

## 🧠 总结

TAT 已在两个独立上下文中得到验证：

| 领域 | 方法 | 关键指标 | DOI |
|------|------|----------|-----|
| **代理系统** | TAT‑Monitor | F1 = 0.926 | [10.5281/zenodo.21326757](https://doi.org/10.5281/zenodo.21326757) |
| **凝聚态物理** | TAT‑Defense | 跨框架收敛 | [10.5281/zenodo.21393316](https://doi.org/10.5281/zenodo.21393316) |

两篇出版物都遵循相同的核心理念：**诊断而不开方 — 让数据说话。**

### 3. 一维莫特绝缘体中自旋能隙预因子的系统数值研究
**作者:** Guanghao Li, Rastislav Drahos, Marat Sultanov
**DOI:** [10.5281/zenodo.21473160](https://doi.org/10.5281/zenodo.21473160)
**状态:** 发表于 Zenodo（开放获取，CC‑BY）
**关键贡献:** EDRN 交叉验证的直接延续。经过收敛性检验的缺陷扫描证实，预因子 A 变化超过 500%，而每个键的拓扑指数 C 变化不到 1%——这是局部响应与全局拓扑的决定性解耦。TAT‑Defense 提供了独立的跨框架盲测，其诚实静默记录已记录于附录中。

---
## 🔗 链接

- [TAT‑ONE‑TAP](https://github.com/maratsultanov2/TAT-ONE-TAP) — 代码和模块
- [TAT‑ROOT](https://github.com/maratsultanov2/TAT-ROOT) — 理论和文档
- [EDRN verification repository](https://github.com/luoxuejian000/edrn-dmrg-verification) — DMRG 数据和分析
