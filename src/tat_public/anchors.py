"""Адаптивные структурные якоря TAT.
Находят структурные минимумы без обучения.
"""
import numpy as np
from scipy.signal import argrelextrema


def adaptive_anchors(series: np.ndarray, window: int = 5, tol: float = 0.1) -> np.ndarray:
    """Находит структурные минимумы в одномерном ряду."""
    n = len(series)
    if n < window:
        return np.array([np.argmin(series)])
    smooth = np.convolve(series, np.ones(window) / window, mode="valid")
    raw = argrelextrema(smooth, np.less, order=min(window, len(smooth) // 2))[0]
    if len(raw) < 2:
        return np.array([np.argmin(series)])
    if len(raw) > 2:
        vals = series[raw]
        thr = np.mean(vals) + tol * np.std(vals)
        filtered = raw[vals < thr]
        return filtered if len(filtered) > 0 else np.array([np.argmin(series)])
    return raw


def anchor_depth(series: np.ndarray, anchors: np.ndarray) -> np.ndarray:
    """Вычисляет относительную глубину каждого якоря."""
    d = []
    for a in anchors:
        left = np.max(series[:a + 1]) if a > 0 else series[a]
        right = np.max(series[a:]) if a < len(series) - 1 else series[a]
        d.append(min(left, right) - series[a])
    return np.array(d)
