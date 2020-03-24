import unittest
from List1.Piotr_Janus_236677_L1Z6 import *


class MyTestCase(unittest.TestCase):

    def test_getting_words(self):
        with open("test_file2.txt", "r") as f:
            content = f.readlines()
        self.assertEqual(get_words(content, '\n'), ["burak", "cukinia", "kura"])

    def test_getting_separator(self):
        with open("test_file2.txt", "r") as f:
            content = f.readlines()
        self.assertEqual(get_separator(content), '\n')

    def test_same_elements(self):
        list1 = ["pojazd", "drabina", "papuga"]
        list2 = ["papuga", "klawiatura", "myszka", 'pojazd']
        list3 = ["myszka", "pojazd", "papuga", "grzyby"]
        self.assertEqual(get_same_elements_sorted(list1, list2, list3), ["papuga", "pojazd"])


if __name__ == '__main__':
    unittest.main()
