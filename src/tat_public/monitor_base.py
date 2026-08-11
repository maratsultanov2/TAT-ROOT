"""Базовый TAT-Monitor: детектор аномалий (div - harm).
Не содержит обученных весов.
"""
import numpy as np


def tat_monitor(series: np.ndarray, window: int = 3, sigma: float = 2.0) -> tuple:
    """Обнаруживает структурные аномалии в одномерном ряду."""
    n = len(series)
    signal = np.zeros(n)
    for i in range(window, n - window):
        left = series[i - window:i]
        right = series[i + 1:i + window + 1]
        div = np.std(left) + np.std(right)
        lr = np.corrcoef(left, right)[0, 1] if np.std(left) > 0 and np.std(right) > 0 else 0
        signal[i] = div - lr
    thr = np.nanmean(signal) + sigma * np.nanstd(signal)
    return np.where(signal > thr)[0], signal, thr


def permutation_test(series: np.ndarray, n_perm: int = 1000, window: int = 3, sigma: float = 2.0) -> tuple:
    """Пермутационный тест значимости для TAT-Monitor."""
    obs, _, _ = tat_monitor(series, window, sigma)
    observed = len(obs)
    null = []
    for _ in range(n_perm):
        s = np.random.permutation(series)
        p, _, _ = tat_monitor(s, window, sigma)
        null.append(len(p))
    null = np.array(null)
    return observed, null, np.mean(null >= observed)
