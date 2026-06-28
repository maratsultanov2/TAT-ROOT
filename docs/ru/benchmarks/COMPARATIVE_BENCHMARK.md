# Сравнительный бенчмарк: TAT-7 против EWC / SI / MAS

## Условия теста

- **Датасет:** Split Fashion-MNIST (5 задач × 2 класса)
- **Эпох на задачу:** 5
- **Метрика:** Divergence Trace (Position − Coherence + Harmony + Gate)
- **Цель:** Измерить сохранение памяти при последовательном обучении

## Сравниваемые методы

| Метод | Механизм | Провал? |
|-------|----------|---------|
| **TripleNet (vanilla)** | Без защиты | ❌ Память ~0.05 |
| **EWC** (Elastic Weight Consolidation) | Штраф Фишера на важные веса | ❌ Память ~0.02–0.09 |
| **SI** (Synaptic Intelligence) | Накопленная важность синапсов | ❌ Память ~0.02–0.11 |
| **MAS** (Memory Aware Synapses) | Важность по чувствительности выхода | ❌ Память ~0.02–0.09 |
| **TAT-7** | Гармонический резонанс + фазовая когерентность | ✅ Память ~0.79 |

## Ключевой вывод

**EWC, SI и MAS проваливаются, потому что защищают веса, а не связи.**
На Split Fashion-MNIST проблема не в дрейфе весов, а в разрушении когерентности между головами.
Три головы TripleNet (yang, yin, to) катастрофически расходятся, и EWC/SI/MAS ничего не могут с этим сделать.

**TAT-7 решает проблему когерентности напрямую.**
Матрица гармонического резонанса удерживает фазовое выравнивание между головами даже при изменении отдельных весов.
Harmony остаётся активной, divergence не превышает 0.20, а сохранение памяти достигает 79% после 5 задач.

## Результаты

| Метрика | TripleNet | EWC | SI | MAS | TAT-7 |
|---------|-----------|-----|----|-----|-------|
| Средняя когерентность | ~0.07 | ~0.09 | ~0.08 | ~0.10 | ~0.76 |
| Финальная память (Задача 1) | ~0.06 | ~0.09 | ~0.09 | ~0.09 | ~0.79 |
| Статус Harmony | Silent (5/5) | Silent (5/5) | Silent (5/5) | Silent (5/5) | Active (4/5) |
| Решение Gate | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Withhold (5/5) | Consolidate / Escalated |

## Данные

- [TripleNet (CSV)](../../data/triplenet_divergence_trace.csv)
- [EWC (CSV)](../../data/ewc_divergence_trace.csv)
- [SI (CSV)](../../data/si_divergence_trace.csv)
- [MAS (CSV)](../../data/mas_divergence_trace.csv)
- [TAT-7 (CSV)](../../data/tat7_divergence_trace.csv)
- [Полный сравнительный график (PNG)](../../data/comparative_benchmark_all_methods.png)

## Воспроизведение

Запустите Colab-ноутбук: [TAT Comparative Benchmark](https://colab.research.google.com/)
