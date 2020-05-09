import unittest
from Sprawdzian1.Piotr_Janus_236677_S1_zad1 import *


class MyTestCase(unittest.TestCase):

    def test_series(self):
        self.assertEqual(get_math_series(2, -5, 10), [2, -3, -8, -13, -18, -23, -28, -33, -38, -43])
        self.assertEqual(get_math_series(14, 1, 2), [14, 15])

    def test_if_is_int(self):
        with self.assertRaises(SystemExit) as cm:
            main(["6", "7", "2.5"])
        self.assertEqual(cm.exception.code, "Some input arguments are not integers. Please put integer numbers")


if __name__ == '__main__':
    unittest.main()
