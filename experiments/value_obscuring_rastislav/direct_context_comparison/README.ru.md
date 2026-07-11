# Метод прямого контекстного сравнения для обнаружения структурных аномалий

[![TAT](https://img.shields.io/badge/TAT-Experimental-blue)](https://github.com/maratsultanov2/TAT-ROOT)
[![Dataset by Rastislav](https://img.shields.io/badge/Dataset-Rastislav_Drahos-green)](https://github.com/DanceNitra/agora)
[![License: AGPL v3](https://img.shields.io/badge/Code-AGPL%20v3-blue)](../../LICENSE-CODE)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--ND%204.0-lightgrey)](../../LICENSE-DATA)
[![Status: Peer‑Reviewed](https://img.shields.io/badge/Status-Peer--Reviewed-brightgreen)](https://github.com/DanceNitra/agora)

## Авторы и роли

- **Марат Султанов** — автор метода прямого контекстного сравнения, архитектуры TAT, модели Triplenet и всех экспериментов на v2, v3, v4 и v4nat.
- **Растислав Драгош (DanceNitra)** — независимый соавтор. Разработал фикстуры value‑obscuring reversion, провёл аудит, воспроизвёл метод и обнаружил факторизацию задачи.

## Результаты на v4nat heldout (46 примеров)

- Accuracy: 0.9130
- Precision: 0.8636
- Recall: 0.9500
- F1: **0.9048**
- AUROC: **0.9635**
- Confusion matrix: [23 3; 1 19]

## Независимое воспроизведение

Растислав Драгош воспроизвёл метод с другим эмбеддером: F1 0.930, AUROC 1.000.

## Полный отчёт и артефакты

- [English](README.md) | [Русский](README.ru.md) | [中文](README.zh.md)
- [Предсказания (CSV)](predictions.csv)
- [Метрики (JSON)](metrics.json)
- [График отчёта](final_report.png)

*Опубликовано: 2026-07-11 21:21*
