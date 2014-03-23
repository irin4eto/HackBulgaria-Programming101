import unittest

from solution import count_words

class TestCountWords(unittest.TestCase):
    def test_count_words(self):
        self.assertDictEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(["apple", "banana", "apple", "pie"]))
        self.assertDictEqual({'ruby': 1, 'python': 3}, count_words(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
    unittest.main()
