import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def test_get(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.get(array, 2, None), 3)
        self.assertEqual(arrs.get(array, -2, None), None)
        self.assertEqual(arrs.get(array, -1, 'default'), 'default')

    def test_slice(self):
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], end=3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -3), [3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -10), [1, 2, 3, 4, 5])

