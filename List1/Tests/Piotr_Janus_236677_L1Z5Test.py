import unittest
from List1.Piotr_Janus_236677_L1Z5 import *


class MyTestCase(unittest.TestCase):

    def test_word_exists_in_file(self):
        with open("test_file1.txt", "r") as f:
            content = f.readlines()

        self.assertTrue(word_exists_in_file(content, "błazenek"))
        self.assertFalse(word_exists_in_file(content, "trawa"))

    def test_vowel_counter(self):
        self.assertEqual(vowel_counter("abecadło"), 4)


if __name__ == '__main__':
    unittest.main()