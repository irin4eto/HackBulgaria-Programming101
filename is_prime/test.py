import unittest

from solution import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))
        self.assertEqual(False, is_prime(8))
        self.assertEqual(True, is_prime(11))
        self.assertEqual(False, is_prime(-10))

if __name__ == '__main__':
    unittest.main()
