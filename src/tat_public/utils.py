"""Утилиты TAT: нормализация, триадное согласие, оценка дрейфа."""
import numpy as np


def normalize(x: np.ndarray) -> np.ndarray:
    """Нормализует массив в диапазон [0, 1]."""
    x_min, x_max = x.min(), x.max()
    return (x - x_min) / (x_max - x_min + 1e-12) if x_max - x_min > 1e-12 else np.zeros_like(x)


def standardize(x: np.ndarray) -> np.ndarray:
    """Стандартизирует массив (среднее=0, std=1)."""
    return (x - x.mean()) / (x.std() + 1e-8)


def triadic_agreement(coarse: np.ndarray, fine: np.ndarray, error: np.ndarray,
                      invert_coarse: bool = False, invert_fine: bool = False) -> np.ndarray:
    """Вычисляет триадное согласие трёх диагностических потоков."""
    c = normalize(coarse)
    f = normalize(fine)
    e = normalize(error)
    if invert_coarse:
        c = 1 - c
    if invert_fine:
        f = 1 - f
    return c * f * (1 - e)


def estimate_drift(series: np.ndarray) -> float:
    """Оценивает линейный дрейф (наклон) временного ряда."""
    t = np.arange(len(series))
    slope, _ = np.polyfit(t, series, 1)
    return slope


def block_shuffle(series: np.ndarray, block_size: int = 3) -> np.ndarray:
    """Перемешивает массив блоками, сохраняя локальную зависимость."""
    n = len(series)
    n_blocks = n // block_size
    blocks = [series[i * block_size:(i + 1) * block_size] for i in range(n_blocks)]
    rem = series[n_blocks * block_size:]
    np.random.shuffle(blocks)
    if len(rem) > 0:
        blocks.append(rem)
    return np.concatenate(blocks)
