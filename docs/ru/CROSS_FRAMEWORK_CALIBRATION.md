# Кросс-фреймворковая калибровка

Конвенции для сравнения TAT с HeartFlow, Cophy Runtime и TLAA по аудиту логики выполнения, сохранению памяти и стабильности идентичности.

## 1. Согласование порогов

| Метрика TAT | Порог TAT | Эквивалент HeartFlow | Примечания |
|-------------|-----------|----------------------|------------|
| Дивергенция | < 0.10 (3 головы) | Нормализованная < 0.10 (стабильно) | Консолидация с низкой дивергенцией |
| Дивергенция | 0.10 – 0.30 (5 голов) | Нормализованная 0.10 – 0.30 (дрейф) | Активная защитная коррекция |
| Дивергенция | > 0.30 (7 голов) | Нормализованная > 0.30 (расхождение) | Отказ / решение TURN |
| Статус Harmony | active / weak / silent | stable / drifting / divergent | Сопоставление структурного вето |

HeartFlow использует шкалу 0–100. Конверсия: `TAT_divergence = HeartFlow_divergence / 100`.

## 2. Сопоставление словарей решений

| Gate TAT | Решение HeartFlow | Семантика |
|----------|-------------------|-----------|
| Consolidate | hold, accelerate | Нормальная работа, низкая дивергенция |
| Escalated (5 голов) | turn | Обнаружена дивергенция, защитная коррекция |
| Withhold (harmony молчит) | heal, pause, rest, transmit | Действие заблокировано или отложено |

## 3. Соглашения о форматах данных

Каждый фреймворк предоставляет результаты в своём родном формате с объявленным полем `raw_format`:

| Фреймворк | raw_format | Типичные поля |
|-----------|------------|---------------|
| TAT | CSV | task_id, phase, position, coherence, divergence, harmony_status, heads, gate_decision |
| HeartFlow | CSV | scenario_id, timestamp, position, coherence, divergence, normalized, harmony_status, h_value, cognitive_load, decision, confidence |
| Cophy Runtime | CSV + markdown | scenario_id, pressure_type, preference_id, applied_correctly, causal_density_at_retrieval |

## 4. Различия в дизайн-философии

| Аспект | TAT | HeartFlow | Cophy Runtime |
|--------|-----|-----------|---------------|
| Сдвиг идентичности при roleplay | Вызывает эскалацию при дивергенции > 0.30 | Допустим, если временный | Измеряется через поведенческие контрфактуалы |
| Pre-execution vs. post-hoc аудит | Harmony gate блокирует консолидацию до вывода | Трёхсторонняя диспетчеризация (truth/lesson/verify) до выполнения | Постфактум health scoring в Dream Cycle |
| Управление памятью | Чанковая карусель (остывание + апоптоз) | Статические правила + Q-таблица | TTL-основанное удаление с causal density |
| Статические vs. обновляемые правила | Пороги gate фиксированы; harmony matrix обучаема | 29 правил, обновляемых без переобучения модели | Фреймворк оценки фиксирован; сценарии обновляемы |

## 5. Авторство

| Концепт | Автор | Фреймворк |
|---------|-------|-----------|
| Divergence trace (Position − Coherence) | Marat Sultanov | TAT |
| Harmony gate (структурное вето) | Marat Sultanov | TAT |
| Чанковая карусель | Marat Sultanov | TAT |
| Принцип чайника (достаточность) | Marat Sultanov | TAT |
| Операционная оболочка (93–96%) | Marat Sultanov | TAT |
| Зеркальная временная метка | Marat Sultanov | TAT |
| Surface coherence | icophy | Cophy Runtime |
| H-value (0.4·U + 0.3·D − 0.3·A) | yun520-1 | HeartFlow |
| Pre-execution verification | yun520-1 | HeartFlow |
| U/D/A/H четырёхмерное поле | luoxuejian000 | Независимый синтез |

## 6. Ссылки

- [Теоретический фундамент TAT](docs/ru/THEORETICAL_FOUNDATION.md)
- [Глоссарий TAT](docs/ru/GLOSSARY.md)
- [Сравнительный бенчмарк TAT](docs/ru/benchmarks/COMPARATIVE_BENCHMARK.md)

---

*Этот документ версионируется в TAT-ROOT. Конвенции могут обновляться по мере развития фреймворков и появления новых данных.*
