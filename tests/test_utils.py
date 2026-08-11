import unittest
import numpy as np
from tat_public.utils import normalize, standardize, estimate_drift, block_shuffle

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.x = np.random.randn(100)

    def test_normalize(self):
        nx = normalize(self.x)
        self.assertAlmostEqual(nx.min(), 0.0)
        self.assertAlmostEqual(nx.max(), 1.0)

    def test_standardize(self):
        sx = standardize(self.x)
        self.assertAlmostEqual(sx.mean(), 0.0, places=5)
        self.assertAlmostEqual(sx.std(), 1.0, places=5)

    def test_estimate_drift(self):
        t = np.arange(100)
        y = 2.5 * t + np.random.randn(100) * 0.1
        slope = estimate_drift(y)
        self.assertAlmostEqual(slope, 2.5, places=1)

    def test_block_shuffle(self):
        y = np.arange(100)
        shuffled = block_shuffle(y, block_size=10)
        self.assertEqual(len(shuffled), 100)
        self.assertFalse(np.array_equal(y, shuffled))  # Маловероятно, что перемешанный массив совпадёт

if __name__ == "__main__":
    unittest.main()
