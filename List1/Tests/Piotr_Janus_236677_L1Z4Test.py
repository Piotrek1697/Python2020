import unittest
from List1.Piotr_Janus_236677_L1Z4 import *


class MyTestCase(unittest.TestCase):

    def test_output_matrix(self):
        numpy.testing.assert_array_equal(multiplication_table(3), numpy.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]]))

    def test_non_int(self):
        with self.assertRaises(SystemExit) as cm:
            main(["3.2"])
        self.assertEqual(cm.exception.code, "Input argument is not integer. Please put integer number")

if __name__ == '__main__':
    unittest.main()
