import numpy as np

THETA = 1.987
IMAG = 1j

def to_complex(x, theta=THETA):
    return x + IMAG * (x * np.sin(theta))

def coherence(v1, v2, theta=THETA):
    c1 = to_complex(v1, theta)
    c2 = to_complex(v2, theta)
    dot = np.vdot(c1, c2)
    norm = np.linalg.norm(c1) * np.linalg.norm(c2) + 1e-8
    return float(np.abs(dot) / norm)

def coherence_matrix(data, theta=THETA):
    n = data.shape[0]
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(i, n):
            c = coherence(data[i], data[j], theta)
            m[i, j] = c
            m[j, i] = c
    return m
