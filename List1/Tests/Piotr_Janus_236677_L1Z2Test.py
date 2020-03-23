import unittest
from List1.Piotr_Janus_236677_L1Z2 import *


class Zad2Test(unittest.TestCase):

    def test_is_square_number(self):
        self.assertTrue(is_square_number(64))
        self.assertFalse(is_square_number(11))

    def test_is_fibonacci_number(self):
        self.assertTrue(is_fibonacci_number(34))
        self.assertFalse(is_fibonacci_number(4))

        with self.assertRaises(SystemExit) as cm:
            main(["6", "7", "2"])
        self.assertEqual(cm.exception.code, "There is no proper fibonacci number in input")

    def test_non_int(self):
        with self.assertRaises(SystemExit) as cm:
            main(["1.1", "7", "2"])
        self.assertEqual(cm.exception.code, "Some input arguments are not integers. Please put integer numbers")

    def test_negative_number_input(self):
        with self.assertRaises(SystemExit) as cm:
            main(["3", "-4", "12"])
        self.assertEqual(cm.exception.code, "Input arguments must be greater then 0")

    def test_check_fibonacci_order(self):
        with self.assertRaises(SystemExit) as cm:
            main(["3", "1", "12"])
        self.assertEqual(cm.exception.code, "y must be greater then x")
        with self.assertRaises(SystemExit) as cm2:
            main(["1", "3", "15"])
        self.assertEqual(cm2.exception.code, "y must be next fibonacci number after x")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1, 2, 4), [1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
