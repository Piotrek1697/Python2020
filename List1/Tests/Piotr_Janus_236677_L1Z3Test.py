import unittest
from List1.Piotr_Janus_236677_L1Z3 import *


class Zad3Test(unittest.TestCase):

    def test_geometric_series(self):
        self.assertEqual(get_math_series(1, 2, 3), [1, 2, 4])


if __name__ == '__main__':
    unittest.main()
