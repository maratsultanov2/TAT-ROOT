import numpy as np

def coherence(e1, e2, theta=1.987):
    c1 = e1 + 1j * (e1 * np.sin(theta))
    c2 = e2 + 1j * (e2 * np.sin(theta))
    dot = np.vdot(c1, c2)
    norm = np.linalg.norm(c1) * np.linalg.norm(c2) + 1e-8
    return abs(dot) / norm
