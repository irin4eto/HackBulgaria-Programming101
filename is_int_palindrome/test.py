import unittest

from solution import is_int_palindrome

class TestIsIntPalindrome(unittest.TestCase):
    def test_is_int_palindrome(self):
        self.assertEqual(True, is_int_palindrome(1))
        self.assertEqual(False, is_int_palindrome(42))
        self.assertEqual(True, is_int_palindrome(100001))
        self.assertEqual(True, is_int_palindrome(999))
        self.assertEqual(False, is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()
