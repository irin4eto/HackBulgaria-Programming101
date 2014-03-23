import unittest

from solution import contains_digits

class TestContainsDigits(unittest.TestCase):
    def test_contains_digits(self):
        self.assertEqual(True, contains_digits(402123, [0, 3, 4]))
        self.assertEqual(False, contains_digits(666, [6, 4]))
        self.assertEqual(False, contains_digits(123456789, [1, 2, 3, 0]))
        self.assertEqual(True, contains_digits(456, []))

if __name__ == '__main__':
    unittest.main()
