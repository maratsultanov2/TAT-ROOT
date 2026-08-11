import unittest
import numpy as np
from tat_public.coherence import to_complex, coherence, coherence_matrix

class TestCoherence(unittest.TestCase):
    def setUp(self):
        self.v1 = np.random.randn(100)
        self.v2 = np.random.randn(100)

    def test_to_complex_shape(self):
        c = to_complex(self.v1)
        self.assertEqual(c.shape, self.v1.shape)
        self.assertTrue(np.iscomplexobj(c))

    def test_coherence_identical(self):
        c = coherence(self.v1, self.v1)
        self.assertAlmostEqual(c, 1.0, places=5)

    def test_coherence_orthogonal(self):
        v1 = np.array([1.0, 0.0])
        v2 = np.array([0.0, 1.0])
        c = coherence(v1, v2)
        self.assertTrue(0.0 <= c <= 1.0)

    def test_coherence_matrix(self):
        data = np.random.randn(10, 20)
        m = coherence_matrix(data)
        self.assertEqual(m.shape, (10, 10))
        self.assertTrue(np.allclose(m, m.T))  # Симметричность

if __name__ == "__main__":
    unittest.main()
