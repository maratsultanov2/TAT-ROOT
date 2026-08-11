import numpy as np
THETA = 1.987; IMAG = 1j
def to_complex(x, theta=THETA): return x + IMAG * (x * np.sin(theta))
def coherence(v1, v2, theta=THETA):
    c1=to_complex(v1,theta); c2=to_complex(v2,theta)
    return float(np.abs(np.vdot(c1,c2))/(np.linalg.norm(c1)*np.linalg.norm(c2)+1e-8))
