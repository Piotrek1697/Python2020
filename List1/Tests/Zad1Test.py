import unittest
from List1.Zad1 import *


class Zad1Test(unittest.TestCase):

    def test_heron_equation(self):
        self.assertEqual(heron_area(3, 4, 5), 6, "Check on ints")
        self.assertEqual(heron_area(6.78, 5.5, 4.3), 11.804681892791528, "Check on floats")
        self.assertNotEqual(heron_area(3, 4, 5), 6.00001)

    def test_three_input_elements(self):
        with self.assertRaises(SystemExit) as cm:
            main(["1"])
        self.assertEqual(cm.exception.code, "Input must have 3 elements")

    def test_not_number_input(self):
        with self.assertRaises(SystemExit) as cm:
            main(["c,2,1"])
        self.assertEqual(cm.exception.code, "Some input arguments are not numbers. Please put numbers")
        with self.assertRaises(SystemExit) as cm2:
            main(["a", "b", "g"])
        self.assertEqual(cm2.exception.code, "Some input arguments are not numbers. Please put numbers")

    def test_negative_number_input(self):
        with self.assertRaises(SystemExit) as cm:
            main(["3", "4", "-7"])
        self.assertEqual(cm.exception.code, "Input arguments must be greater then 0")


if __name__ == '__main__':
    unittest.main()
