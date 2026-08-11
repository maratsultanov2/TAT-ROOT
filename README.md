# TAT (Thermodynamic Adaptive Transformer)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE-DATA)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21875878.svg)](https://doi.org/10.5281/zenodo.21875878)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green)]()
[![CI](https://github.com/maratsultanov2/TAT-ROOT/actions/workflows/ci.yml/badge.svg)](https://github.com/maratsultanov2/TAT-ROOT/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue)](https://pypi.org/project/tat-public/)
[![Coverage](https://img.shields.io/badge/coverage-0%25-red)](https://github.com/maratsultanov2/TAT-ROOT)

**English** | [Русский](#русский) | [中文](#中文)

TAT is a structural diagnostic framework for unsupervised anomaly detection. It uses adaptive anchors, multi-stream moiré interference, and complex coherence (θ=1.987) to detect hidden structures in data without labels.

**Key features:**
- **Adaptive Anchors** — finds structural minima without training
- **TAT-Monitor** — anomaly detection via div-harm decomposition
- **Multi-Stream Moiré Interference** — reveals hidden periodicities
- **Cross-Framework Protocol** — drift-aware permutation test

**Proven on:**
- Quantum spin chains (Sultanov Silence, published in [10.5281/zenodo.21875878](https://doi.org/10.5281/zenodo.21875878))
- Yeast proteomics (GOAI Challenge 2026, 5,244 proteins, 48 treatments)
- CERN dimuon data (blind J/ψ detection at 3.060 GeV)

**Installation:** `pip install tat-public`

**Documentation:** [docs/](docs/) · [Glossary](docs/GLOSSARY.md) · [API Reference](docs/API.md)

**License:** Code — AGPL-3.0. Data & Docs — CC BY-NC-ND 4.0.

**Author:** Marat Sultanov · [GitHub](https://github.com/maratsultanov2) · [Zenodo](https://zenodo.org/search?q=Marat%20Sultanov)

---

## Русский

TAT — это фреймворк структурной диагностики для поиска аномалий без учителя.

**Основные компоненты:**
- **Адаптивные якоря** — поиск структурных минимумов без обучения
- **TAT-Monitor** — детектор аномалий (div - harm)
- **Мультипотоковая муаровая интерференция** — выявление скрытых периодичностей

**Подтверждённые результаты:**
- Квантовые спиновые цепочки (Sultanov Silence, опубликовано)
- Протеомика дрожжей (GOAI Challenge 2026)
- Данные ЦЕРН (слепое обнаружение J/ψ)

**Лицензия:** Код — AGPL-3.0. Данные и документация — CC BY-NC-ND 4.0.

---

## 中文

TAT 是一个用于无监督异常检测的结构诊断框架。

**核心组件：**
- **自适应锚点** — 无需训练即可找到结构最小值
- **TAT-Monitor** — 异常检测器
- **多流莫尔干涉** — 通过相移叠加揭示隐藏的周期性

**已验证的成果：**
- 量子自旋链（苏丹诺夫沉默，已发表）
- 酵母蛋白质组学（GOAI 挑战赛 2026）
- CERN 数据（J/ψ 盲检测）

**许可证：** 代码 — AGPL-3.0。数据与文档 — CC BY-NC-ND 4.0。
