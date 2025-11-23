import unittest
import numpy as np
from src.contour_counter import count_contours


class TestObjectCounter(unittest.TestCase):

    def test_empty_edge_image(self):
        empty_image = np.zeros((100, 100), dtype=np.uint8)
        count, contours = count_contours(empty_image, min_area=1)
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
