import unittest
import numpy as np
from tat_public.monitor_base import tat_monitor, permutation_test

class TestMonitor(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(0, 10, 200)
        self.clean = np.sin(self.x)
        self.noisy = self.clean + np.random.randn(200) * 0.1

    def test_tat_monitor_output(self):
        peaks, signal, thr = tat_monitor(self.noisy)
        self.assertIsInstance(peaks, np.ndarray)
        self.assertEqual(signal.shape, self.noisy.shape)
        self.assertGreater(thr, 0)

    def test_permutation_test(self):
        obs, null, p = permutation_test(self.noisy, n_perm=100)
        self.assertIsInstance(obs, int)
        self.assertEqual(len(null), 100)
        self.assertTrue(0.0 <= p <= 1.0)

if __name__ == "__main__":
    unittest.main()
