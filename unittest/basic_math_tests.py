import unittest

import basic_math as bm


class TestBasicMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(bm.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(bm.sub(1, 2), -1)

    def test_mul(self):
        self.assertEqual(bm.mul(5, 2), 10)

    def test_div(self):
        self.assertEqual(bm.div(1, 2), 0.5)

    def test_pow(self):
        self.assertNotEqual(bm.pow(1, 2), 1)


if __name__ == "__main__":
    unittest.main()
