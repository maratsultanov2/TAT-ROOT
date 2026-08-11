import unittest
import numpy as np
from tat_public.anchors import adaptive_anchors, anchor_depth

class TestAnchors(unittest.TestCase):
    def setUp(self):
        self.x = np.linspace(0, 3, 100)
        self.y = (self.x - 1.5)**2

    def test_adaptive_anchors_single_minimum(self):
        anchors = adaptive_anchors(self.y)
        self.assertGreaterEqual(len(anchors), 1)
        self.assertTrue(40 <= anchors[0] <= 60)

    def test_adaptive_anchors_short_series(self):
        short = np.array([5.0, 2.0, 3.0])
        anchors = adaptive_anchors(short, window=5)
        self.assertEqual(len(anchors), 1)
        self.assertEqual(anchors[0], np.argmin(short))

    def test_anchor_depth(self):
        anchors = np.array([50])
        depths = anchor_depth(self.y, anchors)
        self.assertEqual(len(depths), 1)
        self.assertGreater(depths[0], 0)

if __name__ == "__main__":
    unittest.main()
