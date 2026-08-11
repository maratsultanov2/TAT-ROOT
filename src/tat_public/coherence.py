"""Комплексная когеренция TAT (Thermodynamic Adaptive Transformer).
Использует фазовую константу θ=1.987.
"""
import numpy as np

THETA: float = 1.987
IMAG: complex = 1j


def to_complex(x: np.ndarray, theta: float = THETA) -> np.ndarray:
    """Переводит вещественный массив в комплексное пространство TAT."""
    return x + IMAG * (x * np.sin(theta))


def coherence(v1: np.ndarray, v2: np.ndarray, theta: float = THETA) -> float:
    """Вычисляет комплексную когеренцию между двумя векторами."""
    c1 = to_complex(v1, theta)
    c2 = to_complex(v2, theta)
    dot = np.vdot(c1, c2)
    norm = np.linalg.norm(c1) * np.linalg.norm(c2) + 1e-8
    return float(np.abs(dot) / norm)


def coherence_matrix(data: np.ndarray, theta: float = THETA) -> np.ndarray:
    """Вычисляет попарную матрицу когеренции для набора векторов."""
    n = data.shape[0]
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            c = coherence(data[i], data[j], theta)
            m[i, j] = c
            m[j, i] = c
    return m
