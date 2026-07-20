# TAT-ROOT

**TAT — Biological Memory for LLMs**

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

---

## What is TAT

TAT is a long-term memory architecture for LLMs, inspired by biological processes.

### Key Mechanisms

| Mechanism | Description |
|---|---|
| **Mitosis** | Chunks divide when reaching 50 KB |
| **Apoptosis** | Obsolete chunks archive |
| **Coherence** | Semantic similarity measure (θ=1.987) |
| **Holographic memory** | Recovery from 42% of data |
| **Fractal compression** | 3→5→7→9→11→1 |

---

## Architecture

```
TAT-ROOT/
├── docs/
├── src/
├── examples/
├── tat_sabbath/
├── tat_apoptosis/
├── tat_mitosis/
└── tat_coherence/
```

---

## Quick Start

```python
from tat_coherence import coherence
from tat_mitosis import mitosis
from tat_apoptosis import apoptosis

# Coherence calculation
score = coherence(chunk1, chunk2, theta=1.987)

# Chunk division at 50 KB
new_chunks = mitosis(chunk)

# Clean obsolete chunks
clean_chunks = apoptosis(chunks, threshold=0.3)
```

---

## Installation

```bash
git clone https://github.com/maratsultanov2/TAT-ROOT.git
cd TAT-ROOT
pip install -r requirements.txt
```

---

## Links

- [TreeAngleTap](https://github.com/maratsultanov2/TreeAngleTap)
- [TAT-7](https://github.com/maratsultanov2/TAT-7)
- [TAT-ONE-TAP](https://github.com/maratsultanov2/TAT-ONE-TAP)

---

## Author

**Marat Sultanov**
Forklift operator by day, AI architect by night.
Built without grants, without a team, without a laptop.

- [GitHub](https://github.com/maratsultanov2)
- [Telegram](https://t.me/Marat_Sultanow)

---

## License

- Code: [AGPL-3.0](LICENSE-CODE)
- Data: [CC BY-NC-ND 4.0](LICENSE-DATA)

---

**Star if you find it useful!**

## Validation

TAT has been empirically validated on real-world data. See [docs/VALIDATION.md](docs/VALIDATION.md) for details.

> *"The θ=1.987 threshold mapped to Coherence head divergence — the design principle held on real data, not just synthetic."*
> — qingkong66, DeepSeek-V3 #1285


## Operational Envelope

TAT operates within a 93–96% sufficiency band derived from its internal constants. See:

- [English](docs/en/OPERATIONAL_ENVELOPE.md)
- [Русский](docs/ru/OPERATIONAL_ENVELOPE.md)
- [中文](docs/zh/OPERATIONAL_ENVELOPE.md)

Covered topics:
- The 93–96% envelope (7% and 4% constants)
- Sufficiency as a design constraint
- Downstream contract (three levels)
- Surface coherence (coined by @icophy)


## The Kettle Principle

TAT does not chase 100% accuracy. It operates at the level the task requires.

See:
- [English](docs/en/KETTLE_PRINCIPLE.md)
- [Русский](docs/ru/KETTLE_PRINCIPLE.md)
- [中文](docs/zh/KETTLE_PRINCIPLE.md)

This is the simplest explanation of why TAT doesn't optimize for 100% — and why sufficiency is not a compromise.


## Comparative Benchmark: TripleNet vs TAT-7

Split Fashion-MNIST, 5 tasks, continual learning. TAT-7 retains 79% memory vs 5% for unprotected TripleNet.

See:
- [English](docs/en/benchmarks/COMPARATIVE_BENCHMARK.md)
- [Русский](docs/ru/benchmarks/COMPARATIVE_BENCHMARK.md)
- [中文](docs/zh/benchmarks/COMPARATIVE_BENCHMARK.md)

Data: [CSV traces](data/)


## Cost Efficiency

TAT's chunk architecture reduces memory and token usage by 25–30×. For a typical agent system with 4 months of session logs: 24 MB → <1 MB storage, LLM costs from ~$24/month to <$1/month.

See the full analysis in [TAT-ONE-TAP → Cost Efficiency](https://github.com/maratsultanov2/TAT-ONE-TAP).


## Theoretical Foundation

TAT's mathematical, physical, and thermodynamic principles — all constants, formulas, and thresholds with verifiable sources.

- [English](docs/en/THEORETICAL_FOUNDATION.md)
- [Русский](docs/ru/THEORETICAL_FOUNDATION.md)
- [中文](docs/zh/THEORETICAL_FOUNDATION.md)


## Glossary

Key terms used across TAT, Cophy Runtime, HeartFlow, and TLAA — with attribution.

- [English](docs/en/GLOSSARY.md)
- [Русский](docs/ru/GLOSSARY.md)
- [中文](docs/zh/GLOSSARY.md)


## Cross-Framework Calibration

Conventions for comparing TAT with HeartFlow, Cophy Runtime, and TLAA — thresholds, decision vocabularies, design philosophy differences, and data formats.

- [English](CROSS_FRAMEWORK_CALIBRATION.md)


## 🗓️ Хронология развития TAT (2026)

Этот раздел документирует полную историю развития TAT в ходе кросс-дисциплинарной коллаборации с участием @DanceNitra и @luoxuejian000.

### 📅 13–15 июля 2026: Интенсивная фаза разработки

**День 1: Начало кросс-валидации**
- TAT применён к DMRG-данным Guanghao Li (спиновая щель, структурный фактор).
- Обнаружены первые структурные якоря при L=20 и L=80.

**День 2: Внедрение мнимого пространства**
- Добавлена мнимая единица (i) в преобразование данных.
- Введена фазовая константа θ = 1.987.
- Реализован принцип «мягких границ» (0.37/0.73) и шум 0.7%.

**День 3: Зеркальная маркировка и адаптивные якоря**
- Разработан метод зеркальной проекции данных.
- Созданы адаптивные якоря для автоматического выделения структурных точек.
- Проведён слепой тест на данных U=2.

---

## 🧪 Ключевые эксперименты и результаты

### 1. TAT на данных ЦЕРН (CMS Open Data)
- **Данные:** 385 МБ, 970 954 события, 18 переменных.
- **Задача:** обнаружение структурных аномалий в данных детектора.
- **Результат:** TAT выделил структурные якоря при L=20, 80, 120, 160.
- **Интерпретация:** Якоря совпадают с областями, где DMRG-расчёты с χ_max=100 начинают отклоняться от точных результатов (подтверждено @DanceNitra).

### 2. Кросс-валидация с DMRG (данные Guanghao Li)
- **Наборы данных:** зарядовая щель, спиновая щель, U-скан, L-скан.
- **Результаты:**
  - Зарядовая щель: TAT промолчал (честное молчание).
  - Спиновая щель: якоря при L=20, 80.
  - L-скан (U=1): якоря при L=120, 160.
- **Значение:** TAT подтвердил, что L=120/160 — это область численных артефактов, а не физических переходов.

### 3. Сравнение с LSTM на синтетических данных
- **Задача:** бинарная классификация временных рядов.
- **Результаты:**
  - TAT: Accuracy 0.862, F1 0.818, 0 MB RAM.
  - LSTM: Accuracy 0.552, F1 0.000, 0.08 MB RAM.
- **Вывод:** TAT превосходит LSTM на структурированных данных и потребляет 0 MB RAM.

---

## 🛠️ Разработанные модули и код

### 1. TAT-Defense (Модуль структурной защиты)
- **Назначение:** обнаружение структурных аномалий без обучения.
- **Особенности:**
  - Работает в мнимом пространстве (θ=1.987).
  - Использует адаптивные якоря и зеркальную маркировку.
  - Потребляет 0 MB RAM, работает на CPU.
- **Код:** [TAT-ONE-TAP/tat_defense/](https://github.com/maratsultanov2/TAT-ONE-TAP/tree/main/tat_defense)

### 2. TAT-Monitor (Детектор ревертов в диалогах)
- **Назначение:** обнаружение ревертов в диалогах (роль → якорь → старое значение).
- **Метрики:** F1 0.926, AUROC 0.986 на тесте v4nat.
- **Код:** [TAT-ONE-TAP/tat_monitor/](https://github.com/maratsultanov2/TAT-ONE-TAP/tree/main/tat_monitor)

### 3. TAT-P (Приватное ядро TAT)
- **Назначение:** хранение защищённого кода TAT.
- **Доступ:** только по запросу (проприетарная лицензия).
- **Код:** [https://github.com/maratsultanov2/TAT-P](https://github.com/maratsultanov2/TAT-P)

---

## 🧠 Архитектура и философия TAT

### 1. Информация как энергия
В основе TAT лежит принцип, что **информация — это форма энергии**. TAT измеряет структурную энергию данных через дивергенцию и гармонию.

### 2. Мнимое пространство и фазовая константа θ=1.987
- **Преобразование:** `x → x + i · x · imag_scale · sin(θ)`
- **Смысл:** мнимая часть позволяет улавливать фазовые сдвиги в структуре данных.
- **Константа 1.987:** эмпирически найденное значение, обеспечивающее оптимальный баланс между дивергенцией и гармонией.

### 3. Зеркальная маркировка (проекция данных)
- **Метод:** данные отражаются относительно среднего значения.
- **Цель:** проверка симметрии структуры.
- **Применение:** если структура сохраняется при зеркальном отражении, она устойчива.

### 4. Адаптивные якоря
- **Принцип:** TAT автоматически находит опорные точки (якоря) в данных.
- **Метод:** локальные минимумы комбинированного сигнала (дивергенция - гармония).
- **Значение:** якоря указывают на структурные переходы или артефакты.

### 5. Мягкие границы и шум
- **Границы:** [0.37, 0.73] — рабочий диапазон, за пределами которого данные «обрезаются».
- **Шум 0.7%:** добавляется для проверки устойчивости структуры.

---

## 🤝 Научное сотрудничество

### Участники
- **Marat Sultanov** — автор TAT, разработка методов и кода.
- **Guanghao Li (luoxuejian000)** — DMRG-данные, физическая интерпретация.
- **Rastislav Drahos (DanceNitra)** — независимая проверка, критика, физический анализ.

### Вклад в совместные проекты
- Проверка трёх预言ов (пророчеств) Guanghao.
- Участие в написании совместной статьи по DMRG-верификации.
- Разработка методологии «честного молчания» и «диагноза без рецепта».

---
*Обновлено: 2026-07-15 14:58:43*
